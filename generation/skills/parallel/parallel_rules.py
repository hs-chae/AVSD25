import matplotlib.pyplot as plt
import numpy as np
from .labels import *
import random
import math
import json
from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL,seconds) #used timer instead of alarm
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator

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
            return diagram


        ind+=1

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
        if ind> 30:
            return d
        ind += 1
    d.circles.append(Circle(center, radius, f'({center.label},{radius})'))
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



def parallel_1(d):
    # l = random.choice(d.lines)
    # A, B = l.point1, l.point2

    A = Point(random_coord(), random_coord(), label_point(d))
    new_labels = [A.label]
    ind = 0
    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break
        if ind > 30:
            return d
        ind += 1


    B = Point(random_coord(), random_coord(), B_label)


    #define numpy vector of difference of A, B
    AB_diff = np.array([B.x - A.x, B.y - A.y])

    # tk = random.randint(0,5)
    num_not_prl = random.randint(1, 5)

    new_points_0 = []
    new_points_1 = []
    new_lines = []



    #Generate a parallel line
    ind = 0
    while True:
        scale = random.uniform(-5, 5)
        x, y = random_coord(), random_coord()
        vector = AB_diff
        x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
        if assert_coord_in_range(x_end, y_end):
            break
        if ind > 30:
            return d
        ind += 1

    ind = 0
    while True:
        label0 = label_point(d)
        if label0 not in new_labels:
            new_labels.append(label0)
            break

        if ind > 30:
            return d
        ind += 1

    ind = 0
    while True:
        label1 = label_point(d)
        if label1 not in new_labels:
            new_labels.append(label1)
            break
        if ind > 30:
            return d
        ind += 1

    C = Point(x, y, label0)
    D = Point(x_end, y_end, label1)


    new_lines.append(Line(C, D, label=""))



    #Generate non-parallel lines
    for j in range(num_not_prl):
        ind = 0
        while True:
            angle = random_angle()
            scale = random.uniform(-5, 5)
            x,y = random_coord(), random_coord()
            vector = rotate_vector(AB_diff, angle)
            x_end, y_end = x + vector[0]*scale, y + vector[1]*scale
            if assert_coord_in_range(x_end, y_end):
                break
            if ind > 30:
                return d
            ind += 1

        ind = 0
        while True:
            label0 = label_point(d)
            if label0 not in new_labels:
                new_labels.append(label0)
                break
            if ind > 30:
                return d
            ind += 1

        ind = 0
        while True:
            label1 = label_point(d)
            if label1 not in new_labels:
                new_labels.append(label1)
                break
            if ind > 30:
                return d
            ind += 1

        new_points_0.append(Point(x, y, label0))
        new_points_1.append(Point(x_end, y_end, label1))
        new_lines.append(Line(new_points_0[-1], new_points_1[-1], label=""))


    d.points.extend([A, B])
    d.lines.append(Line(A, B, label=""))
    d.points.extend([C, D])

    d.points.extend(new_points_0)
    d.points.extend(new_points_1)
    d.lines.extend(new_lines)

    d.entities.append(('parallel_1', [A.label, B.label, C.label, D.label] + [new_points_0[0].label,new_points_1[0].label]))

    return d

def C_parallel_1(d):
    # l = random.choice(d.lines)
    # A, B = l.point1, l.point2

    A = Point(random_coord(), random_coord(), label_point(d))
    new_labels = [A.label]
    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break
    B = Point(random_coord(), random_coord(), B_label)



    #define numpy vector of difference of A, B
    AB_diff = np.array([B.x - A.x, B.y - A.y])

    # tk = random.randint(0,5)
    num_not_prl = random.randint(1, 7)

    new_points_0 = []
    new_points_1 = []
    new_lines = []



    ind = 0
    #Generate a parallel line

    while True:
        scale = random.uniform(0.5, 5)
        x, y = random_coord(), random_coord()
        vector = AB_diff
        x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
        if assert_coord_in_range(x_end, y_end):
            break
        if ind > 30:
            return d
        ind += 1

    ind = 0
    while True:
        label0 = label_point(d)
        if label0 not in new_labels:
            new_labels.append(label0)
            break
        if ind > 30:
            return d
        ind += 1

    ind = 0
    while True:
        label1 = label_point(d)
        if label1 not in new_labels:
            new_labels.append(label1)
            break
        if ind > 30:
            return d
        ind += 1

    C = Point(x, y, label0)
    D = Point(x_end, y_end, label1)

    parallel_color = random.choice(d.usable_colors)
    d = remove_color(d, parallel_color)

    new_lines.append(Line(C, D, label="", color = parallel_color))

    color = random.choice(d.usable_colors)
    #Generate non-parallel lines
    for j in range(num_not_prl):
        ind = 0
        while True:
            angle = random_angle()
            scale = random.uniform(-5, 5)
            x,y = random_coord(), random_coord()
            vector = rotate_vector(AB_diff, angle)
            x_end, y_end = x + vector[0]*scale, y + vector[1]*scale
            if assert_coord_in_range(x_end, y_end):
                break
            if ind > 30:
                return d
            ind += 1
        ind = 0
        while True:
            label0 = label_point(d)
            if label0 not in new_labels:
                new_labels.append(label0)
                break
            if ind > 30:
                return d
            ind += 1
        ind = 0
        while True:
            label1 = label_point(d)
            if label1 not in new_labels:
                new_labels.append(label1)
                break
            if ind > 30:
                return d
            ind += 1

        new_points_0.append(Point(x, y, label0))
        new_points_1.append(Point(x_end, y_end, label1))

        color = random.choice(d.usable_colors)
        d = remove_color(d, color)

        new_lines.append(Line(new_points_0[-1], new_points_1[-1], label="", color = color))


    d.points.extend([A, B])

    d.points.extend([C, D])

    d.points.extend(new_points_0)
    d.points.extend(new_points_1)
    d.lines.extend(new_lines)

    if random.choice([True, False]):
        d.lines.append(Line(A, B, label=""))
        d.entities.append(('C_parallel_1', [A.label, B.label, C.label, D.label] + [parallel_color, color] + [new_points_0[0].label, new_points_1[0].label]))

    else:
        col_AB = random.choice(d.usable_colors)
        d = remove_color(d, col_AB)
        d.lines.append(Line(A, B, label="", color = col_AB))
        d.entities.append(('C_parallel_1-2', [col_AB, parallel_color, color] ))
        d.points = []

    return d


