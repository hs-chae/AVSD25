import matplotlib.pyplot as plt
import numpy as np
from .labels import *
import random
import math
import json

def remove_color(diagram, color):
    diagram.usable_colors = [c for c in diagram.usable_colors if c != color]
    return diagram

def random_angle():
    return np.random.uniform(np.pi/9, 17/9*np.pi)

def random_acute():
    return np.random.uniform(np.pi/9, 4/9*np.pi)

def random_obtuse():
    return np.random.uniform(5/9*np.pi, 8/9*np.pi)

def rotate_vector(vector, angle):
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) @ np.array(vector)


def random_coord(start = 10, end = 990):
    return np.random.uniform(start, end)


def line_already_in(diagram, point1, point2):
    for line in diagram.lines:
        if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
            return True
    return False

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def label_point(diagram):
    ind = 0
    while True:
        label = random.choice(capitals.candidates)
        if label not in [point.label for point in diagram.points]:
            return label
        if ind > 30:
            return diagram
       
        ind += 1


def label_line(diagram):
    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label == "" or (label not in [line.label for line in diagram.lines]):
            return label
        if ind > 200:
            return diagram
        ind += 1

def label_line_nonempty(diagram):
    ind = 0
    while True:
        label = random.choice(small_letters_nonempty.candidates)
        if (label not in [line.label for line in diagram.lines]):
            return label
        if ind > 200:
            return diagram
        ind += 1

def random_length():
        return int(random.uniform(200, 700))


def add_radius(center_x, center_y, radius):
    angle = random_angle()
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    length = f'{random_length()}'
    return (x, y, length)


#Objects definition
class Point:
    def __init__(self, x, y, label, color = 'black'):
        self.x = x
        self.y = y
        self.coord = (x,y)
        self.label = label
        self.color = color

    def __str__(self):
        return f'Point({self.x}, {self.y}, {self.label})'


class Line:
    def __init__(self, point1 : Point, point2 : Point, label, infinite=False, tickmarks = 0, dotted = False, color = 'black'):
        self.passing_points = [point1, point2]
        self.point1 = point1
        self.point2 = point2
        self.label = label
        self.infinite = infinite
        self.tickmarks = tickmarks
        self.dotted = dotted
        self.color = color

    def __str__(self):
        return f'Line({self.passing_points}, {self.label}, {self.infinite})'

class Circle:
    def __init__(self, center, radius, label, color = 'black'):
        self.center = center
        self.radius = radius
        self.label = label
        self.color = color

    def __str__(self):
        return f'Circle({self.center}, {self.radius}, {self.label})'

class Triangle:
    def __init__(self, point1, point2, point3, label = ''):
        self.vertices = [point1, point2, point3]
        # self.label = label
        self.label = f'Triangle({point1.label}{point2.label}{point3.label})'

    def __str__(self):
        return f'Triangle({self.vertices}, {self.label})'

class Curve:
    def __init__(self, x, y, label, color = 'black'):
        self.x = x
        self.y = y
        self.label = label
        self.color = color
    def __str__(self):
        return f'Curve({self.label})'




class polygon:
    def __init__(self, points, label = '', edge_color = 'black', fill_color = 'white'):
        self.points = points
        self.label = label
        self.edge_color = edge_color
        self.fill_color = fill_color


    def __str__(self):
        return f'Polygon({self.vertices}, {self.label})'

class filled_circle:
    def __init__(self, center, radius, label = '', edge_color = 'black', fill_color = 'white'):
        self.center = center #(x,y)
        self.radius = radius
        self.label = label
        self.edge_color = edge_color
        self.fill_color = fill_color

    def __str__(self):
        return f'Filled_Circle({self.center}, {self.radius}, {self.label})'

#Diagram definition
class Diagram:
    def __init__(self, points=[], lines=[], circles=[], triangles=[], squares=[], steps=[]):
        self.points = points
        self.lines = lines
        self.circles = circles
        self.triangles = triangles
        self.squares = squares
        self.steps = steps
        self.entities = []
        self.perpendiculars = []
        self.curves = []
        self.angles = []
        self.polygons = []
        self.filled_circles = []
        self.usable_colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'yellow']




def normalize(vector):
    (x, y) = vector
    magnitude = (x**2 + y**2)**0.5
    return (x / magnitude, y / magnitude)

def assert_coord_in_range(x,y):
    return x < 1000 and x > 0 and y < 1000 and y > 0

def add_free_point(diagram : Diagram):
    x_coord, y_coord = random_coord(), random_coord()
    label = label_point(diagram)
    diagram.points.append(Point(x_coord, y_coord, label))
    # diagram.entities.append(f'Point({label})')
    return diagram

def C_add_free_point(diagram : Diagram):
    color = random.choice(diagram.usable_colors)

    x_coord, y_coord = random_coord(), random_coord()
    label = label_point(diagram)
    diagram.points.append(Point(x_coord, y_coord, label))
    # diagram.entities.append(f'Point({label})')
    return diagram

def add_free_line(diagram: Diagram):
    while True:
        x1, y1 = random_coord(), random_coord()
        x2, y2 = random_coord(), random_coord()
        length = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if length > 300:
            break

    label1 = label_point(diagram)

    while True:
        label2 = label_point(diagram)
        if label2 != label1:
            break

    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label not in [line.label for line in diagram.lines]:
            break
        if ind > 30:
            return diagram
        ind += 1
    length = int(length)


    # label = random.sample([label, f'{length}'],1)[0]
    diagram.points.append(Point(x1, y1, label1))
    diagram.points.append(Point(x2, y2, label2))
    label = random.choice([label, "", "", "", "", "", ""])

    diagram.lines.append(Line(diagram.points[-2], diagram.points[-1], label))

    # diagram.entities.extend([f'{label} : Line({label1}{label2})'])
    return diagram

def C_add_free_line(diagram: Diagram):
    color = random.choice(diagram.usable_colors)
    diagram = remove_color(diagram, color)

    while True:
        x1, y1 = random_coord(), random_coord()
        x2, y2 = random_coord(), random_coord()
        length = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        if length > 300:
            break

    label1 = label_point(diagram)

    while True:
        label2 = label_point(diagram)
        if label2 != label1:
            break

    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label not in [line.label for line in diagram.lines]:
            break
        if ind > 30:
            return diagram
        ind += 1
    length = int(length)


    # label = random.sample([label, f'{length}'],1)[0]
    diagram.points.append(Point(x1, y1, label1))
    diagram.points.append(Point(x2, y2, label2))
    label = random.choice([label, "", "", "", "", "", ""])

    diagram.lines.append(Line(diagram.points[-2], diagram.points[-1], label, color = color))

    # diagram.entities.extend([f'{label} : Line({label1}{label2})'])
    return diagram

def add_free_point_with_line(diagram : Diagram):
    if len(diagram.points) == 0:
        diagram = add_free_point(diagram)

    p1 = random.choice(diagram.points)
    ind = 0
    while True:
        x_coord, y_coord = random_coord(), random_coord()
        length = ((p1.x - x_coord)**2 + (p1.y - y_coord)**2)**0.5
        label = label_point(diagram)
        if length > 200:
            break
        if ind  >30:
            return diagram
        ind += 1
    ind = 0
    while True:
        label_l = random.choice(small_letters.candidates)
        if label_l not in [line.label for line in diagram.lines]:
            break
        if ind > 30:
            return diagram
        ind += 1
    diagram.points.append(Point(x_coord, y_coord, label))

    label_l = random.choice([label_l, "", "", "", "", "", ""])
    diagram.lines.append(Line(p1, diagram.points[-1], label_l))

    return diagram

