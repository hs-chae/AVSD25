import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
import random
from .rules import *
import math

fixed_color = 'black'
fix_color   = False

COLOR_TRIPLES = [
    {'background': '#000000', 'shape_fill': '#FFFFFF', 'shape_edge': '#FF4500'},  # Black + White + Orange Red
    {'background': '#013220', 'shape_fill': '#00FFFF', 'shape_edge': '#FFD700'},  # Dark Green + Bright Blue + Gold
    {'background': '#D6EFFF', 'shape_fill': '#000080', 'shape_edge': '#FF4500'},  # Pale Blue + Navy + Orange Red
    {'background': '#FFDAB9', 'shape_fill': '#8B4513', 'shape_edge': '#4B0082'},  # Peach + Rust + Deep Purple
    {'background': '#4B0082', 'shape_fill': '#39FF14', 'shape_edge': '#FFD700'},  # Deep Purple + Neon Green + Gold
    {'background': '#191970', 'shape_fill': '#FFD700', 'shape_edge': '#FF6347'},  # Midnight Blue + Gold + Tomato Red
    {'background': '#2E2E2E', 'shape_fill': '#FF6347', 'shape_edge': '#ADFF2F'},  # Charcoal + Tomato Red + Green-Yellow
    {'background': '#006400', 'shape_fill': '#ADFF2F', 'shape_edge': '#4682B4'},  # Dark Green + Green-Yellow + Steel Blue
    {'background': '#FFA07A', 'shape_fill': '#800000', 'shape_edge': '#4B0082'},  # Light Salmon + Maroon + Deep Purple
    {'background': '#4682B4', 'shape_fill': '#FFDAB9', 'shape_edge': '#2F4F4F'},  # Steel Blue + Peach + Dark Slate Grey
    {'background': '#8B008B', 'shape_fill': '#FFD700', 'shape_edge': '#FF69B4'},  # Dark Magenta + Gold + Hot Pink
    {'background': '#696969', 'shape_fill': '#F0E68C', 'shape_edge': '#00CED1'},  # Dim Grey + Khaki + Dark Turquoise
    {'background': '#A52A2A', 'shape_fill': '#FFDAB9', 'shape_edge': '#FF4500'},  # Brown + Peach + Orange Red
    {'background': '#800080', 'shape_fill': '#FF4500', 'shape_edge': '#FFFF00'},  # Purple + Orange Red + Yellow
    {'background': '#FFFFFF', 'shape_fill': '#00008B', 'shape_edge': '#00CED1'},  # White + Dark Blue + Dark Turquoise
    {'background': '#2F4F4F', 'shape_fill': '#00CED1', 'shape_edge': '#FF7F50'},  # Dark Slate Grey + Dark Turquoise + Coral
    {'background': '#B0C4DE', 'shape_fill': '#4682B4', 'shape_edge': '#8B4513'},  # Light Steel Blue + Steel Blue + Rust
    {'background': '#008080', 'shape_fill': '#FFFFE0', 'shape_edge': '#FF6347'},  # Teal + Light Yellow + Tomato Red
    {'background': '#FF4500', 'shape_fill': '#000000', 'shape_edge': '#ADFF2F'},  # Orange Red + Black + Green-Yellow
    {'background': '#808080', 'shape_fill': '#FFFF00', 'shape_edge': '#800000'},  # Grey + Yellow + Maroon
    {'background': '#FFD700', 'shape_fill': '#4B0082', 'shape_edge': '#1E90FF'},  # Gold + Indigo + Dodger Blue
    {'background': '#708090', 'shape_fill': '#FFD700', 'shape_edge': '#00CED1'},  # Slate Grey + Gold + Dark Turquoise
    {'background': '#D2691E', 'shape_fill': '#FFFFFF', 'shape_edge': '#4682B4'},  # Chocolate + White + Steel Blue
    {'background': '#FF7F50', 'shape_fill': '#2E8B57', 'shape_edge': '#191970'},  # Coral + Sea Green + Midnight Blue
    {'background': '#FF69B4', 'shape_fill': '#1E90FF', 'shape_edge': '#4B0082'},  # Hot Pink + Dodger Blue + Deep Purple
]