def parallel_2(d):

    A = Point(random_coord(), random_coord(), label_point(d))
    new_labels = [A.label]
    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break
    B = Point(random_coord(), random_coord(), B_label)
    # define numpy vector of difference of A, B
    AB_diff = np.array([B.x - A.x, B.y - A.y])


    num_prl = random.randint(1, 5)
    num_not_prl = random.randint(1, 5)

    prl_points_0 = []
    prl_points_1 = []
    non_prl_points_0 = []
    non_prl_points_1 = []
    new_lines = []
    new_labels = []

    #Generate parallel lines
    for i in range(num_prl):
        ind = 0
        while True:
            scale = random.uniform(-5, 5)
            x, y = random_coord(), random_coord()
            vector = AB_diff
            x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
            if assert_coord_in_range(x_end, y_end):
                break
            if ind > 30:
                return d
            ind += 1

        while True:
            label_0 = label_point(d)
            if label_0 not in new_labels:
                new_labels.append(label_0)
                break
            if ind > 100:
                return d
            ind += 1

        while True:
            label_1 = label_point(d)
            if label_1 not in new_labels:
                new_labels.append(label_1)
                break
            if ind > 100:
                return d
            ind += 1

        prl_points_0.append(Point(x, y, label_0))
        prl_points_1.append(Point(x_end, y_end, label_1))

        new_lines.append(Line(prl_points_0[-1], prl_points_1[-1], label=""))


    #Generate non-parallel lines
    for j in range(num_not_prl):
        ind = 0
        while True:
            scale = random.uniform(-5, 5)
            angle = random_angle()
            x, y = random_coord(), random_coord()
            vector = rotate_vector(AB_diff, angle)
            x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
            if assert_coord_in_range(x_end, y_end):
                break
            if ind > 100:
                return d
            ind += 1

        while True:
            label_0 = label_point(d)
            if label_0 not in new_labels:
                new_labels.append(label_0)
                break
            if ind > 100:
                return d
            ind += 1

        while True:
            label_1 = label_point(d)
            if label_1 not in new_labels:
                new_labels.append(label_1)
                break
            if ind > 100:
                return d
            ind += 1

        non_prl_points_0.append(Point(x, y, label_0))
        non_prl_points_1.append(Point(x_end, y_end, label_1))
        new_lines.append(Line(non_prl_points_0[-1], non_prl_points_1[-1], label=""))

    d.points.extend([A, B])

    d.points.extend(prl_points_0)
    d.points.extend(prl_points_1)
    d.points.extend(non_prl_points_0)
    d.points.extend(non_prl_points_1)
    d.lines.extend(new_lines)

    if random.choice([False, True]):
        d.lines.append(Line(A, B, label=""))
        d.entities.append(('parallel_2', [A.label, B.label, f'{num_prl}', f'{num_not_prl}']))
    else:
        w = label_line_nonempty(d)
        d.lines.append(Line(A, B, label=w))
        d.entities.append(('parallel_2-2', [w, f'{num_prl}', f'{num_not_prl}']))
        d.points = []


    # print(f"Parallel_2 : {A.label}{B.label}, {num_prl}, {num_not_prl}")
    return d


def C_parallel_2(d):
    color_0 = random.choice(d.usable_colors)
    d = remove_color(d, color_0)

    A = Point(random_coord(), random_coord(), label_point(d))
    new_labels = [A.label]
    while True:
        B_label = label_point(d)
        if B_label not in new_labels:
            new_labels.append(B_label)
            break
    B = Point(random_coord(), random_coord(), B_label)
    # define numpy vector of difference of A, B
    AB_diff = np.array([B.x - A.x, B.y - A.y])


    num_prl = random.randint(1, 5)
    num_not_prl = random.randint(1, 5)

    prl_points_0 = []
    prl_points_1 = []
    non_prl_points_0 = []
    non_prl_points_1 = []
    new_lines = []

    color = random.choice(d.usable_colors)
    #Generate parallel lines
    for i in range(num_prl):
        ind = 0
        while True:
            scale = random.uniform(-5, 5)
            x, y = random_coord(), random_coord()
            vector = AB_diff
            x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
            if assert_coord_in_range(x_end, y_end):
                break
            if ind > 100:
                return d
            ind += 1

        while True:
            label_0 = label_point(d)
            if label_0 not in new_labels:
                new_labels.append(label_0)
                break
            if ind > 100:
                return d
            ind += 1

        while True:
            label_1 = label_point(d)
            if label_1 not in new_labels:
                new_labels.append(label_1)
                break
            if ind > 100:
                return d
            ind += 1

        prl_points_0.append(Point(x, y, label_0))
        prl_points_1.append(Point(x_end, y_end, label_1))
        color = random.choice(d.usable_colors + ['black'])
        new_lines.append(Line(prl_points_0[-1], prl_points_1[-1], label="", color = color))


    #Generate non-parallel lines
    for j in range(num_not_prl):
        ind = 0
        while True:
            scale = random.uniform(-5, 5)
            angle = random_angle()
            x, y = random_coord(), random_coord()
            vector = rotate_vector(AB_diff, angle)
            x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
            if assert_coord_in_range(x_end, y_end):
                break
            if ind > 100:
                return d
            ind += 1


        while True:
            label_0 = label_point(d)
            if label_0 not in new_labels:
                new_labels.append(label_0)
                break
            if ind > 100:
                return d
            ind += 1

        while True:
            label_1 = label_point(d)
            if label_1 not in new_labels:
                new_labels.append(label_1)
                break
            if ind > 100:
                return d
            ind += 1

        non_prl_points_0.append(Point(x, y, label_0))
        non_prl_points_1.append(Point(x_end, y_end, label_1))
        color = random.choice(d.usable_colors + ['black'])
        new_lines.append(Line(non_prl_points_0[-1], non_prl_points_1[-1], label="", color = color))

    d.points.extend([A, B])
    d.lines.append(Line(A, B, label="", color = color_0))
    d.points.extend(prl_points_0)
    d.points.extend(prl_points_1)
    d.points.extend(non_prl_points_0)
    d.points.extend(non_prl_points_1)
    d.lines.extend(new_lines)

    if random.choice([False, True]):
        d.lines.append(Line(A, B, label=""))
        d.entities.append(('C_parallel_2', [A.label, B.label, f'{num_prl}', color_0]))
    else:
        w = label_line_nonempty(d)
        d.lines.append(Line(A, B, label=w, color = color_0))
        d.entities.append(('C_parallel_2-2', [w, f'{num_prl}', color_0]))
        d.points = []
    return d