def C_add_free_point_with_line(diagram : Diagram):
    # print(f"diagram.usable_colors : {diagram.usable_colors}")
    color = random.choice(diagram.usable_colors)
    diagram = remove_color(diagram, color)

    if len(diagram.points) == 0:
        diagram = add_free_point(diagram)
    p1 = random.choice(diagram.points)
    ind = 0
    while True:
        x_coord, y_coord = random_coord(), random_coord()
        length = ((p1.x - x_coord)**2 + (p1.y - y_coord)**2)**0.5
        label = label_point(diagram)
        if length > 200:
            break
        if ind  >30:
            return diagram
        ind += 1
    ind = 0
    while True:
        label_l = random.choice(small_letters.candidates)
        if label_l not in [line.label for line in diagram.lines]:
            break
        if ind > 30:
            return diagram
        ind += 1
    diagram.points.append(Point(x_coord, y_coord, label))

    label_l = random.choice([label_l, "", "", "", "", "", ""])
    diagram.lines.append(Line(p1, diagram.points[-1], label_l, color = color))
    return diagram

def add_line(diagram : Diagram):
    try:
        ind = 0
        while True:

            point1, point2 = random.sample(diagram.points, 2)
            length = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5


            #assert that the line is not already in the diagram
            already_in = False
            for line in diagram.lines:
                if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
                    already_in = True

            if ind > 100:
                return diagram
            # elif already_in: print('already in')
            else: break

            ind += 1


        label = random.choice(small_letters.candidates.extend(["","","","","",""]))
        diagram.lines.append(Line(point1, point2, label))

        return diagram
    except: return diagram

def C_add_line(diagram : Diagram):
    try:
        color =  random.choice(diagram.usable_colors)
        diagram = remove_color(diagram, color)

        ind = 0
        while True:

            point1, point2 = random.sample(diagram.points, 2)
            length = ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5


            #assert that the line is not already in the diagram
            already_in = False
            for line in diagram.lines:
                if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
                    already_in = True

            if ind > 100:
                return diagram
            # elif already_in: print('already in')
            else: break

            ind += 1


        label = random.choice(small_letters.candidates.extend(["","","","","",""]))
        diagram.lines.append(Line(point1, point2, label, color = color))

        return diagram
    except: return diagram

def add_infinite_line(diagram : Diagram):

    point1, point2 = random.sample(diagram.points, 2)
    label = ''
    diagram.lines.append(Line(point1, point2, label, infinite=True))

    return diagram

def C_add_infinite_line(diagram : Diagram):
    color = random.choice(diagram.usable_colors)
    diagram = remove_color(diagram, color)

    point1, point2 = random.sample(diagram.points, 2)
    label = ''
    diagram.lines.append(Line(point1, point2, label, infinite=True, color = color))


    return diagram

def add_circle(diagram : Diagram, radius = None):
    if len(diagram.points) == 0:
        diagram = add_free_point(diagram)
    center = random.choice(diagram.points)
    max_rad = min(center.x, center.y, 1000 - center.x, 1000 - center.y)
    if radius is None :
        ind = 0
        while True:
            radius = random.uniform(150, max_rad)
            if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
                break
            if ind > 10:
                return diagram
            ind += 1

    else:
        radius = radius
        assert assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                 center.y - radius)


    # label = random.choice(small_letters.candidates)
    label = f'({center.label},{radius})'
    different_pt_label = label_point(diagram)
    diagram.circles.append(Circle(center, radius, label))

    return diagram

def C_add_circle(diagram : Diagram, radius = None):
    color  = random.choice(diagram.usable_colors)
    diagram = remove_color(diagram, color)

    if len(diagram.points) == 0:
        diagram = add_free_point(diagram)

    center = random.choice(diagram.points)
    max_rad = min(center.x, center.y, 1000 - center.x, 1000 - center.y)
    if radius is None :
        ind = 0
        while True:
            radius = random.uniform(150, max_rad)
            if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
                break
            if ind > 10:
                return diagram
            ind += 1

    else:
        radius = radius
        assert assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                 center.y - radius)

    # label = random.choice(small_letters.candidates)
    label = f'({center.label},{radius})'
    different_pt_label = label_point(diagram)
    diagram.circles.append(Circle(center, radius, label, color =  color))

    return diagram

