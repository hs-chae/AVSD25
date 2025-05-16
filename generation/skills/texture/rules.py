import random
import math
import numpy as np

# texture_list = ['/', '\\', '|', '-', '+', 'x', 'o', '.', '//', 'oo', '..', 'xx', '\\\\', '||', '--', '++', '']
texture_list = ['///', 'ooo', '...', 'xxx', '\\\\\\', '|||', '---', '+++', '']

class Point:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

class Line:
    def __init__(self, start, end, style, color, label=""):
        self.start = start
        self.end = end
        self.style = style
        self.color = color
        self.label = label

    def points(self):
        return [
            [self.start.x, self.start.y],
            [self.end.x, self.end.y]
        ]

class Stair:
    def __init__(self, start, end, style, color, label=""):
        self.start = start
        self.end = end
        self.style = style
        self.color = color
        self.label = label

    def points(self):
        p1 = np.array([self.start.x, self.start.y])
        p2 = np.array([self.end.x, self.end.y])

        d = p2 - p1

        theta = np.arctan2(d[1], d[0]) + np.arctan2(2, 1)
        p3 = p1 + np.linalg.norm(d) / np.sqrt(5) * np.array([np.cos(theta), np.sin(theta)])

        theta = np.arctan2(d[1], d[0]) - np.arctan2(1, 2)
        p4 = p1 + 2 * np.linalg.norm(d) / np.sqrt(5) * np.array([np.cos(theta), np.sin(theta)])

        return [
            p1,
            (p1 + p4) / 2,
            (p1 + p2) / 2,
            (p2 + p3) / 2,
            p2
        ]
        
class Wave:
    def __init__(self, start, end, style, color, label="", amplitude=0.1, flip=False):
        self.start = start
        self.end = end
        self.style = style
        self.color = color
        self.label = label
        self.amplitude = amplitude
        self.flip = flip

    def points(self):
        p1 = np.array([self.start.x, self.start.y])
        p2 = np.array([self.end.x, self.end.y])

        d = p2 - p1

        # y = sin(2 * pi * x / d)
        x = np.linspace(0, np.linalg.norm(d), 100)
        y = np.sin(2 * np.pi * x / np.linalg.norm(d)) * self.amplitude * (1 if not self.flip else -1)

        points = np.concatenate([x[:, None], y[:, None]], axis=1)

        # Rotate
        theta = np.arctan2(d[1], d[0])

        R = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        points = points @ R.T

        # Translate
        points += p1

        return points

class Parabola:
    def __init__(self, start, end, style, color, label="", amplitude=0.2, flip=False):
        self.start = start
        self.end = end
        self.style = style
        self.color = color
        self.label = label
        self.amplitude = amplitude
        self.flip = flip

    def points(self):
        p1 = np.array([self.start.x, self.start.y])
        p2 = np.array([self.end.x, self.end.y])

        d = p2 - p1

        # y = a * x^2
        x = np.linspace(0, np.linalg.norm(d), 100)
        y = self.amplitude * x * (x - np.linalg.norm(d)) / np.linalg.norm(d)**2 * (1 if not self.flip else -1) * 4

        points = np.concatenate([x[:, None], y[:, None]], axis=1)

        # Rotate
        theta = np.arctan2(d[1], d[0])

        R = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        points = points @ R.T

        # Translate
        points += p1

        return points

class Polygon:
    def __init__(self, x, y, n, border_color, fill_color, size=0.1, label="", rotation=0, texture="", line_style="solid"):
        self.x = x
        self.y = y
        self.n = n
        self.border_color = border_color
        self.fill_color = fill_color
        self.size = size
        self.label = label
        self.rotation = rotation
        self.texture = texture
        self.line_style = line_style
    
    def points(self):
        if self.n == 4:
            rotation = self.rotation + 45
        else:
            rotation = self.rotation + 90
        rotation = math.radians(rotation)
        return [(self.x + self.size * math.cos(2 * math.pi * i / self.n + rotation), self.y + self.size * math.sin(2 * math.pi * i / self.n + rotation)) for i in range(self.n)]

class Circle:
    def __init__(self, x, y, r, border_color, fill_color, label="", texture="", line_style="solid"):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.texture = texture
        self.line_style = line_style

