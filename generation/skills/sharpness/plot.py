import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
from .labels import *
import random
import json
from .create_tree import *
import math
import matplotlib.patches as patches
from matplotlib.colors import is_color_like

plt.axis("off")


fixed_color = 'black'
fix_color= False

def plot_point(ax, tc, label = '', coord = (random.randint(0, 1000),random.randint(0, 1000)), color = 'black', fixing_color = True):


    # Coordinates for the free point X
    x_coord, y_coord = coord

    # Possible vertical alignments and colors
    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)

    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Basic color abbreviations
    # random_color = random.choice(colors)

    # Plotting point X with a random color
    ax.plot(x_coord, y_coord, marker='o', color=color, markersize=1)  # 'o' stands for circle marker

    # Adding a label "X" next to the point with random vertical alignment and color
    tc.append(x_coord + 20, y_coord, label, verticalalignment=random_vertical_alignment, color='black')

def plot_line(ax, tc, label, point1 : Point, point2 : Point, color = 'black', infinite = False, tickmarks = 0, dotted = False, fixing_color = True):


    # Coordinates for the free point X
    x1, y1 = point1.coord
    x2, y2 = point2.coord

    # Possible vertical alignments and colors
    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)

    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Basic color abbreviations
    # random_color = random.choice(colors)

    if not infinite:
        # Plotting the line between the two points with a random color
        if dotted:
            ax.plot([x1, x2], [y1, y2], color=color, linestyle='dashed')
        else : ax.plot([x1, x2], [y1, y2], color=color)  # 'o' stands for circle marker
        tc.append((x1 + x2)/2 + 20, (y1 + y2)/2, label, verticalalignment=random_vertical_alignment, color='black')
    else:
        direction = np.array([x2 - x1, y2 - y1])
        norm_direction = direction / np.linalg.norm(direction)

        # Extend the line by a large factor (e.g., 10000) beyond the plot limits
        factor = 10000
        new_x1, new_y1 = np.array([x1, y1]) - factor * norm_direction
        new_x2, new_y2 = np.array([x2, y2]) + factor * norm_direction

        ax.plot([new_x1, new_x2], [new_y1, new_y2], color=color)  # Dashed line for visual distinction
        tc.append((x1 + x2) / 2, (y1 + y2) / 2, label, verticalalignment=random_vertical_alignment,
                color='black')

    if tickmarks > 0:
        # Draw tick marks
        tick_length = 10  # Length of the tick marks
        for i in range(tickmarks):
            offset = 10 * (i - tickmarks / 2 + 0.5)  # Offset each tick mark for visibility

            midpoint_x = (x1 + x2) / 2
            midpoint_y = (y1 + y2) / 2
            unit_vec = np.array([x2 - x1, y2 - y1]) / np.linalg.norm(np.array([x2 - x1, y2 - y1]))
            perp_unit_vector = np.array([y2 - y1, x1 - x2]) / np.linalg.norm(np.array([y2 - y1, x1 - x2]))

            tick_start_x = midpoint_x + offset * unit_vec[0] - tick_length * perp_unit_vector[0]
            tick_start_y = midpoint_y + offset * unit_vec[1] - tick_length * perp_unit_vector[1]
            tick_end_x = tick_start_x + 2* tick_length * perp_unit_vector[0]
            tick_end_y = tick_start_y + 2* tick_length * perp_unit_vector[1]
            ax.plot([tick_start_x, tick_end_x], [tick_start_y, tick_end_y], 'k-')  # 'k-' for black line


def plot_circle(ax, tc, label, center, radius, color = 'black'):

    # Coordinates for the free point X
    x, y = center.coord


    # Possible vertical alignments and colors
    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)

    # colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Basic color abbreviations
    # random_color = random.choice(colors)

    # Plotting point X with a random color
    circle = plt.Circle((x, y), radius, color=color, fill=False)  # 'o' stands for circle marker
    ax.add_artist(circle)

    # Adding a label "X" next to the point with random vertical alignment and color
    tc.append(x + 20, y, label, verticalalignment=random_vertical_alignment, color='black')

def plot_triangle(ax, tc, point1, point2, point3, diagram=Diagram(), mark_points = False, color = random.choice(diverse_colors.candidates)):
    if fix_color:
        color = fixed_color
    # Coordinates for the points
    x1, y1 = point1.coord
    x2, y2 = point2.coord
    x3, y3 = point3.coord

    # Define lines of the triangle
    lines = [(point1,point2), (point2, point3), (point3, point1)]
    #check if the lines are already in the diagram
    for line in lines:
        if line not in diagram.lines and (line[1],line[0]) not in diagram.lines:
            plot_line(ax, tc, label='', point1=line[0], point2=line[1], color=color)

    if mark_points:
        plot_point(ax, tc, label=point1.label, coord=point1.coord)
        plot_point(ax, tc, label=point2.label, coord=point2.coord)
        plot_point(ax, tc, label=point3.label, coord=point3.coord)