def add_free_circle(d):
    ind = 0
    while True:
        
        x_coord, y_coord = random_coord(), random_coord()
        center = Point(x_coord, y_coord, label_point(d))
        radius = int(random.uniform(200,500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
            break
        if ind> 10:
            
            return d
        ind += 1

    d.points.append(center)
    d.circles.append(Circle(center, radius, f'({center.label},{radius})'))
    return d

def C_add_free_circle(d):
    color = random.choice(d.usable_colors)

    d = remove_color(d, color)

    ind = 0
    while True:
        x_coord, y_coord = random_coord(), random_coord()
        center = Point(x_coord, y_coord, label_point(d))
        radius = int(random.uniform(200,500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
            break
        if ind> 30:
            return d
        ind += 1

    d.points.append(center)
    d.circles.append(Circle(center, radius, f'({center.label},{radius})', color = color))

    return d

def circle_with_radius(d):
    while True:
        center = Point(random_coord(), random_coord(), label_point(d))
        radius = int( random.uniform(50, 500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
            break
    circle = Circle(center, radius, '')
    angle = random_angle()
    x,y  = center.x + radius * np.cos(angle), center.y + radius * np.sin(angle)
    P = Point(x, y, "")
    length = random_length()
    d.points.append(center)
    d.circles.append(circle)
    d.lines.append(Line(center, P, label=length, dotted=True))

    return d


def C_circle_with_radius(d):
    color = random.choice(d.usable_colors)
    color_2 = random.choice(d.usable_colors)
    d = remove_color(d, color)

    while True:
        center = Point(random_coord(), random_coord(), label_point(d))
        radius = int(random.uniform(50, 500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                 center.y - radius):
            break
    circle = Circle(center, radius, '', color = color)
    angle = random_angle()
    x, y = center.x + radius * np.cos(angle), center.y + radius * np.sin(angle)
    P = Point(x, y, "")
    length = random_length()
    d.points.append(center)
    d.circles.append(circle)
    d.lines.append(Line(center, P, label=length, dotted=True, color = color_2))

    return d


def length_1(d):

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    while True:
        label1 = label_point(d)
        label2 = label_point(d)
        if label2 != label1:
            break
    new_labels.extend([label1, label2])

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    #Generate longer line
    ind = 0
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break
    while True:
        label4 = label_point(d)
        if label4 not in new_labels:
            new_labels.append(label4)
            break

    C = Point(X0, Y0, label3)
    D = Point(X1, Y1, label4)

    d.points.extend([A, B, C, D])
    d.lines.extend([Line(A, B, ''), Line(C, D, '')])
    d.entities.append(('length_1', [A.label, B.label, C.label, D.label]))
    return d

def C_length_1(d):
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)


    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    while True:
        label1 = label_point(d)
        label2 = label_point(d)
        if label2 != label1:
            break
    new_labels.extend([label1, label2])

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    #Generate longer line
    ind = 0
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break
    while True:
        label4 = label_point(d)
        if label4 not in new_labels:
            new_labels.append(label4)
            break

    C = Point(X0, Y0, label3)
    D = Point(X1, Y1, label4)

    d.points.extend([A, B, C, D])
    d.lines.extend([Line(A, B, '', color = col1), Line(C, D, '', color = col2)])
    d.entities.append(('C_length_1', [A.label, B.label, C.label, D.label, col1, col2]))
    return d

def length_2(d):

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_line_nonempty(d)
    new_labels.append(label1)

    A = Point(x0, y0, "")
    B = Point(x1, y1, "")

    #Generate longer line
    ind = 0
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_line_nonempty(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break


    C = Point(X0, Y0, "")
    D = Point(X1, Y1, "")

    # d.points.extend([A, B, C, D])
    d.lines.extend([Line(A, B, label1), Line(C, D, label3)])
    d.entities.append(('length_2', [label1, label3]))
    return d

def C_length_2(d):

    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_line_nonempty(d)
    new_labels.append(label1)

    A = Point(x0, y0, "")
    B = Point(x1, y1, "")

    #Generate longer line
    ind = 0
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_line_nonempty(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break


    C = Point(X0, Y0, "")
    D = Point(X1, Y1, "")

    # d.points.extend([A, B, C, D])
    d.lines.extend([Line(A, B, label1, color = col1), Line(C, D, label3, color = col2)])
    d.entities.append(('C_length_2', [label1, label3, col1, col2]))
    return d


def length_3(d):
    #Generate a longer line and other shorter lines
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_line_nonempty(d)
    new_labels.append(label1)

    A = Point(x0, y0, "")
    B = Point(x1, y1, "")

    ind = 0
    #Generate longer line
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label2 = label_line_nonempty(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    C = Point(X0, Y0, "")
    D = Point(X1, Y1, "")

    #Generate shorter lines
    short_count = random.randint(3, 5)
    short_lines = []
    for i in range(short_count):
        while True:
            x0, y0 = random_coord(), random_coord()
            shorter_length = length * random.uniform(0.2, 0.9)
            angle = random_angle()
            x1, y1 = x0 + shorter_length * np.cos(angle), y0 + shorter_length * np.sin(angle)
            if assert_coord_in_range(x1, y1):
                break

        while True:
            label = label_line_nonempty(d)
            if label not in new_labels:
                new_labels.append(label)
                break

        short_lines.append(Line(Point(x0, y0, ""), Point(x1, y1, ""), label))

    d.lines.extend([Line(A, B, label1), Line(C, D, label2)])
    d.lines.extend(short_lines)
    d.entities.append(('length_3', [label1, label2] + [line.label for line in short_lines]))
    return d

def C_length_3(d):
    #Generate a longest line and other shorter lines
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_line_nonempty(d)
    new_labels.append(label1)

    A = Point(x0, y0, "")
    B = Point(x1, y1, "")

    ind = 0
    #Generate longer line
    while True:
        X0, Y0 = random_coord(), random_coord()
        scale = random.uniform(1.1, 2)
        angle = random_angle()
        X1, Y1 = X0 + scale * length * np.cos(angle), Y0 + scale * length * np.sin(angle)
        if assert_coord_in_range(X1, Y1):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label2 = label_line_nonempty(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    C = Point(X0, Y0, "")
    D = Point(X1, Y1, "")

    #Generate shorter lines
    short_count = random.randint(2, 4)
    short_lines = []
    for i in range(short_count):
        while True:
            x0, y0 = random_coord(), random_coord()
            shorter_length = length * random.uniform(0.2, 0.9)
            angle = random_angle()
            x1, y1 = x0 + shorter_length * np.cos(angle), y0 + shorter_length * np.sin(angle)
            if assert_coord_in_range(x1, y1):
                break

        while True:
            label = label_line_nonempty(d)
            if label not in new_labels:
                new_labels.append(label)
                break

        short_lines.append(Line(Point(x0, y0, ""), Point(x1, y1, ""), label, color = color))

    d.lines.extend([Line(A, B, label1), Line(C, D, label2,color =  color)])
    d.lines.extend(short_lines)
    d.entities.append(('C_length_3', [label1, label2, color] + [line.label for line in short_lines]))
    return d


def length_4(d):
    #Geenrate a target line
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    #Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if radius < length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius, y0 - radius):
            break
        elif ind > 30:
            # print(f"breakout of loop with radius {radius} and length {length}")
            return d
        else:
            # print("too large radius")
            ind+=1


    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_4', [A.label, B.label, C.label]))
    return d

def C_length_4(d):
    #Geenrate a target line
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    #Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if radius < length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius, y0 - radius):
            break
        elif ind > 30:
            # print(f"breakout of loop with radius {radius} and length {length}")
            return d
        else:
            # print("too large radius")
            ind+=1


    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "", color = col2)

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, "", color = col1))
    d.circles.append(circle)
    d.entities.append(('C_length_4', [A.label, B.label, C.label, col1, col2]))
    return d

def length_5(d):
    # Geenrate a target line
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + 0.9 * length * np.cos(angle), y0 + 0.9*  length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    # Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if radius > 1.1 * length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius,
                                                                                                         y0 - radius):
            break
        elif ind > 30:
            # print(f"breakout of loop with radius {radius} and length {length}")
            return d
        else:
            # print("too large radius")
            ind+=1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_5', [A.label, B.label, C.label]))
    return d

def C_length_5(d):
    # Geenrate a target line
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + 0.9* length * np.cos(angle), y0 + 0.9* length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    # Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if radius > 1.1 * length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius,
                                                                                                         y0 - radius):
            break
        elif ind > 30:
            # print(f"breakout of loop with radius {radius} and length {length}")
            return d
        else:
            # print("too large radius")
            ind+=1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "", color = col2)

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, "", color = col1))
    d.circles.append(circle)
    d.entities.append(('C_length_5', [A.label, B.label, C.label, col1, col2]))
    return d


def length_6(d):
    # Geenrate a target line
    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    # Generate a circle
    ind=0
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = length
        if assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius, y0 - radius):
            break
        elif ind > 30:
            # print(f"breakout of loop with lnegth {length}")
            return d
        else:
            # print("too large radius")
            ind+=1


    ind=0
    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break



    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_6', [A.label, B.label, C.label]))
    return d

def C_length_6(d):
    # Geenrate a target line
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    # Generate a circle
    ind=0
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = length
        if assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius, y0 - radius):
            break
        elif ind > 30:
            # print(f"breakout of loop with lnegth {length}")
            return d
        else:
            # print("too large radius")
            ind+=1


    ind=0
    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break



    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "", color= col2)

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, "", color = col1))
    d.circles.append(circle)
    d.entities.append(('C_length_6', [A.label, B.label, C.label, col1, col2]))
    return d


def length_7(d):
    # Geenrate a target line
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    # Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if 2*radius < length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius,
                                                                                                         y0 - radius):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_7', [A.label, B.label, C.label, col1, col2]))

    return d

def C_length_7(d):
    # Geenrate a target line
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    # Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if 2*radius < length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius,
                                                                                                         y0 - radius):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "", color = col2)

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, "", color = col1))
    d.circles.append(circle)
    d.entities.append(('C_length_7', [A.label, B.label, C.label, col1, col2]))

    return d



def length_8(d):
    #Generate a anchor point
    anchor = Point(random_coord(), random_coord(), label_point(d))
    new_label = [anchor.label]

    #Generate the furthest point.
    while True:
        x0, y0 = random_coord(), random_coord()
        if ((x0 - anchor.x)**2 + (y0 - anchor.y)**2)**0.5 > 300:
            break
    while True:
        label = label_point(d)
        if label not in new_label:
            new_label.append(label)
            break

    furthest = Point(x0, y0, label)
    new_points = [anchor, furthest]
    #Generate closer points
    num = random.randint(1, 2)
    for i in range(num):
        while True:
            scale = random.uniform(0.1, 0.9)
            angle = random_angle()
            x1, y1 = anchor.x + scale * ((x0 - anchor.x) * np.cos(angle) - (y0 - anchor.y) * np.sin(angle)), anchor.y + scale * ((x0 - anchor.x) * np.sin(angle) + (y0 - anchor.y) * np.cos(angle))
            if assert_coord_in_range(x1, y1):
                    break
        while True:
            label = label_point(d)
            if label not in new_label:
                new_label.append(label)
                break
        new_points.append(Point(x1, y1, label))

    d.points.extend(new_points)
    d.entities.append(('length_8', new_label))
    return d

def C_length_8(d):
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)
    # d = remove_color(d, col3)

    #Generate a anchor point
    anchor = Point(random_coord(), random_coord(), label_point(d), color = col1)
    new_label = [anchor.label]

    #Generate the furthest point.
    while True:
        x0, y0 = random_coord(), random_coord()
        if ((x0 - anchor.x)**2 + (y0 - anchor.y)**2)**0.5 > 300:
            break
    while True:
        label = label_point(d)
        if label not in new_label:
            new_label.append(label)
            break

    furthest = Point(x0, y0, label, color = col2)
    new_points = [anchor, furthest]
    #Generate closer points
    num = random.randint(1, 2)
    ind = 0
    for i in range(num):
        while True:
            scale = random.uniform(0.1, 0.9)
            angle = random_angle()
            x1, y1 = anchor.x + scale * ((x0 - anchor.x) * np.cos(angle) - (y0 - anchor.y) * np.sin(angle)), anchor.y + scale * ((x0 - anchor.x) * np.sin(angle) + (y0 - anchor.y) * np.cos(angle))
            if assert_coord_in_range(x1, y1):
                    break

            if ind > 30:
                return d 
            ind +=1 
        while True:
            label = label_point(d)
            if label not in new_label:
                new_label.append(label)
                break
        new_points.append(Point(x1, y1, label, color = col2))

    d.points.extend(new_points)
    d.entities.append(('C_length_8', [new_label[0], new_label[1], new_label[2], col1, col2]))
    return d