# FONT_SIZES          = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# FONT_STYLES         = ['normal', 'italic', 'oblique']
MARKER_SIZES        = [4, 5, 6, 7, 8, 9, 10, 11, 12]
# RANDOM_FONT_SIZE    = random.choice(FONT_SIZES)
# RANDOM_FONT_STYLE   = random.choice(FONT_STYLES)
RANDOM_MARKER_SIZE  = random.choice(MARKER_SIZES)
RANDOM_POLYGON_ALPHA = np.random.uniform(0.3, 0.9)

def plot_point(ax, tc, label='', coord=(random.randint(0, 1000), random.randint(0, 1000)), 
               color = random.choice(colors.candidates), font_color = random.choice(colors.candidates)):
    x_coord, y_coord = coord
    ax.plot(x_coord, y_coord, marker='o', color=color, markersize=RANDOM_MARKER_SIZE)
    # ax.text(x_coord + 20, y_coord, label, fontsize=RANDOM_FONT_SIZE, style=RANDOM_FONT_STYLE, color=font_color)
    tc.append(x_coord + 20, y_coord, label, color=font_color)


def plot_fakepoint(ax, tc, label = '', coord = (random.randint(0, 1000),random.randint(0, 1000)), 
                   font_color = random.choice(colors.candidates)):
    x_coord, y_coord = coord
    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)
    # ax.text(x_coord, y_coord, label, fontsize=RANDOM_FONT_SIZE, verticalalignment=random_vertical_alignment, color=font_color)
    tc.append(x_coord, y_coord, label, verticalalignment=random_vertical_alignment, color=font_color)

def plot_coloredpoint(ax, tc, label = '', coord = (random.randint(0, 1000),random.randint(0, 1000)), 
                      color = random.choice(colors.candidates), font_color = random.choice(colors.candidates)):
    x_coord, y_coord = coord
    ax.plot(x_coord, y_coord, marker='o', color=color, markersize=RANDOM_MARKER_SIZE)
    # ax.text(x_coord + 20, y_coord, label, fontsize=RANDOM_FONT_SIZE, style=RANDOM_FONT_STYLE, color=font_color)
    tc.append(x_coord + 20, y_coord, label, color=font_color)

def plot_line(ax, tc, label, point1 : Point, point2 : Point, color = random.choice(colors.candidates), infinite = False, tickmarks = 0, dotted = False, 
              edge_color = random.choice(colors.candidates)):
    if fix_color:
        color = fixed_color

    x1, y1 = point1.coord
    x2, y2 = point2.coord

    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)

    if not infinite:
        if dotted:
            ax.plot([x1, x2], [y1, y2], color=edge_color, linestyle='dashed')
        else : ax.plot([x1, x2], [y1, y2], color=edge_color)  # 'o' stands for circle marker
        # ax.text((x1 + x2)/2 + 20, (y1 + y2)/2, label, fontsize=12, verticalalignment=random_vertical_alignment, color='black')
        tc.append((x1 + x2)/2 + 20, (y1 + y2)/2, label, color='black')

    else:
        direction = np.array([x2 - x1, y2 - y1])
        norm_direction = direction / np.linalg.norm(direction)

        factor = 10000
        new_x1, new_y1 = np.array([x1, y1]) - factor * norm_direction
        new_x2, new_y2 = np.array([x2, y2]) + factor * norm_direction

        ax.plot([new_x1, new_x2], [new_y1, new_y2], color=color)  # Dashed line for visual distinction
        # ax.text((x1 + x2) / 2, (y1 + y2) / 2, label, fontsize=12, verticalalignment=random_vertical_alignment, color='black')
        tc.append((x1 + x2) / 2, (y1 + y2) / 2, label, verticalalignment=random_vertical_alignment, color='black')

    if tickmarks > 0:
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


def plot_circle(ax, label, center, radius, 
                color = random.choice(diverse_colors.candidates)):
    
    if fix_color:
        color = fixed_color

    x, y = center.coord
    vertical_alignments = ['center', 'top', 'bottom']
    random_vertical_alignment = random.choice(vertical_alignments)
    circle = plt.Circle((x, y), radius, color=color, fill=False)  # 'o' stands for circle marker
    ax.add_artist(circle)