def parallel_3(diagram):
    #"X = parallelogram(A, B, C)": { "Description": "Construct X such that ABCX is a parallelogram" },
    while len(diagram.points)< 3:
        diagram = add_free_point(diagram)

    ind = 0
    while True:
        A, B, C = random.sample(diagram.points, 3)
        vector = (B.x - A.x, B.y - A.y)
        D_x = C.x - vector[0]
        D_y = C.y - vector[1]
        if assert_coord_in_range(D_x, D_y):
            break
        if ind > 30:
            return diagram
        ind += 1


    D_label = label_point(diagram)

    D = Point(D_x, D_y, D_label)
    diagram.points.append(D)
    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
    # diagram.entities.append(f'Parallelogram({A.label}{B.label}{C.label}{D.label})')
    diagram.entities.append(('parallel_3', [A.label, B.label, C.label, D.label]))
    return diagram

def C_parallel_3(diagram):
    #"X = parallelogram(A, B, C)": { "Description": "Construct X such that ABCX is a parallelogram" },
    color1, color2, color3, color4 = random.sample(diagram.usable_colors, 4)
    diagram = remove_color(diagram, color1)
    diagram = remove_color(diagram, color2)
    diagram = remove_color(diagram, color3)
    diagram = remove_color(diagram, color4)


    while len(diagram.points)< 3:
        diagram = add_free_point(diagram)

    ind = 0
    while True:
        A, B, C = random.sample(diagram.points, 3)
        vector = (B.x - A.x, B.y - A.y)
        D_x = C.x - vector[0]
        D_y = C.y - vector[1]
        if assert_coord_in_range(D_x, D_y):
            break
        if ind > 30:
            return diagram
        ind += 1


    D_label = label_point(diagram)

    D = Point(D_x, D_y, D_label)
    diagram.points.append(D)
    diagram.lines.extend([Line(A, B, label="", color = color1), Line(B, C, label="", color = color2), Line(C, D, label="", color = color3), Line(D, A, label="", color = color4)])
    # diagram.entities.append(f'Parallelogram({A.label}{B.label}{C.label}{D.label})')
    diagram.entities.append(('C_parallel_3', [A.label, B.label, C.label, D.label, color1, color2, color3, color4]))
    return diagram

def parallel_4(diagram: Diagram):

    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)
    # Randomly select two points A, B to form the base AB of the trapezoid

    ind = 0
    while True:
        A, B = random.sample(diagram.points, 2)

        # Calculate the directional vector for AB and its perpendicular
        AB_vector = (B.x - A.x, B.y - A.y)
        perp_AB = (-AB_vector[1], AB_vector[0])  # Rotate AB_vector by 90 degrees to get perpendicular

        # Normalize the perpendicular vector
        perp_AB_normalized = normalize(perp_AB)

        # Select a random angle θ < π/2 for rotation
        theta = random.uniform(0, np.pi / 6)

        # Calculate the direction for AD by rotating the perpendicular direction by θ
        AD_direction = (perp_AB_normalized[0] * np.cos(theta) - perp_AB_normalized[1] * np.sin(theta),
                        perp_AB_normalized[0] * np.sin(theta) + perp_AB_normalized[1] * np.cos(theta))

        # Calculate the direction for BC by rotating the perpendicular direction by -θ
        BC_direction = (perp_AB_normalized[0] * np.cos(-theta) - perp_AB_normalized[1] * np.sin(-theta),
                        perp_AB_normalized[0] * np.sin(-theta) + perp_AB_normalized[1] * np.cos(-theta))

        # Decide on a length for AD and BC
        leg_length = random.uniform(50, 400)  # Example range for the leg length

        # Calculate points D and C using the determined directions and length
        Dx, Dy = A.x + AD_direction[0] * leg_length, A.y + AD_direction[1] * leg_length
        Cx, Cy = B.x + BC_direction[0] * leg_length, B.y + BC_direction[1] * leg_length


        # Check if D and C are within the diagram range
        if assert_coord_in_range(Dx, Dy) and assert_coord_in_range(Cx, Cy):
            break
        if ind > 30:
            return diagram
        ind += 1


    # Create points C and D
    P_lbls = []
    while len(P_lbls) < 2:
        label = label_point(diagram)
        if label not in P_lbls:
            P_lbls.append(label)
    C_label, D_label = P_lbls
    C = Point(Cx, Cy, C_label)
    D = Point(Dx, Dy, D_label)
    diagram.points.extend([C, D])

    if random.choice([True, False]):
        color = random.choice(diagram.usable_colors)
        diagram = remove_color(diagram, color)
    else:
        color = 'black'
    # Add lines to form the trapezoid
    diagram.lines.extend([
        Line(A, B, label="", color = color),  # Base AB
        Line(B, C, label="", color = color),  # Side BC
        Line(C, D, label="", color = color),  # Top CD, parallel to AB
        Line(D, A, label="", color = color)   # Side AD
    ])

    # diagram.entities.extend([
    #     f'Point({C.label})', f'Point({D.label})',
    #     f'Line({A.label}{B.label})', f'Line({B.label}{C.label})',
    #     f'Line({C.label}{D.label})', f'Line({D.label}{A.label})',
    #     f'Equilateral Trapezoid({A.label}{B.label}{C.label}{D.label})'
    # ])

    diagram.entities.append(('parallel_4', [A.label, B.label, C.label, D.label]))
    # print(f"=====A,B,C,D : {A.label}{B.label}{C.label}{D.label}")
    return diagram

