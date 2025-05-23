import json
import os
import yaml

from pathlib import Path
from tqdm import tqdm
from openai import OpenAI

from loguru import logger as eval_logger

from lmms_eval.tasks._task_utils.file_utils import generate_submission_file

def nugeo_aggregate_accuracy(results, args, *, calculate_gain=False, random_scores=None):
    path = generate_submission_file(f"nugeo_results.json", args)

    with open(path, 'w') as f:
        json.dump(results, f, indent=4)

    updated_results = []

    for result in tqdm(results, desc='Extracting'):
        updated_results.append({
            **result,
            'extraction': extract_answer(result['question'], result['prediction'], config['metadata']['gpt_model'])
        })

    for i, result in enumerate(tqdm(updated_results, desc='Scoring')):
        updated_results[i]['judgment'] = score_answer(result['answer'], result['extraction'], config['metadata']['gpt_model'])

with open(Path(__file__).parent / 'avs.yaml', 'r') as f:
    raw_data = f.readlines()
    safe_data = []
    for i, line in enumerate(raw_data):
        # remove function definition since yaml load cannot handle it
        if "!function" not in line:
            safe_data.append(line)

    config = yaml.safe_load("".join(safe_data))

API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY")

def avs_doc_to_visual(doc):
    if str(doc["image"]).strip() == "":
        return []
    return [doc["image"].convert("RGB")]

def avs_doc_to_text(doc, lmms_eval_specific_kwargs=None):
    if lmms_eval_specific_kwargs['prompt'] == 'cot':
        return doc["question"] + ' Let\'s think step by step.'
    else:
        return doc["question"]
    
def avs_process_results(doc, results):
    prediction = results[0].strip()
    result = {**doc, 'prediction': prediction}
    return {'accuracy': result}

def avsbench_aggregate_accuracy(results, args, *, calculate_gain=False, random_scores=None):
    difficulties = [result['difficulty'] for result in results]

    if len(set(difficulties)) > 1:
        path = generate_submission_file(f"avsbench_results.json", args)
    else:
        split_flag = results[0]['difficulty']
        path = generate_submission_file(f"avsbench_{split_flag}_results.json", args)

    with open(path, 'w') as f:
        json.dump(results, f, indent=4)

    updated_results = []

    for result in tqdm(results, desc='Extracting'):
        updated_results.append({
            **result,
            'extraction': extract_answer(result['question'], result['prediction'], config['metadata']['gpt_model'])
        })

    for i, result in enumerate(tqdm(updated_results, desc='Scoring')):
        updated_results[i]['judgment'] = score_answer(result['answer'], result['extraction'], config['metadata']['gpt_model'])

    with open(path, 'w') as f:
        json.dump(updated_results, f, indent=4)

    eval_logger.info(f"Saved results to {path}")

    accuracy = sum([result['judgment'] for result in updated_results]) / len(updated_results)

    return accuracy

def vitas_aggregate_accuracy(results, args, *, calculate_gain=False, random_scores=None):
    path = generate_submission_file(f"vitas_results.json", args)

    with open(path, 'w') as f:
        json.dump(results, f, indent=4)

    updated_results = []

    for result in tqdm(results, desc='Extracting'):
        updated_results.append({
            **result,
            'extraction': extract_answer(result['question'], result['prediction'], config['metadata']['gpt_model'])
        })

    for i, result in enumerate(tqdm(updated_results, desc='Scoring')):
        updated_results[i]['judgment'] = score_answer(result['answer'], result['extraction'], config['metadata']['gpt_model'])

    with open(path, 'w') as f:
        json.dump(updated_results, f, indent=4)

    eval_logger.info(f"Saved results to {path}")

    accuracy = sum([result['judgment'] for result in updated_results]) / len(updated_results)

    return accuracy  

sys_prompt = """
Imagine you are an intelligent teacher.
Thoroughly read the provided instruction to ensure a solid understanding of the information provided.
"""

demo_prompt_extract = """
Please read the following example. Then extract the answer from the model response and type it at the end of the prompt.
If the question requires a full sentence with a correct word filled in, please provide the word only.

Question: There is a single rectangle with multiple color layers in the image. What is the color of the boundary of the rectangle? The answer should be one of ‘red’, ‘yellow’, ‘green’, or ‘blue’.
Model response: The color of the boundary of the circle is red.
Extracted answer: red

Question: How many line segments are in the image? Answer should be a number.
Model response: There are 4 dashed line segments in the image.
Extracted answer: 4

Question: Choose the word in parentheses that correctly describes the image. Rewrite the sentence with the chosen word.
In the image, shape (A/B) has sides curved inward.
Model response: In the image, shape B has sides curved inward.
Extracted answer: B

Question: Choose the phrase in parentheses that correctly describes the image. Rewrite the sentence with the chosen phrase.
In the given image, the green arrow (is longer than/has the same length as/is shorter than) the black arrow.
Model response: In the given image, the green arrow is longer than the black arrow.
Extracted answer: is longer than

Question: In this image, choose the path which is a single line segment between points A and B from the following options. Provide your answer as a single uppercase letter: (A) the purple path (B) the blue path (C) the green path (D) the red path
Model response: B
Extracted answer: B

Question: Choose the most appropriate color to fill in the box marked with ‘?’ in the image. The answer is one of ‘a’, ‘b’, ‘c’, or ‘d’.
Model response: The correct color to fill in the box marked with '?' is (a) blue.\n\nThe colors are following a gradient pattern from red, to a more purple hue, and finally to blue. The logical next color in the sequence would be blue, as it extends the progression seen in the previous squares.
Extracted answer: a

Question: There is a book in the image. What is the color of the book in the image? Choose answer from the number of the option and give your answer in “1”, “2”, “3”, or “4”. (1) red  (2) yellow (3) blue (4) green
Model response: The color of the guitar in the image is (2) yellow.
Extracted answer: 2
"""