def plot_triangle(ax, tc, point1, point2, point3, diagram=Diagram(), mark_points = False, 
                  color = random.choice(diverse_colors.candidates)):
    if fix_color:
        color = fixed_color
    
    lines = [(point1,point2), (point2, point3), (point3, point1)]
    
    for line in lines:
        if line not in diagram.lines and (line[1],line[0]) not in diagram.lines:
            plot_line(ax, label='', point1=line[0], point2=line[1], color=color, tc=tc)

    if mark_points:
        plot_point(ax, label=point1.label, coord=point1.coord, tc=tc)
        plot_point(ax, label=point2.label, coord=point2.coord, tc=tc)
        plot_point(ax, label=point3.label, coord=point3.coord, tc=tc)


def plot_polygon(ax, points, diagram=Diagram(), visualize_edges_only=True, 
                 background_color = 'w', edge_color = 'k', fill_color = 'gray',
                 alpha= 1.0) : 

    x_coords = [each.coord[0] for each in points]
    y_coords = [each.coord[1] for each in points]
 
    if visualize_edges_only : 
        plt.fill(x_coords, y_coords, 
                 facecolor= 'none', 
                 edgecolor= edge_color, 
                 linewidth= 2,
                 alpha= alpha)
    else : 
        plt.fill(x_coords, y_coords, 
                 facecolor= fill_color, 
                 edgecolor= edge_color, 
                 linewidth= 2,
                 alpha= alpha)
        

def plot_coloredpolygon(ax, points, diagram=Diagram(), visualize_edges_only=True, 
                        background_color = 'w', edge_color = 'k', fill_color = 'gray',
                        alpha=1.0) : 

    x_coords = [each.coord[0] for each in points]
    y_coords = [each.coord[1] for each in points]
 
    if visualize_edges_only : 
        plt.fill(x_coords, y_coords, 
                 facecolor= background_color, 
                 edgecolor= edge_color, 
                 linewidth= 2,
                 alpha= alpha)
    else : 
        plt.fill(x_coords, y_coords, 
                 facecolor= fill_color, 
                 edgecolor= edge_color, 
                 linewidth= 2,
                 alpha= alpha)


def plot_perpendicularity(ax, line1, line2, intersection):
    if fix_color:
        color = fixed_color
    
    x1, y1 = line1.point1.x, line1.point1.y
    x2, y2 = line1.point2.x, line1.point2.y
    x3, y3 = line2.point1.x, line2.point1.y
    x4, y4 = line2.point2.x, line2.point2.y
    x5, y5 = intersection.x, intersection.y

    ind = 0
    while True:
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


def plot_curve(ax,x,y, t_start=0,t_end=1000 ,color = random.choice(diverse_colors.candidates)):
    if fix_color:
        color = fixed_color
    parameter= np.linspace(t_start, t_end, 1000)
    ax.plot(x, y, color=color)


def plot_angle(ax, line1, line2, intersection, color='black', label = ''):
    if fix_color:
        color = fixed_color
        
    x1, y1 = line1.point1.coord
    x2, y2 = line1.point2.coord
    x3, y3 = line2.point1.coord
    x4, y4 = line2.point2.coord
    x_inter, y_inter = intersection.coord

    directions = []
    for (xi, yi) in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
        if not (-1 < xi - x_inter < 1 and -1 < yi - y_inter < 1):
            directions.append((xi - x_inter, yi - y_inter))

    directions.sort(key=lambda p: math.atan2(p[1], p[0]))
    ind = random.choice(range(len(directions) - 1))
    xi, yi = directions[ind]
    xj, yj = directions[ind + 1]

    direction1 = np.array([xi, yi])
    direction2 = np.array([xj, yj])
    norm1 = np.linalg.norm(direction1)
    norm2 = np.linalg.norm(direction2)

    norm_direction1 = direction1 / norm1
    norm_direction2 = direction2 / norm2

    radius = max(50, min(norm1, norm2) / 5)

    angle1 = math.atan2(norm_direction1[1], norm_direction1[0])
    angle2 = math.atan2(norm_direction2[1], norm_direction2[0])

    ang = abs(angle2 - angle1)
    if ang > math.pi:
        ang = 2 * math.pi - ang

    start_angle = min(angle1, angle2)
    end_angle = max(angle1, angle2)

    arc = Arc((x_inter, y_inter), 2 * radius, 2 * radius, angle=0, theta1=math.degrees(start_angle),
              theta2=math.degrees(end_angle), color=color)

    ax.add_artist(arc)

    mid_angle = (start_angle + end_angle) / 2
    label_angle = math.degrees(ang)

    if label_angle < 10 or label_angle > 170:
        label_x = x_inter + radius * math.cos(mid_angle) * 1.2
        label_y = y_inter + radius * math.sin(mid_angle) * 1.2
    else:
        label_x = x_inter + radius * math.cos(mid_angle)
        label_y = y_inter + radius * math.sin(mid_angle)

    # ax.text(label_x, label_y, f"{int(label_angle)}°", fontsize=10, color='black')


