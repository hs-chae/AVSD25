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
        self.usable_colors = ['red', 'blue', 'green', 'purple', 'orange', 'brown', 'pink', 'grey', 'yellow']


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



def ortho1(d):
    # Find a foot

    d.points = []
    d.lines = []

    n = random.randint(2,5)

    answer_type = random.choice(["color", "label"])

    if answer_type == "color":
        colors = random.sample(d.usable_colors, n+1)
        if random.choice([True, False]):
            labels = ["" for _ in range(n+1)]
        else:
            labels = random.sample(capitals.candidates, n+1)
    else:
        if random.choice([True, False]):
            color = random.choice(d.usable_colors)
            remove_color(d,color)
        else: color = "black"
        colors = [color for _ in range(n)]

        labels = random.sample(capitals.candidates, n+1)



    Ax, Ay = 0, 0
    len_AB = random.uniform(200, 900)
    angle = random_angle()

    x_list = []
    ind = 0
    while len(x_list) < n:
        x_tmp = random.uniform(0, len_AB)
        far_enough = True
        for x in x_list:
            if abs(x - x_tmp) < 30:
                far_enough = False

        if far_enough:
            x_list.append(x_tmp)

        if ind > 100:
            return d 
        ind += 1 

    ans_x = x_list[0]
    y = random.uniform(100, 250)

    origin_vec = np.array([ans_x, y])
    candidate_vectors = [np.array([x, 0]) for x in x_list]
    end_1 = np.array([len_AB,0])

    angle = random_angle()

    translation_vector = [random_coord(), random_coord()]

    transformed_origin = rotate_vector(origin_vec, angle) + translation_vector
    transformed_end_0 = translation_vector
    transformed_end_1 = rotate_vector(end_1, angle) + translation_vector
    translated_candidates = [rotate_vector(vec, angle) + translation_vector for vec in candidate_vectors]

    line = Line(Point(transformed_end_0[0], transformed_end_0[1], ""), Point(transformed_end_1[0], transformed_end_1[1], ""), "")
    d.lines.append(line)

    for i in range(n):
        d.points.append(Point(translated_candidates[i][0], translated_candidates[i][1], labels[i], colors[i]))

    d.points.append(Point(transformed_origin[0], transformed_origin[1], labels[-1], colors[-1]))

    if answer_type == "color":
        candidate1 = ""
        candidate2 = ""
        permuted_index = random.sample(range(n), n)
        for i in range(n):
            candidate1 += f"{colors[permuted_index[i]]}, "
            candidate2 += f"{colors[permuted_index[i]]}/"
        d.entities.append((f"ortho1-{answer_type}",[colors[-1], colors[0], colors[1], candidate1[:-2], candidate2[:-1]]))
    else:
        candidate1 = ""
        candidate2 = ""
        permuted_index = random.sample(range(n), n)
        for i in range(n):
            candidate1 += f"{labels[permuted_index[i]]}, "
            candidate2 += f"{labels[permuted_index[i]]}/"
        d.entities.append((f"ortho1-{answer_type}",[labels[-1], labels[0], labels[1], candidate1[:-2], candidate2[:-1]]))
    return d



