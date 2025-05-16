import warnings
import random
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
import matplotlib.path as mpath
import matplotlib.patches as mpatches

point_labels = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
num_labels = set(list("1234567890"))
func_labels = set(list("abcdefghijklmnopqrstuvwxyz"))
color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

class CartesianPoint:
    def __init__(self, label, x, y, color='black', alpha=1, size=20):
        self.label = label
        self.x = x
        self.y = y
        self.color = color
        self.alpha = alpha
        self.size = size

class PolarPoint:
    def __init__(self, label, theta, r, color='black', alpha=1, size=20):
        self.label = label
        self.theta = theta
        self.r = r
        self.color = color
        self.alpha = alpha
        self.size = size

class Poly_Function:
    def __init__(self, label, poly, roots, color, x_range=(-10, 10)):
        self.poly = poly
        self.x_range = x_range
        self.__make_xy()
        self.label = label
        self.roots = roots
        self.color = color
        self.y_intercept = self.f(0)

    def __make_xy(self):
        self.f = np.vectorize(lambda x: float(self.poly.subs(symbols('x'), x)))
        self.x_vals = np.linspace(self.x_range[0], self.x_range[1], 400)
        self.y_vals = self.f(self.x_vals)

class Triangle:
    def __init__(self, triangle_points, edgecolor, facecolor, label=None, alpha=1):
        self.points = triangle_points
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha

class Rectangle:
    def __init__(self, xy, width, height, edgecolor, facecolor, label=None, alpha=1):
        self.xy = xy
        self.width = width
        self.height = height
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha

class Parallelogram:
    def __init__(self, start, vector1, vector2, edgecolor, facecolor, label=None, alpha=1):
        self.points = np.array([
            start,
            start + vector1,
            start + vector1 + vector2,
            start + vector2
        ])
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha

class Circle:
    def __init__(self, xy, radius, edgecolor, facecolor, label=None, alpha=1):
        self.xy = xy
        self.radius = radius
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha

class Ellipse:
    def __init__(self, xy, width, height, edgecolor, facecolor, angle=0.0, label=None, alpha=1):
        self.xy = xy
        self.width = width
        self.height = height
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.angle = angle
        self.label = label
        self.alpha = alpha

class RegularPolygon:
    def __init__(self, xy, numVertices, radius, edgecolor, facecolor, orientation=0, label=None, alpha=1):
        self.xy = xy
        self.numVertices = numVertices
        self.radius = radius
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.orientation = orientation
        self.label = label
        self.alpha = alpha

class Diagram:
    def __init__(
        self,
        c_points=None,
        p_points=None,
        ftns=None,
        triangles=None,
        rectangles=None,
        parallelograms=None,
        circles=None,
        ellipses=None,
        regularpolygons=None,
        entities=None,
        background_color='white',
        labels=None
    ):
        self.c_points = c_points if c_points is not None else []
        self.p_points = p_points if p_points is not None else []
        self.ftns = ftns if ftns is not None else []
        self.triangles = triangles if triangles is not None else []
        self.rectangles = rectangles if rectangles is not None else []
        self.parallelograms = parallelograms if parallelograms is not None else []
        self.circles = circles if circles is not None else []
        self.ellipses = ellipses if ellipses is not None else []
        self.regularpolygons = regularpolygons if regularpolygons is not None else []
        self.entities = entities if entities is not None else []
        self.background_color = background_color
        self.labels = labels if labels is not None else []
        self.plot_type = None

    def set_plot_type(self, plot_type):
        self.plot_type = plot_type

def random_alphabet():
    return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def random_number():
    return random.choice('0123456789')

def random_color():
    return random.choice(color_list + ['black', 'black', 'black'])

def random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=1):
    min_integer = int(min_num * num_divide_1) + 1
    max_integer = int(max_num * num_divide_1)
    possible_coord_list = []

    if generate_type == 1:
        for x in range(min_integer, max_integer + 1):
            for y in range(min_integer, max_integer + 1):
                if num_divide_1 == 1:
                    possible_coord_list.append((x, y))
                else:
                    possible_coord_list.append((x/num_divide_1, y/num_divide_1))
    else:
        x_list = [i for i in range(min_integer, max_integer + 1)]
        y_list = [i for i in range(min_integer, max_integer + 1)]
        random.shuffle(x_list)
        random.shuffle(y_list)
        if num_divide_1 == 1:
            possible_coord_list = [(x, y) for (x, y) in zip(x_list, y_list)]
        else:
            possible_coord_list = [(x/num_divide_1, y/num_divide_1) for (x, y) in zip(x_list, y_list)]

    if len(possible_coord_list) < num_points:
        return possible_coord_list, len(possible_coord_list)

    answer_coord_list = []
    for _ in range(num_points):
        random_index = random.randint(0, len(possible_coord_list) - 1)
        random_element = possible_coord_list.pop(random_index)
        answer_coord_list.append(random_element)
    return answer_coord_list, num_points

def get_point_quadrant(x, y):
    if x == 0 or y == 0:
        return "axis"  
    if x > 0:
        if y > 0:
            return "1"
        else:
            return "4"
    else:
        if y > 0:
            return "2"
        else:
            return "3"

