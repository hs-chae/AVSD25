import random
import math
import colorsys
import nltk
import nltk.corpus as corpus
import numpy as np
import matplotlib.pyplot as plt
nltk.download('words', quiet=True)

class Point:
    def __init__(self, x, y, color, label=""):
        self.x = x
        self.y = y
        self.color = color
        self.label = label

class Polygon:
    def __init__(self, x, y, n, border_color, fill_color, size=0.1, label="", rotation=0):
        self.x = x
        self.y = y
        self.n = n
        self.border_color = border_color
        self.fill_color = fill_color
        self.size = size
        self.label = label
        self.rotation = rotation
    
    def points(self):
        if self.n == 4:
            rotation = self.rotation + 45
        else:
            rotation = self.rotation + 90
        rotation = math.radians(rotation)
        return [(self.x + self.size * math.cos(2 * math.pi * i / self.n + rotation), self.y + self.size * math.sin(2 * math.pi * i / self.n + rotation)) for i in range(self.n)]
    
class Line:
    def __init__(self, x1, y1, x2, y2, color, label=""):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.label = label

class Circle:
    def __init__(self, x, y, r, border_color, fill_color, label=""):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label

class Star:
    def __init__(self, x, y, r, border_color, fill_color, label="", n=5):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.n = n
    
    def points(self):
        points = []

        cx = self.x
        cy = self.y
        outer_r = self.r
        inner_r = self.r / 2

        angle_step = 2 * math.pi / self.n  # Angle step for each outer vertex
        
        for i in range(self.n):
            # Outer vertex
            outer_x = cx + outer_r * math.cos(i * angle_step + math.pi / 2)
            outer_y = cy + outer_r * math.sin(i * angle_step + math.pi / 2)
            points.append((outer_x, outer_y))
            
            # Inner vertex
            inner_x = cx + inner_r * math.cos(i * angle_step + angle_step / 2 + math.pi / 2)
            inner_y = cy + inner_r * math.sin(i * angle_step + angle_step / 2 + math.pi / 2)
            points.append((inner_x, inner_y))
        
        return points
    
class Heart:
    def __init__(self, x, y, r, border_color, fill_color, label=""):
        self.x = x
        self.y = y
        self.r = r / 15
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
    
    def points(self):
        return   [
            (
                self.x + self.r * (16 * math.sin(t)**3), 
                self.y + self.r * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))  # Reverse the sign
            )
            for t in [i * 2 * math.pi / 100 for i in range(100)]
        ]
    
class Text:
    def __init__(self, x, y, text, color, size=0.1):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = size

class TextBox:
    def __init__(self, x, y, text, border_color, fill_color, size=1):
        self.x = x
        self.y = y
        self.text = text
        self.border_color = border_color
        self.fill_color = fill_color
        self.size = size

class Diagram:
    def __init__(self):
        self.polygon = []
        self.line = []
        self.circle = []
        self.star = []
        self.heart = []
        self.text = []
        self.textbox = []
        self.entities = []
        self.point = []
        self.arrow = []
        self.colorbar = []

class Colorbar:
    def __init__(self, x, y, w, h, direction, cmap):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.direction = direction
        self.cmap = cmap

class Arrow:
    def __init__(self, x, y, l, w, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [
            (1/2, 0),
            (1/6, 1/2),
            (1/6, 1/6),
            (-1/2, 1/6),
            (-1/2, -1/6),
            (1/6, -1/6),
            (1/6, -1/2)
        ]
        p = np.array(p)
        p *= np.array([self.l, self.w])
        angle = self.rotation * math.pi / 180
        p = np.dot(p, np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]).T)
        p += np.array([self.x, self.y])
        return p

def random_hsv():
    h = random.uniform(0, 360)
    s = random.uniform(0, 1)
    v = random.uniform(0, 1)
    return (h, s, v)

color_list = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'gray', 'brown', 'pink', 'cyan', 'magenta', 'lime', 'olive', 'maroon', 'navy', 'teal', 'silver', 'gold']
weighted_color_list = ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'gray', 'brown', 'pink']

def random_color():
    return random.choice(random.choice([color_list, weighted_color_list]))

def random_polygon(diagram):
    n = random.randint(3, 6)
    x = random.uniform(0.1, 0.9)
    y = random.uniform(0.1, 0.9)
    border_color = random_color()
    fill_color = random_color()
    size = random.uniform(0.05, 0.15)
    polygon = Polygon(x, y, n, border_color, fill_color, size)

    diagram.polygon.append(polygon)
    return polygon

