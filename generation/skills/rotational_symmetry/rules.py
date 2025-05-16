import numpy as np
import random 
from .labels import *


def label_point(diagram):
    ind = 0
    while True:
        label = random.choice(capitals.candidates)
        if label not in [each.label for each in diagram.points + diagram.fakepoints + diagram.coloredpoints]:
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


def add_point_at_position(diagram, point_pos, label=True):
    point_label = label_point(diagram) if label else ''
    point = Point(point_pos[0], point_pos[1], point_label)
    diagram.points.append(point)

    return diagram, point

def add_fakepoint_at_position(diagram, point_pos, label=True):
    point_label = label_point(diagram) if label else ''
    point = FakePoint(point_pos[0], point_pos[1], point_label)
    diagram.fakepoints.append(point)

    return diagram, point

def add_fakepoint_at_position_given_label(diagram, point_pos, given_label='I am a label'):
    point = FakePoint(point_pos[0], point_pos[1], given_label)
    diagram.fakepoints.append(point)
    return diagram, point

def add_coloredpoint_at_position(diagram, point_pos, point_color='k', label=True):
    diagram.colored = True 
    point_label = label_point(diagram) if label else ''
    point = ColoredPoint(point_pos[0], point_pos[1], 
                         label=point_label, 
                         color=point_color)
    diagram.coloredpoints.append(point)

    return diagram, point


def add_polygon(diagram, center_pos, thetas, radials):
    points = [
        add_fakepoint_at_position(diagram, radial * np.array([np.cos(theta), np.sin(theta)]) + center_pos, label=False)[1]
        for theta, radial in zip(thetas, radials)
    ]
    polygon = Polygon(points)
    diagram.polygons.append(polygon)
    return diagram

def add_coloredpolygon(diagram, center_pos, thetas, radials, color):
    diagram.colored = True 
    points = [
        add_fakepoint_at_position(diagram, radial * np.array([np.cos(theta), np.sin(theta)]) + center_pos, label=False)[1]
        for theta, radial in zip(thetas, radials)
    ]
    polygon = ColoredPolygon(points, color)
    diagram.coloredpolygons.append(polygon)
    return diagram

def add_regular_polygon(diagram, center_pos, n, radius, 
                        random_rotation= True ):
    diagram = add_polygon(
        diagram,
        center_pos=center_pos,
        thetas=np.linspace(0, np.pi * 2, n, endpoint=False) + np.random.uniform(0, np.pi*2),
        radials=radius * np.ones((n,))
    )
    return diagram

def add_regular_coloredpolygon(diagram, center_pos, n, radius, color,
                                random_rotation= True):
    diagram = add_coloredpolygon(
        diagram,
        center_pos=center_pos,
        thetas=np.linspace(0, np.pi * 2, n, endpoint=False) + np.random.uniform(0, np.pi*2),
        radials=radius * np.ones((n,)),
        color= color
    )
    return diagram

def sample_repulsive_cartesian(proposals, pair_potential='hardsphere'):

    def potential(positions, potential_func):
        num_proposals, num_particles, _ = positions.shape
        total_potentials = np.array([
            np.sum(np.triu(potential_func(np.linalg.norm(
                positions[t, :, np.newaxis, :] - positions[t, np.newaxis, :, :], axis=2
            )), k=1))
            for t in range(num_proposals)
        ])
        return total_potentials

    def pair_potential_soft_coulomb(r, eps_r=0.1, temperature=1.0):
        return 1 / (np.sqrt(eps_r**2 + r**2) * temperature)

    def pair_potential_sigmoid(r, transition_r=30, temperature=0.1):
        return 1 / ((np.exp(r - transition_r) + 1) * temperature)

    def pair_potential_hardsphere(r, transition_r=50):
        return np.where(r < transition_r, np.inf, 0.0)

    # Select the pair potential function
    potential_func = pair_potential_hardsphere if pair_potential == 'hardsphere' else None

    # Compute potentials and probabilities
    potentials = potential(proposals, potential_func)
    probabilities = np.exp(-potentials)
    probabilities /= np.sum(probabilities)

    return proposals[np.random.choice(len(proposals), p=probabilities)]

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
    
class ColoredPoint:
    def __init__(self, x, y, label, color):
        self.x = x 
        self.y = y 
        self.coord = (x,y)
        self.color = color
        self.label = label 
    
    def __str__ (self) : 
        return f'ColoredPoint({self.x}, {self.y}, {self.label}, {self.color})'

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