def generate_random_polynomial(degree=3, num_roots=None, is_duplicate=False):
    if num_roots is None:
        num_roots = degree

    if is_duplicate:
        roots = [random.choice(range(-10, 11)) for _ in range(num_roots)]
    else:
        roots = random.sample(range(-10, 11), num_roots)

    poly = 1
    for root in roots:
        poly *= (symbols('x') - root)

    return poly, roots

def shape_to_patch(shape):
    if isinstance(shape, Triangle):
        points = shape.points
        codes = [
            mpath.Path.MOVETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            mpath.Path.CLOSEPOLY
        ]
        vertices = list(points) + [points[0]]  # close path
        path = mpath.Path(vertices, codes)
        patch = mpatches.PathPatch(path, facecolor=shape.facecolor, edgecolor=shape.edgecolor, alpha=shape.alpha)
        return patch

    elif isinstance(shape, Rectangle):
        patch = mpatches.Rectangle(
            shape.xy, shape.width, shape.height,
            facecolor=shape.facecolor,
            edgecolor=shape.edgecolor,
            alpha=shape.alpha
        )
        return patch

    elif isinstance(shape, Parallelogram):
        codes = [
            mpath.Path.MOVETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            mpath.Path.LINETO,
            mpath.Path.CLOSEPOLY
        ]
        vertices = list(shape.points) + [shape.points[0]]
        path = mpath.Path(vertices, codes)
        patch = mpatches.PathPatch(path, facecolor=shape.facecolor, edgecolor=shape.edgecolor, alpha=shape.alpha)
        return patch

    elif isinstance(shape, Circle):
        patch = mpatches.Circle(
            shape.xy, shape.radius,
            facecolor=shape.facecolor,
            edgecolor=shape.edgecolor,
            alpha=shape.alpha
        )
        return patch

    elif isinstance(shape, Ellipse):
        patch = mpatches.Ellipse(
            shape.xy, shape.width, shape.height,
            angle=shape.angle,
            facecolor=shape.facecolor,
            edgecolor=shape.edgecolor,
            alpha=shape.alpha
        )
        return patch

    elif isinstance(shape, RegularPolygon):
        patch = mpatches.RegularPolygon(
            shape.xy, shape.numVertices, radius = shape.radius,
            orientation=shape.orientation,
            facecolor=shape.facecolor,
            edgecolor=shape.edgecolor,
            alpha=shape.alpha
        )
        return patch

    return None

def contains_point(shape, x, y):
    patch = shape_to_patch(shape)
    if patch is None:
        return False

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fig, ax = plt.subplots(figsize=(2,2)) 
        ax.add_patch(patch)
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)

        fig.canvas.draw()  
        disp_coords = ax.transData.transform((x, y))
        inside = patch.contains_point(disp_coords)

        plt.close(fig)
    return inside

def random_shape():
    shape_type = random.choice(["Triangle", "Rectangle", "Parallelogram", "Circle", "Ellipse", "RegularPolygon"])
    edgecolor = random.choice(color_list)
    facecolor = random.choice(color_list)
    alpha_ = random.uniform(0.3, 1.0)
    label_ = random.choice(list(point_labels))

    if shape_type == "Triangle":
        pts = []
        for _ in range(3):
            x = random.uniform(-5, 5)
            y = random.uniform(-5, 5)
            pts.append((x, y))
        return Triangle(pts, edgecolor, facecolor, label=label_, alpha=alpha_)

    elif shape_type == "Rectangle":
        x_ = random.uniform(-5, 5)
        y_ = random.uniform(-5, 5)
        w_ = random.uniform(1, 4)
        h_ = random.uniform(1, 4)
        return Rectangle((x_, y_), w_, h_, edgecolor, facecolor, label=label_, alpha=alpha_)

    elif shape_type == "Parallelogram":
        start = np.array([random.uniform(-5, 5), random.uniform(-5, 5)])
        v1 = np.array([random.uniform(1, 3), random.uniform(-1, 1)])
        v2 = np.array([random.uniform(-1, 1), random.uniform(1, 3)])
        return Parallelogram(start, v1, v2, edgecolor, facecolor, label=label_, alpha=alpha_)

    elif shape_type == "Circle":
        center = (random.uniform(-5, 5), random.uniform(-5, 5))
        r_ = random.uniform(1, 3)
        return Circle(center, r_, edgecolor, facecolor, label=label_, alpha=alpha_)

    elif shape_type == "Ellipse":
        center = (random.uniform(-5, 5), random.uniform(-5, 5))
        w_ = random.uniform(2, 5)
        h_ = random.uniform(1, 4)
        angle_ = random.uniform(0, 45)
        return Ellipse(center, w_, h_, edgecolor, facecolor, angle=angle_, label=label_, alpha=alpha_)

    elif shape_type == "RegularPolygon":
        center = (random.uniform(-5, 5), random.uniform(-5, 5))
        numV = random.randint(3, 8)
        radius = random.uniform(1, 4)
        orientation_ = random.uniform(0, np.pi/4)
        return RegularPolygon(center, numV, radius, edgecolor, facecolor, orientation=orientation_, label=label_, alpha=alpha_)