class Star:
    def __init__(self, x, y, r, border_color, fill_color, label="", n=5, texture="", line_style="solid"):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.n = n
        self.texture = texture
        self.line_style = line_style
    
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
    def __init__(self, x, y, r, border_color, fill_color, label="", texture="", line_style="solid"):
        self.x = x
        self.y = y
        self.r = r / 15
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.texture = texture
        self.line_style = line_style
    
    def points(self):
        return   [
            (
                self.x + self.r * (16 * math.sin(t)**3), 
                self.y + self.r * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))  # Reverse the sign
            )
            for t in [i * 2 * math.pi / 100 for i in range(100)]
        ]

class Diagram:
    def __init__(self, point=None, line=None, shape=None, entities=None):
        self.point = [] if point is None else point
        self.line = [] if line is None else line
        self.shape =  [] if shape is None else shape
        self.entities = [] if entities is None else entities

def random_pos():
    return random.random(), random.random()

def random_color():
    return random.choice(["red", "green", "blue", "yellow", "purple", "orange", "black", "pink", "gray", "brown", "cyan", "magenta"])

def random_color_except(color):
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "black", "pink", "white", "gray", "brown", "cyan", "magenta"]
    colors.remove(color)
    return random.choice(colors)

def random_colors(n):
    return random.sample(["red", "green", "blue", "yellow", "purple", "orange", "black", "pink"], n)

def random_colors_except(color, n):
    colors = ["red", "green", "blue", "yellow", "purple", "orange", "black", "pink"]
    colors.remove(color)
    return random.sample(colors, n)

def random_style():
    return random.choice(["solid", "dashed", "dotted", "dashdot"])

def random_capitals(n):
    return random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", n)

def random_lowercases(n):
    return random.sample("abcdefghijklmnopqrstuvwxyz", n)

def add_line(diagram, label=""):
    p1 = random_pos()
    p2 = random_pos()

    min_length = 0.1

    while ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) < min_length ** 2:
        p1 = random_pos()
        p2 = random_pos()
    
    Point1 = Point(p1[0], p1[1], "")
    Point2 = Point(p2[0], p2[1], "")

    diagram.point.append(Point1)
    diagram.point.append(Point2)

    style = random_style()
    color = random_color()

    l = Line(Point1, Point2, style, color, label)
    diagram.line.append(l)

    return l

def texture1(diagram):
    type = random.randint(0, 2)     # 0: label of line, 1: label of points, 2: color of line
    num_lines = random.randint(3, 6)

    rand1 = random.randint(0, 1)    # 0: same color, 1: different color
    rand2 = random.randint(0, 1)    # 0: parallel, 1: not parallel

    lines = []

    for _ in range(num_lines):
        lines.append(add_line(diagram))

    if type == 0:
        labels = random_lowercases(num_lines)
        for i in range(num_lines):
            lines[i].label = labels[i]

    elif type == 1:
        labels = random_capitals(num_lines * 2)
        for i in range(num_lines):
            lines[i].start.label = labels[i * 2]
            lines[i].end.label = labels[i * 2 + 1]
    else:
        colors = random_colors(num_lines)
        for i in range(num_lines):
            lines[i].color = colors[i]

    if rand1 == 0 and type != 2:
        color = random.choice(['black', random_color()])
        for i in range(0, num_lines):
            lines[i].color = color

    if rand2 == 0:
        vector = lines[0].end.x - lines[0].start.x, lines[0].end.y - lines[0].start.y
        for i in range(1, num_lines):
            lines[i].end.x = lines[i].start.x + vector[0]
            lines[i].end.y = lines[i].start.y + vector[1]
            if lines[i].end.x < 0:
                lines[i].end.x = 0
            if lines[i].end.x > 1:
                lines[i].end.x = 1
            if lines[i].end.y < 0:
                lines[i].end.y = 0
            if lines[i].end.y > 1:
                lines[i].end.y = 1

    style1 = random_style()
    style2 = random_style()

    while style1 == style2:
        style2 = random_style()

    lines[0].style = style1
    for i in range(1, num_lines):
        lines[i].style = style2
    
    diagram.entities.append(("texture1", lines, type))