#Line l is shorter than the diameter of the circle


def length_9(d):
    # Geenrate a target line
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    # Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if 2*radius > 1.1*length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius,
                                                                                                         y0 - radius):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "")

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, ""))
    d.circles.append(circle)
    d.entities.append(('length_9', [A.label, B.label, C.label, col1, col2]))

    return d

def C_length_9(d):
    # Geenrate a target line
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)

    while True:
        x0, y0 = random_coord(), random_coord()
        length = random_length()
        angle = random_angle()
        x1, y1 = x0 + length * np.cos(angle), y0 + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break

    new_labels = []
    label1 = label_point(d)
    new_labels.append(label1)
    while True:
        label2 = label_point(d)
        if label2 not in new_labels:
            new_labels.append(label2)
            break

    A = Point(x0, y0, label1)
    B = Point(x1, y1, label2)

    ind = 0
    # Generate a circle
    while True:
        x0, y0 = random_coord(), random_coord()
        radius = random_length()
        if 2*radius > 1.1* length and assert_coord_in_range(x0 + radius, y0 + radius) and assert_coord_in_range(x0 - radius,
                                                                                                         y0 - radius):
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        label3 = label_point(d)
        if label3 not in new_labels:
            new_labels.append(label3)
            break

    C = Point(x0, y0, label3)
    circle = Circle(C, radius, "", color = col2)

    d.points.extend([A, B, C])
    d.lines.append(Line(A, B, "", color = col1))
    d.circles.append(circle)
    d.entities.append(('C_length_9', [A.label, B.label, C.label, col1, col2]))

    return d


def length_10(d):
    #Line l is shorter than the distance of point A and point B
    while len(d.points) < 1:
        d = add_free_point(d)

    new_labels = []

    #Generate two ends of line l
    P = random.choice(d.points)

    ind = 0
    while True:
        length = random_length()
        angle = random_angle()
        x1, y1 = P.x + length * np.cos(angle), P.y + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break
        if ind > 30:
            return d
        ind += 1

    Q_label  = label_point(d)
    new_labels.append(Q_label)
    Q = Point(x1, y1, Q_label)

    #Generate point A, B
    ind = 0
    while True:
        Ax, Ay, B_x, B_y = random_coord(), random_coord(), random_coord(), random_coord()
        if ((Ax - B_x)**2 + (Ay - B_y)**2)**0.5 > 1.1 * length:
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        A_label = label_point(d)
        if A_label not in new_labels:
            new_labels.append(A_label)
            break

    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break

    A = Point(Ax, Ay, A_label)
    B = Point(B_x, B_y, B_label)

    d.points.extend([A, B, Q])
    d.lines.extend([Line(P, Q, '')])
    d.entities.append(('length_10', [P.label, Q.label, A.label, B.label]))

    return d

def C_length_10(d):
    #Line l is shorter than the distance of point A and point B
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    while len(d.points) < 1:
        d = add_free_point(d)

    new_labels = []

    #Generate two ends of line l
    P = random.choice(d.points)

    ind = 0
    while True:
        length = random_length()
        angle = random_angle()
        x1, y1 = P.x + length * np.cos(angle), P.y + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break
        if ind > 30:
            return d
        ind += 1

    Q_label  = label_point(d)
    new_labels.append(Q_label)
    Q = Point(x1, y1, Q_label)

    #Generate point A, B
    ind = 0
    while True:
        Ax, Ay, B_x, B_y = random_coord(), random_coord(), random_coord(), random_coord()
        if ((Ax - B_x)**2 + (Ay - B_y)**2)**0.5 > 1.1 * length:
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        A_label = label_point(d)
        if A_label not in new_labels:
            new_labels.append(A_label)
            break

    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break

    A = Point(Ax, Ay, A_label)
    B = Point(B_x, B_y, B_label)

    d.points.extend([A, B, Q])
    d.lines.extend([Line(P, Q, '', color = color)])
    d.entities.append(('C_length_10', [P.label, Q.label, A.label, B.label, color]))

    return d


def length_11(d):
    #Line l has length equal to the distance of point A and point B

    while len(d.points) < 1:
        d = add_free_point(d)

    new_labels = []

    # Generate two ends of line l
    P = random.choice(d.points)

    ind = 0
    while True:
        length = random_length()
        angle = random_angle()
        x1, y1 = P.x + length * np.cos(angle), P.y + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break
        if ind > 30:
            return d
        ind += 1

    Q_label = label_point(d)
    new_labels.append(Q_label)
    Q = Point(x1, y1, Q_label)

    # Generate point A, B
    ind = 0
    while True:
        Ax, Ay = random_coord(), random_coord()
        angle = random_angle()
        B_x, B_y = Ax + length * np.cos(angle), Ay + length * np.sin(angle)
        if assert_coord_in_range(B_x, B_y):
            break

        if ind > 30:
            return d
        ind += 1

    while True:
        A_label = label_point(d)
        if A_label not in new_labels:
            new_labels.append(A_label)
            break

    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break

    A = Point(Ax, Ay, A_label)
    B = Point(B_x, B_y, B_label)

    d.points.extend([A, B, Q])
    d.lines.extend([Line(P, Q, '')])
    d.entities.append(('length_11', [P.label, Q.label, A.label, B.label]))

    return d

def C_length_11(d):
    #Line l has length equal to the distance of point A and point B
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    while len(d.points) < 1:
        d = add_free_point(d)

    new_labels = []

    # Generate two ends of line l
    P = random.choice(d.points)

    ind = 0
    while True:
        length = random_length()
        angle = random_angle()
        x1, y1 = P.x + length * np.cos(angle), P.y + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break
        if ind > 30:
            return d
        ind += 1

    Q_label = label_point(d)
    new_labels.append(Q_label)
    Q = Point(x1, y1, Q_label)

    # Generate point A, B
    ind = 0
    while True:
        Ax, Ay = random_coord(), random_coord()
        angle = random_angle()
        B_x, B_y = Ax + length * np.cos(angle), Ay + length * np.sin(angle)
        if assert_coord_in_range(B_x, B_y):
            break

        if ind > 30:
            return d
        ind += 1

    while True:
        A_label = label_point(d)
        if A_label not in new_labels:
            new_labels.append(A_label)
            break

    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break

    A = Point(Ax, Ay, A_label)
    B = Point(B_x, B_y, B_label)

    d.points.extend([A, B, Q])
    d.lines.extend([Line(P, Q, '', color = color)])
    d.entities.append(('C_length_11', [P.label, Q.label, A.label, B.label, color]))

    return d


def length_12(d):
    #Line l is longer than the distance of point A and point B
    while len(d.points) < 1:
        d = add_free_point(d)

    new_labels = []

    #Generate two ends of line l
    P = random.choice(d.points)

    ind = 0
    while True:
        length = random_length()
        angle = random_angle()
        x1, y1 = P.x + length * np.cos(angle), P.y + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break
        if ind > 30:
            return d
        ind += 1

    Q_label  = label_point(d)
    new_labels.append(Q_label)
    Q = Point(x1, y1, Q_label)

    #Generate point A, B
    ind = 0
    while True:
        Ax, Ay, B_x, B_y = random_coord(), random_coord(), random_coord(), random_coord()
        if ((Ax - B_x)**2 + (Ay - B_y)**2)**0.5 < 0.9 * length:
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        A_label = label_point(d)
        if A_label not in new_labels:
            new_labels.append(A_label)
            break

    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break

    A = Point(Ax, Ay, A_label)
    B = Point(B_x, B_y, B_label)

    d.points.extend([A, B, Q])
    d.lines.extend([Line(P, Q, '')])
    d.entities.append(('length_12', [P.label, Q.label, A.label, B.label]))

    return d

