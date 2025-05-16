import random
import math
import nltk
import nltk.corpus as corpus
import numpy as np
nltk.download('words', quiet=True)

class Point:
    def __init__(self, x, y, label="", o=False):
        self.x = x
        self.y = y
        self.label = label
        self.o = o

class Line:
    def __init__(self, p1, p2, color='black', infinite=False, label="", symbol="", symbol_color='black'):
        self.p1 = p1
        self.p2 = p2
        self.infinite = infinite
        self.color = color
        self.label = label
        self.symbol = symbol
        self.symbol_color = symbol_color

class Circle:
    def __init__(self, center, radius, color='black', label=""):
        self.center = center
        self.radius = radius
        self.color = color
        self.label = label

class Angle:
    def __init__(self, l1, l2, color='black', symbol=""):
        self.l1 = l1
        self.l2 = l2
        self.color = color
        self.symbol = symbol

class Perpendicular:
    def __init__(self, l1, l2, color='black'):
        self.l1 = l1
        self.l2 = l2
        self.color = color

class Text:
    def __init__(self, x, y, text, color='black'):
        self.x = x
        self.y = y
        self.text = text
        self.color = color

class TextBox:
    def __init__(self, x, y, text, border_color='black', fill_color='none'):
        self.x = x
        self.y = y
        self.text = text
        self.border_color = border_color
        self.fill_color = fill_color

class Check:
    def __init__(self, x, y, correct):
        self.x = x
        self.y = y
        self.correct = correct

class OX:
    def __init__(self, x, y, correct):
        self.x = x
        self.y = y
        self.correct = correct

class Diagram:
    def __init__(self):
        self.points = []
        self.lines = []
        self.circles = []
        self.angles = []
        self.perpendiculars = []
        self.text = []
        self.textboxes = []
        self.checks = []
        self.oxs = []
        self.entities = []

def random_word():
    return random.choice(corpus.words.words())

def random_position():
    return random.random(), random.random()

def random_radius():
    return random.random() * 0.5

color_list = ['black', 'red', 'blue', 'green', 'yellow', 'purple', 'orange']

def random_color():
    return random.choice(color_list)

def sample_colors(n):
    return random.sample(color_list, n)

def random_capitals(n):
    return random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", n)

def random_lowercases(n):
    return random.sample("abcdefghijklmnopqrstuvwxyz", n)

def random_point(diagram):
    p = Point(*random_position())
    diagram.points.append(p)
    return p

def random_line(diagram):
    p1 = random_point(diagram)
    p2 = random_point(diagram)
    l = Line(p1, p2)
    diagram.lines.append(l)
    return l

def random_line_with_point(diagram, point):
    p = random_point(diagram)
    l = Line(point, p)
    diagram.lines.append(l)
    return l

def random_circle(diagram):
    center = random_point(diagram)
    radius = random_radius()
    c = Circle(center, radius)
    diagram.circles.append(c)
    return c

def random_circle_with_center(diagram, center):
    radius = random.random()
    c = Circle(center, radius)
    diagram.circles.append(c)
    return c

def random_angle(diagram):
    center = random_point(diagram)
    p1 = random_point(diagram)
    p2 = random_point(diagram)

    l1 = Line(center, p1)
    l2 = Line(center, p2)
    diagram.lines.append(l1)
    diagram.lines.append(l2)

    angle = Angle(l1, l2, 'black')
    diagram.angles.append(angle)

    return l1, l2, angle

def not_in_line(p, line):
    x1, y1 = line.p1.x, line.p1.y
    x2, y2 = line.p2.x, line.p2.y
    x, y = p

    if x < min(x1, x2) or x > max(x1, x2) or y < min(y1, y2) or y > max(y1, y2):
        return True

