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
    diagram = create_tree()
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)
    tc.draw(ax)
    question_type, conversation = generate_conversation(diagram, long_answer)

    ax.axis('off')
    ax.set_aspect('equal')

    if question_type[-2:] in ['11', '12', '13']:
        ax.set_xlim(-50, 200)
        ax.set_ylim(-50, 200)
        ax.set_aspect('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    return image, conversation

def generate_with_augmentation(long_answer=False, controlnet_pipeline=None):
    diagram = create_tree()

    ### Generate a conversation and check if it is augmentable
    question_type, conversation = generate_conversation(diagram, long_answer)
    max_tries = 100

    while not augment_isavailable(conversation) and max_tries > 0:
        diagram = create_tree()
        question_type, conversation = generate_conversation(diagram, long_answer)
        max_tries -= 1

    fig, ax = plt.subplots()
    tc = TextCollection()

    plot_diagram(ax, tc, diagram, set_visible = True)
    tc.draw(ax, set_visible = False)

    ax.axis('off')
    ax.set_aspect('equal')

    if question_type[-2:] in ['11', '12', '13']:
        ax.set_xlim(-50, 200)
        ax.set_ylim(-50, 200)
        ax.set_aspect('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image1 = Image.open(buf)
    plt.close(fig)

    fig, ax = plt.subplots()
    tc = TextCollection()

    plot_diagram(ax, tc, diagram, set_visible = False)
    tc.draw(ax, set_visible = True)

    ax.axis('off')
    ax.set_aspect('equal')

    if question_type[-2:] in ['11', '12', '13']:
        ax.set_xlim(-50, 200)
        ax.set_ylim(-50, 200)
        ax.set_aspect('equal')


    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight', transparent=True)
    buf.seek(0)
    image2 = Image.open(buf)
    plt.close(fig)


    fig, ax = plt.subplots()
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    ax.imshow(image1, extent=[-30, 30, -30, 30], aspect='auto')
    ax.imshow(image2, extent=[-30, 30, -30, 30], aspect='auto')
    ax.axis('off')
    ax.set_aspect('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight', pad_inches=0.1)
    buf.seek(0)
    final_image = Image.open(buf)
    plt.close(fig)

    return final_image, conversation

def generate_image_caption_pair():
    fig, ax = plt.subplots()
    diagram = create_tree()
    tc = TextCollection()
    plot_diagram(ax, tc, diagram)
    tc.draw(ax)
    question_type, conversation = generate_conversation(diagram)

    ax.axis('off')
    ax.set_aspect('equal')

    if question_type[-2:] in ['11', '12', '13']:
        ax.set_xlim(-50, 200)
        ax.set_ylim(-50, 200)
        ax.set_aspect('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    caption = generate_caption(diagram)

    return image, caption

__all__ = ['generate', 'generate_with_augmentation', 'generate_image_caption_pair']
