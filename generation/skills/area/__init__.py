from .tree import create_tree
from .plot import plot_diagram
from .conversation import generate_conversation

from ..utils import *

import matplotlib.pyplot as plt
import io
from PIL import Image

def generate(long_answer=False, caption_answer=False):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    # ax.axis('off')
    diagram = create_tree()
    tc = TextCollection()

    # plot_diagram(ax, diagram)
    plot_diagram(ax, tc, diagram)

    tc.draw(ax)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    conversation = generate_conversation(diagram, long_answer, caption_answer)

    return image, conversation

def generate_image_caption_pair(long_answer=False):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    # ax.axis('off')
    diagram = create_tree()
    tc = TextCollection()

    # plot_diagram(ax, diagram)
    plot_diagram(ax, tc, diagram)

    tc.draw(ax)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    conversation = generate_conversation(diagram, long=False, caption=True)

    conversation = conversation[0][1]
    # print(conversation)

    return image, conversation

def generate_with_augmentation(long_answer=False, controlnet_pipeline=None, caption_answer=False):
    diagram = create_tree()

    ### Generate a conversation and check if it is augmentable
    conversation = generate_conversation(diagram, long_answer, caption_answer)
    max_tries = 100

    while not augment_isavailable(conversation) and max_tries > 0:
        diagram = create_tree()
        conversation = generate_conversation(diagram, long_answer, caption_answer)
        max_tries -= 1
    ###############################################

    fig, ax = plt.subplots()
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.axis('off')
    ax.set_aspect('equal')
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    ### apply controlnet pipeline
    if augment_isavailable(conversation):
        image = apply_controlnet_pipeline(image, controlnet_pipeline)

    fig, ax = plt.subplots()
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.imshow(image, extent=[0, 1000, 0, 1000], aspect='auto')
    ax.axis('off')
    ax.set_aspect('equal')
    tc.draw(ax)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    return image, conversation

__all__ = ['generate', 'generate_with_augmentation', 'generate_image_caption_pair']