def get_polygon_quadrants(vertices):
    quadrants = set()
    for (x, y) in vertices:
        if x == 0 or y == 0:
            quadrants.add("axis")
        elif x > 0 and y > 0:
            quadrants.add("1")
        elif x < 0 and y > 0:
            quadrants.add("2")
        elif x < 0 and y < 0:
            quadrants.add("3")
        elif x > 0 and y < 0:
            quadrants.add("4")

    if len(quadrants) == 0:
        return "None"
    elif "axis" in quadrants:
        return "axis"
    else:
        return ",".join(sorted(list(quadrants)))


def coordinate2(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(1, 10)
    label_list = random.sample(list(point_labels), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])
    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=1)

    for idx in range(actual_num_points):
        label = label_list[idx]
        x, y = points[idx]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.c_points.append(CartesianPoint(label, x, y, color, alpha, size))
        diagram.labels.append(label)

    if actual_num_points > 0:
        label = label_list[actual_num_points - 1]
        x, y = points[actual_num_points - 1]
        diagram.entities.append(("coordinate2", ["plot_1", str(label), str(x), str(y)]))
    else:
        diagram.entities.append(("coordinate2", ["plot_1", "no_points"]))

    return diagram

def coordinate3(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(1, 10)
    color_random_list = random.sample(list(color_list), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])
    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=1)

    for idx in range(actual_num_points):
        x, y = points[idx]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.c_points.append(CartesianPoint("", x, y, color, alpha, size))

    if actual_num_points > 0:
        color = color_random_list[actual_num_points - 1]
        x, y = points[actual_num_points - 1]
        diagram.entities.append(("coordinate3", ["plot_1", str(color), str(x), str(y)]))
    else:
        diagram.entities.append(("coordinate3", ["plot_1", "no_points"]))

    return diagram

def coordinate4(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(3, 10)
    label_list = random.sample(list(point_labels), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])

    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)
    coord_choice = random.choice(["x", "y"])

    trial = 0
    while actual_num_points < 2:
        num_divide_1 = random.choice([1, 2, 5, 10])
        min_num = random.choice([-20, -15, -10, -5])
        max_num = random.choice([5, 10, 15, 20])

        points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)
        coord_choice = random.choice(["x", "y"])
        trial += 1
        if trial > 50:
            raise

    for idx in range(actual_num_points):
        label = label_list[idx]
        x, y = points[idx]
        if idx == 1:
            if coord_choice == "x":
                x = points[0][0]
            else:
                y = points[0][1]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.c_points.append(CartesianPoint(label, x, y, color, alpha, size))
        diagram.labels.append(label)

    diagram.entities.append(("coordinate4", ["plot_1", str(label_list[0]), str(coord_choice), str(label_list[1])]))
    return diagram

def coordinate5(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(3, 10)
    color_random_list = random.sample(list(color_list), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])

    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)
    coord_choice = random.choice(["x", "y"])

    while actual_num_points < 2:
        # 간단히: 점이 부족하니 엔티티만 남긴다거나, 혹은 리턴
        num_divide_1 = random.choice([1, 2, 5, 10])
        min_num = random.choice([-20, -15, -10, -5])
        max_num = random.choice([5, 10, 15, 20])

        points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)
        coord_choice = random.choice(["x", "y"])
        trial += 1
        if trial > 50:
            raise


    for idx in range(actual_num_points):
        x, y = points[idx]
        if idx == 1:
            if coord_choice == "x":
                x = points[0][0]
            else:
                y = points[0][1]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.c_points.append(CartesianPoint("", x, y, color, alpha, size))

    diagram.entities.append(("coordinate5", ["plot_1", str(color_random_list[0]), str(coord_choice), str(color_random_list[1])]))
    return diagram

def coordinate6(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(3, 10)
    label_list = random.sample(list(point_labels), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])

    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)
    coord_choice = random.choice(["x", "y"])

    while actual_num_points < 2:
        num_divide_1 = random.choice([1, 2, 5, 10])
        min_num = random.choice([-20, -15, -10, -5])
        max_num = random.choice([5, 10, 15, 20])

        points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)
        coord_choice = random.choice(["x", "y"])
        trial += 1
        if trial > 50:
            raise


    for idx in range(actual_num_points):
        label = label_list[idx]
        x, y = points[idx]
        if idx == 1:
            if coord_choice == "x":
                x = points[0][0]
            else:
                y = points[0][1]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.c_points.append(CartesianPoint(label, x, y, color, alpha, size))
        diagram.labels.append(label)

    diagram.entities.append(("coordinate6", ["plot_1", str(coord_choice), str(label_list[0]), str(label_list[1])]))
    return diagram

