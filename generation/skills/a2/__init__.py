import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .a2_rules import *
from .plot import *
import os
from .labels import *
from ..utils import *
import math

import random
from .rule_list import a2_rules as full_rules

import matplotlib.pyplot as plt
import io
from PIL import Image

with open(os.path.join(os.path.dirname(__file__), 'conversations/conversation.json')) as file:
    long_conversation = json.load(file)
with open(os.path.join(os.path.dirname(__file__), 'conversations/short_conversation.json')) as file:
    short_conversation = json.load(file)
with open(os.path.join(os.path.dirname(__file__), 'conversations/captions.json')) as file:
    captions = json.load(file)
with open(os.path.join(os.path.dirname(__file__), 'conversations/twisted_captions.json')) as file:
    twist_captions = json.load(file)
with open(os.path.join(os.path.dirname(__file__), 'conversations/questions.json')) as file:
    q_data = json.load(file)



def any_pair_within(d):
    """
    Given a list of (x, y) points, return True if
    there exists at least one pair of points whose
    Euclidean distance is less than 100, otherwise False.
    """
    points = d.points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i].x, points[i].y,
            x2, y2 = points[j].x, points[i].y
            distance = math.dist((x1, y1), (x2, y2))
            # Alternatively, you can calculate the distance manually:
            # distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if distance < 50:
                return True
    return False


def max_less_than_10_times_min(d):
    """
    Given a list of (x, y) points, return True if the
    maximum pairwise distance is less than 10 times
    the minimum pairwise distance, otherwise False.
    """
    points = d.points
    if len(points) < 2:
        return False

    min_dist = float('inf')
    max_dist = float('-inf')

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i].x, points[i].y,
            x2, y2 = points[j].x, points[i].y
            distance = math.dist((x1, y1), (x2, y2))  # requires Python 3.8+

            if distance < min_dist:
                min_dist = distance
            if distance > max_dist:
                max_dist = distance

    if min_dist < 50:

        return True
    # print(f"max : {max_dist}, min: {min_dist}")
    return max_dist > 20 * min_dist


def create_diagram(num_entities):
    diagram = Diagram(points=[], lines=[], circles=[], triangles=[], squares=[], steps=[])

    indx = 0

    while True:
        diagram = a2_tree(diagram)
        if len(diagram.entities) >= num_entities or len(diagram.points)>12 or len(diagram.steps) > 6: #or indx > len(diagram.entities)*1.5
            break
        # if len(diagram.entities) > 0:
        #     if 'angle' or 'length' or 'parallel' or '' in diagram.entities[-1][0]:
        #         break
        else:
            indx += 1
        #   
    return diagram


def generate_twist_caption(diagram):
    while True:
        try:
            conv_data = captions
            rand_rule = random.choice(full_rules)

            point_labels = [point.label for point in diagram.points]
            random.shuffle(point_labels)
            while len(point_labels) < 10:
                point_labels.append(random.choice(capitals.candidates))
            
            key = rand_rule

            answer = random.choice(conv_data[key])
            break

        except: pass

    for i in range(len(point_labels)):
        answer = answer.replace(f'<{i + 1}>', f'{point_labels[i]}')

    return answer

def generate_fake_caption(diagram):
    while True:
        try:
            conv_data = twist_captions

            if len(diagram.entities) == 0:
                raise ValueError(
                    f"No entities in the diagram with steps {diagram.steps} and {len(diagram.lines)} lines and  {len(diagram.circles)} circles")
            entity = random.choice(diagram.entities)
            key = entity[0]
            inputs = entity[1]

            answer = random.choice(conv_data[key])
            break
        except: pass
    inputs.append(random.choice(capitals.candidates))

    for i in range(len(inputs)):
        answer = answer.replace(f'<{i + 1}>', f'{inputs[i]}')

    return answer


def generate_one_correct(diagram):
    conv_data = captions

    if len(diagram.entities) == 0:
        raise ValueError(
            f"No entities in the diagram with steps {diagram.steps} and {len(diagram.lines)} lines and  {len(diagram.circles)} circles")
    entity = random.choice(diagram.entities)
    key = entity[0]
    inputs = entity[1]

    answer = random.choice(conv_data[key])
    inputs.append(random.choice(capitals.candidates))

    for i in range(len(inputs)):
        answer = answer.replace(f'<{i + 1}>', f'{inputs[i]}')

    return answer