def C_length_12(d):
    #Line l is longer than the distance of point A and point B
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    while len(d.points) < 1:
        d = add_free_point(d)

    new_labels = []

    #Generate two ends of line l
    P = random.choice(d.points)

    ind = 0
    while True:
        length = random_length()
        angle = random_angle()
        x1, y1 = P.x + length * np.cos(angle), P.y + length * np.sin(angle)
        if assert_coord_in_range(x1, y1):
            break
        if ind > 30:
            return d
        ind += 1

    Q_label  = label_point(d)
    new_labels.append(Q_label)
    Q = Point(x1, y1, Q_label)

    #Generate point A, B
    ind = 0
    while True:
        Ax, Ay, B_x, B_y = random_coord(), random_coord(), random_coord(), random_coord()
        if ((Ax - B_x)**2 + (Ay - B_y)**2)**0.5 < 0.9 * length:
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        A_label = label_point(d)
        if A_label not in new_labels:
            new_labels.append(A_label)
            break

    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break

    A = Point(Ax, Ay, A_label)
    B = Point(B_x, B_y, B_label)

    d.points.extend([A, B, Q])
    d.lines.extend([Line(P, Q, '', color = color)])
    d.entities.append(('C_length_12', [P.label, Q.label, A.label, B.label, color]))

    return d


def length_13(d):
    # All edges in a triangle are all equal
    
    while len(d.points) < 2:
        d = add_free_point(d)

    ind = 0
    while True:
        A, B = random.sample(d.points, 2)
        length = ((A.x - B.x)**2 + (A.y - B.y)**2)**0.5
        angle = random.choice([np.pi/3,(-1)*np.pi/3])
        vec_AB = np.array([B.x - A.x, B.y - A.y])
        vec_AC = rotate_vector(vec_AB, angle)
        C_x, C_y = A.x + vec_AC[0], A.y + vec_AC[1]

        if assert_coord_in_range(C_x, C_y):
            break

        if ind > 100:
            # print(f"x,y : {C_x, C_y}")
            raise NotImplementedError
            # return d
        ind += 1

    C_label = label_point(d)
    C = Point(C_x, C_y, C_label)

    d.points.append(C)
    d.lines.extend([Line(A, B, ''), Line(B, C, ''), Line(C, A, '')])
    d.entities.append(('length_13', [A.label, B.label, C.label]))

    return d


def C_length_13(d):
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    # All edges in a triangle are all equal
    while len(d.points) < 2:
        d = add_free_point(d)

    ind = 0
    while True:
        A, B = random.sample(d.points, 2)
        length = ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5
        angle = random.choice([np.pi / 3, (-1) * np.pi / 3])
        vec_AB = np.array([B.x - A.x, B.y - A.y])
        vec_AC = rotate_vector(vec_AB, angle)
        C_x, C_y = A.x + vec_AC[0], A.y + vec_AC[1]
        if assert_coord_in_range(C_x, C_y):
            break

        if ind > 30:
            return d
        ind += 1

    C_label = label_point(d)
    C = Point(C_x, C_y, C_label)

    d.points.append(C)
    d.lines.extend([Line(A, B, '', color = color), Line(B, C, '', color = color), Line(C, A, '', color = color)])
    d.entities.append(('C_length_13', [A.label, B.label, C.label, color]))

    return d

def length_14_1(d):
    # Two edges in a triangle are equal, #Choose an angle larger than 60 degrees
    while len(d.points) < 2:
        d = add_free_point(d)

    ind = 0
    while True:
        A, B = random.sample(d.points, 2)
        length = ((A.x - B.x)**2 + (A.y - B.y)**2)**0.5
        angle = random.uniform(np.pi * 5/12, np.pi * 19/12)
        vec_AB = np.array([B.x - A.x, B.y - A.y])
        vec_AC = rotate_vector(vec_AB, angle)
        C_x, C_y = A.x + vec_AC[0], A.y + vec_AC[1]
        if assert_coord_in_range(C_x, C_y):
            break

        if ind > 30:
            return d
        ind += 1

    C_label = label_point(d)
    C = Point(C_x, C_y, C_label)

    d.points.append(C)
    d.lines.extend([Line(A, B, ''), Line(B, C, ''), Line(C, A, '')])
    d.entities.append(('length_14_1', [A.label, B.label, C.label])) #A is the pivot (angle) point, BC is the only different length

    return d


def C_length_14_1(d):
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    # All edges in a triangle are all equal
    while len(d.points) < 2:
        d = add_free_point(d)

    ind = 0
    while True:
        A, B = random.sample(d.points, 2)
        length = ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5
        angle = random.uniform(np.pi * 5/12, np.pi * 19/12)
        vec_AB = np.array([B.x - A.x, B.y - A.y])
        vec_AC = rotate_vector(vec_AB, angle)
        C_x, C_y = A.x + vec_AC[0], A.y + vec_AC[1]
        if assert_coord_in_range(C_x, C_y):
            break

        if ind > 30:
            return d
        ind += 1

    C_label = label_point(d)
    C = Point(C_x, C_y, C_label)

    d.points.append(C)
    d.lines.extend([Line(A, B, '', color = color), Line(B, C, '', color = color), Line(C, A, '', color = color)])
    d.entities.append(('C_length_14_1', [A.label, B.label, C.label, color]))

    return d

def length_14_2(d):
    # All edges in a triangle are all equal, #Choose an angle smaller than 60 degrees
    while len(d.points) < 2:
        d = add_free_point(d)





    ind = 0
    while True:
        A, B = random.sample(d.points, 2)
        length = ((A.x - B.x)**2 + (A.y - B.y)**2)**0.5
        angle = random.uniform(-np.pi/4, np.pi/4)
        vec_AB = np.array([B.x - A.x, B.y - A.y])
        vec_AC = rotate_vector(vec_AB, angle)
        C_x, C_y = A.x + vec_AC[0], A.y + vec_AC[1]
        if assert_coord_in_range(C_x, C_y):
            break

        if ind > 30:
            return d
        ind += 1

    C_label = label_point(d)
    C = Point(C_x, C_y, C_label)

    d.points.append(C)
    d.lines.extend([Line(A, B, ''), Line(B, C, ''), Line(C, A, '')])
    d.entities.append(('length_14_2', [A.label, B.label, C.label])) #A is the pivot (angle) point, BC is the only different length

    return d


def C_length_14_2(d):
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    # All edges in a triangle are all equal
    while len(d.points) < 2:
        d = add_free_point(d)

    ind = 0
    while True:
        A, B = random.sample(d.points, 2)
        length = ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5
        angle = random.uniform(-np.pi/4, np.pi/4)
        vec_AB = np.array([B.x - A.x, B.y - A.y])
        vec_AC = rotate_vector(vec_AB, angle)
        C_x, C_y = A.x + vec_AC[0], A.y + vec_AC[1]
        if assert_coord_in_range(C_x, C_y):
            break

        if ind > 30:
            return d
        ind += 1

    C_label = label_point(d)
    C = Point(C_x, C_y, C_label)

    d.points.append(C)
    d.lines.extend([Line(A, B, '', color = color), Line(B, C, '', color = color), Line(C, A, '', color = color)])
    d.entities.append(('C_length_14_2', [A.label, B.label, C.label, color]))

    return d

def length_15(d):
    # ALl edges are clearly not equal in a triangle
    while len(d.points) < 2:
        d = add_free_point(d)

    ind = 0
    while True:
        A, B = random.sample(d.points, 2)
        C_x, C_y = random_coord(), random_coord()
        #Check that AB, BC, CA differ at least by 1.2 each
        #Sort AB, BC, CA by the length
        lengths = sorted([((A.x - B.x)**2 + (A.y - B.y)**2)**0.5, ((B.x - C_x)**2 + (B.y - C_y)**2)**0.5, ((C_x - A.x)**2 + (C_y - A.y)**2)**0.5])
        if lengths[0] < 1.2 * lengths[1] and lengths[1] < 1.2 * lengths[2] and lengths[0] > 100:
            break

        if ind > 100:
            return d
        ind += 1

    C_label = label_point(d)
    C = Point(C_x, C_y, C_label)
    d.points.append(C)
    d.lines.extend([Line(A, B, ''), Line(B, C, ''), Line(C, A, '')])
    d.entities.append(('length_15', [A.label, B.label, C.label]))

    return d

