import matplotlib.pyplot as plt
import numpy as np
from .labels import *
import random
import math
import json


def sort_clockwise(points, center):
    return sorted(points, key=lambda p: math.atan2(p.y - center.y, p.x - center.x))

def remove_color(diagram, color):
    diagram.usable_colors = [c for c in diagram.usable_colors if c != color]
    return diagram


def random_angle():
    return np.random.uniform(np.pi / 9, 17 / 9 * np.pi)


def random_acute():
    return np.random.uniform(np.pi / 9, 4 / 9 * np.pi)


def random_obtuse():
    return np.random.uniform(5 / 9 * np.pi, 8 / 9 * np.pi)


def rotate_vector(vector, angle):
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) @ np.array(vector)


def random_coord(start=10, end=1990):
    return np.random.uniform(start, end)


def line_already_in(diagram, point1, point2):
    for line in diagram.lines:
        if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
            return True
    return False


def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def dist(p1, p2):
    try: value = np.linalg.norm(np.array([p1.x, p1.y]) - np.array([p2.x, p2.y]))
    except:
        try: value = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        except: raise ValueError
    return value

def points_too_close(coordinates, new_coordinate):
    min_dist = min([dist(coord, new_coordinate) for coord in coordinates])
    return min_dist < 100


def label_point(diagram):
    ind = 0
    while True:
        label = random.choice(capitals.candidates)
        if label not in [point.label for point in diagram.points]:
            return label
        if ind > 200:
            raise ValueError(
                f'No possible label found with currently {len(diagram.points)} points of list : {[point.label for point in diagram.points]}')

        ind += 1


def label_line(diagram):
    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if (label == "") or (label not in [line.label for line in diagram.lines]):
            return label
        if ind > 200:
            raise ValueError(
                f'No possible label found with currently {len(diagram.lines)} lines of list : {[line.label for line in diagram.lines]}')
        ind += 1

def label_line_nonempty(diagram):
    ind = 0
    while True:
        label = random.choice(small_letters_nonempty.candidates)
        if label not in [line.label for line in diagram.lines]:
            return label
        if ind > 200:
            raise ValueError(
                f'No possible label found with currently {len(diagram.lines)} lines of list : {[line.label for line in diagram.lines]}')
        ind += 1


def random_length():
    return int(random.uniform(300, 2000))


def add_radius(center_x, center_y, radius):
    angle = random_angle()
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    length = f'{random_length()}'
    return (x, y, length)


def intersection_of_two_lines(L1, L2):
    A, B = L1.point1, L1.point2
    P, Q = L2.point1, L2.point2

    A_ab = B.y - A.y
    B_ab = A.x - B.x
    C_ab = B.x * A.y - A.x * B.y

    A_pq = Q.y - P.y
    B_pq = P.x - Q.x
    C_pq = Q.x * P.y - P.x * Q.y

    x = (B_ab * C_pq - B_pq * C_ab)/(A_ab * B_pq - A_pq * B_ab)
    y = (A_pq * C_ab - A_ab * C_pq)/(A_ab * B_pq - A_pq * B_ab)


    return (x,y)


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


# Objects definition
class Point:
    def __init__(self, x, y, label, color='black'):
        self.x = x
        self.y = y
        self.coord = (x, y)
        self.label = label
        self.color = color

    def __str__(self):
        return f'Point({self.x}, {self.y}, {self.label})'


class Line:
    def __init__(self, point1: Point, point2: Point, label, infinite=False, tickmarks=0, dotted=False, color='black'):
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
    def __init__(self, center, radius, label, color='black'):
        self.center = center
        self.radius = radius
        self.label = label
        self.color = color

    def __str__(self):
        return f'Circle({self.center}, {self.radius}, {self.label})'


class Triangle:
    def __init__(self, point1, point2, point3, label=''):
        self.vertices = [point1, point2, point3]
        # self.label = label
        self.label = f'Triangle({point1.label}{point2.label}{point3.label})'

    def __str__(self):
        return f'Triangle({self.vertices}, {self.label})'


class Curve:
    def __init__(self, x, y, label, color='black'):
        self.x = x
        self.y = y
        self.label = label
        self.color = color

    def __str__(self):
        return f'Curve({self.label})'


class polygon:
    def __init__(self, points, label='', edge_color='black', fill_color='white'):
        self.points = points
        self.label = label
        self.edge_color = edge_color
        self.fill_color = fill_color

    def __str__(self):
        return f'Polygon({self.vertices}, {self.label})'


class filled_circle:
    def __init__(self, center, radius, label='', edge_color='black', fill_color='white'):
        self.center = center  # (x,y)
        self.radius = radius
        self.label = label
        self.edge_color = edge_color
        self.fill_color = fill_color

    def __str__(self):
        return f'Filled_Circle({self.center}, {self.radius}, {self.label})'


# Diagram definition
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
    x, y = vector
    assert x!= 0 or y!= 0
    
    magnitude = (x ** 2 + y ** 2) ** 0.5
    return (x / magnitude, y / magnitude)


def assert_coord_in_range(x, y):
    return x < 1000 and x > 0 and y < 1000 and y > 0


def add_free_point(diagram: Diagram):
    x_coord, y_coord = random_coord(), random_coord()
    label = label_point(diagram)
    diagram.points.append(Point(x_coord, y_coord, label))
    # diagram.entities.append(f'Point({label})')
    return diagram


def C_add_free_point(diagram: Diagram):
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
        length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if length > 400:
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
        length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
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

    diagram.lines.append(Line(diagram.points[-2], diagram.points[-1], label, color=color))

    # diagram.entities.extend([f'{label} : Line({label1}{label2})'])
    return diagram


def add_free_point_with_line(diagram: Diagram):
    if len(diagram.points) == 0:
        diagram = add_free_point(diagram)

    p1 = random.choice(diagram.points)
    ind = 0
    while True:
        x_coord, y_coord = random_coord(), random_coord()
        length = ((p1.x - x_coord) ** 2 + (p1.y - y_coord) ** 2) ** 0.5
        label = label_point(diagram)
        if length > 200:
            break
        if ind > 30:
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


def C_add_free_point_with_line(diagram: Diagram):
    color = random.choice(diagram.usable_colors)
    diagram = remove_color(diagram, color)

    if len(diagram.points) == 0:
        diagram = add_free_point(diagram)
    p1 = random.choice(diagram.points)
    ind = 0
    while True:
        x_coord, y_coord = random_coord(), random_coord()
        length = ((p1.x - x_coord) ** 2 + (p1.y - y_coord) ** 2) ** 0.5
        label = label_point(diagram)
        if length > 200:
            break
        if ind > 30:
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
    diagram.lines.append(Line(p1, diagram.points[-1], label_l, color=color))
    return diagram


def add_line(diagram: Diagram):
    try:
        ind = 0
        while True:

            point1, point2 = random.sample(diagram.points, 2)
            length = ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

            # assert that the line is not already in the diagram
            already_in = False
            for line in diagram.lines:
                if (line.point1 == point1 and line.point2 == point2) or (
                        line.point1 == point2 and line.point2 == point1):
                    already_in = True

            if ind > 100:
                raise ValueError('No possible line found')
            # elif already_in: print('already in')
            else:
                break

            ind += 1

        label = random.choice(small_letters.candidates.extend(["", "", "", "", "", ""]))
        diagram.lines.append(Line(point1, point2, label))

        return diagram
    except:
        return diagram


def C_add_line(diagram: Diagram):
    try:
        color = random.choice(diagram.usable_colors)
        diagram = remove_color(diagram, color)

        ind = 0
        while True:

            point1, point2 = random.sample(diagram.points, 2)
            length = ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

            # assert that the line is not already in the diagram
            already_in = False
            for line in diagram.lines:
                if (line.point1 == point1 and line.point2 == point2) or (
                        line.point1 == point2 and line.point2 == point1):
                    already_in = True

            if ind > 100:
                raise ValueError('No possible line found')
            # elif already_in: print('already in')
            else:
                break

            ind += 1

        label = random.choice(small_letters.candidates.extend(["", "", "", "", "", ""]))
        diagram.lines.append(Line(point1, point2, label, color=color))

        return diagram
    except:
        return diagram


def add_infinite_line(diagram: Diagram):
    point1, point2 = random.sample(diagram.points, 2)
    label = ''
    diagram.lines.append(Line(point1, point2, label, infinite=True))

    return diagram


def C_add_infinite_line(diagram: Diagram):
    color = random.choice(diagram.usable_colors)
    diagram = remove_color(diagram, color)

    point1, point2 = random.sample(diagram.points, 2)
    label = ''
    diagram.lines.append(Line(point1, point2, label, infinite=True, color=color))

    return diagram


def add_circle(diagram: Diagram, radius=None):
    if len(diagram.points) == 0:
        diagram = add_free_point(diagram)
    center = random.choice(diagram.points)
    max_rad = min(center.x, center.y, 1000 - center.x, 1000 - center.y)
    if radius is None:
        ind = 0
        while True:
            radius = random.uniform(150, max_rad)
            if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                     center.y - radius):
                break
            if ind > 10:
                return diagram
            ind += 1

    else:
        radius = radius
        

    # label = random.choice(small_letters.candidates)
    label = f'({center.label},{radius})'
    different_pt_label = label_point(diagram)
    diagram.circles.append(Circle(center, radius, label))

    return diagram


def C_add_circle(diagram: Diagram, radius=None):
    color = random.choice(diagram.usable_colors)
    diagram = remove_color(diagram, color)

    if len(diagram.points) == 0:
        diagram = add_free_point(diagram)

    center = random.choice(diagram.points)
    max_rad = min(center.x, center.y, 1000 - center.x, 1000 - center.y)
    if radius is None:
        ind = 0
        while True:
            radius = random.uniform(150, max_rad)
            if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                     center.y - radius):
                break
            if ind > 10:
                return diagram
            ind += 1

    else:
        radius = radius
        

    # label = random.choice(small_letters.candidates)
    label = f'({center.label},{radius})'
    different_pt_label = label_point(diagram)
    diagram.circles.append(Circle(center, radius, label, color=color))

    return diagram


def add_free_circle(d):
    ind = 0
    while True:
        x_coord, y_coord = random_coord(), random_coord()
        center = Point(x_coord, y_coord, label_point(d))
        radius = int(random.uniform(200, 500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                 center.y - radius):
            break
        if ind > 30:
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
        radius = int(random.uniform(200, 500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                 center.y - radius):
            break
        if ind > 30:
            return d
        ind += 1

    d.points.append(center)
    d.circles.append(Circle(center, radius, f'({center.label},{radius})', color=color))

    return d


def circle_with_radius(d):
    while True:
        center = Point(random_coord(), random_coord(), label_point(d))
        radius = int(random.uniform(50, 500))
        if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                 center.y - radius):
            break
    circle = Circle(center, radius, '')
    angle = random_angle()
    x, y = center.x + radius * np.cos(angle), center.y + radius * np.sin(angle)
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
    circle = Circle(center, radius, '', color=color)
    angle = random_angle()
    x, y = center.x + radius * np.cos(angle), center.y + radius * np.sin(angle)
    P = Point(x, y, "")
    length = random_length()
    d.points.append(center)
    d.circles.append(circle)
    d.lines.append(Line(center, P, label=length, dotted=True, color=color_2))

    return d



def angle_bisector(diagram: Diagram):
    while len(diagram.points) < 3:
        diagram = add_free_point(diagram)


    ind = 0
    while True:
        print(f"angle bisector: {len(diagram.points)}")
        A, B, C = random.sample(diagram.points, 3)

        # Calculate direction vectors BA and BC
        vector_BA = (A.x - B.x, A.y - B.y)
        vector_BC = (C.x - B.x, C.y - B.y)

        # Normalize the vectors to get unit vectors
        unit_BA = normalize(vector_BA)
        unit_BC = normalize(vector_BC)
        if unit_BA[0]*unit_BC[0] + unit_BA[1]*unit_BC[1] < 0.71: #pi/4
            # If Line(AB) is not in the diagram.entities, add it
            if (A, B) not in [(line.point1, line.point2) for line in diagram.lines] and (B, A) not in [
                (line.point1, line.point2) for line in diagram.lines]:
                diagram.lines.append(Line(A, B, ""))
                # diagram.entities.append(f'Line({A.label}{B.label})')

            if (B, C) not in [(line.point1, line.point2) for line in diagram.lines] and (C, B) not in [
                (line.point1, line.point2) for line in diagram.lines]:
                diagram.lines.append(Line(B, C, ""))
                # diagram.entities.append(f'Line({B.label}{C.label})')
            break
        if ind > 50:
            return diagram
        ind += 1


    # Add the unit vectors to get the direction of the bisector
    bisector_direction = (unit_BA[0] + unit_BC[0], unit_BA[1] + unit_BC[1])
    bisector_unit = normalize(bisector_direction)

    ind = 0
    # Determine the length for the bisector and calculate the endpoint X
    while True:
        length = random_coord()
        if assert_coord_in_range(B.x + bisector_unit[0] * length, B.y + bisector_unit[1] * length):
            break
        if ind > 50:
            return diagram
        ind += 1

    new_label = label_point(diagram)

    bisector_pt = Point(B.x + bisector_unit[0] * length, B.y + bisector_unit[1] * length, new_label)

    #add stuffs to diagram
    diagram.points.append(bisector_pt)
    ind = 0
    while True:
        new_label = random.choice(small_letters.candidates)
        if new_label not in [line.label for line in diagram.lines]:
            break
        if ind>30:
            return diagram
        ind += 1



    is_infinite = random_coord() < 500
    diagram.lines.append(Line(B, bisector_pt, new_label,infinite=is_infinite))
    # diagram.entities.append(f'{new_label} : Line({B.label}{bisector_pt.label}) bisecting angle {A.label}{B.label}{C.label}')
    diagram.entities.append(('angle_bisector', [A.label, B.label, C.label, bisector_pt.label]))

    return diagram


def circle_center(diagram: Diagram):

    if len(diagram.lines) < 1:
        diagram = add_free_line(diagram)
    # Calculate midpoints of AB and BC
    line = random.choice(diagram.lines)

    color = line.color

    A, B = line.point1, line.point2

    C_x, C_y = random_coord(), random_coord()
    C_label = label_point(diagram)
    C = Point(C_x, C_y, C_label)



    midpoint_AB = ((A.x + B.x) / 2, (A.y + B.y) / 2)
    midpoint_BC = ((B.x + C.x) / 2, (B.y + C.y) / 2)

    perp_bisector_AB = None
    perp_bisector_BC = None

    # Check for vertical lines and set perpendicular directions
    if A.x == B.x:  # AB is vertical
        perp_bisector_AB = "horizontal"
        c_AB = midpoint_AB[0]  # x-coordinate for the vertical bisector
    else:
        slope_AB = (B.y - A.y) / (B.x - A.x)
        perp_slope_AB = -1 / slope_AB
        c_AB = midpoint_AB[1] - perp_slope_AB * midpoint_AB[0]

    if B.x == C.x:  # BC is vertical
        perp_bisector_BC = "horizontal"
        c_BC = midpoint_BC[0]  # x-coordinate for the vertical bisector
    else:
        slope_BC = (C.y - B.y) / (C.x - B.x)
        perp_slope_BC = -1 / slope_BC
        c_BC = midpoint_BC[1] - perp_slope_BC * midpoint_BC[0]

    # Calculate the intersection of the perpendicular bisectors
    if perp_bisector_AB == "horizontal" and perp_bisector_BC != "horizontal":
        Xx = c_AB
        Xy = perp_slope_BC * Xx + c_BC
    elif perp_bisector_BC == "horizontal" and perp_bisector_AB != "horizontal":
        Xx = c_BC
        Xy = perp_slope_AB * Xx + c_AB
    elif perp_bisector_AB != "horizontal" and perp_bisector_BC != "horizontal":
        Xx = (c_BC - c_AB) / (perp_slope_AB - perp_slope_BC)
        Xy = perp_slope_AB * Xx + c_AB

    new_label = label_point(diagram)

    radius = ((Xx - A.x) ** 2 + (Xy - A.y) ** 2) ** 0.5
    

    circumcenter = Point(Xx, Xy, new_label)
    diagram.points.extend([C, circumcenter])
    diagram.lines.extend([Line(B, C, '', color = color), Line(C, A, '', color = color)])
    # diagram.entities.append(f'Circumcenter Point({new_label})')

    diagram.circles.append(Circle(circumcenter, radius, ''))
    # diagram.entities.append(f'Circumscriber Circle({circumcenter.label},{radius}) for triangle {A.label}{B.label}{C.label}')
    diagram.entities.append(('circle_center', [A.label, B.label, C.label, circumcenter.label]))

    return diagram

def eq_quadrilateral(diagram: Diagram):
    #Geneerate a quadrilateral with AD= BC
    # Randomly select three points
    while len(diagram.points) < 1:
        diagram = add_free_point(diagram)

    # 그냥 x축 기준으로 사각형 만들어서 x축 cross 안하게 하고 rotate시켜...
    ind = 0
    while True:
        l = random_length()
        l2 = random_length()
        A = random.choice(diagram.points)
        Bx, By = A.x + l, A.y

        angle_BC = random.uniform(np.pi/7, np.pi*6/7) #Make sure its y coord > 0
        Cx, Cy = Bx + l2*np.cos(angle_BC), By + l2*np.sin(angle_BC)

        angle_AD = random.uniform(np.pi/7, np.pi*6/7) #Make sure its y coord > 0
        Dx, Dy = A.x + l2*np.cos(angle_AD), A.y + l2*np.sin(angle_AD)

        if  Dx < Cx: #Make sure AD does not cross BC
            #rotate the points
            angle = random.uniform(0, np.pi*2)
            pivot = np.array([A.x, A.y])


            Bx, By = rotate_vector( np.array([Bx, By]) - pivot , angle) + pivot
            Cx, Cy = rotate_vector( np.array([Cx, Cy]) - pivot , angle) + pivot
            Dx, Dy = rotate_vector( np.array([Dx, Dy]) - pivot , angle) + pivot

            if  assert_coord_in_range(Bx, By) and assert_coord_in_range(Cx, Cy) and assert_coord_in_range(Dx, Dy):
                break

        if ind > 50:
            return diagram
        ind += 1

    # Create points B, C, D
    B_label, C_label, D_label = random.sample(capitals.candidates, 3)
    B = Point(Bx, By, B_label)
    C = Point(Cx, Cy, C_label)
    D = Point(Dx, Dy, D_label)

    diagram.points.extend([B, C, D])


    if random.choice([True,False]):
        tcks = 0
    else: tcks = random.randint(1,3)

    # Add lines to form the quadrilateral
    diagram.lines.extend([
        Line(A, B, label=""),
        Line(B, C, label="", tickmarks=tcks),
        Line(C, D, label=""),
        Line(D, A, label="", tickmarks=tcks)
    ])

    diagram.entities.append(('eq_quadrilateral', [A.label, B.label, C.label, D.label]))

    return diagram




def eq_trapezoid(diagram: Diagram): #Construct trapezoid with AD = BC
    
    # Randomly select two points A, B to form the base AB of the trapezoid
    if len(diagram.points) < 1:
        diagram = add_free_point(diagram)
    if len(diagram.lines) < 1:
        diagram = add_free_point_with_line(diagram)

    if random.choice([True, False]):
        A, B = random.sample(diagram.points, 2)
    else: #Make sure the line is not horizontal
        line = random.choice(diagram.lines)
        A, B = line.point1, line.point2
    
    


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

    ind = 0
    
    # Decide on a length for AD and BC
    leg_length = random_length()

    # Calculate points D and C using the determined directions and length
    Dx, Dy = A.x + AD_direction[0] * leg_length, A.y + AD_direction[1] * leg_length
    Cx, Cy = B.x + BC_direction[0] * leg_length, B.y + BC_direction[1] * leg_length

    # Check if D and C are within the diagram range
        
    

    # Create points C and D
    C_label, D_label = random.sample(capitals.candidates, 2)
    C = Point(Cx, Cy, C_label)
    D = Point(Dx, Dy, D_label)
    diagram.points.extend([C, D])
    
    tck = random.choice([1,2,3,4,5])
    # Add lines to form the trapezoid
    diagram.lines.extend([
        Line(A, B, label=""),  # Base AB
        Line(B, C, label="", tickmarks=tck),  # Side BC
        Line(C, D, label=""),  # Top CD, parallel to AB
        Line(D, A, label="", tickmarks=tck)   # Side AD
    ])

    
    diagram.entities.append(('eq_trapezoid', [A.label, B.label, C.label, D.label]))
    return diagram


def eqtriangle(diagram: Diagram): #Construct X that XBC is an equilateral triangle, ieqtriangle also included.
    if random.choice([True, False]):
        new_labels = []
        while len(diagram.points) < 2:
            diagram = add_free_point(diagram)

        if len(diagram.lines) < 1:
            diagram = add_free_point_with_line(diagram)

        if random.choice([True, False]):
            # Calculate the length of BC
            B,C = random.sample(diagram.points, 2)
        else:
            line = random.choice(diagram.lines)
            B, C = line.point1, line.point2
    else:
        while True:
            Bx, By, Cx, Cy = random_coord(), random_coord(), random_coord(), random_coord()
            if dist((Bx,By),(Cx,Cy)) > 100:
                while True:
                    B_label, C_label = label_point(diagram), label_point(diagram)
                    if B_label != C_label:
                        break
                    
                B = Point(Bx, By, B_label)
                C = Point(Cx, Cy, C_label)
                diagram.points.extend([B,C])
                new_labels = [B.label, C.label]
                break
            



    BC_length = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)

    # Angle of line BC with the horizontal
    angle_BC = np.arctan2(C.y - B.y, C.x - B.x)

    # Calculate the positions for X
    # Adding 60 degrees (π/3 radians) for one position
    is_equilateral = random.choice([True,False])
    if is_equilateral:
        randang = np.pi/3
    elif random.choice([True, False]):
        randang = random.uniform(np.pi/9, np.pi / 3.5)
    else: randang = -random.uniform(np.pi/2.5, np.pi / 1.2)
    angle_X1 = angle_BC + randang
    X1_x = B.x + BC_length * np.cos(angle_X1)
    X1_y = B.y + BC_length * np.sin(angle_X1)

    

    # Subtracting 60 degrees (π/3 radians) for the other position
    angle_X2 = angle_BC - randang
    X2_x = B.x + BC_length * np.cos(angle_X2)
    X2_y = B.y + BC_length * np.sin(angle_X2)

    # Choose one of the positions for X (for example, the first one)
    while True:
        X_label = label_point(diagram)
        if X_label not in new_labels:
            break
    X = Point(X1_x, X1_y, X_label)
    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label})')


    if random.choice([True, True, False]):
        tcks = 0
    else:
        tcks = random.randint(1,3)
    # Add lines to form the equilateral triangle


    # label = f'Equilateral Triangle({X.label}{B.label}{C.label}) with length {int(BC_length)}' if is_equilateral else f'Isosceles Triangle({X.label}{B.label}{C.label})'
    # diagram.entities.append(label)
    if is_equilateral:
        diagram.lines.extend([
            Line(B, C, label="", tickmarks=tcks),
            Line(C, X, label="", tickmarks=tcks),
            Line(X, B, label="", tickmarks=tcks)
        ])
        diagram.entities.append(('equilateral_triangle', [X.label, B.label, C.label]))
    else :
        diagram.lines.extend([
            Line(B, C, label="", tickmarks=tcks),
            Line(C, X, label=""),
            Line(X, B, label="", tickmarks=tcks)
        ])
        diagram.entities.append(('isosceles_triangle', [X.label, B.label, C.label]))
    return diagram


