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
    C_label, D_label = random.sample(capitals.candidates, 2)
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
    C_label, D_label = random.sample(capitals.candidates, 2)
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


def random_polynomial(t, max_degree=5, coef_range=(-0.1, 0.1)):
    """
    Generate a random polynomial of degree up to 'max_degree'
    evaluated at the points in 't'.
    """
    degree = random.randint(1, max_degree)
    coeffs = [random.uniform(*coef_range) for _ in range(degree + 1)]

    # Evaluate polynomial = c0 + c1*t + c2*t^2 + ...
    poly_vals = np.zeros_like(t)
    for k, c in enumerate(coeffs):
        poly_vals += c * (t ** k)
    return poly_vals


def get_derivative_angle(x_vals, y_vals, t_vals, t_target=500):
    """
    Compute the derivative (via np.gradient) and return the angle
    of the derivative vector at the index closest to t_target.
    Angle = arctan2(dy, dx).
    """
    dx = np.gradient(x_vals)
    dy = np.gradient(y_vals)

    # Find the index in t_vals closest to t_target
    idx = np.argmin(np.abs(t_vals - t_target))
    angle = np.arctan2(dy[idx], dx[idx])
    return angle


def shift_polynomial_to_point(x_vals, y_vals, t_vals, t_target, x_target, y_target):
    """
    Shift the polynomial curves x_vals, y_vals so that at t_target
    they match (x_target, y_target).

    Approach:
      - Find index of t_target
      - Current values at that index: (x_curr, y_curr)
      - Shift all x_vals by [x_target - x_curr]
      - Shift all y_vals by [y_target - y_curr]
    """
    idx = np.argmin(np.abs(t_vals - t_target))
    x_curr = x_vals[idx]
    y_curr = y_vals[idx]

    shift_x = x_target - x_curr
    shift_y = y_target - y_curr

    return x_vals + shift_x, y_vals + shift_y


def sharp1(d):
    t0 = random.randint(100,900)

    x = np.linspace(0, 1000, 1000)
    a = random.uniform(-0.1, 0.1)
    i = random.choice(range(1, 10))
    y = a
    for j in range(i):
        b = random.uniform(200, 800)
        y = y * (x - b)

    y_scale = np.max(y) - np.min(y)
    translation = random.uniform(0, 500)
    y = (y - np.min(y))/y_scale * random.uniform(450,1000-translation)    + translation

    # max_y = max(abs(np.min(y)), abs(np.max(y)))
    # y = y / max_y * 500 + 500
    # 4) Derivative angle of (X1, Y1) at t=500
    angle_1 = get_derivative_angle(x, y, x, t_target=t0)

    # 5) Generate (X2, Y2) with constraints:
    #    (a) (X2(500), Y2(500)) = (X1(500), Y1(500))
    #    (b) The derivative angle differs by >= pi/9 at t=500

    min_angle_diff = np.pi / 9

    ind = 0
    while True:
        # Generate random polynomials

        a = random.uniform(-0.1, 0.1)
        i = random.choice(range(1, 10))
        y2 = a
        for j in range(i):
            b = random.uniform(200, 800)
            y2 = y2 * (x - b)

        y_scale = np.max(y2) - np.min(y2)
        translation = random.uniform(0, 500)
        y2 = (y2 - np.min(y2)) / y_scale * random.uniform(450, 1000 - translation) + translation
        y2 = y2 - y2[t0] + y[t0]

        # Compute derivative angle at t=500
        angle_2 = get_derivative_angle(x, y2, x, t_target=t0)

        # Check if the angle difference is at least pi/9
        if abs(angle_2 - angle_1) >= min_angle_diff:
            # Great, we found a valid second curve
            break

        if ind > 30:
            return d
        ind += 1

    # 6) Build the final piecewise curve X(t), Y(t)
    #    For 0 <= t <= 500, use X1, Y1
    #    For 500 < t <= 1000, use X2, Y2
    # NOTE: Because we used a fine grid, we can do this by masking or slicing.

    # We'll simply create new arrays X, Y

    mask = x > t0

    y[mask] = y2[mask]

    t_list = []
    ind = 0
    while len(t_list) < 4:
        new_t = random.randint(10, 990)
        stop = True
        for s in t_list + [t0]:
            if (y[new_t]-y[s])**2 < 400: #too close
                stop = False

        if stop:
            t_list.append(new_t)


        if ind > 100:
            return d
        ind += 1





    t1, t2, t3, t4 = t_list

    labels = []
    for i in range(5):
        ind = 0
        while True:
            label = label_point(d)
            if label not in labels:
                labels.append(label)
                break
            if ind > 30:
                return d
            ind += 1

    if random.choice([True, False]):
        points = [Point(t0, y[t0], labels[0]), Point(t1, y[t1], labels[1]), Point(t3, y[t3], labels[3])]
    else:
        points = [Point(t0, y[t0], labels[0]), Point(t1, y[t1], labels[1]), Point(t2, y[t2], labels[2]), Point(t3, y[t3], labels[3]), Point(t4, y[t4], labels[4])]

    color = random.choice(d.usable_colors)

    d.curves = []
    d.curves.append(Curve(x, y, '', color = color ))

    d.points.extend(points)

    candidate1 = ""
    candidate2 = ""
    random.shuffle(labels)

    for i in range(len(labels)):
        candidate1 += labels[i] + "/"
        candidate2 += labels[i] + ", "

    d.entities.append(('sharp1', [color, points[0].label, points[1].label, candidate1[:-1], candidate2[:-2]]))
    return d