def C_length_15(d):
    # ALl edges are clearly not equal in a triangle
    color = random.choice(d.usable_colors)
    while len(d.points) < 1:
        d = add_free_point(d)

    ind = 0
    while True:
        A= random.choice(d.points)
        B = Point(random_coord(), random_coord(), label_point(d))
        C_x, C_y = random_coord(), random_coord()
        #Check that AB, BC, CA differ at least by 1.2 each
        #Sort AB, BC, CA by the length
        lengths = sorted([((A.x - B.x)**2 + (A.y - B.y)**2)**0.5, ((B.x - C_x)**2 + (B.y - C_y)**2)**0.5, ((C_x - A.x)**2 + (C_y - A.y)**2)**0.5])
        if lengths[0] < 1.2 * lengths[1] and lengths[1] < 1.2 * lengths[2] and lengths[0] > 100:
            break

        if ind > 100:
            return d
        ind += 1

    while True:
        C_label = label_point(d)
        if C_label != B.label:
            break



    C = Point(C_x, C_y, C_label)
    d.points.extend([B, C])
    d.lines.extend([Line(A, B, '',color = color), Line(B, C, '', color = color), Line(C, A, '', color = color)])
    d.entities.append(('C_length_15', [A.label, B.label, C.label, color]))
    return d




def length_16(diagram):
    #Raidus of circle A is longer than the Radius of circle B
 
    while len(diagram.circles) < 1:
        diagram = add_free_circle(diagram)


    circle_A = random.choice(diagram.circles)

    A_radius = circle_A.radius
    
    #Generate B

    B_radius = A_radius * random.uniform(0.3, 0.9)
    ind = 0

    while True:
        B_x, B_y = random_coord(), random_coord()
        if assert_coord_in_range(B_x + B_radius, B_y + B_radius) and assert_coord_in_range(B_x - B_radius, B_y - B_radius):
            break

        ind +=1
        if ind > 100:
            return diagram

    B_label = label_point(diagram)
    B = Point(B_x, B_y, B_label)
    circle_B = Circle(B, B_radius, '')

    diagram.points.append(B)
    diagram.circles.append(circle_B)
    diagram.entities.append(('length_16', [circle_A.center.label, B.label]))
    return diagram

def C_length_16(diagram):
    #Raidus of circle A is longer than the Radius of circle B
    color1, color2 = random.sample(diagram.usable_colors, 2)
    diagram = remove_color(diagram, color1)
    diagram = remove_color(diagram, color2)

    ind = 0
    while True:
        A_radius = random_length()
        x0, y0 = random_coord(), random_coord()
        A_label = label_point(diagram)
        if assert_coord_in_range(x0 + A_radius, y0 + A_radius) and assert_coord_in_range(x0 - A_radius, y0 - A_radius):
            break
        if ind > 100:
            return diagram
        ind += 1 

    new_labels = [A_label]
    A = Point(x0, y0, A_label)
    circle_A = Circle(A, A_radius, '', color = color1)


    #Generate B

    B_radius = A_radius * random.uniform(0.3, 0.9)
    ind = 0
    while True:
        B_x, B_y = random_coord(), random_coord()
        if assert_coord_in_range(B_x + B_radius, B_y + B_radius) and assert_coord_in_range(B_x - B_radius, B_y - B_radius):
            break

        ind +=1
        if ind > 100:
            return diagram

    while True:
        B_label = label_point(diagram)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break
        ind += 1
        if ind > 100:
            return diagram

    B = Point(B_x, B_y, B_label)
    circle_B = Circle(B, B_radius, '', color = color2)

    diagram.points.extend([A, B])
    diagram.circles.extend([circle_A, circle_B])
    diagram.entities.append(('C_length_16', [A_label, B_label, color1, color2]))
    return diagram


def length_17_1(d):
    # Line B is 2 times longer than line A
    while len(d.points) < 2:
        d = add_free_point(d)

    ratio = 2

    ind = 0
    while True:
        A1, A2 = random.sample(d.points, 2)
        length1 = random_length()
        angle1 = random_angle()

        x1, y1 = A1.x + length1 * np.cos(angle1), A1.y + length1 * np.sin(angle1) #line a

        angle_2 = random_angle()
        x2, y2 = A2.x + ratio * length1 * np.cos(angle_2), A2.y + ratio * length1 * np.sin(angle_2)
        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break

        if ind > 100:
            return d
        ind += 1

    B1 = Point(x1, y1, label_point(d))
    B2 = Point(x2, y2, label_point(d))

    d.points.extend([B1, B2])
    d.lines.extend([Line(A1, B1, ''), Line(A2, B2, '')])
    d.entities.append(('length_17_1', [A2.label, B2.label, A1.label, B1.label]))

    return d

def length_17_2(d):
    # Line B is 3 times longer than line A
    while len(d.points) < 2:
        d = add_free_point(d)

    ratio = 3

    ind = 0
    while True:
        A1, A2 = random.sample(d.points, 2)
        length1 = random_length()
        angle1 = random_angle()

        x1, y1 = A1.x + length1 * np.cos(angle1), A1.y + length1 * np.sin(angle1) #line a

        angle_2 = random_angle()
        x2, y2 = A2.x + ratio * length1 * np.cos(angle_2), A2.y + ratio * length1 * np.sin(angle_2)
        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break

        if ind > 100:
            return d
        ind += 1

    B1 = Point(x1, y1, label_point(d))
    B2 = Point(x2, y2, label_point(d))

    d.points.extend([B1, B2])
    d.lines.extend([Line(A1, B1, ''), Line(A2, B2, '')])
    d.entities.append(('length_17_2', [A2.label, B2.label, A1.label, B1.label]))

    return d

def length_17_3(d):
    # Line B is n times longer than line A
    while len(d.points) < 2:
        d = add_free_point(d)

    ratio = random.randint(2, 5)

    ind = 0
    while True:
        A1, A2 = random.sample(d.points, 2)
        length1 = random_length()
        angle1 = random_angle()

        x1, y1 = A1.x + length1 * np.cos(angle1), A1.y + length1 * np.sin(angle1) #line a

        angle_2 = random_angle()
        x2, y2 = A2.x + ratio * length1 * np.cos(angle_2), A2.y + ratio * length1 * np.sin(angle_2)
        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break

        if ind > 100:
            return d
        ind += 1

    B1 = Point(x1, y1, label_point(d))
    B2 = Point(x2, y2, label_point(d))

    d.points.extend([B1, B2])
    d.lines.extend([Line(A1, B1, ''), Line(A2, B2, '')])
    d.entities.append(('length_17_3', [A2.label, B2.label, A1.label, B1.label, ratio]))

    return d


def C_length_17_1(d):
    # Line B is 2 times longer than line A
    color1, color2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, color1)
    d = remove_color(d, color2)


    while len(d.points) < 2:
        d = add_free_point(d)

    ratio = 2

    ind = 0
    while True:
        A1, A2 = random.sample(d.points, 2)
        length1 = random_length()
        angle1 = random_angle()

        x1, y1 = A1.x + length1 * np.cos(angle1), A1.y + length1 * np.sin(angle1) #line a

        angle_2 = random_angle()
        x2, y2 = A2.x + ratio * length1 * np.cos(angle_2), A2.y + ratio * length1 * np.sin(angle_2)
        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break

        if ind > 100:
            return d
        ind += 1

    B1 = Point(x1, y1, label_point(d))
    B2 = Point(x2, y2, label_point(d))

    d.points.extend([B1, B2])
    d.lines.extend([Line(A1, B1, '', color = color1), Line(A2, B2, '', color = color2)])
    d.entities.append(('C_length_17_1', [A2.label, B2.label, A1.label, B1.label, color2, color1]))

    return d

