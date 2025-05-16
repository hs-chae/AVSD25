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
    return np.random.uniform(np.pi / 9, 17 / 9 * np.pi)


def random_acute():
    return np.random.uniform(np.pi / 9, 4 / 9 * np.pi)


def random_obtuse():
    return np.random.uniform(5 / 9 * np.pi, 8 / 9 * np.pi)


def rotate_vector(vector, angle):
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) @ np.array(vector)


def random_coord(start=10, end=990):
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
            raise ValueError(
                f'No possible label found with currently {len(diagram.points)} points of list : {[point.label for point in diagram.points]}')

        ind += 1


def label_line(diagram):
    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label == "" or (label not in [line.label for line in diagram.lines]):
            return label
        if ind > 200:
            raise ValueError(
                f'No possible label found with currently {len(diagram.lines)} lines of list : {[line.label for line in diagram.lines]}')
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
        self.usable_colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'yellow', 'grey']


def normalize(vector):
    (x, y) = vector
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
                ind += 1
                break

            

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
        assert assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                     center.y - radius)

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
        assert assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius,
                                                                                                     center.y - radius)

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


def length_19(d):
    #Among multiple square, triangle, circle, bar, find the tallest
    d.polygons = []
    d.filled_circles = []
    # Which is tallest / smallest among the circles/rectangles/triangles/bars

    answer_in = random.choice(['color', 'label'])
    target_type = random.choice(['smallest', 'tallest'])
     # 'circles', 'rectangles', 'triangles',
    object_counts = random.randint(2, 10)

    # Choose the answer and wrong index
    answer_index = random.randint(0, object_counts - 1)
    wrong_index = random.choice([i for i in range(object_counts) if i != answer_index])

    # Choose bottom height
    y_bot = random.uniform(10, 600)

    # Choose top heights
    y_tops = []
    radiuses = []

    for _ in range(object_counts - 1):
        y_top = random.uniform(y_bot + 100, 900)
        y_tops.append(y_top)
        radiuses.append((y_top - y_bot) / 2)

    if target_type == 'smallest':
        y_top_answer = random.uniform(y_bot + 50, min(y_tops) - 50)
        radius_answer = (y_top_answer - y_bot) / 2
    else:
        y_top_answer = random.uniform(max(y_tops) + 50, 990)
        radius_answer = (y_top_answer - y_bot) / 2

    ind = 0
    # Choose x coordinates
    while True:
        x_lefts = []
        x_rights = []
        x_peaks = []
        x_right = 0
        j = 0
        # Choose width
        width = random.uniform(50, 200)
        object_types = []
        for i in range(object_counts):
            object_type = random.choice(['circle', 'rectangle', 'triangle', 'bar'])
            object_types.append(object_type)
            if object_type == 'bar':

                x_left = random.uniform(x_right + 10, x_right + 200)
                x_right = x_left + width
                x_lefts.append(x_left)
                x_rights.append(x_right)

            elif object_type == 'rectangle':
                width = random.uniform(50, 300)
                x_left = random.uniform(x_right + 10, x_right + 200)
                x_right = x_left + width
                x_lefts.append(x_left)
                x_rights.append(x_right)

            elif object_type == 'triangle':
                width = random.uniform(50, 200)
                x_left = random.uniform(x_right + 10, x_right + 200)
                x_right = x_left + width
                x_lefts.append(x_left)
                x_rights.append(x_right)

                x_peaks.append(random.uniform(x_left, x_right))

            elif object_type == 'circle':
                x_left = random.uniform(x_right + 10, x_right + 200)
                if i == answer_index:
                    x_right = x_left + 2 * radius_answer
                else:
                    x_right = x_left + 2 * radiuses[j]
                    j += 1

                x_lefts.append(x_left)
                x_rights.append(x_right)

        if assert_coord_in_range(x_rights[-1], y_bot):
            break

        if ind > 100:
            return d
        ind += 1

    # Choose colors
    use_black_edge = random.choice([True, False])
    color_pair_list = random.sample(color_pairs.candidates, object_counts)

    # If answering in label, you must add label. Otherwise, randomly choose to add label or not
    if answer_in == 'label' or random.choice([True, False]):
        labels = random.sample(capitals.candidates, object_counts)
    else:
        labels = []

    i, j = 0, 0

    total_length = len(d.polygons) + len(d.filled_circles)
    while len(d.polygons) + len(d.filled_circles) < object_counts:
        total_length = len(d.polygons) + len(d.filled_circles)
        # print(f"color: {color_pair_list[len(d.polygons)]}")
        object_type = object_types[len(d.polygons) + len(d.filled_circles)]
        if object_type == 'bar':
            if total_length == answer_index:
                d.polygons.append(polygon([(x_lefts[total_length], y_bot), (x_rights[total_length], y_bot),
                                           (x_rights[total_length], y_top_answer),
                                           (x_lefts[total_length], y_top_answer)],
                                          '' if len(labels) == 0 else labels[total_length],
                                          edge_color='black' if use_black_edge else color_pair_list[total_length][0],
                                          fill_color=color_pair_list[total_length][1]))

            else:
                d.polygons.append(polygon([(x_lefts[total_length], y_bot), (x_rights[total_length], y_bot),
                                           (x_rights[total_length], y_tops[j]),
                                           (x_lefts[total_length], y_tops[j])],
                                          '' if len(labels) == 0 else labels[total_length],
                                          edge_color='black' if use_black_edge else color_pair_list[total_length][0],
                                          fill_color=color_pair_list[total_length][1]))
                j += 1

        elif object_type == 'rectangle':
            if total_length == answer_index:
                d.polygons.append(polygon([(x_lefts[total_length], y_bot), (x_rights[total_length], y_bot),
                                           (x_rights[total_length], y_top_answer),
                                           (x_lefts[total_length], y_top_answer)],
                                          '' if len(labels) == 0 else labels[total_length],
                                          edge_color='black' if use_black_edge else color_pair_list[total_length][0],
                                          fill_color=color_pair_list[total_length][1]))

            else:
                d.polygons.append(polygon([(x_lefts[total_length], y_bot), (x_rights[total_length], y_bot),
                                           (x_rights[total_length], y_tops[j]),
                                           (x_lefts[total_length], y_tops[j])],
                                          '' if len(labels) == 0 else labels[total_length],
                                          edge_color='black' if use_black_edge else color_pair_list[total_length][0],
                                          fill_color=color_pair_list[total_length][1]))
                j += 1

        elif object_type == 'triangle':
            if total_length == answer_index:
                d.polygons.append(polygon([(x_lefts[total_length], y_bot), (x_rights[total_length], y_bot),
                                           (x_peaks[total_length], y_top_answer)],
                                          '' if len(labels) == 0 else labels[total_length],
                                          edge_color='black' if use_black_edge else color_pair_list[total_length][0],
                                          fill_color=color_pair_list[total_length][1]))

            else:
                d.polygons.append(polygon([(x_lefts[total_length], y_bot), (x_rights[total_length], y_bot),
                                           (x_peaks[total_length], y_tops[j])],
                                          '' if len(labels) == 0 else labels[total_length],
                                          edge_color='black' if use_black_edge else color_pair_list[total_length][0],
                                          fill_color=color_pair_list[total_length][1]))
                j += 1

        elif object_type == 'circle':
            if total_length == answer_index:
                d.filled_circles.append(
                    filled_circle((x_lefts[total_length] + radius_answer, y_bot + radius_answer),
                                  radius_answer, '' if len(labels) == 0 else labels[total_length],
                                  edge_color='black' if use_black_edge else color_pair_list[total_length][0],
                                  fill_color=color_pair_list[total_length][1]))
            else:
                # print(f"answer index: {answer_index}, j: {j}, len(d.filled_circles): {len(d.filled_circles)}, len(radiuses): {len(radiuses)}, len(x_lefts): {len(x_lefts)}, len(x_rights): {len(x_rights)}, len(color_pair_list): {len(color_pair_list)}")
                d.filled_circles.append(
                    filled_circle((x_lefts[total_length] + radiuses[j], y_bot + radiuses[j]), radiuses[j],
                                  '' if len(labels) == 0 else labels[total_length],
                                  edge_color='black' if use_black_edge else color_pair_list[total_length][0],
                                  fill_color=color_pair_list[total_length][1]))
                j += 1

        # tmp.append((object_type), label)
    if answer_in == 'color':
        candidates = ""
        permuted_index = random.sample(range(object_counts), object_counts)
        for i in range(object_counts):
            candidates += color_pair_list[permuted_index[i]][1] + ', '
        candidates = candidates[:-2]
    else:
        candidates = ""
        permuted_index = random.sample(range(object_counts), object_counts)
        for i in range(object_counts):
            candidates += labels[permuted_index[i]] + ', '
        candidates = candidates[:-2]

    if answer_in == 'color':
        d.entities.append((f'length_19_color_{target_type}',
                           [object_types[answer_index], candidates, color_pair_list[answer_index][1],
                            color_pair_list[wrong_index][
                                1]]))  # , len(d.polygons), object_counts, color_pair_list, labels]))
    else:
        d.entities.append((f'length_19_label_{target_type}', [object_types[answer_index], candidates, labels[answer_index],
                                                              labels[
                                                                  wrong_index]]))  # , len(d.polygons), object_counts, color_pair_list, labels]))

    # target type : smallest, tallest
    # object type : circles, rectangles, triangles, bars
    # answer_in : color, label
    # answer_index + 1: index of the answer
    # color_pairs[answer_index][1] : color of the answer

    d.points = []
    d.lines = []
    d.circles = []

    if random.choice([True, False]):
        d.lines.append(
            Line(Point(0, y_bot - 2, ''), Point(1000, y_bot - 2, ''), '', color=random.choice(d.usable_colors)))

    return d