def texture2(diagram):
    line = add_line(diagram)

    type = random.randint(0, 3)         # 0: label of line, 1: label of points, 2: color of line
    num_lines = random.randint(3, 6)

    rand1 = random.randint(0, 1)        # 0: same color, 1: different color
    rand2 = random.randint(0, 2)        # 0: not parallel, 1, 2: parallel

    lines = []

    for _ in range(num_lines):
        lines.append(add_line(diagram))
    
    if type == 0:
        labels = random_lowercases(num_lines + 1)
        for i in range(num_lines):
            lines[i].label = labels[i]
        line.label = labels[-1]
    elif type == 1:
        labels = random_capitals(num_lines * 2 + 2)
        for i in range(num_lines):
            lines[i].start.label = labels[i * 2]
            lines[i].end.label = labels[i * 2 + 1]
        line.start.label = labels[-2]
        line.end.label = labels[-1]
    elif type == 2:
        colors = random_colors(num_lines + 1)
        for i in range(num_lines):
            lines[i].color = colors[i]
        line.color = colors[-1]
    else:
        colors = random_colors(2)
        labels = list(range(1, num_lines + 1))
        random.shuffle(labels)
        for i in range(num_lines):
            lines[i].label = str(labels[i])
        line.color = colors[0]

    if rand1 == 0 and type != 2 or type == 3:
        color = random.choice(['black', random_color()])
        while color == line.color:
            color = random.choice(['black', random_color()])
        for i in range(num_lines):
            lines[i].color = color
    
    if rand2 == 0:
        vector = line.end.x - line.start.x, line.end.y - line.start.y
        for i in range(num_lines):
            lines[i].end.x = lines[i].start.x + vector[0]
            lines[i].end.y = lines[i].start.y + vector[1]
            if lines[i].end.x < 0:
                lines[i].end.x = 0
            if lines[i].end.x > 1:
                lines[i].end.x = 1
            if lines[i].end.y < 0:
                lines[i].end.y = 0
            if lines[i].end.y > 1:
                lines[i].end.y = 1

    style = random_style()
    while style == line.style:
        style = random_style()
    
    lines[0].style = line.style
    for i in range(1, num_lines):
        lines[i].style = style

    diagram.entities.append(("texture2", line, lines, type))

def texture3_a(diagram):
    shape = random.choice(["circle", "polygon"])
    centers1 = [(0.2, 0.5), (0.4, 0.5), (0.6, 0.5), (0.8, 0.5)]
    centers2 = [(0.5, 0.8), (0.5, 0.6), (0.5, 0.4), (0.5, 0.2)]
    centers3 = [(0.3, 0.7), (0.7, 0.7), (0.3, 0.3), (0.7, 0.3)]
    centers = random.choice([centers1, centers2, centers3])

    texture1, texture2 = random.sample(texture_list, 2)

    textures = [None, None, None, None]
    answer = random.randint(0, 3)
    for i in range(4):
        if i == answer:
            textures[i] = texture1
        else:
            textures[i] = texture2

    shapes = []

    if shape == "circle":
        r = random.uniform(0.05, 0.1)

        if random.randint(0, 1):
            for center, texture in zip(centers, textures):
                circle = Circle(center[0], center[1], r, 'black', random_color_except('black'), "", texture)
                shapes.append(circle)
        else:
            color = random_color_except('black')
            for center, texture in zip(centers, textures):
                circle = Circle(center[0], center[1], r, 'black', color, "", texture)
                shapes.append(circle)

    else:
        n = random.randint(3, 6)
        size = random.uniform(0.05, 0.1)

        if random.randint(0, 1):
            for center, texture in zip(centers, textures):
                polygon = Polygon(center[0], center[1], n, 'black', random_color_except('black'), size, "", 0, texture)
                shapes.append(polygon)
        else:
            color = random_color_except('black')
            for center, texture in zip(centers, textures):
                polygon = Polygon(center[0], center[1], n, 'black', color, size, "", 0, texture)
                shapes.append(polygon)

    labeling = random.randint(0, 2)    # 0: number, 1: alphabet, 2: color

    if labeling == 0:
        for i in range(4):
            shapes[i].label = str(i + 1)
        answer = str(answer + 1)
    elif labeling == 1:
        for i in range(4):
            shapes[i].label = chr(i + ord('A'))
        answer = chr(answer + ord('A'))
    else:
        colors = random_colors_except('black', 4)
        for i in range(4):
            shapes[i].fill_color = colors[i]
        answer = shapes[answer].fill_color

    diagram.shape.extend(shapes)
    diagram.entities.append(("texture3_a", answer, labeling))