def C_length_17_2(d):
    # Line B is 3 times longer than line A
    color1, color2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, color1)
    d = remove_color(d, color2)


    while len(d.points) < 2:
        d = add_free_point(d)

    ratio = 3

    ind = 0
    while True:
        A1, A2 = random.sample(d.points, 2)
        length1 = random_length()
        angle1 = random_angle()

        x1, y1 = A1.x + length1 * np.cos(angle1), A1.y + length1 * np.sin(angle1) #line a

        angle_2 = random_angle()
        x2, y2 = A2.x + ratio * length1 * np.cos(angle_2), A2.y + ratio * length1 * np.sin(angle_2)
        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break

        if ind > 100:
            return d
        ind += 1

    B1 = Point(x1, y1, label_point(d))
    B2 = Point(x2, y2, label_point(d))

    d.points.extend([B1, B2])
    d.lines.extend([Line(A1, B1, '', color = color1), Line(A2, B2, '', color = color2)])
    d.entities.append(('C_length_17_2', [A2.label, B2.label, A1.label, B1.label, color2, color1]))

    return d

def C_length_17_3(d):
    color1, color2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, color1)
    d = remove_color(d, color2)

    # Line B is n times longer than line A
    while len(d.points) < 2:
        d = add_free_point(d)

    ratio = random.randint(2, 5)

    ind = 0
    while True:
        A1, A2 = random.sample(d.points, 2)
        length1 = random_length()
        angle1 = random_angle()

        x1, y1 = A1.x + length1 * np.cos(angle1), A1.y + length1 * np.sin(angle1) #line a

        angle_2 = random_angle()
        x2, y2 = A2.x + ratio * length1 * np.cos(angle_2), A2.y + ratio * length1 * np.sin(angle_2)
        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break

        if ind > 100:
            return d
        ind += 1

    B1 = Point(x1, y1, label_point(d))
    B2 = Point(x2, y2, label_point(d))

    d.points.extend([B1, B2])
    d.lines.extend([Line(A1, B1, '', color = color1), Line(A2, B2, '', color = color2)])
    d.entities.append(('C_length_17_3', [A2.label, B2.label, A1.label, B1.label, ratio, color2, color1]))

    return d

def length_18(d):
    # Among n lines, the line that is twice as long as the line A is line B.

    ind = 0
    # Generate line A
    while True:
        A1x, A1y = random_coord(), random_coord()
        l = random_length()
        angle = random_angle()
        A2x, A2y = A1x + l * np.cos(angle), A1y + l * np.sin(angle)


        make_non_parallel = random.choice([True, False]) #If true, make all the lines nonparallel
        if make_non_parallel:
            angle = random_angle()


        B1x, B1y = random_coord(), random_coord()
        B2x, B2y = B1x + 2* l * np.cos(angle), B1y + 2 * l * np.sin(angle)

        if assert_coord_in_range(A2x, A2y) and assert_coord_in_range(B2x, B2y):
            break

        if ind > 100:
            return d
        ind += 1

    A1 = Point(A1x, A1y, label_point(d))
    new_labels = [A1.label]
    while True:
        label = label_point(d)
        if label not in new_labels:
            A2 = Point(A2x, A2y, label)
            new_labels.append(label)
            break
    while True:
        label1, label2 = label_point(d), label_point(d)
        if label1 != label2 and label1 not in new_labels:
            B1 = Point(B1x, B1y, label1)
            B2 = Point(B2x, B2y, label2)
            new_labels.extend([label1, label2])
            break


    # Generate other lines
    n = random.randint(1, 3)
    for i in range(n):
        ind = 0
        while True:
            if make_non_parallel:
                angle = random_angle()
            x1, y1 = random_coord(), random_coord()
            if random.choice([True, False]):
                scale = random.uniform(0.5, 1.8)
            else:
                scale = random.uniform(2.2, 3.5)

            x2, y2 = x1 + scale* l * np.cos(angle), y1 + scale * l * np.sin(angle)
            if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
                break

            if ind > 100:
                return d
            ind += 1

        while True:
            label1 = label_point(d)
            label2 = label_point(d)
            if label1 != label2 and label1 not in new_labels:
                new_labels.extend([label1, label2])
                break

        d.points.extend([Point(x1, y1, label1), Point(x2, y2, label2)])
        d.lines.append( Line( Point(x1, y1, label1), Point(x2, y2, label2), label='' ))

    d.points.extend([A1, A2, B1, B2])
    d.lines.extend([Line(A1, A2, ''), Line(B1, B2, '')])
    d.entities.append(('length_18', [A1.label, A2.label, B1.label, B2.label, label1, label2]))

    return d

def C_length_18(d):
    # Among n lines, the line that is twice as long as the line A is line B.
    colorA, colorB = random.sample(d.usable_colors, 2)
    d.usable_colors.remove(colorA)
    d.usable_colors.remove(colorB)

    ind = 0
    # Generate line A
    while True:
        A1x, A1y = random_coord(), random_coord()
        l = random_length()
        angle = random_angle()
        A2x, A2y = A1x + l * np.cos(angle), A1y + l * np.sin(angle)

        make_non_parallel = random.choice([True, False])  # If true, make all the lines nonparallel
        if make_non_parallel:
            angle = random_angle()

        B1x, B1y = random_coord(), random_coord()
        B2x, B2y = B1x + 2 * l * np.cos(angle), B1y + 2 * l * np.sin(angle)

        if assert_coord_in_range(A2x, A2y) and assert_coord_in_range(B2x, B2y):
            break

        if ind > 100:
            return d
        ind += 1

    A1 = Point(A1x, A1y, label_point(d))
    new_labels = [A1.label]
    while True:
        label = label_point(d)
        if label not in new_labels:
            A2 = Point(A2x, A2y, label)
            new_labels.append(label)
            break
    while True:
        label1, label2 = label_point(d), label_point(d)
        if label1 != label2 and label1 not in new_labels:
            B1 = Point(B1x, B1y, label1)
            B2 = Point(B2x, B2y, label2)
            new_labels.extend([label1, label2])
            break

    # Generate other lines
    n = random.randint(1, 3)
    for i in range(n):
        ind = 0
        while True:
            if make_non_parallel:
                angle = random_angle()
            x1, y1 = random_coord(), random_coord()
            if random.choice([True, False]):
                scale = random.uniform(0.5, 1.8)
            else:
                scale = random.uniform(2.2, 3.5)

            x2, y2 = x1 + scale * l * np.cos(angle), y1 + scale * l * np.sin(angle)
            if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
                break

            if ind > 100:
                return d
            ind += 1

        while True:
            label1 = label_point(d)
            label2 = label_point(d)
            if label1 != label2 and label1 not in new_labels:
                new_labels.extend([label1, label2])
                break

        d.points.extend([Point(x1, y1, label1), Point(x2, y2, label2)])
        color = random.choice(d.usable_colors)
        d.usable_colors.remove(color)
        d.lines.append(Line(Point(x1, y1, label1), Point(x2, y2, label2), label = '', color = color))

    d.points.extend([A1, A2, B1, B2])
    d.lines.extend([Line(A1, A2, '', color = colorA), Line(B1, B2, '', color = colorB)])
    d.entities.append(('C_length_18', [A1.label, A2.label, B1.label, B2.label, label1, label2, colorA, colorB, color]))

    return d


def length_20(d):
    #Which is larger : width vs height of the rectangle
    edge_color, fill_color = 'black', random.choice(d.usable_colors)
    d = remove_color(d, fill_color)

    larger_side = random.choice(['width', 'height'])
    while True:
        x1, y1 = random_coord(), random_coord() #bottom left
        width = random_length()
        if larger_side == 'width':
            smaller_side = 'height'
            height = random.uniform(0.2, 0.9) * width
        else:
            smaller_side = 'width'
            height = random.uniform(1.1,5) * width

        x3, y3 = x1 + width, y1 + height
        if assert_coord_in_range(x3, y3):
            break

    x2, y2 = x1, y3
    x4, y4 = x3, y1

    d.polygons.append(polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)], '', 'black' , fill_color))
    d.entities.append(('length_20', [larger_side, fill_color, smaller_side]))
    return d

