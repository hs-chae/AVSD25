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
def random_length():
        return int(random.uniform(200, 700))


def add_radius(center_x, center_y, radius):
    angle = random_angle()
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    length = f'{random_length()}'
    return (x, y, length)


def is_convex(polygon):
    """
    Checks if a polygon (list of points in order) is strictly convex.
    Returns True if it is convex, False otherwise.
    """
    # A polygon is convex if the sign of cross products of consecutive edges is consistent.
    # polygon = [(x0,y0), (x1,y1), ..., (xn-1,yn-1)]
    # We'll assume the polygon is closed, i.e., polygon[n] = polygon[0] for indexing convenience.
    n = len(polygon)
    # We expect n >= 3
    # Cross product sign storage
    sign = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        x3, y3 = polygon[(i + 2) % n]
        # Vectors: (x2 - x1, y2 - y1) and (x3 - x2, y3 - y2)
        dx1 = x2 - x1
        dy1 = y2 - y1
        dx2 = x3 - x2
        dy2 = y3 - y2
        cross = dx1 * dy2 - dy1 * dx2
        this_sign = 1 if cross > 0 else (-1 if cross < 0 else 0)
        if this_sign == 0:
            # Degenerate case (collinear points). For strict convexity, reject.
            return False
        if sign == 0:
            sign = this_sign
        else:
            # If the sign flips, not convex
            if sign != this_sign:
                return False
    return True


def shift_and_scale_into_bbox(polygon, minx=0, maxx=1000, miny=0, maxy=1000):
    """
    Shift and scale the polygon so that it fits in the specified bounding box.
    """
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    current_minx, current_maxx = min(xs), max(xs)
    current_miny, current_maxy = min(ys), max(ys)

    width = current_maxx - current_minx
    height = current_maxy - current_miny

    # In case the polygon is degenerate, avoid divide-by-zero
    if width == 0 or height == 0:
        return None

    # Scale factor so that polygon fits within bounding box
    scale_x = (maxx - minx) / width
    scale_y = (maxy - miny) / height
    scale = min(scale_x, scale_y)

    # Shift so that min x->0, min y->0, then scale, then shift again if needed
    shifted_scaled = []
    for (x, y) in polygon:
        # shift so that minx->0, miny->0
        x_shifted = x - current_minx
        y_shifted = y - current_miny
        # scale
        x_final = x_shifted * scale + minx
        y_final = y_shifted * scale + miny
        shifted_scaled.append((x_final, y_final))
    return shifted_scaled

def random_convex_polygon(n, parallel_pairs=0, max_tries=1000):
    """
    Generates a random convex polygon with n vertices (3 <= n <= 6)
    in the bounding box [0,1000] x [0,1000],
    and forces exactly 'parallel_pairs' pairs of parallel edges (when possible).

    If it fails to generate a valid polygon within 'max_tries', returns None.
    """
    if n < 3 or n > 6:
        raise ValueError("n must be between 3 and 6.")

    # If n=3 (triangle), you cannot have parallel edges.
    if n == 3 and parallel_pairs > 0:
        print("Warning: A triangle cannot have parallel edges. Setting parallel_pairs=0.")
        parallel_pairs = 0

    for attempt in range(max_tries):
        # Step 1: Generate random angles and radii
        angles = sorted([random.uniform(0, 2 * math.pi) for _ in range(n)])
        # To avoid degenerate (very small or very large polygons), pick a moderate radius range
        radii = [random.uniform(50, 500) for _ in range(n)]

        # Step 2: Construct points in (x, y)
        points = []
        for theta, r in zip(angles, radii):
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            points.append((x, y))

        # Step 3: If we want parallel edges, we forcibly create them.
        # For example, if parallel_pairs=1 and n>=4,
        #   - pick two edges (v0->v1) and (v2->v3) to be parallel.
        #   - we do this by adjusting the direction of (v2->v3).
        # This is a simplistic approach; more sophisticated methods are possible.
        if parallel_pairs > 0 and n >= 4:
            # Let’s try to create the required number of pairs:
            # We will do it pair by pair until we reach parallel_pairs or we run out of edges.
            pairs_assigned = 0
            edge_indices = list(range(n))  # edges: (i -> i+1 % n)

            # We'll pair up edges in sequence: (0->1) with (2->3), (1->2) with (3->4), etc.
            i = 0
            while pairs_assigned < parallel_pairs and i + 2 < n:
                # Edge i -> i+1
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % n]
                vx1 = x2 - x1
                vy1 = y2 - y1

                # Edge i+2 -> i+3
                j = (i + 2) % n
                k = (i + 3) % n
                x3, y3 = points[j]
                x4, y4 = points[k]
                vx2 = x4 - x3
                vy2 = y4 - y3

                # Force (vx2, vy2) to be parallel to (vx1, vy1).
                # We'll keep the same length as (vx2, vy2) initially had, for "randomness".
                length2 = math.hypot(vx2, vy2)
                length1 = math.hypot(vx1, vy1)
                if length1 == 0:
                    # Degenerate edge => skip
                    i += 1
                    continue

                # Direction of (vx1, vy1) -> normalize
                dx1 = vx1 / length1
                dy1 = vy1 / length1

                # Set (vx2, vy2) to be ±(dx1, dy1) * length2
                # Decide the sign randomly (could be parallel or anti-parallel)
                sign = random.choice([-1, 1])
                vx2_new = sign * dx1 * length2
                vy2_new = sign * dy1 * length2

                # Update the coordinates of point k to enforce the new vector
                x4_new = x3 + vx2_new
                y4_new = y3 + vy2_new
                points[k] = (x4_new, y4_new)

                pairs_assigned += 1
                i += 2  # move to the next pair or set of edges

        # Step 4: Check convexity
        if not is_convex(points):
            continue

        # Step 5: Shift and scale into the bounding box
        final_polygon = shift_and_scale_into_bbox(points)
        if final_polygon is None:
            continue  # degeneracy, try again

        # Double-check final_polygon is convex after shift/scale
        if is_convex(final_polygon):
            return final_polygon

    # If we arrive here, we failed to generate after max_tries
    return None


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
                raise ValueError('No possible line found')
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


def angle1(d):
    # generate two lines with an acute angle
    new_labels = []
    p1 = Point(random_coord(),random_coord(),label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(),random_coord(),label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_acute()
        vector2 = rotate_vector(vector, angle)
        scale = random.uniform(0.5, 1.5)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale*vector2[0], p1.y + scale*vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('angle1', [p1.label, p2.label, p3.label]))

    return d

def C_angle1(d):
    # generate two lines with an acute angle
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    new_labels = []
    p1 = Point(random_coord(),random_coord(),label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(),random_coord(),label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_acute()
        vector2 = rotate_vector(vector, angle)
        scale = random.uniform(0.5, 1.5)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale*vector2[0], p1.y + scale*vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d), color = color)
    l2 = Line(p1, p3, label_line(d), color = color)

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('C_angle1', [p1.label, p2.label, p3.label, color]))

    return d

def angle2(d):
    # generate two lines with an obtuse angle
    # generate two lines with an acute angle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_obtuse()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale* vector2[0], p1.y + scale* vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('angle2', [p1.label, p2.label, p3.label]))

    return d

