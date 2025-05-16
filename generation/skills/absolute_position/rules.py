'''
유형
(1) 좌, 우 중 어느 쪽에 위치하는지 판단하는 문제
(2) 위, 아래 중 어느 쪽에 위치하는지 판단하는 문제
(3) 좌상, 우상, 좌하, 우하 중 어느 쪽에 위치하는지 판단하는 문제

object
(1) 점
(2) 선
(3) 원
'''
from .labels import capitals, small_letters, small_letters_nonempty

import random
import math
import numpy as np

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




#Diagram definition
class Diagram:
    def __init__(self):
        self.points = []
        self.lines = []
        self.circles = []
        self.triangles = []
        self.squares = []
        self.steps = []
        self.entities = []
        self.perpendiculars = []
        self.curves = []
        self.angles = []
        self.usable_colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'yellow']

        # for line in self.lines:
        #     for point in line.passing_points:
        #         assert point in self.points
        #
        # for triangle in self.triangles:
        #     for point in triangle.vertices:
        #         assert point in self.points

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
        if ind > 200:
            raise ValueError(f'No possible label found with currently {len(diagram.points)} points of list : {[point.label for point in diagram.points]}')


        ind+=1


def label_line(diagram):
    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label == "" or (label not in [line.label for line in diagram.lines]):
            return label
        if ind > 200:
            raise ValueError(f'No possible label found with currently {len(diagram.lines)} lines of list : {[line.label for line in diagram.lines]}')
        ind += 1

def label_line_nonempty(diagram):
    ind = 0
    while True:
        label = random.choice(small_letters_nonempty.candidates)
        if (label not in [line.label for line in diagram.lines]):
            return label
        if ind > 200:
            raise ValueError(f'No possible label found with currently {len(diagram.lines)} lines of list : {[line.label for line in diagram.lines]}')
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




#Diagram definition
class Diagram:
    def __init__(self):
        self.points = []
        self.lines = []
        self.circles = []
        self.triangles = []
        self.squares = []
        self.steps = []
        self.entities = []
        self.perpendiculars = []
        self.curves = []
        self.angles = []
        self.usable_colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'yellow']

        # for line in self.lines:
        #     for point in line.passing_points:
        #         assert point in self.points
        #
        # for triangle in self.triangles:
        #     for point in triangle.vertices:
        #         assert point in self.points
    def reset(self):
        self.points = []
        self.lines = []
        self.circles = []
        self.triangles = []
        self.squares = []
        self.steps = []
        self.entities = []
        self.perpendiculars = []
        self.curves = []
        self.angles = []



def normalize(vector):
    (x, y) = vector
    magnitude = (x**2 + y**2)**0.5
    return (x / magnitude, y / magnitude)

def assert_coord_in_range(x,y, xlim=(0, 1000), ylim=(0, 1000)):
    return xlim[0] <= x <= xlim[1] and ylim[0] <= y <= ylim[1]

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
    print(f"diagram.usable_colors : {diagram.usable_colors}")
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
                raise ValueError('No possible line found')
            elif already_in: print('already in')
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
                raise ValueError('No possible line found')
            elif already_in: print('already in')
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
        if ind> 30:
            return d
        ind += 1

    d.points.append(center)
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

## Functions used in the rules

def abs_position(xdir=None, ydir=None):
    if xdir == 'left':
        x_coord_range = (10, 490)
    elif xdir == 'right':
        x_coord_range = (510, 990)
    else:
        x_coord_range = (10, 990)
    if ydir == 'top':
        y_coord_range = (510, 990)
    elif ydir == 'bottom':
        y_coord_range = (10, 490)
    else:
        y_coord_range = (10, 990)

    def f(d):
        x = random_coord(*x_coord_range)
        y = random_coord(*y_coord_range)
        label = label_point(d)
        point = Point(x, y, label)
        d.points.append(point)
        d.entities.append(('abs_position', [label], xdir, ydir))
        return d
    return f

def C_abs_position(xdir=None, ydir=None):
    if xdir == 'left':
        x_coord_range = (10, 490)
    elif xdir == 'right':
        x_coord_range = (510, 990)
    else:
        x_coord_range = (10, 990)
    if ydir == 'top':
        y_coord_range = (510, 990)
    elif ydir == 'bottom':
        y_coord_range = (10, 490)
    else:
        y_coord_range = (10, 990)

    def f(d):
        color = random.choice(d.usable_colors)
        d = remove_color(d, color)
        x = random_coord(*x_coord_range)
        y = random_coord(*y_coord_range)
        label = label_point(d)
        point = Point(x, y, label, color = color)
        d.points.append(point)
        d.entities.append(('C_abs_position', [label, color], xdir, ydir))
        return d
    return f