class Polygon:
    def __init__(self, points, label = '') : 
        self.vertices = points
        self.label = f'Polygon({[each.label for each in points]})'
    def __str__(self) : 
        return f'Polygon({self.vertices}, {self.label})'
    
class ColoredPolygon : 
    def __init__(self, points, color = 'gray', label = '', alpha = 0.5) : 
        self.vertices = points
        self.label = f'ColoredPolygon({[each.label for each in points]}, {color})'
        self.color = color 
        self.alpha = alpha 
    def __str__(self) : 
        return f'ColoredPolygon({self.vertices}, {self.label})'

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

def reflection_1 (diagram : Diagram) : 

    print('reflection_1 is called')

    # theta (\in thetas) determines the tangent of each line.
    # idx determines which line to be the correct line of reflection. 
    def sample_thetas_and_idx ( _delta_mean = 10 * np.pi / 180, _delta_std = 20 * np.pi / 180, _delta_min = 4.0 * np.pi / 180) : 
        # Generate 4 random increments from a Gamma distribution + constant. 
        deltas      = _delta_min + np.random.gamma(shape=(_delta_mean/_delta_std) ** 2, scale=(_delta_std ** 2)/_delta_mean, size=3)
        answer_idx  = np.random.choice(np.arange(len(deltas)+1))
        thetas      = np.cumsum(np.insert(deltas, 0, 0))
        thetas      = thetas - thetas[answer_idx]
        thetas      += np.random.uniform(-np.pi, np.pi)
        return thetas, answer_idx 
    
    thetas, real_idx = sample_thetas_and_idx() 

    # [R, phi] determines the position of pointP and pointQ relative to pointO
    def sample_R (_R_mean = 250, _R_std = 200, _R_max = 500, _R_min = 50 ) : 
        # Generate R from a Gamma distribution and reject values > 250
        while True :
            R = np.random.gamma(shape=(_R_mean/_R_std)**2, scale=(_R_std ** 2)/_R_mean)
            if R <= _R_max and R >= _R_min :
                break
        return R
    
    R   = sample_R() 
    phi = np.random.uniform(-np.pi, np.pi)

    # # Generate r uniformly distributed in [0, R]
    # r = np.random.uniform(0, R)

    # Compute Cartesian coordinates for the two reflected points P and Q 
    theta_star  = thetas[real_idx]
    pointO_pos  = np.random.normal(loc=500, scale=50, size=(2,))
    pointP_pos  = R * np.array([np.cos(theta_star + phi), np.sin(theta_star + phi)]) + pointO_pos
    pointQ_pos  = R * np.array([np.cos(theta_star - phi), np.sin(theta_star - phi)]) + pointO_pos

    # Add pointP
    def add_point_at_position (diagram, point_pos, label=True) : 
        point_label = label_point(diagram) if label else ''
        point       = Point(point_pos[0], point_pos[1], point_label)
        diagram.points.append(point)
        return diagram, point
    
    diagram, pointO = add_point_at_position(diagram, pointO_pos)
    diagram, pointP = add_point_at_position(diagram, pointP_pos)
    diagram, pointQ = add_point_at_position(diagram, pointQ_pos)

    point1s = []
    for idx in range(len(thetas)): 
        
        _tangent        = np.array([np.cos(thetas[idx]), np.sin(thetas[idx])])
        point1_pos      =   450 * _tangent + pointO_pos
        point2_pos      = - 450 * _tangent + pointO_pos
        
        diagram, point1 = add_point_at_position(diagram, point1_pos)
        diagram, point2 = add_point_at_position(diagram, point2_pos, label=False)
        point1s.append(point1)

        ln12        = Line(point1, point2, '', infinite=True)
        diagram.lines.append(ln12)
        
    diagram.entities.append(('reflection_1', [pointP.label, pointQ.label, pointO.label, point1s[real_idx].label, 
                                              point1s[0].label, point1s[1].label, point1s[2].label, point1s[3].label]))
    
    return diagram 