def ortho2(d):
    # Find the origin of the foot
    d.points = []
    d.lines = []

    n = random.randint(2, 5)

    answer_type = random.choice(["color", "label"])

    if answer_type == "color":
        colors = random.sample(d.usable_colors, n + 1)
        if random.choice([True, False]):
            labels = ["" for _ in range(n + 1)]
        else:
            labels = random.sample(capitals.candidates, n + 1)
    else:
        if random.choice([True, False]):
            color = random.choice(d.usable_colors)
            remove_color(d, color)
        else:
            color = "black"
        colors = [color for _ in range(n)]

        labels = random.sample(capitals.candidates, n + 1)

    Ax, Ay = 0, 0
    len_AB = random.uniform(200, 900)
    angle = random_angle()

    x_list = []
    ind = 0
    while len(x_list) < n:
        x_tmp = random.uniform(0, len_AB)
        far_enough = True
        for x in x_list:
            if abs(x - x_tmp) < 30:
                far_enough = False

        if far_enough:
            x_list.append(x_tmp)
        
        if ind > 100:
            return d 
        ind += 1

    ans_x = x_list[0]


    ans_vec = np.array([ans_x, 0])
    candidate_vectors = [np.array([x, random.uniform(50, 250)]) for x in x_list]
    end_1 = np.array([len_AB, 0])

    angle = random_angle()

    translation_vector = [random_coord(), random_coord()]

    transformed_origin = rotate_vector(ans_vec, angle) + translation_vector
    transformed_end_0 = translation_vector
    transformed_end_1 = rotate_vector(end_1, angle) + translation_vector
    translated_candidates = [rotate_vector(vec, angle) + translation_vector for vec in candidate_vectors]

    line = Line(Point(transformed_end_0[0], transformed_end_0[1], ""),
                Point(transformed_end_1[0], transformed_end_1[1], ""), "")
    d.lines.append(line)

    for i in range(n):
        d.points.append(Point(translated_candidates[i][0], translated_candidates[i][1], labels[i], colors[i]))

    d.points.append(Point(transformed_origin[0], transformed_origin[1], labels[-1], colors[-1]))

    if answer_type == "color":
        candidate1 = ""
        candidate2 = ""
        permuted_index = random.sample(range(n), n)
        for i in range(n):
            candidate1 += f"{colors[permuted_index[i]]}, "
            candidate2 += f"{colors[permuted_index[i]]}/"
        d.entities.append(
            (f"ortho2-{answer_type}", [colors[-1], colors[0], colors[1], candidate1[:-2], candidate2[:-1]]))
    else:
        candidate1 = ""
        candidate2 = ""
        permuted_index = random.sample(range(n), n)
        for i in range(n):
            candidate1 += f"{labels[permuted_index[i]]}, "
            candidate2 += f"{labels[permuted_index[i]]}/"
        d.entities.append(
            (f"ortho2-{answer_type}", [labels[-1], labels[0], labels[1], candidate1[:-2], candidate2[:-1]]))
    return d



def ortho3(d): #Find a perpendicular line to line XY

    d.lines = []



    answer_type = random.choice(["color", "label"])
    if answer_type == "color":
        n = random.randint(2, 6)
        colors = random.sample(d.usable_colors, n+1)
        if random.choice([True, False]):
            labels = ["" for _ in range(2*n+2)]
        else:
            labels = random.sample(capitals.candidates, 2*n+2)
    else:
        n = random.randint(2, 3)
        if random.choice([True, False]):
            color = random.choice(d.usable_colors)
            remove_color(d,color)
        else: color = "black"
        colors = [color for _ in range(n+1)]

        labels = random.sample(capitals.candidates, 2*n+2)


    #Choose the pillar line

    Ox, Oy = random_coord(), random_coord()
    angle = random.uniform(0, 2 * np.pi)
    length = random.uniform(200, 1000)
    Ux, Uy = Ox + length * np.cos(angle), Oy + length * np.sin(angle)



    perp_angle1, perp_angle2 = angle + np.pi/2, angle - np.pi/2
    candidate_lines =[]
    #Choose the perpendicular line
    if random.choice([True, False]):
        #Every line passes through the pillar line
        ind = 0
        while len(candidate_lines) < n:
            scale = random.uniform(0.1, 0.9)
            x = Ox + scale * (Ux - Ox)
            y = Oy + scale * (Uy - Oy)

            far_enough = True
            for line in candidate_lines:
                if abs(line[0] - x) < 30 and abs(line[1]-y) < 30:
                    far_enough = False

            if far_enough:
                candidate_lines.append([x,y])

            if ind > 100:
                return d 
            ind += 1 

    else:
        candidate_lines = [[random_coord(), random_coord()] for _ in range(n)]

    length1, length2 = random.uniform(100, 750), random.uniform(100, 750)
    i = 0
    x1, y1 = candidate_lines[i][0] + length1 * np.cos(perp_angle1), candidate_lines[i][1] + length1 * np.sin(
        perp_angle1)
    x2, y2 = candidate_lines[i][0] + length2 * np.cos(perp_angle2), candidate_lines[i][1] + length2 * np.sin(
        perp_angle2)
    candidate_lines2 = [Line(Point(x1, y1, labels[2*i+2],  color = colors[i+1]), Point(x2, y2, labels[2*i+3],  color = colors[i+1]), "",  color = colors[i+1])]


    ind = 0
    while len(candidate_lines2) < n :

        length1, length2 = random.uniform(100, 750), random.uniform(100, 750)
        i = len(candidate_lines2)
        if random.choice([True, False]):
            cand_angle = random.uniform(angle + np.pi/6.5, angle + np.pi/2.5)
        else: cand_angle = random.uniform(angle - np.pi/2.5, angle - np.pi/6.5)
        x1, y1 = candidate_lines[i][0] + length1 * np.cos(cand_angle), candidate_lines[i][1] + length1 * np.sin(cand_angle)
        x2, y2 = candidate_lines[i][0] - length2 * np.cos(cand_angle), candidate_lines[i][1] + length2 * np.sin(cand_angle)

        # print(f"n: {n}, i : {i}, len(labels) : {len(labels)}, len(colors) : {len(colors)}")
        candidate_lines2.append(Line(Point(x1, y1, labels[2*i+2], color = colors[i+1]), Point(x2, y2, labels[2*i+3], colors[i+1]), "",  color = colors[i+1]))

        if ind > 100:
            return d
        
        ind +=1 

    d.lines.extend(candidate_lines2)
    d.lines.append(Line(Point(Ox, Oy, labels[0], color = colors[0]), Point(Ux, Uy, labels[1], color = colors[0]), "",  color = colors[0]))

    if answer_type == "color":
        d.points = []
        candidate1 = ""
        candidate2 = ""
        permuted_index = random.sample(range(n), n)
        for i in range(n):
            candidate1 += f"{colors[permuted_index[i]]}, "
            candidate2 += f"{colors[permuted_index[i]]}/"
        d.entities.append((f"ortho3-{answer_type}",[colors[0], colors[1], colors[2], candidate1[:-2], candidate2[:-1]]))

    else:

        candidate1 = ""
        candidate2 = ""
        permuted_index = random.sample(range(n), n)
        for i in range(n):
            candidate1 += f"{labels[2*permuted_index[i]+2]}{labels[2*permuted_index[i]+3]}, "
            candidate2 += f"{labels[2*permuted_index[i]+2]}{labels[2*permuted_index[i]+3]}/"
        d.entities.append((f"ortho3-{answer_type}",[f"{labels[0]}{labels[1]}", f"{labels[2]}{labels[3]}", f"{labels[4]}{labels[5]}",candidate1[:-2], candidate2[:-1]]))

        d.points.extend([Point(Ox, Oy, labels[0], color=colors[0]), Point(Ux, Uy, labels[1], color=colors[0])])
        d.points.extend([line.point1 for line in candidate_lines2])
        d.points.extend([line.point2 for line in candidate_lines2])

    return d

