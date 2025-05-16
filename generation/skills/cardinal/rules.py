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
        center_pos = center_pos,
        thetas =    np.linspace(0, np.pi * 2, n, endpoint=False) + np.random.uniform(0, np.pi*2),
        radials =   radius * np.ones((n,)),
        alpha =     alpha 
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
    """
    Samples repulsive Cartesian positions based on a specified pair potential.

    Args:
        proposals (np.ndarray): Array of proposed positions, shape (num_proposals, num_particles, 2 or 3).
        pair_potential (str): Type of pair potential ('hardsphere', 'soft_coulomb', 'sigmoid').

    Returns:
        np.ndarray: Selected Cartesian positions based on computed probabilities.
    """

    def potential(positions, potential_func):
        """
        Computes total potentials for all proposals using the given pair potential function.

        Args:
            positions (np.ndarray): Proposed positions, shape (num_proposals, num_particles, dims).
            potential_func (callable): Function to compute pairwise potential.

        Returns:
            np.ndarray: Array of total potentials for each proposal.
        """
        num_proposals, num_particles, _ = positions.shape
        total_potentials = np.array([
            np.sum(np.triu(potential_func(np.linalg.norm(
                positions[t, :, np.newaxis, :] - positions[t, np.newaxis, :, :], axis=2
            )), k=1))
            for t in range(num_proposals)
        ])
        return total_potentials

    def pair_potential_soft_coulomb(r, eps_r=0.1, temperature=0.01):
        """Soft Coulomb potential."""
        return 1 / (np.sqrt(eps_r**2 + r**2) * temperature)

    def pair_potential_sigmoid(r, transition_r=30, temperature=0.1):
        """Sigmoid potential."""
        return 1 / ((np.exp(r - transition_r) + 1) * temperature)

    def pair_potential_hardsphere(r, transition_r=50):
        """Hard sphere potential."""
        return np.where(r < transition_r, np.inf, 0.0)

    # Mapping potential names to functions
    potential_map = {
        'hardsphere': pair_potential_hardsphere,
        'soft_coulomb': pair_potential_soft_coulomb,
        'sigmoid': pair_potential_sigmoid
    }

    # Select the pair potential function
    potential_func = potential_map.get(pair_potential)
    if potential_func is None:
        raise ValueError(f"Unsupported pair_potential '{pair_potential}'. Choose from {list(potential_map.keys())}.")

    # Compute potentials and probabilities
    potentials = potential(proposals, potential_func)
    probabilities = np.exp(-potentials)
    probabilities /= np.sum(probabilities)

    # Sample a proposal based on probabilities
    return proposals[np.random.choice(len(proposals), p=probabilities)]

def get_min_distance_from_positions (positions) : 
        dist_matrix = np.linalg.norm(positions[:, None] - positions, axis=2)
        np.fill_diagonal(dist_matrix, np.inf)
        min_distance = min(np.min(dist_matrix) / 2, *np.min(positions, axis=0), *np.min(1000 - positions, axis=0))
        return min_distance

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


# Function to sample a polygon shape
def sample_polygon_shape(shape_n=None, return_shape_name=True):
    """
    Generates a random polygon shape with specified or random number of vertices.
    
    Args:
        shape_n (int, optional): Number of vertices for the polygon. Random if None.
        return_shape_name (bool): Whether to return the name of the polygon.

    Returns:
        tuple: shape_radials, shape_thetas, (optional) polygon_name
    """
    polygon_names = {
        3: 'triangle',
        4: 'square',
        5: 'pentagon',
        6: 'hexagon',
        7: 'heptagon'
    }
    
    if shape_n is None:
        shape_n = random.choice([3, 4, 5, 6, 7])

    shape_radials = np.random.uniform(50, 400, shape_n)
    _shape_deltas = np.random.uniform(0.5, 1, shape_n)
    _shape_deltas = (_shape_deltas / np.sum(_shape_deltas)) * np.pi * 2
    shape_thetas = np.cumsum(np.insert(_shape_deltas, 0, 0))

    if return_shape_name:
        return shape_radials, shape_thetas, polygon_names[shape_n]
    
    return shape_radials, shape_thetas