def point_1 (diagram : Diagram) : 

    print('point_1 is called')

    def add_point_at_position (diagram, point_pos, label=True) : 
        point_label = label_point(diagram) if label else ''
        point       = Point(point_pos[0], point_pos[1], point_label)
        diagram.points.append(point)
        return diagram, point
    
    def add_fakepoint_at_position (diagram, point_pos, label=True) : 
        fakepoint_label = label_point(diagram) if label else ''
        fakepoint       = FakePoint(point_pos[0], point_pos[1], fakepoint_label)
        diagram.fakepoints.append(fakepoint)
        return diagram, fakepoint
    
    num_labels  = 5
    answer_idx  = np.random.choice(np.arange(num_labels))
    point1s     = []
    
    for idx in range(num_labels): 
        point1_pos      = np.random.uniform(100, 900, 2)
        if (idx == answer_idx) : 
            diagram, point1  = add_fakepoint_at_position (diagram, point1_pos, label=True) 
        else : 
            diagram, point1  = add_point_at_position     (diagram, point1_pos, label=True)
        print('num points :', len(diagram.points), ', num fakepoints :', len(diagram.fakepoints))
        point1s.append(point1)

    diagram.entities.append(('point_1', [point1s[answer_idx].label, point1s[0].label, point1s[1].label, point1s[2].label, point1s[3].label, point1s[4].label]))

    return diagram 


def cardinal_1 (diagram : Diagram) : 

    print('cardinal_1 is called')

    def add_point_at_position (diagram, point_pos, label=True) : 
        point_label = label_point(diagram) if label else ''
        point       = Point(point_pos[0], point_pos[1], point_label)
        diagram.points.append(point)
        return diagram, point
    
    min_cnt     = 3
    max_cnt     = 8
    cnt         = np.random.choice((np.arange(min_cnt, max_cnt)))
    for idx in range(cnt): 
        point1_pos       = np.random.uniform(0, 1000, 2)
        diagram, point1  = add_point_at_position (diagram, point1_pos, label='')
    
    diagram.entities.append(('cardinal_1', [f'{cnt}']))

    return diagram 


def similarity_1 (diagram : Diagram) : 

    print('similarity_1 is called')

    def add_point_at_position (diagram, point_pos, label=True) : 
        point_label = label_point(diagram) if label else ''
        point       = Point(point_pos[0], point_pos[1], point_label)
        diagram.points.append(point)
        return diagram, point
    
    def add_triangle_at_point_positions (diagram, point_pos_lst, label=True) : 
        point_lst = [] 

        for point_pos in point_pos_lst : 
            diagram, point = add_point_at_position (diagram, point_pos, label=True) 
            point_lst.append(point)

        triangle    = Triangle (point_lst[0], point_lst[1], point_lst[2], label='')
        diagram.triangles.append(triangle)
        
        return diagram, triangle

    # thetas determine shape of a triangle
    def sample_triangle_thetas ( delta_resolution = 0.05) : 
        
        # Random three points on a circle radius 1 
        deltas      = np.random.uniform( delta_resolution,  1.0,  3 )
        deltas      = (deltas / np.sum(deltas)) * (np.pi * 2)
        thetas      = np.cumsum(np.insert(deltas, 0, 0))[1:]
        return thetas
        
    num_triangles   = 4
    answer_idx      = np.random.choice(np.arange(num_triangles))

    real_thetas = sample_triangle_thetas()
    fake_thetas = sample_triangle_thetas()

    # Hyperparams for scales and locations of each triangles 
    scale_max   = 150
    scale_min   = scale_max / 4
    loc_sche    = np.array([[1/3, 1/3], [1/3, 2/3], [2/3, 1/3], [2/3, 2/3]]) * 1000
    
    triangles = []
    for idx in range(num_triangles) : 

        scale   = np.random.uniform(scale_min, scale_max)
        rot     = np.random.uniform(0, 2 * np.pi)
        loc     = loc_sche[idx]

        thetas      = fake_thetas if idx == answer_idx else real_thetas
        positions   = np.array([np.cos(thetas + rot), np.sin(thetas + rot)]).T * scale + loc
    
        diagram, triangle = add_triangle_at_point_positions (diagram, positions, label=True)
        triangles.append(triangle)

    diagram.entities.append(('similarity_1', [triangles[answer_idx].label, triangles[0].label, triangles[1].label, triangles[2].label, triangles[3].label,]))
    return diagram 