def texture4(diagram):
    shape = random.choice(["circle", "polygon"])
    centers1 = [(0.5, 0.7), (0.2, 0.3), (0.4, 0.3), (0.6, 0.3), (0.8, 0.3)]
    centers2 = [(0.3, 0.5), (0.7, 0.8), (0.7, 0.6), (0.7, 0.4), (0.7, 0.2)]
    centers3 = [(0.1, 0.5), (0.5, 0.7), (0.9, 0.7), (0.5, 0.3), (0.9, 0.3)]
    centers = random.choice([centers1, centers2, centers3])

    rand = random.randint(0, 1)    # 0: choose same color, 1: choose different color

    shapes = []

    if shape == "circle":
        r = random.uniform(0.05, 0.1)
        for center in centers:
            circle = Circle(center[0], center[1], r, 'black', random_color_except('black'))
            shapes.append(circle)
            diagram.shape.append(circle)
    else:
        n = random.randint(3, 6)
        size = random.uniform(0.05, 0.1)
        for center in centers:
            polygon = Polygon(center[0], center[1], n, 'black', random_color_except('black'), size)
            shapes.append(polygon)
            diagram.shape.append(polygon)

    texture1, texture2 = random.sample(texture_list, 2)
    index = random.randint(1, 4)

    shapes[0].texture = texture1

    for j in range(1, 5):
        if rand == 0:
            shapes[j].texture = texture1 if j == index else texture2
        else:
            shapes[j].texture = texture1 if j != index else texture2

    if random.randint(0, 1):
        if random.randint(0, 1):
            for shape in shapes:
                shape.border_color = random_color_except('white')
                shape.fill_color = 'white'
        else:
            color = random_color_except('white')
            for shape in shapes:
                shape.border_color = color
                shape.fill_color = 'white'
    else:
        if random.randint(0, 1):
            color = random_color_except('black')
            for shape in shapes:
                shape.fill_color = color
            shapes[0].fill_color = random.choice([color, random_color_except('black')])

    labels = random.choice([
        '1234',
        'ABCD',
        ['I', 'II', 'III', 'IV'],
    ])

    for i in range(1, 5):
        shapes[i].label = labels[i - 1]

    diagram.entities.append(("texture4", index, rand, shapes))

def texture6(diagram):
    center = random_pos()
    center = (center[0] / 2 + 0.25, center[1] / 2 + 0.25)
    radius = random.random() / 3 + 0.1
    n = random.randint(3, 6)

    rotation = random.choice([0, random.random() * 2 * math.pi])

    positions = [(
        center[0] - radius * math.sin(2 * math.pi * i / n + rotation),
        center[1] + radius * math.cos(2 * math.pi * i / n + rotation)
    ) for i in range(n)]

    points = []
    lines = []

    for i in range(n):
        points.append(Point(positions[i][0], positions[i][1], ""))
    
    for i in range(n):
        lines.append(Line(points[i], points[(i + 1) % n], random_style(), random_color(), ""))

    if random.randint(0, 1):
        for line in lines:
            line.color = 'black'

    label_type = random.randint(0, 1)   # 0: label of line, 1: label of points
    if label_type == 0:
        labels = random_lowercases(n)
        for i in range(n):
            lines[i].label = labels[i]
    else:
        labels = random_capitals(n)
        for i in range(n):
            points[i].label = labels[i]
    
    diagram.point.extend(points)
    diagram.line.extend(lines)
    diagram.entities.append(("texture6", lines, label_type))