def coordinate7(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(3, 10)
    color_random_list = random.sample(list(color_list), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])

    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)
    coord_choice = random.choice(["x", "y"])

    while actual_num_points < 2:
        num_divide_1 = random.choice([1, 2, 5, 10])
        min_num = random.choice([-20, -15, -10, -5])
        max_num = random.choice([5, 10, 15, 20])

        points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)
        coord_choice = random.choice(["x", "y"])
        trial += 1
        if trial > 50:
            raise


    for idx in range(actual_num_points):
        x, y = points[idx]
        if idx == 1:
            if coord_choice == "x":
                x = points[0][0]
            else:
                y = points[0][1]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.c_points.append(CartesianPoint("", x, y, color, alpha, size))

    diagram.entities.append(("coordinate7", ["plot_1", str(coord_choice), str(color_random_list[0]), str(color_random_list[1])]))
    return diagram

def coordinate8(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(3, 10)
    label_list = random.sample(list(point_labels), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])
    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)

    info_dict = {
        "max_x": {"x/y": "x", "largest/smallest": "largest", "value": float("-inf"), "label": None},
        "max_y": {"x/y": "y", "largest/smallest": "largest", "value": float("-inf"), "label": None},
        "min_x": {"x/y": "x", "largest/smallest": "smallest", "value": float("inf"), "label": None},
        "min_y": {"x/y": "y", "largest/smallest": "smallest", "value": float("inf"), "label": None}
    }

    for idx in range(actual_num_points):
        label = label_list[idx]
        x, y = points[idx]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.c_points.append(CartesianPoint(label, x, y, color, alpha, size))
        diagram.labels.append(label)

        if x > info_dict['max_x']['value']:
            info_dict['max_x']['value'] = x
            info_dict['max_x']['label'] = label
        if y > info_dict['max_y']['value']:
            info_dict['max_y']['value'] = y
            info_dict['max_y']['label'] = label
        if x < info_dict['min_x']['value']:
            info_dict['min_x']['value'] = x
            info_dict['min_x']['label'] = label
        if y < info_dict['min_y']['value']:
            info_dict['min_y']['value'] = y
            info_dict['min_y']['label'] = label

    if actual_num_points > 0:
        random_key = random.choice(list(info_dict.keys()))
        s1 = info_dict[random_key]['x/y']
        s2 = info_dict[random_key]['largest/smallest']
        s3 = info_dict[random_key]['label']
        diagram.entities.append(("coordinate8", ["plot_1", str(s1), str(s2), str(s3)]))
    else:
        diagram.entities.append(("coordinate8", ["plot_1", "no_points"]))

    return diagram

def coordinate9(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(3, 10)
    color_random_list = random.sample(list(color_list), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])
    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=2)

    info_dict = {
        "max_x": {"x/y": "x", "largest/smallest": "largest", "value": float("-inf"), "label": None},
        "max_y": {"x/y": "y", "largest/smallest": "largest", "value": float("-inf"), "label": None},
        "min_x": {"x/y": "x", "largest/smallest": "smallest", "value": float("inf"), "label": None},
        "min_y": {"x/y": "y", "largest/smallest": "smallest", "value": float("inf"), "label": None}
    }

    for idx in range(actual_num_points):
        x, y = points[idx]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.c_points.append(CartesianPoint("", x, y, color, alpha, size))

        if x > info_dict['max_x']['value']:
            info_dict['max_x']['value'] = x
            info_dict['max_x']['label'] = color
        if y > info_dict['max_y']['value']:
            info_dict['max_y']['value'] = y
            info_dict['max_y']['label'] = color
        if x < info_dict['min_x']['value']:
            info_dict['min_x']['value'] = x
            info_dict['min_x']['label'] = color
        if y < info_dict['min_y']['value']:
            info_dict['min_y']['value'] = y
            info_dict['min_y']['label'] = color

    if actual_num_points > 0:
        random_key = random.choice(list(info_dict.keys()))
        s1 = info_dict[random_key]['x/y']
        s2 = info_dict[random_key]['largest/smallest']
        s3 = info_dict[random_key]['label']
        diagram.entities.append(("coordinate9", ["plot_1", str(s1), str(s2), str(s3)]))
    else:
        diagram.entities.append(("coordinate9", ["plot_1", "no_points"]))

    return diagram

def coordinate10(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(1, 10)
    label_list = random.sample(list(point_labels), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])

    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=1)
    chosen_label = None
    quadrant = None

    for idx in range(actual_num_points):
        label = label_list[idx]
        x, y = points[idx]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)

        if (not chosen_label) and (x != 0) and (y != 0):
            chosen_label = label
            quadrant = get_point_quadrant(x, y)

        if idx == actual_num_points - 1 and (not chosen_label):
            x = 1
            y = 1
            chosen_label = label
            quadrant = get_point_quadrant(x, y)

        diagram.c_points.append(CartesianPoint(label, x, y, color, alpha, size))
        diagram.labels.append(label)

    if chosen_label is not None and quadrant is not None:
        diagram.entities.append(("coordinate10", ["plot_1", chosen_label, quadrant]))
    else:
        diagram.entities.append(("coordinate10", ["plot_1", "no_quadrant"]))

    return diagram