def sharp2(d): # Find most pointy spots
    #Choose the number of pointy spots
    num_spots = random.choice([2,3,4])

    #Generate random polynomial curves
    x = np.linspace(0, 1000, 1000)

    y_list = []
    for _ in range(num_spots+1):
        a = random.uniform(-0.1, 0.1)
        i = random.choice(range(1, 10))
        y = a
        for j in range(i):
            b = random.uniform(0, 800)
            y = y * (x - b)

        y_scale = np.max(y) - np.min(y)
        translation = random.uniform(0, 500)
        y = (y - np.min(y))/y_scale * random.uniform(750,1000)
        y_list.append(y)

    while True:
        #Choose the pointy spots
        spot_indices = random.sample(range(100, 900), num_spots)
        spot_indices.sort()
        spot_diffs = [spot_indices[i+1]-spot_indices[i] for i in range(num_spots-1)]
        if min(spot_diffs) > 50:
            break

    angle_diffs  = []
    y_final = y_list[0]
    for i in range(num_spots):
        #Compute derivative angle at the pointy spot
        angle_before = get_derivative_angle(x, y_list[i], x, t_target=spot_indices[i]-1)
        angle_after = get_derivative_angle(x, y_list[i+1], x, t_target=spot_indices[i]+1)
        angle_diffs.append(abs(angle_after - angle_before))


        #Glue y_list[i+1] to y_final at spot_indices[i]


        tmp1 = y_list[i + 1][spot_indices[i]]
        tmp0 = y_list[i][spot_indices[i]]
        mask = x > spot_indices[i] - 1
        y_list[i + 1] = y_list[i + 1] - tmp1 + tmp0
        y_final[mask] = y_list[i + 1][mask]

    #Choose the most pointy spot
    max_diff = max(angle_diffs)
    max_diff_index = angle_diffs.index(max_diff)

    #Choose labels
    labels = []
    for i in range(num_spots):
        ind = 0
        while True:
            label = label_point(d)
            if label not in labels:
                labels.append(label)
                break
            if ind > 30:
                return d
            ind += 1

    max_label = labels[max_diff_index]
    wrong_index = random.choice([i for i in range(num_spots) if i != max_diff_index])
    wrong_label = labels[wrong_index]


    points = []
    for i in range(num_spots):
        points.append(Point(spot_indices[i], y_final[spot_indices[i]], labels[i]))

    #Choose color : color of the curve
    color = random.choice(d.usable_colors)

    d.curves = []
    d.curves.append(Curve(x, y_final, '', color = color ))
    d.points.extend(points)

    candidate1 = ""
    candidate2 = ""
    random.shuffle(labels)

    for i in range(len(labels)):
        candidate1 += labels[i] + "/"
        candidate2 += labels[i] + ", "

    d.entities.append(('sharp2', [color, max_label, wrong_label, candidate1[:-1], candidate2[:-2]]))

    return d

def sharp3(d):
    #Decide whether the curve is smooth or pointy
    is_smooth = random.choice([True, False, False])


    x = np.linspace(0, 1000, 1000)
    a = random.uniform(-0.1, 0.1)
    i = random.choice(range(1, 10))
    y = a
    for j in range(i):
        b = random.uniform(200, 800)
        y = y * (x - b)

    y_scale = np.max(y) - np.min(y)
    translation = random.uniform(0, 500)
    y = (y - np.min(y)) / y_scale * random.uniform(450, 1000 - translation) + translation

    # max_y = max(abs(np.min(y)), abs(np.max(y)))
    # y = y / max_y * 500 + 500
    # 4) Derivative angle of (X1, Y1) at t=500


    # 5) Generate (X2, Y2) with constraints:
    #    (a) (X2(500), Y2(500)) = (X1(500), Y1(500))
    #    (b) The derivative angle differs by >= pi/9 at t=500

    t0 = random.randint(100, 900)
    min_angle_diff = np.pi / 6
    angle_1 = get_derivative_angle(x, y, x, t_target=t0)
    ind = 0
    while not is_smooth:
        # Generate random polynomials

        a = random.uniform(-0.1, 0.1)
        i = random.choice(range(1, 10))
        y2 = a
        for j in range(i):
            b = random.uniform(200, 800)
            y2 = y2 * (x - b)

        y_scale = np.max(y2) - np.min(y2)
        translation = random.uniform(0, 500)
        y2 = (y2 - np.min(y2)) / y_scale * 1000 #vrandom.uniform(450, 1000 - translation)
        y2 = y2 - y2[t0] + y[t0]

        # Compute derivative angle at t=500
        angle_2 = get_derivative_angle(x, y2, x, t_target=t0)

        # Check if the angle difference is at least pi/9
        if abs(angle_2 - angle_1) >= min_angle_diff:
            # Great, we found a valid second curve
            mask = x > t0
            y[mask] = y2[mask]
            break

        if ind > 200:
            return d
        ind += 1





    color = random.choice(d.usable_colors)

    d.curves = []
    d.curves.append(Curve(x, y, '', color=color))

    if is_smooth:
        d.entities.append(('sharp3-1', [color]))
    else:
        d.entities.append(('sharp3-2', [color]))

    return d