demo_prompt_score = """
The [Standard Answer] is the correct answer to the question, and the [Model Answer] is the answer generated by a model for that question.
Thoroughly read both the [Standard Answer] and the [Model Answer]. Assess the consistency of the information provided in these two responses.
Although you do not know the specific question, you can still assess the consistency between the two responses by checking for logical conflicts if both responses are assumed to be correct.
If the [Model Answer] is consistent with the [Standard Answer], please answer '1'. Otherwise, answer '0'.
When the [Standard Answer] is provided as a list, answer '1' if the [Model Answer] is consistent with at least one item on the list. Otherwise, answer '0'.
Below are the examples of the correct consistency judgment.

Don't explain anything. Just answer in 0 or 1.

**
Rememeber the format should be
Judgment: 0
or
Judgment: 1
**

You must keep the format!!!

[Standard Answer] a
[Model Answer] a
Judgment: 1

[Standard Answer] 1
[Model Answer] 4
Judgment: 0

[Standard Answer] circle
[Model Answer] the circle
Judgment: 1

[Standard Answer] 4
[Model Answer] shape 4
Judgment: 1

[Standard Answer] line segment B and C
[Model Answer] B, C
Judgment: 1

[Standard Answer] ac
[Model Answer] ca
Judgment: 0

[Standard Answer] 2
[Model Answer] two
Judgment: 1

[Standard Answer] three
[Model Answer] 3
Judgment: 1

[Standard Answer] ['ac', 'ca']
[Model Answer] ca
Judgment: 1

"""

def get_evaluation_chat_response(sys_prompt, user_prompt, api_key, model='gpt-4o-mini'):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )   
    return response.choices[0].message.content

def get_eval_response(test_prompt, model='gpt-4o-mini'):
    return get_evaluation_chat_response(sys_prompt, test_prompt, API_KEY, model)

def create_extract_prompt(demo_prompt, question, response):
    demo_prompt = demo_prompt.strip()
    test_prompt = f"Question: {question}\nModel response: {response}\nExtracted Answer: "
    full_prompt = f"{demo_prompt}\n\n{test_prompt}"
    return full_prompt

def extract_answer(question, response, model='gpt-4o-mini'):
    try:
        test_prompt = create_extract_prompt(demo_prompt_extract, question, response)
        extraction = get_eval_response(test_prompt, model)
        # Only extract the content after 'Extracted Answer:'
        if 'Extracted answer:' in extraction:
            return extraction.split('Extracted answer:')[-1].strip()
        # If the model does not provide the answer in an instructed format, return the whole response
        else:
            return extraction.strip()
    except Exception as e:
        eval_logger.warning(f"Error in extracting answer for '{response}'")
    return ""

def verify_judgment(judgment):
    judgment = judgment.strip()
    if judgment == None or judgment not in ['0', '1']:
        return False
    return True

def create_score_prompt(demo_prompt, answer, extraction):
    demo_prompt = demo_prompt.strip()
    test_prompt = f"[Standard Answer] {answer}\n[Model Answer] {extraction}\njudgment: "
    full_prompt = f"{demo_prompt}\n\n{test_prompt}"
    return full_prompt

def match_answer(answer, extraction, model='gpt-4o-mini'):
    try:
        test_prompt = create_score_prompt(demo_prompt_score, answer, extraction)
        judgment = get_eval_response(test_prompt, model)
        return judgment.lower().replace("judgment:", "").strip()
    except Exception as e:
        eval_logger.warning(f"Error in matching answer:\n[Standard Answer] {answer}\n[Model Answer] {extraction}")
    return ""

def score_answer(answer, extraction, model='gpt-4o-mini'):
    judgment = match_answer(answer, extraction, model)

    max_try = 20
    while True:
        max_try -= 1
        if not verify_judgment(judgment):
            eval_logger.warning('Wrong judgment format: ', judgment)
            judgment = match_answer(answer, extraction, model)
        else:
            judgment = int(judgment)
            break

        if max_try == 0:
            judgment = 0
            break

    return judgment