def width1(d):
    # Find widest or narrowest road

    #Choose the number of roads to draw
    num_roads = random.choice([2, 3, 4])

    #Choose the answer type
    answer_type = random.choice(['widest', 'narrowest'])
    answer_in = random.choice(['color', 'label'])

    if answer_in == "color":
        colors = random.sample(color_pairs.candidates, num_roads)
        if random.choice([True, False]):
            labels = [""] * num_roads
        else:
            labels = random.sample(small_letters_nonempty.candidates, num_roads)
    else :
        labels = random.sample(small_letters_nonempty.candidates, num_roads)
        if random.choice([True, False]):
            colors = random.sample(color_pairs.candidates, num_roads)
        else:
            color = random.choice(color_pairs.candidates)
            colors = [color] * num_roads


    #Choose the width of the roads
    widths = []
    if answer_type == 'widest':
        width_answer = random.uniform(200, 400)
        for i in range(num_roads):
            if i == 0:
                width = width_answer
            else:
                width = random.uniform(50, 0.9* width_answer)
            widths.append(width)
    else:
        width_answer = random.uniform(50, 150)
        for i in range(num_roads):
            if i == 0:
                width = width_answer
            else:
                width = random.uniform(1.1 * width_answer, 400)
            widths.append(width)


    #Choose heights of the roads
    heights = []
    for i in range(num_roads):
        heights.append(random.uniform(600, 990))



    permuted_index = random.sample(range(num_roads), num_roads)
    if random.choice([True, False]): #The roads are vertical
        x_lefts = []
        y_lefts = []
        x_rights = []
        y_rights = []

        x_right =  random.uniform(50, 200)
        # y_right = random.uniform(50, 200)
        for i in range(num_roads):
            x_left = x_right + random.uniform (50, 200)
            y_left = random.uniform(50, 200)

            x_right = x_left + widths[permuted_index[i]]
            y_right = y_left

            x_lefts.append(x_left)
            y_lefts.append(y_left)
            x_rights.append(x_right)
            y_rights.append(y_right)


        for i in range(num_roads):
            road_coordinates = [(x_lefts[permuted_index[i]], y_lefts[permuted_index[i]]), (x_rights[permuted_index[i]], y_rights[permuted_index[i]]),
                                (x_rights[permuted_index[i]],y_rights[permuted_index[i]] + heights[permuted_index[i]]), (x_lefts[permuted_index[i]],y_lefts[permuted_index[i]] + heights[permuted_index[i]])]
            d.polygons.append(polygon(road_coordinates, labels[permuted_index[i]], edge_color=colors[permuted_index[i]][0], fill_color=colors[permuted_index[i]][1]))



    else: #The roads are horizontal
        x_tops = []
        y_tops = []
        x_bottoms = []
        y_bottoms = []

        y_top =  random.uniform(50, 200)
        # y_right = random.uniform(50, 200)
        for i in range(num_roads):
            y_bottom = y_top + random.uniform (50, 200)
            x_top = random.uniform(50, 200)

            y_top = y_bottom + widths[permuted_index[i]]
            x_bottom = x_top

            x_tops.append(x_top)
            y_tops.append(y_top)
            x_bottoms.append(x_bottom)
            y_bottoms.append(y_bottom)

        for i in range(num_roads):
            road_coordinates = [(x_tops[permuted_index[i]], y_tops[permuted_index[i]]), (x_bottoms[permuted_index[i]], y_bottoms[permuted_index[i]]),
                                (x_bottoms[permuted_index[i]] + heights[permuted_index[i]],y_bottoms[permuted_index[i]]), (x_tops[permuted_index[i]] + heights[permuted_index[i]],y_tops[permuted_index[i]])]
            d.polygons.append(polygon(road_coordinates, labels[permuted_index[i]], edge_color=colors[permuted_index[i]][0], fill_color=colors[permuted_index[i]][1]))


    if answer_in == 'color':
        candidates = ""
        for i in range(num_roads):
            candidates += colors[permuted_index[i]][1] + ', '
        candidates = candidates[:-2]
    else:
        candidates = ""
        for i in range(num_roads):
            candidates += labels[permuted_index[i]] + ', '
        candidates = candidates[:-2]

    #find the correct j such that permuted_index[j] = 0
    j = permuted_index.index(0)
    #Find the index l such that j!=l
    l = random.choice([i for i in range(num_roads) if i != j])


    if answer_in == 'color':
        d.entities.append((f'width1-color-{answer_type}', [candidates, colors[j][1], colors[l][1], num_roads]))
    else:
        d.entities.append((f'width1-label-{answer_type}', [candidates, labels[j], labels[l], num_roads]))
    return d


