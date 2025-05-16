import numpy as np
import random 
from .labels import *

def label_point(diagram, labeltype='capitals'):
    ind = 0
    if labeltype == 'capitals' :
        candidates = capitals.candidates 
    elif labeltype == 'nums' :
        candidates = nums.candidates 

    while True:
        label = random.choice(candidates)
        if label not in [each.label for each in diagram.points + diagram.fakepoints]:
            return label
        if ind > 200:
            raise ValueError(f'No possible label found with currently {len(diagram.points)} points of list : {[point.label for point in diagram.points]}')
        ind+=1

def label_line(diagram): 
    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label not in [line.label for line in diagram.lines]:
            return label
        if ind > 200:
            raise ValueError(f'No possible label found with currently {len(diagram.lines)} points of list : {[line.label for line in diagram.lines]}')
        ind+=1

#Objects definition
class Point:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.coord = (x,y)
        self.label = label

    def __str__(self):
        return f'Point({self.x}, {self.y}, {self.label})'
    
class FakePoint:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.coord = (x,y)
        self.label = label

    def __str__(self):
        return f'FakePoint({self.x}, {self.y}, {self.label})'

class Line:
    def __init__(self, point1 : Point, point2 : Point, label, infinite=False, tickmarks = 0, dotted = False):
        self.passing_points = [point1, point2]
        self.point1     = point1
        self.point2     = point2
        self.label      = label
        self.infinite   = infinite
        self.tickmarks  = tickmarks
        self.dotted     = dotted

    def __str__(self):
        return f'Line({self.passing_points}, {self.label}, {self.infinite})'

class Circle:
    def __init__(self, center, radius, label):
        self.center = center
        self.radius = radius
        self.label = label

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
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def __str__(self):
        return f'Curve({self.label})'

#Diagram definition
class Diagram:
    def __init__(self, points=[], fakepoints=[], lines=[], circles=[], triangles=[], squares=[], steps=[]):
        self.points     = points
        self.fakepoints = fakepoints 
        self.coloredpoints = []
        self.lines      = lines
        self.circles    = circles
        self.triangles  = triangles
        self.squares    = squares
        self.steps      = steps
        self.entities   = []
        self.perpendiculars = []
        self.curves     = []
        self.angles     = []
        self.polygons   = []
        self.coloredpolygons   = []
        
        self.colored = False

def add_point_at_position (diagram, point_pos, labeltype) : 
    point_label = label_point(diagram, labeltype)
    point       = Point(point_pos[0], point_pos[1], point_label)
    diagram.points.append(point)
    return diagram, point
    
def add_fakepoint_at_position (diagram, point_pos, labeltype) : 
    fakepoint_label = label_point(diagram, labeltype) 
    fakepoint       = FakePoint(point_pos[0], point_pos[1], fakepoint_label)
    diagram.fakepoints.append(fakepoint)
    return diagram, fakepoint

def point_1(diagram: Diagram):
    # print('point_1 is called')

    num_labels = 5
    answer_idx = np.random.choice(np.arange(num_labels))
    point1s = []

    labeltype = random.choice(['capitals', 'nums'])

    for idx in range(num_labels):
        
        point1_pos = np.random.uniform(100, 900, 2)

        if idx == answer_idx:
            diagram, point1 = add_fakepoint_at_position(diagram, point1_pos, labeltype=labeltype)
        else:
            diagram, point1 = add_point_at_position(diagram, point1_pos, labeltype=labeltype)

        # print('num points :', len(diagram.points), ', num fakepoints :', len(diagram.fakepoints))
        point1s.append(point1)

    diagram.entities.append(('point_1', [p.label for p in point1s] + [point1s[answer_idx].label]))

    return diagram


def point_2 (diagram : Diagram ) : 

    "The only point in the picture is labeled with the number right below it. Which number denotes the label of the only point in the picture?"
    "In the given picture, there are five points and six numbers, meaning that one of the six numbers does not have a corresponding point. Identify the number that does not have a corresponding point."
    
    # print('point_2 is called')

    num_labels  = 5
    answer_idx  = np.random.choice(np.arange(num_labels))
    point1s     = []

    labeltype = random.choice(['capitals', 'nums'])
    
    for idx in range(num_labels): 
        point1_pos      = np.random.uniform(100, 900, 2)
        if (idx == answer_idx) : 
            diagram, point1  = add_point_at_position (diagram, point1_pos, labeltype) 
        else : 
            diagram, point1  = add_fakepoint_at_position (diagram, point1_pos, labeltype)
        # print('num points :', len(diagram.points), ', num fakepoints :', len(diagram.fakepoints))
        point1s.append(point1)

    diagram.entities.append(('point_2', [p.label for p in point1s] + [point1s[answer_idx].label]))

    return diagram 

rules = [point_1, point_2]