def plot_diagram(ax, tc, diagram, verbose=False):

    # tc is updated by : plot_point, plot_fakepoint, plot_coloredpoint, plot_line, plot_triangle
    
    if diagram.colored : 
        gray_value = np.random.uniform(0, 1)  # Random value between 0 (black) and 1 (white)
        background_color = (gray_value, gray_value, gray_value)  # Grayscale RGB tuple
        fill_color = 'k'
        edge_color = 'k'
        font_color = 'k'

    else : 
        selected_triple = random.choice(COLOR_TRIPLES) # color [background, shape fill, shape edge]
        background_color    = selected_triple['background']
        fill_color          = selected_triple['shape_fill']
        edge_color          = selected_triple['shape_edge']
        font_color          = edge_color

    visualize_edges_only = random.choice([True, False])

    ax.set_facecolor(background_color)
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    for spine in ax.spines.values():
        spine.set_visible(False)
        
    for point in diagram.points:
        plot_point(ax, label=point.label, coord=point.coord, 
                   color=font_color, font_color=font_color, tc= tc)
        if verbose : 
            print("Plotted point", point.label)

    for fakepoint in diagram.fakepoints: 
        plot_fakepoint(ax, label=fakepoint.label, coord=fakepoint.coord, 
                       font_color=font_color, tc= tc)
        if verbose : 
            print("Plotted fakepoint", fakepoint.label)

    for coloredpoint in diagram.coloredpoints:
        plot_coloredpoint(ax, label=coloredpoint.label, coord=coloredpoint.coord, 
                          color=coloredpoint.color,
                          font_color=font_color, tc= tc)
        if verbose : 
            print("Plotted coloredpoint", coloredpoint.label)

    for line in diagram.lines:
        plot_line(ax, label=line.label, point1=line.point1, point2=line.point2, infinite=line.infinite, tickmarks=line.tickmarks, dotted=line.dotted,
                  edge_color=fill_color, tc= tc)            

    for tup in diagram.perpendiculars:
        line1, line2, intersection = tup
        plot_perpendicularity(ax, line1, line2, intersection)

    for circle in diagram.circles:
        plot_circle(ax, label='', center=circle.center, radius=circle.radius,
                    color=edge_color)

    for triangle in diagram.triangles:
        plot_triangle(ax, point1=triangle.vertices[0], point2=triangle.vertices[1], point3=triangle.vertices[2],
                      color=edge_color, tc= tc)

    for curve in diagram.curves:
        plot_curve(ax,curve.x,curve.y)

    for _polygon in diagram.polygons :
        plot_polygon(ax, _polygon.vertices, visualize_edges_only=visualize_edges_only,
                     background_color   = background_color, 
                     edge_color         = fill_color, 
                     fill_color         = fill_color,
                     alpha              = RANDOM_POLYGON_ALPHA)
        
    for _coloredpolygon in diagram.coloredpolygons :
        plot_coloredpolygon(ax, _coloredpolygon.vertices, visualize_edges_only=False, 
                            background_color    = background_color, 
                            edge_color          = _coloredpolygon.color, 
                            fill_color          = _coloredpolygon.color,
                            alpha               = _coloredpolygon.alpha)

    for ang in diagram.angles:
        line1, line2, intersection, ang_label = ang
        plot_angle(ax, line1, line2, intersection, label = ang_label)