def plot_perpendicularity(ax, tc, line1, line2, intersection):
    if fix_color:
        color = fixed_color
    # Coordinates for the points
    x1, y1 = line1.point1.x, line1.point1.y
    x2, y2 = line1.point2.x, line1.point2.y
    x3, y3 = line2.point1.x, line2.point1.y
    x4, y4 = line2.point2.x, line2.point2.y
    x5, y5 = intersection.x, intersection.y

    ind = 0
    while True:
        # Choosing a random point from line1:

        x_rand, y_rand = random.choice([(x1, y1), (x2, y2)])
        if not (-1 < x_rand - x5 < 1 and  -1 < y_rand - y5 < 1):
            break
        elif ind > 5 :
            print(f"x1,y1 : {x1, y1}")
            print(f"x2,y2 : {x2, y2}")
            print(f"x_rand,y_rand : {x_rand, y_rand}")
            raise ValueError("Random point is too close to the intersection point")
        ind += 1


    ind = 0
    while True:
        # Choosing a random point from line2:
        x_rand2, y_rand2 = random.choice([(x3, y3), (x4, y4)])
        if not ( -1 < x_rand2 - x5 < 1 and -1 < y_rand2 - y5 < 1):
            break
        elif ind > 5 :
            print(f"x3,y3 : {x3, y3}")
            print(f"x4,y4 : {x4, y4}")
            print(f"x_rand2,y_rand2 : {x_rand2, y_rand2}")
            raise ValueError("Random point is too close to the intersection point")
        ind += 1

    direction1 = np.array([x_rand - x5, y_rand - y5])
    direction2 = np.array([x_rand2 - x5, y_rand2 - y5])
    length1 = np.linalg.norm(direction1)
    length2 = np.linalg.norm(direction2)
    length = (length1 + length2)/20

    norm_direction1 = direction1 * length / length1
    norm_direction2 = direction2 * length / length2

    #draw the square mark
    ax.plot([x5+ norm_direction2[0], x5 + norm_direction1[0] +  norm_direction2[0]], [y5+ norm_direction2[1], y5+ norm_direction1[1]+ norm_direction2[1] ], color='black')
    ax.plot([x5 + norm_direction1[0] , x5+ norm_direction2[0] + norm_direction1[0] ], [y5+ norm_direction1[1], y5+ norm_direction1[1] + norm_direction2[1]], color='black')

def plot_curve(ax, tc,x,y, t_start=0,t_end=1000 ,color = 'black', label  =''):

    parameter= np.linspace(t_start, t_end, t_end-t_start)
    ax.plot(x, y, color=color)

    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)
    # t = random.choice(range(x[0], x[-1]))
    # tc.append(x[t] + 20, y[t], label, verticalalignment=random_vertical_alignment, color='black')


def plot_arc(ax, tc, line1, angle, color='black', label=''):

    """
    Plots an arc of angle t (in radians) around point A,
    starting at point B and rotating counterclockwise.
    """

    # Unpack points A and B
    ax, tc, Ay = line1.point1.coord
    Bx, By = line1.point2.coord

    # Radius (distance from A to B)
    r = np.sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)

    # Initial angle from A to B
    theta_start = np.arctan2(By - Ay, Bx - Ax)

    # Parameter for angles from theta_start to theta_start + t
    theta_vals = np.linspace(theta_start, theta_start + t, 100)

    # Parametric equations for the arc
    x_arc = Ax + r * np.cos(theta_vals)
    y_arc = Ay + r * np.sin(theta_vals)

    # Plot arc
    plt.plot(x_arc, y_arc, 'b-')

    # Plot center A and starting point B for reference
    plt.scatter([Ax], [Ay], color='red', label='Center A')
    plt.scatter([Bx], [By], color='green', label='Start B')

    # Plot end point of the arc
    B_endx = Ax + r * np.cos(theta_start + t)
    B_endy = Ay + r * np.sin(theta_start + t)
    plt.scatter([B_endx], [B_endy], color='orange', label='End of arc')

    # Setting aspect equal for better visualization
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title(f"Arc around A from B through angle t = {t:.2f} rad")
    plt.xlabel("x")
    plt.ylabel("y")
plt.grid(True)