def C_angle2(d):
    # generate two lines with an obtuse angle
    # generate two lines with an acute angle
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_obtuse()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale* vector2[0], p1.y + scale* vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d), color = color)
    l2 = Line(p1, p3, label_line(d), color = color)

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('C_angle2', [p1.label, p2.label, p3.label, color]))

    return d


def angle3(d):
    # generate a right angle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    ind=0
    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break
        if ind > 30:
            return d
        ind += 1

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    while True:
        angle = np.pi/2
        vector2 = rotate_vector(vector, angle)
        scale = random.uniform(0.5, 1.5)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 60:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('angle3', [p1.label, p2.label, p3.label]))
    return d

def C_angle3(d):
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)
    # generate a right angle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    ind=0
    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break
        if ind > 30:
            return d
        ind += 1

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    while True:
        angle = np.pi/2
        vector2 = rotate_vector(vector, angle)
        scale = random.uniform(0.5, 1.5)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 60:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d), color = color)
    l2 = Line(p1, p3, label_line(d), color = color)

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2])
    d.entities.append(('C_angle3', [p1.label, p2.label, p3.label, color]))
    return d


def angle4(d):
    # generate an acute triangle
    new_labels = []
    if len(d.lines) > 0 and random.random() > 0.5:
        l1 = random.choice(d.lines)
        p1 = l1.point1
        p2 = l1.point2
    else:
        p1 = Point(random_coord(), random_coord(), label_point(d))
        new_labels.append(p1.label)

        while True:
            label_2 = label_point(d)
            if label_2 != p1.label:
                new_labels.append(label_2)
                break

        p2 = Point(random_coord(), random_coord(), label_2)
        d.points.extend([p1,p2])
        d.lines.append(Line(p1, p2, label_line(d)))
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_acute()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        V_23 = np.array([p3.x - p2.x, p3.y - p2.y])
        cs_1 = cos_sim((-1) * vector, V_23) #v21 and v23
        cs_2 = cos_sim((-1) * V_23, (-1)*vector2) #v32 and v31

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels and cs_1 > 0 and cs_2 > 0:
            break
        if ind > 30:
            return d
        ind += 1


    l2 = Line(p1, p3, label_line(d))
    l3 = Line(p2, p3, label_line(d))

    d.points.extend([p3])
    d.lines.extend([l2, l3])
    d.entities.append(('angle4', [p1.label, p2.label, p3.label]))

    return d

def C_angle4(d):
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    # generate an acute triangle
    new_labels = []

    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    d.points.extend([p1,p2])
    d.lines.append(Line(p1, p2, label_line(d), color = color))
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_acute()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        V_23 = np.array([p3.x - p2.x, p3.y - p2.y])
        cs_1 = cos_sim((-1) * vector, V_23) #v21 and v23
        cs_2 = cos_sim((-1) * V_23, (-1)*vector2) #v32 and v31

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels and cs_1 > 0 and cs_2 > 0:
            break
        if ind > 30:
            return d
        ind += 1


    l2 = Line(p1, p3, label_line(d), color = color)
    l3 = Line(p2, p3, label_line(d), color = color)

    d.points.extend([p3])
    d.lines.extend([l2, l3])
    d.entities.append(('C_angle4', [p1.label, p2.label, p3.label, color]))

    return d



def angle5(d):
    # generate an obtuse triangle

    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_obtuse()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))
    l3 = Line(p2, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2, l3])
    d.entities.append(('angle5', [p1.label, p2.label, p3.label]))
    return d

def C_angle5(d):
    # generate an obtuse triangle
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = random_obtuse()
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 50:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d), color = color)
    l2 = Line(p1, p3, label_line(d), color = color)
    l3 = Line(p2, p3, label_line(d), color = color)

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2, l3])
    d.entities.append(('C_angle5', [p1.label, p2.label, p3.label, color]))
    return d

def angle6(d):
    # generate a right triangle
    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = np.pi/2
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d))
    l2 = Line(p1, p3, label_line(d))
    l3 = Line(p2, p3, label_line(d))

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2, l3])
    d.entities.append(('angle6', [p1.label, p2.label, p3.label]))
    return d

def C_angle6(d):
    # generate a right triangle
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    new_labels = []
    p1 = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(p1.label)

    while True:
        label_2 = label_point(d)
        if label_2 != p1.label:
            new_labels.append(label_2)
            break

    p2 = Point(random_coord(), random_coord(), label_2)
    vector = np.array([p2.x - p1.x, p2.y - p1.y])

    ind=0
    while True:
        angle = np.pi/2
        scale = random.uniform(0.5, 1.5)
        vector2 = rotate_vector(vector, angle)
        label_3 = label_point(d)
        p3 = Point(p1.x + scale * vector2[0], p1.y + scale * vector2[1], label_3)

        if assert_coord_in_range(p3.x, p3.y) and p3.label not in new_labels:
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(p1, p2, label_line(d), color = color)
    l2 = Line(p1, p3, label_line(d), color = color)
    l3 = Line(p2, p3, label_line(d), color = color)

    d.points.extend([p1, p2, p3])
    d.lines.extend([l1, l2, l3])
    d.entities.append(('C_angle6', [p1.label, p2.label, p3.label, color]))
    return d

def angle7(d):
    # Make  one obtuse angles and one acute angle
    new_labels = []
    O = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(O.label)


    while True:
        label_A = label_point(d)
        if label_A != O.label:
            new_labels.append(label_A)
            break
    A_x, A_y = random_coord(), random_coord()
    A = Point(A_x, A_y, label_A)

    while True:
        label_B = label_point(d)
        if label_B not in new_labels:
            break

    while True:
        label_C = label_point(d)
        if label_C not in new_labels:
            break

    #Choos a clockwise angle
    #If random > 0.5, then angle_1 is acute and else obtuse
    ent = "angle7"
    if random.random() > 0.5:
        angle_1 = random_acute()
        angle_2 = random_obtuse()
    else:
        angle_1 = random_obtuse()
        angle_2 = random_acute()
        ent = "angle7-2"

    ind=0
    #Choose a random scale
    while True:
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(np.array([A_x - O.x, A_y - O.y]), angle_1)
        x, y = O.x + scale1 * vector_B[0], O.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B = Point(O.x + scale1 * vector_B[0], O.y + scale1 * vector_B[1], label_B)
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(np.array([A_x - O.x, A_y - O.y]), -angle_2)
        x, y = O.x + scale2 * vector_C[0], O.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            C = Point(O.x + scale2 * vector_C[0], O.y + scale2 * vector_C[1], label_C)
            break
        if ind > 60:
            return d
        ind += 1

    l1 = Line(O, A, label_line(d))
    l2 = Line(O, B, label_line(d))
    l3 = Line(O, C, label_line(d))

    d.points.extend([O, A, B, C])
    d.lines.extend([l1, l2, l3])

    # if ent = "angle7", then AOB is acute. if ent= angle7-2 AOB is obtuse
    d.entities.append((ent, [O.label, A.label, B.label, C.label]))

    return d