def random_intersecting_lines_with_angle(diagram):
    l1 = random_line(diagram)
    l2 = random_line(diagram)

    # get the intersection point
    x1, y1 = l1.p1.x, l1.p1.y
    x2, y2 = l1.p2.x, l1.p2.y
    x3, y3 = l2.p1.x, l2.p1.y
    x4, y4 = l2.p2.x, l2.p2.y

    x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
    y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))

    if x < 0 or x > 1 or y < 0 or y > 1 or not_in_line((x, y), l1) or not_in_line((x, y), l2):
        diagram.lines.remove(l1)
        diagram.lines.remove(l2)
        return random_intersecting_lines_with_angle(diagram)
    else:
        angle = Angle(l1, l2, 'black')
        diagram.angles.append(angle)
        return l1, l2, angle

def random_perpendicular(diagram):
    l1 = random_line(diagram)
    x1, y1 = l1.p1.x, l1.p1.y
    x2, y2 = l1.p2.x, l1.p2.y
    t = random.random()

    t = 0.2 + t * 0.6

    p = Point(x1 + t*(x2-x1), y1 + t*(y2-y1))
    l2 = Line(p, Point(p.x + y2 - y1, p.y + x1 - x2))
    diagram.lines.append(l2)

    perpendicular = Perpendicular(l1, l2)
    diagram.perpendiculars.append(perpendicular)

    return l1, l2, perpendicular

def add_angle(diagram, l1, l2):
    angle = Angle(l1, l2, 'black')
    diagram.angles.append(angle)
    return angle

def polygon_on_circle(diagram, circle):
    n = random.randint(3, 6)
    points = []
    for i in range(n):
        theta = random.random() * 2 * math.pi
        x = circle.center.x + circle.radius * math.cos(theta)
        y = circle.center.y + circle.radius * math.sin(theta)
        points.append((theta, Point(x, y)))
        diagram.points.append(points[-1][1])
    
    points.sort()
    points = [p[1] for p in points]

    for i in range(n):
        diagram.lines.append(Line(points[i], points[(i+1)%n]))

    return points

def random_triangle(diagram):
    p1 = random_point(diagram)
    p2 = random_point(diagram)
    p3 = random_point(diagram)

    # calculate the size of the triangle
    a = math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    b = math.sqrt((p2.x-p3.x)**2 + (p2.y-p3.y)**2)
    c = math.sqrt((p3.x-p1.x)**2 + (p3.y-p1.y)**2)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    if area < 0.1:
        diagram.points.remove(p1)
        diagram.points.remove(p2)
        diagram.points.remove(p3)
        return random_triangle(diagram)

    diagram.lines.append(Line(p1, p2))
    diagram.lines.append(Line(p2, p3))
    diagram.lines.append(Line(p3, p1))
    return p1, p2, p3

def random_text(diagram):
    x, y = random_position()
    text = random_word()
    color = random_color()
    t = Text(x, y, text, color)
    diagram.text.append(t)
    return t

def symbol_1_a(diagram):
    p1, p2, p3 = random_triangle(diagram)
    angle = add_angle(diagram, diagram.lines[-1], diagram.lines[-2])
    
    labels = random_capitals(3)
    p1.label = labels[0]
    p2.label = labels[1]
    p3.label = labels[2]

    line_color = random_color()
    for line in diagram.lines:
        line.color = line_color

    angle.color = random_color()

    diagram.entities.append(("symbol_1_a", p1, p2, p3))

def symbol_1_b(diagram):
    l1, l2, angle = random.choice([random_angle, random_intersecting_lines_with_angle])(diagram)

    num_dummies = random.randint(1, 3)

    for _ in range(num_dummies):
        rand = random.choice([0, 1, 2])

        if rand == 0:
            random_line(diagram)
        elif rand == 1:
            random_line_with_point(diagram, random.choice(diagram.points))
        else:
            random_circle(diagram)

    labels = random_lowercases(len(diagram.lines))
    line_color = random_color()

    for i, line in enumerate(diagram.lines):
        line.infinite = True
        line.color = line_color
        line.label = labels[i]

    angle.color = random_color()

    diagram.entities.append(("symbol_1_b", l1, l2))