def rotation_1 (diagram : Diagram) :

    def add_point_at_position (diagram, point_pos, label=True) : 
        point_label = label_point(diagram) if label else ''
        point       = Point(point_pos[0], point_pos[1], point_label)
        diagram.points.append(point)
        return diagram, point
    
    def add_triangle_at_point_positions (diagram, point_pos_lst, label=True) : 
        point_lst = [] 

        for point_pos in point_pos_lst : 
            diagram, point = add_point_at_position (diagram, point_pos, label=True) 
            point_lst.append(point)

        triangle    = Triangle (point_lst[0], point_lst[1], point_lst[2], label='')
        diagram.triangles.append(triangle)
        
        return diagram, triangle

    # thetas determine shape of a triangle
    def sample_triangle_thetas ( delta_resolution = 0.05) : 
        
        # Random three points on a circle radius 1 
        deltas      = np.random.uniform( delta_resolution,  1.0,  3 )
        deltas      = (deltas / np.sum(deltas)) * (np.pi * 2)
        thetas      = np.cumsum(np.insert(deltas, 0, 0))[1:]
        return thetas

    num_triangles   = 6 
    answer_idx      = np.random.choice(np.arange(1, num_triangles))
    phis            = (np.arange(0, num_triangles) / num_triangles) * (np.pi * 2)
    
    thetas     = sample_triangle_thetas()
    scale      = 100
    
    pointO_pos      = np.array([500, 500])
    diagram, pointO = add_point_at_position(diagram, pointO_pos, label=True)

    triangles  = []
    for idx in range(num_triangles) : 
        rot         = phis[idx] 
        if answer_idx == idx : 
            rot += np.random.uniform(30, 330) * np.pi / 180

        loc         = 300 * np.array([np.cos(phis[idx]), np.sin(phis[idx])]) + pointO_pos
        positions   = np.array([np.cos(thetas + rot), np.sin(thetas + rot)]).T * scale + loc

        diagram, triangle = add_triangle_at_point_positions (diagram, positions, label=True)
        triangles.append(triangle)

    diagram.entities.append(('rotation_1', [triangles[answer_idx].label, triangles[0].label, triangles[1].label, triangles[2].label, triangles[3].label, triangles[4].label, triangles[5].label, pointO.label]))
    return diagram 
    
def rotational_symmetry_1 (diagram : Diagram) :

    def add_point_at_position (diagram, point_pos, label=True) : 
        point_label = label_point(diagram) if label else ''
        point       = Point(point_pos[0], point_pos[1], point_label)
        diagram.points.append(point)
        return diagram, point
    
    def add_triangle_at_point_positions (diagram, point_pos_lst, label=True) : 
        point_lst = [] 

        for point_pos in point_pos_lst : 
            diagram, point = add_point_at_position (diagram, point_pos, label=True) 
            point_lst.append(point)

        triangle    = Triangle (point_lst[0], point_lst[1], point_lst[2], label='')
        diagram.triangles.append(triangle)
        
        return diagram, triangle

    # thetas determine shape of a triangle
    def sample_triangle_thetas ( delta_resolution = 0.05) : 
        
        # Random three points on a circle radius 1 
        deltas      = np.random.uniform( delta_resolution,  1.0,  3 )
        deltas      = (deltas / np.sum(deltas)) * (np.pi * 2)
        thetas      = np.cumsum(np.insert(deltas, 0, 0))[1:]
        return thetas

    # num_triangles   = 6 
    num_points      = 5
    answer_idx      = np.random.choice(np.arange(0, num_points))
    
    # pointO_pos      = np.array([500, 500])
    # diagram, pointO = add_point_at_position(diagram, pointO_pos, label=True)

    point1s  = []
    for idx in range(num_points) : 
        point1_pos = np.random.normal(500, 100, 2)
        diagram, point1 = add_point_at_position(diagram, point1_pos, label=True)
        point1s.append(point1)

    thetas = sample_triangle_thetas()
    scale = 100

    rotation_radius = np.random.uniform(100, 400)
    phi = np.random.uniform(0, np.pi * 2)

    # triangle 1 
    loc1         = point1s[answer_idx].coord + rotation_radius * np.array([np.cos(phi), np.sin(phi)])
    positions1   = np.array([np.cos(thetas + 0),     np.sin(thetas + 0)]).T      * scale + loc1
    diagram, triangle1 = add_triangle_at_point_positions (diagram, positions1, label=True) 

    # triangle 2 
    loc2         = point1s[answer_idx].coord - rotation_radius * np.array([np.cos(phi), np.sin(phi)])
    positions2   = np.array([np.cos(thetas + np.pi), np.sin(thetas + np.pi)]).T  * scale + loc2
    diagram, triangle2 = add_triangle_at_point_positions (diagram, positions2, label=True) 

    diagram.entities.append(('rotational_symmetry_1', [triangle1.label, triangle2.label,
                                                       point1s[0].label, point1s[1].label, point1s[2].label, point1s[3].label, point1s[4].label, 
                                                       point1s[answer_idx].label]))
    return diagram 


