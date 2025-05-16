from .rules import *
import random
import matplotlib.pyplot as plt
import numpy as np
import yaml

def plot_point(ax, tc, point):
    if point.o:
        ax.plot(point.x, point.y, 'o', color='black')

    if point.label:
        tc.append(point.x, point.y, point.label)

def plot_line(ax, tc, line):
    if line.infinite:
        x = np.linspace(0, 1, 100)
        a = (line.p2.y - line.p1.y) / (line.p2.x - line.p1.x)
        b = line.p1.y - a * line.p1.x
        y = a * x + b
        ax.plot(x, y, color=line.color)
    else:
        ax.plot([line.p1.x, line.p2.x], [line.p1.y, line.p2.y], color=line.color)
    if line.label:
        x = (line.p1.x + line.p2.x) / 2
        y = (line.p1.y + line.p2.y) / 2
        tc.append(x, y, line.label)
    if line.symbol:
        symbol_color = line.symbol_color if line.symbol_color else line.color

        x = (line.p1.x + line.p2.x) / 2
        y = (line.p1.y + line.p2.y) / 2

        dl = 0.01
        dx = dl * (line.p2.x - line.p1.x)
        dy = dl * (line.p2.y - line.p1.y)

        if line.symbol == '>':
            ax.arrow(x-dx, y-dy, dx, dy, head_width=0.05, head_length=0.1, fc=symbol_color, ec=line.color)
        elif line.symbol == '>>':
            ax.arrow(x-dx*4, y-dy*4, dx, dy, head_width=0.05, head_length=0.05, fc=symbol_color, ec=symbol_color, overhang=1)
            ax.arrow(x+dx*3, y+dy*3, dx, dy, head_width=0.05, head_length=0.05, fc=symbol_color, ec=symbol_color, overhang=1)
        elif line.symbol == '|':
            center = np.array([x, y])
            perp = np.array([dy, -dx]) * 4
            p1 = center - perp
            p2 = center + perp
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=symbol_color)
        elif line.symbol == '||':
            for p in [(x+dx, y+dy), (x-dx, y-dy)]:
                center = np.array(p)
                perp = np.array([dy, -dx]) * 4
                p1 = center - perp
                p2 = center + perp
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=symbol_color)
        elif line.symbol == '|||':
            for p in [(x, y), (x+dx*2, y+dy*2), (x-dx*2, y-dy*2)]:
                center = np.array(p)
                perp = np.array([dy, -dx]) * 4
                p1 = center - perp
                p2 = center + perp
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=symbol_color)

def plot_circle(ax, tc, circle):
    circ = plt.Circle((circle.center.x, circle.center.y), circle.radius, color=circle.color, fill=False)
    ax.add_artist(circ)
    if circle.label:
        tc.append(circle.center.x, circle.center.y, circle.label, color=circle.color)

def calculate_angle_arc(center, p1, p2, radius=0.1, num_points=100):
    # Vectors from the center to the points
    v1 = np.array([p1[0] - center[0], p1[1] - center[1]])
    v2 = np.array([p2[0] - center[0], p2[1] - center[1]])

    # Calculate angles of the vectors relative to the x-axis
    angle1 = np.arctan2(v1[1], v1[0])
    angle2 = np.arctan2(v2[1], v2[0])

    # Ensure the angles are in correct order for plotting the arc
    if angle1 > angle2:
        angle2 += 2 * np.pi

    # Generate points for the arc
    angle_range = np.linspace(angle1, angle2, num_points)
    arc_x = center[0] + radius * np.cos(angle_range)
    arc_y = center[1] + radius * np.sin(angle_range)

    return arc_x, arc_y

def find_intersection(p1, p2, p3, p4):
    """
    Find the intersection of two lines given by points p1, p2 and p3, p4.

    :param p1: Tuple (x1, y1) for the first point of the first line
    :param p2: Tuple (x2, y2) for the second point of the first line
    :param p3: Tuple (x3, y3) for the first point of the second line
    :param p4: Tuple (x4, y4) for the second point of the second line
    :return: Tuple (x, y) for the intersection point or None if lines are parallel
    """
    # Line 1: A1x + B1y = C1
    A1 = p2[1] - p1[1]
    B1 = p1[0] - p2[0]
    C1 = A1 * p1[0] + B1 * p1[1]

    # Line 2: A2x + B2y = C2
    A2 = p4[1] - p3[1]
    B2 = p3[0] - p4[0]
    C2 = A2 * p3[0] + B2 * p3[1]

    # Determinant
    determinant = A1 * B2 - A2 * B1

    if determinant == 0:
        # Lines are parallel
        return None

    # Intersection point
    x = (C1 * B2 - C2 * B1) / determinant
    y = (A1 * C2 - A2 * C1) / determinant
    return x, y