def intersecting(line1, line2):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        return 0 if val == 0 else (1 if val > 0 else 2)

    def on_segment(p, q, r):
        return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

    def do_intersect(p1, q1, p2, q2):
        o1, o2 = orientation(p1, q1, p2), orientation(p1, q1, q2)
        o3, o4 = orientation(p2, q2, p1), orientation(p2, q2, q1)
        if o1 != o2 and o3 != o4:
            return True
        return (o1 == 0 and on_segment(p1, p2, q1)) or (o2 == 0 and on_segment(p1, q2, q1)) or \
            (o3 == 0 and on_segment(p2, p1, q2)) or (o4 == 0 and on_segment(p2, q1, q2))

    x1, y1 = line1.p1.x, line1.p1.y
    x2, y2 = line1.p2.x, line1.p2.y
    x3, y3 = line2.p1.x, line2.p1.y
    x4, y4 = line2.p2.x, line2.p2.y

    return do_intersect((x1, y1), (x2, y2), (x3, y3), (x4, y4))

def symbol_1_c(diagram):
    l1, l2, angle = random_perpendicular(diagram)
    l1.infinite = True
    l2.infinite = True

    lines = [l1, l2]

    num_dummies = random.randint(1, 3)

    for _ in range(num_dummies):
        rand = random.choice([0, 1, 2])

        if rand == 0:
            l = random_line(diagram)
            lines.append(l)
            l.infinite = True
        elif rand == 1:
            l = random_line_with_point(diagram, random.choice(diagram.points))
            lines.append(l)
            l.infinite = True
        else:
            random_circle(diagram)

    dummy_angles = []

    for i, line1 in enumerate(diagram.lines):
        for line2 in diagram.lines[i+1:]:
            if intersecting(line1, line2) and not ((l1 == line1 and l2 == line2) or (l1 == line2 and l2 == line1)):
                dummy_angles.append(add_angle(diagram, line1, line2))

    type = random.choice(['color', 'label'])

    if 1 + len(dummy_angles) > len(color_list):
        type = 'label'

    if type == 'color':
        colors = sample_colors(1 + len(dummy_angles))
        angle.color = colors[-1]

        for i, angle in enumerate(dummy_angles):
            angle.color = colors[i]
    else:
        colors = []
        color = random_color()
        angle.color = color
        for angle in dummy_angles:
            angle.color = color
        labels = random_lowercases(len(lines))
        for i, line in enumerate(lines):
            line.label = labels[i]

    diagram.entities.append(("symbol_1_c", type, colors, l1, l2))

def symbol_2_a(diagram):
    n = random.randint(3, 5)
    texts = [random_text(diagram) for _ in range(n)]
    correct = random.randint(0, n-1)
    symbol_class = random.choice([Check, OX])

    text_x, symbol_x = random.choice([(0.3, 0.65), (0.45, 0.35)])

    symbols = [symbol_class(symbol_x, i / (n+1), i == correct) for i in range(n)]

    positions = [(text_x, i / (n+1)) for i in range(n)]
    for i, text in enumerate(texts):
        text.x = positions[i][0]
        text.y = positions[i][1]

    if symbol_class == Check:
        diagram.checks.extend(symbols)
    elif symbol_class == OX:
        diagram.oxs.extend(symbols)

    words = [text.text for text in texts]

    diagram.entities.append(("symbol_2_a", words, correct))

def symbol_2_b(diagram):
    n = random.randint(3, 5)
    words = [random_word() for _ in range(n)]
    correct = random.randint(0, n-1)

    color = random_color()

    for i in range(n):
        x, y = 0.2, i / (n+1)
        if i == correct:
            tb = TextBox(x, y, words[i], color)
            diagram.textboxes.append(tb)
        else:
            t = Text(x, y, words[i])
            diagram.text.append(t)

    answer = words[correct]

    diagram.entities.append(("symbol_2_b", color, answer))