def width2(d):
    # The road is getting wider or narrower

    answer_type, wrong_answer_type = random.sample(["wider", "narrower"], 2)
    direction = random.choice(["up", "down", "right", "left"])

    #The road is getting wider or narrower as it goes to the direction

    larger_width = random.uniform(200, 500)
    smaller_width = random.uniform(50, 0.9*larger_width)

    length = random.uniform(700, 990)

    if direction == "up":
        x1,y1 = random.uniform(50, 500), random.uniform(50, 100)
        if answer_type == "wider":
            x2, y2 = x1 + smaller_width, y1
            x4, y4 = random.uniform(50, 500), y1 + length
            x3, y3 = x4 + larger_width, y4
        else:
            x2, y2 = x1 + larger_width, y1
            x4, y4 = random.uniform(50, 500), y1 + length
            x3, y3 = x4 + smaller_width, y4
    elif direction == "down":
        x1,y1 = random.uniform(50, 500), random.uniform(900, 950)
        if answer_type == "wider":
            x2, y2 = x1 + smaller_width, y1
            x4, y4 = random.uniform(50, 500), y1 - length
            x3, y3 = x4 + larger_width, y4
        else:
            x2, y2 = x1 + larger_width, y1
            x4, y4 = random.uniform(50, 500), y1 - length
            x3, y3 = x4 + smaller_width, y4
    elif direction == "right":
        x1, y1 = random.uniform(50, 100), random.uniform(50, 500)
        if answer_type == "wider":
            x2, y2 = x1, y1 + smaller_width
            x4, y4 = x1 + length, random.uniform(50, 500)
            x3, y3 = x4, y4 + larger_width
        else:
            x2, y2 = x1, y1 + larger_width
            x4, y4 = x1 + length, random.uniform(50, 500)
            x3, y3 = x4, y4 + smaller_width
    else: #direction == "left"
        x1, y1 = random.uniform(900, 950), random.uniform(50, 500)
        if answer_type == "wider":
            x2, y2 = x1, y1 + smaller_width
            x4, y4 = x1 - length, random.uniform(50, 500)
            x3, y3 = x4, y4 + larger_width
        else:
            x2, y2 = x1, y1 + larger_width
            x4, y4 = x1 - length, random.uniform(50, 500)
            x3, y3 = x4, y4 + smaller_width


    color_pair = random.choice(color_pairs.candidates)
    label = random.choice(small_letters_nonempty.candidates)

    d.polygons.append(polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], label, edge_color=color_pair[0], fill_color=color_pair[1]))
    d.entities.append((f'width2', [direction, color_pair[1], label, answer_type, wrong_answer_type]))

    return d