def eqdia_quadrilateral(diagram: Diagram): #Construct quadrilateral with AC = BD

    
    
    Ox, Oy = random_coord(), random_coord()
    l1 = random_length()
    l2 = random_length()

    ang_AC = random.uniform(0, np.pi*2)
    ang_BD = random.uniform(np.pi/9, np.pi*8/9)

    Ax, Ay = Ox + l1*np.cos(ang_AC), Oy + l1*np.sin(ang_AC)
    Cx, Cy = Ox - l2*np.cos(ang_AC), Oy - l2*np.sin(ang_AC)

    if random.choice([True, False]):
        Bx, By = Ox + l1*np.cos(ang_AC + ang_BD), Oy + l1*np.sin(ang_AC + ang_BD)
        Dx, Dy = Ox - l2*np.cos(ang_AC + ang_BD), Oy - l2*np.sin(ang_AC + ang_BD)
    else:
        Bx, By = Ox + l2 * np.cos(ang_AC + ang_BD), Oy + l2 * np.sin(ang_AC + ang_BD)
        Dx, Dy = Ox - l1 * np.cos(ang_AC + ang_BD), Oy - l1 * np.sin(ang_AC + ang_BD)

        

    new_labels = []
    while True:
        label = label_point(diagram)
        if label not in new_labels:
            new_labels.append(label)
            if len(new_labels) == 4:
                break

    A = Point(Ax, Ay, new_labels[0])
    B = Point(Bx, By, new_labels[1])
    C = Point(Cx, Cy, new_labels[2])
    D = Point(Dx, Dy, new_labels[3])
    diagram.points.extend([A,B,C,D])

    if random.choice([True, False]):
        tcks = 0
    else:
        tcks = random.randint(1,3)
    # Add lines to form the quadrilateral
    diagram.lines.extend([
        Line(A, B, label=""),
        Line(B, C, label=""),
        Line(C, D, label=""),
        Line(D, A, label=""),
        Line(A,C, label="", dotted=True, tickmarks=tcks),
        Line(B,D, label="", dotted=True, tickmarks=tcks)
    ])

    # Label the quadrilateral
    # label = f'Quadrilateral({A.label}{B.label}{C.label}{D.label}) with {A.label}{C.label}={B.lable}{D.label}'
    # diagram.entities.append(label)
    diagram.entities.append(('eqdia', [A.label, B.label, C.label, D.label]))
    return diagram

def eqdistance(diagram: Diagram): #Construct X such that AX = BC
    while len(diagram.points) < 3:
        diagram = add_free_point(diagram)


    A,B,C = random.sample(diagram.points, 3)
    # Calculate the length of BC
    BC_length = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)

    # Choose a random direction for AX; theta is the angle from the horizontal
    theta = random.uniform(0, 2 * np.pi)  # Angle in radians

    # Calculate the coordinates for X such that the distance AX equals BC's length
    X_x = A.x + BC_length * np.cos(theta)
    X_y = A.y + BC_length * np.sin(theta)

    # Ensure X is within a valid range, if there's such a constraint
        

    if random.choice([True, False]):
        tk = random.randint(1,4)
    else: tk = 0

    diagram.lines.append(Line(B, C, label="", tickmarks=tk))

    X_label = label_point(diagram)
    X = Point(X_x, X_y, X_label)

    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label})')
    diagram.lines.append(Line(A, X, label="", tickmarks=tk))
    # diagram.entities.append(f'Line({A.label}{X.label}) such that {A.label}{X.label}={B.label}{C.label}')
    diagram.entities.append(('eqdistance', [A.label, B.label, C.label, X.label]))
    return diagram


def foot(diagram): #Construct X as the foot of A to BC
    while len(diagram.points) < 3:
        diagram = add_free_point(diagram)

    A,B,C = random.sample(diagram.points, 3)
    # Vector BC
    BC = np.array([C.x - B.x, C.y - B.y])
    # Vector BA
    BA = np.array([A.x - B.x, A.y - B.y])

    # Project BA onto BC to find the vector BX
    t = np.dot(BA, BC) / np.dot(BC, BC)
    BX = t * BC

    # Coordinates of X
    X_x = B.x + BX[0]
    X_y = B.y + BX[1]
    X_label = label_point(diagram)

    X = Point(X_x, X_y, X_label)



    # Ensure X is within a valid range, if necessary
    

    # if not line_already_in(diagram, B, C):
    #     diagram.lines.append(Line(B, C, label=""))
    #     diagram.entities.append(f'Line({B.label}{C.label})')


    # Update the diagram with the new point and potentially the line AX for clarity
    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label}) : foot of {A.label} to {B.label}{C.label}')
    diagram.lines.append(Line(A, X, label="", dotted= True))
    diagram.lines.append(Line(C, B, label=""))
    diagram.lines.append(Line(X, B, label=""))

    # Optionally, label the perpendicular line AX if needed
    # diagram.entities.append(f'Line({A.label}{X.label}), perpendicular to {B.label}{C.label})')
    diagram.entities.append(('foot', [A.label, B.label, C.label, X.label]))
    diagram.perpendiculars.append((Line(A, X, label=""), Line(B, C, label=""), X))

    return diagram


def incenter(diagram: Diagram): #Construct X as the incenter of ABC
    while len(diagram.points) < 3:
        diagram = add_free_point(diagram)

    ind = 0
    while True:
        A, B, C = random.sample(diagram.points, 3)
        length_AB = np.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
        length_BC = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)
        length_CA = np.sqrt((A.x - C.x) ** 2 + (A.y - C.y) ** 2)


        X_x = (length_BC * A.x + length_CA * B.x + length_AB * C.x) / (length_AB + length_BC + length_CA)
        X_y = (length_BC * A.y + length_CA * B.y + length_AB * C.y) / (length_AB + length_BC + length_CA)

        X_label = label_point(diagram)
        X = Point(X_x, X_y, X_label)

        #radius of the incircle
        s = (length_AB + length_BC + length_CA) / 2
        radius = (s * (s - length_AB) * (s - length_BC) * (s - length_CA)) ** 0.5 / s

        if radius > 50:
            break

        if ind > 100:
            return diagram
        ind += 1

    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])

    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label}) : incenter of {A.label}{B.label}{C.label}')


    diagram.circles.append(Circle(X, radius, ''))
    # diagram.entities.append(f'Incircle({X.label},{radius}) for triangle {A.label}{B.label}{C.label}')
    diagram.entities.append(('incenter', [A.label, B.label, C.label, X.label, f'{radius}']))
    return diagram

def incenter2(diagram: Diagram): #Constrcut X as the incenter of ABC with touchpoints
    while len(diagram.points) < 3:
        diagram = add_free_point(diagram)
    # Randomly select three points A, B, and C
    ind = 0
    while True:
        A, B, C = random.sample(diagram.points, 3)

        length_AB = np.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
        length_BC = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)
        length_CA = np.sqrt((A.x - C.x) ** 2 + (A.y - C.y) ** 2)

        X_x = (length_BC * A.x + length_CA * B.x + length_AB * C.x) / (length_AB + length_BC + length_CA)
        X_y = (length_BC * A.y + length_CA * B.y + length_AB * C.y) / (length_AB + length_BC + length_CA)
        X_label = label_point(diagram)

        X = Point(X_x, X_y, X_label)

        # radius of the incircle
        s = (length_AB + length_BC + length_CA) / 2
        radius = (s * (s - length_AB) * (s - length_BC) * (s - length_CA)) ** 0.5 / s

        if radius > 50:
            break

        if ind > 30:
            return diagram
        ind += 1


    # Get touchpoints of the incircle
    AB = np.array([B.x - A.x, B.y - A.y])
    BC = np.array([C.x - B.x, C.y - B.y])
    CA = np.array([A.x - C.x, A.y - C.y])

    # Calculate the foots from X
    touch_AB_x = A.x + np.dot(AB, (X_x - A.x, X_y - A.y)) / np.dot(AB, AB) * AB[0]
    touch_AB_y = A.y + np.dot(AB, (X_x - A.x, X_y - A.y)) / np.dot(AB, AB) * AB[1]
    touch_BC_x = B.x + np.dot(BC, (X_x - B.x, X_y - B.y)) / np.dot(BC, BC) * BC[0]
    touch_BC_y = B.y + np.dot(BC, (X_x - B.x, X_y - B.y)) / np.dot(BC, BC) * BC[1]
    touch_CA_x = C.x + np.dot(CA, (X_x - C.x, X_y - C.y)) / np.dot(CA, CA) * CA[0]
    touch_CA_y = C.y + np.dot(CA, (X_x - C.x, X_y - C.y)) / np.dot(CA, CA) * CA[1]



    label_touch_BC = label_point(diagram)
    label_list = [label_touch_BC]
    ind = 0
    while True:
        label_touch_CA = label_point(diagram)
        if label_touch_CA != label_touch_BC:
            label_list.append(label_touch_CA)
            break
        if ind > 30:
            return diagram
        ind = ind + 1

    ind = 0
    while True:
        label_touch_AB = label_point(diagram)
        if label_touch_AB not in label_list:
            break
        if ind > 30:
            return diagram
        ind = ind + 1

    touch_BC = Point(touch_BC_x, touch_BC_y, label_touch_BC)
    touch_CA = Point(touch_CA_x, touch_CA_y, label_touch_CA)
    touch_AB = Point(touch_AB_x, touch_AB_y, label_touch_AB)

    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])

    if random.choice([True, False]):

        diagram.perpendiculars.append((Line(X, touch_AB, ''), Line(A, B, ''), touch_AB))
        diagram.perpendiculars.append((Line(X, touch_BC, ''), Line(B, C, ''), touch_BC))
        diagram.perpendiculars.append((Line(X, touch_CA, ''), Line(C, A, ''), touch_CA))
        diagram.lines.extend([Line(X, touch_AB, label="", dotted=True), Line(X, touch_BC, label="", dotted=True), Line(X, touch_CA, label="", dotted=True)])

    diagram.points.append(X)
    diagram.points.extend([touch_AB, touch_BC, touch_CA])
    diagram.circles.append(Circle(X, radius, f'Incenter Circle({X.label},{radius})'))

    diagram.entities.append(('incenter2', [A.label, B.label, C.label, X.label, f'{radius}', touch_AB.label, touch_BC.label, touch_CA.label]))

    return diagram