def abs_position_line(xdir=None, ydir=None):
    if xdir == 'left':
        x_coord_range = (10, 490)
    elif xdir == 'right':
        x_coord_range = (510, 990)
    else:
        x_coord_range = (10, 990)
    if ydir == 'top':
        y_coord_range = (510, 990)
    elif ydir == 'bottom':
        y_coord_range = (10, 490)
    else:
        y_coord_range = (10, 990)

    def f(d):
        x1 = random_coord(*x_coord_range)
        y1 = random_coord(*y_coord_range)
        x2 = random_coord(*x_coord_range)
        y2 = random_coord(*y_coord_range)
        label1 = label_point(d)
        point1 = Point(x1, y1, label1)
        d.points.append(point1)
        label2 = label_point(d)
        point2 = Point(x2, y2, label2)
        d.points.append(point2)
        line = Line(point1, point2, label_line(d))
        d.lines.append(line)
        d.entities.append(('abs_position_line', [label1, label2], xdir, ydir))
        return d
    return f

def C_abs_position_line(xdir=None, ydir=None):
    if xdir == 'left':
        x_coord_range = (10, 490)
    elif xdir == 'right':
        x_coord_range = (510, 990)
    else:
        x_coord_range = (10, 990)
    if ydir == 'top':
        y_coord_range = (510, 990)
    elif ydir == 'bottom':
        y_coord_range = (10, 490)
    else:
        y_coord_range = (10, 990)
    def f(d):
        color = random.choice(d.usable_colors)
        d = remove_color(d, color)
        x1 = random_coord(*x_coord_range)
        y1 = random_coord(*y_coord_range)
        x2 = random_coord(*x_coord_range)
        y2 = random_coord(*y_coord_range)
        label1 = label_point(d)
        point1 = Point(x1, y1, label1)
        d.points.append(point1)
        label2 = label_point(d)
        point2 = Point(x2, y2, label2)
        d.points.append(point2)
        line = Line(point1, point2, label_line(d), color = color)
        d.lines.append(line)
        d.entities.append(('C_abs_position_line', [label1, label2, color], xdir, ydir))
        return d
    return f

def abs_position_circle(xdir=None, ydir=None):
    # The entire circle should be in the specified region
    if xdir == 'left':
        x_coord_range = (50, 450)
    elif xdir == 'right':
        x_coord_range = (550, 950)
    else:
        x_coord_range = (50, 950)
    if ydir == 'top':
        y_coord_range = (550, 950)
    elif ydir == 'bottom':
        y_coord_range = (50, 450)
    else:
        y_coord_range = (50, 950)
    def f(d):
        x = random_coord(*x_coord_range)
        y = random_coord(*y_coord_range)
        center = Point(x, y, label_point(d))
        d.points.append(center)
        max_rad = min(center.x - x_coord_range[0], x_coord_range[1] - center.x, center.y - y_coord_range[0], y_coord_range[1] - center.y)
        radius = random.uniform(50, max_rad)
        circle = Circle(center, radius, '')
        d.circles.append(circle)
        d.entities.append(('abs_position_circle', [center.label], xdir, ydir))
        return d
    return f

def C_abs_position_circle(xdir=None, ydir=None):
    # The entire circle should be in the specified region
    if xdir == 'left':
        x_coord_range = (50, 450)
    elif xdir == 'right':
        x_coord_range = (550, 950)
    else:
        x_coord_range = (50, 950)
    if ydir == 'top':
        y_coord_range = (550, 950)
    elif ydir == 'bottom':
        y_coord_range = (50, 450)
    else:
        y_coord_range = (50, 950)
    def f(d):
        color = random.choice(d.usable_colors)
        d = remove_color(d, color)
        x = random_coord(*x_coord_range)
        y = random_coord(*y_coord_range)
        center = Point(x, y, label_point(d))
        d.points.append(center)
        max_rad = min(center.x - x_coord_range[0], x_coord_range[1] - center.x, center.y - y_coord_range[0], y_coord_range[1] - center.y)
        radius = random.uniform(50, max_rad)
        circle = Circle(center, radius, '', color = color)
        d.circles.append(circle)
        d.entities.append(('C_abs_position_circle', [center.label, color], xdir, ydir))
        return d
    return f