def rotational_symmetry_2 (diagram : Diagram) : 

    "There is a square in the image, which is symmetric with respect to some point. Choose the point that can be the center of the symmetry. State the label (A, B, C, or D) of the point. For example, if the center of the symmetry is point X, your answer should be “X”.",
    
    "There is a <1> in the image, which is symmetric with respect to some point. Choose the point that can be the center of this rotational symmetry. State the label (<2>, <3>, <4>, or <5>) of the point. For example, if the center of the symmetry is point X, your answer should be “X”.",

    shape_names = {
            3 : "triangle", 
            4 : "square", 
            5 : "pentagon",
            6 : "hexagon",
            1000 : "circle"
        }
    n           = random.choice(list(shape_names.keys()))
    radius      = np.random.uniform(300, 450) 
    center_pos  = np.random.uniform(radius, 1000 - radius, 2)
    diagram = add_regular_polygon (diagram, center_pos, n, radius)

    # candidates 
    num_candidates  = 4
    answer_idx      = random.choice(range(num_candidates))    
    num_proposal    = 100 
    proposals       = np.zeros((num_proposal, num_candidates, 2))
    random_angles   = np.random.uniform(0, np.pi * 2, size=(num_proposal, num_candidates))
    random_radii    = np.random.uniform(0.1, 1.0, size=(num_proposal, num_candidates)) * radius * np.cos(np.pi / n)
    for t in range(num_proposal):
        proposals[t] = center_pos + random_radii[t, :, None] * np.stack([np.cos(random_angles[t]), np.sin(random_angles[t])], axis=-1)
        proposals[t, answer_idx] = center_pos  # Set the correct answer position
                
    positions = sample_repulsive_cartesian(proposals)
    label_lst = [] 
    for idx in range(len(positions)) : 
        diagram, _point = add_point_at_position(diagram, positions[idx], label= True)
        label_lst.append ( _point.label )
    
    diagram.entities.append(('rotational_symmetry_2', [shape_names[n]] + label_lst + [label_lst[answer_idx]]))

    return diagram 


def rotational_symmetry_3 (diagram : Diagram) : 

    "There is a circle in the image, which is symmetric with respect to some point. Choose the point that can be the center of symmetry. State the color (red, orange, yellow, or green) of the point. For example, if the center of symmetry is the black point, your answer should be \"black\".",

    "There is a <1> in the image, which is symmetric with respect to some point. Choose the point that can be the center of symmetry. State the color (<1>, <2>, <3>, or <4>) of the point. For example, if the center of symmetry is the black point, your answer should be \"black\".",

    diagram.colored = True 
    
    shape_names = {
            3 : "triangle", 
            4 : "square", 
            5 : "pentagon",
            6 : "hexagon",
            1000 : "circle"
        }
    n           = random.choice(list(shape_names.keys()))
    radius      = np.random.uniform(300, 450) 
    center_pos  = np.random.uniform(radius, 1000 - radius, 2)
    diagram = add_regular_polygon (diagram, center_pos, n, radius)

    # candidates 
    num_candidates  = 4
    answer_idx      = random.choice(range(num_candidates))    
    num_proposal    = 100 
    proposals       = np.zeros((num_proposal, num_candidates, 2))
    random_angles   = np.random.uniform(0, np.pi * 2, size=(num_proposal, num_candidates))
    random_radii    = np.random.uniform(0.1, 1.0, size=(num_proposal, num_candidates)) * radius * np.cos(np.pi / n)
    for t in range(num_proposal):
        proposals[t] = center_pos + random_radii[t, :, None] * np.stack([np.cos(random_angles[t]), np.sin(random_angles[t])], axis=-1)
        proposals[t, answer_idx] = center_pos  # Set the correct answer position
                
    positions = sample_repulsive_cartesian(proposals)
    color_lst = random.sample(['red', 'orange', 'yellow', 'green', 'blue', 'purple'], 
                              num_candidates)
    for idx in range(len(positions)) : 
        diagram, _coloredpoint = add_coloredpoint_at_position(diagram, positions[idx], label= False, point_color= color_lst[idx])
    
    diagram.entities.append(('rotational_symmetry_3', [shape_names[n]] + color_lst + [color_lst[answer_idx]]))

    return diagram 
    