def random_circle(diagram):
    r = random.uniform(0.05, 0.2)
    x = random.uniform(0.1 + r, 0.9 - r)
    y = random.uniform(0.1 + r, 0.9 - r)
    border_color = random_color()
    fill_color = random_color()
    circle = Circle(x, y, r, border_color, fill_color)

    diagram.circle.append(circle)
    return circle

def random_star(diagram):
    r = random.uniform(0.05, 0.2)
    x = random.uniform(0.1 + r, 0.9 - r)
    y = random.uniform(0.1 + r, 0.9 - r)
    n = random.randint(5, 6)
    border_color = random_color()
    fill_color = random_color()
    star = Star(x, y, r, border_color, fill_color, n=n)

    diagram.star.append(star)
    return star

def random_heart(diagram):
    r = random.uniform(0.05, 0.2)
    x = random.uniform(0.1 + r, 0.9 - r)
    y = random.uniform(0.1 + r, 0.9 - r)
    border_color = random_color()
    fill_color = random_color()
    heart = Heart(x, y, r, border_color, fill_color)

    diagram.heart.append(heart)
    return heart

def random_text(diagram):
    rand = random.randint(0, 1) # 0: color, 1: any

    x = random.uniform(0.1, 0.9)
    y = random.uniform(0.1, 0.9)

    if rand == 0:
        text = random_color()
    else:
        text = random.choice(corpus.words.words())
    
    color = random_color()
    size = random.uniform(10, 30)
    
    text = Text(x, y, text, color, size)
    diagram.text.append(text)
    return text

def random_textbox(diagram):
    x = random.uniform(0.1, 0.9)
    y = random.uniform(0.1, 0.9)
    text = random.choice(corpus.words.words())
    border_color = random_color()
    fill_color = random_color()
    size = random.uniform(10, 30)
    
    textbox = TextBox(x, y, text, border_color, fill_color, size)
    diagram.textbox.append(textbox)
    return textbox

def random_line(diagram):
    x1 = random.uniform(0.1, 0.9)
    y1 = random.uniform(0.1, 0.9)
    x2 = random.uniform(0.1, 0.9)
    y2 = random.uniform(0.1, 0.9)
    color = random_color()
    line = Line(x1, y1, x2, y2, color)

    diagram.line.append(line)
    return line

def random_point(diagram):
    x = random.uniform(0.1, 0.9)
    y = random.uniform(0.1, 0.9)
    color = random_color()
    point = Point(x, y, color)

    diagram.point.append(point)
    return point

def color1(diagram):
    random_object = random.choice([random_polygon, random_circle, random_star, random_heart, random_text, random_textbox])
    object = random_object(diagram)

    rand = random.randint(0, 1) # 0: border, 1: fill

    if rand == 0:
        object.fill_color = "white"
    else:
        object.border_color = "white"

    diagram.entities.append(('color1', object, rand))

    return object

def is_valid_point(new_point, points, min_distance):
    """
    Check if the new_point is valid given existing points and minimum distance.
    """
    for point in points:
        distance = math.sqrt((new_point[0] - point[0])**2 + (new_point[1] - point[1])**2)
        if distance <= min_distance:
            return False
    return True

def select_coordinates(n, d):
    """
    Select n coordinates in the range (0, 0) to (1, 1) such that the minimum
    distance between any two points is greater than d.
    """
    selected_points = []
    attempts = 0  # To prevent infinite loops in case n and d are incompatible.

    while len(selected_points) < n and attempts < 10000:
        new_point = (random.uniform(0, 1), random.uniform(0, 1))
        if is_valid_point(new_point, selected_points, d):
            selected_points.append(new_point)
        attempts += 1

    if len(selected_points) < n:
        raise ValueError(f"Could not find {n} points with minimum distance {d} after 10,000 attempts.")
    
    return selected_points