def coordinate11(diagram):
    diagram.set_plot_type("cartesian")
    num_points = random.randint(1, 10)
    color_random_list = random.sample(list(color_list), num_points)
    num_divide_1 = random.choice([1, 2, 5, 10])
    min_num = random.choice([-20, -15, -10, -5])
    max_num = random.choice([5, 10, 15, 20])

    points, actual_num_points = random_cartesian_coordinates(num_points, num_divide_1, min_num, max_num, generate_type=1)
    chosen_color = None
    quadrant = None

    for idx in range(actual_num_points):
        x, y = points[idx]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)

        if (not chosen_color) and (x != 0) and (y != 0):
            chosen_color = color
            quadrant = get_point_quadrant(x, y)

        if idx == actual_num_points - 1 and (not chosen_color):
            x = 2
            y = -2
            chosen_color = color
            quadrant = get_point_quadrant(x, y)

        diagram.c_points.append(CartesianPoint("", x, y, color, alpha, size))

    if chosen_color is not None and quadrant is not None:
        diagram.entities.append(("coordinate11", ["plot_1", chosen_color, quadrant]))
    else:
        diagram.entities.append(("coordinate11", ["plot_1", "no_quadrant"]))

    return diagram

def coordinate12(diagram):
    diagram.set_plot_type("cartesian")
    degree = random.randint(1, 5)
    poly, roots = generate_random_polynomial(degree, is_duplicate=True)
    color = random.choice(color_list)
    label = random.choice(list(func_labels))
    ftn = Poly_Function(label, poly, roots, color)
    diagram.ftns.append(ftn)
    diagram.entities.append(("coordinate12", ["plot_1", label, "x", ", ".join(map(str, roots))]))
    return diagram

def coordinate13(diagram):
    diagram.set_plot_type("cartesian")
    shape = random_shape()
    label_ = shape.label
    if isinstance(shape, Triangle):
        diagram.triangles.append(shape)
        q_str = get_polygon_quadrants(shape.points)
    elif isinstance(shape, Rectangle):
        diagram.rectangles.append(shape)
        x0, y0 = shape.xy
        rect_verts = [
            (x0, y0),
            (x0 + shape.width, y0),
            (x0 + shape.width, y0 + shape.height),
            (x0, y0 + shape.height)
        ]
        q_str = get_polygon_quadrants(rect_verts)
    elif isinstance(shape, Parallelogram):
        diagram.parallelograms.append(shape)
        q_str = get_polygon_quadrants(shape.points)
    elif isinstance(shape, Circle):
        diagram.circles.append(shape)
        cx, cy = shape.xy
        r = shape.radius
        circle_verts = [
            (cx - r, cy - r),
            (cx - r, cy + r),
            (cx + r, cy + r),
            (cx + r, cy - r)
        ]
        q_str = get_polygon_quadrants(circle_verts)
    elif isinstance(shape, Ellipse):
        diagram.ellipses.append(shape)
        cx, cy = shape.xy
        w2 = shape.width / 2
        h2 = shape.height / 2
        ellipse_verts = [
            (cx - w2, cy - h2),
            (cx - w2, cy + h2),
            (cx + w2, cy + h2),
            (cx + w2, cy - h2)
        ]
        q_str = get_polygon_quadrants(ellipse_verts)
    elif isinstance(shape, RegularPolygon):
        diagram.regularpolygons.append(shape)
        center_x, center_y = shape.xy
        R = shape.radius
        N = shape.numVertices
        theta0 = shape.orientation
        poly_verts = []
        for i in range(N):
            theta_i = theta0 + 2 * np.pi * i / N
            px = center_x + R * np.cos(theta_i)
            py = center_y + R * np.sin(theta_i)
            poly_verts.append((px, py))
        q_str = get_polygon_quadrants(poly_verts)

    diagram.entities.append(("coordinate13", ["plot_1", label_, q_str]))
    return diagram

def coordinate14(diagram):
    diagram.set_plot_type("cartesian")
    shape = random_shape()
    label_ = shape.label

    if isinstance(shape, Triangle):
        diagram.triangles.append(shape)
        q_str = get_polygon_quadrants(shape.points)
    elif isinstance(shape, Rectangle):
        diagram.rectangles.append(shape)
        x0, y0 = shape.xy
        rect_verts = [
            (x0, y0),
            (x0 + shape.width, y0),
            (x0 + shape.width, y0 + shape.height),
            (x0, y0 + shape.height)
        ]
        q_str = get_polygon_quadrants(rect_verts)
    elif isinstance(shape, Parallelogram):
        diagram.parallelograms.append(shape)
        q_str = get_polygon_quadrants(shape.points)
    elif isinstance(shape, Circle):
        diagram.circles.append(shape)
        cx, cy = shape.xy
        r = shape.radius
        circle_verts = [
            (cx - r, cy - r),
            (cx - r, cy + r),
            (cx + r, cy + r),
            (cx + r, cy - r)
        ]
        q_str = get_polygon_quadrants(circle_verts)
    elif isinstance(shape, Ellipse):
        diagram.ellipses.append(shape)
        cx, cy = shape.xy
        w2 = shape.width / 2
        h2 = shape.height / 2
        ellipse_verts = [
            (cx - w2, cy - h2),
            (cx - w2, cy + h2),
            (cx + w2, cy + h2),
            (cx + w2, cy - h2)
        ]
        q_str = get_polygon_quadrants(ellipse_verts)
    elif isinstance(shape, RegularPolygon):
        diagram.regularpolygons.append(shape)
        center_x, center_y = shape.xy
        R = shape.radius
        N = shape.numVertices
        theta0 = shape.orientation
        poly_verts = []
        for i in range(N):
            theta_i = theta0 + 2 * np.pi * i / N
            px = center_x + R * np.cos(theta_i)
            py = center_y + R * np.sin(theta_i)
            poly_verts.append((px, py))
        q_str = get_polygon_quadrants(poly_verts)

    diagram.entities.append(("coordinate14", ["plot_1", label_, q_str]))
    return diagram

