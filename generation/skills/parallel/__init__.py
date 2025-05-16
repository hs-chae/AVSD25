import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from .parallel_rules import *
from .plot import *
import os
from .labels import *
from ..utils import *

import matplotlib.pyplot as plt
import io
from PIL import Image

with open(os.path.join(os.path.dirname(__file__), 'conversations', 'conversation.json')) as file:
    long_conversation = json.load(file)

with open(os.path.join(os.path.dirname(__file__), 'conversations', 'short_conversation.json')) as file:
    short_conversation = json.load(file)

with open(os.path.join(os.path.dirname(__file__), 'conversations', 'caption.json')) as file:
    captions = json.load(file)
    

def create_diagram(num_entities):
    diagram = Diagram(points=[], lines=[], circles=[], triangles=[], squares=[], steps=[])

    indx = 0

    while True:
        diagram = C_parallel_tree(diagram)
        if len(diagram.entities) >= num_entities or len(diagram.points)>12 or len(diagram.steps) > 6: #or indx > len(diagram.entities)*1.5
            break
        if len(diagram.entities) > 0:
            if 'parallel' in diagram.entities[-1][0]:
        #
                break
        else:
            indx += 1
        #   
    return diagram

def generate_conversation(diagram, long_answer = False):
    if long_answer : 
        conv_data = long_conversation
    else: conv_data = short_conversation
        
    if len(diagram.entities) == 0:
        raise ValueError(f"No entities in the diagram with steps {diagram.steps} and {len(diagram.lines)} lines and  {len(diagram.circles)} circles")
    entity = random.choice(diagram.entities)

    key = entity[0]
    question, answer = random.choice(conv_data[key])
    inputs = entity[1]

    try:
        inputs.append(random.choice(capitals.candidates))
        for i in range(len(inputs)):
            
            question = question.replace(f'<{i+1}>', f'{inputs[i]}')
            answer = answer.replace(f'<{i+1}>', f'{inputs[i]}')
        
    except Exception as e:
        print(f"Error in generating conversation: {e}")
        print(0/0)
    
    
    conversation = [(question,answer)]
    
    return conversation
        
        
    # else:
        



def generate(long_answer=False):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Randomly set axis visibility
    if random.choice([True, True, True, False]):
        plt.axis("off")
    else:
        plt.axis("on")

    # Generate Diagram
    j = random.randint(1, 5)
    diagram = create_diagram(j)

    # Generate Image
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)
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
    conversation = generate_conversation(diagram, long_answer)
    return image, conversation



def generate_with_augmentation(long_answer=False, controlnet_pipeline=None):
    # Generate Diagram
    j = random.randint(1, 5)
    diagram = create_diagram(j)

    ### Generate a conversation and check if it is augmentable
    conversation = generate_conversation(diagram, long_answer)
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

def generate_caption(diagram):
    if len(diagram.entities) == 0:
        raise ValueError #(f"No entities in the diagram with steps {diagram.steps} and {len(diagram.lines)} lines and  {len(diagram.circles)} circles")
    entity = random.choice(diagram.entities)

    key = entity[0]
    caption = random.choice(captions[key])
    inputs = entity[1]

    inputs.append(random.choice(capitals.candidates))
    for i in range(len(inputs)):
        caption = caption.replace(f'<{i+1}>', f'{inputs[i]}')    
    
    return caption

def generate_image_caption_pair():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Randomly set axis visibility
    if random.choice([True, False]):
        plt.axis("off")
    else:
        plt.axis("on")

    # Generate Diagram
    j = random.randint(1, 5)
    diagram = create_diagram(j)

    # Generate Image
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)
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
    caption = generate_caption(diagram)
    return image, caption

__all__ = ['generate', 'generate_with_augmentation', 'generate_image_caption_pair']