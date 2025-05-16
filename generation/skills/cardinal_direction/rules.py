'''
유형
(1) 좌, 우 중 한 object가 다른 object 기준 어느 쪽에 위치하는지 판단하는 문제
(2) 상, 하 중 한 object가 다른 object 기준 어느 쪽에 위치하는지 판단하는 문제
(3) 좌상, 우상, 좌하, 우하 중 한 object가 다른 object 기준 어느 쪽에 위치하는지 판단하는 문제
(4) 어느 object가 다른 것 기준 특정 방향에 위치하는지 판단하는 문제(좌, 우)
(5) 어느 object가 다른 것 기준 특정 방향에 위치하는지 판단하는 문제(상, 하)
(6) 어느 object가 다른 것 기준 특정 방향에 위치하는지 판단하는 문제(좌상, 우상, 좌하, 우하)

object
(1) 점
(2) 선
(3) 원

others
prompt의 형태를 (word1/word2/.../wordn)으로 나타내면, word1, word2, ..., wordn 중 하나를 선택하여 prompt에 넣는 형태도 시도해볼 수 있을 것 같다.
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

# return a function that adds two objects(points, lines, or circles) to the diagram
# one of new objects should be clearly on the specified side of the other object
def card_direction(xdir=None, ydir=None, task_name=None, colored=False):
    assert xdir in ['left', 'right', None]
    assert ydir in ['top', 'bottom', None]
    assert not (xdir is None and ydir is None)
    
    def f(d):
        x1_boundary_range = (100, 900)
        y1_boundary_range = (100, 900)
        x1_boundary_coord = random_coord(*x1_boundary_range)
        y1_boundary_coord = random_coord(*y1_boundary_range)

        if xdir == 'left':
            x2_boundary_range = (90, x1_boundary_coord - 5)
        elif xdir == 'right':
            x2_boundary_range = (x1_boundary_coord + 5, 910)
        else:
            x2_boundary_range = (90, 910)
        
        if ydir == 'top':
            y2_boundary_range = (y1_boundary_coord + 5, 910)
        elif ydir == 'bottom':
            y2_boundary_range = (90, y1_boundary_coord - 5)
        else:
            y2_boundary_range = (90, 910)
        
        x2_boundary_coord = random_coord(*x2_boundary_range)
        y2_boundary_coord = random_coord(*y2_boundary_range)

        obj1_type = random.choice(['point', 'line', 'circle'])
        obj2_type = random.choice(['point', 'line', 'circle'])
        obj1_color = None
        obj2_color = None
        if colored:
            obj1_color = random.choice(d.usable_colors)
            d = remove_color(d, obj1_color)
            obj2_color = random.choice(d.usable_colors)
            d = remove_color(d, obj2_color)

        if obj1_type == 'point':
            # obj1 point label
            label1 = label_point(d)
            point1 = Point(x1_boundary_coord, y1_boundary_coord, label1, color = obj1_color if colored else 'black')
            d.points.append(point1)
        elif obj1_type == 'line':
            if xdir == 'left':
                x1_secondary_coord = random_coord(x1_boundary_coord + 40, 990)
            elif xdir == 'right':
                x1_secondary_coord = random_coord(10, x1_boundary_coord - 40)
            else:
                x1_secondary_coord = random_coord(10, 990)

            if ydir == 'top':
                y1_secondary_coord = random_coord(10, y1_boundary_coord - 40)
            elif ydir == 'bottom':
                y1_secondary_coord = random_coord(y1_boundary_coord + 40, 990)
            else:
                y1_secondary_coord = random_coord(10, 990)

            label11 = label_point(d)
            point11 = Point(x1_boundary_coord, y1_boundary_coord, label11)
            label12 = label_point(d)
            point12 = Point(x1_secondary_coord, y1_secondary_coord, label12)
            # obj1 line label
            label1 = label11 + label12            
            d.points.append(point11)
            d.points.append(point12)
            d.lines.append(Line(point11, point12, label1, color = obj1_color if colored else 'black'))
        elif obj1_type == 'circle':
            # obj1 circle label
            label1 = label_point(d)
            if xdir == 'left':
                x1_circle_radius = random.uniform(40, (990-x1_boundary_coord)/2)
                x1_center_coord = x1_boundary_coord + x1_circle_radius
            elif xdir == 'right':
                x1_circle_radius = random.uniform(40, (x1_boundary_coord-10)/2)
                x1_center_coord = x1_boundary_coord - x1_circle_radius
            else:
                x1_circle_radius = random.uniform(40, min(x1_boundary_coord-10, 990-x1_boundary_coord)/2)
                circle_direction = random.choice([-1, 1])
                x1_center_coord = x1_boundary_coord + circle_direction * x1_circle_radius

 
            if ydir == 'top':
                y1_circle_radius = random.uniform(40, (y1_boundary_coord-10)/2)
                y1_center_coord = y1_boundary_coord - y1_circle_radius
            elif ydir == 'bottom':
                y1_circle_radius = random.uniform(40, (990-y1_boundary_coord)/2)
                y1_center_coord = y1_boundary_coord + y1_circle_radius
            else:
                y1_circle_radius = random.uniform(40, min(y1_boundary_coord-10, 990-y1_boundary_coord)/2)
                circle_direction = random.choice([-1, 1])
                y1_center_coord = y1_boundary_coord + circle_direction * y1_circle_radius

            center = Point(x1_center_coord, y1_center_coord, label1)
            d.points.append(center)
            d.circles.append(Circle(center, x1_circle_radius, label1, color = obj1_color if colored else 'black'))

        if obj2_type == 'point':
            # obj2 point label
            label2 = label_point(d)
            point2 = Point(x2_boundary_coord, y2_boundary_coord, label2, color = obj2_color if colored else 'black')
            d.points.append(point2)
        elif obj2_type == 'line':
            if xdir == 'left':
                x2_secondary_coord = random_coord(10, x2_boundary_coord - 40)
            elif xdir == 'right':
                x2_secondary_coord = random_coord(x2_boundary_coord + 40, 990)
            else:
                x2_secondary_coord = random_coord(10, 990)

            if ydir == 'top':
                y2_secondary_coord = random_coord(y2_boundary_coord + 40, 990)
            elif ydir == 'bottom':
                y2_secondary_coord = random_coord(10, y2_boundary_coord - 40)
            else:
                y2_secondary_coord = random_coord(10, 990)

            label21 = label_point(d)
            point21 = Point(x2_boundary_coord, y2_boundary_coord, label21)
            label22 = label_point(d)
            point22 = Point(x2_secondary_coord, y2_secondary_coord, label22)
            # obj2 line label
            label2 = label21 + label22
            d.points.append(point21)
            d.points.append(point22)
            d.lines.append(Line(point21, point22, label2, color = obj2_color if colored else 'black'))
        elif obj2_type == 'circle':
            # obj2 circle label
            label2 = label_point(d)
            if xdir == 'left':
                x2_circle_radius = random.uniform(40, (x2_boundary_coord-10)/2)
                x2_center_coord = x2_boundary_coord - x2_circle_radius
            elif xdir == 'right':
                x2_circle_radius = random.uniform(40, (990-x2_boundary_coord)/2)
                x2_center_coord = x2_boundary_coord + x2_circle_radius
            else:
                x2_circle_radius = random.uniform(40, min(x2_boundary_coord-10, 990-x2_boundary_coord)/2)
                circle_direction = random.choice([-1, 1])
                x2_center_coord = x2_boundary_coord + circle_direction * x2_circle_radius

 
            if ydir == 'top':
                y2_circle_radius = random.uniform(40, (990-y2_boundary_coord)/2)
                y2_center_coord = y2_boundary_coord + y2_circle_radius
            elif ydir == 'bottom':
                y2_circle_radius = random.uniform(40, (y2_boundary_coord-10)/2)
                y2_center_coord = y2_boundary_coord - y2_circle_radius
            else:
                y2_circle_radius = random.uniform(40, min(y2_boundary_coord-10, 990-y2_boundary_coord)/2)
                circle_direction = random.choice([-1, 1])
                y2_center_coord = y2_boundary_coord + circle_direction * y2_circle_radius

            center = Point(x2_center_coord, y2_center_coord, label2)
            d.points.append(center)
            d.circles.append(Circle(center, x2_circle_radius, label2, color = obj2_color if colored else 'black'))

        d.entities.append((task_name, [obj2_type, obj1_type, label2, label1, xdir, ydir, obj2_color, obj1_color]))
        return d
    return f

rules = [
    card_direction('right', None, 'cardinal_direction_dir_horizontal'),
    card_direction('left', None, 'cardinal_direction_dir_horizontal'),
    card_direction(None, 'top', 'cardinal_direction_dir_vertical'),
    card_direction(None, 'bottom', 'cardinal_direction_dir_vertical'),
    card_direction('right', 'top', 'cardinal_direction_dir_both'),
    card_direction('left', 'top', 'cardinal_direction_dir_both'),
    card_direction('right', 'bottom', 'cardinal_direction_dir_both'),
    card_direction('left', 'bottom', 'cardinal_direction_dir_both'),
    card_direction('right', None, 'cardinal_direction_dir_horizontal', colored=True),
    card_direction('left', None, 'cardinal_direction_dir_horizontal', colored=True),
    card_direction(None, 'top', 'cardinal_direction_dir_vertical', colored=True),
    card_direction(None, 'bottom', 'cardinal_direction_dir_vertical', colored=True),
    card_direction('right', 'top', 'cardinal_direction_dir_both', colored=True),
    card_direction('left', 'top', 'cardinal_direction_dir_both', colored=True),
    card_direction('right', 'bottom', 'cardinal_direction_dir_both', colored=True),
    card_direction('left', 'bottom', 'cardinal_direction_dir_both', colored=True),
    card_direction('right', None, 'cardinal_direction_obj_horizontal'),
    card_direction('left', None, 'cardinal_direction_obj_horizontal'),
    card_direction(None, 'top', 'cardinal_direction_obj_vertical'),
    card_direction(None, 'bottom', 'cardinal_direction_obj_vertical'),
    card_direction('right', 'top', 'cardinal_direction_obj_both'),
    card_direction('left', 'top', 'cardinal_direction_obj_both'),
    card_direction('right', 'bottom', 'cardinal_direction_obj_both'),
    card_direction('left', 'bottom', 'cardinal_direction_obj_both'),
    card_direction('right', None, 'cardinal_direction_obj_horizontal', colored=True),
    card_direction('left', None, 'cardinal_direction_obj_horizontal', colored=True),
    card_direction(None, 'top', 'cardinal_direction_obj_vertical', colored=True),
    card_direction(None, 'bottom', 'cardinal_direction_obj_vertical', colored=True),
    card_direction('right', 'top', 'cardinal_direction_obj_both', colored=True),
    card_direction('left', 'top', 'cardinal_direction_obj_both', colored=True),
    card_direction('right', 'bottom', 'cardinal_direction_obj_both', colored=True),
    card_direction('left', 'bottom', 'cardinal_direction_obj_both', colored=True),
]