def texture7(diagram):
    p1 = random_pos()
    p2 = random_pos()

    min_length = 0.7
    while ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) < min_length ** 2:
        p1 = random_pos()
        p2 = random_pos()

    interval = random.randint(2, 5)

    t = [random.random() for _ in range(interval)]
    sum_t = sum(t)
    t = [i / sum_t for i in t]
    while min(t) < 0.1:
        t = [random.random() for _ in range(interval)]
        sum_t = sum(t)
        t = [i / sum_t for i in t]

    acc = 0
    for i in range(interval):
        acc += t[i]
        t[i] = acc

    points = [Point(p1[0], p1[1], "")]
    for i in range(interval):
        points.append(Point(p1[0] + (p2[0] - p1[0]) * t[i], p1[1] + (p2[1] - p1[1]) * t[i], ""))

    lines = []
    style_previous = "dummy"
    for i in range(interval):
        lines.append(Line(points[i], points[i + 1], random_style(), random_color(), ""))
        while lines[i].style == style_previous or lines[i].style == "dashdot":
            lines[i].style = random_style()
        style_previous = lines[i].style

    color = random.choice(['black', random_color()])
    
    for i in range(interval + 1):
        diagram.point.append(points[i])

    for i in range(interval):
        lines[i].color = color
        diagram.line.append(lines[i])

    diagram.entities.append(("texture7", interval))

def sample_geometric_with_noise(m, start, end, noise_factor=0.1):
    # Generate geometric sequence
    geo_sequence = np.geomspace(start, end, m)
    # Add random noise
    noise = np.random.uniform(-noise_factor, noise_factor, m) * geo_sequence
    return geo_sequence + noise

def texture8(diagram):
    rand = random.randint(0, 2)     # 0: random, 1: parallel (tilted), 2: parallel (horizontal/vertical)
    n = random.randint(3, 6)

    labels = random.choice(['123456', random.choice([
        'ABCDEF',
        'abcdef',
        ['I', 'II', 'III', 'IV', 'V', 'VI'],
        ['i', 'ii', 'iii', 'iv', 'v', 'vi']
    ])])[:n]

    lines = [add_line(diagram, labels[i]) for i in range(n)]

    if rand == 1:
        a = math.tan(random.random() * 2 * math.pi)

        if a >= 0:
            p = [(a / (a + 1) * i / (n + 1), 1 / (a + 1) * (n - i) / (n + 1)) for i in range(1, n + 1)]
        else:
            p = [(1 / (1 - a) + i / (n + 1) * (-a) / (1 - a), i / (n + 1) / (1 - a)) for i in range(1, n + 1)]
        
        if random.randint(0, 1):
            p.reverse()

        for i in range(n):
            lines[i].start.x = p[i][0]
            lines[i].start.y = p[i][1]
            lines[i].end.x = 1 - p[n - i - 1][0]
            lines[i].end.y = 1 - p[n - i - 1][1]
    elif rand == 2:
        if random.randint(0, 1):
            for i in range(n):
                lines[i].start.x = 0.2
                lines[i].start.y = (n - i) / (n + 1)
                lines[i].end.x = 0.8
                lines[i].end.y = (n - i) / (n + 1)
        else:
            for i in range(n):
                lines[i].start.x = (i + 1) / (n + 1)
                lines[i].start.y = 0.2
                lines[i].end.x = (i + 1) / (n + 1)
                lines[i].end.y = 0.8

    density = sample_geometric_with_noise(n, 0.15, 1)
    random.shuffle(density)

    for i in range(n):
        lines[i].style = density[i]

    diagram.entities.append(("texture8", labels, density))

def texture9(diagram):
    n = random.randint(4, 6)
    m = random.randint(1, 4)

    style_pool = random.sample(["solid", "dashed", "dotted", "dashdot"], m)
    styles = style_pool + random.choices(style_pool, k = n - m)
    color = random.choice(['black', random_color()])

    lines = [add_line(diagram) for _ in range(n)]

    for i in range(n):
        lines[i].style = styles[i]
        lines[i].color = color

    diagram.entities.append(("texture9", styles, m))

def texture10(diagram):
    n = random.randint(4, 6)
    m = random.randint(1, n)

    style = random_style()
    style_pool = list({"solid", "dashed", "dotted", "dashdot"} - {style})
    styles = [style] * m + random.choices(style_pool, k = n - m)
    color = random.choice(['black', random_color()])

    lines = [add_line(diagram) for _ in range(n)]

    for i in range(n):
        lines[i].style = styles[i]
        lines[i].color = color

    diagram.entities.append(("texture10", styles, m, style))