def color2_a(diagram):
    same_shape = random.randint(0, 1)
    objects = []
    n = random.randint(4, 8)

    if same_shape:
        random_object = random.choice([random_polygon, random_circle, random_star, random_heart, random_line, random_point])
        objects = [random_object(diagram) for _ in range(n)]
        if isinstance(objects[0], Polygon):
            for object in objects:
                object.n = objects[0].n
    else:
        for _ in range(n):
            random_object = random.choice([random_polygon, random_circle, random_star, random_heart])
            objects.append(random_object(diagram))

    rand = random.randint(0, 1) # 0: border, 1: fill

    if not isinstance(objects[0], Line) and not isinstance(objects[0], Point):
        if rand == 0:
            for object in objects:
                object.fill_color = "none"
        else:
            for object in objects:
                object.border_color = "none"

        if rand == 1 or random.randint(0, 1):
            positions = select_coordinates(n, 0.2)
            for i, object in enumerate(objects):
                object.x, object.y = positions[i]

    if isinstance(objects[0], Line) or isinstance(objects[0], Point):
        colors = [object.color for object in objects]
    else:
        if rand == 0:
            colors = [object.border_color for object in objects]
        else:
            colors = [object.fill_color for object in objects]

    colors = list(set(colors))
    diagram.entities.append(('color2_a', objects, colors, same_shape))

def color2_b(diagram):
    n = random.randint(3, 6)
    x = random.uniform(0.1, 0.9)
    y = random.uniform(0.1, 0.9)
    r = random.uniform(0.1, 0.3)
    positions = [
        (
            x - r * math.sin(2 * math.pi * i / n),
            y + r * math.cos(2 * math.pi * i / n)
        )
        for i in range(n)
    ]
    lines = []
    for i in range(n):
        x1, y1 = positions[i]
        x2, y2 = positions[(i + 1) % n]
        color = random_color()
        line = Line(x1, y1, x2, y2, color)
        lines.append(line)
    diagram.line.extend(lines)

    colors = [line.color for line in lines]
    colors = list(set(colors))

    diagram.entities.append(('color2_b', n, colors))

def color3(diagram):
    base_color = random_hsv()

    variation = random.randint(0, 1)    # 0: s, 1: v

    if base_color[1] < 0.5:
        base_color = (base_color[0], 0.5, base_color[2])
    if base_color[2] < 0.5:
        base_color = (base_color[0], base_color[1], 0.5)

    if variation == 0:
        colors =[
            (base_color[0], 2/7, base_color[2]),
            (base_color[0], 3/7, base_color[2]),
            (base_color[0], 4/7, base_color[2]),
            (base_color[0], 5/7, base_color[2])
        ]
    else:
        colors = [
            (base_color[0], base_color[1], 5/10),
            (base_color[0], base_color[1], 6/10),
            (base_color[0], base_color[1], 7/10),
            (base_color[0], base_color[1], 8/10)
        ]

    if random.randint(0, 1):
        colors.reverse()
    
    change_positions = [
        (1/6, 0.5), (2/6, 0.5), (3/6, 0.5), (4/6, 0.5), (5/6, 0.5)
    ]
    options_positions = random.choice([
        [
            (1/5, 0.2), (2/5, 0.2), (3/5, 0.2), (4/5, 0.2)
        ],
        [
            (1/5, 0.8), (2/5, 0.8), (3/5, 0.8), (4/5, 0.8)
        ]
    ])

    random_shape = random.choice([random_polygon, random_circle])
    objects = [random_shape(diagram) for _ in range(5)]


    n = random.randint(3, 6)

    if random_shape == random_polygon:
        for object in objects:
            object.n = n

    for i, object in enumerate(objects[:-1]):
        object.fill_color = colorsys.hsv_to_rgb(*colors[i])
        object.border_color = "none"
        object.x, object.y = change_positions[i]
        object.size = 1/12
        object.r = 1/12 - 0.01
    
    objects[-1].fill_color = 'black'
    objects[-1].border_color = 'none'
    objects[-1].x, objects[-1].y = change_positions[-1]
    objects[-1].size = 1/12
    objects[-1].r = 1/12 - 0.01
    objects[-1].label = '?'

    if variation == 0:
        answer_color = base_color[0], 1/7 if colors[-1][1] < 0.7 else 6/7, base_color[2]
    else:
        answer_color = base_color[0], base_color[1], 4/10 if colors[-1][2] < 0.7 else 9/10

    options_colors = [answer_color]

    for _ in range(3):
        color = random_hsv()
        while h_difference(color[0], answer_color[0]) < 90:
            color = random_hsv()
        options_colors.append(color)

    index_options = [(i, options_colors[i]) for i in range(4)]
    random.shuffle(index_options)
    options_colors = [color for i, color in index_options]

    answer_index = 0

    for i in range(4):
        if index_options[i][0] == 0:
            answer_index = i

    labels = random.choice([
        '1234',
        'ABCD',
        ['I', 'II', 'III', 'IV'],
    ])

    for i, color in enumerate(options_colors):
        object = random_shape(diagram)
        if random_shape == random_polygon:
            object.n = n
        object.fill_color = colorsys.hsv_to_rgb(*color)
        object.border_color = "none"
        object.x, object.y = options_positions[i]
        object.size = 1/12
        object.r = 1/12 - 0.01
        object.label = labels[i]

    diagram.entities.append(('color3', labels[answer_index]))