# Function to sample a circle shape
def sample_circle_shape():
    """
    Generates a circle shape with evenly spaced points.
    
    Returns:
        tuple: shape_radials (constant), shape_thetas (angles around the circle)
    """
    return np.ones((1000,)) * np.random.uniform(50, 400), np.linspace(0, np.pi * 2, 1000, endpoint=False)

# Function to sample a heart shape
def sample_heart_shape():
    """
    Generates a heart shape based on one of two predefined styles.
    
    Returns:
        tuple: shape_radials, shape_thetas
    """
    heart_style = random.choice([0, 1])

    if heart_style == 0:
        shape_thetas = np.array([1.1071487177940904, 1.155334029870846, 1.1988860479019368, 1.2384947761194036, 1.2747101985509963, 1.3079686216645356, 1.3386136373317137, 1.366912591994641, 1.3930695076348503, 1.4172353307728707, 1.439516288109684, 1.4599810408381722, 1.478667263597807, 1.4955882223571066, 1.5107398719821263, 1.524108914808729, 1.5356821262991702, 1.5454570319258158, 1.5534536888135182, 1.559726889551673, 1.5643776122510455, 1.5675620989898629, 1.5694967185496562, 1.570456938323544, 1.5707694101619611, 1.5707973252121263, 1.5709205666960224, 1.571513382295098, 1.5729229010778878, 1.5754516121465514, 1.5793459807153536, 1.58479203864823, 1.5919174811430579, 1.6007988684394134, 1.6114721136839367, 1.6239444873879199, 1.6382067259296558, 1.6542443167073384, 1.672047506874257, 1.6916199686980982, 1.712986329236365, 1.7361989469955683, 1.76134442161925, 1.7885503856938159, 1.8179931778157987, 1.8499070534655957, 1.8845956665601153, 1.922446649226154, 1.963950208545718, 2.009722682329481, 2.060535797969815, 2.117351622713851, 2.181361182709901, 2.2540201030777944, 2.3370649837964343, 2.432476125435261, 2.542323231303903, 2.668398119412492, 2.811540425535511, 2.9706894394189094, -3.1411531449664727, -2.964196340650936, -2.789607522037317, -2.624545995430358, -2.4736315406120073, -2.338588673664589, -2.2189430943746, -2.112997017338148, -2.0185917787028194, -1.9335505192489664, -1.8558764870345048, -1.78380846521683, -1.7158059893919007, -1.6505053277673096, -1.5866659526156501, -1.5231154440990375, -1.4586949483487195, -1.392204852985705, -1.3223499138930455, -1.2476844166495278, -1.1665618524707697, -1.077101984479789, -0.9772042732227751, -0.8646634430016559, -0.7374766241693782, -0.5944429366551823, -0.43606618950398585, -0.2654794571535822, -0.0887071030785834, 0.08640061193468995, 0.2523110733103171, 0.4037470394056635, 0.5383454464077747, 0.6561222175777032, 0.7584981369260563, 0.8474674458976169, 0.9250851897886208, 0.9932198978723833, 1.0534678967267501, 1.1071487177940904])
        shape_radials = 90. * np.array([0.5590169943749475, 0.5789522279225902, 0.5960311564292625, 0.6100933495950358, 0.6210613263239195, 0.6289323476205959, 0.6337710506370138, 0.6357025421549809, 0.6349056951136178, 0.6316064894515144, 0.6260713113976072, 0.6186001776311788, 0.6095198861451077, 0.5991771170027255, 0.5879315156471845, 0.5761487910660748, 0.5641938535922867, 0.5524240064336406, 0.5411821970489992, 0.5307903368993465, 0.5215427190806879, 0.5136996087035972, 0.5074811498727266, 0.5030618144817455, 0.500565689129564, 0.5000629282413904, 0.5015676696778598, 0.5050376073740738, 0.5103752627886021, 0.517430832759257, 0.526006360188095, 0.5358609064728905, 0.5467164067865642, 0.5582639443890239, 0.5701702598104105, 0.5820843880765167, 0.5936443749982342, 0.6044840562920355, 0.6142398940315593, 0.6225578611097026, 0.6291003541987059, 0.6335531059810205, 0.6356320630853435, 0.635090200441008, 0.631724257926755, 0.6253814132733734, 0.6159659486231122, 0.6034460302087793, 0.5878608053639695, 0.5693281324426883, 0.5480533977088885, 0.5243400270395849, 0.4986024235860094, 0.4713820266507099, 0.4433666794749131, 0.4154118413935311, 0.38855814725528426, 0.3640317657094855, 0.34320169154794455, 0.32745818377008645, 0.31798975043883415, 0.3154971771880987, 0.31997031506819507, 0.33066666826684554, 0.34630936936007145, 0.3653801706588284, 0.3863662360962833, 0.40790269070890367, 0.4288265283044536, 0.44817986425346246, 0.46519251564577563, 0.4792603063166212, 0.48992597771339536, 0.49686469570271674, 0.49987414351946285, 0.49886862337655213, 0.4938766350134225, 0.4850416755248338, 0.4726263472480013, 0.45702018278373324, 0.4387517871985294, 0.41850570567386236, 0.39714328063975546, 0.3757235395822924, 0.35551312778812194, 0.33796232365842455, 0.3246112478797475, 0.3168937231344691, 0.31585398484033356, 0.3218810288730515, 0.3346118406327944, 0.35306618015898156, 0.3759208786765128, 0.4017748561822413, 0.4293211336583023, 0.4574244296120154, 0.4851382623846416, 0.5116936035881381, 0.536478414256667, 0.5590169943749473])

    elif heart_style == 1:
        shape_thetas = np.array([0.7853981633974483, 0.8488626508313906, 0.9122985759780292, 0.9756314547222229, 1.038733866983336, 1.1014205234958483, 1.1634413617990975, 1.2244727510302524, 1.2841070428972812, 1.3418410151609481, 1.3970643152628377, 1.4490499805163344, 1.4969507039402523, 1.5398069760253912, 1.576576684046485, 1.60619976989613, 1.6277142870633916, 1.640437092412402, 1.6442056433782213, 1.6396396209917181, 1.6283280220192393, 1.6128139939913173, 1.5962924637927787, 1.5820717410586131, 1.5729958154514083, 1.5705467235383845, 1.564848858041444, 1.5528927355938504, 1.5371247849394978, 1.5206862679033837, 1.5069043009932162, 1.498703674472081, 1.4981695410334284, 1.506392498845628, 1.5235702397755542, 1.549246895138677, 1.5825731016448694, 1.6225195132091483, 1.668024140843451, 1.7180806469978327, 1.7717835358605842, 1.8283455765231962, 1.8870990472673992, 1.9474885391334025, 2.00906009626989, 2.071449472283203, 2.134371031524356, 2.197608082494028, 2.2610050110792095, 2.324461357863783, 2.3879278761181224, 2.451404565842227, 2.5149406737657243, 2.578636659304731, 2.6426481365722565, 2.707191797067622, 2.7725532764398126, 2.839096821082488, 2.9072763868469633, 2.9776473826930303, 3.050877530338957, 3.127754060693254, -3.074002837611957, -2.9870162126675575, -2.893409382665071, -2.7921530015195155, -2.682397705940762, -2.563687627244284, -2.4362204572969532, -2.30108679426714, -2.1603717908482922, -2.0170002373035003, -1.8742992501404698, -1.735410091184198, -1.6027791891785776, -1.4733970607568758, -1.337388098640993, -1.1962343393981496, -1.0527797726909311, -0.9103327081543305, -0.7720880726731737, -0.6405890137779909, -0.5174245282351322, -0.40321429707546447, -0.2977957777340486, -0.20048582707501364, -0.11032249858742915, -0.026245734163889926, 0.052786578920870304, 0.127733950176053, 0.19944368658284167, 0.26864275082785294, 0.3359414954695027, 0.4018431427470264, 0.4667553409524558, 0.5310017209486217, 0.5948323451961879, 0.6584325029606725, 0.7219296143227121, 0.7853981633974482])
        shape_radials = 230. * np.array([0.28284271247461906, 0.28227383183487514, 0.2805763435650835, 0.27777756428252093, 0.2739225549082071, 0.2690734712947208, 0.26330875888837774, 0.25672229996206175, 0.24942265853722398, 0.24153260607951582, 0.23318914605461066, 0.2245442776516618, 0.21576672893128054, 0.20704481193161162, 0.1985903484250579, 0.19064320162771634, 0.18347523890085446, 0.17739153296651292, 0.17272553391473688, 0.1698245682525529, 0.16902361466337582, 0.17060979863404546, 0.17478619872184933, 0.18164708993842785, 0.19117342853845265, 0.1969027235048887, 0.1860823781858547, 0.17787971555094184, 0.17236561715399032, 0.16950327694726797, 0.16914207340414447, 0.1710328111020727, 0.17485968774485708, 0.18027756377319948, 0.18694351552315, 0.19453715333033364, 0.20276986760582233, 0.21138618069263593, 0.2201608191583879, 0.2288942622778378, 0.23740841859719375, 0.24554320927591497, 0.253154284110259, 0.26011179916449606, 0.2663000531171657, 0.27161774125265126, 0.2759785953752066, 0.27931220824367153, 0.28156487841850814, 0.28270034900267604, 0.282700349002676, 0.2815648784185081, 0.27931220824367153, 0.2759785953752066, 0.2716177412526512, 0.26630005311716576, 0.260111799164496, 0.253154284110259, 0.24554320927591497, 0.23740841859719375, 0.22889426227783777, 0.22016081915838792, 0.21138618069263587, 0.20276986760582236, 0.1945371533303336, 0.18694351552315006, 0.1802775637731994, 0.174859687744857, 0.1710328111020727, 0.16914207340414444, 0.1695032769472679, 0.17236561715399037, 0.17787971555094176, 0.1860823781858546, 0.19690272350488877, 0.1911734285384526, 0.18164708993842782, 0.17478619872184936, 0.17060979863404546, 0.16902361466337573, 0.16982456825255282, 0.17272553391473688, 0.1773915329665129, 0.1834752389008544, 0.19064320162771634, 0.198590348425058, 0.20704481193161164, 0.21576672893128052, 0.22454427765166174, 0.23318914605461072, 0.24153260607951585, 0.24942265853722398, 0.25672229996206164, 0.2633087588883778, 0.2690734712947208, 0.27392255490820705, 0.277777564282521, 0.28057634356508354, 0.2822738318348751, 0.282842712474619])

    return shape_radials, shape_thetas