def texture11(diagram):
    n = random.randint(3, 4)

    shape_list = ["circle", "triangle", "square", "pentagon", "hexagon", "star", "heart"]
    shapes = random.sample(shape_list, n)
    string_shapes = shapes.copy()
    styles = random.sample(["solid", "dashed", "dotted", "dashdot"], n)

    random_size = lambda: random.uniform(0.1, 0.2)

    one_different = random.choice([True, False])

    if one_different:
        for i in range(2, n):
            styles[i] = styles[1]

    for i in range(n):
        if shapes[i] == 'circle':
            circle = Circle(random_pos()[0], random_pos()[1], random_size(), random_color(), 'none', line_style=styles[i])
            shapes[i] = circle
        elif shapes[i] == 'triangle':
            triangle = Polygon(random_pos()[0], random_pos()[1], 3, random_color(), 'none', random_size(), line_style=styles[i])
            shapes[i] = triangle
        elif shapes[i] == 'square':
            square = Polygon(random_pos()[0], random_pos()[1], 4, random_color(), 'none', random_size(), line_style=styles[i])
            shapes[i] = square
        elif shapes[i] == 'pentagon':
            pentagon = Polygon(random_pos()[0], random_pos()[1], 5, random_color(), 'none', random_size(), line_style=styles[i])
            shapes[i] = pentagon
        elif shapes[i] == 'hexagon':
            hexagon = Polygon(random_pos()[0], random_pos()[1], 6, random_color(), 'none', random_size(), line_style=styles[i])
            shapes[i] = hexagon
        elif shapes[i] == 'star':
            star = Star(random_pos()[0], random_pos()[1], random_size(), random_color(), 'none', line_style=styles[i])
            shapes[i] = star
        else:
            heart = Heart(random_pos()[0], random_pos()[1], random_size(), random_color(), 'none', line_style=styles[i])
            shapes[i] = heart

    diagram.shape.extend(shapes)

    diagram.entities.append(("texture11", string_shapes, one_different, styles))

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
    outer_attempts = 0

    while outer_attempts < 10000:
        selected_points = []
        attempts = 0
        while len(selected_points) < n and attempts < 10000:
            new_point = (random.uniform(0, 1), random.uniform(0, 1))
            if is_valid_point(new_point, selected_points, d):
                selected_points.append(new_point)
            attempts += 1
        if len(selected_points) == n:
            break
        outer_attempts += 1

    if outer_attempts == 10000:
        print("Warning: select_coordinates failed to find valid coordinates.")
    
    return selected_points

def texture12(diagram):
    m = random.randint(3, 5)
    n = random.randint(m + 1, 6)

    thetas = np.array([random.uniform(0.5, 1) for _ in range(n)])
    thetas /= thetas.sum()
    thetas *= 2 * np.pi
    start = random.uniform(0, 2 * np.pi)
    # accumulate theta
    thetas = np.cumsum(thetas) + start
    index_theta = [(i, thetas[i]) for i in range(n)]
    
    # random.shuffle(index_theta)
    thetas = [index_theta[i][1] for i in range(n)]
    indices = [index_theta[i][0] for i in range(n)]
    
    positions = [(0.5 + 0.4 * np.cos(theta), 0.5 + 0.4 * np.sin(theta)) for theta in thetas]

    points = []

    for i in range(n):
        points.append(Point(positions[i][0], positions[i][1], ""))

    diagram.point.extend(points)

    lines = []
    style = random_style()

    another_style = random_style()

    while another_style == style:
        another_style = random_style()

    indices = random.sample(indices, m)
    indices.sort()

    for i in range(n):
        for j in range(i + 1, n):
            lines.append(Line(points[i], points[j], style, 'black', ""))

    for i in range(m):
        i1, i2 = indices[i], indices[(i + 1) % m]
        if i1 > i2:
            i1, i2 = i2, i1
        line_index = i1 * (2 * n - i1 - 1) // 2 + i2 - i1 - 1
        lines[line_index].style = another_style

    diagram.line.extend(lines)

    diagram.entities.append(("texture12", m, another_style))