def C_parallel_4(diagram: Diagram):
    # print(f"usalbe colors : {diagram.usable_colors}")
    color1, color2, color3, color4 = random.sample(diagram.usable_colors, 4)
    diagram = remove_color(diagram, color1)
    diagram = remove_color(diagram, color2)
    diagram = remove_color(diagram, color3)
    diagram = remove_color(diagram, color4)


    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)
    # Randomly select two points A, B to form the base AB of the trapezoid
    ind = 0
    while True:
        A, B = random.sample(diagram.points, 2)

        # Calculate the directional vector for AB and its perpendicular
        AB_vector = (B.x - A.x, B.y - A.y)
        perp_AB = (-AB_vector[1], AB_vector[0])  # Rotate AB_vector by 90 degrees to get perpendicular

        # Normalize the perpendicular vector
        perp_AB_normalized = normalize(perp_AB)

        # Select a random angle θ < π/2 for rotation
        theta = random.uniform(0, np.pi / 6)

        # Calculate the direction for AD by rotating the perpendicular direction by θ
        AD_direction = (perp_AB_normalized[0] * np.cos(theta) - perp_AB_normalized[1] * np.sin(theta),
                        perp_AB_normalized[0] * np.sin(theta) + perp_AB_normalized[1] * np.cos(theta))

        # Calculate the direction for BC by rotating the perpendicular direction by -θ
        BC_direction = (perp_AB_normalized[0] * np.cos(-theta) - perp_AB_normalized[1] * np.sin(-theta),
                        perp_AB_normalized[0] * np.sin(-theta) + perp_AB_normalized[1] * np.cos(-theta))

        # Decide on a length for AD and BC
        leg_length = random.uniform(50, 400)  # Example range for the leg length

        # Calculate points D and C using the determined directions and length
        Dx, Dy = A.x + AD_direction[0] * leg_length, A.y + AD_direction[1] * leg_length
        Cx, Cy = B.x + BC_direction[0] * leg_length, B.y + BC_direction[1] * leg_length

        # Check if D and C are within the diagram range
        if assert_coord_in_range(Dx, Dy) and assert_coord_in_range(Cx, Cy):
            break
        if ind > 30:
            return diagram
        ind += 1



    # Create points C and D
    P_lbls = []
    while len(P_lbls) < 2:
        label = label_point(d)
        if label not in P_lbls:
            P_lbls.append(label)
    C_label, D_label = P_lbls
    C = Point(Cx, Cy, C_label)
    D = Point(Dx, Dy, D_label)
    diagram.points.extend([C, D])

    # Add lines to form the trapezoid
    diagram.lines.extend([
        Line(A, B, label="", color = color1),  # Base AB
        Line(B, C, label="", color = color2),  # Side BC
        Line(C, D, label="", color = color3),  # Top CD, parallel to AB
        Line(D, A, label="", color = color4)   # Side AD
    ])

    # diagram.entities.extend([
    #     f'Point({C.label})', f'Point({D.label})',
    #     f'Line({A.label}{B.label})', f'Line({B.label}{C.label})',
    #     f'Line({C.label}{D.label})', f'Line({D.label}{A.label})',
    #     f'Equilateral Trapezoid({A.label}{B.label}{C.label}{D.label})'
    # ])
    if random.choice([True, False]):
        diagram.entities.append(('C_parallel_4', [A.label, B.label, C.label, D.label, color1, color2, color3, color4]))
    else:
        diagram.entities.append(('C_parallel_4-2', [A.label, B.label, C.label, D.label, color1, color2, color3, color4]))
        diagram.points = []
    # print(f"=====A,B,C,D : {A.label}{B.label}{C.label}{D.label}")
    return diagram

def parallel_5(d):
    # No / 1 / 2 parallel pairs in the polygon

    # Choose the number of edges in the polygon
    num_edges = random.choice([3, 3, 4, 4, 4, 5, 5, 6])
    #Choose random number of parallel pairs for the polygon
    if num_edges == 3:
        num_parallel_pairs = 0
    else:
        num_parallel_pairs = random.choice([0, 1, 2])

    polygon_points = random_convex_polygon(num_edges, num_parallel_pairs, 1000)
    if polygon_points is None:
        return d

    edge_color, fill_color = random.choice(color_pairs.candidates)

    if random.choice([True, False]):
        label = label_point(d)
    else:
        label = ""
    d.polygons.append(polygon(polygon_points, label=label, edge_color=edge_color, fill_color=fill_color))
    d.entities.append((f'parallel_5-{num_edges}', [fill_color, num_parallel_pairs]))

    d.points = []
    d.lines = []
    d.circles = []

    return d