def coordinate17(diagram):
    num_points = random.randint(1, 10)
    label_list = random.sample(list(point_labels), num_points)
    choice = random.randint(0, 1)
    if choice == 0:
        diagram.set_plot_type("polar1")
    else:
        diagram.set_plot_type("polar2")

    all_theta_candidates = [i*np.pi/6 for i in range(0, 12)]
    if num_points > len(all_theta_candidates):
        num_points = len(all_theta_candidates)
    thetas = random.sample(all_theta_candidates, num_points)

    all_r_candidates = [i/2 for i in range(1, 20)]
    if num_points > len(all_r_candidates):
        num_points = len(all_r_candidates)
    rs = random.sample(all_r_candidates, num_points)

    points = [(r, theta) for (r, theta) in zip(rs, thetas)]

    for idx in range(num_points):
        label = label_list[idx]
        r, theta = points[idx]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.p_points.append(PolarPoint(label, theta, r, color, alpha, size))
        diagram.labels.append(label)

    if num_points > 0:
        r, theta = points[-1]
        label = label_list[-1]
        if choice == 0:
            i = round(theta * 6 / np.pi)
            diagram.entities.append(("coordinate17", ["plot_2", str(label), str(r), str(30*i) + " degrees"]))
        else:
            diagram.entities.append(("coordinate17", ["plot_2", str(label), str(r), str(theta)]))
    else:
        diagram.entities.append(("coordinate17", ["plot_2", "no_points"]))

    return diagram

def coordinate18(diagram):
    num_points = random.randint(1, 10)
    color_random_list = random.sample(list(color_list), num_points)
    choice = random.randint(0, 1)
    if choice == 0:
        diagram.set_plot_type("polar1")
    else:
        diagram.set_plot_type("polar2")

    all_theta_candidates = [i*np.pi/6 for i in range(0, 12)]
    if num_points > len(all_theta_candidates):
        num_points = len(all_theta_candidates)
    thetas = random.sample(all_theta_candidates, num_points)

    all_r_candidates = [i/2 for i in range(1, 20)]
    if num_points > len(all_r_candidates):
        num_points = len(all_r_candidates)
    rs = random.sample(all_r_candidates, num_points)

    points = [(r, theta) for (r, theta) in zip(rs, thetas)]

    for idx in range(num_points):
        r, theta = points[idx]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.p_points.append(PolarPoint("", theta, r, color, alpha, size))

    if num_points > 0:
        r, theta = points[-1]
        color = color_random_list[-1]
        if choice == 0:
            i = round(theta * 6 / np.pi)
            diagram.entities.append(("coordinate18", ["plot_2", str(color), str(r), str(30*i) + " degrees"]))
        else:
            diagram.entities.append(("coordinate18", ["plot_2", str(color), str(r), str(theta)]))
    else:
        diagram.entities.append(("coordinate18", ["plot_2", "no_points"]))

    return diagram

def coordinate19(diagram):
    num_points = random.randint(3, 10)
    label_list = random.sample(list(point_labels), num_points)
    choice = random.randint(0, 1)
    if choice == 0:
        diagram.set_plot_type("polar1")
    else:
        diagram.set_plot_type("polar2")

    all_theta_candidates = [i*np.pi/6 for i in range(0, 12)]
    if num_points > len(all_theta_candidates):
        num_points = len(all_theta_candidates)
    thetas = random.sample(all_theta_candidates, num_points)

    all_r_candidates = [i/2 for i in range(1, 20)]
    if num_points > len(all_r_candidates):
        num_points = len(all_r_candidates)
    rs = random.sample(all_r_candidates, num_points)

    coord_choice = random.choice(["r", "theta"])

    if len(rs) < 2 or len(thetas) < 2:
        diagram.entities.append(("coordinate20", ["plot_2", "not_enough_points"]))
        return diagram

    for idx in range(num_points):
        label = label_list[idx]
        r, theta = rs[idx], thetas[idx]
        if idx == 1:
            if coord_choice == "r":
                r = rs[0]
            else:
                theta = thetas[0]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.p_points.append(PolarPoint(label, theta, r, color, alpha, size))
        diagram.labels.append(label)

    if num_points >= 2:
        diagram.entities.append(("coordinate19", ["plot_2", str(label_list[0]), str(coord_choice), str(label_list[1])]))
    else:
        diagram.entities.append(("coordinate19", ["plot_2", "no_points"]))

    return diagram

