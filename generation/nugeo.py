
import skills.a2 as a2
import traceback



import json
from tqdm import tqdm
import os
from multiprocessing import Pool, cpu_count
import argparse

skill_list = [
    "a2"
]

def generate_data(skill, path, index, long_answer):
    """Function to generate an image and conversation."""
    while True:
        try:
            image, conversation = eval(skill).generate(long_answer)
            break
        except Exception as e:
            # traceback.print_exc()
            continue

    
    refined_conversations = []
    for conv in conversation:
        
        refined_conversations.append(
        {
                "from": "human",
                "value": f"<image>\n{conv[0]}"
            },
        )
        refined_conversations.append(
            {
                "from": "gpt",
                "value": f"{conv[1]}"
            }
        )
    image_path = os.path.join(path, skill, f'{index}.png')
    image.save(image_path, quality=90)
    
    return {
        'image': f'{path}/{skill}/{index}.png',
        'conversations': refined_conversations
    }

def generate_data_wrapper(args):
    """Wrapper for multiprocessing to handle multiple arguments."""
    skill, path, index, long_answer = args
    return generate_data(skill, path, index, long_answer)

def main(num_samples_per_skill, num_processes, skills, path, long_answer):
    results = []

    for skill in tqdm(skills, position=0, desc='Generating data'):
        image_path = os.path.join(path, skill)
        if not os.path.exists(image_path):
            os.makedirs(image_path)
        with Pool(processes=num_processes) as pool:
            args = [(skill, path, index, long_answer) for index in range(num_samples_per_skill)]
            results.extend(
                list(tqdm(
                    pool.imap(generate_data_wrapper, args),
                    total=num_samples_per_skill,
                    position=1,
                    desc=f'{skill}'
                ))
            )

    json_path = os.path.join(path, 'dataset.json')
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate dataset for the conversation model.')
    parser.add_argument('--samples', type=int, default = 100, required=True, help='Number of samples per skill.')
    parser.add_argument('--num_processes', type=int, default=cpu_count(), help='Number of processes to use.')
    parser.add_argument('--skills', nargs='+', choices=skill_list, default=skill_list, help='List of skills to generate data for.')
    parser.add_argument('--path', type=str, required=True, help='Path to save data.')
    parser.add_argument('--long_answer', action='store_true', help='Generate long answer for conversation.')
    args = parser.parse_args()

    main(args.samples, args.num_processes, args.skills, args.path, args.long_answer)