def sharp4(d):
    #Find a smooth curve or pointy curve
    target = random.choice(["smooth", "pointy"])

    # Choose colors
    colors = random.sample(d.usable_colors, 4)

    if target == "smooth" :
        num_smooth, num_pointy = 1, 3
    else:
        num_smooth, num_pointy = 3, 1

    x_list = []
    for _ in range(4):
        x_list.append(np.linspace(0, 500, 500))

    y_list = []
    for i in range(num_smooth):
        a = random.uniform(-0.1, 0.1)
        i = random.choice(range(1, 10))
        y = a
        y = a
        for j in range(i):
            b = random.uniform(200, 800)
            y = y * (x_list[0] - b)

        y_scale = np.max(y) - np.min(y)
        translation = random.uniform(0, 500)
        y = (y - np.min(y))/y_scale * random.uniform(450,1000-translation)    + translation
        y_list.append(y)


    for i in range(num_pointy):
        a = random.uniform(-0.1, 0.1)
        i = random.choice(range(1, 10))
        y1 = a
        for j in range(i):
            b = random.uniform(200, 800)
            y1 = y1 * (x_list[0] - b)

        y1_scale = np.max(y1) - np.min(y1)
        translation = random.uniform(0, 500)
        y1 = (y1 - np.min(y1))/y1_scale * 1000

        a = random.uniform(-0.1, 0.1)
        i = random.choice(range(1, 10))
        y2 = a
        for j in range(i):
            b = random.uniform(200, 800)
            y2 = y2 * (x_list[0] - b)

        y2_scale = np.max(y2) - np.min(y2)
        translation = random.uniform(0, 500)
        y2 = (y2 - np.min(y2))/y2_scale * 1000

        t0 = random.randint(100, 400)
        mask = x_list[0] > t0
        y1[mask] = y2[mask]
        y_list.append(y1)


    #Choose colors and lables
    labels = []
    for i in range(4):
        ind = 0
        while True:
            label = label_point(d)
            if label not in labels:
                labels.append(label)
                break
            if ind > 30:
                return d
            ind += 1



    #Choose answer_type
    answer_type = random.choice(['label', 'color'])
    # if answer_type == 'label':
    #     if random.choice([True,False]):
    #         colors = [colors[0] for _ in range(4)]
    #
    #
    #     candidate1 = ""
    #     candidate2 = ""
    #     permute_index = random.sample(range(4), 4)
    #     for i in range(4):
    #         candidate1 += labels[permute_index[i]] + "/"
    #         candidate2 += labels[permute_index[i]] + ", "
    #     d.entities.append((f'sharp4-{target}-1', [labels[0], labels[1], labels[2], labels[3], candidate1[:-1], candidate2[:-2]]))
    #
    # else:
    if True:
        candidate1 = ""
        candidate2 = ""
        permute_index = random.sample(range(4), 4)
        for i in range(4):
            candidate1 += colors[permute_index[i]] + "/"
            candidate2 += colors[permute_index[i]] + ", "
        d.entities.append((f'sharp4-{target}-2', [colors[0], colors[1], colors[2], colors[3], candidate1[:-1], candidate2[:-2]]))

    d.curves = []
    d.lines = []
    d.points = []
    d.circles = []

    permute_index = random.sample(range(4), 4)
    #Put these curves in left to right order by scaling two of them from 500~1000, two of them 0~500 for each of x and y
    for i in range(4):
        y = y_list[permute_index[i]]
        x = x_list[i] + 500 if i % 2 == 0 else x_list[i]

        if i < 2:
            y = (y - np.min(y)) / (np.max(y) - np.min(y)) * 500

        else:
            y = (y - np.min(y)) / (np.max(y) - np.min(y)) * 500 + 500

        d.curves.append(Curve(x, y, '', color=colors[permute_index[i]]))




    return d




#AVSB motivated
#Find a shape with pointy ends
#Find a shape without pointy ends (smooth)
#Find a smooth part
#Find a smooth curve
#Find a pointy curve
#Choose all the pointy parts


#General
#Find sharp ends of a polygon
#Find sharp points of curves