def plot_angle(ax, tc, angle):
    p11 = angle.l1.p1
    p12 = angle.l1.p2
    p21 = angle.l2.p1
    p22 = angle.l2.p2

    if p11 == p21 or p11 == p22:
        center = p11
        p1 = p12
        p2 = p22 if p11 == p21 else p21
        arc_x, arc_y = calculate_angle_arc((center.x, center.y), (p1.x, p1.y), (p2.x, p2.y))

    elif p12 == p21 or p12 == p22:
        center = p12
        p1 = p11
        p2 = p21 if p12 == p22 else p22
        arc_x, arc_y = calculate_angle_arc((center.x, center.y), (p1.x, p1.y), (p2.x, p2.y))
    else:
        center = find_intersection((p11.x, p11.y), (p12.x, p12.y), (p21.x, p21.y), (p22.x, p22.y))
        if center is None:
            return
        p1 = random.choice([p11, p12])
        p2 = random.choice([p21, p22])
        arc_x, arc_y = calculate_angle_arc(center, (p1.x, p1.y), (p2.x, p2.y))

    if angle.symbol not in ['o', 'O']:
            ax.plot(arc_x, arc_y, color=angle.color)

    if angle.symbol == 'o':
        i = len(arc_x) // 2
        c = np.array([center.x, center.y])
        p = np.array([arc_x[i], arc_y[i]])
        p = c + (p - c) * 0.8
        ax.scatter(p[0], p[1], 50, color=angle.color, fc='none', ec=angle.color)
    elif angle.symbol == 'O':
        i = len(arc_x) // 2
        c = np.array([center.x, center.y])
        p = np.array([arc_x[i], arc_y[i]])
        p = c + (p - c) * 0.8
        ax.plot(p[0], p[1], 'o', color=angle.color)
    elif angle.symbol == '|':
        i = len(arc_x) // 2
        c = np.array([center.x, center.y])
        p = np.array([arc_x[i], arc_y[i]])
        p1 = c + (p - c) * 0.9
        p2 = c + (p - c) * 1.1
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=angle.color)

def normalize(v, factor=1):
    norm = (v[0]**2 + v[1]**2)**0.5
    return v[0]/norm * factor, v[1]/norm * factor


def plot_perpendicular(ax, tc, perpendicular):
    center = perpendicular.l2.p1.x, perpendicular.l2.p1.y
    direction1 = perpendicular.l1.p2.x - perpendicular.l1.p1.x, perpendicular.l1.p2.y - perpendicular.l1.p1.y
    direction2 = perpendicular.l2.p2.x - perpendicular.l2.p1.x, perpendicular.l2.p2.y - perpendicular.l2.p1.y
    direction1 = normalize(direction1, 0.05)
    direction2 = normalize(direction2, 0.05)

    p1 = center[0] + direction1[0], center[1] + direction1[1]
    p2 = center[0] + direction1[0] + direction2[0], center[1] + direction1[1] + direction2[1]
    p3 = center[0] + direction2[0], center[1] + direction2[1]
    ax.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color=perpendicular.color)

def plot_text(ax, tc, text):
    tc.append(text.x, text.y, text.text)

def plot_textbox(ax, tc, textbox):
    tc.append(textbox.x, textbox.y, textbox.text, bbox=dict(facecolor=textbox.fill_color, edgecolor=textbox.border_color))

def plot_check(ax, tc, check):
    if check.correct:
        tc.append(check.x, check.y, '✓', fontsize=20, color='green')
    else:
        tc.append(check.x, check.y, '✗', fontsize=20, color='red')

def plot_OX(ax, tc, ox):
    if ox.correct:
        tc.append(ox.x, ox.y, 'O', fontsize=20, color='green')
    else:
        tc.append(ox.x, ox.y, 'X', fontsize=20, color='red')

def plot_diagram(ax, tc, diagram):
    for point in diagram.points:
        plot_point(ax, tc, point)

    for line in diagram.lines:
        plot_line(ax, tc, line)

    for circle in diagram.circles:
        plot_circle(ax, tc, circle)

    for angle in diagram.angles:
        plot_angle(ax, tc, angle)

    for perpendicular in diagram.perpendiculars:
        plot_perpendicular(ax, tc, perpendicular)

    for text in diagram.text:
        plot_text(ax, tc, text)

    for textbox in diagram.textboxes:
        plot_textbox(ax, tc, textbox)

    for check in diagram.checks:
        plot_check(ax, tc, check)

    for ox in diagram.oxs:
        plot_OX(ax, tc, ox)