def rotational_symmetry_4 (diagram : Diagram) : 
    
    "Among shapes labeled as <2> and <3>, which shape is most likely to have <1>-fold rotational symmetry? In other words, which shape is most likely to look the same when rotated by 90 degrees around some point? The answer should be a single number.",

    num_candidates = 2 

    answer_idx = random.choice(range(num_candidates))

    n = random.choice([3, 4, 5, 6])

    labels = [] 
    for idx in range(num_candidates) : 

        center_pos = np.array([333 * (idx + 1), 500])

        diagram, _fakepoint = add_fakepoint_at_position(diagram, center_pos + np.array([0, 200]), label=True)
        labels.append(_fakepoint.label)

        if idx == answer_idx : 
            radius = np.random.uniform(100, 150)
            diagram = add_regular_polygon(diagram, center_pos=center_pos, n=n, radius=radius, random_rotation=True)

        else : 
            fake_n = np.random.choice([3, 4, 5, 6])    
            radials = np.random.uniform(100, 150, fake_n)
            deltas = np.random.uniform(0.1, 1, fake_n)
            deltas = (deltas / np.sum(deltas)) * np.pi * 2
            thetas = np.cumsum(np.insert(deltas, 0, 0))
            diagram = add_polygon(diagram, center_pos=center_pos, thetas=thetas, radials=radials)

    diagram.entities.append(('rotational_symmetry_4', [f'{n}'] + labels + [labels[answer_idx]])) 


def rotational_symmetry_4_1 (diagram : Diagram) : 
    "In this figure, shapes are labeled with numbers, E, and 'Rotated E.' Among numbered shapes, which shape is most likely to have 4-fold rotational symmetry? In other words, which shape is most likely to look the same when rotated by 90 degrees around the red dot in each shape? To clarify, the shape labeled 'Rotated E' shows the result of a 90-degree rotation of shape E. The answer should be a single number."

    "In this figure, shapes are labeled with numbers, <1>, and 'Rotated <1>.' Among numbered shapes, which shape is most likely to have 4-fold rotational symmetry? In other words, which shape is most likely to look the same when rotated by 90 degrees around the red dot in each shape? To clarify, the shape labeled 'Rotated <1>' shows the result of a 90-degree rotation of shape <1>. The answer should be a single number."
    "In this figure, shapes are labeled with numbers, <1>, and 'Rotated <1>.' Among numbered shapes 1 and 2, which shape is most likely to have 4-fold rotational symmetry? In other words, which shape is most likely to look the same when rotated by 90 degrees around the red dot in each shape? To clarify, the shape labeled 'Rotated <1>' shows the result of a 90-degree rotation of shape <1>. The answer should be a single number."

    
    # arrow shape 
    scale = np.random.uniform(50, 100)
    x1 = np.random.uniform(-0.1, +0.5)
    y  = np.random.uniform(0.5, 1.0)
    y1_ratio = np.random.uniform(0.3, 0.7)

    def arrow_radials_thetas (scale, x1, y, y1_ratio) : 
        y1 = y * y1_ratio
        arrow_radials = np.array([1, np.sqrt(x1**2 + y**2), np.sqrt(x1**2 + y1**2), np.sqrt(1 + y1**2), 
                            np.sqrt(1 + y1**2), np.sqrt(x1**2 + y1**2), np.sqrt(x1**2 + y**2)]) * scale 
        if x1 > 0 : 
            arrow_thetas  = np.array([0, np.arctan(y/x1), np.arctan(y1/x1), np.pi - np.arctan(y1),
                                - (np.pi - np.arctan(y1)), -np.arctan(y1/x1), -np.arctan(y / x1) ])
        elif x1 < 0 : 
            arrow_thetas  = np.array([0, (np.pi-np.arctan(-y/x1)), (np.pi-np.arctan(-y1/x1)), np.pi - np.arctan(y1),
                                - (np.pi - np.arctan(y1)), -(np.pi-np.arctan(-y1/x1)), -(np.pi-np.arctan(-y/x1)) ])
        return arrow_radials, arrow_thetas

    arrow_radials, arrow_thetas = arrow_radials_thetas (scale, x1, y, y1_ratio)   
    
    arrow_center_1 = np.asarray([250,667])
    arrow_center_2 = np.asarray([250,333])
    
    arrow_color = 'b'
    diagram = add_coloredpolygon(diagram, center_pos=arrow_center_1, thetas=arrow_thetas, radials=arrow_radials, color=arrow_color)
    diagram = add_coloredpolygon(diagram, center_pos=arrow_center_2, thetas=arrow_thetas - np.pi/2, radials=arrow_radials, color=arrow_color)
    
    
    diagram, fake_point = add_fakepoint_at_position(diagram, arrow_center_1 + np.array([0, scale + 50]), label=True)
    diagram, _ = add_fakepoint_at_position_given_label(diagram, arrow_center_2 + np.array([0, scale + 50]), given_label=f'Rotated {fake_point.label}')

    diagram, _ = add_coloredpoint_at_position(diagram, arrow_center_1, label=False, point_color='r')
    diagram, _ = add_coloredpoint_at_position(diagram, arrow_center_2, label=False, point_color='r')

    num_candidates = 2 

    answer_idx = random.choice(range(num_candidates))

    # n = random.choice([3, 4, 5, 6])
    n = 4 

    labels = [] 
    color = random.choice(['yellow', 'orange', 'green', 'purple'])
    for idx in range(num_candidates) : 

        center_pos = np.array([625 + (idx * 250), 500])

        diagram, _fakepoint = add_fakepoint_at_position_given_label(diagram, center_pos + np.array([0, 150]), given_label=f'{idx+1}')
        labels.append(_fakepoint.label)

        diagram, _ = add_coloredpoint_at_position(diagram, center_pos, label=False, point_color='r')

        if idx == answer_idx : 
            radius = np.random.uniform(80, 110)
            diagram = add_regular_coloredpolygon(diagram, center_pos=center_pos, n=n, radius=radius, color=color, random_rotation=True)

        else : 
            fake_n = np.random.choice([3, 4, 5, 6])    
            radials = np.random.uniform(80, 110, fake_n)
            deltas = np.random.uniform(0.1, 1, fake_n)
            deltas = (deltas / np.sum(deltas)) * np.pi * 2
            thetas = np.cumsum(np.insert(deltas, 0, 0))
            diagram = add_coloredpolygon(diagram, center_pos=center_pos, thetas=thetas, radials=radials, color=color)


    diagram.entities.append(('rotational_symmetry_4_1', [f'{fake_point.label}', f'{answer_idx}'])) 
    return diagram 