def C_angle7(d):
    # Make  one obtuse angles and one acute angle
    color1, color2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, color1)
    d = remove_color(d, color2)

    new_labels = []
    O = Point(random_coord(), random_coord(), label_point(d))
    new_labels.append(O.label)


    while True:
        label_A = label_point(d)
        if label_A != O.label:
            new_labels.append(label_A)
            break
    A_x, A_y = random_coord(), random_coord()
    A = Point(A_x, A_y, label_A)

    while True:
        label_B = label_point(d)
        if label_B not in new_labels:
            break

    while True:
        label_C = label_point(d)
        if label_C not in new_labels:
            break

    #Choos a clockwise angle
    #If random > 0.5, then angle_1 is acute and else obtuse
    ent = "C_angle7"
    if random.random() > 0.5:
        angle_1 = random_acute()
        angle_2 = random_obtuse()
    else:
        angle_1 = random_obtuse()
        angle_2 = random_acute()
        ent = "C_angle7-2"

    ind=0
    #Choose a random scale
    while True:
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(np.array([A_x - O.x, A_y - O.y]), angle_1)
        x, y = O.x + scale1 * vector_B[0], O.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B = Point(O.x + scale1 * vector_B[0], O.y + scale1 * vector_B[1], label_B)
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(np.array([A_x - O.x, A_y - O.y]), -angle_2)
        x, y = O.x + scale2 * vector_C[0], O.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            C = Point(O.x + scale2 * vector_C[0], O.y + scale2 * vector_C[1], label_C)
            break
        if ind > 60:
            return d
        ind += 1

    l1 = Line(O, A, label_line(d))
    l2 = Line(O, B, label_line(d), color = color1)
    l3 = Line(O, C, label_line(d), color = color2)

    d.points.extend([O, A, B, C])
    d.lines.extend([l1, l2, l3])

    # if ent = "angle7", then AOB is acute. if ent= angle7-2 AOB is obtuse
    d.entities.append((ent, [O.label, A.label, B.label, C.label, color1,  color2]))

    return d



def angle8(d):
    # Make  one acute angle and one obtuse angle and one right angle
    new_labels = []
    while True:
        label1, label2, label3 = label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3:
            new_labels.extend([label1, label2, label3])
            break


    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = np.pi/2
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")

    d.points.extend([O_1, O_2, O_3])
    d.lines.extend([l1, l2, l3, l4, l5, l6])

    tmp = [[O_1, "acute"], [O_2, "obtuse"], [O_3, "right"]]
    random.shuffle(tmp)
    d.entities.append(('angle8', [tmp[0][0].label, tmp[0][1], tmp[1][0].label, tmp[1][1], tmp[2][0].label, tmp[2][1]]))

    return d


def C_angle8(d):
    col1, col2, col3 = random.sample(d.usable_colors, 3)
    d = remove_color(d, col1)
    d = remove_color(d, col2)
    d = remove_color(d, col3)

    # Make  one acute angle and one obtuse angle and one right angle
    new_labels = []
    while True:
        label1, label2, label3 = label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3:
            new_labels.extend([label1, label2, label3])
            break


    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = np.pi/2
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "", color = col1)
    l2 = Line(O_1, B_1, "", color = col1)
    l3 = Line(O_2, A_2, "", color = col2)
    l4 = Line(O_2, B_2, "", color = col2)
    l5 = Line(O_3, A_3, "", color = col3)
    l6 = Line(O_3, B_3, "", color = col3)

    d.points.extend([O_1, O_2, O_3])
    d.lines.extend([l1, l2, l3, l4, l5, l6])

    tmp = [[O_1, "acute", col1], [O_2, "obtuse", col2], [O_3, "right",col3]]
    random.shuffle(tmp)
    d.entities.append(('C_angle8', [tmp[0][0].label, tmp[0][1], tmp[1][0].label, tmp[1][1], tmp[2][0].label, tmp[2][1], tmp[0][2], tmp[1][2], tmp[2][2]]))

    return d


def angle9(d):
    # Make different pairs of lines with one acute, and three obtuse angles
    new_labels = []
    while True:
            label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
            if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
                new_labels.extend([label1, label2, label3, label4])
                break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind = 0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1


    ind = 0
    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    ind=0
    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    ind=0
    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle9', [O_1.label, O_2.label, O_3.label, O_4.label])) #O_1 : ocute, O_2~4 : obtuse

    return d

def C_angle9(d):
    # col1, col2, col3, col4 = random.sample(d.usable_colors, 4)
    # d = remove_color(d, col1)
    # d = remove_color(d, col2)
    # d = remove_color(d, col3)
    # d = remove_color(d, col4)

    col = random.choice(d.usable_colors)
    d = remove_color(d, col)

    # Make different pairs of lines with one acute, and three obtuse angles
    new_labels = []
    while True:
            label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
            if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
                new_labels.extend([label1, label2, label3, label4])
                break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind = 0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1


    ind = 0
    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    ind=0
    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    ind=0
    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "", color = col)
    l2 = Line(O_1, B_1, "", color = col)
    l3 = Line(O_2, A_2, "", color = col)
    l4 = Line(O_2, B_2, "", color = col)
    l5 = Line(O_3, A_3, "", color = col)
    l6 = Line(O_3, B_3, "", color = col)
    l7 = Line(O_4, A_4, "", color = col)
    l8 = Line(O_4, B_4, "", color = col)

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('C_angle9', [O_1.label, O_2.label, O_3.label, O_4.label, col])) #O_1 : ocute, O_2~4 : obtuse

    return d
def angle10(d):
    # Make different pairs of lines with one obtuse, and three acute angles


    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_obtuse()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle10', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def C_angle10(d):
    # Make different pairs of lines with one obtuse, and three acute angles
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_obtuse()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "", color = color)
    l2 = Line(O_1, B_1, "", color = color)
    l3 = Line(O_2, A_2, "", color = color)
    l4 = Line(O_2, B_2, "", color = color)
    l5 = Line(O_3, A_3, "", color = color)
    l6 = Line(O_3, B_3, "", color = color)
    l7 = Line(O_4, A_4, "", color = color)
    l8 = Line(O_4, B_4, "", color = color)

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('C_angle10', [O_1.label, O_2.label, O_3.label, O_4.label, color]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def angle11(d):
    # Make different pairs of lines with one right, and three acute angles
    new_labels = []

    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = np.pi/2
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle11', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse
    return d

def C_angle11(d):
    # Make different pairs of lines with one right, and three acute angles
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    new_labels = []

    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = np.pi/2
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "", color = color)
    l2 = Line(O_1, B_1, "", color = color)
    l3 = Line(O_2, A_2, "", color = color)
    l4 = Line(O_2, B_2, "", color = color)
    l5 = Line(O_3, A_3, "", color = color)
    l6 = Line(O_3, B_3, "", color = color)
    l7 = Line(O_4, A_4, "", color = color)
    l8 = Line(O_4, B_4, "", color = color)

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('C_angle11', [O_1.label, O_2.label, O_3.label, O_4.label, color]))  # O_1 : ocute, O_2~4 : obtuse
    return d

