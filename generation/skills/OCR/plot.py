from .rules import *

import matplotlib.pyplot as plt

def plot_letter(ax, tc, letter):
    italic = 'normal'
    weight = 1

    if letter.italic:
        italic = 'italic'
    
    if letter.bold:
        weight = 'extra bold'

    tc.append(letter.coordinate[0], letter.coordinate[1], letter.letter, fontsize=letter.size, color=letter.color, fontweight=weight, fontstyle=italic, fontname=letter.font, rotation=letter.rotate, verticalalignment='center', horizontalalignment='center')
    if letter.highlight:
        ax.add_patch(plt.Rectangle(letter.coordinate, 1, 1, fill=True, color=letter.highlight.color))
    if letter.underline:
        ax.add_patch(plt.Rectangle(letter.coordinate, 1, 1, fill=False, color=letter.underline.color))


def plot_word(ax, tc, word):
    italic = 'normal'
    weight = 1

    if word.italic:
        italic = 'italic'
    
    if word.bold:
        weight = 'extra bold'

    tc.append(word.coordinate[0], word.coordinate[1], word.word, fontsize=word.size, color=word.color, fontweight=weight, fontstyle=italic, fontname=word.font, rotation=word.rotate, verticalalignment='center', horizontalalignment='center')
    if word.highlight:
        ax.add_patch(plt.Rectangle(word.coordinate, 1, 1, fill=True, color=word.highlight.color))
    if word.underline:
        ax.add_patch(plt.Rectangle(word.coordinate, 1, 1, fill=False, color=word.underline.color))


def plot_circle(ax, tc, circle):
    ax.add_patch(plt.Circle(circle.center, circle.radius, fill=False, color=circle.color))

def plot_text(ax, tc, text):
    if text.align == 'left':
        tc.append(-0.2, 0.5, text.text, horizontalalignment='left', verticalalignment='center', wrap=True, fontname=text.font, rotation=text.rotate)
    elif text.align == 'right':
        tc.append(1.2, 0.5, text.text, horizontalalignment='right', verticalalignment='center', wrap=True, fontname=text.font, rotation=text.rotate)
    else:
        tc.append(0.5, 0.5, text.text, horizontalalignment='center', verticalalignment='center', wrap=True, fontname=text.font, rotation=text.rotate)

def plot_diagram(ax, tc, diagram):
    for letter in diagram.letter:
        plot_letter(ax, tc, letter)
    
    for word in diagram.word:
        plot_word(ax, tc, word)

    for text in diagram.text:
        plot_text(ax, tc, text)

    for circle in diagram.circle:
        plot_circle(ax, tc, circle)