def line1(d):
    d.lines = []
    d.points = []

    answer_target = random.choice(["exists", "not"])
    answer_in = ["color", "label"]

    n = random.randint(2, 5)
    if answer_in == "color":
        colors = random.sample(d.usable_colors, n)
        if random.choice([True, False]):
            line_labels = [""] * n
        else:
            line_labels = random.sample(small_letters_nonempty.candidates, n)

        point_labels = [""] * 2*n
        labels = colors
        label_with_point = False



    else:
        if random.choice([True,False]):
            label_with_point = True
            point_labels = random.sample(small_letters_nonempty.candidates, 2*n)
            line_labels = [""] * n
            labels = [f"{point_labels[2*i]}{point_labels[2*i+1]}" for i in range(n)]
        else:
            label_with_point = False
            point_labels = [""] * 2*n
            line_labels = random.sample(small_letters_nonempty.candidates, n)
            labels = line_labels

        if random.choice([True, False]):
            colors = random.sample(d.usable_colors, n)
        else:
            colors = [random.choice(d.usable_colors)] * n


    permute = random.sample(range(n), n)


    if answer_target == "exists":
        for i in range(n):

            x1, y1 = random.uniform(50, 950), random.uniform(50, 950)
            x2, y2 = random.uniform(50, 950), random.uniform(50, 950)
            d.points.append(Point(x1, y1, point_labels[2*i]))
            d.points.append(Point(x2, y2, point_labels[2*i+1]))
            if i == 0:
                d.lines.append(Line(d.points[-2], d.points[-1], line_labels[i], color=colors[i]))


    else:
        for i in range(n):
            x1, y1 = random.uniform(50, 950), random.uniform(50, 950)
            x2, y2 = random.uniform(50, 950), random.uniform(50, 950)
            d.points.append(Point(x1, y1, point_labels[2*i]))
            d.points.append(Point(x2, y2, point_labels[2*i+1]))
            if i != 0:
                d.lines.append(Line(d.points[-2], d.points[-1], line_labels[i], color=colors[i]))


    if not label_with_point:
        d.points = []

    candidates = ""
    for i in range(n):
        candidates += labels[permute[i]] + ', '
    candidates = candidates[:-2]

    d.entities.append((f'line1-{answer_target}', [candidates, labels[0], labels[1], n]))
    return d