# def parallel_5(diagram: Diagram):
#    # Line a, and point P on a, and different lines passing through Q, only one line b is parallel to a"
#     while len(diagram.points) < 2:
#         diagram = add_free_point(diagram)
#
#     P, Q = random.sample(diagram.points, 2)
#
#     #   Generate line a = A1_A2
#     A1_x,A1_y = random_coord(), random_coord()
#     vec_A1_P = (P.x - A1_x, P.y - A1_y)
#
#     ind = 0
#     while True:
#         scale = random.uniform(0.1, 3)
#         A2_x, A2_y = P.x + vec_A1_P[0] * scale, P.y + vec_A1_P[1] * scale
#         if assert_coord_in_range(A2_x, A2_y):
#             break
#         if ind > 10:
#             return diagram
#         ind += 1
#
#
#     l1 = label_line_nonempty(diagram)
#     line_labels = [l1]
#     diagram.lines.append(Line(Point(A1_x, A1_y, ""), Point(A2_x, A2_y, ""), l1))
#     diagram.points.extend([Point(A1_x, A1_y, ""), Point(A2_x, A2_y, "")])
#     # Generate a parallel line v on Q
#     ind =0
#     while True:
#         scale = random.uniform(0.1, 3)
#         scale2 = random.uniform(0.1, 3)
#         v1_x, v1_y = Q.x + vec_A1_P[0] * scale, Q.y + vec_A1_P[1] * scale
#         v2_x, v2_y = Q.x - vec_A1_P[0] * scale2, Q.y - vec_A1_P[1] * scale2
#
#         if assert_coord_in_range(v1_x, v1_y) and assert_coord_in_range(v2_x, v2_y):
#             break
#         if ind > 30:
#             return diagram
#
#         ind+=1
#     while True:
#         l2 = label_line(diagram)
#         if l2 not in line_labels:
#             line_labels.append(l2)
#             break
#
#     diagram.lines.append(Line(Point(v1_x, v1_y, ""), Point(v2_x, v2_y, ""), l2))
#     diagram.points.extend([Point(v1_x, v1_y, ""), Point(v2_x, v2_y, "")])
#     #generate non-parallel lines
#     n = random.randint(1,3)
#     nonpar_list = []
#     for i in range(n):
#         vec = np.array([vec_A1_P[0], vec_A1_P[1]])
#         angle = random.uniform(np.pi/9, 17/9*np.pi)
#         vec = rotate_vector(vec, angle)
#         ind = 0
#         while True:
#             scale1 = random.uniform(0.1, 3)
#             scale2 = random.uniform(0.1, 3)
#             x1, y1 = Q.x + vec[0] * scale1, Q.y + vec[1] * scale1
#             x2, y2 = Q.x - vec[0] * scale2, Q.y - vec[1] * scale2
#
#             if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
#                 break
#             if ind > 30:
#                 return diagram
#
#             ind+=1
#         while True:
#             l = label_line(diagram)
#             if l not in line_labels:
#                 line_labels.append(l)
#                 break
#
#         nonpar_list.append(Line(Point(x1, y1, ""), Point(x2, y2, ""), l))
#         diagram.points.extend([Point(x1, y1, ""), Point(x2, y2, "")])
#
#     diagram.lines.extend(nonpar_list)
#     diagram.entities.append(('parallel_5', [P.label, Q.label, l1, l2] + [line.label for line in nonpar_list]))
#
#     return diagram
#
# def C_parallel_5(diagram: Diagram):
#    # Line a, and point P on a, and different lines passing through Q, only one line b is parallel to a"
#     color1, color2 = random.sample(diagram.usable_colors, 2)
#     diagram = remove_color(diagram, color1)
#     diagram = remove_color(diagram, color2)
#
#     line_labels = []
#
#     while len(diagram.points) < 2:
#         diagram = add_free_point(diagram)
#
#     P, Q = random.sample(diagram.points, 2)
#
#     #   Generate line a = A1_A2
#     A1_x,A1_y = random_coord(), random_coord()
#     vec_A1_P = (P.x - A1_x, P.y - A1_y)
#
#     ind = 0
#     while True:
#         scale = random.uniform(0.1, 3)
#         A2_x, A2_y = P.x + vec_A1_P[0] * scale, P.y + vec_A1_P[1] * scale
#         if assert_coord_in_range(A2_x, A2_y):
#             break
#         if ind > 10:
#             return diagram
#         ind += 1
#
#
#     l1 = label_line_nonempty(diagram)
#     line_labels.append(l1)
#     diagram.lines.append(Line(Point(A1_x, A1_y, ""), Point(A2_x, A2_y, ""), l1, color = color1))
#     diagram.points.extend([Point(A1_x, A1_y, ""), Point(A2_x, A2_y, "")])
#     # Generate a parallel line v on Q
#     ind =0
#     while True:
#         scale = random.uniform(0.1, 3)
#         scale2 = random.uniform(0.1, 3)
#         v1_x, v1_y = Q.x + vec_A1_P[0] * scale, Q.y + vec_A1_P[1] * scale
#         v2_x, v2_y = Q.x - vec_A1_P[0] * scale2, Q.y - vec_A1_P[1] * scale2
#
#         if assert_coord_in_range(v1_x, v1_y) and assert_coord_in_range(v2_x, v2_y):
#             break
#         if ind > 30:
#             return diagram
#
#         ind+=1
#
#     while True:
#         l2 = label_line_nonempty(diagram)
#         if l2 not in line_labels:
#             line_labels.append(l2)
#             break
#
#     diagram.lines.append(Line(Point(v1_x, v1_y, ""), Point(v2_x, v2_y, ""), l2, color = color2))
#     diagram.points.extend([Point(v1_x, v1_y, ""), Point(v2_x, v2_y, "")])
#     #generate non-parallel lines
#     n = random.randint(1,3)
#     nonpar_list = []
#
#     color = random.choice(diagram.usable_colors)
#     for i in range(n):
#         vec = np.array([vec_A1_P[0], vec_A1_P[1]])
#         angle = random.uniform(np.pi/9, 17/9*np.pi)
#         vec = rotate_vector(vec, angle)
#         ind = 0
#         while True:
#             scale1 = random.uniform(0.1, 3)
#             scale2 = random.uniform(0.1, 3)
#             x1, y1 = Q.x + vec[0] * scale1, Q.y + vec[1] * scale1
#             x2, y2 = Q.x - vec[0] * scale2, Q.y - vec[1] * scale2
#
#             if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
#                 break
#             if ind > 30:
#                 return diagram
#
#             ind+=1
#         color = random.choice(diagram.usable_colors)
#         diagram = remove_color(diagram, color)
#         while True:
#
#             l = label_line(diagram)
#             if l not in line_labels:
#                 line_labels.append(l)
#                 break
#
#         nonpar_list.append(Line(Point(x1, y1, ""), Point(x2, y2, ""), l, color = color))
#         diagram.points.extend([Point(x1, y1, ""), Point(x2, y2, "")])
#
#     diagram.lines.extend(nonpar_list)
#     diagram.entities.append(('C_parallel_5', [P.label, Q.label, l1, l2, color1, color2] + [line.label for line in nonpar_list]))
#
#     return diagram