def coordinate20(diagram):
    num_points = random.randint(3, 10)
    color_random_list = random.sample(list(color_list), num_points)
    choice = random.randint(0, 1)
    if choice == 0:
        diagram.set_plot_type("polar1")
    else:
        diagram.set_plot_type("polar2")

    all_theta_candidates = [i*np.pi/6 for i in range(0, 12)]
    if num_points > len(all_theta_candidates):
        num_points = len(all_theta_candidates)
    thetas = random.sample(all_theta_candidates, num_points)

    all_r_candidates = [i/2 for i in range(1, 20)]
    if num_points > len(all_r_candidates):
        num_points = len(all_r_candidates)
    rs = random.sample(all_r_candidates, num_points)

    coord_choice = random.choice(["r", "theta"])

    if len(rs) < 2 or len(thetas) < 2:
        diagram.entities.append(("coordinate20", ["plot_2", "not_enough_points"]))
        return diagram

    for idx in range(num_points):
        r, theta = rs[idx], thetas[idx]
        if idx == 1:
            if coord_choice == "r":
                r = rs[0]
            else:
                theta = thetas[0]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.p_points.append(PolarPoint("", theta, r, color, alpha, size))

    if num_points >= 2:
        diagram.entities.append(("coordinate20", ["plot_2", str(color_random_list[0]), str(coord_choice), str(color_random_list[1])]))
    else:
        diagram.entities.append(("coordinate20", ["plot_2", "no_points"]))

    return diagram

def coordinate21(diagram):
    num_points = random.randint(3, 10)
    label_list = random.sample(list(point_labels), num_points)
    choice = random.randint(0, 1)
    if choice == 0:
        diagram.set_plot_type("polar1")
    else:
        diagram.set_plot_type("polar2")

    all_theta_candidates = [i*np.pi/6 for i in range(0, 12)]
    if num_points > len(all_theta_candidates):
        num_points = len(all_theta_candidates)
    thetas = random.sample(all_theta_candidates, num_points)

    all_r_candidates = [i/2 for i in range(1, 20)]
    if num_points > len(all_r_candidates):
        num_points = len(all_r_candidates)
    rs = random.sample(all_r_candidates, num_points)

    coord_choice = random.choice(["r", "theta"])

    if len(rs) < 2 or len(thetas) < 2:
        diagram.entities.append(("coordinate21", ["plot_2", "not_enough_points"]))
        return diagram

    for idx in range(num_points):
        label = label_list[idx]
        r, theta = rs[idx], thetas[idx]
        if idx == 1:
            if coord_choice == "r":
                r = rs[0]
            else:
                theta = thetas[0]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.p_points.append(PolarPoint(label, theta, r, color, alpha, size))
        diagram.labels.append(label)

    if num_points >= 2:
        diagram.entities.append(("coordinate21", ["plot_2", str(coord_choice), str(label_list[0]), str(label_list[1])]))
    else:
        diagram.entities.append(("coordinate21", ["plot_2", "no_points"]))

    return diagram

def coordinate22(diagram):
    num_points = random.randint(3, 10)
    color_random_list = random.sample(list(color_list), num_points)
    choice = random.randint(0, 1)
    if choice == 0:
        diagram.set_plot_type("polar1")
    else:
        diagram.set_plot_type("polar2")

    all_theta_candidates = [i*np.pi/6 for i in range(0, 12)]
    if num_points > len(all_theta_candidates):
        num_points = len(all_theta_candidates)
    thetas = random.sample(all_theta_candidates, num_points)

    all_r_candidates = [i/2 for i in range(1, 20)]
    if num_points > len(all_r_candidates):
        num_points = len(all_r_candidates)
    rs = random.sample(all_r_candidates, num_points)

    coord_choice = random.choice(["r", "theta"])

    if len(rs) < 2 or len(thetas) < 2:
        diagram.entities.append(("coordinate22", ["plot_2", "not_enough_points"]))
        return diagram

    for idx in range(num_points):
        r, theta = rs[idx], thetas[idx]
        if idx == 1:
            if coord_choice == "r":
                r = rs[0]
            else:
                theta = thetas[0]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.p_points.append(PolarPoint("", theta, r, color, alpha, size))

    if num_points >= 2:
        diagram.entities.append(("coordinate22", ["plot_2", str(coord_choice), str(color_random_list[0]), str(color_random_list[1])]))
    else:
        diagram.entities.append(("coordinate22", ["plot_2", "no_points"]))

    return diagram