def abs_position_object(task_name=None, colored=False, quadrant_mode=False):
    # add a point, line, or circle (randomly) to each position(center and four corners)
    def f(d):
        if not quadrant_mode:
            positions_coord = {
            'left': (150, 500),
            'right': (500, 850),
            'top': (150, 500),
            'bottom': (500, 850),
            'center': (500, 500),
            'top right': (850, 850),
            'top left': (150, 850),
            'bottom right': (850, 150),
            'bottom left': (150, 150)
            }
            coord_var_limit = 100
        else:
            positions_coord = {
                'top right': (750, 750),
                'top left': (250, 750),
                'bottom right': (750, 250),
                'bottom left': (250, 250)
            }
            coord_var_limit = 240
        # randomly select positions to add objects (select each position with 80% chance)
        # if no position is selected, add objects to all positions
        selected_positions = []
        objects = []
        for position, _ in positions_coord.items():
            if random.random() < 0.8:
                selected_positions.append(position)
        if len(selected_positions) <= 1:
            selected_positions = list(positions_coord.keys())

        answer_position = random.choice(selected_positions)
        answer_obj_type = None
        answer_label = None
        answer_color = None
        answer_index = -1

        for position in selected_positions:
            obj_type = random.choice(['point', 'line', 'circle'])
            color = 'black'
            if colored:
                color = random.choice(d.usable_colors)
                d = remove_color(d, color)
            if obj_type == 'point':
                x, y = positions_coord[position] + np.random.uniform(-coord_var_limit, coord_var_limit, 2)
                label = label_point(d)
                d.points.append(Point(x, y, label))
            elif obj_type == 'line':
                x1, y1 = positions_coord[position] + np.random.uniform(-(coord_var_limit-50), (coord_var_limit-50), 2)
                # x2, y2 should have at least 50 distance from x1, y1
                x2, y2 = x1, y1
                while abs(x2 - x1) < 50:
                    x2 = x1 + np.random.uniform(-coord_var_limit, coord_var_limit)
                while abs(y2 - y1) < 50:
                    y2 = y1 + np.random.uniform(-coord_var_limit, coord_var_limit)
                label1 = label_point(d)
                point1 = Point(x1, y1, label1)
                label2 = label_point(d)
                point2 = Point(x2, y2, label2)
                label = label1 + label2
                d.points.append(point1)
                d.points.append(point2)
                d.lines.append(Line(point1, point2, label, color = color if colored else 'black'))
            elif obj_type == 'circle':
                x, y = positions_coord[position] + np.random.uniform(-(coord_var_limit-50), (coord_var_limit-50), 2)
                label = label_point(d)
                center = Point(x, y, label)
                max_rad = min(
                    center.x-positions_coord[position][0]+coord_var_limit,
                    positions_coord[position][0]+coord_var_limit-center.x,
                    center.y-positions_coord[position][1]+coord_var_limit,
                    positions_coord[position][1]+coord_var_limit-center.y
                )
                radius = random.uniform(50, max_rad)
                d.points.append(center)
                d.circles.append(Circle(center, radius, label, color = color if colored else 'black'))
            objects.append((obj_type, position, label, color))
            if position == answer_position:
                answer_obj_type = obj_type
                answer_label = label
                answer_color = color
                answer_index = len(objects) - 1
        d.entities.append((task_name, objects, (answer_obj_type, answer_position, answer_label, answer_color, answer_index)))
        return d
    return f



rules = [
    abs_position('right', None),
    abs_position('left', None),
    abs_position(None, 'top'),
    abs_position(None, 'bottom'),
    abs_position('right', 'top'),
    abs_position('left', 'top'),
    abs_position('right', 'bottom'),
    abs_position('left', 'bottom'),
    abs_position_line('right', None),
    abs_position_line('left', None),
    abs_position_line(None, 'top'),
    abs_position_line(None, 'bottom'),
    abs_position_line('right', 'top'),
    abs_position_line('left', 'top'),
    abs_position_line('right', 'bottom'),
    abs_position_line('left', 'bottom'),
    abs_position_circle('right', None),
    abs_position_circle('left', None),
    abs_position_circle(None, 'top'),
    abs_position_circle(None, 'bottom'),
    abs_position_circle('right', 'top'),
    abs_position_circle('left', 'top'),
    abs_position_circle('right', 'bottom'),
    abs_position_circle('left', 'bottom'),
    C_abs_position('right', None),
    C_abs_position('left', None),
    C_abs_position(None, 'top'),
    C_abs_position(None, 'bottom'),
    C_abs_position('right', 'top'),
    C_abs_position('left', 'top'),
    C_abs_position('right', 'bottom'),
    C_abs_position('left', 'bottom'),
    C_abs_position_line('right', None),
    C_abs_position_line('left', None),
    C_abs_position_line(None, 'top'),
    C_abs_position_line(None, 'bottom'),
    C_abs_position_line('right', 'top'),
    C_abs_position_line('left', 'top'),
    C_abs_position_line('right', 'bottom'),
    C_abs_position_line('left', 'bottom'),
    C_abs_position_circle('right', None),
    C_abs_position_circle('left', None),
    C_abs_position_circle(None, 'top'),
    C_abs_position_circle(None, 'bottom'),
    C_abs_position_circle('right', 'top'),
    C_abs_position_circle('left', 'top'),
    C_abs_position_circle('right', 'bottom'),
    C_abs_position_circle('left', 'bottom'),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object', colored=False, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_colored', colored=True, quadrant_mode=False),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_quadrant', colored=False, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
    abs_position_object(f'abs_position_object_colored_quadrant', colored=True, quadrant_mode=True),
]