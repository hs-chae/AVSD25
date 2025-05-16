from skills import skill_list, generate_with_augmentation

import json
from tqdm import tqdm
import os
import argparse
import yaml
import re
from copy import deepcopy
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp

import torch
from diffusers import FluxControlNetModel
from diffusers import FluxControlNetPipeline
from diffusers.utils import logging

logging.disable_progress_bar()
logging.disable_default_handler()
logging.disable_propagation()
logging.get_logger('diffusers').setLevel(logging.ERROR)

from transformers.utils import logging

logging.disable_progress_bar()
logging.disable_default_handler()
logging.disable_propagation()
logging.get_logger('transformers').setLevel(logging.ERROR)

conv_type_list = ['llava', 'internvl']

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

controlnet_list = []

pbar_lock = mp.Lock()

def extract_start_index(skill, dataset):
    max_index = -1

    for data in dataset:
        match = re.match(skill + r'/(\d+).png', data['image'])
        if match:
            index = int(match.group(1))
            max_index = max(max_index, index)
    
    return max_index + 1
    
def generate_data_with_augmentation(skill, path, index, long_answer, conv_type, controlnet_pipeline):
    """Function to generate an image and conversation."""
    while True:
        try:
            image, conversations = generate_with_augmentation(skill, long_answer, controlnet_pipeline)
            break
        except Exception as e:
            print(f'Error: {e}')
            continue
    image_path = os.path.join(path, 'images', skill, f'{index}.png')
    image.save(image_path, quality=90)

    if conv_type == 'llava':
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

def skill_main(num_samples_per_skill, skill, path, answer_type, conv_type, dataset=[]):
    gpu = int(mp.current_process().name.split('-')[-1]) - 1

    controlnet = FluxControlNetModel.from_pretrained(
        config['controlnet_model'],
        torch_dtype=torch.bfloat16,

    )

    pipeline = FluxControlNetPipeline.from_pretrained(
        config['base_model'],
        controlnet=controlnet,
        torch_dtype=torch.bfloat16
    )

    pipeline.to(f'cuda:{gpu}')
    pipeline.set_progress_bar_config(disable=True)

    start_index = extract_start_index(skill, dataset)
    image_path = os.path.join(path, 'images', skill)
    if not os.path.exists(image_path):
        os.makedirs(image_path)

    results = deepcopy(dataset)

    if answer_type == 'mixed':
        long_answer_list = [True] * (num_samples_per_skill // 2) + [False] * (num_samples_per_skill - num_samples_per_skill // 2)
    elif answer_type == 'long':
        long_answer_list = [True] * num_samples_per_skill
    else:
        long_answer_list = [False] * num_samples_per_skill

    for index in tqdm(range(start_index, start_index + num_samples_per_skill), position=gpu+1, desc=f'{skill}'):
        results.append(generate_data_with_augmentation(skill, path, index, long_answer_list[index - start_index], conv_type, pipeline))

    return results

def main(num_samples_per_skill, skills, path, answer_type, conv_type, reset):
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

    gpus = torch.cuda.device_count()        

    futures = []

    with tqdm(total=len(skills), position=0, desc='Generating data') as pbar:
        not_updated_skills = []

        with ProcessPoolExecutor(max_workers=gpus) as executor:
            for skill in skill_list:
                skill_dataset = list(filter(lambda x: x['image'].startswith(skill), results))
                if skill in skills:
                    futures.append(
                        executor.submit(
                            skill_main, num_samples_per_skill, skill, path, answer_type, conv_type, skill_dataset
                        )
                    )
                else:
                    not_updated_skills.extend(skill_dataset)

        results = not_updated_skills
        for future in futures:
            results.extend(future.result())
            pbar.update(1)

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
    parser.add_argument('--skills', nargs='+', choices=skill_list, default=skill_list, help='List of skills to generate data for.')
    parser.add_argument('--path', type=str, required=True, help='Path to save data.')
    parser.add_argument('--answer_type', type=str, choices=['short', 'long', 'mixed'], default='mixed', help='Type of answer for the conversation model.')
    parser.add_argument('--conv_type', type=str, choices=conv_type_list, default='llava', help='Prompt type for the conversation model.')
    parser.add_argument('--reset', action='store_true', help='Reset the dataset.')
    args = parser.parse_args()

    main(args.samples, args.skills, args.path, args.answer_type, args.conv_type, args.reset)
