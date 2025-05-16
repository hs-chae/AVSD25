from .rules import *

import random
from matplotlib import pyplot as plt

def plot_polygon(ax, tc, polygon):
    tc.append(polygon.x, polygon.y, polygon.label)
    polygon = plt.Polygon(polygon.points(), edgecolor=polygon.border_color, facecolor=polygon.fill_color)
    ax.add_artist(polygon)

def plot_circle(ax, tc, circle):
    tc.append(circle.x, circle.y, circle.label)
    circle = plt.Circle((circle.x, circle.y), circle.r, edgecolor=circle.border_color, facecolor=circle.fill_color)
    ax.add_artist(circle)

def plot_star(ax, tc, star):
    tc.append(star.x, star.y, star.label)
    star = plt.Polygon(star.points(), edgecolor=star.border_color, facecolor=star.fill_color)
    ax.add_artist(star)

def plot_heart(ax, tc, heart):
    tc.append(heart.x, heart.y, heart.label)
    heart = plt.Polygon(heart.points(), edgecolor=heart.border_color, facecolor=heart.fill_color)
    ax.add_artist(heart)

def plot_text(ax, tc, text):
    tc.append(text.x, text.y, text.text, fontsize=text.size, color=text.color)

def plot_line(ax, tc, line):
    ax.plot([line.x1, line.x2], [line.y1, line.y2], color=line.color)

def plot_textbox(ax, tc, textbox):
    tc.append(textbox.x, textbox.y, textbox.text, fontsize=textbox.size, color='black', bbox=dict(facecolor=textbox.fill_color, edgecolor=textbox.border_color, boxstyle='round,pad=0.5'))

def plot_point(ax, tc, point):
    ax.plot(point.x, point.y, 'o', color=point.color)
    tc.append(point.x, point.y, point.label)

def plot_arrow(ax, tc, arrow):
    shape_plt = plt.Polygon(arrow.points(), edgecolor=arrow.border_color, facecolor=arrow.fill_color)
    ax.add_artist(shape_plt)

def plot_colorbar(ax, tc, colorbar):
    if colorbar.direction == 'horizontal':
        gradient = np.linspace(0, 1, 300).reshape(1, -1)
    else:
        gradient = np.linspace(0, 1, 300).reshape(-1, 1)

    x, y, w, h = colorbar.x, colorbar.y, colorbar.w, colorbar.h

    extent = [x - w/2, x + w/2, y - h/2, y + h/2]

    ax.imshow(gradient, cmap=colorbar.cmap, aspect='auto', extent=extent)

def plot_diagram(ax, tc, diagram):
    for polygon in diagram.polygon:
        plot_polygon(ax, tc, polygon)

    for circle in diagram.circle:
        plot_circle(ax, tc, circle)

    for star in diagram.star:
        plot_star(ax, tc, star)

    for heart in diagram.heart:
        plot_heart(ax, tc, heart)

    for text in diagram.text:
        plot_text(ax, tc, text)

    for textbox in diagram.textbox:
        plot_textbox(ax, tc, textbox)

    for line in diagram.line:
        plot_line(ax, tc, line)

    for point in diagram.point:
        plot_point(ax, tc, point)

    for arrow in diagram.arrow:
        plot_arrow(ax, tc, arrow)

    for colorbar in diagram.colorbar:
        plot_colorbar(ax, tc, colorbar)