def color5(diagram):
    color = random_hsv()
    brightnesses = [0.2, 0.4, 0.6, 0.8]
    random.shuffle(brightnesses)
    colors = [(color[0], color[1], brightness) for brightness in brightnesses]

    rand = random.randint(0, 4)

    positions = [
        [(0.2, 0.5), (0.4, 0.5), (0.6, 0.5), (0.8, 0.5)],
        [(0.5, 0.8), (0.5, 0.6), (0.5, 0.4), (0.5, 0.2)],
        [(0.2, 0.5), (0.4, 0.5), (0.6, 0.5), (0.8, 0.5)],
        [(0.5, 0.8), (0.5, 0.6), (0.5, 0.4), (0.5, 0.2)],
        select_coordinates(4, 0.2)
    ][rand]

    random_shape = random.choice([random_polygon, random_circle, random_star, random_heart])
    objects = [random_shape(diagram) for _ in range(4)]

    if random_shape == random_polygon:
        if random.randint(0, 2):
            for object in objects:
                object.n = objects[0].n

        for object in objects:
            object.size = min(object.size, 0.1)
        
        if random.randint(0, 2):
            object.size = objects[0].size
    else:
        for object in objects:
            object.r = min(object.r, 0.1)
        if random.randint(0, 2):
            for object in objects:
                object.r = objects[0].r
    
    if random_shape == random_star:
        for object in objects:
            object.n = objects[0].n

    for i, object in enumerate(objects):
        object.fill_color = colorsys.hsv_to_rgb(*colors[i])
        object.border_color = 'none'
        object.x, object.y = positions[i]

    for i in range(len(objects)):
        objects[i].label = str(i + 1)
    
    diagram.entities.append(('color5', objects, brightnesses))

def color6(diagram):
    color = random_hsv()
    brightness = max(0.3, color[2])
    saturations = [0.2, 0.4, 0.6, 0.8]
    random.shuffle(saturations)
    colors = [(color[0], saturation, brightness) for saturation in saturations]

    rand = random.randint(0, 4)

    positions = [
        [(0.2, 0.5), (0.4, 0.5), (0.6, 0.5), (0.8, 0.5)],
        [(0.5, 0.8), (0.5, 0.6), (0.5, 0.4), (0.5, 0.2)],
        [(0.2, 0.5), (0.4, 0.5), (0.6, 0.5), (0.8, 0.5)],
        [(0.5, 0.8), (0.5, 0.6), (0.5, 0.4), (0.5, 0.2)],
        select_coordinates(4, 0.2)
    ][rand]

    random_shape = random.choice([random_polygon, random_circle, random_star, random_heart])
    objects = [random_shape(diagram) for _ in range(4)]

    if random_shape == random_polygon:
        if random.randint(0, 2):
            for object in objects:
                object.n = objects[0].n

        for object in objects:
            object.size = min(object.size, 0.1)
        
        if random.randint(0, 2):
            object.size = objects[0].size
    else:
        for object in objects:
            object.r = min(object.r, 0.1)
        if random.randint(0, 2):
            for object in objects:
                object.r = objects[0].r
    
    if random_shape == random_star:
        for object in objects:
            object.n = objects[0].n

    for i, object in enumerate(objects):
        object.fill_color = colorsys.hsv_to_rgb(*colors[i])
        object.border_color = 'none'
        object.x, object.y = positions[i]

    for i in range(len(objects)):
        objects[i].label = str(i + 1)

    diagram.entities.append(('color6', objects, saturations))

def color7(diagram):
    background = random_polygon(diagram)
    background.fill_color = random_color()
    background.n = 4
    background.size = 2

    n = random.randint(4, 10)
    objects = [random_polygon(diagram) for _ in range(n)]

    if random.randint(0, 1):
        for object in objects:
            object.fill_color = "none"
    else:
        positions = select_coordinates(n, 0.2)
        for object in objects:
            object.x, object.y = positions.pop()
            object.border_color = "none"

    diagram.entities.append(('color7', background.fill_color))