def rotational_symmetry_5 (diagram : Diagram) : 
    "Among the red, blue, and black shapes in the given picture, which one is symmetric to the green shape with respect to a point, not a line? Choose one and write your last sentence as follows: The [red/blue/black/yellow] shape is symmetric to the green shape with respect to a point not shown in the image."
    "Among the <2>, <3>, and <4> shapes in the given picture, which one is symmetric to the <1> shape with respect to a point, not a line? Choose one and write your last sentence as follows: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to a point not shown in the image."

    num_candidates = 4 

    color_lst = random.sample(['red', 'orange', 'yellow', 'green', 'blue', 'purple'], 
                              num_candidates)
    
    shape_n         = np.random.choice([3, 4])
    shape_radials   = np.random.uniform(20, 250 / np.sqrt(2), shape_n)
    _shape_deltas   = np.random.uniform(0.1, 1, shape_n)
    _shape_deltas   = (_shape_deltas / np.sum(_shape_deltas)) * np.pi * 2
    shape_thetas    = np.cumsum(np.insert(_shape_deltas, 0, 0))

    global_radius = np.random.uniform(np.sqrt(2) * np.max(shape_radials), 250)
    global_phis   = np.linspace(0, np.pi*2, num_candidates, endpoint=False) + np.random.uniform(0, np.pi*2)

    dist_from_global_center = global_radius + np.max(shape_radials)
    global_center = np.random.uniform(dist_from_global_center, 1000 - dist_from_global_center, 2)

    for idx in range( num_candidates ) : 

        shape_center_pos = global_radius * np.array([np.cos(global_phis[idx]), np.sin(global_phis[idx])]) + dist_from_global_center
        
        reflect_each_shape = 1 if idx%2 == 0 else -1 

        diagram = add_coloredpolygon(diagram, 
                                     center_pos =shape_center_pos, 
                                     thetas     =shape_thetas * reflect_each_shape + global_phis[0] + (np.pi / 2) * idx, 
                                     radials    =shape_radials, 
                                     color      =color_lst[idx])
        
    diagram.entities.append(('rotational_symmetry_5', 
                             [color_lst[0]] + random.sample([color_lst[1], color_lst[2], color_lst[3]], 3) + [color_lst[2]]))

    