def C_angle12(d):
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    # Make different pairs of lines with one right, and three obtuse angles
    new_labels = []
    while True:
      label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
      if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
          new_labels.extend([label1, label2, label3, label4])
          break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
      angle_1 = np.pi/2
      scale1 = random.uniform(0.5, 1.5)
      vector_B = rotate_vector(vector_1, angle_1)
      x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
      if assert_coord_in_range(x, y):
          B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
          break
      if ind > 30:
          return d
      ind += 1

    while True:
      angle_2 = random_obtuse()
      scale2 = random.uniform(0.5, 1.5)
      vector_C = rotate_vector(vector_2, angle_2)
      x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
      if assert_coord_in_range(x, y):
          B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
          break
      if ind > 60:
          return d
      ind += 1

    while True:
      angle_3 = random_obtuse()
      scale3 = random.uniform(0.5, 1.5)
      vector_D = rotate_vector(vector_3, angle_3)
      x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
      if assert_coord_in_range(x, y):
          B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
          break
      if ind > 90:
          return d
      ind += 1

    while True:
      angle_4 = random_obtuse()
      scale4 = random.uniform(0.5, 1.5)
      vector_E = rotate_vector(vector_4, angle_4)
      x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
      if assert_coord_in_range(x, y):
          B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
          break
      if ind > 120:
          return d
      ind += 1

    l1 = Line(O_1, A_1, "", color = color)
    l2 = Line(O_1, B_1, "", color = color)
    l3 = Line(O_2, A_2, "", color = color)
    l4 = Line(O_2, B_2, "", color = color)
    l5 = Line(O_3, A_3, "", color = color)
    l6 = Line(O_3, B_3, "", color = color)
    l7 = Line(O_4, A_4, "", color = color)
    l8 = Line(O_4, B_4, "", color = color)

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('C_angle12', [O_1.label, O_2.label, O_3.label, O_4.label,color]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def angle12(d):
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    # Make different pairs of lines with one right, and three obtuse angles
    new_labels = []
    while True:
      label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
      if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
          new_labels.extend([label1, label2, label3, label4])
          break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
      angle_1 = np.pi/2
      scale1 = random.uniform(0.5, 1.5)
      vector_B = rotate_vector(vector_1, angle_1)
      x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
      if assert_coord_in_range(x, y):
          B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
          break
      if ind > 30:
          return d
      ind += 1

    while True:
      angle_2 = random_obtuse()
      scale2 = random.uniform(0.5, 1.5)
      vector_C = rotate_vector(vector_2, angle_2)
      x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
      if assert_coord_in_range(x, y):
          B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
          break
      if ind > 60:
          return d
      ind += 1

    while True:
      angle_3 = random_obtuse()
      scale3 = random.uniform(0.5, 1.5)
      vector_D = rotate_vector(vector_3, angle_3)
      x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
      if assert_coord_in_range(x, y):
          B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
          break
      if ind > 90:
          return d
      ind += 1

    while True:
      angle_4 = random_obtuse()
      scale4 = random.uniform(0.5, 1.5)
      vector_E = rotate_vector(vector_4, angle_4)
      x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
      if assert_coord_in_range(x, y):
          B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
          break
      if ind > 120:
          return d
      ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle12', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def angle13(d):
    # Make different pairs of lines with two acute, and two obtuse angles
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    ind=0
    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    ind = 0
    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 60:
            return d
        ind += 1


    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle13', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def C_angle13(d):
    color = random.choice(d.usable_colors)
    d = remove_color(d, color)

    # Make different pairs of lines with two acute, and two obtuse angles
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    ind=0
    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    ind = 0
    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 60:
            return d
        ind += 1


    l1 = Line(O_1, A_1, "", color = color)
    l2 = Line(O_1, B_1, "", color = color)
    l3 = Line(O_2, A_2, "", color = color)
    l4 = Line(O_2, B_2, "", color = color)
    l5 = Line(O_3, A_3, "", color = color)
    l6 = Line(O_3, B_3, "", color = color)
    l7 = Line(O_4, A_4, "", color = color)
    l8 = Line(O_4, B_4, "", color = color)

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('C_angle13', [O_1.label, O_2.label, O_3.label, O_4.label, color]))  # O_1 : ocute, O_2~4 : obtuse

    return d



def angle14(d):
    # Make AOB + COD acute
    new_labels = [ ]
    while True:
        label1, label2 = label_point(d), label_point(d)
        if label1 != label2:
            new_labels.extend([label1, label2])
            break

    O1 = Point(random_coord(), random_coord(), label1)
    O2 = Point(random_coord(), random_coord(), label2)
    A1 = Point(random_coord(), random_coord(), "")
    A2 = Point(random_coord(), random_coord(), "")

    vector1 = np.array([A1.x - O1.x, A1.y - O1.y])
    vector2 = np.array([A2.x - O2.x, A2.y - O2.y])

    ind = 0
    while True:
        total_angle = random.uniform(np.pi/4, np.pi/2)
        angle1 = random.uniform(np.pi/8, total_angle-np.pi/8)
        angle2 = total_angle - angle1

        scale1 = random.uniform(0.5, 1.5)
        vector_A = rotate_vector(vector1, angle1)
        x1, y1 = O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1]

        scale2 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector2, angle2)
        x2, y2 = O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1]

        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            B1 = Point(O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1], "")
            B2 = Point(O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1], "")
            break

        if ind > 100:
            raise ValueError("Cannot find a valid point")
        ind += 1

    l1 = Line(O1, A1, "")
    l2 = Line(O1, B1, "")
    l3 = Line(O2, A2, "")
    l4 = Line(O2, B2, "")

    d.points.extend([O1, O2])
    d.lines.extend([l1, l2, l3, l4])
    d.entities.append(('angle14', [O1.label, O2.label]))

    return d


def C_angle14(d):
    # Make AOB + COD acute
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)


    new_labels = [ ]
    while True:
        label1, label2 = label_point(d), label_point(d)
        if label1 != label2:
            new_labels.extend([label1, label2])
            break

    O1 = Point(random_coord(), random_coord(), label1)
    O2 = Point(random_coord(), random_coord(), label2)
    A1 = Point(random_coord(), random_coord(), "")
    A2 = Point(random_coord(), random_coord(), "")

    vector1 = np.array([A1.x - O1.x, A1.y - O1.y])
    vector2 = np.array([A2.x - O2.x, A2.y - O2.y])

    ind = 0
    while True:
        total_angle = random.uniform(np.pi/4, np.pi/2)
        angle1 = random.uniform(np.pi/8, total_angle-np.pi/8)
        angle2 = total_angle - angle1

        scale1 = random.uniform(0.5, 1.5)
        vector_A = rotate_vector(vector1, angle1)
        x1, y1 = O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1]

        scale2 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector2, angle2)
        x2, y2 = O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1]

        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            B1 = Point(O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1], "")
            B2 = Point(O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1], "")
            break

        if ind > 100:
            raise ValueError("Cannot find a valid point")
        ind += 1

    l1 = Line(O1, A1, "", color = col1)
    l2 = Line(O1, B1, "", color = col1)
    l3 = Line(O2, A2, "", color = col2)
    l4 = Line(O2, B2, "", color = col2)

    d.points.extend([O1, O2])
    d.lines.extend([l1, l2, l3, l4])
    d.entities.append(('C_angle14', [O1.label, O2.label, col1, col2]))

    return d