def tangent(diagram): #Construct T such that T is tangent to circle O at point P
    while len(diagram.circles) < 1:
        diagram = add_free_circle(diagram)
    circ = random.choice(diagram.circles)
    center = circ.center
    radius = circ.radius
    ang = random.uniform(0, 2*np.pi)
    Tx = center.x + radius * np.cos(ang)
    Ty = center.y + radius * np.sin(ang)

    T_label = label_point(diagram)

    point = Point(Tx, Ty, T_label)
    vec = (point.x - center.x, point.y - center.y)
    perp_vec = [vec[1], -vec[0]]
    ind = 0
    while True:
        scale = random.uniform(-3, 3)

        perp_vec[0] = scale * perp_vec[0]
        perp_vec[1] = scale * perp_vec[1]
        new_label = label_point(diagram)

        if ind > 100:
            return diagram
        if new_label != T_label:
            break
        ind +=1

    if random.choice([True, False]) :
        is_inf, inf_label = (True,f'Infinite tangent line at {T_label}')
        diagram.entities.append(('inf_tangent', [center.label, T_label]))

    else:
        is_inf, inf_label = (False, f'Line({T_label}{new_label}) tangent')
        diagram.points.append(Point(point.x + perp_vec[0], point.y + perp_vec[1], new_label))
        diagram.entities.append(('tangent', [center.label, T_label, new_label]))


    diagram.points.append(point)
    diagram.lines.append(Line(center, point, label="", dotted = True))
    diagram.lines.append(Line(point, Point(point.x + perp_vec[0], point.y + perp_vec[1], ""), label="", infinite=is_inf))
    # diagram.entities.append(inf_label + f' to Circle({center.label},{radius})')

    return diagram


def mirror(diagram : Diagram): # given A, O, find B such that O is the midpoint of AB
    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)
    A, O = random.sample(diagram.points, 2)
    if A == O:
        return diagram
    vector = (O.x - A.x, O.y - A.y)

    B_x = O.x + vector[0]
    B_y = O.y + vector[1]
    B_label = label_point(diagram)
    B = Point(B_x, B_y, B_label)

    if random.choice([True, False]):
        tk = random.randint(1,5)
        diagram.lines.append(Line(A, O, label="", tickmarks=tk))
        diagram.lines.append(Line(O, B, label="", tickmarks=tk))

    diagram.points.append(B)
    # diagram.entities.append(f'Point({B.label}) : mirror of {A.label} over {O.label}')
    diagram.entities.append(('mirror', [A.label, O.label, B.label]))
    return diagram

def right_iso(diagram: Diagram): 
    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)

    #given A, B, find C such that ABC is a right isosceles triangle, "rotate90" of the original rules
    A, B = random.sample(diagram.points, 2)
    vector = (B.x - A.x, B.y - A.y)

    if random.choice([True, False]):
        C_x, C_y = A.x + vector[1], A.y - vector[0]
    else:
        C_x, C_y = A.x - vector[1], A.y + vector[0]

    ind = 0
    C_label = label_point(diagram)
    C = Point(C_x, C_y, C_label)
    diagram.points.append(C)

    tk = random.randint(0,5)

    diagram.lines.extend([Line(A, B, label="", tickmarks=tk), Line(B, C, label=""), Line(C, A, label="", tickmarks=tk)])
    diagram.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
    diagram.entities.append(('right_iso', [A.label, B.label, C.label]))

    return diagram

def parallelogram(diagram: Diagram): #"X = parallelogram(A, B, C)": { "Description": "Construct X such that ABCX is a parallelogram" },
    while len(diagram.points) < 3:
        diagram = add_free_point(diagram)

    A, B, C = random.sample(diagram.points, 3)
    vector = (B.x - A.x, B.y - A.y)
    D_x = C.x - vector[0]
    D_y = C.y - vector[1]
    

    D_label = label_point(diagram)

    D = Point(D_x, D_y, D_label)
    diagram.points.append(D)
    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
    # diagram.entities.append(f'Parallelogram({A.label}{B.label}{C.label}{D.label})')
    diagram.entities.append(('parallelogram', [A.label, B.label, C.label, D.label])) #D = X
    return diagram


def pentagon(diagram: Diagram):
    #"Pentagon(A, B, C, D, E)": { "Description": "Construct a pentagon with vertices A, B, C, D, E" },
    randnum = random.randint(0, 3)

    while len(diagram.points) < randnum:
        diagram = add_free_point(diagram)
    points = random.sample(diagram.points, randnum)
    label_list = []
    for i in range(5 - randnum):
        while True:
            x, y = random_coord(), random_coord()
            label = label_point(diagram)
            if assert_coord_in_range(x, y) and label not in label_list:
                label_list.append(label)
                break
        points.append(Point(x, y, label))


    midpt = (0,0)
    for point in points:
        midpt = (midpt[0] + point.x/5, midpt[1] + point.y/5)

    #sort the points in clockwise order
    points.sort(key=lambda point: np.arctan2(point.y - midpt[1], point.x - midpt[0]))
    for i in range(5):
        diagram.points.append(points[i])
        diagram.lines.append(Line(points[i], points[(i+1)%5], label=""))

    # diagram.entities.append(f'Pentagon({points[0].label}{points[1].label}{points[2].label}{points[3].label}{points[4].label})')
    diagram.entities.append(('pentagon', [point.label for point in points]))
    return diagram


def quadrilateral(d): #quadrilateral of the old rules, generate a random quadrilateral
    while len(d.points) < 2:
        d = add_free_point(d)
    A, B = random.sample(d.points, 2)
    C_x, C_y = random_coord(), random_coord()
    D_x, D_y = random_coord(), random_coord()
    while True:
        C_label, D_label = label_point(d), label_point(d)
        if C_label != D_label:
            break

    C = Point(C_x, C_y, C_label)
    D = Point(D_x, D_y, D_label)
    d.points.extend([C, D])

    #sort A,B,C,D clockwise
    points = [A, B, C, D]
    center = Point((A.x + B.x + C.x + D.x)/4, (A.y + B.y + C.y + D.y)/4, '')
    points.sort(key=lambda p: np.arctan2(p.y - center.y, p.x - center.x))
    A, B, C, D = points

    d.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
    # d.entities.append(f'Square({A.label}{B.label}{C.label}{D.label})')
    d.entities.append(('quadrilateral', [A.label, B.label, C.label, D.label]))

    return d

def ellipse_line_intersect(d):
    t = np.linspace(0, 2 * np.pi, 1000)

    while True:
        x, y = int(random_coord()), int(random_coord())
        length1 = int(random.uniform(100, 400))
        angle1 = random_angle()
        length2 = int(random.uniform(1.5, 3) * length1)
        # angle2 = angle1 + np.pi/2

        x0 = length1 * np.cos(t)
        y0 = length2 * np.sin(t)

        if assert_coord_in_range(x + length2, y + length2) and assert_coord_in_range(x - length2, y - length2):
            break

    x1 = np.cos(angle1) * x0 - np.sin(angle1) * y0 + x
    y1 = np.sin(angle1) * x0 + np.cos(angle1) * y0 + y

    t1 = random.uniform(0, np.pi)
    t2 = t1 + random.uniform(np.pi / 4, np.pi)
    # T1_x, T1_y = x + length1 * np.cos(t1), y + length2 * np.sin(t1)
    # T2_x, T2_y = x + length1 * np.cos(t2), y + length2 * np.sin(t2)

    T1_x, T1_y = x1[int(t1/2/np.pi*1000)], y1[int(t1/2/np.pi*1000)]
    T2_x, T2_y = x1[int(t2/2/np.pi*1000)], y1[int(t2/2/np.pi*1000)]

    T1_label = label_point(d)
    while True:
        T2_label = label_point(d)
        if T2_label != T1_label:
            break

    T1, T2 = Point(T1_x, T1_y, T1_label), Point(T2_x, T2_y, T2_label)
    d.points.extend([T1, T2])
    d.lines.append(Line(T1, T2, label="", infinite=True))
    d.curves.append(Curve(x1, y1, label="ellipse"))
    # d.entities.append(f'An ellipse and a line intersects at points {T1.label} and {T2.label}')
    d.entities.append(('ellipse_line_intersect', [T1.label, T2.label]))
    return d

def ellipse(d):
    t = np.linspace(0, 2 * np.pi, 1000)


    x,y = int(random_coord()), int(random_coord())
    length1 = int(random.uniform(100, 400))
    angle1 = random_angle()
    length2 = int(random.uniform(1.5, 3) * length1)
    # angle2 = angle1 + np.pi/2

    x0 =  length1 * np.cos(t)
    y0 =  length2 * np.sin(t)

    c = (length2**2 -length1**2)**0.5

    x1 = np.cos(angle1) * x0 - np.sin(angle1) * y0 + x
    y1 = np.sin(angle1) * x0 + np.cos(angle1) * y0 + y

    d.curves.append(Curve(x1, y1, label="ellipse"))



    focus1_x, focus1_y = np.cos(angle1+np.pi/2) * c + x, np.sin(angle1+np.pi/2) * c + y
    focus2_x, focus2_y = np.cos(angle1+np.pi/2) * (-c) + x, np.sin(angle1+np.pi/2) * (-c) + y
    new_labels = []
    while len(new_labels) < 2:
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)

    d.entities.append(('ellipse', new_labels))
    d.points.extend([Point(focus1_x, focus1_y, new_labels[0]), Point(focus2_x, focus2_y, new_labels[1])])

    return d


def random_curve(d):
    x = np.linspace(0, 1000, 1000)
    a = random.uniform(-0.1, 0.1)
    i = random.choice(range(1,10))
    y = a
    for j in range(i):
        b = random.uniform(200,800)
        y= y*(x-b)

    max_y = max(abs(np.min(y)), abs(np.max(y)))
    y= y / max_y * 500 + 500

    d.curves.append(Curve(x, y, label=""))
    # d.entities.append(f'Random curve')
    d.entities.append(('random_curve', []))

    return d




def square(diagram):
    if random.choice([True, False]):
        while len(diagram.lines) < 1:
            diagram = add_free_line(diagram)
        l = random.choice(diagram.lines)
        A, B = l.point1, l.point2
    else:
        while len(diagram.points) < 2:
            diagram = add_free_point(diagram)
        A, B = random.sample(diagram.points, 2)
        diagram.lines.append(Line(A, B, label=""))
    vector = random.choice( [(B.x - A.x, B.y - A.y), (A.x - B.x, A.y - B.y)])


    perp_vector = (vector[1], -vector[0])
    C_x, C_y = A.x + perp_vector[0], A.y +perp_vector[1]
    D_x, D_y = B.x + perp_vector[0], B.y + perp_vector[1]
    
    C_x, C_y = A.x - perp_vector[0], A.y -  perp_vector[1]
    D_x, D_y = B.x - perp_vector[0], B.y -  perp_vector[1]
    

    lable_C = label_point(diagram)
    label_D = label_point(diagram)
    C = Point(C_x, C_y, lable_C)
    D = Point(D_x, D_y, label_D)
    diagram.points.extend([C, D])

    if random.choice([True, False]):
        tk = random.choice([1, 1, 2, 2, 3, 3, 4, 5])
        diagram.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
        diagram.perpendiculars.append((Line(D, C, label=""), Line(D, B, label=""), D))
        diagram.perpendiculars.append((Line(A, B, label=""), Line(B, D, label=""), B))
        diagram.perpendiculars.append((Line(C, D, label=""), Line(C, A, label=""), C))
    else:
        tk = 0

    diagram.lines.extend([Line(A, B, label="", tickmarks=tk), Line(B, D, label="", tickmarks=tk),
                          Line(C, D, label="", tickmarks=tk), Line(C, A, label="",tickmarks=tk)])

    # diagram.entities.append(f'Square({A.label}{B.label}{D.label}{C.label})')
    diagram.entities.append(('square', [A.label, B.label, D.label,C.label]))
    return diagram


def triangle12(diagram):
    #construct triangle ABC with AB : BC = 1: 2
    if random.choice([True, False]):  #Use new oints

        B = Point(random_coord(), random_coord(), label_point(diagram))
        new_labels = [B.label]
        length = random_length()
        angle1 = random_angle()
        angle2 = random_angle()
        ratio = random.randint(1, 4)

        A_x = B.x + length * np.cos(angle1)
        A_y = B.y + length * np.sin(angle1)
        C_x = B.x + ratio*length * np.cos(angle2)
        C_y = B.y + ratio*length * np.sin(angle2)


        while True:
            label_A = label_point(diagram)
            label_C = label_point(diagram)
            if label_A not in new_labels and label_C != label_A:
                new_labels.append(label_A)
                new_labels.append(label_C)
                break

        A = Point(A_x, A_y, label_A)
        C = Point(C_x, C_y, label_C)

        diagram.points.extend([A, B, C])
        diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])
        diagram.entities.append(('triangle12', [A.label, B.label, C.label, f'{ratio}']))

    else: #Use existing line,
        while len(diagram.lines) < 1:
            diagram = add_free_line(diagram)

        l = random.choice(diagram.lines)
        A, B = l.point1, l.point2
        ratio = random.randint(1, 4)

        angle = random.uniform(0, np.pi*2)
        vec_BA = np.array([A.x - B.x, A.y - B.y])
        vec_BC = rotate_vector(vec_BA, angle)
        C_x = B.x + ratio * vec_BC[0]
        C_y = B.y + ratio * vec_BC[1]

        C = Point(C_x, C_y, label_point(diagram))

        diagram.points.append(C)
        diagram.lines.append(Line(B, C, label=""))
        diagram.lines.append(Line(C, A, label=""))
        diagram.entities.append(('triangle12', [A.label, B.label, C.label, f'{ratio}']))

    return diagram


def init_square(diagram):
    while True:
        A, B = Point(random_coord(), random_coord(), label_point(diagram)), Point(random_coord(), random_coord(), label_point(diagram))
        if A.label != B.label:
            new_labels = [A.label, B.label]
            diagram.points.extend([A, B])
            break

    diagram.lines.append(Line(A, B, label=""))
    vector = random.choice( [(B.x - A.x, B.y - A.y), (A.x - B.x, A.y - B.y)])


    perp_vector = (vector[1], -vector[0])
    C_x, C_y = A.x + perp_vector[0], A.y +perp_vector[1]
    D_x, D_y = B.x + perp_vector[0], B.y + perp_vector[1]
    
    C_x, C_y = A.x - perp_vector[0], A.y -  perp_vector[1]
    D_x, D_y = B.x - perp_vector[0], B.y -  perp_vector[1]
    
    lable_C = label_point(diagram)
    label_D = label_point(diagram)
    C = Point(C_x, C_y, lable_C)
    D = Point(D_x, D_y, label_D)
    diagram.points.extend([C, D])

    if random.choice([True, False]):
        tk = random.choice([1, 1, 2, 2, 3, 3, 4, 5])
        diagram.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
        diagram.perpendiculars.append((Line(D, C, label=""), Line(D, B, label=""), D))
        diagram.perpendiculars.append((Line(A, B, label=""), Line(B, D, label=""), B))
        diagram.perpendiculars.append((Line(C, D, label=""), Line(C, A, label=""), C))
    else:
        tk = 0

    diagram.lines.extend([Line(A, B, label="", tickmarks=tk), Line(B, D, label="", tickmarks=tk),
                          Line(C, D, label="", tickmarks=tk), Line(C, A, label="",tickmarks=tk)])

    diagram.entities.append(('square', [A.label, B.label, D.label,C.label]))
    return diagram


def on_bline(diagram: Diagram):
    #"X = on_bline(X, A, B)": { "Description": "Construct X on the perpendicular bisector of AB" },
    if len(diagram.lines) < 1:
        while len(diagram.points) < 2:
            diagram = add_free_point(diagram)
        A, B = random.sample(diagram.points, 2)
        diagram.lines.append(Line(A, B, label=""))
        l = Line(A, B, label="")
    else:
        l = random.choice(diagram.lines)
    A,B = l.point1, l.point2
    vector = (B.x - A.x, B.y - A.y)

    X_label = label_point(diagram)

    ind = 0
    while True :
        mdpt_label = label_point(diagram)
        if mdpt_label != X_label:
            break
        if ind > 30:
            return diagram
        ind = ind + 1
    midpt = Point((A.x + B.x) / 2, (A.y + B.y) / 2, mdpt_label)
    diagram.points.append(midpt)

    perp_vector = (vector[1], -vector[0])
    ind = 0
    while True:
        scale = random.uniform(-3, 3)
        X_x = midpt.x + scale * perp_vector[0]
        X_y = midpt.y + scale * perp_vector[1]
        if assert_coord_in_range(X_x, X_y):
            break
        if ind > 30:
            return diagram
        ind = ind + 1
    X = Point(X_x, X_y, X_label)
    diagram.points.append(X)

    tk = random.randint(1,5)
    diagram.lines.append(Line(A, midpt, label="", tickmarks=tk))
    diagram.lines.append(Line(B, midpt, label="", tickmarks=tk))
    bisector = Line(X, midpt, label="", infinite= True)
    diagram.lines.append(bisector)
    # diagram.entities.append(f'Point({midpt.label}) : midpoint of Line({A.label}{B.label})')
    # diagram.entities.append(f'Point({X.label}) on the perpendicular bisector of {A.label}{B.label}')
    diagram.entities.append(('on_bline', [A.label, B.label, X.label, midpt.label]))
    diagram.perpendiculars.append((bisector, l, midpt))

    return diagram



