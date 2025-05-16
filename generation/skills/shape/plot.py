from .rules import *

import matplotlib.pyplot as plt
import yaml

def plot_shape(ax, tc, shape):
    if isinstance(shape, Circle):
        shape_plt = plt.Circle((shape.x, shape.y), shape.r, edgecolor=shape.border_color, facecolor=shape.fill_color)
    else:
        shape_plt = plt.Polygon(shape.points(), edgecolor=shape.border_color, facecolor=shape.fill_color)

    ax.add_artist(shape_plt)

    tc.append(shape.x, shape.y, shape.label, ha='center', va='center', color='black')

def plot_diagram(ax, tc, diagram):
    for shape in diagram.shapes:
        plot_shape(ax, tc, shape)