def line2(d):
    # line vs curve
    # Find a curve or straight line
    target = random.choice(["curve", "line"])

    # Choose colors
    colors = random.sample(d.usable_colors, 4)

    if target == "curve":
        num_curve, num_line = 1, 3
        answer_index = 0
    else:
        num_curve, num_line = 3, 1
        answer_index = 3

    x_list = []
    for _ in range(4):
        x_list.append(np.linspace(0, 500, 500))

    y_list = []
    for i in range(num_curve):
        a = random.uniform(-0.1, 0.1)
        i = random.choice(range(2, 10))
        y = a
        for j in range(i):
            b = random.uniform(200, 800)
            y = y * (x_list[0] - b)

        y_scale = np.max(y) - np.min(y)
        translation = random.uniform(0, 500)
        y = (y - np.min(y)) / y_scale * random.uniform(450, 1000 - translation) + translation
        y_list.append(y)

    for i in range(num_line):
        a =0.0001
        i = random.choice(range(1, 10))
        y1 = a * x_list[0] + random.uniform(-500,500)

        y1_scale = np.max(y1) - np.min(y1)
        translation = random.uniform(0, 500)
        y1 = (y1 - np.min(y1)) / y1_scale * 1000 * random.uniform(0.5, 1.5)

        y_list.append(y1)

    # Choose colors and lables
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

    permute_index = random.sample(range(4), 4)
    # answer_index = permute_index.index(answer_index)
    # wrong_index = random.choice([i for i in range(4) if i != answer_index])

    # Choose answer_type
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

        for i in range(4):
            candidate1 += colors[i] + "/"
            candidate2 += colors[i] + ", "
        d.entities.append(
            (f'line2-{target}', [colors[answer_index],colors[2], colors[3], "", candidate1[:-1], candidate2[:-2]]))

    d.curves = []
    d.lines = []
    d.points = []
    d.circles = []


    # Put these curves in left to right order by scaling two of them from 500~1000, two of them 0~500 for each of x and y
    for i in range(4):
        y = y_list[permute_index[i]]
        x = x_list[i] + random.uniform(525, 600) if i % 2 == 0 else x_list[i]

        if i < 2:
            y = (y - np.min(y)) / (np.max(y) - np.min(y)) * 475 * random.uniform(0.5, 1.5)

        else:
            y = (y - np.min(y)) / (np.max(y) - np.min(y)) * 475 * random.uniform(0.5, 1.5) + 550

        d.curves.append(Curve(x, y, '', color=colors[permute_index[i]]))

    return d