def on_circle(diagram: Diagram):
    # Construct X such that  OX = OA
    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)

    ind = 0
    while True:
        O , A = random.sample(diagram.points, 2)
        #Construct X such that  OX = OA

        vector = (A.x - O.x, A.y - O.y)
        radius = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
        if radius > 200:
            break
        if ind > 30:
            return diagram
        ind +=1
    angle_OA = np.arctan2(vector[1], vector[0])
    angle_OX = angle_OA + random.uniform(np.pi/6, 11*np.pi/6)

    X_x = O.x + radius * np.cos(angle_OX)
    X_y = O.y + radius * np.sin(angle_OX)

    X_label = label_point(diagram)

    X = Point(X_x, X_y, X_label)
    diagram.points.append(X)
    diagram.circles.append(Circle(O, radius, f'{O.label},{radius}'))
    if not line_already_in(diagram, O, A):
        diagram.lines.append(Line(O, A, label=""))
    # diagram.entities.append(f'Point({X.label}) on Circle({O.label},{radius}) with radius {O.label}{A.label}')

    if random.choice([True, False]):
        x,y, length = add_radius(O.x, O.y, radius)
        diagram.lines.append(Line(O, Point(x, y, ""), label=length, dotted=True))
        diagram.entities.append(('on_circle_with_r', [O.label, A.label, X.label,length]))
    else : diagram.entities.append(('on_circle', [O.label, A.label, X.label]))


    return diagram


def on_line(diagram: Diagram):
    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)
    A, B = random.sample(diagram.points, 2)
    vector = (B.x - A.x, B.y - A.y)
    X_label = label_point(diagram)
    if random.choice([True, False]):
        is_infinite = True
        scale1, scale2 = 1.2 , 4
    else:
        is_infinite = False
        scale1, scale2 = 0.2, 0.8

    diagram.lines.append(Line(A, B, label="",infinite=is_infinite))
    ind = 0
    while True:
        scale = random.uniform(scale1, scale2)
        X_x = A.x + scale * vector[0]
        X_y = A.y + scale * vector[1]
        if assert_coord_in_range(X_x, X_y):
            break
        if ind > 30:
            return diagram
        ind = ind + 1
    X = Point(X_x, X_y, X_label)
    diagram.points.append(X)
    diagram.entities.append(('on_line', [A.label, B.label, X.label]))

    return diagram

def on_pline(diagram: Diagram):
    #"X = on_pline(A, B, C)": { "Description": "Construct X such that XA is parallel to BC" },
    while len(diagram.lines) < 1:
        diagram = add_free_line(diagram)

    while len(diagram.points) < 3:
        diagram = add_free_point(diagram)

    l = random.choice(diagram.lines)
    A,B = l.point1, l.point2
    ind = 0
    while True:
        C = random.choice(diagram.points)
        if C != A and C != B:
            break
        if ind > 30:
            print(f"failed because length of points: {len(diagram.points)}")
            return diagram
        ind = ind + 1

    vector = (B.x - A.x, B.y - A.y)
    ind = 0
    while True:
        scale = random.uniform(-3, 3)
        X_x = C.x + scale * vector[0]
        X_y = C.y + scale * vector[1]
        if assert_coord_in_range(X_x, X_y):
            break
        if ind>30:
            return diagram
        ind = ind + 1
    X_label = label_point(diagram)

    X = Point(X_x, X_y, X_label)
    diagram.points.append(X)

    # tk = random.randint(1,5)
    tk = 0
    diagram.lines.append(Line(A, B, label="", tickmarks=tk))
    diagram.lines.append(Line(C, X, label="", tickmarks=tk))

    # diagram.entities.append(f'Line({C.label}{X.label}) parallel to Line({A.label}{B.label})')
    diagram.entities.append(('on_pline', [A.label, B.label, C.label, X.label]))
    return diagram

def r_triangle(diagram):
    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)

    A, B = random.sample(diagram.points, 2)
    perp_vector = (B.y - A.y, A.x - B.x)
    ind = 0

    scale = random.uniform(-4, 4)
    C_x = A.x + scale * perp_vector[0]
    C_y = A.y + scale * perp_vector[1]
    C_label = label_point(diagram)


    C = Point(C_x, C_y, C_label)
    diagram.points.append(C)

    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])
    # diagram.entities.append(f'Right Triangle({A.label}{B.label}{C.label})')
    diagram.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
    diagram.entities.append(('r_triangle', [A.label, B.label, C.label]))
    return diagram


def rectangle(diagram):
    new_labels = []
    if random.choice([True, False]):
        while True:
            A, B = Point(random_coord(), random_coord(), label_point(diagram)), Point(random_coord(), random_coord(), label_point(diagram))
            if A.label != B.label:
                diagram.points.extend([A, B])
                new_labels = [A.label, B.label]
                break
    else:
        while len(diagram.points) < 2:
            diagram = add_free_point(diagram)
        A, B = random.sample(diagram.points, 2)
    vector = (B.x - A.x, B.y - A.y)
    perp_vector = (vector[1], -vector[0])

    scale = random.uniform(-4, 4)
    C_x = B.x + scale * perp_vector[0]
    C_y = B.y + scale * perp_vector[1]
    D_x = A.x + scale * perp_vector[0]
    D_y = A.y + scale * perp_vector[1]
    ind = 0
    while True:
        C_label = label_point(diagram)
        D_label = label_point(diagram)
        if C_label != D_label and C_label not in new_labels:
            break
        if ind > 30:
            return diagram
        ind += 1

    C = Point(C_x, C_y, C_label)
    D = Point(D_x, D_y, D_label)
    diagram.points.extend([C, D])

    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
    diagram.entities.append(('rectangle', [A.label, B.label, C.label, D.label]))
    diagram.perpendiculars.append((Line(A, B, label=""), Line(A, D, label=""), A))
    diagram.perpendiculars.append((Line(B, C, label=""), Line(B, A, label=""), B))
    diagram.perpendiculars.append((Line(C, D, label=""), Line(C, B, label=""), C))
    diagram.perpendiculars.append((Line(D, A, label=""), Line(D, C, label=""), D))

    return diagram


def reflect(diagram):
    #"X = reflect(A, B, C)": { "Description": "Construct X as the reflection of A about BC" },
    while len(diagram.points) < 3:
        diagram = add_free_point(diagram)

    A, B, C = random.sample(diagram.points, 3)
    vec_BC = (C.x - B.x, C.y - B.y)
    vec_BA = (A.x - B.x, A.y - B.y)
    foot_x = B.x + np.dot(vec_BC, vec_BA) / np.dot(vec_BC, vec_BC) * vec_BC[0]
    foot_y = B.y + np.dot(vec_BC, vec_BA) / np.dot(vec_BC, vec_BC) * vec_BC[1]
    X_x = A.x + 2 * (foot_x - A.x)
    X_y = A.y + 2 * (foot_y - A.y)

    

    X_label = label_point(diagram)
    X = Point(X_x, X_y, X_label)
    diagram.points.append(X)
    diagram.lines.extend([Line(B, C, label="", infinite=True)])
    if random.choice([True, False]):
        diagram.lines.append(Line(A, X, label="", dotted=True))
        diagram.perpendiculars.append((Line(A, X, ''), Line(B, C, ''), Point((A.x + X.x) / 2, (A.y + X.y) / 2, '')))
    diagram.entities.append(('reflect', [A.label, B.label, C.label, X.label]))
    return diagram

def trapezoid(diagram : Diagram): #Construct a trapezoid such that BA // CD
    while len(diagram.points) < 2:
        diagram = add_free_point(diagram)
    A , B = random.sample(diagram.points, 2)
    vector = (B.x - A.x, B.y - A.y)

    C_x, C_y = random_coord(), random_coord()
    C_label = label_point(diagram)

    C = Point(C_x, C_y, C_label)

    ind  = 0

    scale = random.uniform(0.5, 3)
    D_x = C.x + scale * vector[0]
    D_y = C.y + scale * vector[1]
    while True:
        D_label = label_point(diagram)
        if D_label != C_label:
            break
        if ind > 30:
            return diagram
        ind += 1

    D = Point(D_x, D_y, D_label)
    if random.choice([True, False]):
        tk = 0
    else:
        # tk = random.randint(1,5)
        tk = 0
    diagram.points.extend([C, D])
    diagram.lines.extend([Line(A, B, label="", tickmarks=tk), Line(B, D, label=""), Line(C, D, label="", tickmarks=tk), Line(C, A, label="")])
    diagram.entities.append(('trapezoid', [A.label, B.label, C.label, D.label]))
    return diagram

def trisegment(d):
    while len(d.lines) < 1:
        d = add_free_line(d)
    l = random.choice(d.lines)
    A, B = l.point1, l.point2
    vector = (B.x - A.x, B.y - A.y)
    p1_x, p1_y = A.x + vector[0] / 3, A.y + vector[1] / 3
    p2_x, p2_y = A.x + 2 * vector[0] / 3, A.y + 2 * vector[1] / 3

    p1_label = label_point(d)
    while True:
        p2_label = label_point(d)
        if p2_label != p1_label:
            break
    p1 = Point(p1_x, p1_y, p1_label)
    p2 = Point(p2_x, p2_y, p2_label)
    d.points.extend([p1, p2])

    if random.choice([True, False, False]):
        tk = random.randint(1,5)
        l_label = ""
    else: 
        tk = 0
        l_label = label_line(d)
    d.lines.extend([Line(A, p1, label=l_label, tickmarks=tk), Line(p1, p2, label=l_label, tickmarks=tk), Line(p2, B, label=l_label, tickmarks=tk)])
    # d.entities.append(f'Line({A.label}{p1.label}) = Line({p1.label}{p2.label}) = Line({p2.label}{B.label})')
    d.entities.append(('trisegment', [A.label, B.label, p1.label, p2.label]))
    return d

def cc_tangent(d):

    while len(d.points) < 1:
        d = add_free_point(d)

    c1_center = random.choice(d.points)
    c1_radius = random.uniform(100, 400)

    angle = random_angle()
    distance = random.uniform(2, 5) * c1_radius
    x = c1_center.x + distance * np.cos(angle)
    y = c1_center.y + distance * np.sin(angle)


    angle0 = np.arctan((y - c1_center.y) / (x - c1_center.x))
    if x < c1_center.x:
        angle0 += np.pi
    angle = np.arccos(c1_radius / distance)

    p1_x, p1_y = c1_center.x + c1_radius * np.cos(angle + angle0), c1_center.y + c1_radius * np.sin(angle + angle0)
    p2_x, p2_y = c1_center.x + c1_radius * np.cos(-angle + angle0), c1_center.y + c1_radius * np.sin(-angle + angle0)

    ind = 0
    while True:
        label = label_point(d)
        p1_label = label + '1'
        p2_label = label + '2'
        P_label = label_point(d)
        if P_label != label:
            break
        if ind > 30:
            return d
        ind += 1


    p1 = Point(p1_x, p1_y, p1_label)
    p2 = Point(p2_x, p2_y, p2_label)
    P = Point(x, y, P_label)
    vec_x, vec_y = c1_center.x-x, c1_center.y-y
    ind = 0

    while True:
        scale = random. uniform(0.5, 1)
        x1, y1 = x + scale * vec_x, y + scale * vec_y
        rad_1 = c1_radius * scale
        if np.linalg.norm([x1 - c1_center.x, y1 - c1_center.y]) > c1_radius + rad_1:
            break
        if ind > 30:
            return d
        ind += 1

    c2_center = Point(x1, y1, label_point(d))
    c2 = Circle(c2_center, rad_1, '')
    t1_x, t1_y = scale * (p1_x - x) + x, scale * (p1_y - y) + y
    t2_x, t2_y = scale * (p2_x - x) + x, scale * (p2_y - y) + y
    t_label = label_point(d)
    t1 = Point(t1_x, t1_y, t_label + '1')
    t2 = Point(t2_x, t2_y, t_label + '2')

    d.points.extend([t1,t2])
    d.points.append(c2.center)
    d.circles.append(c2)
    d.circles.append(Circle(c1_center, c1_radius, f"{c1_center.label, c1_radius}"))


    d.points.extend([p1, p2, P])
    d.lines.extend([Line(p1, P, label=""), Line(p2, P, label=""), ])

    # d.entities.append(
    # print(f'Line({p1.label}{P.label}) and Line({p2.label}{P.label}) are tangent to Circle({c1_center.label},{c1_radius}) and Circle({c2_center.label},{rad_1})')
    if random.choice([True, False]):
        x,y, length = add_radius(c1_center.x, c1_center.y, c1_radius)
        x2, y2, length2 = add_radius(c2_center.x, c2_center.y, rad_1)
        d.lines.extend([Line(c1_center, Point(x,y,""), label=f"{length}", dotted=True), Line(c2_center, Point(x2,y2,""), label=f"{length}", dotted=True)])
        d.entities.append(('cc_tangent_with_r',
                           [c1_center.label, length, c2_center.label, length2, p1.label, p2.label, P.label,
                            t1.label, t2.label]))
    else: d.entities.append(('cc_tangent', [c1_center.label , c2_center.label, p1.label, p2.label, P.label, t1.label, t2.label]))

    return d


def eqangle2(d): #construct X such that BAX = XCB, on_aline
    while len(d.points) < 3:
        d = add_free_point(d)

    #Get A, B, C
    points = random.sample(d.points, 3)
    center = Point(sum([p.x for p in points]) / 3, sum([p.y for p in points]) / 3 , "")
    if random.choice([0,1]) < 1:
        A, B, C = sort_clockwise(points, center)
    else:
        B, C, A = sort_clockwise(points, center)
    
    vec_BC = (C.x - B.x, C.y - B.y)

    #Construct X
    Xx, Xy = A.x + vec_BC[0], A.y + vec_BC[1]
    X_label = label_point(d)
    X = Point(Xx, Xy, X_label)

    #add objects to d
    d.points.append(X)

    line_AB, line_CB, line_CX, line_AX = Line(A, B, label=""), Line(C, B, label=""), Line(C, X, label=""), Line(A, X, label="")
    d.lines.extend([line_AB, line_CB, line_CX, line_AX])

    angle_label = label_line_nonempty(d)
    min_length = min([np.linalg.norm([B.x - A.x, B.y - A.y]), np.linalg.norm([C.x - B.x, C.y - B.y]), np.linalg.norm([C.x - X.x, C.y - X.y]), np.linalg.norm([A.x - X.x, A.y - X.y])])

    vec_AB, vec_AX = np.array([B.x - A.x, B.y - A.y]), np.array([X.x - A.x, X.y - A.y])
    angle_BAX = np.arccos(np.dot(vec_AB, vec_AX) / (np.linalg.norm(vec_AB) * np.linalg.norm(vec_AX)))

    ang_BAX = (line_AB, angle_BAX, A, 'black', angle_label, min_length)

    vec_CX, vec_CB = np.array([X.x - C.x, X.y - C.y]), np.array([B.x - C.x, B.y - C.y])
    angle_XCB = np.arccos(np.dot(vec_CX, vec_CB) / (np.linalg.norm(vec_CX) * np.linalg.norm(vec_CB)))
    ang_XCB = (line_CX, angle_XCB, C, 'black', angle_label, min_length)
    d.angles.extend([ang_BAX, ang_XCB])

    d.entities.append(('eqangle2', [A.label, B.label, C.label, X.label, angle_label]))

    return d



#########################################################################################################
#########################################################################################################
########################################################################################################################
#New Rules (no caption)
########################################################################################################################
#########################################################################################################
#########################################################################################################

def intersection(d):
    return d

def colinear(d):
    while len(d.points) < 2:
        d = add_free_point(d)

    A, B = random.sample(d.points, 2)
    vec_AB = np.array([B.x - A.x, B.y - A.y])
    if random.choice([True, False]):
        scale = random.uniform(1.15, 3)
    else : scale = random.uniform(-2, -0.15)

    C_x = A.x + scale * vec_AB[0]
    C_y = A.y + scale * vec_AB[1]

    C_label = label_point(d)

    C = Point(C_x, C_y, C_label)
    d.points.append(C)
    d.lines.append(Line(A, B, label="", infinite=True))
    d.lines.append(Line(B, C, label="", infinite=True))

    d.entities.append(('colinear', [A.label, B.label, C.label]))
    return d


