from .tree import create_tree
from .plot import plot_diagram
from .conversation import generate_conversation
from .caption import generate_caption

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import io
from PIL import Image
import random

def generate(long_answer=False):
    diagram = create_tree()

    # plot_type에 따른 Axes 생성
    if diagram.plot_type == 'polar1':
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
    elif diagram.plot_type == 'polar2':
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
    else:
        fig, ax = plt.subplots()

    # 그림 그리기
    plot_diagram(ax, diagram)

    # 추가 설정
    if diagram.plot_type == 'polar1':
        ax.grid(True)
        ax.set_rmax(11)
    elif diagram.plot_type == 'polar2':
        t = [
            0,
            np.pi/6,
            np.pi/3,
            np.pi/2,
            2*np.pi/3,
            5*np.pi/6,
            np.pi,
            7*np.pi/6,
            4*np.pi/3,
            3*np.pi/2,
            5*np.pi/3,
            11*np.pi/6
        ]
        t_labels = [
            r'0',
            r'$\pi/6$',
            r'$\pi/3$',
            r'$\pi/2$',
            r'$2\pi/3$',
            r'$5\pi/6$',
            r'$\pi$',
            r'$7\pi/6$',
            r'$4\pi/3$',
            r'$3\pi/2$',
            r'$5\pi/3$',
            r'$11\pi/6$'
        ]
        ax.set_xticks(t)
        ax.set_xticklabels(t_labels)
        ax.grid(True)
        ax.set_rmax(11)
    else:
        
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        def skip_zero_label(val, pos):
            if val == 0:
                return ''
            return str(int(val)) 
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(skip_zero_label))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(skip_zero_label))
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.text(0, 0, '0', ha='right', va='top', fontsize=12)
        ax.grid(visible=(random.randint(1, 2) == 1))

    # 이미지로 저장
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    conversation = generate_conversation(diagram, long_answer)
    return image, conversation

def generate_image_caption_pair():
    diagram = create_tree()

    # plot_type에 따른 Axes 생성
    if diagram.plot_type == 'polar1':
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
    elif diagram.plot_type == 'polar2':
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
    else:
        fig, ax = plt.subplots()

    # 그림 그리기
    plot_diagram(ax, diagram)

    # 추가 설정
    if diagram.plot_type == 'polar1':
        ax.grid(True)
        ax.set_rmax(11)
    elif diagram.plot_type == 'polar2':
        t = [
            0,
            np.pi/6,
            np.pi/3,
            np.pi/2,
            2*np.pi/3,
            5*np.pi/6,
            np.pi,
            7*np.pi/6,
            4*np.pi/3,
            3*np.pi/2,
            5*np.pi/3,
            11*np.pi/6
        ]
        t_labels = [
            r'0',
            r'$\pi/6$',
            r'$\pi/3$',
            r'$\pi/2$',
            r'$2\pi/3$',
            r'$5\pi/6$',
            r'$\pi$',
            r'$7\pi/6$',
            r'$4\pi/3$',
            r'$3\pi/2$',
            r'$5\pi/3$',
            r'$11\pi/6$'
        ]
        ax.set_xticks(t)
        ax.set_xticklabels(t_labels)
        ax.grid(True)
        ax.set_rmax(11)
    else:
        
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        def skip_zero_label(val, pos):
            if val == 0:
                return ''
            return str(int(val)) 
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(skip_zero_label))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(skip_zero_label))
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.text(0, 0, '0', ha='right', va='top', fontsize=12)
        ax.grid(visible=(random.randint(1, 2) == 1))

    # 이미지로 저장
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    buf.seek(0)
    image = Image.open(buf)
    plt.close(fig)

    caption = generate_caption(diagram)

    return image, caption

__all__ = ['generate', 'generate_image_caption_pair']