def parallel_6(diagram):
    # TF question: line a is parallel to line b
    for _ in range(2):
        diagram = add_free_point(diagram)
    # Randomly select two points A, B to form the base AB of the trapezoid

    ind = 0
    while True:
        A, B = random.sample(diagram.points, 2)

        # Calculate the directional vector for AB and its perpendicular
        AB_vector = (B.x - A.x, B.y - A.y)
        perp_AB = (-AB_vector[1], AB_vector[0])  # Rotate AB_vector by 90 degrees to get perpendicular

        # Normalize the perpendicular vector
        perp_AB_normalized = normalize(perp_AB)

        # Select a random angle θ < π/2 for rotation
        theta = random.uniform(0, np.pi / 6)

        # Calculate the direction for AD by rotating the perpendicular direction by θ
        AD_direction = (perp_AB_normalized[0] * np.cos(theta) - perp_AB_normalized[1] * np.sin(theta),
                        perp_AB_normalized[0] * np.sin(theta) + perp_AB_normalized[1] * np.cos(theta))

        # Calculate the direction for BC by rotating the perpendicular direction by -θ
        BC_direction = (perp_AB_normalized[0] * np.cos(-theta) - perp_AB_normalized[1] * np.sin(-theta),
                        perp_AB_normalized[0] * np.sin(-theta) + perp_AB_normalized[1] * np.cos(-theta))

        # Decide on a length for AD and BC
        leg_length = random.uniform(50, 400)  # Example range for the leg length

        # Calculate points D and C using the determined directions and length
        Dx, Dy = A.x + AD_direction[0] * leg_length, A.y + AD_direction[1] * leg_length
        Cx, Cy = B.x + BC_direction[0] * leg_length, B.y + BC_direction[1] * leg_length


        # Check if D and C are within the diagram range
        if assert_coord_in_range(Dx, Dy) and assert_coord_in_range(Cx, Cy):
            break
        if ind > 30:
            return diagram
        ind += 1


    # Create points C and D
    P_lbls = []
    while len(P_lbls) < 2:
        label = label_point(d)
        if label not in P_lbls:
            P_lbls.append(label)
    C_label, D_label = P_lbls
    C = Point(Cx, Cy, C_label)
    D = Point(Dx, Dy, D_label)
    diagram.points.extend([C, D])

    if random.choice([True, False]):
        color = random.choice(diagram.usable_colors)
        diagram = remove_color(diagram, color)
    else:
        color = 'black'

    if random.choice([True, False]):
        line_1_label, line_2_label = random.sample(small_letters_nonempty.candidates, 2)
        diagram.lines.extend([
            Line(A, B, label=line_1_label, color = color),  # Base AB
            Line(C, D, label=line_2_label, color = color),  # Top CD, parallel to AB
        ])
    else:
        line_1_label = str(A.label)+str(B.label)
        line_2_label = str(C.label)+str(D.label)
        diagram.lines.extend([
            Line(A, B, label="", color = color),  # Base AB
            Line(C, D, label="", color = color),  # Top CD, parallel to AB
        ])
    diagram.entities.append(('parallel_6', [line_1_label, line_2_label]))

    return diagram