def eqangle3(d): #Construct X such that AXB = CDE
    while len(d.points) < 5:
        d = add_free_point(d)


    A, B, C, D, E = random.sample(d.points, 5)

    E, C = sort_clockwise([C, E], D)

    vec_DE = np.array([E.x - D.x, E.y - D.y])
    vec_DC = np.array([C.x - D.x, C.y - D.y])
    vec_AB = np.array([B.x - A.x, B.y - A.y])
    angle_DE = np.arctan2(vec_DE[1], vec_DE[0])
    angle_DC = np.arctan2(vec_DC[1], vec_DC[0])
    angle_CDE = angle_DC - angle_DE

    if angle_CDE < np.pi/12 or angle_CDE > np.pi*11/12:
        return d

    scale = random.uniform(0.5, 1.5)
    vec_rot =rotate_vector(vec_AB, angle_CDE)
    X_x = A.x + scale * vec_rot[0]
    X_y = A.y + scale * vec_rot[1]

    X_label = label_point(d)
    X = Point(X_x, X_y, X_label)
    d.points.append(X)
    d.lines.extend([Line(A, B, label=""), Line(C, D, label=""), Line(D, E, label=""), Line(A, X, label="")])

    angle_label = label_line_nonempty(d)
    angle_length = min([np.linalg.norm([A.x - X.x, A.y - X.y]), np.linalg.norm([B.x - A.x, B.y - A.y]), np.linalg.norm([C.x - D.x, C.y - D.y]), np.linalg.norm([E.x - D.x, E.y - D.y])])
    d.angles.append((Line(A, B, ""), angle_CDE, A, 'black', angle_label, angle_length))
    d.angles.append((Line(D, E, ""), angle_CDE, D, 'black', angle_label, angle_length))
    d.entities.append(('eqangle3', [A.label, B.label, C.label, D.label, E.label, X.label]))

    return d

def on_dia(d): #Construct X such that AX perp BX
    while len (d.points) < 2:
        d = add_free_point(d)

    A, B = random.sample(d.points, 2)
    M_x, M_y = (A.x + B.x) / 2, (A.y + B.y) / 2
    radius = np.linalg.norm([A.x - B.x, A.y - B.y]) / 2

    ind = 0
    while True:
        angle = random.uniform(0, 2 * np.pi)
        X_x = M_x + radius * np.cos(angle)
        X_y = M_y + radius * np.sin(angle)

        vec_AX = np.array([X_x - A.x, X_y - A.y])
        vec_AB = np.array([B.x - A.x, B.y - A.y])
        cosine = np.dot(vec_AX, vec_AB) / (np.linalg.norm(vec_AX) * np.linalg.norm(vec_AB))

        if cosine < 0.9 and cosine > 0.1:
            break
        if ind > 100:
            return d
        ind += 1


    X_label = label_point(d)

    X = Point(X_x, X_y, X_label)
    d.points.append(X)
    d.lines.append(Line(A, X, label=""))
    d.lines.append(Line(B, X, label=""))
    d.entities.append(('on_dia', [A.label, B.label, X.label]))
    d.perpendiculars.append((Line(A, X, ''), Line(B, X, ''), X))

    return d

def trisect(d): #Construct X,Y on line AC such that trisects angle ABC
    while len(d.points) < 3:
        d = add_free_point(d)

    P1, B, P2 = random.sample(d.points, 3)
    A, C = sort_clockwise([P1, P2], B)
    vec_BA = np.array([A.x - B.x, A.y - B.y])
    vec_BC = np.array([C.x - B.x, C.y - B.y])
    angle_BA = np.arctan2(vec_BA[1], vec_BA[0])
    angle_BC = np.arctan2(vec_BC[1], vec_BC[0])
    angle_ABC = angle_BC - angle_BA

    angle1 = angle_BA + angle_ABC / 3
    angle2 = angle_BA + 2 * angle_ABC / 3
    length = max([np.linalg.norm([A.x - B.x, A.y - B.y]), np.linalg.norm([C.x - B.x, C.y - B.y])])
    if angle_ABC < np.pi/6 or angle_ABC > np.pi*8/9 or length < 200:
        return d


    X_x = B.x + length * np.cos(angle1)
    X_y = B.y + length * np.sin(angle1)
    Y_x = B.x + length * np.cos(angle2)
    Y_y = B.y + length * np.sin(angle2)

    Xx, Xy = intersection_of_two_lines(Line(A, C, ""), Line(B, Point(X_x, X_y, ""), ""))
    Yx, Yy = intersection_of_two_lines(Line(A, C, ""), Line(B, Point(Y_x, Y_y, ""), ""))

    new_labels = []
    while len(new_labels) < 2:
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)

    X = Point(Xx, Xy, new_labels[0])
    Y = Point(Yx, Yy, new_labels[1])

    d.points.extend([X, Y])
    d.lines.extend([Line(A, B, ""), Line(B, C, ""), Line(A, C, ""), Line(B, X, ""), Line(B, Y, "")])
    d.entities.append(('trisect', [A.label, B.label, C.label, X.label, Y.label]))

    angle_label = label_line_nonempty(d)
    angle_length = min( [np.linalg.norm([Y.x - B.x, Y.y - B.y]), np.linalg.norm([X.x - B.x, X.y - B.y])])
    d.angles.append((Line(B, Y, ""), angle_ABC / 3, B, 'black', angle_label, angle_length))
    d.angles.append((Line(B, X, ""), angle_ABC / 3, B, 'black', angle_label, angle_length))
    d.angles.append((Line(B, A, ""), angle_ABC / 3, B, 'black', angle_label, angle_length))

    return d

def one_line_one_circle(d): #1L1C, construct circle center I such that touches line AC and BC and circle O,A at X, Y, Z
    while len(d.circles) < 1:
        d = add_free_circle(d)

    while len(d.points) < 2:
        d = add_free_point(d)

    ind = 0
    while True:
        c = random.choice(d.circles)
        O = c.center
        r = c.radius

        #Get A
        rand_angle = random.uniform(0, 2*np.pi)
        A_x = O.x + r * np.cos(rand_angle)
        A_y = O.y + r * np.sin(rand_angle)
        A = Point(A_x, A_y, label_point(d))

        new_labels = [A.label]

        
        C = random.choice(d.points)

        vec_AC = np.array([C.x - A.x, C.y - A.y])
        perp_AC = np.array([vec_AC[1], -vec_AC[0]])
        tmp_x, tmp_y = O.x + perp_AC[0], O.y + perp_AC[1]
        foot_x, foot_y = intersection_of_two_lines(Line(O, Point(tmp_x, tmp_y, ""), ""), Line(A, C, ""))

        I_radius = np.linalg.norm([foot_x - O.x, foot_y - O.y])

        if I_radius > 100 or r > 100:
            break
        
        if ind > 100:
            return d 
        
        if ind // 10 == 5:
            d = add_free_circle(d)
        ind += 1
        

    I_x = O.x + (r + I_radius) * vec_AC[0] / np.linalg.norm(vec_AC)
    I_y = O.y + (r + I_radius) * vec_AC[1] / np.linalg.norm(vec_AC)

    I_label = label_point(d)
    while I_label == new_labels[0]:
        I_label = label_point(d)
    I = Point(I_x, I_y, I_label)

    d.points.extend([A, I])
    d.circles.append(Circle(I, I_radius, ""))
    d.lines.append(Line(A, C, "", infinite=True))
    d.entities.append(('one_line_one_circle', [O.label, A.label, C.label, I.label]))
    return d

def two_lines_one_circle(d): #2L1C, construct circle center I such that touches line AC and BC and circle O,A at X, Y, Z
    while len(d.circles) < 1:
        d = add_free_circle(d)

    while len(d.points) < 2:
        d = add_free_point(d)

    ind = 0
    while True:
        c = random.choice(d.circles)
        O = c.center
        r = c.radius

        new_labels = []
        while len(new_labels) < 6:
            label = label_point(d)
            if label not in new_labels:
                new_labels.append(label)

        #Get A
        rand_angle = random.uniform(0, 2*np.pi)
        A_x = O.x + r * np.cos(rand_angle)
        A_y = O.y + r * np.sin(rand_angle)
        A = Point(A_x, A_y, new_labels[0])



        C = random.choice(d.points)

        vec_AC = np.array([C.x - A.x, C.y - A.y])
        perp_AC = np.array([vec_AC[1], -vec_AC[0]])
        tmp_x, tmp_y = O.x + perp_AC[0], O.y + perp_AC[1]
        foot_x, foot_y = intersection_of_two_lines(Line(O, Point(tmp_x, tmp_y, ""), ""), Line(A, C, ""))



        I_radius = np.linalg.norm([foot_x - O.x, foot_y - O.y])

        if I_radius > 100 or r > 100:
            break

        if ind > 100:
            return d 
        if ind // 10 == 5:
            d = add_free_circle(d)
        ind += 1 
            

    I_x = O.x + (r + I_radius) * vec_AC[0] / np.linalg.norm(vec_AC)
    I_y = O.y + (r + I_radius) * vec_AC[1] / np.linalg.norm(vec_AC)

    I_label = new_labels[4]
    I = Point(I_x, I_y, I_label)


    #Now choose the second line
    vec_OI = np.array([I.x - O.x, I.y - O.y])
    Xx, Xy = foot_x + vec_OI[0], foot_y + vec_OI[1]
    X = Point(Xx, Xy, new_labels[1])

    vec_CI = np.array([I.x - C.x, I.y - C.y])
    vec_CX = np.array([X.x - C.x, X.y - C.y])
    angle_CI = np.arctan2(vec_CI[1], vec_CI[0])
    angle_CX = np.arctan2(vec_CX[1], vec_CX[0])
    angle_ICX = angle_CX - angle_CI

    rot_vec = rotate_vector(vec_CI, -angle_ICX)
    Yx, Yy = C.x + rot_vec[0], C.y + rot_vec[1]
    Y = Point(Yx, Yy, new_labels[2])

    Zx, Zy = O.x + vec_OI[0] * r/(r + I_radius), O.y + vec_OI[1] * r/(r + I_radius)
    Z = Point(Zx, Zy, new_labels[3])


    scale_B = random.uniform(1.2, 2)
    Bx, By = C.x + scale_B * rot_vec[0], C.y + scale_B * rot_vec[1]
    B = Point(Bx, By, new_labels[5])


    d.points.extend([A, I, X, Y, Z, B])
    d.circles.append(Circle(I, I_radius, ""))
    d.lines.append(Line(A, C, "", infinite=True))
    d.lines.append(Line(C, B, "", infinite=True))
    d.entities.append(('two_lines_one_circle', [O.label, A.label, C.label, I.label, X.label, Y.label, Z.label, B.label]))
    return d

def shift(d): #Construct X such that CX = BA and BX = CA
    while len(d.points) < 3:
        d = add_free_point(d)

    # Get A, B, C
    points = random.sample(d.points, 3)
    center = Point(sum([p.x for p in points]) / 3, sum([p.y for p in points]) / 3, "")
    A, B, C = sort_clockwise(points, center)
    vec_BC = (C.x - B.x, C.y - B.y)

    # Construct X
    Xx, Xy = A.x + vec_BC[0], A.y + vec_BC[1]
    X_label = label_point(d)
    X = Point(Xx, Xy, X_label)

    # add objects to d
    d.points.append(X)

    if random.choice([True, False]):
        tk1 = 0
        tk2 = 0

        ind = 0
        while True:
            label1, label2 = label_line_nonempty(d), label_line_nonempty(d)
            if label1 != label2:
                break
            if ind > 30:
                return d
            ind +=1

        name_line = True

    else:
        tk1, tk2 = random.sample ([1, 2, 3, 4, 5], 2)
        label1, label2 = "", ""
        name_line = False



    line_AB, line_CB, line_CX, line_AX = Line(A, B, label=label1, tickmarks=tk1), Line(C, B, label=label2, tickmarks=tk2), Line(C, X, label=label1, tickmarks=tk1), Line(A, X,
                                                                                                                label=label2, tickmarks=tk2)
    d.lines.extend([line_AB, line_CB, line_CX, line_AX])


    if name_line:
        d.entities.append(('shift1', [A.label, B.label, C.label, X.label, label1, label2]))
    else:
        d.entities.append(('shift2', [A.label, B.label, C.label, X.label]))


    return d



def rotate_angle(d): #angle: construct X such that BAX = alpha
    while len(d.lines) < 1:
        d = add_free_line(d)

    l = random.choice(d.lines)
    A, B = l.point1, l.point2

    vec_AB = np.array([B.x - A.x, B.y - A.y])
    angle = random.uniform(np.pi/9, np.pi)
    length = random_length()
    vecAX = rotate_vector(vec_AB, angle)
    X_x = A.x + vecAX[0]
    X_y = A.y + vecAX[1]

    X = Point(X_x, X_y, label_point(d))
    d.points.append(X)
    d.lines.append(Line(A, X, label=""))
    if random.choice([True, False]):
        angle_label = label_line_nonempty(d)
    else:
        angle_label = f"{int(np.degrees(angle))}°"
    d.angles.append((Line(A, B, label=""), angle, A, 'black', angle_label, length))

    d.entities.append(('rotate_angle', [A.label, B.label, X.label, angle_label]))
    return d


def risos(d): #construct right isoceles triangle ABC starting from one line 
    if random.choice([True, False]):
        while len(d.lines) < 1:
            d = add_free_line(d)
        l = random.choice(d.lines)
        A, B = l.point1, l.point2
        new_labels = [A.label, B.label]
        length = np.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
    else:
        new_labels = []
        while len(new_labels) < 2:
            label = label_point(d)
            if label not in new_labels:
                new_labels.append(label)

        A = Point(random_coord(), random_coord(), new_labels[0])
        angle = random.uniform(0, np.pi*2)
        length = random_length()
        B_x = A.x + length * np.cos(angle)
        B_y = A.y + length * np.sin(angle)
        B = Point(B_x, B_y, new_labels[1])
        d.points.extend([A, B])
        d.lines.append(Line(A, B, label=""))

    vector = (B.x - A.x, B.y - A.y)
    perp_vector = (vector[1], -vector[0])
    C_x, C_y = A.x + perp_vector[0], A.y + perp_vector[1]
    C = Point(C_x, C_y, label_point(d))
    d.points.append(C)
    d.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])
    d.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
    d.entities.append(('risos', [A.label, B.label, C.label]))

    return d

def r_trapezoid(d): #Construct right trapezoid ABCD
    if random.choice([True, False]):
        # Use existing lines
        while len(d.lines) < 1:
            d = add_free_line(d)
        l = random.choice(d.lines)
        A, B = l.point1, l.point2
        new_labels = [A.label, B.label]

    else: #use new points
        new_labels = []
        while len(new_labels) < 2:
            label = label_point(d)
            if label not in new_labels:
                new_labels.append(label)

        A = Point(random_coord(), random_coord(), new_labels[0])
        angle = random.uniform(0, np.pi*2)
        length = random_length()
        B_x = A.x + length * np.cos(angle)
        B_y = A.y + length * np.sin(angle)
        B = Point(B_x, B_y, new_labels[1])
        d.points.extend([A, B])
        d.lines.append(Line(A, B, label=""))

    vector = (B.x - A.x, B.y - A.y)
    perp_vector = (vector[1], -vector[0])
    if random.choice([True, False]):
        scale1 = random.uniform(0.5, 4)
        scale2 = random.uniform(0.5, 4)
    else:
        scale1 = random.uniform(-4, -0.5)
        scale2 = random.uniform(-4, -0.5)



    C_x, C_y = A.x + scale1 * perp_vector[0], A.y + scale1 * perp_vector[1]
    D_x, D_y = B.x + scale2 * perp_vector[0], B.y + scale2 * perp_vector[1]

    while len(new_labels) < 4 :
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)

    C = Point(C_x, C_y, new_labels[2])
    D = Point(D_x, D_y, new_labels[3])
    d.points.extend([C, D])
    d.lines.extend([Line(B, D, label=""), Line(D, C, label=""), Line(C, A, label="")])

    d.perpendiculars.append((Line(A, B, label=""), Line(B, D, label=""), B))
    d.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))

    d.entities.append(('r_trapezoid', [A.label, B.label, D.label, C.label]))

    return d