def angle15(d):
    # Make AOB + BOC obtuse
    new_labels = []
    while True:
        label1, label2 = label_point(d), label_point(d)
        if label1 != label2:
            new_labels.extend([label1, label2])
            break

    O1 = Point(random_coord(), random_coord(), label1)
    O2 = Point(random_coord(), random_coord(), label2)
    A1 = Point(random_coord(), random_coord(), "")
    A2 = Point(random_coord(), random_coord(), "")

    vector1 = np.array([A1.x - O1.x, A1.y - O1.y])
    vector2 = np.array([A2.x - O2.x, A2.y - O2.y])

    ind = 0
    while True:
        total_angle = random.uniform(np.pi / 2, np.pi * 0.9 )
        angle1 = random.uniform(np.pi / 6, total_angle - np.pi / 6)
        angle2 = total_angle - angle1

        scale1 = random.uniform(0.5, 1.5)
        vector_A = rotate_vector(vector1, angle1)
        x1, y1 = O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1]

        scale2 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector2, angle2)
        x2, y2 = O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1]

        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            B1 = Point(O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1], "")
            B2 = Point(O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1], "")
            break

        if ind > 100:
            raise ValueError("Cannot find a valid point")
        ind += 1

    l1 = Line(O1, A1, "")
    l2 = Line(O1, B1, "")
    l3 = Line(O2, A2, "")
    l4 = Line(O2, B2, "")

    d.points.extend([O1, O2])
    d.lines.extend([l1, l2, l3, l4])
    d.entities.append(('angle15', [O1.label, O2.label]))

    return d

def C_angle15(d):
    col1, col2 = random.sample(d.usable_colors, 2)
    d = remove_color(d, col1)
    d = remove_color(d, col2)


    # Make AOB + BOC obtuse
    new_labels = []
    while True:
        label1, label2 = label_point(d), label_point(d)
        if label1 != label2:
            new_labels.extend([label1, label2])
            break

    O1 = Point(random_coord(), random_coord(), label1)
    O2 = Point(random_coord(), random_coord(), label2)
    A1 = Point(random_coord(), random_coord(), "")
    A2 = Point(random_coord(), random_coord(), "")

    vector1 = np.array([A1.x - O1.x, A1.y - O1.y])
    vector2 = np.array([A2.x - O2.x, A2.y - O2.y])

    ind = 0
    while True:
        total_angle = random.uniform(np.pi / 2, np.pi * 0.9 )
        angle1 = random.uniform(np.pi / 6, total_angle - np.pi / 6)
        angle2 = total_angle - angle1

        scale1 = random.uniform(0.5, 1.5)
        vector_A = rotate_vector(vector1, angle1)
        x1, y1 = O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1]

        scale2 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector2, angle2)
        x2, y2 = O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1]

        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            B1 = Point(O1.x + scale1 * vector_A[0], O1.y + scale1 * vector_A[1], "")
            B2 = Point(O2.x + scale2 * vector_B[0], O2.y + scale2 * vector_B[1], "")
            break

        if ind > 100:
            raise ValueError("Cannot find a valid point")
        ind += 1

    l1 = Line(O1, A1, "", color = col1)
    l2 = Line(O1, B1, "", color = col1)
    l3 = Line(O2, A2, "", color = col2)
    l4 = Line(O2, B2, "", color = col2)

    d.points.extend([O1, O2])
    d.lines.extend([l1, l2, l3, l4])
    d.entities.append(('C_angle15', [O1.label, O2.label, col1, col2]))

    return d

def angle16(d):

    # Make different pairs of lines with all acute.
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 110:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle16', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def C_angle16(d):
    col1, col2, col3, col4 = random.sample(d.usable_colors, 4)
    d = remove_color(d, col1)
    d = remove_color(d, col2)
    d = remove_color(d, col3)
    d = remove_color(d, col4)


    # Make different pairs of lines with all acute.
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_acute()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_acute()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = random_acute()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    while True:
        angle_4 = random_acute()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 110:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "", color = col1)
    l2 = Line(O_1, B_1, "", color = col1)
    l3 = Line(O_2, A_2, "", color = col2)
    l4 = Line(O_2, B_2, "", color = col2)
    l5 = Line(O_3, A_3, "", color = col3)
    l6 = Line(O_3, B_3, "", color = col3)
    l7 = Line(O_4, A_4, "", color = col4)
    l8 = Line(O_4, B_4, "", color = col4)

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('C_angle16', [O_1.label, O_2.label, O_3.label, O_4.label, col1, col2, col3, col4]))  # O_1 : ocute, O_2~4 : obtuse

    return d


def angle17(d):
    # Make different pairs of lines with all acute.
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_obtuse()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "")
    l2 = Line(O_1, B_1, "")
    l3 = Line(O_2, A_2, "")
    l4 = Line(O_2, B_2, "")
    l5 = Line(O_3, A_3, "")
    l6 = Line(O_3, B_3, "")
    l7 = Line(O_4, A_4, "")
    l8 = Line(O_4, B_4, "")

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle17', [O_1.label, O_2.label, O_3.label, O_4.label]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def C_angle17(d):
    col1, col2, col3, col4 = random.sample(d.usable_colors, 4)
    d = remove_color(d, col1)
    d = remove_color(d, col2)
    d = remove_color(d, col3)
    d = remove_color(d, col4)

    # Make different pairs of lines with all acute.
    new_labels = []
    while True:
        label1, label2, label3, label4 = label_point(d), label_point(d), label_point(d), label_point(d)
        if label1 != label2 and label2 != label3 and label1 != label3 and label1 != label4 and label2 != label4 and label3 != label4:
            new_labels.extend([label1, label2, label3, label4])
            break

    O_1 = Point(random_coord(), random_coord(), label1)
    O_2 = Point(random_coord(), random_coord(), label2)
    O_3 = Point(random_coord(), random_coord(), label3)
    O_4 = Point(random_coord(), random_coord(), label4)

    A_1 = Point(random_coord(), random_coord(), "")
    A_2 = Point(random_coord(), random_coord(), "")
    A_3 = Point(random_coord(), random_coord(), "")
    A_4 = Point(random_coord(), random_coord(), "")

    vector_1 = np.array([A_1.x - O_1.x, A_1.y - O_1.y])
    vector_2 = np.array([A_2.x - O_2.x, A_2.y - O_2.y])
    vector_3 = np.array([A_3.x - O_3.x, A_3.y - O_3.y])
    vector_4 = np.array([A_4.x - O_4.x, A_4.y - O_4.y])

    ind=0
    while True:
        angle_1 = random_obtuse()
        scale1 = random.uniform(0.5, 1.5)
        vector_B = rotate_vector(vector_1, angle_1)
        x, y = O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1]
        if assert_coord_in_range(x, y):
            B_1 = Point(O_1.x + scale1 * vector_B[0], O_1.y + scale1 * vector_B[1], "")
            break
        if ind > 30:
            return d
        ind += 1

    while True:
        angle_2 = random_obtuse()
        scale2 = random.uniform(0.5, 1.5)
        vector_C = rotate_vector(vector_2, angle_2)
        x, y = O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1]
        if assert_coord_in_range(x, y):
            B_2 = Point(O_2.x + scale2 * vector_C[0], O_2.y + scale2 * vector_C[1], "")
            break
        if ind > 60:
            return d
        ind += 1

    while True:
        angle_3 = random_obtuse()
        scale3 = random.uniform(0.5, 1.5)
        vector_D = rotate_vector(vector_3, angle_3)
        x, y = O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1]
        if assert_coord_in_range(x, y):
            B_3 = Point(O_3.x + scale3 * vector_D[0], O_3.y + scale3 * vector_D[1], "")
            break
        if ind > 90:
            return d
        ind += 1

    while True:
        angle_4 = random_obtuse()
        scale4 = random.uniform(0.5, 1.5)
        vector_E = rotate_vector(vector_4, angle_4)
        x, y = O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1]
        if assert_coord_in_range(x, y):
            B_4 = Point(O_4.x + scale4 * vector_E[0], O_4.y + scale4 * vector_E[1], "")
            break
        if ind > 120:
            return d
        ind += 1

    l1 = Line(O_1, A_1, "", color = col1)
    l2 = Line(O_1, B_1, "", color = col1)
    l3 = Line(O_2, A_2, "", color = col2)
    l4 = Line(O_2, B_2, "", color = col2)
    l5 = Line(O_3, A_3, "", color = col3)
    l6 = Line(O_3, B_3, "", color = col3)
    l7 = Line(O_4, A_4, "", color = col4)
    l8 = Line(O_4, B_4, "", color = col4)

    d.points.extend([O_1, O_2, O_3, O_4])
    d.lines.extend([l1, l2, l3, l4, l5, l6, l7, l8])

    d.entities.append(('angle17', [O_1.label, O_2.label, O_3.label, O_4.label, col1, col2, col3, col4]))  # O_1 : ocute, O_2~4 : obtuse

    return d