def parallel_7(diagram):
    # negative mining: line a is not parallel to any line in the image.
    for _ in range(2):
        diagram = add_free_point(diagram)

    attempt_count = 0
    while True:
        # A, B를 랜덤으로 뽑는다.
        A, B = random.sample(diagram.points, 2)

        # AB 벡터와, 그에 수직인 벡터를 구한다.
        AB_vector = (B.x - A.x, B.y - A.y)
        perp_AB = (-AB_vector[1], AB_vector[0])

        # 만약 AB가 길이가 너무 작다면(같거나 유사한 점일 경우) 다시 뽑기
        if np.hypot(*AB_vector) < 1e-6:
            attempt_count += 1
            if attempt_count > 30:
                return diagram
            continue

        # perp_AB 정규화
        perp_AB_normalized = normalize(perp_AB)
        if random.choice([True, False]):
            color = random.choice(diagram.usable_colors)
        else:
            color = 'black'

        if random.choice([True, False]):
            line_1_label = random.choice(small_letters_nonempty.candidates)
            diagram.lines.append(
                Line(A, B, label=line_1_label, color = color),  # Base AB
            )
        else:
            line_1_label = str(A.label)+str(B.label)
            diagram.lines.append(
                Line(A, B, label="", color = color),  # Base AB
            ) 
        break

    num_lines = random.randint(2, 10)
    line_label_list = []
    for _ in range(num_lines):
        while True:
            theta1 = random.uniform(0, np.pi)
            theta2 = random.uniform(0, np.pi)
            # 혹시 theta1 ~ theta2가 거의 같은 값이면 다시
            while abs(theta1 - theta2) < 1e-3:  # 너무 가까우면 평행 가능성 높아지므로 재시도
                theta2 = random.uniform(0, np.pi)

            # 회전 행렬 적용 (2D):
            # 회전된 벡터 = ( x*cosθ - y*sinθ , x*sinθ + y*cosθ )
            dir1 = (
                perp_AB_normalized[0] * np.cos(theta1) - perp_AB_normalized[1] * np.sin(theta1),
                perp_AB_normalized[0] * np.sin(theta1) + perp_AB_normalized[1] * np.cos(theta1)
            )
            dir2 = (
                perp_AB_normalized[0] * np.cos(theta2) - perp_AB_normalized[1] * np.sin(theta2),
                perp_AB_normalized[0] * np.sin(theta2) + perp_AB_normalized[1] * np.cos(theta2)
            )

            # 두 선분의 길이를 랜덤하게 정한다.
            length1 = random.uniform(50, 300)
            length2 = random.uniform(50, 300)

            # 새로운 점 C, D를 만든다 (AB와는 전혀 상관없는 방향으로)
            Cx, Cy = A.x + dir1[0]*length1, A.y + dir1[1]*length1
            Dx, Dy = B.x + dir2[0]*length2, B.y + dir2[1]*length2

            # 다이어그램 범위 안에 있으면 확정
            if assert_coord_in_range(Cx, Cy) and assert_coord_in_range(Dx, Dy):
                # Label은 예시로 적당히 만든다
                P_lbls = []
                while len(P_lbls) < 2:
                    label = label_point(d)
                    if label not in P_lbls:
                        P_lbls.append(label)
                C_label, D_label = P_lbls
                C = Point(Cx, Cy, C_label)
                D = Point(Dx, Dy, D_label)
                diagram.points.extend([C, D])

                # 선에 적용할 색 선택
                if random.choice([True, False]):
                    color = random.choice(diagram.usable_colors)
                else:
                    color = 'black'

                if random.choice([True, False]):
                    line_2_label = random.choice(small_letters_nonempty.candidates)
                    diagram.lines.extend([
                        Line(C, D, label=line_2_label, color = color),  
                    ])
                else:
                    line_2_label = str(C.label)+str(D.label)
                    diagram.lines.extend([
                        Line(C, D, label="", color = color), 
                    ])
                
                line_label_list.append(line_2_label)

                break

            attempt_count += 1
            if attempt_count > 30:
                # 너무 오래 시도해도 범위를 못 맞추면 그냥 반환
                return diagram
    
    diagram.entities.append(('parallel_7', [line_1_label, ", ".join(line_label_list)]))

    return diagram

def parallel_8(diagram):
    # Among the edges of a triangle, choose a parallel line to a given line
    for _ in range(2):
        diagram = add_free_point(diagram)
    # Randomly select two points A, B to form the base AB of the trapezoid

    ind = 0
    while True:
        A, B = random.sample(diagram.points, 2)

        # Calculate the directional vector for AB and its perpendicular
        AB_vector = (B.x - A.x, B.y - A.y)
        perp_AB = (-AB_vector[1], AB_vector[0])  # Rotate AB_vector by 90 degrees to get perpendicular

        # Normalize the perpendicular vector
        perp_AB_normalized = normalize(perp_AB)

        # Select a random angle θ < π/2 for rotation
        theta = random.uniform(0, np.pi / 6)

        # Calculate the direction for AD by rotating the perpendicular direction by θ
        AD_direction = (perp_AB_normalized[0] * np.cos(theta) - perp_AB_normalized[1] * np.sin(theta),
                        perp_AB_normalized[0] * np.sin(theta) + perp_AB_normalized[1] * np.cos(theta))

        # Calculate the direction for BC by rotating the perpendicular direction by -θ
        BC_direction = (perp_AB_normalized[0] * np.cos(-theta) - perp_AB_normalized[1] * np.sin(-theta),
                        perp_AB_normalized[0] * np.sin(-theta) + perp_AB_normalized[1] * np.cos(-theta))

        # Decide on a length for AD and BC
        leg_length = random.uniform(50, 400)  # Example range for the leg length

        # Calculate points D and C using the determined directions and length
        Dx, Dy = A.x + AD_direction[0] * leg_length, A.y + AD_direction[1] * leg_length
        Cx, Cy = B.x + BC_direction[0] * leg_length, B.y + BC_direction[1] * leg_length


        # Check if D and C are within the diagram range
        if assert_coord_in_range(Dx, Dy) and assert_coord_in_range(Cx, Cy):
            break
        if ind > 30:
            return diagram
        ind += 1


    # Create points C and D
    P_lbls = []
    while len(P_lbls) < 2:
        label = label_point(d)
        if label not in P_lbls:
            P_lbls.append(label)
    C_label, D_label = P_lbls
    C = Point(Cx, Cy, C_label)
    D = Point(Dx, Dy, D_label)
    diagram.points.extend([C, D])
    diagram = add_free_point(diagram)
    E = diagram.points[-1]

    if random.choice([True, False]):
        color = random.choice(diagram.usable_colors)
        diagram = remove_color(diagram, color)
    else:
        color = 'black'

    if random.choice([True, False]):
        line_1_label = random.choice(small_letters_nonempty.candidates)
        diagram.lines.append(
            Line(A, B, label=line_1_label, color = color),  # Base AB
        )
    else:
        line_1_label = str(A.label)+str(B.label)
        diagram.lines.append(
            Line(A, B, label="", color = color),  # Base AB
        )
    diagram.lines.extend([
            Line(C, D, label="", color = color),  
            Line(C, E, label="", color = color),  
            Line(E, D, label="", color = color)
        ])
    answer_label = str(C.label)+str(D.label)
    if random.choice([True, False]):
        answer_label = str(C.label)+str(D.label)
    else:
        answer_label = str(D.label)+str(C.label)    
    
    label_list = [C.label, D.label, E.label]
    random.shuffle(label_list)
    label_2, label_3, label_4 = label_list

    diagram.entities.append(('parallel_8', [line_1_label, answer_label, label_2, label_3, label_4]))
    return diagram