# Function to sample a star shape
def sample_star_shape(star_n=None):
    """
    Generates a star shape with alternating large and small radii.
    
    Args:
        star_n (int, optional): Number of points in the star. Random if None.

    Returns:
        tuple: shape_radials, shape_thetas
    """
    if star_n is None:
        star_n = random.choice([4, 5, 6, 7])

    large_radius = 100.0
    small_over_large = np.random.uniform(0.3, 0.6)
    small_radius = large_radius * small_over_large

    shape_radials = np.array([large_radius, small_radius] * star_n)
    shape_thetas = np.linspace(0, np.pi * 2, star_n * 2, endpoint=False) + np.pi / 2
    return shape_radials, shape_thetas


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
    def __init__(self, point1 : FakePoint, point2 : FakePoint, label, infinite=False, tickmarks = 0, dotted = False):
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

def cardinal_2 (diagram : Diagram) : 

    "How many line segments are in the image? Answer in a number."

    min_cnt     = 2
    max_cnt     = 10
    cnt = np.random.choice((np.arange(min_cnt, max_cnt)))
    cnt = np.random.choice((np.arange(min_cnt, max_cnt))) if cnt >= 5 else cnt 
    cnt = np.random.choice((np.arange(min_cnt, max_cnt))) if cnt >= 8 else cnt 

    n_shapes_diveded_by_2 = random.choice(range(cnt, cnt * 2))
    line_indices = random.sample(range(n_shapes_diveded_by_2), cnt)
    
    shape_radials   = np.random.uniform(20, 400, size= n_shapes_diveded_by_2*2 )
    _shape_deltas   = np.random.uniform(0.5, 1, n_shapes_diveded_by_2*2 )
    _shape_deltas   = (_shape_deltas / np.sum(_shape_deltas)) * np.pi * 2
    shape_thetas    = np.cumsum(np.insert(_shape_deltas, 0, 0))

    center_pos = np.random.uniform(np.max(shape_radials), 1000 - np.max(shape_radials), 2)

    for idx in line_indices : 

        diagram, fakepoint_1 = add_fakepoint_at_position(diagram, point_pos= shape_radials[2*idx] * np.array([np.cos(shape_thetas[2*idx]), np.sin(shape_thetas[2*idx])]) + center_pos,
                                                         label=False)
        diagram, fakepoint_2 = add_fakepoint_at_position(diagram, point_pos= shape_radials[2*idx + 1] * np.array([np.cos(shape_thetas[2*idx + 1]), np.sin(shape_thetas[2*idx + 1])]) + center_pos,
                                                         label=False)

        line_12 = Line(point1= fakepoint_1, point2= fakepoint_2, label='')
        diagram.lines.append(line_12)
    
    diagram.entities.append(('cardinal_2', [f'{n_shapes_diveded_by_2}']))

