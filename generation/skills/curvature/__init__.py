from .tree import create_tree
from .conversation import generate_conversation
from .caption import generate_caption

from ..utils import *

import matplotlib.pyplot as plt
import io
from PIL import Image

def generate(long_answer=False):
    fig, ax = plt.subplots()
    tc = TextCollection()
    diagram = create_tree(ax, tc)
    tc.draw(ax)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    conversation = generate_conversation(diagram, long_answer)

    return image, conversation

def generate_with_augmentation(long_answer=False, controlnet_pipeline=None):
    fig, ax = plt.subplots()
    tc = TextCollection()
    diagram = create_tree(ax, tc)

    ### Generate a conversation and check if it is augmentable
    conversation = generate_conversation(diagram, long_answer)
    max_tries = 100

    while not augment_isavailable(conversation) and max_tries > 0:
        plt.close(fig)
        fig, ax = plt.subplots()
        tc = TextCollection()
        diagram = create_tree(ax, tc)
        conversation = generate_conversation(diagram, long_answer)
        max_tries -= 1
    ###############################################

    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)


    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    ### apply controlnet pipeline
    if augment_isavailable(conversation):
        image = apply_controlnet_pipeline(image, controlnet_pipeline)

    fig, ax = plt.subplots()
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    ax.imshow(image, extent=[-30, 30, -30, 30], aspect='auto')
    ax.axis('off')
    ax.set_aspect('equal')
    tc.draw(ax)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    return image, conversation

def generate_image_caption_pair():
    fig, ax = plt.subplots()
    tc = TextCollection()
    diagram = create_tree(ax, tc)
    tc.draw(ax)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    caption = generate_caption(diagram)

    return image, caption

__all__ = ['generate', 'generate_with_augmentation', 'generate_image_caption_pair']
