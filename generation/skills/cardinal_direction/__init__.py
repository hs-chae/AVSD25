from .tree import create_tree
from .plot import plot_diagram
from .conversation import generate_conversation
from .caption import generate_caption
from .rules import Diagram

from ..utils import *


import matplotlib.pyplot as plt
import io
from PIL import Image
import random

def create_diagram(num_entities):
    diagram = Diagram()
    while True:
        diagram = create_tree(diagram)
        if len(diagram.entities) >= num_entities or len(diagram.points)>12 or len(diagram.steps) > 6: #or indx > len(diagram.entities)*1.5
            break
    return diagram

def generate(long_answer=False):
    fig, ax = plt.subplots(figsize=(8, 8))

    plt.axis('off')

    # Generate Diagram
    j = random.randint(1, 4)
    diagram = create_diagram(j)

    # Generate Image
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)
    tc.draw(ax)

    # Set aspect ratio while keeping the limits consistent
    ax.set_aspect('equal')
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)

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
    diagram = create_diagram(1)

    ### Generate a conversation and check if it is augmentable
    conversation = generate_conversation(diagram, long_answer)
    max_tries = 500

    while not augment_isavailable(conversation) and max_tries > 0:
        diagram = create_tree()
        conversation = generate_conversation(diagram, long_answer)
        max_tries -= 1
    ###############################################

    fig, ax = plt.subplots(figsize=(8, 8))

    plt.axis('off')

    # Generate Image
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)

    # Set aspect ratio while keeping the limits consistent
    ax.set_aspect('equal')
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)

    # Save the figure to a buffer without cutting content
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)

    # Load the image from the buffer
    image = Image.open(buf)
    plt.close(fig)

    ### apply controlnet pipeline
    if augment_isavailable(conversation):
        image = apply_controlnet_pipeline(image, controlnet_pipeline)

    # Set aspect ratio while keeping the limits consistent
    ax.set_aspect('equal')
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    tc.draw(ax)

    # Save the figure to a buffer without cutting content
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)

    # Load the image from the buffer
    image = Image.open(buf)
    plt.close(fig)

    return image, conversation

def generate_image_caption_pair():
    fig, ax = plt.subplots(figsize=(8, 8))

    plt.axis('off')

    # Generate Diagram
    j = random.randint(1, 4)
    diagram = create_diagram(j)

    # Generate Image
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)
    tc.draw(ax)

    # Set aspect ratio while keeping the limits consistent
    ax.set_aspect('equal')
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)

    # Save the figure to a buffer without cutting content
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)

    # Load the image from the buffer
    image = Image.open(buf)
    plt.close(fig)

    #Generate Conversation
    conversation = generate_caption(diagram)
    return image, conversation

__all__ = ['generate', 'generate_with_augmentation', 'generate_image_caption_pair']