def coordinate23(diagram):
    num_points = random.randint(1, 10)
    label_list = random.sample(list(point_labels), num_points)
    choice = random.randint(0, 1)
    if choice == 0:
        diagram.set_plot_type("polar1")
    else:
        diagram.set_plot_type("polar2")

    all_theta_candidates = [i*np.pi/6 for i in range(0, 12)]
    if num_points > len(all_theta_candidates):
        num_points = len(all_theta_candidates)
    thetas = random.sample(all_theta_candidates, num_points)

    all_r_candidates = [i/2 for i in range(1, 20)]
    if num_points > len(all_r_candidates):
        num_points = len(all_r_candidates)
    rs = random.sample(all_r_candidates, num_points)

    info_dict = {
        "max_r": {"r/theta": "r", "largest/smallest": "largest", "value": -1, "label": None},
        "max_theta": {"r/theta": "theta", "largest/smallest": "largest", "value": -1, "label": None},
        "min_r": {"r/theta": "r", "largest/smallest": "smallest", "value": float('inf'), "label": None},
        "min_theta": {"r/theta": "theta", "largest/smallest": "smallest", "value": float('inf'), "label": None}
    }

    if len(rs) == 0:
        diagram.entities.append(("coordinate23", ["plot_2", "no_points"]))
        return diagram

    points = [(r, theta) for (r, theta) in zip(rs, thetas)]
    for idx in range(num_points):
        label = label_list[idx]
        r, theta = points[idx]
        color = random.choice(color_list)
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.p_points.append(PolarPoint(label, theta, r, color, alpha, size))
        diagram.labels.append(label)

        if r > info_dict['max_r']['value']:
            info_dict['max_r']['value'] = r
            info_dict['max_r']['label'] = label
        if theta > info_dict['max_theta']['value']:
            info_dict['max_theta']['value'] = theta
            info_dict['max_theta']['label'] = label
        if r < info_dict['min_r']['value']:
            info_dict['min_r']['value'] = r
            info_dict['min_r']['label'] = label
        if theta < info_dict['min_theta']['value']:
            info_dict['min_theta']['value'] = theta
            info_dict['min_theta']['label'] = label

    random_key = random.choice(list(info_dict.keys()))
    s1 = info_dict[random_key]['r/theta']
    s2 = info_dict[random_key]['largest/smallest']
    s3 = info_dict[random_key]['label']
    diagram.entities.append(("coordinate23", ["plot_2", str(s1), str(s2), str(s3)]))
    return diagram

def coordinate24(diagram):
    num_points = random.randint(1, 10)
    color_random_list = random.sample(list(color_list), num_points)
    choice = random.randint(0, 1)
    if choice == 0:
        diagram.set_plot_type("polar1")
    else:
        diagram.set_plot_type("polar2")

    all_theta_candidates = [i*np.pi/6 for i in range(0, 12)]
    if num_points > len(all_theta_candidates):
        num_points = len(all_theta_candidates)
    thetas = random.sample(all_theta_candidates, num_points)

    all_r_candidates = [i/2 for i in range(1, 20)]
    if num_points > len(all_r_candidates):
        num_points = len(all_r_candidates)
    rs = random.sample(all_r_candidates, num_points)

    info_dict = {
        "max_r": {"r/theta": "r", "largest/smallest": "largest", "value": -1, "label": None},
        "max_theta": {"r/theta": "theta", "largest/smallest": "largest", "value": -1, "label": None},
        "min_r": {"r/theta": "r", "largest/smallest": "smallest", "value": float('inf'), "label": None},
        "min_theta": {"r/theta": "theta", "largest/smallest": "smallest", "value": float('inf'), "label": None}
    }

    if len(rs) == 0:
        diagram.entities.append(("coordinate24", ["plot_2", "no_points"]))
        return diagram

    points = [(r, theta) for (r, theta) in zip(rs, thetas)]
    for idx in range(num_points):
        r, theta = points[idx]
        color = color_random_list[idx]
        alpha = random.uniform(0.3, 1)
        size = random.randint(15, 45)
        diagram.p_points.append(PolarPoint("", theta, r, color, alpha, size))

        if r > info_dict['max_r']['value']:
            info_dict['max_r']['value'] = r
            info_dict['max_r']['label'] = color
        if theta > info_dict['max_theta']['value']:
            info_dict['max_theta']['value'] = theta
            info_dict['max_theta']['label'] = color
        if r < info_dict['min_r']['value']:
            info_dict['min_r']['value'] = r
            info_dict['min_r']['label'] = color
        if theta < info_dict['min_theta']['value']:
            info_dict['min_theta']['value'] = theta
            info_dict['min_theta']['label'] = color

    random_key = random.choice(list(info_dict.keys()))
    s1 = info_dict[random_key]['r/theta']
    s2 = info_dict[random_key]['largest/smallest']
    s3 = info_dict[random_key]['label']
    diagram.entities.append(("coordinate24", ["plot_2", str(s1), str(s2), str(s3)]))
    return diagram

rules = [
    coordinate2,
    coordinate3,
    coordinate4,
    coordinate5,
    coordinate6,
    coordinate7,
    coordinate8,
    coordinate9,
    coordinate10,
    coordinate11,
    coordinate12,
    coordinate13,
    coordinate14,
    coordinate17,
    coordinate18,
    coordinate19,
    coordinate20,
    coordinate21,
    coordinate22,
    coordinate23,
    coordinate24
]