def orthocenter(d): #Construct X as the orthocenter of ABC
    while len(d.points) < 3:
        d = add_free_point(d)

    ind = 0
    while True:
        A, B, C = random.sample(d.points, 3)
        lengths = [(B.x - C.x) ** 2 + (B.y - C.y) ** 2, (A.x - C.x) ** 2 + (A.y - C.y) ** 2, (A.x - B.x) ** 2 + (A.y - B.y) ** 2]

        vec_AB = np.array([B.x - A.x, B.y - A.y])
        vec_BC = np.array([C.x - B.x, C.y - B.y])
        vec_CA = np.array([A.x - C.x, A.y - C.y])
        cos_A = np.dot(vec_CA, -vec_BC) / (np.linalg.norm(vec_CA) * np.linalg.norm(vec_BC))
        cos_B = np.dot(vec_AB, -vec_CA) / (np.linalg.norm(vec_AB) * np.linalg.norm(vec_CA))
        cos_C = np.dot(vec_BC, -vec_AB) / (np.linalg.norm(vec_BC) * np.linalg.norm(vec_AB))

        if cos_A > 0 and cos_B > 0 and cos_C > 0:
            if max(lengths) > 10000 and min(lengths) * 4 > max(lengths):
                break


        
            
        if ind > 100:
            return d 
        if ind // 10 == 5:
            d = add_free_point(d)
        ind +=1 
        

    

    
    new_labels = []
    while len(new_labels) < 4:
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)

    m1 = (B.x - C.x) / (C.y - B.y)
    m2 = (A.x - C.x) / (C.y - A.y)

    x_H = (m1 * A.x - m2 * B.x + B.y - A.y) / (m1 - m2)
    y_H = m1 * (x_H - A.x) + A.y

    H = Point(x_H, y_H, new_labels[0])
    d.points.append(H)

    d.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])


    #foot from A to BC
    a = B.y - C.y
    b = C.x - B.x
    c = B.x * C.y - C.x * B.y

    x = A.x - a*(a*A.x + b*A.y + c) / (a ** 2 + b ** 2)
    y = A.y - b*(a*A.x + b*A.y + c)/ (a ** 2 + b ** 2)

    foot_A = Point(x, y, new_labels[1])

    #foot from B to AC
    a = C.y - A.y
    b = A.x - C.x
    c = C.x * A.y - A.x * C.y

    x = B.x - a * (a * B.x + b * B.y + c) / (a ** 2 + b ** 2)
    y = B.y - b * (a * B.x + b * B.y + c) / (a ** 2 + b ** 2)

    foot_B = Point(x, y, new_labels[2])

    #foot from C to AB
    a = A.y - B.y
    b = B.x - A.x
    c = A.x * B.y - B.x * A.y

    x = C.x - a * (a * C.x + b * C.y + c) / (a ** 2 + b ** 2)
    y = C.y - b * (a * C.x + b * C.y + c) / (a ** 2 + b ** 2)

    foot_C = Point(x, y, new_labels[3])

    dotted = random.choice([True, False])
    d.lines.extend([Line(A, foot_A, label="", dotted=dotted), Line(B, foot_B, label="", dotted=dotted), Line(C, foot_C, label="", dotted=dotted)])
    d.perpendiculars.append((Line(A, foot_A, label=""), Line(B, C, label=""), foot_A))
    d.perpendiculars.append((Line(B, foot_B, label=""), Line(A, C, label=""), foot_B))
    d.perpendiculars.append((Line(C, foot_C, label=""), Line(A, B, label=""), foot_C))

    d.entities.append(('orthocenter', [A.label, B.label, C.label, H.label]))
    return d

def triangle(d): #Construct triangle ABC
    if random.choice([True, False]):
        # Use existing line (if none, make one)
        if len(d.points) < 1:
            d = add_free_point(d)
        if len(d.lines) < 1:
            d = add_free_point_with_line(d)

        l = random.choice(d.lines)
        A, B = l.point1, l.point2


        C = Point(random_coord(), random_coord(), label_point(d))
        d.points.append(C)
        d.lines.append(Line(A, C, label=""))
        d.lines.append(Line(C, B, label=""))

        d.entities.append(('triangle', [A.label, B.label, C.label]))

    else:
        Ax, Ay, Bx, By, Cx, Cy = random_coord(), random_coord(), random_coord(), random_coord(), random_coord(), random_coord()
        new_labels = []
        while True:
            label = label_point(d)
            if label not in new_labels:
                new_labels.append(label)
                if len(new_labels) == 3:
                    break

        A = Point(Ax, Ay, new_labels[0])
        B = Point(Bx, By, new_labels[1])
        C = Point(Cx, Cy, new_labels[2])

        d.points.extend([A, B, C])
        d.lines.extend([
            Line(A, B, label=""),
            Line(B, C, label=""),
            Line(C, A, label="")
        ])
        d.entities.append(('triangle', [A.label, B.label, C.label]))

    return d





def add_line_label(d):
    if len(d.lines) < 1:
        d = add_line(d)
    l = random.choice(d.lines)

    if l.label == "":
        new_label = random.choice(small_letters_nonempty.candidates)
        while new_label not in [line.label for line in d.lines]:
            new_label = random.choice(small_letters_nonempty.candidates)


        # remove l from d.lines
        d.lines = [line for line in d.lines if line != l]
        l.label = new_label
        d.lines.append(l)
        d.entities.append(('line_label', [f"{l.point1.label}{l.point2.label}", l.label]))
    return d

def isos(d): #construct A,B,C such that AB = AC
    while len(d.points) < 2:
        d = add_free_point(d)

    A, B = random.sample(d.points, 2)
    len_AB = np.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
    angle = random.uniform(0, np.pi*2)
    C = Point(A.x + len_AB * np.cos(angle),  A.y + len_AB * np.sin(angle), label_point(d))
    d.points.append(C)
    d.lines.append(Line(A, B, label=""))
    d.lines.append(Line(A, C, label=""))
    d.entities.append(('isos', [A.label, B.label, C.label]))

    return d


def excenter(d): #Construct X as the excenter of ABC
    while len(d.points) < 3:
        d = add_free_point(d)

    A, B, C = random.sample(d.points, 3)

    a = np.sqrt((B.x - C.x) ** 2 + (B.y - C.y) ** 2)
    b = np.sqrt((A.x - C.x) ** 2 + (A.y - C.y) ** 2)
    c = np.sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)
    s = (a + b + c) / 2

    if min(a, b, c) < 50:
        return d
    if min(a, b, c) * 4 < max(a, b, c):
        return

    r = np.sqrt( (s - b) * (s - c) * s / (s - a) )

    if r < 50:
        return d

    # Calculate the excenter
    x = (-a * A.x + b * B.x + c * C.x) / (-a + b + c)
    y = (-a * A.y + b * B.y + c * C.y) / (-a + b + c)
    X = Point(x, y, label_point(d))

    d.points.append(X)
    d.circles.append(Circle(X, r, ""))
    d.lines.append(Line(A, B, label="", infinite=True))
    d.lines.append(Line(B, C, label=""))
    d.lines.append(Line(C, A, label="", infinite=True))
    d.entities.append(('excenter', [A.label, B.label, C.label, X.label]))
    return d

def midpointcircle(d): #Construct ABC as midpoint of PQR, and X as the circumcenter of ABC
    while len(d.points) < 3:
        d = add_free_point(d)

    P, Q, R = random.sample(d.points, 3)
    lengths_squares = [(P.x - Q.x) ** 2 + (P.y - Q.y) ** 2, (Q.x - R.x) ** 2 + (Q.y - R.y) ** 2, (R.x - P.x) ** 2 + (R.y - P.y) ** 2]
    if max(lengths_squares) < 10000:
        return d

    new_labels = []
    while len(new_labels) < 4:
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)

    A = Point((P.x + Q.x) / 2, (P.y + Q.y) / 2, new_labels[0])
    B = Point((Q.x + R.x) / 2, (Q.y + R.y) / 2, new_labels[1])
    C = Point((R.x + P.x) / 2, (R.y + P.y) / 2, new_labels[2])

    midpoint_AB = ((A.x + B.x) / 2, (A.y + B.y) / 2)
    midpoint_BC = ((B.x + C.x) / 2, (B.y + C.y) / 2)

    perp_bisector_AB = None
    perp_bisector_BC = None

    # Check for vertical lines and set perpendicular directions
    if A.x == B.x:  # AB is vertical
        perp_bisector_AB = "horizontal"
        c_AB = midpoint_AB[0]  # x-coordinate for the vertical bisector
    else:
        slope_AB = (B.y - A.y) / (B.x - A.x)
        perp_slope_AB = -1 / slope_AB
        c_AB = midpoint_AB[1] - perp_slope_AB * midpoint_AB[0]

    if B.x == C.x:  # BC is vertical
        perp_bisector_BC = "horizontal"
        c_BC = midpoint_BC[0]  # x-coordinate for the vertical bisector
    else:
        slope_BC = (C.y - B.y) / (C.x - B.x)
        perp_slope_BC = -1 / slope_BC
        c_BC = midpoint_BC[1] - perp_slope_BC * midpoint_BC[0]

    # Calculate the intersection of the perpendicular bisectors
    if perp_bisector_AB == "horizontal" and perp_bisector_BC != "horizontal":
        Xx = c_AB
        Xy = perp_slope_BC * Xx + c_BC
    elif perp_bisector_BC == "horizontal" and perp_bisector_AB != "horizontal":
        Xx = c_BC
        Xy = perp_slope_AB * Xx + c_AB
    elif perp_bisector_AB != "horizontal" and perp_bisector_BC != "horizontal":
        Xx = (c_BC - c_AB) / (perp_slope_AB - perp_slope_BC)
        Xy = perp_slope_AB * Xx + c_AB

    radius = ((Xx - A.x) ** 2 + (Xy - A.y) ** 2) ** 0.5
    if max(lengths_squares)  < radius**2:
        return d


    X = Point(Xx, Xy, new_labels[3]) # Circumcenter

    d.points.extend([A, B, C, X])
    d.circles.append(Circle(X, radius, ""))



    if random.choice([True, False]):
        tks = [0] * 3
    else:
        tks = random.sample(range(1, 5), 3)

    if random.choice([True, False]):
        d.lines.append(Line(A, B, label=""))
        d.lines.append(Line(B, C, label=""))
        d.lines.append(Line(C, A, label=""))

    d.lines.extend([Line(P, A , label="", tickmarks=tks[0]), Line(A, Q, label="", tickmarks=tks[0]),
                    Line(Q, B, label="", tickmarks=tks[1]), Line(B, R, label="", tickmarks=tks[1]),
                    Line(R, C, label="", tickmarks=tks[2]), Line(C, P, label="", tickmarks=tks[2])])


    d.entities.append(('midpointcircle', [P.label, Q.label, R.label, A.label, B.label, C.label, X.label]))


    return d

def on_tline(d): #Construct X such that XA is orthogonal to BC
    while len(d.points) < 3:
        d = add_free_point(d)

    A, B, C = random.sample(d.points, 3)
    vec_BC = np.array([C.x - B.x, C.y - B.y])
    if random.choice([True, False]):
        vec_XA = rotate_vector(vec_BC, np.pi/2)
    else:
        vec_XA = rotate_vector(vec_BC, -np.pi/2)

    scale = random.uniform(0.5, 1.5)
    X_x, X_y = A.x + scale * vec_XA[0], A.y + scale * vec_XA[1]
    X_label = label_point(d)

    X = Point(X_x, X_y, X_label)
    d.points.append(X)
    d.lines.extend([Line(B, C, label=""), Line(A, X, label="")])

    d.entities.append(('on_tline', [A.label, B.label, C.label, X.label]))
    return d


def centroid(d): #Construct X as the centroid of ABC
    while len(d.points) < 3:
        d = add_free_point(d)

    A, B, C = random.sample(d.points, 3)
    x = (A.x + B.x + C.x) / 3
    y = (A.y + B.y + C.y) / 3

    vec_AX = np.array([x - A.x, y - A.y])
    ax, ay = A.x + 1.5 * vec_AX[0], A.y + 1.5* vec_AX[1]

    vec_BX = np.array([x - B.x, y - B.y])
    bx, by = B.x + 1.5 * vec_BX[0], B.y + 1.5* vec_BX[1]

    vec_CX = np.array([x - C.x, y - C.y])
    cx, cy = C.x + 1.5 * vec_CX[0], C.y + 1.5* vec_CX[1]

    X = Point(x, y, label_point(d))
    d.points.append(X)
    d.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])
    d.lines.extend([Line(A, Point(ax, ay, ""), label="", dotted=True), Line(B, Point(bx, by, ""), label="", dotted=True), Line(C, Point(cx, cy, ""), label="", dotted=True)])
    d.entities.append(('centroid', [A.label, B.label, C.label, X.label]))
    return d




def midpoint(diagram: Diagram, line = None):
    A, B = random.sample(diagram.points, 2)

    X_x = (A.x + B.x) / 2
    X_y = (A.y + B.y) / 2

    X_label = label_point(diagram)

    X = Point(X_x, X_y, X_label)

    if random.choice([True, False]):
        tk = 0
    else:
        tk = random.randint(1,5)
    diagram.lines.append(Line(A, X, label="", tickmarks=tk))
    diagram.lines.append(Line(X, B, label="", tickmarks=tk))


    diagram.points.append(X)
    diagram.entities.append(('midpoint', [A.label, B.label, X.label]))
    return diagram

def rotate90(d): #Construct X such that X is the 90 degree rotation of A about O
    while len (d.points) < 2:
        d = add_free_point(d)
    A, O = random.sample(d.points, 2)

    vec_OA = np.array([A.x - O.x, A.y - O.y])
    vec_OX = rotate_vector(vec_OA, np.pi/2)

    X_x, X_y = O.x + vec_OX[0], O.y + vec_OX[1]
    X_label = label_point(d)
    X = Point(X_x, X_y, X_label)
    d.points.append(X)

    d.lines.append(Line(A, O, label=""))
    d.lines.append(Line(O, X, label=""))
    d.perpendiculars.append((Line(A, O, ''), Line(O, X, ''), O))
    d.entities.append(('rotate90', [A.label, O.label, X.label]))

    return d




def on_circle2(d): #Construct X on circle O
    while len(d.circles) < 1:
        d = add_free_circle(d)
    c = random.choice(d.circles)


    is_on = random.choice(["p", "l", "t", "sq"])

    center = c.center
    radius = c.radius
    answer, object = "", ""

    if is_on == "p": # a point is on the circle
        angle = random.uniform(0, 2*np.pi)
        x = center.x + radius * np.cos(angle)
        y = center.y + radius * np.sin(angle)
        X = Point(x, y, label_point(d))
        d.points.append(X)

        answer = random.choice([f"point {X.label}", f"Point {X.label}", f"{X.label}"])
        object = "point"

    elif is_on == "l": # a line is on the circle
        angle1, angle2 = random.uniform(0, 2*np.pi), random.uniform(np.pi/6, 11*np.pi/6)
        x1, y1 = center.x + radius * np.cos(angle1), center.y + radius * np.sin(angle1)
        x2, y2 = center.x + radius * np.cos(angle1 + angle2), center.y + radius * np.sin(angle1 + angle2)

        if random.choice([True, False]):
            ind = 0
            while True:
                label1, label2 = label_point(d), label_point(d)
                if label1 != label2:
                    break
                if ind > 100:
                    return d
                ind+=1
            d.points.extend([Point(x1, y1, label1), Point(x2, y2, label2)])
            d.lines.append(Line(Point(x1, y1, label1), Point(x2, y2, label2), label=""))
            answer = random.choice([f"line {label1}{label2}", f"Line {label1}{label2}", f"{label1}{label2}"])
        else:
            label1 = label_line_nonempty(d)
            d.lines.append(Line(Point(x1, y1, ""), Point(x2, y2, ""), label=label1))
            answer = random.choice([f"line {label1}", f"Line {label1}", f"{label1}"])

        object = "line"

    elif is_on == "t": # a triangle is on the circle
        while True:
            angle1, angle2, angle3 = random.uniform(0, 2*np.pi), random.uniform(np.pi/6, 11*np.pi/6), random.uniform(np.pi/6, 11*np.pi/6)
            if angle2 + angle3 < 2*np.pi*0.9:
                break


        x1, y1 = center.x + radius * np.cos(angle1), center.y + radius * np.sin(angle1)
        x2, y2 = center.x + radius * np.cos(angle1 + angle2), center.y + radius * np.sin(angle1 + angle2)
        x3, y3 = center.x + radius * np.cos(angle1 + angle2 + angle3), center.y + radius * np.sin(angle1 + angle2 + angle3)

        ind = 0
        new_labels = []
        while len(new_labels)<3:
            label = label_point(d)
            if label not in new_labels:
                new_labels.append(label)
        d.points.extend([Point(x1, y1, new_labels[0]), Point(x2, y2, new_labels[1]), Point(x3, y3, new_labels[2])])
        d.lines.extend([Line(Point(x1, y1, new_labels[0]), Point(x2, y2, new_labels[1]), ""), Line(Point(x2, y2, new_labels[1]), Point(x3, y3, new_labels[2]), ""), Line(Point(x3, y3, new_labels[2]), Point(x1, y1, new_labels[0]), "")])
        answer = random.choice([f"triangle {new_labels[0]}{new_labels[1]}{new_labels[2]}", f"Triangle {new_labels[0]}{new_labels[1]}{new_labels[2]}", f"{new_labels[0]}{new_labels[1]}{new_labels[2]}"])

        object = "triangle"

    elif is_on == "sq": # a square is on the circle
        angle0 = random.uniform(0, 2*np.pi)
        while True:
            angle1, angle2, angle3 = random.uniform(np.pi/6, 11*np.pi/6), random.uniform(np.pi/6, 11*np.pi/6), random.uniform(np.pi/6, 11*np.pi/6)
            if angle1 + angle2 + angle3 < 2*np.pi*0.9:
                break
        x1, y1 = center.x + radius * np.cos(angle0), center.y + radius * np.sin(angle0)
        x2, y2 = center.x + radius * np.cos(angle0 + angle1), center.y + radius * np.sin(angle0 + angle1)
        x3, y3 = center.x + radius * np.cos(angle0 + angle1 + angle2), center.y + radius * np.sin(angle0 + angle1 + angle2)
        x4, y4 = center.x + radius * np.cos(angle0 + angle1 + angle2 + angle3), center.y + radius * np.sin(angle0 + angle1 + angle2 + angle3)

        ind = 0
        new_labels = []
        while len(new_labels)<4:
            label = label_point(d)
            if label not in new_labels:
                new_labels.append(label)
        d.points.extend([Point(x1, y1, new_labels[0]), Point(x2, y2, new_labels[1]), Point(x3, y3, new_labels[2]), Point(x4, y4, new_labels[3])])
        d.lines.extend([Line(Point(x1, y1, new_labels[0]), Point(x2, y2, new_labels[1]), ""), Line(Point(x2, y2, new_labels[1]), Point(x3, y3, new_labels[2]), ""), Line(Point(x3, y3, new_labels[2]), Point(x4, y4, new_labels[3]), ""), Line(Point(x4, y4, new_labels[3]), Point(x1, y1, new_labels[0]), "")])
        answer = random.choice([f"square {new_labels[0]}{new_labels[1]}{new_labels[2]}{new_labels[3]}", f"Square {new_labels[0]}{new_labels[1]}{new_labels[2]}{new_labels[3]}", f"{new_labels[0]}{new_labels[1]}{new_labels[2]}{new_labels[3]}"])

        object = "square"


    d.entities.append(('on_circle2', [c.center.label, c.radius, object, answer]))

    return d