def symbol3_a(diagram):
    l1 = random_line(diagram)
    l2 = random_line(diagram)

    lines = [l1, l2]
    rand = random.randint(1, 2)
    n = 2

    l1.symbol = random.choice(['>', '>>'])
    l2.symbol = l1.symbol

    l1.symbol_color = random_color()
    l2.symbol_color = l1.symbol_color

    if rand == 1:
        a = math.tan(random.random() * 2 * math.pi)

        if a >= 0:
            p = [(a / (a + 1) * i / (n + 1), 1 / (a + 1) * (n - i) / (n + 1)) for i in range(1, n + 1)]
        else:
            p = [(1 / (1 - a) + i / (n + 1) * (-a) / (1 - a), i / (n + 1) / (1 - a)) for i in range(1, n + 1)]
        
        if random.randint(0, 1):
            p.reverse()

        for i in range(n):
            lines[i].p1.x = p[i][0]
            lines[i].p1.y = p[i][1]
            lines[i].p2.x = 1 - p[n - i - 1][0]
            lines[i].p2.y = 1 - p[n - i - 1][1]
    elif rand == 2:
        if random.randint(0, 1):
            for i in range(n):
                lines[i].p1.x = 0.2
                lines[i].p1.y = (n - i) / (n + 1)
                lines[i].p2.x = 0.8
                lines[i].p2.y = (n - i) / (n + 1)
        else:
            for i in range(n):
                lines[i].p1.x = (i + 1) / (n + 1)
                lines[i].p1.y = 0.2
                lines[i].p2.x = (i + 1) / (n + 1)
                lines[i].p2.y = 0.8

    if random.randint(0, 1):
        l1.p1, l1.p2 = l1.p2, l1.p1
        l2.p1, l2.p2 = l2.p2, l2.p1

    diagram.entities.append(("symbol3_a", l1.symbol_color))

def symbol3_b(diagram):
    l1 = random_line(diagram)
    l2 = random_line(diagram)

    lines = [l1, l2]
    rand = random.randint(1, 2)
    n = 2

    l1.symbol = random.choice(['|', '||', '|||'])
    l2.symbol = l1.symbol

    l1.symbol_color = random_color()
    l2.symbol_color = l1.symbol_color

    if rand == 1:
        a = math.tan(random.random() * 2 * math.pi)

        if a >= 0:
            p = [(a / (a + 1) * i / (n + 1), 1 / (a + 1) * (n - i) / (n + 1)) for i in range(1, n + 1)]
        else:
            p = [(1 / (1 - a) + i / (n + 1) * (-a) / (1 - a), i / (n + 1) / (1 - a)) for i in range(1, n + 1)]
        
        if random.randint(0, 1):
            p.reverse()

        for i in range(n):
            lines[i].p1.x = p[i][0]
            lines[i].p1.y = p[i][1]
            lines[i].p2.x = 1 - p[n - i - 1][0]
            lines[i].p2.y = 1 - p[n - i - 1][1]
    elif rand == 2:
        if random.randint(0, 1):
            for i in range(n):
                lines[i].p1.x = 0.2
                lines[i].p1.y = (n - i) / (n + 1)
                lines[i].p2.x = 0.8
                lines[i].p2.y = (n - i) / (n + 1)
        else:
            for i in range(n):
                lines[i].p1.x = (i + 1) / (n + 1)
                lines[i].p1.y = 0.2
                lines[i].p2.x = (i + 1) / (n + 1)
                lines[i].p2.y = 0.8

    if random.randint(0, 1):
        l1.p1, l1.p2 = l1.p2, l1.p1
        l2.p1, l2.p2 = l2.p2, l2.p1

    diagram.entities.append(("symbol3_b", l1.symbol_color))

