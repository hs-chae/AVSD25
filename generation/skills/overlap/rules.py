import numpy as np
import random 
from .labels import *
from shapely.geometry import Polygon as ShapelyPolygon


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


def add_polygon(diagram, center_pos, thetas, radials, 
                alpha=1.0, 
                return_polygon=False):
    points = [
        add_fakepoint_at_position(diagram, radial * np.array([np.cos(theta), np.sin(theta)]) + center_pos, label=False)[1]
        for theta, radial in zip(thetas, radials)
    ]
    polygon = Polygon(points, alpha=alpha)
    diagram.polygons.append(polygon)
    
    if return_polygon : 
        return diagram, polygon
    
    return diagram

def add_coloredpolygon(diagram, center_pos, thetas, radials, color, 
                       alpha=1.0,
                       return_polygon=False):
    diagram.colored = True 
    points = [
        add_fakepoint_at_position(diagram, radial * np.array([np.cos(theta), np.sin(theta)]) + center_pos, label=False)[1]
        for theta, radial in zip(thetas, radials)
    ]
    polygon = ColoredPolygon(points, color, alpha=alpha)
    diagram.coloredpolygons.append(polygon)

    if return_polygon : 
        return diagram, polygon

    return diagram

def add_regular_polygon(diagram, center_pos, n, radius, 
                        alpha= 1.0,
                        random_rotation= True):
    diagram = add_polygon(
        diagram,
        center_pos=center_pos,
        thetas=np.linspace(0, np.pi * 2, n, endpoint=False) + np.random.uniform(0, np.pi*2),
        radials=radius * np.ones((n,)),
        alpha = alpha 
    )
    return diagram