def cardinal_3 (diagram : Diagram) : 

    "How many <1>s are there in the image? Answer in number."

    min_cnt     = 2
    max_cnt     = 10
    cnt = np.random.choice((np.arange(min_cnt, max_cnt)))
    if cnt >= 8 : 
        cnt = np.random.choice((np.arange(min_cnt, max_cnt)))

    shape_functions = {
        'polygon':  lambda: sample_polygon_shape(return_shape_name=True),
        'circle':   lambda: (*sample_circle_shape(), 'circle'),
        'heart':    lambda: (*sample_heart_shape(), 'heart'),
        'star':     lambda: (*sample_star_shape(), 'star'),
    }
    
    shape = random.choice(list(shape_functions.keys()))
    shape_radials, shape_thetas, shape_name = shape_functions[shape]()

    center_positions_proposals = np.random.uniform(100, 900, (100, cnt, 2))
    center_positions = sample_repulsive_cartesian (proposals=center_positions_proposals, pair_potential='soft_coulomb')    
    
    min_distance = get_min_distance_from_positions (positions= center_positions)
    epsilon = 1e-1
    shape_radials *= np.random.uniform(0.6, 1 - epsilon) * min_distance / np.max(shape_radials) 

    for center_pos in center_positions : 
        diagram = add_polygon(diagram, center_pos, 
                              thetas    = shape_thetas+np.random.uniform(0,np.pi*2), 
                              radials   = shape_radials, 
                              alpha     = np.random.uniform(0.5, 1.0))
        
    diagram.entities.append(('cardinal_3', [shape_name, f'{cnt}']))    
    return diagram 