def plot_angle(ax, tc, line1, line2, intersection, color='black', label = ''):
    if fix_color:
        color = fixed_color
        # Coordinates for the points
    x1, y1 = line1.point1.coord
    x2, y2 = line1.point2.coord
    x3, y3 = line2.point1.coord
    x4, y4 = line2.point2.coord
    x_inter, y_inter = intersection.coord

    directions = []
    for (xi, yi) in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
        if not (-1 < xi - x_inter < 1 and -1 < yi - y_inter < 1):
            directions.append((xi - x_inter, yi - y_inter))

    # Sort the directions clockwise
    directions.sort(key=lambda p: math.atan2(p[1], p[0]))
    ind = random.choice(range(len(directions) - 1))
    xi, yi = directions[ind]
    xj, yj = directions[ind + 1]

    direction1 = np.array([xi, yi])
    direction2 = np.array([xj, yj])
    norm1 = np.linalg.norm(direction1)
    norm2 = np.linalg.norm(direction2)

    # Normalize the direction vectors
    norm_direction1 = direction1 / norm1
    norm_direction2 = direction2 / norm2

    radius = max(50, min(norm1, norm2) / 5)

    # Calculate the angles relative to the positive x-axis
    angle1 = math.atan2(norm_direction1[1], norm_direction1[0])
    angle2 = math.atan2(norm_direction2[1], norm_direction2[0])

    # Calculate the angle between the lines
    ang = abs(angle2 - angle1)
    if ang > math.pi:
        ang = 2 * math.pi - ang

    # Determine the start and end angles for the arc
    start_angle = min(angle1, angle2)
    end_angle = max(angle1, angle2)

    # Plot the arc
    arc = Arc((x_inter, y_inter), 2 * radius, 2 * radius, angle=0, theta1=math.degrees(start_angle),
              theta2=math.degrees(end_angle), color=color)

    ax.add_artist(arc)

    # Add the angle label at the midpoint of the arc
    mid_angle = (start_angle + end_angle) / 2
    label_angle = math.degrees(ang)

    # Adjust the label position based on the angle value
    if label_angle < 10 or label_angle > 170:
        label_x = x_inter + radius * math.cos(mid_angle) * 1.2
        label_y = y_inter + radius * math.sin(mid_angle) * 1.2
    else:
        label_x = x_inter + radius * math.cos(mid_angle)
        label_y = y_inter + radius * math.sin(mid_angle)

    tc.append(label_x, label_y, f"{int(label_angle)}°", color='black')

def plot_polygon(ax, tc, points, edge_color='black', fill_color = 'white', label='' ):
   
    ax.add_patch(
        patches.Polygon(points,
                        closed=True,
                        facecolor=fill_color,
                        edgecolor=edge_color,
                        linewidth=2)
    )

    midpoint_x = sum([point[0] for point in points]) / len(points)
    midpoint_y = sum([point[1] for point in points]) / len(points)
    tc.append(midpoint_x, midpoint_y, label, verticalalignment='center', color='black')


def plot_filled_circle(ax, tc, center, radius, label='', edge_color = 'black', fill_color = 'yellow'):
    ax.add_patch( patches.Circle(center, radius, edgecolor=edge_color, facecolor=fill_color, linewidth=2) )

    tc.append(center[0], center[1], label, verticalalignment='center', color='black')



def plot_diagram(ax, tc, diagram):
    # fig, ax = plt.subplots()
    # ax.set_xlim(0, 1000)
    # ax.set_ylim(0, 1000)
    for plgn in diagram.polygons:
        plot_polygon(ax, tc, points=plgn.points, edge_color=plgn.edge_color, fill_color=plgn.fill_color, label=plgn.label)

    for filled_circle in diagram.filled_circles:
        plot_filled_circle(ax, tc, center=filled_circle.center, radius=filled_circle.radius, label=filled_circle.label, edge_color=filled_circle.edge_color, fill_color=filled_circle.fill_color)



    for line in diagram.lines:
        plot_line(ax, tc, label=line.label, point1=line.point1, point2=line.point2, infinite=line.infinite, tickmarks=line.tickmarks, dotted=line.dotted, color = line.color)

    for tup in diagram.perpendiculars:
        line1, line2, intersection = tup
        plot_perpendicularity(ax, tc, line1, line2, intersection)

    for circle in diagram.circles:
        # print(f"BEFORE PLOTTING CIRCLE {circle.label}")
        plot_circle(ax, tc, label='', center=circle.center, radius=circle.radius, color=circle.color)
        # print(f"AFTER PLOTTING CIRCLE {circle.label}")
    for triangle in diagram.triangles:
        plot_triangle(ax, tc, point1=triangle.vertices[0], point2=triangle.vertices[1], point3=triangle.vertices[2])

    for curve in diagram.curves:
        plot_curve(ax, tc,curve.x,curve.y, color = curve.color, label = curve.label)

    for ang in diagram.angles:
        line1, line2, intersection, ang_label = ang
        plot_angle(ax, tc, line1, line2, intersection, label = ang_label)


    for point in diagram.points:
        plot_point(ax, tc, label=point.label, coord=point.coord, color=point.color)
