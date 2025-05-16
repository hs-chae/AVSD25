from .tree import create_tree
from .plot import plot_diagram
from .conversation import generate_conversation
from .caption import generate_caption

from ..utils import *

import matplotlib.pyplot as plt
import io
from PIL import Image

def generate(long_answer=False):
    fig, ax = plt.subplots()
    ax.set_xlim(-100, 200)
    ax.set_ylim(-100, 200)
    ax.axis('off')
    ax.axis('equal')
    diagram = create_tree()
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)
    tc.draw(ax)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    conversation = generate_conversation(diagram, long_answer)

    return image, conversation

def generate_with_augmentation(long_answer=False, controlnet_pipeline=None):
    x_start = -10
    x_end = 50
    y_start = -10
    y_end = 50

    diagram = create_tree()

    ### Generate a conversation and check if it is augmentable
    conversation = generate_conversation(diagram, long_answer)
    max_tries = 100

    while not augment_isavailable(conversation) and max_tries > 0:
        diagram = create_tree()
        conversation = generate_conversation(diagram, long_answer)
        max_tries -= 1
    ###############################################

    fig, ax = plt.subplots(figsize=(6, 6)) 
    ax.set_xlim(x_start, x_end)
    ax.set_ylim(y_start, y_end)
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')
    tc = TextCollection()

    plot_diagram(ax, tc, diagram)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    base_image = Image.open(buf)
    plt.close(fig)

    if augment_isavailable(conversation) and controlnet_pipeline is not None:
        base_image = apply_controlnet_pipeline(base_image, controlnet_pipeline)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(x_start, x_end)
    ax.set_ylim(y_start, y_end)
    ax.axis('off')
    ax.set_aspect('equal', adjustable='box')

    ax.imshow(base_image, extent=[x_start, x_end, y_start, y_end], aspect='auto')

    tc.draw(ax)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)
    final_image = Image.open(buf)
    plt.close(fig)

    return final_image, conversation

def generate_image_caption_pair():
    fig, ax = plt.subplots()
    ax.set_xlim(-100, 200)
    ax.set_ylim(-100, 200)
    ax.axis('off')
    ax.axis('equal')
    diagram = create_tree()
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)
    tc.draw(ax)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    caption = generate_caption(diagram)

    return image, caption

__all__ = ['generate', 'generate_with_augmentation', 'generate_image_caption_pair']