def cardinal_4 (diagram : Diagram) : 
    
    "How many different shapes are there? If there are multiple shapes that look exactly alike, count them as one. The answer should be a number."

    min_cnt     = 2
    max_cnt     = 6
    cnt = np.random.choice((np.arange(min_cnt, max_cnt)))

    shape_functions = {
        'triangle':     lambda: sample_polygon_shape(shape_n= 3, return_shape_name=True),
        'square':       lambda: sample_polygon_shape(shape_n= 4, return_shape_name=True),
        'pentagon':     lambda: sample_polygon_shape(shape_n= 5, return_shape_name=True),
        'circle':   lambda: (*sample_circle_shape(), 'circle'),
        'heart':    lambda: (*sample_heart_shape(), 'heart'),
        'star':     lambda: (*sample_star_shape(), 'star'),
    }

    shape_lst = random.sample(list(shape_functions.keys()), cnt)
    shape_info_lst = []
    for idx in range(cnt) : 
        shape_radials, shape_thetas, shape_name = shape_functions[shape_lst[idx]]()
        shape_info_lst.append((shape_radials, shape_thetas, shape_name))

    center_positions_proposals = np.random.uniform(100, 900, (100, cnt, 2))
    center_positions = sample_repulsive_cartesian (proposals=center_positions_proposals, pair_potential='soft_coulomb')
    min_distance = get_min_distance_from_positions (positions= center_positions)
    
    epsilon = 1e-1

    for center_pos, (shape_radials, shape_thetas, shape_name) in zip(center_positions, shape_info_lst) : 
        
        shape_radials *= np.random.uniform(0.6, 1 - epsilon) * min_distance / np.max(shape_radials) 

        diagram = add_polygon(diagram, center_pos, 
                              thetas    = shape_thetas+np.random.uniform(0,np.pi*2), 
                              radials   = shape_radials, 
                              alpha     = np.random.uniform(0.5, 1.0))
        
    diagram.entities.append(('cardinal_4', [f'{cnt}']))