def color8(diagram):
    random_object = random.choice([random_polygon, random_circle, random_star, random_heart])
    n = random.randint(3, 7)
    shapes = [random_object(diagram) for _ in range(n)]

    if random.randint(0, 1):
        for shape in shapes:
            shape.fill_color = "none"
        while all(shapes[i].border_color == shapes[i + 1].border_color for i in range(n - 1)):
            for shape in shapes:
                shape.border_color = random_color()
    else:
        for shape in shapes:
            shape.border_color = "none"
        while all(shapes[i].fill_color == shapes[i + 1].fill_color for i in range(n - 1)):
            for shape in shapes:
                shape.fill_color = random_color()

    positions = select_coordinates(n, 0.35)

    for i, shape in enumerate(shapes):
        shape.x, shape.y = positions[i]

    random.shuffle(shapes)

    arrow = Arrow(0.5, 0.5, 0.1, 0.05, "black", "none")
    diagram.arrow.append(arrow)

    x, y = shapes[0].x, shapes[0].y
    p = np.array([x, y])
    theta = random.uniform(0, 2 * math.pi)
    arrow_position = p + np.array([math.cos(theta), math.sin(theta)]) * 0.2
    arrow.x, arrow.y = arrow_position
    rotation = (theta + math.pi) * 180 / math.pi
    arrow.rotation = rotation

    if random.randint(0, 1):
        arrow.fill_color = random.choice(['black', random_color()])
        arrow.border_color = random.choice(['black', 'none'])
    else:
        arrow.fill_color = 'white'
        arrow.border_color = random.choice(['black', random_color()])

    diagram.entities.append(('color8', shapes))

def h_difference(h1, h2):
    return min(abs(h1 - h2), 360 - abs(h1 - h2))

def color9(diagram):
    n = 5
    rand = random.randint(0, 2)    # 0: same color, 1, 2: similar color

    rand2 = random.randint(0, 2)
    centers1 = [(0.5, 0.7), (0.2, 0.3), (0.4, 0.3), (0.6, 0.3), (0.8, 0.3)]
    centers2 = [(0.3, 0.5), (0.7, 0.8), (0.7, 0.6), (0.7, 0.4), (0.7, 0.2)]
    centers3 = [(0.1, 0.5), (0.5, 0.7), (0.9, 0.7), (0.5, 0.3), (0.9, 0.3)]
    centers = [centers1, centers2, centers3][rand2]

    s = random.uniform(0.3, 1)
    v = random.uniform(0.3, 1)

    base_color = random_hsv()[0], s, v

    colors = [base_color]
    h = (base_color[0] + random.uniform(-25, 25)) % 360 if rand else base_color[0]
    colors.append((h, s, v))

    for _ in range(n - 2):
        color = random_hsv()[0], s, v
        while h_difference(color[0], base_color[0]) < 90:
            color = random_hsv()[0], s, v
        colors.append(color)

    partial_colors = colors[1:]
    random.shuffle(partial_colors)
    colors = [colors[0]] + partial_colors
    index = np.argmin([h_difference(color[0], base_color[0]) for color in partial_colors])
    colors = [colorsys.hsv_to_rgb(h / 360, s, v) for h, s, v in colors]

    circles = [random_circle(diagram) for _ in range(n)]

    labels = random.choice([
        '1234',
        'ABCD',
        ['I', 'II', 'III', 'IV'],
        'abcd'
    ])

    for i, circle in enumerate(circles):
        circle.fill_color = colors[i]
        circle.border_color = 'none'
        circle.x = centers[i][0]
        circle.y = centers[i][1]
        circle.r = 0.1
        if i != 0:
            circle.label = labels[i - 1]

    diagram.entities.append(('color9', rand, labels[index], rand2))