def angle18(d):
    #Which line n-sects?
    d.points = []
    d.lines = []

    #Choose bisect / trisect / quadrisect
    nun_sections = random.choice([2,2,2,3,3])

    #Choose labels
    labels = random.sample(capitals.candidates, nun_sections*2+3)
    label_O, label_A1, label_A2, label_B1, label_B2 = labels[0], labels[1], labels[2], labels[3], labels[4]

    #Choose color types
    color_type = random.choice([1,2,3])
    if color_type == 1: # Every lines have the same color
        if random.choice([True, False]):
            wrapper_color = 'black'
        else: wrapper_color = random.choice(d.usable_colors)
        other_color = wrapper_color
        d = remove_color(d, wrapper_color)
    elif color_type == 2: # Only wrapper colors are different
        wrapper_color, other_color = random.sample(d.usable_colors, 2)
        d = remove_color(d, wrapper_color)
        d = remove_color(d, other_color)
    else : wrapper_color, other_color = None, None #Type 3: all colors are different

    #Choose the wrapper lines
        #Choose the full angle
    full_angle = random.uniform(np.pi/4, np.pi)

    ind = 0
    while True:
        O = Point(random_coord(), random_coord(), label_O) # Choose the intersection point
        A1 = Point(random_coord(), random_coord(), label_A1)

        #rotate 0A1 to get B1
        vec_A1 = np.array([A1.x - O.x, A1.y - O.y])
        vec_B1  = rotate_vector(vec_A1, full_angle)
        scale = random.uniform(0.5, 1.5)
        x, y = O.x + scale * vec_B1[0], O.y + scale * vec_B1[1]
        if assert_coord_in_range(x, y) and ((A1.x - O.x)**2 + (A1.y - O.y)**2) > 10000:
            B1 = Point(x, y, label_B1)
            break

        if ind > 100:
            return d
        ind += 1

    # Try to extend A1, B2 to the other side of O if the space allows
    vec_A1 = np.array([A1.x - O.x, A1.y - O.y])
    scale = random.uniform(0.5, 1.5)

    A2x, A2y = O.x - scale * vec_A1[0], O.y - scale * vec_A1[1]
    if assert_coord_in_range(A2x, A2y):
        A2 = Point(A2x, A2y, label_A2)
    else: A2 = O

    vec_B1 = np.array([B1.x - O.x, B1.y - O.y])
    scale = random.uniform(0.5, 1.5)

    B2x, B2y = O.x - scale * vec_B1[0], O.y - scale * vec_B1[1]
    if assert_coord_in_range(B2x, B2y):
        B2 = Point(B2x, B2y, label_B2)
    else:
        B2 = O



    #Choose the n-secting lines
    angle = full_angle / nun_sections
    secting_endpoints_1 = []
    secting_endpoints_2 = []

    for i in range(nun_sections-1):
        vec = rotate_vector(vec_A1, angle * (i + 1))

        ind = 0
        while True:
            scale = random.uniform(0.3, 2)
            x, y = O.x + scale * vec[0], O.y + scale * vec[1]
            if assert_coord_in_range(x, y):
                secting_endpoints_1.append(Point(x, y, labels[2*i+5]))
                break

            if ind > 100:
                return d
            ind += 1

        scale = random.uniform(0.5, 1.5)
        x2, y2 = O.x - scale * vec[0], O.y - scale * vec[1]
        if assert_coord_in_range(x2, y2):
            secting_endpoints_2.append(Point(x2, y2, labels[2*i+6]))
        else:
            secting_endpoints_2.append(O)

    #Choose noisy lines to make the problem harder
    num_noisy_lines = random.randint(1, 3)
    noisy_lines = []

    for i in range(num_noisy_lines):
        ind = 0
        while True:
            angle = random.uniform(np.pi/8, full_angle *0.9)
            scale = random.uniform(0.5, 1.5)
            vec = rotate_vector(vec_A1, angle)
            x, y = O.x + scale * vec[0], O.y + scale * vec[1]
            if assert_coord_in_range(x, y) and (angle - full_angle/nun_sections)**2 > 0.1 and (angle - 2*full_angle/nun_sections)**2 > 0.1 and (angle - 3*full_angle/nun_sections)**2 > 0.1:
                break

            if ind > 100:
                return d
            ind += 1

        ind = 0
        while True:
            noisy_label = label_point(d)
            if noisy_label not in labels:
                labels.append(noisy_label)
                break

            if ind > 100:
                return d

            ind += 1

        #extend the line to the other side of O
        scale = random.uniform(0.5, 1.5)
        x2, y2 = O.x - scale * vec[0], O.y - scale * vec[1]

        #Choose color type
        if color_type == 3: #All colors are different
            color = random.choice(d.usable_colors)
            d = remove_color(d, color)
        else:
            color = other_color


        if assert_coord_in_range(x2, y2):
            ind = 0
            while True:
                noisy_label2 = label_point(d)
                if noisy_label2 not in labels:
                    labels.append(noisy_label2)
                    break
                if ind > 100:
                    return d
                ind += 1

            noisy_lines.append(Line(Point(x, y, noisy_label), Point(x2, y2, noisy_label2), "", color = color))
        else:
            noisy_lines.append(Line(Point(x, y, noisy_label), O, "", color = color))


    #Add points and lines
    d.points.append(O)

    wrapper_points = [A1, A2, B1, B2]
    d.points.extend(point for point in wrapper_points if point != O)
    d.points.extend([point for point in secting_endpoints_1 if point != O])
    d.points.extend([point for point in secting_endpoints_2 if point != O])
    d.points.extend([line.point1 for line in noisy_lines if line.point1 != O])
    d.points.extend([line.point2 for line in noisy_lines if line.point2 != O])

    if color_type == 3:
        colors_list = random.sample(d.usable_colors, nun_sections + 1)
    else:
        colors_list = [wrapper_color, wrapper_color] + [other_color for i in range(nun_sections - 1)]

    wrapper_lines = [Line(A1, A2, "", color = colors_list[0]), Line(B1, B2, "", color = colors_list[1])]
    n_secting_lines = [Line(secting_endpoints_1[i], secting_endpoints_2[i], "", color = colors_list[i+2]) for i in
                       range(nun_sections - 1)]

    d.lines.extend(wrapper_lines)
    d.lines.extend(n_secting_lines)
    d.lines.extend(noisy_lines)

    if color_type == 3:
        d.points = []
        color_candidates = colors_list[2:] + [line.color for line in noisy_lines]
        random.shuffle(color_candidates)
        color_candidates_1 = ""
        color_candidates_2 = ""
        for i in range(len(color_candidates)):
            color_candidates_1 += color_candidates[i] + ", "
            color_candidates_2 += color_candidates[i] + "/"
        d.entities.append((f'angle18-{nun_sections}-3',colors_list + [color, color_candidates_1[:-2], color_candidates_2[:-1]] ))
    elif color_type == 2:
        d.entities.append((f'angle18-{nun_sections}-2',[wrapper_color, other_color] + [f'{secting_endpoints_1[i].label}{secting_endpoints_2[i].label}' for i in range(len(secting_endpoints_2))] + [f'{line.point1.label}{line.point2.label}' for line in noisy_lines]))
    else:
        d.entities.append((f'angle18-{nun_sections}-1', [f'{A1.label}{O.label}{B1.label}', f'{A1.label}{A2.label}', f'{B1.label}{B2.label}'] + [f'{secting_endpoints_1[i].label}{secting_endpoints_2[i].label}' for i in range(len(secting_endpoints_2))] + [f'{line.point1.label}{line.point2.label}' for line in noisy_lines]))

    return d


