from utils import *
from prompts import *

import yaml
import argparse
import copy
from tqdm import tqdm

with open("config.yaml", 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

API_KEY = config['OPENAI_API_KEY']

def create_test_prompt(demo_prompt, question, response):
    demo_prompt = demo_prompt.strip()
    test_prompt = f"Question: {question}\nModel response: {response}\nExtracted Answer: "
    full_prompt = f"{demo_prompt}\n\n{test_prompt}"
    return full_prompt

def get_eval_response(test_prompt):
    return get_evaluation_chat_response(sys_prompt, test_prompt, API_KEY)

def extract_answer(question, response, verbose=False):
    try:
        test_prompt = create_test_prompt(demo_prompt_extract, question, response)
        extraction = get_eval_response(test_prompt)
        # Only extract the content after 'Extracted Answer:'
        if 'Extracted answer:' in extraction:
            return extraction.split('Extracted answer:')[-1].strip()
        # If the model does not provide the answer in an instructed format, return the whole response
        else:
            return extraction.strip()
    except Exception as e:
        printv(e, verbose)
        print(f"Error in extracting answer for '{response}'")
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

    for i, inst in enumerate(tqdm(results)):
        save_inst = copy.deepcopy(inst)
        if 'model_answer' in save_inst:
            response = save_inst['model_answer']
        else:
            response = ''
            printv(save_inst, args.verbose)
            printv("######### NO MODEL ANSWER ###########", args.verbose)  # some model may output nothing due to safety issue

        save_inst['extraction'] = extract_answer(save_inst['question'], response, args.verbose)
        save_results.append(save_inst)

        if (i+1) % args.save_every == 0 or i == len(results) - 1:
            printv(f"Saving results to {args.output}...", args.verbose)
            write_json(args.output, save_results)
            printv(f"Results saved.", args.verbose)