def add_regular_coloredpolygon(diagram, center_pos, n, radius, color, 
                               alpha= 1.0, 
                               random_rotation= True):
    diagram = add_coloredpolygon(
        diagram,
        center_pos=center_pos,
        thetas=np.linspace(0, np.pi * 2, n, endpoint=False) + np.random.uniform(0, np.pi*2),
        radials=radius * np.ones((n,)),
        color= color,
        alpha= alpha 
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

def is_overlapping(cvxpos_1, cvxpos_2):
    """
    Determine if two polygons overlap using the Separating Axis Theorem.

    Parameters:
        polygon1 (list of tuples): List of 2D positions representing the first polygon.
        polygon2 (list of tuples): List of 2D positions representing the second polygon.

    Returns:
        bool: True if polygons overlap, False otherwise.
    """
    def get_edges(polygon):
        return [polygon[i] - polygon[i - 1] for i in range(len(polygon))]

    def get_normals(edges):
        return [np.array([-edge[1], edge[0]]) for edge in edges]

    def project(polygon, axis):
        projections = [np.dot(vertex, axis) for vertex in polygon]
        return min(projections), max(projections)

    def overlap(min1, max1, min2, max2):
        return max1 >= min2 and max2 >= min1

    cvxpos_1 = np.array(cvxpos_1)
    cvxpos_2 = np.array(cvxpos_2)

    edges1 = get_edges(cvxpos_1)
    edges2 = get_edges(cvxpos_2)
    normals = get_normals(edges1) + get_normals(edges2)

    for axis in normals:
        axis = axis / np.linalg.norm(axis)  # Normalize the axis
        min1, max1 = project(cvxpos_1, axis)
        min2, max2 = project(cvxpos_2, axis)
        if not overlap(min1, max1, min2, max2):
            return False  # Found a separating axis

    return True  # No separating axis found, polygons overlap

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
    def __init__(self, points, label = '', alpha = 1.0) : 
        self.vertices = points
        self.label = f'Polygon({[each.label for each in points]})'
        self.alpha = alpha 
        self.coords = [point.coord for point in points]
    def __str__(self) : 
        return f'Polygon({self.vertices}, {self.label}, {self.alpha})'
    
class ColoredPolygon : 
    def __init__(self, points, color = 'gray', edgelabel = '', alpha = 1.0) : 
        self.vertices = points
        self.label = f'ColoredPolygon({[each.label for each in points]}, {color})'
        self.color = color 
        self.alpha = alpha 
        self.coords = [point.coord for point in points]
    def __str__(self) : 
        return f'ColoredPolygon({self.vertices}, {self.label}, {self.alpha})'

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
        # diagram.entities.append(('circle',[f'{pointO.label}',f'{label_point(diagram)}']))
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


def orientation_1 (diagram : Diagram) :

    def add_point_at_position (diagram, point_pos, label=True) : 
        point_label = label_point(diagram) if label else ''
        point       = Point(point_pos[0], point_pos[1], point_label)
        diagram.points.append(point)
        return diagram, point
    
    def add_circle (diagram, loc, scale) :
        diagram, pointO = add_point_at_position(diagram, loc, label=False)
        diagram.circles.append(Circle(pointO, scale, f'(O,{scale})'))
        # diagram.entities.append(('circle',[f'{pointO.label}',f'{label_point(diagram)}']))
        return diagram 

    # "question": "In the given image, there is a shape with letters within the shape. If we read those letters clockwise or counterclockwise, we can read a word ‘MATE’. Which direction should we read? Answer clockwise or counterclockwise.",
    # "In the given image, there is letters on a circle. If we read those letters clockwise or counterclockwise, we can read a word(sequence of letters) ‘<1>’. Which direction should we read? Answer clockwise or counterclockwise.",
    
    num_points  = np.random.choice([4,5,6])
    delta_phis  = np.random.uniform(0.2, 1, num_points)
    phis        = np.cumsum(np.insert(delta_phis, 0, 0))[1:]
    # phis        = (np.arange(0, num_points) / num_points) * (np.pi * 2) + np.random.uniform(0, np.pi * 2)
    
    answer_ori = np.random.choice(['clockwise', 'counterclockwise'])
    
    scale   = np.random.uniform(100, 450)
    loc     = np.random.uniform(scale, 1000-scale, 2)

    diagram = add_circle(diagram, loc, scale)

    point1s = []
 
    for phi in phis : 
        if answer_ori == 'counterclockwise' : 
            point1_pos = loc + scale * np.array([np.cos(phi), np.sin(phi)])
        else : 
            point1_pos = loc + scale * np.array([np.cos(-phi), np.sin(-phi)])

        diagram, point1 = add_point_at_position(diagram, point1_pos)
        point1s.append(point1)

    read_letters = f'{[each.label for each in point1s]}'
    
    diagram.entities.append(('orientation_1', [read_letters, answer_ori]))
    return diagram 


def overlap_1 (diagram : Diagram) : 
    
    "Choose the phrase in parentheses that correctly describes the image. In the image, the green hexagon and the orange shape {do not meet/are tangent to each other/overlap}.",
    "In the image, you can see two circles. Do the interiors of these circles overlap?"

    def add_circle (diagram, loc, scale) :
        diagram, pointO = add_fakepoint_at_position(diagram, loc, label=False)
        diagram.circles.append(Circle(pointO, scale, f'(O,{scale})'))
        # diagram.entities.append(('circle',[f'{pointO.label}',f'{label_point(diagram)}']))
        return diagram 

    ## List of shapes
    overlap         = np.random.choice([True, False])

    scale1 = np.random.uniform(50, 300)
    scale2 = np.random.uniform(100, scale1)
    
    loc1 = np.random.uniform(scale1, 1000-scale1, 2)
    loc2 = np.random.uniform(scale1, 1000-scale1, 2)

    overlap = (np.sqrt(((loc1 - loc2)**2).sum()) < scale1 + scale2)    

    diagram = add_circle(diagram, loc1, scale1)    
    diagram = add_circle(diagram, loc2, scale2)   
    
    if not overlap : 
        answer_long = np.random.choice([
            "The interiors of the two circles do not overlap.",
            "There is no overlap between the interiors of the two circles.",
            "The two circles have interiors that do not intersect.",
            "The interiors of the circles remain distinct and do not overlap.",
            "No overlapping occurs between the interiors of the two circles.",
            "The two circles do not share overlapping interior regions.",
            "The interiors of the circles do not intersect with each other.",
            "There is no intersection or overlap within the interiors of the two circles.",
            "The interior spaces of the two circles are separate and do not overlap.",
            "The interior regions of the two circles remain non-overlapping."
        ])
    else :
        answer_long = np.random.choice([
            "The interiors of the two circles overlap.",
            "There is an overlap between the interiors of the two circles.",
            "The two circles have interiors that intersect.",
            "The interiors of the circles are not distinct and overlap.",
            "Overlapping occurs between the interiors of the two circles.",
            "The two circles share overlapping interior regions.",
            "The interiors of the circles intersect with each other.",
            "There is an intersection or overlap within the interiors of the two circles.",
            "The interior spaces of the two circles are overlapping.",
            "The interior regions of the two circles overlap with each other."
        ])
        
    if not overlap : 
        answer_short = np.random.choice([
            "No"
        ])
    else :
        answer_short = np.random.choice([
            "Yes"
        ])
    
    diagram.entities.append(('overlap_1', [answer_long, answer_short]))

    return diagram 

def overlap_2 (diagram : Diagram) : 

    "In the image, you can see two triangles. Do the interiors of these triangles overlap?"
    
    def _sample_polygon_shape_parameter () : 

        shape_n         = np.random.choice([3])
        shape_radials   = np.random.uniform(150, 250, shape_n)
        _shape_deltas   = np.random.uniform(0.2, 1, shape_n)
        _shape_deltas   = (_shape_deltas / np.sum(_shape_deltas)) * np.pi * 2
        shape_thetas    = np.cumsum(np.insert(_shape_deltas, 0, 0))

        return shape_radials, shape_thetas

    polygon_position_lst = [] 

    for idx in range(2) : 

        shape_radials, shape_thetas = _sample_polygon_shape_parameter() 

        center_pos = np.random.uniform(np.max(shape_radials), 1000-np.max(shape_radials), 2)

        diagram, polygon = add_polygon(diagram, center_pos, 
                                       thetas=shape_thetas, radials=shape_radials,
                                       alpha= 0.5, return_polygon=True)
        
        polygon_position_lst.append( polygon.coords )

    _shapelypolygon1 = ShapelyPolygon(polygon_position_lst[0])
    _shapelypolygon2 = ShapelyPolygon(polygon_position_lst[1])

    overlap = _shapelypolygon1.intersects(_shapelypolygon2)
    
    if not overlap:
        answer_long = np.random.choice([
            "The interiors of the two triangles do not overlap.",
            "There is no overlap between the interiors of the two triangles.",
            "The two triangles have interiors that do not intersect.",
            "The interiors of the triangles remain distinct and do not overlap.",
            "No overlapping occurs between the interiors of the two triangles.",
            "The two triangles do not share overlapping interior regions.",
            "The interiors of the triangles do not intersect with each other.",
            "There is no intersection or overlap within the interiors of the two triangles.",
            "The interior spaces of the two triangles are separate and do not overlap.",
            "The interior regions of the two triangles remain non-overlapping."
        ])
    else:
        answer_long = np.random.choice([
            "The interiors of the two triangles overlap.",
            "There is an overlap between the interiors of the two triangles.",
            "The two triangles have interiors that intersect.",
            "The interiors of the triangles are not distinct and overlap.",
            "Overlapping occurs between the interiors of the two triangles.",
            "The two triangles share overlapping interior regions.",
            "The interiors of the triangles intersect with each other.",
            "There is an intersection or overlap within the interiors of the two triangles.",
            "The interior spaces of the two triangles are overlapping.",
            "The interior regions of the two triangles overlap with each other."
        ])
        
    if not overlap : 
        answer_short = np.random.choice([
            "No"
        ])
    else :
        answer_short = np.random.choice([
            "Yes"
        ])
    
    diagram.entities.append(('overlap_2', [answer_long, answer_short]))
    
    return diagram 

def overlap_2_1 (diagram : Diagram) : 

    "In the image, you can see two squares. Do the interiors of these squares overlap?"
    
    def _sample_polygon_shape_parameter () : 

        shape_n         = np.random.choice([4])
        shape_radials   = np.random.uniform(150, 250, shape_n)
        _shape_deltas   = np.random.uniform(0.2, 1, shape_n)
        _shape_deltas   = (_shape_deltas / np.sum(_shape_deltas)) * np.pi * 2
        shape_thetas    = np.cumsum(np.insert(_shape_deltas, 0, 0))

        return shape_radials, shape_thetas

    polygon_position_lst = [] 

    for idx in range(2) : 

        shape_radials, shape_thetas = _sample_polygon_shape_parameter() 

        center_pos = np.random.uniform(np.max(shape_radials), 1000-np.max(shape_radials), 2)

        diagram, polygon = add_polygon(diagram, center_pos, 
                                       thetas=shape_thetas, radials=shape_radials,
                                       alpha= 0.5, return_polygon=True)
        
        polygon_position_lst.append( polygon.coords )

    _shapelypolygon1 = ShapelyPolygon(polygon_position_lst[0])
    _shapelypolygon2 = ShapelyPolygon(polygon_position_lst[1])

    overlap = _shapelypolygon1.intersects(_shapelypolygon2)
    
    if not overlap:
        answer_long = np.random.choice([
            "The interiors of the two squares do not overlap.",
            "There is no overlap between the interiors of the two squares.",
            "The two squares have interiors that do not intersect.",
            "The interiors of the squares remain distinct and do not overlap.",
            "No overlapping occurs between the interiors of the two squares.",
            "The two squares do not share overlapping interior regions.",
            "The interiors of the squares do not intersect with each other.",
            "There is no intersection or overlap within the interiors of the two squares.",
            "The interior spaces of the two squares are separate and do not overlap.",
            "The interior regions of the two squares remain non-overlapping."
        ])
    else:
        answer_long = np.random.choice([
            "The interiors of the two squares overlap.",
            "There is an overlap between the interiors of the two squares.",
            "The two squares have interiors that intersect.",
            "The interiors of the squares are not distinct and overlap.",
            "Overlapping occurs between the interiors of the two squares.",
            "The two squares share overlapping interior regions.",
            "The interiors of the squares intersect with each other.",
            "There is an intersection or overlap within the interiors of the two squares.",
            "The interior spaces of the two squares are overlapping.",
            "The interior regions of the two squares overlap with each other."
        ])

    if not overlap : 
        answer_short = np.random.choice([
            "No"
        ])
    else :
        answer_short = np.random.choice([
            "Yes"
        ])
    
    diagram.entities.append(('overlap_2_1', [answer_long, answer_short]))
    
    return diagram 

def overlap_5 (diagram : Diagram) : 
    "Choose the word in parentheses that correctly describes the image. Rewrite the sentence with the chosen word. In the image, the purple region and the orange region overlap each other, and the shape of the intersection is a (triangle/point/pentagon/circle)."
    "Choose the word in parentheses that correctly describes the image. Rewrite the sentence with the chosen word. In the image, the purple region and the orange region overlap each other, and the shape of the intersection is a (triangle/square/pentagon/circle)."
    "Choose the word in parentheses that correctly describes the image. Rewrite the sentence with the chosen word. In the image, the purple shape <1> and the orange shape <2> overlap each other, and the shape of the intersection is a (triangle/square/pentagon/circle)."

    shape_names = {
        3 : 'triangle',
        4 : 'square',
        5 : 'pentagon',
        1000 : 'circle',
    }
    def _sample_polygon_shape_parameter ( min_radials=50, max_radials=200, shape_n=3) : 
    
        if shape_n < 10 : 
            shape_radials   = np.random.uniform(min_radials, max_radials, shape_n)
        else : 
            shape_radials   = np.ones((shape_n,)) * np.random.uniform(min_radials, max_radials)

        _shape_deltas   = np.random.uniform(0.2, 1, shape_n)
        _shape_deltas   = (_shape_deltas / np.sum(_shape_deltas)) * np.pi * 2
        shape_thetas    = np.cumsum(np.insert(_shape_deltas, 0, 0))
        # shape_thetas = np.linspace(0, np.pi*2, shape_n, endpoint=False)

        return shape_radials, shape_thetas
    
    small_n, big_n = random.sample([3, 4, 5, 1000], 2)

    small_radials, small_thetas = _sample_polygon_shape_parameter(shape_n= small_n)

    # big_radials, big_thetas = _sample_polygon_shape_parameter(min_radials= np.max(small_radials) / np.cos(np.pi / big_n), shape_n= big_n)
    big_radials = np.ones((big_n,)) * np.random.uniform(np.max(small_radials) / np.cos(np.pi / big_n), 500)
    big_thetas = np.linspace(0, np.pi*2, big_n, endpoint=False)

    center_pos = np.random.uniform(np.max(big_radials), 1000 - np.max(big_radials))

    diagram = add_coloredpolygon(diagram, center_pos=center_pos, thetas=big_thetas, radials=big_radials, color='purple', alpha=0.5)
    diagram = add_coloredpolygon(diagram, center_pos=center_pos, thetas=small_thetas, radials=small_radials, color='orange', alpha=0.5)
    
    diagram.entities.append(('overlap_5', [shape_names[small_n]]))
    return diagram 
    

def overlap_4 (diagram : Diagram) : 
    "In the image, there are five circles with different colors: red, blue, green, orange, and purple. Choose the circle which is overlapping with multiple circles. Answer the color of that circle. For example, if the black circle overlaps with multiple circles, then the answer will be \"black.\""

    "In the image, there are five circles with different colors: <1>, <2>, <3>, <4> and <5>. Choose the circle which is overlapping with multiple circles. Answer the color of that circle. For example, if the black circle overlaps with multiple circles, then the answer will be \"black.\""

    radius = np.random.uniform(80, 100)

    num_circles = 5 

    color_lst = random.sample(['red', 'orange', 'yellow', 'green', 'blue', 'purple'], 5)

    answer_idx = np.random.choice(range(1, num_circles+1))

    answer_center = np.random.uniform( 3 * radius, 1000 - 3 * radius, 2)


rules = []
rules += [overlap_1]
rules += [overlap_2]
rules += [overlap_2_1]
rules += [overlap_5]