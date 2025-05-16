from .rules import *

import matplotlib.pyplot as plt

def plot_arrow(ax, tc, arrow):
    shape_plt = plt.Polygon(arrow.points(), edgecolor=arrow.border_color, facecolor=arrow.fill_color)
    ax.add_artist(shape_plt)
    tc.append(arrow.x, arrow.y, arrow.label, ha='center', va='center', color='black')

def plot_text(ax, tc, text):
    if text.size:
        tc.append(text.x, text.y, text.text, ha='center', va='center', color=text.color, fontsize=text.size)
    else:
        tc.append(text.x, text.y, text.text, ha='center', va='center', color=text.color)

def plot_circle(ax, tc, circle):
    shape_plt = plt.Circle((circle.x, circle.y), circle.r, edgecolor=circle.border_color, facecolor=circle.fill_color)
    ax.add_artist(shape_plt)
    tc.append(circle.x, circle.y, circle.label, ha='center', va='center', color='black')

def plot_diagram(ax, tc, diagram):
    for text in diagram.texts:
        plot_text(ax, tc, text)

    for circle in diagram.circles:
        plot_circle(ax, tc, circle)

    for arrow in diagram.arrows:
        plot_arrow(ax, tc, arrow)