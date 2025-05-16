from .tree import create_tree
from .plot import plot_diagram, copy_plot_diagram
from .conversation import generate_conversation
from .caption import generate_caption

from ..utils import *

import matplotlib.pyplot as plt
import io
from PIL import Image

def generate(long_answer=False):
    fig, ax = plt.subplots(1, 2)
    tc1 = TextCollection()
    tc2 = TextCollection()
    tc = np.array([tc1, tc2])
    diagram = create_tree()
    plot_diagram(ax, tc, diagram)
    for i in range(2):
        tc[i].draw(ax[i])
    for i in range(2):
        ax[i].axis('off')
        ax[i].set_aspect('equal')
        ax[i].set_xlim(-20, 120)
        ax[i].set_ylim(-20, 120)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    conversation = generate_conversation(diagram, long_answer)

    return image, conversation

def generate_with_augmentation(long_answer=False, controlnet_pipeline=None):
    diagram = create_tree()

    ### Generate a conversation and check if it is augmentable
    conversation = generate_conversation(diagram, long_answer)
    max_tries = 100

    while not augment_isavailable(conversation) and max_tries > 0:
        diagram = create_tree()
        conversation = generate_conversation(diagram, long_answer)
        max_tries -= 1
    ###############################################

    ### image만 있음
    fig, ax = plt.subplots(1, 2)
    tc1 = TextCollection()
    tc2 = TextCollection()
    tc = np.array([tc1, tc2])
    plot_diagram(ax, tc, diagram, set_visible=True)
    for i in range(2):
        tc[i].draw(ax[i], set_visible=False)
    for i in range(2):
        ax[i].axis('off')
        ax[i].set_aspect('equal')
        ax[i].set_xlim(-20, 120)
        ax[i].set_ylim(-20, 120)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    ### text만 있음
    fig, ax = plt.subplots(1, 2)
    tc1 = TextCollection()
    tc2 = TextCollection()
    tc = np.array([tc1, tc2])
    copy_plot_diagram(ax, tc, diagram, set_visible=False)
    for i in range(2):
        tc[i].draw(ax[i], set_visible=True)
    for i in range(2):
        ax[i].axis('off')
        ax[i].set_aspect('equal')
        ax[i].set_xlim(-20, 120)
        ax[i].set_ylim(-20, 120)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight', transparent=True)
    buf.seek(0)
    image2 = Image.open(buf)
    plt.close(fig)

    ### apply controlnet pipeline
    if augment_isavailable(conversation):
        image = apply_controlnet_pipeline(image, controlnet_pipeline)

    fig, ax = plt.subplots()
    ax.set_xlim(-30, 30)
    ax.set_ylim(-30, 30)
    ax.imshow(image, extent=[-30, 30, -30, 30], aspect='auto')
    ax.imshow(image2, extent=[-30, 30, -30, 30], aspect='auto')
    ax.axis('off')
    ax.set_aspect('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    return image, conversation

def generate_image_caption_pair():
    fig, ax = plt.subplots(1, 2)
    tc1 = TextCollection()
    tc2 = TextCollection()
    tc = np.array([tc1, tc2])
    diagram = create_tree()
    plot_diagram(ax, tc, diagram)
    for i in range(2):
        tc[i].draw(ax[i])
    for i in range(2):
        ax[i].axis('off')
        ax[i].set_aspect('equal')
        ax[i].set_xlim(-20, 120)
        ax[i].set_ylim(-20, 120)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=resolution(), bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    caption = generate_caption(diagram)

    return image, caption

__all__ = ['generate', 'generate_with_augmentation', 'generate_image_caption_pair']