def symbol4_a(diagram):
    n = random.randint(3, 4)
    lines = [random_line(diagram) for _ in range(n)]

    # make lines[0] and lines[1] have the same length
    a = math.sqrt((lines[0].p1.x - lines[0].p2.x)**2 + (lines[0].p1.y - lines[0].p2.y)**2)
    b = math.sqrt((lines[1].p1.x - lines[1].p2.x)**2 + (lines[1].p1.y - lines[1].p2.y)**2)
    lines[1].p2.x = lines[1].p1.x + (lines[1].p2.x - lines[1].p1.x) * a / b
    lines[1].p2.y = lines[1].p1.y + (lines[1].p2.y - lines[1].p1.y) * a / b

    while lines[1].p2.x > 1 or lines[1].p2.x < 0 or lines[1].p2.y > 1 or lines[1].p2.y < 0:
        lines[1].p1.x, lines[1].p1.y = random.uniform(0, 1), random.uniform(0, 1)
        lines[1].p2.x, lines[1].p2.y = random.uniform(0, 1), random.uniform(0, 1)
        b = math.sqrt((lines[1].p1.x - lines[1].p2.x)**2 + (lines[1].p1.y - lines[1].p2.y)**2)
        lines[1].p2.x = lines[1].p1.x + (lines[1].p2.x - lines[1].p1.x) * a / b
        lines[1].p2.y = lines[1].p1.y + (lines[1].p2.y - lines[1].p1.y) * a / b

    lines[0].symbol = random.choice(['|', '||', '|||'])
    lines[1].symbol = lines[0].symbol

    lines[0].symbol_color = random_color()
    lines[1].symbol_color = lines[0].symbol_color

    labels = random_capitals(n * 2)
    for i in range(n):
        lines[i].p1.label = labels[i]
        lines[i].p2.label = labels[n + i]

    label1 = lines[0].p1.label + lines[0].p2.label
    label2 = lines[1].p1.label + lines[1].p2.label

    diagram.entities.append(("symbol4_a", lines[0].symbol_color, label1, label2))