def cardinal_5 (diagram : Diagram) :
    
    "In the image, there are several colored shapes. How many different colors are in the image? Ignore the background color."

    min_cnt     = 2
    max_cnt     = 7
    cnt = np.random.choice((np.arange(min_cnt, max_cnt)))

    color_candidates = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    shape_functions = {
        'triangle':     lambda: sample_polygon_shape(shape_n= 3, return_shape_name=True),
        'square':       lambda: sample_polygon_shape(shape_n= 4, return_shape_name=True),
        'pentagon':     lambda: sample_polygon_shape(shape_n= 5, return_shape_name=True),
        'circle':   lambda: (*sample_circle_shape(), 'circle'),
        'heart':    lambda: (*sample_heart_shape(), 'heart'),
        'star':     lambda: (*sample_star_shape(), 'star'),
    }

    color_lst = random.sample(color_candidates, cnt)
    shape_info_lst = [] 
    for idx in range(cnt) : 
        shape = random.choice(list(shape_functions.keys()))
        shape_radials, shape_thetas, shape_name = shape_functions[shape]()
        shape_info_lst.append((shape_radials, shape_thetas, color_lst[idx]))

    center_positions_proposals = np.random.uniform(100, 900, (100, cnt, 2))
    center_positions = sample_repulsive_cartesian (proposals=center_positions_proposals, pair_potential='soft_coulomb')
    min_distance = get_min_distance_from_positions (positions= center_positions)
    
    epsilon = 1e-1

    for center_pos, (shape_radials, shape_thetas, color) in zip(center_positions, shape_info_lst) : 
        
        shape_radials *= np.random.uniform(0.6, 1 - epsilon) * min_distance / np.max(shape_radials) 

        diagram = add_coloredpolygon(diagram, center_pos, 
                                     thetas    = shape_thetas+np.random.uniform(0,np.pi*2),
                                     radials   = shape_radials, 
                                     alpha     = np.random.uniform(0.8, 1.0),
                                     color     = color)
        
    diagram.entities.append(('cardinal_5', [f'{cnt}']))

def cardinal_6 (diagram : Diagram) :
    
    "In the image, there are several points and letters '<1>'. Count all the '<1>'s. The answer should be one of 3, 4, 5, or 6."

    min_cnt     = 3
    max_cnt     = 6
    cnt = np.random.choice((np.arange(min_cnt, max_cnt)))

    shape_functions = {
        'triangle':     lambda: sample_polygon_shape(shape_n= 3, return_shape_name=True),
        'square':       lambda: sample_polygon_shape(shape_n= 4, return_shape_name=True),
        'circle':   lambda: (*sample_circle_shape(), 'circle'),
    }

    shape = random.choice(list(shape_functions.keys()))
    shape_radials, shape_thetas, shape_name = shape_functions[shape]()
    
    center_positions_proposals = np.random.uniform(100, 900, (100, cnt, 2))
    center_positions = sample_repulsive_cartesian (proposals=center_positions_proposals, pair_potential='soft_coulomb')
    min_distance = get_min_distance_from_positions (positions= center_positions)
    
    epsilon = 1e-1
    shape_radials *= np.random.uniform(0.6, 1 - epsilon) * min_distance / np.max(shape_radials) 

    letter = label_point(diagram)

    for center_pos in center_positions : 

        diagram, _ = add_fakepoint_at_position_given_label (diagram, point_pos=center_pos, given_label= letter)
        
        diagram = add_polygon(diagram, center_pos, 
                              thetas    = shape_thetas+np.random.uniform(0,np.pi*2),
                              radials   = shape_radials, 
                              alpha     = 1.0
                              )

        diagram, fakepoint_1 = add_fakepoint_at_position(diagram, point_pos= center_pos, label=False)
        diagram, fakepoint_2 = add_fakepoint_at_position(diagram, point_pos= center_positions[random.choice(range(cnt))], label=False)
        line_12 = Line(point1= fakepoint_1, point2= fakepoint_2, label='')
        diagram.lines.append(line_12)

    diagram.entities.append(('cardinal_6', [letter, f'{cnt}']))

# def cardinal_3 (diagram : Diagram ) : 

rules = [] 
rules += [cardinal_1]
rules += [cardinal_2]
rules += [cardinal_3]
rules += [cardinal_4]
rules += [cardinal_5]
rules += [cardinal_6]