def line3(d):
    # Find connected points
    d.lines = []
    d.points = []

    n = random.randint(5,9)
    while len(d.points) < n:
        d = add_free_point(d)

    answer_target = random.choice(["exists", "not"])

    if answer_target == "exists": num_lines = random.randint(1, 3)
    else: num_lines = random.randint(3, 6)

    if random.choice([True, False]) and len(d.usable_colors) > num_lines:
        colors = random.sample(d.usable_colors, num_lines)
    else : colors = [random.choice(d.usable_colors)] * num_lines

    ind = 0
    line_labels = []
    existing_lines = []
    while len(d.lines) < num_lines:

        point1, point2 = random.sample(d.points, 2)
        #Check if they are too close
        if (point1.x - point2.x)**2 + (point1.y - point2.y)**2 < 625:
            continue

        #Check if the line already exists
        already_in = False
        for line in d.lines:
            if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
                already_in = True
                break
        if already_in: continue

        if random.choice ([True, False]):
            label = ""
        else:
            ind2 = 0
            while True:
                label = label_line(d)
                if label not in line_labels or label == "":
                    line_labels.append(label)
                    break
                if ind2 > 30:
                    return d
                ind2 += 1

        d.lines.append(Line(point1, point2, label, color=colors[ind]))
        existing_lines.append((f"{point1.label}{point2.label}", f"{point2.label}{point1.label}"))
        ind += 1


    #Generate not existing lines:
    not_existing_lines = []
    ind = 0
    if answer_target == "exists": num_nonlines = random.randint(3, 5)
    else: num_nonlines = random.randint(1, 3)

    while len(not_existing_lines) < 1:
        p1, p2 = random.sample(d.points, 2)

        if f"{p1.label}{p2.label}" in [x[0] for x in existing_lines] or f"{p1.label}{p2.label}" in [x[1] for x in existing_lines]:
            continue

        not_existing_lines.append((f"{p1.label}{p2.label}", f"{p2.label}{p1.label}"))

        if ind > 100:
            return d
        ind += 1


    answer_cands = [x[0] for x in existing_lines] + [x[0] for x in not_existing_lines]
    answer_cands = random.sample(answer_cands, len(answer_cands))
    canddiates = ""
    for cand in answer_cands:
        canddiates += cand + ", "

    answers = [x[0] for x in existing_lines]
    non_answers = [x[0] for x in not_existing_lines]
    if answer_target == "not":
        answers = [x[0] for x in not_existing_lines]
        non_answers = [x[0] for x in existing_lines]

    answer_string = ""
    for answer in answers:
        answer_string += answer + ", "


    if answer_target == "exists" and random.choice([True, False]):
        #find connecting points
        answer_target = "points"

        answer_string = ""
        tmp = [x[0][0] for x in existing_lines] + [x[0][1] for x in existing_lines]
        answer_points = []
        for p in tmp:
            if p not in answer_points:
                answer_points.append(p)
                answer_string += p + ", "

        while True:
            wrong_point = random.choice(capitals.candidates)
            if wrong_point not in answer_points:
                break

        n_points = len(answer_points)

        d.entities.append((f'line3-{answer_target}', [answer_string[:-2], answer_points[0], wrong_point, n_points]))
        return d



    d.entities.append((f'line3-{answer_target}', [canddiates[:-2], answers[0], non_answers[0], answer_string[:-2], num_lines, num_nonlines]))
    return d