def generate_full_caption(diagram):
    conv_data = captions

    if len(diagram.entities) == 0:
        raise ValueError(
            f"No entities in the diagram with steps {diagram.steps} and {len(diagram.lines)} lines and  {len(diagram.circles)} circles")

    full_answer = ""
    for entity in diagram.entities:
        key = entity[0]
        inputs = entity[1]

        answer = random.choice(conv_data[key])
        inputs.append(random.choice(capitals.candidates))

        for i in range(len(inputs)):
            answer = answer.replace(f'<{i + 1}>', f'{inputs[i]}')

        full_answer += answer + " "

    return full_answer[:-1]



def task1(d): #Generate full caption.
    question = random.choice(captions["caption"])
    answer = generate_full_caption(d)

    conversation = [(question,answer)]

    return conversation

def task2(d): #Which is the correct description?
    
    q = "Between (i) and (ii), which best describes the image?"

    correct = generate_one_correct(d)
    wrong = generate_twist_caption(d)
    
    if random.choice([True,False]):
        a = "(i)"
        q += f" (i) {correct} (ii) {wrong}"

    else:
        a = "(ii)"
        q += f" (i) {wrong} (ii) {correct}"

    conversation = [(q,a)]
    
    return conversation

def task3(d): #True or False
    
    q = "Answer the following question based on the given image. True or False: According to the image, "

    correct = generate_one_correct(d)
    wrong = generate_twist_caption(d)
    
    if random.choice([True,False]):
        a = "True"
        q += correct

    else:
        a = "False"
        q += wrong

    conversation = [(q,a)]
    
    return conversation

def generate_conversation(diagram, long_answer = False):
    conv_data = captions

    if len(diagram.entities) == 0:
        raise ValueError(f"No entities in the diagram with steps {diagram.steps} and {len(diagram.lines)} lines and  {len(diagram.circles)} circles")
    entity = random.choice(diagram.entities)
    key = entity[0]
    inputs = entity[1]

    fake_entity = random.choice(diagram.entities)
    fake_key = fake_entity[0]
    fake_inputs = fake_entity[1]

    # question, answer = random.choice(conv_data[key])
    answer = random.choice(conv_data[key])
    # fake_answer = random.choice(twist_captions[fake_key])

    inputs.append(random.choice(capitals.candidates))
    # fake_inputs.append(random.choice(capitals.candidates))

    for i in range(len(inputs)):
        answer = answer.replace(f'<{i + 1}>', f'{inputs[i]}')


    question = "Describe this image."

    conversation = [(question,answer)]
    
    return conversation
        
        

def generate(long_answer=False):
    # Generate Diagram
    j = random.randint(1,3)
    while True:
        fig, ax = plt.subplots(figsize=(8, 8))

        # Randomly set axis visibility
        
        plt.axis("off")

        while True:
            diagram = create_diagram(j)
            if not any_pair_within(diagram) and not max_less_than_10_times_min(diagram):
                break

    # Generate Image
        tc = TextCollection()
        

        plot_diagram(ax, tc, diagram)
        if not tc.too_close(20):
            break
        plt.close(fig)
    tc.draw(ax)
   
    # Set aspect ratio while keeping the limits consistent
    ax.set_aspect('equal')
    ax.relim()  # Recompute limits based on content
    ax.autoscale_view()  # Autoscale to fit the recomputed limits

    # Save the figure to a buffer without cutting content
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)
    
    # Load the image from the buffer
    image = Image.open(buf)
    plt.close(fig)
    
    
    #Generate Conversation
    conversation = random.choice([task1, task2, task3])(diagram)
    
    return image, conversation



def generate_with_augmentation(long_answer=False, controlnet_pipeline=None):
    # Generate Diagram
    j = random.randint(1, 3)
    while True:
        diagram = create_diagram(j)
        if not any_pair_within(diagram) and not max_less_than_10_times_min(diagram):
            break

    ### Generate a conversation and check if it is augmentable
    conversation = random.choice([task1,task2,task3])(diagram)
    max_tries = 100

    while not augment_isavailable(conversation) and max_tries > 0:
        diagram = create_diagram(j)
        conversation = generate_conversation(diagram, long_answer)
        max_tries -= 1
    ###############################################

    fig, ax = plt.subplots()
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.axis('off')
    ax.set_aspect('equal')
    tc = TextCollection()

        
    plot_diagram(ax, tc, diagram)

    # print("111111")

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)


    # print("222222")

    ### apply controlnet pipeline
    if augment_isavailable(conversation):
        image = apply_controlnet_pipeline(image, controlnet_pipeline)

    fig, ax = plt.subplots()
    ax.imshow(image, extent=[0,1000, 0,1000], aspect='auto')
    tc.draw(ax)

    # ax.relim()  # Recompute limits based on content
    # ax.autoscale_view()  # Autoscale to fit the recomputed limits
    # print("3333333")

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    return image, conversation

__all__ = ['generate', 'generate_with_augmentation']