def angle19(d):
    # Choose the largest / smallest angle
    d.points = []
    d.lines = []


    #Choose largest/smallest
    question_type = random.choice(["largest", "smallest"])

    #Choose the number of angles
    num_angles = random.randint(3, 8)

    #Choose the labels
    labels = random.sample(capitals.candidates, num_angles)

    #Choose the color type
    color_type = random.choice([1,2])
    if color_type == 1: #All colors are the same
        color = random.choice(d.usable_colors)
        d = remove_color(d, color)
        colors = [color for i in range(num_angles)]
    else:
        colors = random.sample(d.usable_colors, num_angles)
        for color in colors:
            d = remove_color(d, color)

    #Choose the angles
    angles = []

    if question_type == "largest":
        ans_angle = random.uniform(np.pi/4, 0.9 * np.pi)
    else:
        ans_angle = random.uniform(0.1 * np.pi, 3*np.pi/4)
    angles.append(ans_angle)

    for i in range(num_angles - 1):
        if question_type == "largest":
            angle = random.uniform(0, ans_angle * 0.85)
        else:
            angle = random.uniform(ans_angle * 1.15, np.pi)

        angles.append(angle)

    #Choose the intersection points
    center_coordinates = []
    for i in range(num_angles):
        ind = 0
        while True:
            x,y = random.choice([1,3,5,7,9])* 100, random.choice([1,3,5,7,9]) * 100
            if (x,y) not in center_coordinates:
                break
            if ind > 100:
                return d
            ind += 1

        center_coordinates.append((x,y))


    #Generate two lines for each angle
    lines1 = []
    lines2 = []

    for i in range(num_angles):
        rotation = random.uniform(0, 2* np.pi)
        vec1 = np.array([np.cos(rotation), np.sin(rotation)])
        vec2 = rotate_vector(vec1, angles[i])

        center = Point(center_coordinates[i][0], center_coordinates[i][1], labels[i], color = "transparent")

        scale = random.uniform(25, 125)
        x1, y1 = center.x + scale * vec1[0], center.y + scale * vec1[1]
        scale = random.uniform(25, 125)
        x2, y2 = center.x + scale * vec2[0], center.y + scale * vec2[1]

        lines1.append(Line(center, Point(x1, y1, ""), "", color = colors[i]))
        lines2.append(Line(center, Point(x2, y2, ""), "", color = colors[i]))


    d.points.extend([line.point1 for line in lines1])
    d.lines.extend(lines1)
    d.lines.extend(lines2)



    if color_type == 1: # All angles have same color
        answer_label = labels[0]
        wrong_label = labels[1]

        random.shuffle(labels)
        candidates1, candidates2 = "", ""
        for label in labels:
            candidates1 += label + ", "
            candidates2 += label + "/"

        d.entities.append((f"angle19-{question_type}-1", [colors[0], answer_label, wrong_label, candidates1[:-2], candidates2[:-1]]))

    else: #All labels have different colors
        answer_color = colors[0]
        wrong_color = colors[1]

        random.shuffle(colors)
        candidates1, candidates2 = "", ""
        for color in colors:
            candidates1 += color + ", "
            candidates2 += color + "/"

        d.entities.append((f"angle19-{question_type}-2", [answer_color, wrong_color, candidates1[:-2], candidates2[:-1]]))
        d.points = []

    return d