@timeout(10)
def parallel_9(diagram):
    # # Compare parallelity in super-complicated diagram
    color_parallel_rules = ['add_free_point','add_circle','add_free_circle',"circle_with_radius",'C_add_free_point', 'C_add_circle', 'C_add_free_circle', 'C_circle_with_radius', 'add_free_point_with_line', 'C_add_free_point_with_line', 'add_line', 'C_add_line',
                         'C_parallel_1', 'C_parallel_2', 'C_parallel_3', 'C_parallel_4',
                         'parallel_1','parallel_2','parallel_3','parallel_4',
                         'parallel_5', 'parallel_6', 'parallel_10']
    num_trials = random.randint(5, 10)
    for _ in range(num_trials):
        rule_name = random.choice(color_parallel_rules)
        diagram = eval(rule_name)(diagram)
        diagram.steps.append(rule_name)
        diagram.usable_colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'yellow']
    diagram.entities = []
    diagram.usable_colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'yellow']
    if random.choice([True, False]):
        diagram = parallel_6(diagram)
    else:
        diagram = parallel_10(diagram)
    return diagram

def parallel_10(diagram):
    # TF question: line a is not parallel to line b
    for _ in range(2):
        diagram = add_free_point(diagram)

    attempt_count = 0
    while True:
        # A, B를 랜덤으로 뽑는다.
        A, B = random.sample(diagram.points, 2)

        # AB 벡터와, 그에 수직인 벡터를 구한다.
        AB_vector = (B.x - A.x, B.y - A.y)
        perp_AB = (-AB_vector[1], AB_vector[0])

        # 만약 AB가 길이가 너무 작다면(같거나 유사한 점일 경우) 다시 뽑기
        if np.hypot(*AB_vector) < 1e-6:
            attempt_count += 1
            if attempt_count > 30:
                return diagram
            continue

        # perp_AB 정규화
        perp_AB_normalized = normalize(perp_AB)

        theta1 = random.uniform(0, np.pi)
        theta2 = random.uniform(0, np.pi)
        # 혹시 theta1 ~ theta2가 거의 같은 값이면 다시
        while abs(theta1 - theta2) < 1e-3:  # 너무 가까우면 평행 가능성 높아지므로 재시도
            theta2 = random.uniform(0, np.pi)

        # 회전 행렬 적용 (2D):
        # 회전된 벡터 = ( x*cosθ - y*sinθ , x*sinθ + y*cosθ )
        dir1 = (
            perp_AB_normalized[0] * np.cos(theta1) - perp_AB_normalized[1] * np.sin(theta1),
            perp_AB_normalized[0] * np.sin(theta1) + perp_AB_normalized[1] * np.cos(theta1)
        )
        dir2 = (
            perp_AB_normalized[0] * np.cos(theta2) - perp_AB_normalized[1] * np.sin(theta2),
            perp_AB_normalized[0] * np.sin(theta2) + perp_AB_normalized[1] * np.cos(theta2)
        )

        # 두 선분의 길이를 랜덤하게 정한다.
        length1 = random.uniform(50, 300)
        length2 = random.uniform(50, 300)

        # 새로운 점 C, D를 만든다 (AB와는 전혀 상관없는 방향으로)
        Cx, Cy = A.x + dir1[0]*length1, A.y + dir1[1]*length1
        Dx, Dy = B.x + dir2[0]*length2, B.y + dir2[1]*length2

        # 다이어그램 범위 안에 있으면 확정
        if assert_coord_in_range(Cx, Cy) and assert_coord_in_range(Dx, Dy):
            # Label은 예시로 적당히 만든다
            P_lbls = []
            while len(P_lbls) < 2:
                label = label_point(diagram)
                if label not in P_lbls:
                    P_lbls.append(label)
            C_label, D_label = P_lbls
            C = Point(Cx, Cy, C_label)
            D = Point(Dx, Dy, D_label)
            diagram.points.extend([C, D])

            # 선에 적용할 색 선택
            if random.choice([True, False]):
                color = random.choice(diagram.usable_colors)
                diagram = remove_color(diagram, color)
            else:
                color = 'black'

            if random.choice([True, False]):
                line_1_label, line_2_label = random.sample(small_letters_nonempty.candidates, 2)
                diagram.lines.extend([
                    Line(A, B, label=line_1_label, color = color),  
                    Line(C, D, label=line_2_label, color = color),  
                ])
            else:
                line_1_label = str(A.label)+str(B.label)
                line_2_label = str(C.label)+str(D.label)
                diagram.lines.extend([
                    Line(A, B, label="", color = color), 
                    Line(C, D, label="", color = color), 
                ])

            break

        attempt_count += 1
        if attempt_count > 30:
            # 너무 오래 시도해도 범위를 못 맞추면 그냥 반환
            return diagram
    
    diagram.entities.append(('parallel_10', [line_1_label, line_2_label]))

    return diagram