#
# def ortho4(d): #Find the spot of orthogonal lines
#     d.points = []
#     d.lines = []
#
#     n = random.randint(3, 3) #Number of vertices
#     # labels = random.sample(capitals.candidates, n)
#     labels = [f"{i}" for i in range(n)]
#
#     Px, Py = [], []
#     while len(Px) < n:
#         x, y = random_coord(), random_coord()
#         far_enough = True
#         for i in range(len(Px)):
#             if abs(Px[i] - x) < 200 and abs(Py[i] - y) < 200:
#                 far_enough = False
#         if far_enough:
#             Px.append(x)
#             Py.append(y)
#
#     directions = {i: [] for i in range(n)}
#     # for i in range(n):
#     #     directions[i] = []
#
#     edges = []
#     connected = set()
#     threshold = random.randint(n-1, 10)
#     c = 0
#     # print(f"1. Edges: {edges}, connected: {connected}, threshold : {threshold}, c : {c}")
#     while (len(edges) < threshold or len(connected) < n ) and c < 100:
#         c += 1
#         # if c % 100 == 0:
#         # print(f"2. Edges: {edges}, connected: {connected}, threshold : {threshold}, c : {c}")
#         i, j = random.sample(range(n), 2)
#         if i < j and (i,j) not in edges:
#             edges.append((i,j))
#
#         #connected : set of connected vertices
#
#         connected.add(i)
#         connected.add(j)
#
#
#     for i, j in edges:
#         for l, m in edge
#
#
#
#     for i in range(n):
#         d.points.append(Point(Px[i], Py[i], labels[i], color = 'transparent'))
#
#     for i, j in edges:
#         d.lines.append(Line(d.points[i], d.points[j], ""))
#
#     d.entities.append(("ortho4", [labels]))
#     return d
#










    # answer_type = random.choice(["color", "label"])




















#Find a rihgt angle