def divide_angle(n):
    while True:
        # Start by generating n-2 random values > 20
        values = [random.randint(21, 360 // n) for _ in range(n - 2)]
        
        # Ensure that the remaining sum is divisible by 2 for a duplicate
        remaining = 360 - sum(values)
        if remaining <= 40 or remaining % 2 != 0:
            continue
        
        # Add two equal values
        equal_value = remaining // 2
        if equal_value > 20:
            values.extend([equal_value, equal_value])
            indices = list(range(n))  # Create indices
            
            # Shuffle both values and indices together
            combined = list(zip(values, indices))
            random.shuffle(combined)
            
            # Separate back into values and indices
            shuffled_values, shuffled_indices = zip(*combined)
            
            # Find the indices of the duplicate values
            duplicate_value = equal_value
            duplicate_indices = [i for i, v in enumerate(shuffled_values) if v == duplicate_value]
            
            return list(shuffled_values), duplicate_indices

def generate_polygon_with_equal_sides(n, c=(0.5, 0.5), r=0.4):
    angles, (side1, side2) = divide_angle(n)
    points = []

    base_angle = random.randint(0, 360)

    for i in range(n):
        theta = math.radians(sum(angles[:i]) + base_angle)
        x = c[0] + r * math.cos(theta)
        y = c[1] + r * math.sin(theta)
        points.append((x, y))

    return points, side1, side2

def symbol4_b(diagram):
    n = random.randint(3, 8)
    points, idx1, idx2 = generate_polygon_with_equal_sides(n)

    labels = random_capitals(n)

    for i in range(n):
        diagram.lines.append(Line(Point(*points[i]), Point(*points[(i + 1) % n])))
        if i == idx1:
            diagram.lines[-1].symbol = random.choice(['|', '||', '|||'])
            diagram.lines[-1].symbol_color = random_color()
        if i == idx2:
            diagram.lines[-1].symbol = diagram.lines[idx1].symbol
            diagram.lines[-1].symbol_color = diagram.lines[idx1].symbol_color
        diagram.points.append(Point(*points[i], labels[i]))

    label1 = labels[idx1] + labels[(idx1 + 1) % n] if random.randint(0, 1) else labels[(idx1 + 1) % n] + labels[idx1]
    label2 = labels[idx2] + labels[(idx2 + 1) % n] if random.randint(0, 1) else labels[(idx2 + 1) % n] + labels[idx2]

    diagram.entities.append(("symbol4_b", diagram.lines[idx1].symbol_color, label1, label2))

def symbol4_c(diagram):
    p1 = random.random(), random.random()
    p2 = random.random(), random.random()

    if random.randint(0, 1):
        p2 = p2[0], p1[1]

    while (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 < 0.25:
        p1 = random.random(), random.random()
        p2 = random.random(), random.random()

        if random.randint(0, 1):
            p2 = p2[0], p1[1]

    labels = random_capitals(3)

    p3 = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
    mean_point = Point(*p3, labels[0], True)

    p1 = Point(*p1, labels[1], True)
    p2 = Point(*p2, labels[2], True)

    diagram.points.extend([p1, p2, mean_point])

    l1 = Line(p1, mean_point)
    l2 = Line(mean_point, p2)

    diagram.lines.append(l1)
    diagram.lines.append(l2)

    l1.symbol = random.choice(['|', '||', '|||'])
    l2.symbol = l1.symbol

    l1.symbol_color = random_color()
    l2.symbol_color = l1.symbol_color

    diagram.entities.append(("symbol4_c", l1.symbol_color, labels[0], labels[1], labels[2]))
        
def symbol5(diagram):
    theta1 = random.random() * 2 * math.pi
    theta2 = random.random() * 2 * math.pi

    while abs(theta1 - theta2) < math.pi / 6 or abs(theta1 - theta2) > 11 * math.pi / 6:
        theta2 = random.random() * 2 * math.pi

    if theta2 < theta1:
        if random.randint(0, 4):
            theta1, theta2 = theta2, theta1
        else:
            theta2 += 2 * math.pi

    theta_mid = (theta1 + theta2) / 2

    labels = random_capitals(4)

    center = random_point(diagram)
    center.x = center.x * 0.3 + 0.35
    center.y = center.y * 0.3 + 0.35
    center.label = labels[0]

    r = min([
        center.x, 1 - center.x, center.y, 1 - center.y
    ])

    p1 = Point(center.x + r * math.cos(theta1), center.y + r * math.sin(theta1))
    p2 = Point(center.x + r * math.cos(theta2), center.y + r * math.sin(theta2))

    p1.label = labels[1]
    p2.label = labels[2]

    diagram.points.extend([p1, p2])

    l1 = Line(center, p1)
    l2 = Line(center, p2)

    diagram.lines.append(l1)
    diagram.lines.append(l2)

    x = l1.p1.x + r * math.cos(theta_mid)
    y = l1.p1.y + r * math.sin(theta_mid)

    p = Point(x, y)
    p.label = labels[3]
    diagram.points.append(p)

    l = Line(l1.p1, p)
    diagram.lines.append(l)

    angle1 = Angle(l1, l, random_color())
    angle2 = Angle(l, l2, angle1.color)

    angle1.symbol = random.choice(['|', 'o', 'O'])
    angle2.symbol = angle1.symbol
    
    diagram.angles.extend([angle1, angle2])

    diagram.entities.append(("symbol5", angle1.color, center.label, p1.label, p2.label, p.label))


rules = [symbol_1_a, symbol_1_b, symbol_1_c, symbol_2_a, symbol_2_b, symbol3_a, symbol3_b, symbol4_a, symbol4_b, symbol4_c, symbol5]
