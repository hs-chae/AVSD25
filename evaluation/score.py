from utils import *
from prompts import *

import yaml
import argparse
import copy
from tqdm import tqdm
from collections import defaultdict


with open("config.yaml", 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

API_KEY = config['OPENAI_API_KEY']

def get_eval_response(test_prompt):
    return get_evaluation_chat_response(sys_prompt, test_prompt, API_KEY)

def verify_judgment(judgment):
    judgment = judgment.strip()
    if judgment == None or judgment not in ['0', '1']:
        return False
    return True

def create_test_prompt(demo_prompt, answer, extraction):
    demo_prompt = demo_prompt.strip()
    test_prompt = f"[Standard Answer] {answer}\n[Model Answer] {extraction}\njudgment: "
    full_prompt = f"{demo_prompt}\n\n{test_prompt}"
    return full_prompt

def match_answer(answer, extraction, verbose=False):
    try:
        test_prompt = create_test_prompt(demo_prompt_score, answer, extraction)
        judgment = get_eval_response(test_prompt)
        return judgment.lower().replace("judgment:", "").strip()
    except Exception as e:
        printv(e, verbose)
        print(f"Error in matching answer:\n[Standard Answer] {answer}\n[Model Answer] {extraction}")
    return ""

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    parser.add_argument('--output', type=str)
    parser.add_argument('--save_every', type=int, default=10, help='save every n problems')
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose mode')
    args = parser.parse_args()

    # Read results
    result_file = args.input
    printv(f"Reading {result_file}...", args.verbose)
    results = read_json(result_file)

    save_results = []

    score_dict = defaultdict(lambda: defaultdict(list))
    score_version_dict = defaultdict(list)

    for i, inst in enumerate(tqdm(results)):
        save_inst = copy.deepcopy(inst)

        judgment = match_answer(save_inst['answer'], save_inst['extraction'], args.verbose)

        max_try = 20

        while max_try > 0:
            max_try -= 1
            if not verify_judgment(judgment):
                print('Wrong judgment format: ', judgment)
                judgment = match_answer(save_inst['answer'], save_inst['extraction'], args.verbose)
            else:
                judgment = int(judgment)
                break

            if max_try == 0:
                judgment = 0
                break

        save_inst['judgment'] = judgment

        save_results.append(save_inst)

        # Print and save judgment statistics
        printv(f"Total: {len(save_results)}, Correct: {len([inst for inst in save_results if inst['judgment']])}", args.verbose)

        if (i+1) % args.save_every == 0 or i == len(results)-1:
            printv(f"Saving results to {args.output}...", args.verbose)
            write_json(args.output, save_results)
            printv(f"Results saved.", args.verbose)

    print(f"Total: {len(save_results)}, Correct: {len([inst for inst in save_results if inst['judgment']])}")