def angle20(d):
    # Find the equal angle
    # Choose the largest / smallest angle
    d.points = []
    d.lines = []


    # Choose the number of angles
    num_angles = random.choice([3,3,3,4,4,5,5,6,7,8])

    # Choose the labels
    labels = random.sample(capitals.candidates, num_angles)

    # Choose the color type
    color_type = random.choice([1, 2])
    if color_type == 1:  # All colors are the same
        color = random.choice(d.usable_colors)
        d = remove_color(d, color)
        colors = [color for i in range(num_angles)]
    else:
        colors = random.sample(d.usable_colors, num_angles)
        for color in colors:
            d = remove_color(d, color)

    # Choose the angles


    ans_angle = random.uniform(np.pi / 9,  np.pi)
    angles = [ans_angle, ans_angle]

    for i in range(num_angles - 2):
        while True:
            angle = random.uniform(np.pi/9, np.pi)
            if abs(angle - ans_angle) > np.pi/9:
                break
        angles.append(angle)



    # Choose the intersection points
    center_coordinates = []
    for i in range(num_angles):
        ind = 0
        while True:
            x, y = random.choice([1, 3, 5, 7, 9]) * 100, random.choice([1, 3, 5, 7, 9]) * 100
            if (x, y) not in center_coordinates:
                break
            if ind > 100:
                return d
            ind += 1

        center_coordinates.append((x, y))

    # Generate two lines for each angle
    lines1 = []
    lines2 = []

    for i in range(num_angles):
        rotation = random.uniform(0, 2 * np.pi)
        vec1 = np.array([np.cos(rotation), np.sin(rotation)])
        vec2 = rotate_vector(vec1, angles[i])

        center = Point(center_coordinates[i][0], center_coordinates[i][1], labels[i], color="transparent")

        scale = random.uniform(25, 200)
        x1, y1 = center.x + scale * vec1[0], center.y + scale * vec1[1]
        scale = random.uniform(25, 200)
        x2, y2 = center.x + scale * vec2[0], center.y + scale * vec2[1]

        lines1.append(Line(center, Point(x1, y1, ""), "", color=colors[i]))
        lines2.append(Line(center, Point(x2, y2, ""), "", color=colors[i]))

    d.points.extend([line.point1 for line in lines1])
    d.lines.extend(lines1)
    d.lines.extend(lines2)

    if color_type == 1:  # All angles have same color
        answer_label1 = labels[0]
        answer_label2 = labels[1]
        wrong_label = labels[2]

        random.shuffle(labels)
        candidates1, candidates2 = "", ""
        for label in labels:
            candidates1 += label + ", "
            candidates2 += label + "/"

        d.entities.append(
            (f"angle20-1", [colors[0], answer_label1, answer_label2, wrong_label, candidates1[:-2], candidates2[:-1]]))

    else:  # All labels have different colors
        answer_color = colors[0]
        answer_color2 = colors[1]
        wrong_color = colors[2]
        random.shuffle(colors)
        candidates1, candidates2 = "", ""
        for color in colors:
            candidates1 += color + ", "
            candidates2 += color + "/"

        d.entities.append(
            (f"angle20-2", [answer_color, answer_color2, wrong_color, candidates1[:-2], candidates2[:-1]]))
        d.points = []

    return d



#
#
# def angle21(d):
#     #Find the largest angle in a polygon
#     num_edges = random.choice([3, 4])
#
#     type = random.choice(["smallest","largest"])
#
#     # 2) Choose the polygon’s vertex labels
#     labels = random.sample(capitals.candidates, num_edges)
#
#     # 3) Choose the color type: (1) all same color, (2) all different colors
#     color_type = random.choice([1, 2])
#     if color_type == 1:
#         color = random.choice(d.usable_colors)
#         d = remove_color(d, color)
#         colors = [color for _ in range(num_edges)]
#     else:
#         colors = random.sample(d.usable_colors, num_edges)
#         for c in colors:
#             d = remove_color(d, c)
#
#     # 4) Choose the angles
#     angles = []
#     if num_edges == 3:
#         if type == "largest":
#             ans_angle = random.uniform(np.pi/2, np.pi)
#             angle1 =  random.uniform(0, np.pi - ans_angle)
#             angle2 = np.pi - ans_angle - angle1
#         else:
#             ans_angle = random.uniform(0, np.pi/4)
#             angle1 = random.uniform(np.pi/4,  np.pi/2)
#             angle2 = np.pi - ans_angle - angle1
#         angles = [ans_angle, angle1, angle2]
#
#     else:
#         if type == "largest":
#             ans_angle = random.uniform(np.pi/2, np.pi)
#             while True:
#                 angle1 = random.uniform(0, ans_angle)
#                 angle2 = random.uniform(0, ans_angle)
#                 angle3 = 2*np.pi - ans_angle - angle1 - angle2
#                 if angle3 < np.pi:
#                     break
#
#         else:
#             ans_angle = random.uniform(0, np.pi/4)
#             while True:
#                 angle1 = random.uniform(np.pi/4, np.pi/2)
#                 angle2 = random.uniform(np.pi/4, np.pi/2)
#                 angle3 = 2*np.pi - ans_angle - angle1 - angle2
#                 if angle3 < np.pi:
#                     break
#
#         angles = [angle1, angle2, angle3]
#         random.shuffle(angles)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     return d

def angle22(d):
    #Angle bigger than 180 with arcs

    d. points = []
    d.lines = []

    #Choose the number of angles
    num_angles = random.choice([2,3,4])

    # Choose the labels
    labels = random.sample(capitals.candidates, num_angles)
    colors = random.sample(d.usable_colors, num_angles)
    for color in colors:
        d = remove_color(d, color)

    ans_angle = random.uniform(np.pi/2, 2*np.pi)
    angles = [ans_angle]
    for _ in range(num_angles-1):
        angle = random.uniform(np.pi/9, ans_angle*0.85)
        angles.append(angle)


    # Choose the intersection points
    center_coordinates = []
    for i in range(num_angles):
        ind = 0
        while True:
            x, y = random.choice([2, 4, 6, 8]) * 100, random.choice([2,4,6,8]) * 100
            if (x, y) not in center_coordinates:
                break
            if ind > 100:
                return d
            ind += 1

        center_coordinates.append((x, y))

    # Generate two lines for each angle
    lines1 = []
    lines2 = []

    for i in range(num_angles):
        rotation = random.uniform(0, 2 * np.pi)
        vec1 = np.array([np.cos(rotation), np.sin(rotation)])
        vec2 = rotate_vector(vec1, angles[i])

        center = Point(center_coordinates[i][0], center_coordinates[i][1], labels[i], color="transparent")

        scale = random.uniform(50, 200)
        x1, y1 = center.x + scale * vec1[0], center.y + scale * vec1[1]
        scale = random.uniform(50, 200)
        x2, y2 = center.x + scale * vec2[0], center.y + scale * vec2[1]

        lines1.append(Line(center, Point(x1, y1, ""), "", color='black'))
        lines2.append(Line(center, Point(x2, y2, ""), "", color='black'))

    d.points.extend([line.point1 for line in lines1])
    d.lines.extend(lines1)
    d.lines.extend(lines2)
    answer_label1 = labels[0]
    wrong_label = labels[1]

    answer_color = colors[0]
    wrong_color = colors[1]
    random.shuffle(colors)

    # line1, line2, intersection, ang_label = ang

    for i in range(num_angles):
        # print(f"color, lable: {colors[i]}, {labels[i]}")
        d.angles.append((lines1[i], angles[i], lines1[i].point1, colors[i], labels[i]))


    if random.choice([True, False]):

        random.shuffle(labels)
        candidates1, candidates2 = "", ""
        for label in labels:
            candidates1 += label + ", "
            candidates2 += label + "/"

        d.entities.append(
            (f"angle22-1", [colors[0], answer_label1, wrong_label, candidates1[:-2], candidates2[:-1]]))
    else:
        candidates1, candidates2 = "", ""
        for color in colors:
            candidates1 += color + ", "
            candidates2 += color + "/"

        d.entities.append(
            (f"angle22-2", [answer_color, wrong_color, candidates1[:-2], candidates2[:-1]]))


    return d


















#Angle bigger than 180 with arcs


#Find the largest angle in a polygon
#vertical angles
#slope