def inter_ll(d):
    #Intersection of two lines
    while len(d.lines) < 2:
        d = add_free_line(d)
    l1, l2 = random.sample(d.lines, 2)
    x,y = intersection_of_two_lines(l1, l2)
    label = label_point(d)
    P = Point(x, y, label)

    # Assert that the two line segment crosses.
    if not (min(l1.point1.x, l1.point2.x) <= P.x <= max(l1.point1.x, l1.point2.x) and min(l2.point1.y, l2.point2.y) <= P.y <= max(l2.point1.y, l2.point2.y)):
        return d

    label1 = l1.point1.label
    label2 = l1.point2.label
    label3 = l2.point1.label
    label4 = l2.point2.label

    #Assert that they are not blank
    if label1 == "" or label2 == "" or label3 == "" or label4 == "":
        return d

    d.points.append(P)
    d.entities.append(('inter_ll', [f"{label1}{label2}",f"{label3}{label4}", P.label]))

    return d

def cc_tangent_one(d):
    while len(d.circles) < 1:
        d = add_free_circle(d)
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius
    ind = 0
    while True:
        x, y = random_coord(), random_coord()
        length = np.linalg.norm([x - c1_center.x, y - c1_center.y])
        if length > 3 * c1_radius:
            break
        if ind > 100:
            return d
        ind += 1

    angle0 = np.arctan((y - c1_center.y) / (x - c1_center.x))
    if x < c1_center.x:
        angle0 += np.pi
    angle = np.arccos(c1_radius / length)

    p1_x, p1_y = c1_center.x + c1_radius * np.cos(angle + angle0), c1_center.y + c1_radius * np.sin(angle + angle0)

    new_labels = []
    while True:
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)
            if len(new_labels) == 5:
                break


    label = new_labels[0]
    P_label = new_labels[1]
    p1_label = new_labels[2]
    c2_label = new_labels[3]

    p1 = Point(p1_x, p1_y, p1_label)

    P = Point(x, y, P_label)

    vec_x, vec_y = c1_center.x - x, c1_center.y - y
    ind = 0
    while True:
        scale = random. uniform(0.2, 1)
        x1, y1 = x + scale * vec_x, y + scale * vec_y
        rad_1 = c1_radius * scale
        if np.linalg.norm([x1 - c1_center.x, y1 - c1_center.y]) > c1_radius + rad_1:
            break
        if ind > 100:
            return d
        ind += 1
    c2_center = Point(x1, y1, c2_label)
    c2 = Circle(c2_center, rad_1, '')
    t1_x, t1_y = scale * (p1_x - x) + x, scale * (p1_y - y) + y

    t_label = new_labels[4]
    t1 = Point(t1_x, t1_y, t_label)

    d.points.extend([t1])
    d.points.append(c2.center)
    d.circles.append(c2)

    d.points.extend([p1, P])
    d.lines.extend([Line(p1, P, label="") ])
    d.entities.append(('cc_tangent_one', [c1_center.label, f'{c1_radius}', c2_center.label, f'{rad_1}', p1.label, P.label]))
    return d

def intersect_cl(d): #Line intersecting a circle at two points
    while len(d.circles) < 1:
        d = add_free_circle(d)
    c = random.choice(d.circles)
    center = c.center
    radius = c.radius

    ang0 = random_angle()
    ang1 = random.uniform(np.pi/4, 7*np.pi/4)

    x0, y0 = center.x + radius * np.cos(ang0), center.y + radius * np.sin(ang0)
    x1, y1 = center.x + radius * np.cos(ang1+ang0), center.y + radius * np.sin(ang1+ang0)
    vec= (x1 - x0, y1 - y0)


    scale0, scale1 = random.uniform(-5, -0.2), random.uniform(1.2, 5)
    X0, Y0 = x0 + scale0 * vec[0], y0 + scale0 * vec[1]
    X1, Y1 = x0 + scale1 * vec[0], y0 + scale1 * vec[1]

    p0_label = label_point(d)
    ind = 0

    while True:
        p1_label = label_point(d)
        if p1_label != p0_label:
            break
        if ind > 10:
            return d
        ind += 1
    ind = 0
    while True:
        P0_label = label_point(d)
        if P0_label != p0_label and P0_label != p1_label:
            break
        if ind > 10:
            return d
        ind += 1
    ind = 0
    while True:
        P1_label = label_point(d)
        if P1_label != p0_label and P1_label != p1_label and P1_label != P0_label:
            break
        if ind > 10:
            return d
        ind += 1

    p0 = Point(x0, y0, p0_label)
    p1 = Point(x1, y1, p1_label)
    P0 = Point(X0, Y0, P0_label)
    P1 = Point(X1, Y1, P1_label)
    d.points.extend([p0, p1, P0, P1])
    d.lines.extend([Line(P0, P1, label="")])
    d.entities.append(('intersect_cl', [center.label, f'{radius}', p0.label, p1.label, P0.label, P1.label]))
    return d



def intersect_cc(d):
    while len(d.circles) < 1:
        d = add_free_circle(d)
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius

    c2_radius = random.uniform(0.75, 3) * c1_radius
    ind = 0
    while True:
        angle = random_angle()
        scale = random.uniform(1.25, 5)
        x, y = c1_center.x + scale * c1_radius * np.cos(angle), c1_center.y + scale * c1_radius * np.sin(angle)
        if np.linalg.norm([x - c1_center.x, y - c1_center.y]) < c1_radius + c2_radius:
            break
        if ind > 30:
            return d
        ind += 1

    c2_center = Point(x, y, label_point(d))
    c2 = Circle(c2_center, c2_radius, '')

    length = np.linalg.norm([c2_center.x - c1_center.x, c2_center.y - c1_center.y])
    angle0 = np.arctan((c2_center.y - c1_center.y) / (c2_center.x - c1_center.x))
    if c2_center.x < c1_center.x:
        angle0 += np.pi
    angle = np.arccos((c1_radius ** 2 + length ** 2 - c2_radius ** 2) / (2 * c1_radius * length))

    p1_x, p1_y = c1_center.x + c1_radius * np.cos(angle + angle0), c1_center.y + c1_radius * np.sin(angle + angle0)
    p2_x, p2_y = c1_center.x + c1_radius * np.cos(-angle + angle0), c1_center.y + c1_radius * np.sin(-angle + angle0)

    c2_center = Point(x, y, label_point(d))
    while True:
        p1_label = label_point(d)
        p2_label = label_point(d)
        if p2_label != p1_label and p1_label != c2_center.label and p2_label != c2_center.label:
            break

    p1 = Point(p1_x, p1_y, p1_label)
    p2 = Point(p2_x, p2_y, p2_label)

    d.points.extend([p1, p2, c2_center])
    d.circles.append(c2)
    d.entities.append(('intersect_cc', [c1_center.label, f'{c1_radius}', c2_center.label, f'{c2_radius}', p1.label, p2.label]))
    return d



def touches_cc(d):
    while len(d.circles) < 1:
        d = add_free_circle(d)
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius



    angle = random_angle()
    c2_radius = random.uniform(0.75, 3) * c1_radius
    scale = c1_radius + c2_radius
    x, y = c1_center.x + scale *  np.cos(angle), c1_center.y + scale * np.sin(angle)



    c2_label = label_point(d)
    c2_center = Point(x, y, c2_label)
    c2 = Circle(c2_center, c2_radius, '')

    while True:
        label = label_point(d)
        if label != c2_label:
            break
    touchpoint = Point(c1_center.x + c1_radius * np.cos(angle), c1_center.y + c1_radius * np.sin(angle), label)
    d.points.append(touchpoint)
    d.points.append(c2_center)
    d.circles.append(c2)
    # d.entities.append(f'Circle({c1_center.label},{c1_radius}) touches Circle({c2_center.label},{c2_radius}) at {touchpoint.label}')
    d.entities.append(('touches_cc', [c1_center.label, f'{c1_radius}', c2_center.label, f'{c2_radius}', touchpoint.label]))
    return d

def touches_cc2(d):
    while len(d.circles) < 1:
        d = add_free_circle(d)
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius

    ind = 0

    angle = random_angle()
    c2_radius = random.uniform(0.25, 0.75) * c1_radius
    scale = c1_radius - c2_radius
    x, y = c1_center.x + scale * np.cos(angle), c1_center.y + scale * np.sin(angle)


    c2_label = label_point(d)
    c2_center = Point(x, y, c2_label)
    c2 = Circle(c2_center, c2_radius, '')

    while True:
        label = label_point(d)
        if label != c2_label:
            break
    touchpoint = Point(c1_center.x + c1_radius * np.cos(angle), c1_center.y + c1_radius * np.sin(angle), label)
    d.points.append(touchpoint)
    d.points.append(c2_center)
    d.circles.append(c2)
    d.entities.append(('touches_cc2', [c1_center.label, f'{c1_radius}', c2_center.label, f'{c2_radius}', touchpoint.label]))
    return d


def touches_clc(d):
    while len(d.circles) < 1:
        d = add_free_circle(d)
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius

    angle = random_angle()
    c2_radius = random.uniform(0.75, 3) * c1_radius
    scale = c1_radius + c2_radius
    x, y = c1_center.x + scale * np.cos(angle), c1_center.y + scale * np.sin(angle)


    c2_label = label_point(d)
    c2_center = Point(x, y, c2_label)
    c2 = Circle(c2_center, c2_radius, '')

    while True:
        label = label_point(d)
        if label != c2_label:
            break
    touchpoint = Point(c1_center.x + c1_radius * np.cos(angle), c1_center.y + c1_radius * np.sin(angle), label)
    perp_vec = normalize((c1_center.y - touchpoint.y, touchpoint.x - c1_center.x))

    scale1 = random.uniform(50, 200)
    scale2 = random.uniform(50, 200)
    x1, y1 = touchpoint.x + scale1 * perp_vec[0], touchpoint.y + scale1 * perp_vec[1]
    x2, y2 = touchpoint.x - scale2 * perp_vec[0], touchpoint.y - scale2 * perp_vec[1]

    while True:
        label1 = label_point(d)
        label2 = label_point(d)
        if label1 != label2 and label1 != c2_label and label2 != c2_label and label1 != label and label2 != label:
            break

    p1 = Point(x1, y1, label1)
    p2 = Point(x2, y2, label2)
    d.points.extend([p1, p2, touchpoint, c2_center])
    d.circles.append(c2)
    d.lines.append(Line(p1, p2, label="",infinite=random.choice([True, False])))
    # d.entities.append(f'Circle({c1_center.label},{c1_radius}) touches Circle({c2_center.label},{c2_radius}) on Line({p1.label}{p2.label}) at {touchpoint.label}')
    d.entities.append(('touches_clc', [c1_center.label, f'{c1_radius}', c2_center.label, f'{c2_radius}', p1.label, p2.label, touchpoint.label]))
    return d

def touches_clc2(d):
    while True:
        A_x, A_y = random_coord(), random_coord()
        B_x, B_y = random_coord(), random_coord()
        if  dist((A_x,A_y),(B_x,B_y)) > 600:
            break
    A = Point(A_x,A_y, "")
    B = Point(B_x, B_y, "")
    vector = (B_x - A_x, B_y - A_y)
    perp_vec = normalize((vector[1], -vector[0]))

    scale1, scale2 = random.uniform(0.1, 0.4), random.uniform(0.6, 0.9)
    x1, y1 = A_x + scale1 * vector[0], A_y + scale1 * vector[1]
    x2, y2 = A_x + scale2 * vector[0], A_y + scale2 * vector[1]

    while True:
        label1 = label_point(d)
        label2 = label_point(d)
        if label1 != label2:
            break

    p1 = Point(x1, y1, label1)
    p2 = Point(x2, y2, label2)

    ind = 0

    c1_radius = random.uniform(100, 500)
    c2_radius = random.uniform(100, 500)
    c1_x, c1_y = x1 + c1_radius * perp_vec[0], y1 + c1_radius * perp_vec[1]
    c2_x, c2_y = x2 - c2_radius * perp_vec[0], y2 - c2_radius * perp_vec[1]

    while True:
        c1_label = label_point(d)
        c2_label = label_point(d)
        if c1_label != c2_label and c1_label != label1 and c1_label != label2 and c2_label != label1 and c2_label != label2:
            break

    c1_center = Point(c1_x, c1_y, c1_label)
    c2_center = Point(c2_x, c2_y, c2_label)
    c1 = Circle(c1_center, c1_radius, '')
    c2 = Circle(c2_center, c2_radius, '')

    d.points.extend([p1, p2, c1_center, c2_center])
    d.circles.extend([c1, c2])
    d.lines.append(Line(A,B , label=""))
    d.entities.append(('touches_clc2', [c1_center.label, f'{c1_radius}', c2_center.label, f'{c2_radius}', p1.label, p2.label]))
    return d

def rhombus(d):
    while len(d.points) < 2:
        d = add_free_point(d)

    A, B = random.sample(d.points, 2)
    vector = (B.x - A.x, B.y - A.y)
    if np.linalg.norm(vector) < 100:
        return d

    center_x,  center_y, center_label = (A.x+B.x)/2, (A.y+B.y)/2, label_point(d)

    perp_vec = (vector[1], -vector[0])



    scale = random.uniform(1/3, 3)
    C_x, C_y = center_x + scale * perp_vec[0], center_y + scale * perp_vec[1]
    D_x, D_y = center_x - scale * perp_vec[0], center_y - scale * perp_vec[1]


    ind = 0
    while True:

        C_label = label_point(d)
        D_label = label_point(d)
        if C_label != D_label and C_label != center_label and D_label != center_label:
            break
        if ind > 30:
            return d
        ind +=1
    C = Point(C_x, C_y, C_label)
    D = Point(D_x, D_y, D_label)
    center = Point(center_x, center_y, center_label)
    d.points.extend([center, C, D])

    tk = random.randint(1, 5)
    d.lines.extend([Line(A, C, label="", tickmarks=tk), Line(C, B, label="", tickmarks=tk),
                    Line(B, D, label="", tickmarks=tk), Line(A, D, label="", tickmarks=tk)])
    d.entities.append(('rhombus', [A.label, B.label, C.label, D.label, center.label]))
    if random_coord() > 500:
        d.lines.extend([Line(A, B, label="", dotted = True), Line(C, D, label="", dotted = True)])
        d.perpendiculars.append((Line(A, B, label=""), Line(D, C, label=""), center))

    return d


def convex_quad(d):
    # No / 1 / 2 parallel pairs in the quadrilateral

    # Choose the number of edges in the polygon
    num_edges = 4
    #Choose random number of parallel pairs for the polygon

    num_parallel_pairs = random.choice([0, 1, 2])

    polygon_points = random_convex_polygon(num_edges, num_parallel_pairs, 1000)
    if polygon_points is None:
        return d

    # edge_color, fill_color = random.choice(color_pairs.candidates)
    edge_color = "black"
    fill_color = "none"

    # if random.choice([True, False]):
    #     label = label_point(d)
    # else:
    #     label = ""

    new_labels = []
    while len(new_labels) < 4:
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)
            d.points.append(Point(polygon_points[len(new_labels)-1][0], polygon_points[len(new_labels)-1][1], label))


    d.polygons.append(polygon(polygon_points, label="", edge_color=edge_color, fill_color=fill_color))

    d.entities.append((f'convex_quad', [num_parallel_pairs] + new_labels))

    return d


