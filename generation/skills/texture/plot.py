from .rules import *
import matplotlib.pyplot as plt

def draw_line_with_n_breaks(ax, x, y, n, color='black'):
    line, = ax.plot(x, y, color=color)
    dash_length = 1 / n
    dash_pattern = [dash_length, dash_length]
    line.set_dashes(dash_pattern)

def plot_line(ax, tc, line):
    points = np.array(line.points())
    if isinstance(line.style, float):
        draw_line_with_n_breaks(ax, points[:, 0], points[:, 1], line.style, color=line.color)
    else:
        ax.plot(points[:, 0], points[:, 1], color=line.color, linestyle=line.style)
    tc.append((points[0, 0] + points[1, 0]) / 2, (points[0, 1] + points[1, 1]) / 2, line.label, color=line.color)

def plot_point(ax, tc, point):
    tc.append(point.x, point.y, point.label, color='black')

def plot_polygon(ax, tc, polygon):
    text_color = 'black'
    tc.append(polygon.x, polygon.y, polygon.label, color=text_color)
    points = polygon.points()
    polygon = plt.Polygon(points, edgecolor=polygon.border_color, facecolor=polygon.fill_color, hatch=polygon.texture, linestyle=polygon.line_style)
    ax.add_artist(polygon)

def plot_circle(ax, tc, circle): 
    text_color = 'black'
    tc.append(circle.x, circle.y, circle.label, color=text_color)
    circle = plt.Circle((circle.x, circle.y), circle.r, edgecolor=circle.border_color, facecolor=circle.fill_color, hatch=circle.texture, linestyle=circle.line_style)
    ax.add_artist(circle)

def plot_star(ax, tc, star):
    text_color = 'black'
    tc.append(star.x, star.y, star.label, color=text_color)
    points = star.points()
    star = plt.Polygon(points, edgecolor=star.border_color, facecolor=star.fill_color, hatch=star.texture, linestyle=star.line_style)
    ax.add_artist(star)

def plot_heart(ax, tc, heart):
    text_color = 'black'
    tc.append(heart.x, heart.y, heart.label, color=text_color)
    points = heart.points()
    heart = plt.Polygon(points, edgecolor=heart.border_color, facecolor=heart.fill_color, hatch=heart.texture, linestyle=heart.line_style)
    ax.add_artist(heart)

def plot_shape(ax, tc, shape):
    if isinstance(shape, Polygon):
        plot_polygon(ax, tc, shape)
    elif isinstance(shape, Circle):
        plot_circle(ax, tc, shape)
    elif isinstance(shape, Star):
        plot_star(ax, tc, shape)
    elif isinstance(shape, Heart):
        plot_heart(ax, tc, shape)


def plot_diagram(ax, tc, diagram):
    for point in diagram.point:
        plot_point(ax, tc, point)
    for line in diagram.line:
        plot_line(ax, tc, line)
    for shape in diagram.shape:
        plot_shape(ax, tc, shape)