def color10(diagram):
    n = random.randint(4, 8)

    positions = select_coordinates(n, 0.21)

    labels = random.choice([
        '12345678',
        'ABCDEFGH',
        ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'],
        'abcdefgh',
        random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 8)
    ])[:n]
    labels = list(labels)
    random.shuffle(labels)

    circles = [random_circle(diagram) for _ in range(n)]
    random.shuffle(circles)

    s = random.uniform(0.3, 1)
    v = random.uniform(0.3, 1)

    base_color = random_hsv()[0], s, v

    for i, circle in enumerate(circles):
        circle.border_color = 'none'
        circle.x, circle.y = positions[i]
        circle.r = 0.1
        circle.label = labels[i]
        if i == 0:
            h = random_hsv()[0]
            while h_difference(h, base_color[0]) < 90:
                h = random.uniform(0, 360)
            circle.fill_color = colorsys.hsv_to_rgb(h / 360, s, v)
        else:
            h = (base_color[0] + random.uniform(-20, 20)) % 360
            circle.fill_color = colorsys.hsv_to_rgb(h / 360, s, v)

    diagram.entities.append(('color10', labels[0]))

def random_cmap():
    all_cmaps = plt.colormaps()

    continuous_cmaps = [
        cmap for cmap in all_cmaps
        if not cmap.startswith(('tab', 'Pastel', 'Paired', 'Accent', 'Dark', 'Set'))
    ]

    return random.choice(continuous_cmaps)

def color11(diagram):
    coordinates = select_coordinates(4, 0.3)
    random.shuffle(coordinates)
    color_pool = random.sample(random.choice([color_list, weighted_color_list]), 6)
    labels = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)

    for i in range(4):
        point = random_point(diagram)
        point.x, point.y = coordinates[i]
        point.color = 'none'
        point.label = labels[i]

    colors = []
    line_lables = []

    for i in range(4):
        for j in range(i + 1, 4):
            color = color_pool.pop()
            colors.append(color)
            line = Line(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1], color)
            line_lables.append(labels[i] + labels[j])
            diagram.line.append(line)

    diagram.entities.append(('color11', colors, line_lables))

def color12(diagram):
    direction = random.choice(['horizontal', 'vertical'])
    if direction == 'horizontal':
        colorbar = Colorbar(0.5, 0.5, 1, 0.3, direction, random_cmap())
    else:
        colorbar = Colorbar(0.5, 0.5, 0.3, 1, direction, random_cmap())
    diagram.colorbar.append(colorbar)

    n = random.randint(1, 5)
    positions = [random.uniform(0.1, 0.9) for _ in range(n)]
    color = random.choice(['black', 'white'])

    for i in range(n):
        if direction == 'horizontal':
            x1, y1 = positions[i], 0.35
            x2, y2 = positions[i], 0.65
        else:
            x1, y1 = 0.35, positions[i]
            x2, y2 = 0.65, positions[i]

        line = Line(x1, y1, x2, y2, color)
        diagram.line.append(line)

    diagram.entities.append(('color12', n))

def color13(diagram):
    variation = random.randint(0, 1)    # 0: saturation, 1: value
    n = random.randint(3, 6)

    h = random.uniform(0, 360)
    shapes = [random_circle(diagram) for _ in range(n)]
    positions = select_coordinates(n, 0.2)

    random.shuffle(positions)

    labels = random.choice([
        '123456',
        'ABCDEF',
        ['I', 'II', 'III', 'IV', 'V', 'VI'],
    ])[:n]


    labels = list(labels)
    random.shuffle(labels)

    for i, shape in enumerate(shapes):
        shape.x, shape.y = positions[i]
        shape.r = 0.1
        shape.border_color = 'none'
        shape.label = labels[i]

    if variation == 0:
        v = random.uniform(0.3, 0.7)
        s1 = random.random()
        s2 = random.random()
        while abs(s1 - s2) < 0.4:
            s1 = random.random()
            s2 = random.random()
        shapes[0].fill_color = colorsys.hsv_to_rgb(h / 360, s1, v)
        for i in range(1, n):
            shapes[i].fill_color = colorsys.hsv_to_rgb(h / 360, s2, v)
    else:
        s = random.uniform(0.3, 0.7)
        v1 = random.uniform(0.2, 1)
        v2 = random.uniform(0.2, 1)
        while abs(v1 - v2) < 0.2:
            v1 = random.uniform(0.2, 1)
            v2 = random.uniform(0.2, 1)
        shapes[0].fill_color = colorsys.hsv_to_rgb(h / 360, s, v1)
        for i in range(1, n):
            shapes[i].fill_color = colorsys.hsv_to_rgb(h / 360, s, v2)

    diagram.entities.append(('color13', variation, labels[0]))
    

rules = [color1, color2_a, color2_b, color3, color5, color6, color7, color8, color9, color10, color11, color12, color13]
