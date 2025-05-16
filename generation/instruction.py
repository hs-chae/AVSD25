from skills import skill_list, generate, generate_with_augmentation

import json
from tqdm import tqdm
import os
from multiprocessing import Pool, cpu_count
import argparse
import yaml
import re
import random

conv_type_list = ['llava', 'internvl']

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

def extract_start_index(skill, dataset):
    max_index = -1

    for data in dataset:
        match = re.match(skill + r'/(\d+).png', data['image'])
        if match:
            index = int(match.group(1))
            max_index = max(max_index, index)
    
    return max_index + 1

def generate_data(skill, path, index, long_answer, conv_type):
    """Function to generate an image and conversation."""
    while True:
        try:
            image, conversations = generate(skill, long_answer)
            break
        except Exception as e:
            # print(f'Error: {e}')
            continue
    image_path = os.path.join(path, 'images', skill, f'{index}.png')
    image.save(image_path, quality=90)

    if conv_type == 'llava' or conv_type == 'internvl':
        def human(value):
            return {
                'from': 'human',
                'value': f'<image>\n{value}'
            }
        def gpt(value):
            return {
                'from': 'gpt',
                'value': value
            }
        return {
            'image': f'{skill}/{index}.png',
            'conversations': [
                formatting(conversation[i])
                for conversation in conversations
                for i, formatting in enumerate([human, gpt])
            ]
        }
    else:
        return {
            'image': f'{skill}/{index}.png',
            'conversations': conversations
        }

def generate_data_wrapper(args):
    """Wrapper for multiprocessing to handle multiple arguments."""
    skill, path, index, long_answer, conv_type = args
    return generate_data(skill, path, index, long_answer, conv_type)

def main(num_samples_per_skill, num_processes, skills, path, answer_type, conv_type, reset):
    results = []

    if conv_type == 'llava':
        if not reset and os.path.exists(os.path.join(path, 'dataset.json')):
            with open(os.path.join(path, 'dataset.json'), 'r') as f:
                results = json.load(f)
    elif conv_type == 'internvl':
        if not reset and os.path.exists(os.path.join(path, 'dataset.jsonl')):
            with open(os.path.join(path, 'dataset.jsonl'), 'r') as f:
                for line in f:
                    results.append(json.loads(line))

    for skill in tqdm(skills, position=0, desc='Generating data'):
        image_path = os.path.join(path, 'images', skill)
        
        start_index = extract_start_index(skill, results)

        if not os.path.exists(image_path):
            os.makedirs(image_path)
        with Pool(processes=num_processes) as pool:
            if answer_type == 'mixed':
                long_answer_list = [True] * (num_samples_per_skill // 2) + [False] * (num_samples_per_skill - num_samples_per_skill // 2)
                random.shuffle(long_answer_list)
            elif answer_type == 'long':
                long_answer_list = [True] * num_samples_per_skill
            else:
                long_answer_list = [False] * num_samples_per_skill
            
            args = [
                (skill, path, index, long_answer, conv_type) 
                for index, long_answer in zip(range(start_index, start_index + num_samples_per_skill), long_answer_list)
            ]
            
            results.extend(
                list(tqdm(
                    pool.imap(generate_data_wrapper, args),
                    total=num_samples_per_skill,
                    position=1,
                    desc=f'{skill}'
                ))
            )

    if conv_type == 'llava':
        json_path = os.path.join(path, 'dataset.json')
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)
    elif conv_type == 'internvl':
        jsonl_path = os.path.join(path, 'dataset.jsonl')
        with open(jsonl_path, 'w') as f:
            for result in results:
                f.write(json.dumps(result, ensure_ascii=False))
                f.write('\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate dataset for the conversation model.')
    parser.add_argument('--samples', type=int, required=True, help='Number of samples per skill.')
    parser.add_argument('--num_processes', type=int, default=cpu_count(), help='Number of processes to use.')
    parser.add_argument('--skills', nargs='+', choices=skill_list, default=skill_list, help='List of skills to generate data for.')
    parser.add_argument('--path', type=str, required=True, help='Path to save data.')
    parser.add_argument('--answer_type', type=str, choices=['mixed', 'long', 'short'], default='mixed', help='Type of answer for the conversation model.')
    parser.add_argument('--conv_type', type=str, choices=conv_type_list, default='llava', help='Prompt type for the conversation model.')
    parser.add_argument('--reset', action='store_true', help='Reset the dataset.')
    args = parser.parse_args()

    main(args.samples, args.num_processes, args.skills, args.path, args.answer_type, args.conv_type, args.reset)