def length_21(d):
    #Which is tallest / smallest among the circles/rectangles/triangles/bars

    answer_in = random.choice(['color', 'label'])
    target_type = random.choice(['smallest', 'tallest'])
    object_type = random.choice(['circles', 'rectangles', 'triangles','bars']) #'circles', 'rectangles', 'triangles',
    object_counts = random.randint(2, 10)

    #Choose the answer and wrong index
    answer_index = random.randint(0, object_counts-1)
    wrong_index = random.choice([i for i in range(object_counts) if i != answer_index])

    #Choose bottom height
    y_bot = random.uniform(10, 600)

    #Choose top heights
    y_tops  =[]
    radiuses = []


    for _ in range(object_counts-1):
        y_top = random.uniform(y_bot + 100,900)
        y_tops.append(y_top)
        radiuses.append((y_top - y_bot)/2)

    if target_type == 'smallest':
        y_top_answer = random.uniform(y_bot + 50, min(y_tops)-50)
        radius_answer = (y_top_answer - y_bot)/2
    else:
        y_top_answer = random.uniform(max(y_tops)+50, 990)
        radius_answer = (y_top_answer - y_bot)/2

    ind = 0
    #Choose x coordinates
    while True:
        x_lefts = []
        x_rights = []
        x_peaks = []
        x_right = 0
        j = 0
        # Choose width
        width = random.uniform(50, 200)
        for i in range(object_counts):
            if object_type == 'bars':

                x_left = random.uniform(x_right + 10, x_right + 200)
                x_right = x_left + width
                x_lefts.append(x_left)
                x_rights.append(x_right)

            elif object_type == 'rectangles':
                width = random.uniform(50, 300)
                x_left = random.uniform(x_right + 10, x_right + 200)
                x_right = x_left + width
                x_lefts.append(x_left)
                x_rights.append(x_right)

            elif object_type == 'triangles':
                width = random.uniform(50, 200)
                x_left = random.uniform(x_right + 10, x_right + 200)
                x_right = x_left + width
                x_lefts.append(x_left)
                x_rights.append(x_right)

                x_peaks.append(random.uniform(x_left, x_right))

            elif object_type == 'circles':
                x_left = random.uniform(x_right + 10, x_right + 200)
                if i == answer_index:
                    x_right = x_left + 2 * radius_answer
                else:
                    x_right = x_left + 2 * radiuses[j]
                    j += 1


                x_lefts.append(x_left)
                x_rights.append(x_right)





        if assert_coord_in_range(x_rights[-1], y_bot):
            break

        if ind > 100:
            return d
        ind += 1

    #Choose colors
    use_black_edge = random.choice([True, False])
    color_pair_list = random.sample(color_pairs.candidates, object_counts)
    


    #If answering in label, you must add label. Otherwise, randomly choose to add label or not
    if answer_in == 'label' or random.choice([True, False]):
        labels = random.sample(capitals.candidates, object_counts)
    else:
        labels = []

    i, j = 0, 0
    
    while len(d.polygons) < object_counts and len(d.filled_circles) < object_counts:
        # print(f"color: {color_pair_list[len(d.polygons)]}")
        if object_type == 'bars':
            if len(d.polygons) == answer_index:
                d.polygons.append(polygon([(x_lefts[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_top_answer), (x_lefts[len(d.polygons)], y_top_answer)], '' if len(labels) == 0 else labels[len(d.polygons)], edge_color='black' if use_black_edge else color_pair_list[len(d.polygons)][0], fill_color=color_pair_list[len(d.polygons)][1]))

            else:
                d.polygons.append(polygon([(x_lefts[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_tops[j]), (x_lefts[len(d.polygons)], y_tops[j])], '' if len(labels) == 0 else labels[len(d.polygons)], edge_color='black' if use_black_edge else color_pair_list[len(d.polygons)][0], fill_color=color_pair_list[len(d.polygons)][1]))
                j += 1

        elif object_type == 'rectangles':
            if len(d.polygons) == answer_index:
                d.polygons.append(polygon([(x_lefts[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_top_answer), (x_lefts[len(d.polygons)], y_top_answer)], '' if len(labels) == 0 else labels[len(d.polygons)], edge_color='black' if use_black_edge else color_pair_list[len(d.polygons)][0], fill_color=color_pair_list[len(d.polygons)][1]))

            else:
                d.polygons.append(polygon([(x_lefts[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_tops[j]), (x_lefts[len(d.polygons)], y_tops[j])], '' if len(labels) == 0 else labels[len(d.polygons)], edge_color='black' if use_black_edge else color_pair_list[len(d.polygons)][0], fill_color=color_pair_list[len(d.polygons)][1]))
                j += 1

        elif object_type == 'triangles':
            if len(d.polygons) == answer_index:
                d.polygons.append(polygon([(x_lefts[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_bot), (x_peaks[len(d.polygons)], y_top_answer)], '' if len(labels) == 0 else labels[len(d.polygons)], edge_color='black' if use_black_edge else color_pair_list[len(d.polygons)][0], fill_color=color_pair_list[len(d.polygons)][1]))

            else:
                d.polygons.append(polygon([(x_lefts[len(d.polygons)], y_bot), (x_rights[len(d.polygons)], y_bot), (x_peaks[len(d.polygons)], y_tops[j])], '' if len(labels) == 0 else labels[len(d.polygons)], edge_color='black' if use_black_edge else color_pair_list[len(d.polygons)][0], fill_color=color_pair_list[len(d.polygons)][1]))
                j += 1

        elif object_type == 'circles':
            if len(d.filled_circles) == answer_index:
                d.filled_circles.append(filled_circle((x_lefts[len(d.filled_circles)] + radius_answer, y_bot + radius_answer), radius_answer, '' if len(labels) == 0 else labels[len(d.filled_circles)], edge_color='black' if use_black_edge else color_pair_list[len(d.filled_circles)][0], fill_color=color_pair_list[len(d.filled_circles)][1]))
            else:
                # print(f"answer index: {answer_index}, j: {j}, len(d.filled_circles): {len(d.filled_circles)}, len(radiuses): {len(radiuses)}, len(x_lefts): {len(x_lefts)}, len(x_rights): {len(x_rights)}, len(color_pair_list): {len(color_pair_list)}")
                d.filled_circles.append(filled_circle((x_lefts[len(d.filled_circles)] + radiuses[j], y_bot + radiuses[j] ),  radiuses[j], '' if len(labels) == 0 else labels[len(d.filled_circles)], edge_color='black' if use_black_edge else color_pair_list[len(d.filled_circles)][0], fill_color=color_pair_list[len(d.filled_circles)][1]))
                j += 1


    if answer_in == 'color':
        candidates = ""
        for i in range(object_counts):
            candidates += color_pair_list[i][1] + ', '
        candidates = candidates[:-2]
    else:
        candidates = ""
        for i in range(object_counts):
            candidates += labels[i] + ', '
        candidates = candidates[:-2]

    if answer_in == 'color':
        d.entities.append((f'length_21_color_{target_type}', [object_type[:-1], candidates, color_pair_list[answer_index][1], color_pair_list[wrong_index][1]])) #, len(d.polygons), object_counts, color_pair_list, labels]))
    else:
        d.entities.append((f'length_21_label_{target_type}', [object_type[:-1], candidates, labels[answer_index], labels[wrong_index]]))#, len(d.polygons), object_counts, color_pair_list, labels]))


  
    #target type : smallest, tallest
    #object type : circles, rectangles, triangles, bars
    #answer_in : color, label
    #answer_index + 1: index of the answer
    #color_pairs[answer_index][1] : color of the answer

    d.points = []
    d.lines = []
    d.circles = []

    if random.choice([True, False]):
        d.lines.append(Line(Point(0, y_bot-2, ''), Point(1000, y_bot-2, ''), '', color = random.choice(d.usable_colors)))
    
    return d