def parabola(d):
    a = random.uniform(0, 0.1)
    b = int(random.uniform(200,800 ))
    c = int(random.uniform(200, 800))

    t= np.linspace(0, 1000, 1000)
    x0 = t
    y0 = a*(t-b)**2 + c

    angle = random_angle()
    x = (x0-500)*np.cos(angle) - (y0-500)*np.sin(angle) + 500
    y = (x0-500)*np.sin(angle) + (y0-500)*np.cos(angle) + 500

    pt_lbl =  label_point(d)
    d.curves.append(Curve(x, y, label=""))
    d.points.append(Point(b, c, pt_lbl))
    d.entities.append(('parabola', [pt_lbl]))
    return d

def incenter3(diagram: Diagram): #Circle O is an incenter of ABC with one touchpoint Z and raidus r.
    while len(diagram.points) < 3:
        d = add_free_point(diagram)

    ind = 0
    while True:
        # Randomly select three points A, B, and C
        A, B, C = random.sample(diagram.points, 3)

        length_AB = np.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
        length_BC = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)
        length_CA = np.sqrt((A.x - C.x) ** 2 + (A.y - C.y) ** 2)
        if length_AB > 200 and length_BC > 200 and length_CA > 200:
            break
        if ind > 30:
            return diagram
        ind+=1

    X_x = (length_BC * A.x + length_CA * B.x + length_AB * C.x) / (length_AB + length_BC + length_CA)
    X_y = (length_BC * A.y + length_CA * B.y + length_AB * C.y) / (length_AB + length_BC + length_CA)
    X_label = label_point(diagram)

    X = Point(X_x, X_y, X_label)

    # radius of the incircle
    s = (length_AB + length_BC + length_CA) / 2
    radius = (s * (s - length_AB) * (s - length_BC) * (s - length_CA)) ** 0.5 / s

    # Get touchpoints of the incircle
    AB = np.array([B.x - A.x, B.y - A.y])
    BC = np.array([C.x - B.x, C.y - B.y])
    CA = np.array([A.x - C.x, A.y - C.y])

    # Calculate the foots from X
    touch_AB_x = A.x + np.dot(AB, (X_x - A.x, X_y - A.y)) / np.dot(AB, AB) * AB[0]
    touch_AB_y = A.y + np.dot(AB, (X_x - A.x, X_y - A.y)) / np.dot(AB, AB) * AB[1]
    touch_BC_x = B.x + np.dot(BC, (X_x - B.x, X_y - B.y)) / np.dot(BC, BC) * BC[0]
    touch_BC_y = B.y + np.dot(BC, (X_x - B.x, X_y - B.y)) / np.dot(BC, BC) * BC[1]
    touch_CA_x = C.x + np.dot(CA, (X_x - C.x, X_y - C.y)) / np.dot(CA, CA) * CA[0]
    touch_CA_y = C.y + np.dot(CA, (X_x - C.x, X_y - C.y)) / np.dot(CA, CA) * CA[1]

    label_touch_BC = label_point(diagram)
    label_list = [label_touch_BC]
    ind = 0
    while True:
        label_touch_CA = label_point(diagram)
        if label_touch_CA != label_touch_BC:
            label_list.append(label_touch_CA)
            break
        if ind > 30:
            return diagram
        ind = ind + 1

    ind = 0
    while True:
        label_touch_AB = label_point(diagram)
        if label_touch_AB not in label_list:
            break
        if ind > 30:
            return diagram
        ind = ind + 1

    touch_BC = Point(touch_BC_x, touch_BC_y, label_touch_BC)
    touch_CA = Point(touch_CA_x, touch_CA_y, label_touch_CA)
    touch_AB = Point(touch_AB_x, touch_AB_y, label_touch_AB)


    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])

    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label}) : Incenter of {A.label}{B.label}{C.label}')
    #
    touchpoint = random.choice([touch_AB, touch_BC, touch_CA])
    radius_label = str(random_length())
    diagram.points.append(touchpoint)
    diagram.lines.append(Line(X, touchpoint, label=radius_label, dotted=True))

    diagram.circles.append(Circle(X, radius, f'Incenter Circle({X.label},{radius})'))

    diagram.entities.append(('incenter3',
                             [A.label, B.label, C.label, X.label, radius_label, touchpoint.label]))
    diagram.perpendiculars.append((Line(X, touchpoint, ''), Line(A, B, ''), touchpoint))

    return diagram


def semicircle(d):
    if random.choice([True, False]):
        x, y = random_coord(), random_coord()
        center = Point(x, y, label_point(d))
        d.points.append(center)
    else:
        while len(d.points) < 1 :
            d = add_free_point(d)
        center = random.choice(d.points)


    angle = np.pi

    radius = random.randint(150, 500)
    angle_0 = random_angle()
    start_point = Point(center.x + radius * np.cos(angle_0), center.y + radius * np.sin(angle_0), "")
    end_point = Point(center.x + radius * np.cos(angle_0 + angle), center.y + radius * np.sin(angle_0 + angle), "")

    #Draw the circular sector as curve with paramter t
    t = np.linspace(0, angle, 1000)
    x = center.x + radius * np.cos(t + angle_0)
    y = center.y + radius * np.sin(t + angle_0)

    if random.choice([True,False]):
        raidus_angle = random.uniform(angle_0, angle_0 + angle)
        ex = center.x + radius * np.cos(raidus_angle)
        ey = center.y + radius * np.sin(raidus_angle)
        length = f'{random_length()}'
        d.lines.append(Line(center, Point(ex, ey, ""), label=length, dotted=True))
        d.entities.append(('semicircle_with_radius', [center.label, length]))
        d.lines.append(Line(center, end_point, label=''))

    elif random.choice([True,False]):
        d.entities.append(('semicircle', [center.label]))
        d.lines.append(Line(center, end_point, label=''))
    else:
        length = f'{random_length()}'
        d.entities.append(('semicircle_with_radius', [center.label,length]))
        d.lines.append(Line(center, end_point, label=length))

    d.curves.append(Curve(x, y, label=""))
    d.points.extend([start_point, end_point])
    d.lines.extend([Line(center, start_point, label="")])
    # d.entities.append(f'Semi-circle with center {center.label} with radius {radius}')

    return d



def circular_sector(d):

    x, y = random_coord(), random_coord()
    radius = random.randint(150, 500)


    center = Point(x, y, label_point(d))
    angle = random.uniform(np.pi/6, np.pi/2)
    angle_0 = random_angle()

    angle_label = random.choice(angle_letters.candidates)
    angle_number = f"{int(math.degrees(angle))}°"
    label = random.choice([angle_label, angle_number])

    start_point = Point(center.x + radius * np.cos(angle_0), center.y + radius * np.sin(angle_0), "")
    end_point = Point(center.x + radius * np.cos(angle_0 + angle), center.y + radius * np.sin(angle_0 + angle), "")

    #Draw the circular sector as curve with paramter t
    t = np.linspace(0, angle, 1000)
    x = center.x + radius * np.cos(t + angle_0)
    y = center.y + radius * np.sin(t + angle_0)
    d.curves.append(Curve(x, y, label=""))


    if random.choice([True,False]):
        raidus_angle = random.uniform(angle_0, angle_0 + angle)
        x = center.x + radius * np.cos(raidus_angle)
        y = center.y + radius * np.sin(raidus_angle)
        length = f'{random_length()}'
        d.lines.append(Line(center, Point(x, y, ""), label=length, dotted=True))
        d.entities.append(('circular_sector_with_radius', [center.label, length, label]))
    else: d.entities.append(('circular_sector', [center.label, label]))



    #input :  line1, angle, intersection, color, ang_label, length
    d.angles.append((Line(center, start_point, ''), angle, center, 'black', label, radius))

    d.points.extend([center, start_point, end_point])
    d.lines.extend([Line(center, start_point, label=""), Line(center, end_point, label="")])
    # d.entities.append(f'Circular sector with center {center.label}, radius {radius} and angle {label}')


    return d


def l_in_c(d):
    while len(d.circles) < 1:
        d = add_free_circle(d)
    c = random.choice(d.circles)
    center = c.center
    radius = c.radius

    angle1 = random_angle()
    angle2 = random.uniform(angle1+np.pi/4, angle1 + np.pi*7/4)
    ratio1 = random.uniform(0.1, 0.9)
    ratio2 = random.uniform(0.1, 0.9)
    x1, y1 = center.x + radius * np.cos(angle1)*ratio1, center.y + radius * np.sin(angle1)*ratio1
    x2, y2 = center.x + radius * np.cos(angle2)*ratio2, center.y + radius * np.sin(angle2)*ratio2

    while True:
        label1 = label_point(d)
        label2 = label_point(d)
        if label1 != label2:
            break
    p1 = Point(x1, y1, label1)
    p2 = Point(x2, y2, label2)
    d.points.extend([p1, p2])
    d.lines.append(Line(p1, p2, label=""))
    d.entities.append(('l_in_c', [center.label, f'{radius}', p1.label, p2.label]))
    return d


def l_out_c(d):
    while len(d.circles)<1:
        d = add_free_circle(d)
    c = random.choice(d.circles)
    center = c.center
    radius = c.radius


    ind = 0
    while True:
        angle1 = random_angle()
        angle2 = random.uniform(np.pi / 6, angle1 + np.pi /3)
        ratio1 = random.uniform(2, 5)
        ratio2 = random.uniform(2, 5)
        x1, y1 = center.x + radius * np.cos(angle1+angle2)*ratio1, center.y + radius * np.sin(angle1+angle2)*ratio1
        x2, y2 = center.x + radius * np.cos(angle1-angle2)*ratio2, center.y + radius * np.sin(angle1-angle2)*ratio2
        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break
        if ind > 30:
            return d
        ind += 1

    ind=0
    while True:
        label1 = label_point(d)
        label2 = label_point(d)
        if label1 != label2:
            break
        if ind > 30:
            return d
        ind +=1
    p1 = Point(x1, y1, label1)
    p2 = Point(x2, y2, label2)
    d.points.extend([p1, p2])
    d.lines.append(Line(p1, p2, label=""))
    # d.entities.append(f'Line({p1.label}{p2.label}) outside Circle({center.label},{radius})')
    d.entities.append(('l_out_c', [center.label, f'{radius}', p1.label, p2.label]))
    return d

def ll_angle(d):

    interpt_x, interpt_y = random_coord(), random_coord()
    angle1 = random_angle()
    angle2 = random.uniform(angle1 + np.pi / 6, angle1 + np.pi /2)
    leng = [random.uniform(100,500) for _ in range(4)]
    x11, y11 = interpt_x + leng[0] * np.cos(angle1), interpt_y + leng[0] * np.sin(angle1)
    x12, y12 = interpt_x - leng[1] * np.cos(angle1), interpt_y - leng[1] * np.sin(angle1)
    x21, y21 = interpt_x + leng[2] * np.cos(angle2), interpt_y + leng[2] * np.sin(angle2)
    x22, y22 = interpt_x - leng[3] * np.cos(angle2), interpt_y - leng[3] * np.sin(angle2)


    angle_label = random.choice(small_letters_nonempty.candidates)
    angle_number = f"{int(math.degrees(angle1-angle2))}°" if angle1-angle2 >  0 else f"{int(math.degrees(angle2-angle1))}°"

    label = random.choice([angle_label, angle_number])

    new_labels = []
    while len(new_labels) <5:
        p_label = label_point(d)
        if p_label not in new_labels:
            new_labels.append(p_label)
    label11, label12, label21, label22, inter_label = new_labels


    p11, p12, p21, p22, interpt = Point(x11, y11, label11), Point(x12, y12, label12), Point(x21, y21, label21), Point(x22, y22, label22), Point(interpt_x, interpt_y, inter_label)
    d.points.extend([p11, p12, p21, p22, interpt ])
    d.lines.extend([Line(p11,p12, label=""), Line(p21,p22, label="")])
    # d.entities.append(f'Line({p11.label}{p12.label}) and Line({p21.label}{p22.label}) intersect with angle {label}')
    d.entities.append(('ll_angle', [p11.label, p12.label, p21.label, p22.label, interpt.label, label]))
    d.angles.append((Line(p11,p12, label=""), angle2-angle1, interpt, "black", label, min([((x11-x12)**2+(y11-y12)**2)**0.5,((x21-x22)**2+(y21-y22)**2)**0.5])))
    return d


def ccl1(d): # Two circles and one line with line ending at both of the circles
    while len(d.circles) < 1:
        d = add_free_circle(d)

    X = random.choice(d.circles)
    X_center = X.center
    X_radius = X.radius

    new_labels = [label_point(d)]
    x,y = random_coord(), random_coord()
    dist = ((x - X_center.x) ** 2 + (y - X_center.y) ** 2) ** 0.5

    ind = 0
    while dist < 500:
        x, y = random_coord(), random_coord()
        dist = ((x - X_center.x) ** 2 + (y - X_center.y) ** 2) ** 0.5

        if ind > 100:
            return d
        ind +=1
    Y_center = Point(x,y, new_labels[0])

    radius = random_length()


    Y = Circle(Y_center, radius, "")

    angle_A = random.uniform(0, 2*np.pi)
    Ax, Ay = X_center.x + X_radius * np.cos(angle_A), X_center.y + X_radius * np.sin(angle_A)


    angle_B = random.uniform(0, 2 * np.pi)
    Bx, By = x + radius * np.cos(angle_B), y + radius * np.sin(angle_B)

    while len(new_labels) <3 :
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)

    A = Point(Ax, Ay, new_labels[1])
    B = Point(Bx, By, new_labels[2])

    d.points.extend([Y_center,A,B])
    d.lines.append(Line(A,B,""))
    d.circles.extend([Y])
    d.entities.append(("ccl1", [X_center.label, Y.center.label, A.label, B.label]))
    return d

def ccl2(d): # Two circles and one line with line ending at only one of the circles
    while len(d.circles) < 1:
        d = add_free_circle(d)

    X = random.choice(d.circles)
    X_center = X.center
    X_radius = X.radius

    new_labels = [label_point(d)]
    x,y = random_coord(), random_coord()
    dist = ((x - X_center.x) ** 2 + (y - X_center.y) ** 2) ** 0.5

    ind = 0
    while dist < 500:
        x, y = random_coord(), random_coord()
        dist = ((x - X_center.x) ** 2 + (y - X_center.y) ** 2) ** 0.5

        if ind > 100:
            return d
        ind +=1
    Y_center = Point(x,y, new_labels[0])

    radius = X_radius * random.uniform(0.3, 2.5)


    Y = Circle(Y_center, radius, "")

    angle_A = random.uniform(0, 2*np.pi)
    Ax, Ay = X_center.x + X_radius * np.cos(angle_A), X_center.y + X_radius * np.sin(angle_A)


    angle_B = random.uniform(0, 2 * np.pi)
    if random.choice([True, False]):
        scale = random.uniform(1.1, 1.3)
    else:
        scale = random.uniform(0.5, 0.9)
    radius *= scale

    Bx, By = x + radius * np.cos(angle_B), y + radius * np.sin(angle_B)

    while len(new_labels) <3 :
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)

    A = Point(Ax, Ay, new_labels[1])
    B = Point(Bx, By, new_labels[2])

    d.points.extend([Y_center,A,B])
    d.lines.append(Line(A,B,""))
    d.circles.extend([Y])
    d.entities.append(("ccl2", [X_center.label, Y.center.label, A.label, B.label]))
    return d


def ccl3(d): # Two circles and one line with line ending at inside of two circles
    while len(d.circles) < 1:
        d = add_free_circle(d)

    X = random.choice(d.circles)
    X_center = X.center
    X_radius = X.radius

    new_labels = [label_point(d)]
    x,y = random_coord(), random_coord()
    dist = ((x - X_center.x) ** 2 + (y - X_center.y) ** 2) ** 0.5

    ind = 0
    while dist < 500:
        x, y = random_coord(), random_coord()
        dist = ((x - X_center.x) ** 2 + (y - X_center.y) ** 2) ** 0.5

        if ind > 100:
            return d
        ind +=1
    Y_center = Point(x,y, new_labels[0])

    radius = X_radius * random.uniform(0.3, 2.5)


    Y = Circle(Y_center, radius, "")

    angle_A = random.uniform(0, 2*np.pi)
    X_radius *= random.uniform(0.5,0.95)
    Ax, Ay = X_center.x + X_radius * np.cos(angle_A), X_center.y + X_radius * np.sin(angle_A)


    angle_B = random.uniform(0, 2 * np.pi)
    scale = random.uniform(0.5, 0.95)
    radius *= scale


    Bx, By = x + radius * np.cos(angle_B), y + radius * np.sin(angle_B)

    while len(new_labels) <3 :
        label = label_point(d)
        if label not in new_labels:
            new_labels.append(label)

    A = Point(Ax, Ay, new_labels[1])
    B = Point(Bx, By, new_labels[2])

    d.points.extend([Y_center,A,B])
    d.lines.append(Line(A,B,""))
    d.circles.extend([Y])
    d.entities.append(("ccl3", [X_center.label, Y.center.label, A.label, B.label]))
    return d



#two line segments share a same endpoint

#Three circles share  intersection
#Three circles are mutually disjoint





# Two circles and one line with line ending at neither of the circles

# Circle inscribed in a quadrilateral
# Circle inscribed in a parallelogram
# Circle inscribed in a rhombus
# Circle inscribed in a rectangle