def texture13(diagram):
    n = random.randint(3, 5)
    lines = []

    positions = select_coordinates(n * 2, 0.1)
    random.shuffle(positions)

    for i in range(n):
        point1 = Point(*positions[2 * i], "")
        point2 = Point(*positions[2 * i + 1], "")

        l_type = random.choice([Line, Stair, Wave, Parabola])

        if l_type == Line or l_type == Stair:
            l = l_type(point1, point2, random_style(), random_color())
        else:
            l = l_type(point1, point2, random_style(), random_color(), flip=random.choice([True, False]))

        lines.append(l)

        diagram.point.append(point1)
        diagram.point.append(point2)
    
    diagram.line.extend(lines)

    rand = random.randint(0, 2)

    if rand == 1:
        a = math.tan(random.random() * 2 * math.pi)

        if a >= 0:
            p = [(a / (a + 1) * i / (n + 1), 1 / (a + 1) * (n - i) / (n + 1)) for i in range(1, n + 1)]
        else:
            p = [(1 / (1 - a) + i / (n + 1) * (-a) / (1 - a), i / (n + 1) / (1 - a)) for i in range(1, n + 1)]
        
        if random.randint(0, 1):
            p.reverse()

        for i in range(n):
            lines[i].start.x = p[i][0]
            lines[i].start.y = p[i][1]
            lines[i].end.x = 1 - p[n - i - 1][0]
            lines[i].end.y = 1 - p[n - i - 1][1]
    elif rand == 2:
        if random.randint(0, 1):
            for i in range(n):
                lines[i].start.x = 0.2
                lines[i].start.y = (n - i) / (n + 1)
                lines[i].end.x = 0.8
                lines[i].end.y = (n - i) / (n + 1)
        else:
            for i in range(n):
                lines[i].start.x = (i + 1) / (n + 1)
                lines[i].start.y = 0.2
                lines[i].end.x = (i + 1) / (n + 1)
                lines[i].end.y = 0.8

    labeling = random.randint(0, 2)    # 0: line, 1: points, 2: color

    if labeling == 0:
        labels = random.choice([random_lowercases(n), range(1, n + 1)])
        for i in range(n):
            lines[i].label = str(labels[i])
    elif labeling == 1:
        labels = random_capitals(n * 2)
        for i in range(n):
            lines[i].start.label = labels[2 * i]
            lines[i].end.label = labels[2 * i + 1]
    else:
        colors = random_colors(n)
        for i in range(n):
            lines[i].color = colors[i]

    diagram.entities.append(("texture13", labeling, lines))
    
def texture14(diagram):
    n = random.randint(3, 5)
    lines = []

    positions = select_coordinates(n * 2, 0.1)
    random.shuffle(positions)

    answer_style = random_style()
    styles = [answer_style] 

    for i in range(n - 1):
        style = random_style()
        while style == answer_style:
            style = random_style()
        styles.append(style)

    random.shuffle(styles)
    answer_index = styles.index(answer_style)

    for i in range(n):
        point1 = Point(*positions[2 * i], "")
        point2 = Point(*positions[2 * i + 1], "")

        l_type = random.choice([Line, Stair, Wave, Parabola])

        if l_type == Line or l_type == Stair:
            l = l_type(point1, point2, styles[i], random_color())
        else:
            l = l_type(point1, point2, styles[i], random_color(), flip=random.choice([True, False]))

        lines.append(l)

        diagram.point.append(point1)
        diagram.point.append(point2)
    
    diagram.line.extend(lines)

    rand = random.randint(0, 2)

    if rand == 1:
        a = math.tan(random.random() * 2 * math.pi)

        if a >= 0:
            p = [(a / (a + 1) * i / (n + 1), 1 / (a + 1) * (n - i) / (n + 1)) for i in range(1, n + 1)]
        else:
            p = [(1 / (1 - a) + i / (n + 1) * (-a) / (1 - a), i / (n + 1) / (1 - a)) for i in range(1, n + 1)]
        
        if random.randint(0, 1):
            p.reverse()

        for i in range(n):
            lines[i].start.x = p[i][0]
            lines[i].start.y = p[i][1]
            lines[i].end.x = 1 - p[n - i - 1][0]
            lines[i].end.y = 1 - p[n - i - 1][1]
    elif rand == 2:
        if random.randint(0, 1):
            for i in range(n):
                lines[i].start.x = 0.2
                lines[i].start.y = (n - i) / (n + 1)
                lines[i].end.x = 0.8
                lines[i].end.y = (n - i) / (n + 1)
        else:
            for i in range(n):
                lines[i].start.x = (i + 1) / (n + 1)
                lines[i].start.y = 0.2
                lines[i].end.x = (i + 1) / (n + 1)
                lines[i].end.y = 0.8

    labeling = random.randint(0, 2)    # 0: line, 1: points, 2: color

    if labeling == 0:
        labels = random.choice([random_lowercases(n), range(1, n + 1)])
        for i in range(n):
            lines[i].label = str(labels[i])
        answer = str(labels[answer_index])
    elif labeling == 1:
        labels = random_capitals(n * 2)
        for i in range(n):
            lines[i].start.label = labels[2 * i]
            lines[i].end.label = labels[2 * i + 1]
        answer = labels[2 * answer_index] + labels[2 * answer_index + 1]
    else:
        colors = random_colors(n)
        for i in range(n):
            lines[i].color = colors[i]
        answer = colors[answer_index]

    diagram.entities.append(("texture14", answer, labeling, lines, answer_style))