def line4(d):
    #Choose the endpoints of the line
    d.points =[]

    while len(d.points) < 2:
        d = add_free_point(d)

    A, B = random.sample(d.points, 2)
    vec_AB = np.array([B.x - A.x, B.y - A.y])

    fake_points = []
    new_labels = []
    while len(fake_points) < 3:
        if random.choice([True, False]):
            scale = random.uniform(0.75, 0.95)
        else:
            scale = random.uniform(1.05, 1.25)

        if random.choice([True, False]):
            x,y = A.x + scale * vec_AB[0], A.y + scale * vec_AB[1]
        else :
            x,y = B.x - scale * vec_AB[0], B.y - scale * vec_AB[1]

        while True:
            label = label_point(d)
            if label not in new_labels:
                new_labels.append(label)
                break

        fake_points.append(Point(x, y, label))

    color = random.choice(d.usable_colors)
    d.lines.append(Line(A, B, '', color=color))
    d.points.extend(fake_points)
    d.entities.append((f'line4', [color, A.label, B.label, fake_points[0].label, fake_points[1].label, fake_points[2].label]))

    return d


def line5(d):
    #Find the lines connected to P
    d.points = []
    d.lines = []

    num_candidates = random.randint(3, 7)
    while len(d.points) < num_candidates:
        d = add_free_point(d)

    noise_num  = random.randint(0, 4)

    while len(d.lines) < noise_num:
        d = add_free_line(d)
    # print(f"succeeded with {len(d.lines)} lines")

    P_x, P_y = random.uniform(50, 950), random.uniform(50, 950)
    P = Point(P_x, P_y, label_point(d))

    num_answers = random.randint(0, num_candidates-1)
    if num_answers == 0:
        d.points.append(P)
        d.entities.append((f'line5-0', [P.label, num_candidates]))
        return d

    answer_points = random.sample(d.points, num_answers)
    d.points.append(P)
    answer_string = ""
    for point in answer_points:
        answer_string += point.label + ", "
        d.lines.append(Line(P, point, ''))
    d.entities.append((f'line5', [P.label, num_answers, answer_string[:-2]]))
    return d

def line6(d):
    #A curve and a line is connected to AB
    d.lines = []
    d.curves = []
    curve_color, line_color = random.sample(d.usable_colors, 2)
    d.usable_colors.remove(curve_color)
    d.usable_colors.remove(line_color)

    #add a random curve
    a = random.uniform(-0.1, 0.1)
    i = random.choice(range(2, 10))
    x = np.linspace(0, 500, 500)
    y = a
    for j in range(i):
        b = random.uniform(200, 800)
        y = y * (x - b)

    y_scale = np.max(y) - np.min(y)
    translation = random.uniform(0, 500)
    y = (y - np.min(y)) / y_scale * random.uniform(450, 1000 - translation) + translation

    d.curves.append(Curve(x, y, '', color=curve_color))

    #Define the endpoints of the curve
    labels = []
    while len(labels) < 2:
        label = label_point(d)
        if label not in labels:
            labels.append(label)

    Endpoint1 = Point(x[0], y[0], labels[0])
    Endpoint2 = Point(x[-1], y[-1], labels[1])

    #Define the line
    d.lines.append(Line(Endpoint1, Endpoint2, '', color=line_color))
    d.entities.append((f'line6', [curve_color, line_color, labels[0], labels[1]]))
    return d



#line segment인지 infinite line인지, line이 어디서 끝나는지, line 존재하는지

# find the points connected by the line
# line exists s/ line does not exist