def ordinal_1 (diagram : Diagram) : 
    
    "What is the name of the third shape from the bottom? Choose from 'circle,' 'triangle,' 'rectangle,' 'hexagon,' and 'arrow.'"

    def add_point_at_position (diagram, point_pos, label=True) : 
        point_label = label_point(diagram) if label else ''
        point       = Point(point_pos[0], point_pos[1], point_label)
        diagram.points.append(point)
        return diagram, point

    def add_circle (diagram, loc, scale) :
        diagram, pointO = add_point_at_position(diagram, loc, label=False)
        diagram.circles.append(Circle(pointO, scale, f'(O,{scale})'))
        return diagram 

    def add_line (diagram, point1, point2, infinite=True) : 
        ln12        = Line(point1, point2, '', infinite=infinite)
        diagram.lines.append(ln12)
        return diagram, ln12
    
    def add_rectangle (diagram, loc, scale1, scale2) : 
        
        # add rectangle composing points
        diagram, pointA = add_point_at_position(diagram, loc + np.array([scale1/2, scale2/2]), label=False)
        diagram, pointB = add_point_at_position(diagram, loc + np.array([scale1/2, -scale2/2]), label=False)
        diagram, pointC = add_point_at_position(diagram, loc + np.array([-scale1/2, -scale2/2]), label=False)
        diagram, pointD = add_point_at_position(diagram, loc + np.array([-scale1/2, scale2/2]), label=False)
        
        # add rectangle composing lines 
        diagram, _ = add_line(diagram, pointA, pointB, infinite=False)
        diagram, _ = add_line(diagram, pointC, pointB, infinite=False)
        diagram, _ = add_line(diagram, pointC, pointD, infinite=False)
        diagram, _ = add_line(diagram, pointA, pointD, infinite=False)

        return diagram 
    
    def add_polygon (diagram, loc, scale, n) : 
                
        phis    = (np.arange(0, n) / n) * (np.pi * 2)
        phis    += np.random.uniform(0, np.pi * 2)

        # add hexagon composing points
        point1s = [] 
        for phi in phis :  
            diagram, point1 = add_point_at_position(diagram, loc + scale * np.array([np.cos(phi), np.sin(phi)]), label=False)
            point1s.append(point1)
        
        # add hexagon composing lines
        for i in range(n) : 
            j           = (i+1)%n
            diagram, _  = add_line(diagram, point1s[i], point1s[j], infinite=False)  

        return diagram

    ## List of shapes
    shape_lst = np.random.permutation(['hexagon', 'rectangle', 'circle', 'triangle', 'pentagon'])
    
    for idx in range(len(shape_lst)) : 

        loc = np.array([np.random.uniform(300, 600), (idx+1) * (1000/(len(shape_lst)+1))])
        scale = np.random.uniform(50, 100)

        if shape_lst[idx] == 'hexagon' :     
            diagram = add_polygon(diagram, loc, scale, n=6)

        elif shape_lst[idx] == 'rectangle' : 
            diagram = add_rectangle(diagram, loc, scale * 1.5, scale / 1.5)

        elif shape_lst[idx] == 'circle' : 
            diagram = add_circle(diagram, loc, scale)

        elif shape_lst[idx] == 'triangle' : 
            diagram = add_polygon(diagram, loc, scale, n=3)

        elif shape_lst[idx] == 'pentagon' : 
            diagram = add_polygon(diagram, loc, scale, n=5)

    idx_to_ask      = np.random.choice([0,1,2,3,4])
    from_the_bottom = ['first', 'second', 'third', 'fourth', 'fifth']
    diagram.entities.append(('ordinal_1', [from_the_bottom[idx_to_ask], shape_lst[idx_to_ask]]))

    return diagram 
    
rules = []
rules += [rotational_symmetry_1]
rules += [rotational_symmetry_2]
rules += [rotational_symmetry_3]
rules += [rotational_symmetry_4]
rules += [rotational_symmetry_4_1]
rules += [rotational_symmetry_5]