def texture15(diagram):
    n = random.randint(3, 5)
    lines = []

    positions = select_coordinates(n * 2, 0.1)
    random.shuffle(positions)

    answer_style = random_style()
    styles = [answer_style] 
    another_style = random_style()
    while another_style == answer_style:
        another_style = random_style()

    for i in range(n - 1):
        styles.append(another_style)

    random.shuffle(styles)
    answer_index = styles.index(answer_style)

    for i in range(n):
        point1 = Point(*positions[2 * i], "")
        point2 = Point(*positions[2 * i + 1], "")

        l_type = random.choice([Line, Stair, Wave, Parabola])

        if l_type == Line or l_type == Stair:
            l = l_type(point1, point2, styles[i], random_color())
        else:
            l = l_type(point1, point2, styles[i], random_color(), flip=random.choice([True, False]))

        lines.append(l)

        diagram.point.append(point1)
        diagram.point.append(point2)
    
    diagram.line.extend(lines)

    rand = random.randint(0, 2)

    if rand == 1:
        a = math.tan(random.random() * 2 * math.pi)

        if a >= 0:
            p = [(a / (a + 1) * i / (n + 1), 1 / (a + 1) * (n - i) / (n + 1)) for i in range(1, n + 1)]
        else:
            p = [(1 / (1 - a) + i / (n + 1) * (-a) / (1 - a), i / (n + 1) / (1 - a)) for i in range(1, n + 1)]
        
        if random.randint(0, 1):
            p.reverse()

        for i in range(n):
            lines[i].start.x = p[i][0]
            lines[i].start.y = p[i][1]
            lines[i].end.x = 1 - p[n - i - 1][0]
            lines[i].end.y = 1 - p[n - i - 1][1]
    elif rand == 2:
        if random.randint(0, 1):
            for i in range(n):
                lines[i].start.x = 0.2
                lines[i].start.y = (n - i) / (n + 1)
                lines[i].end.x = 0.8
                lines[i].end.y = (n - i) / (n + 1)
        else:
            for i in range(n):
                lines[i].start.x = (i + 1) / (n + 1)
                lines[i].start.y = 0.2
                lines[i].end.x = (i + 1) / (n + 1)
                lines[i].end.y = 0.8

    labeling = random.randint(0, 2)    # 0: line, 1: points, 2: color

    if labeling == 0:
        labels = random.choice([random_lowercases(n), range(1, n + 1)])
        for i in range(n):
            lines[i].label = str(labels[i])
        answer = str(labels[answer_index])
    elif labeling == 1:
        labels = random_capitals(n * 2)
        for i in range(n):
            lines[i].start.label = labels[2 * i]
            lines[i].end.label = labels[2 * i + 1]
        answer = labels[2 * answer_index] + labels[2 * answer_index + 1]
    else:
        colors = random_colors(n)
        for i in range(n):
            lines[i].color = colors[i]
        answer = colors[answer_index]

    diagram.entities.append(("texture15", answer, labeling, lines))


rules = [texture1, texture2, texture3_a, texture4, texture6, texture7, texture8, texture9, texture10, texture11, texture12, texture13, texture14, texture15]
