import math
import numpy as np
import random

class Text:
    def __init__(self, x, y, text, color, size=None):
        self.x = x
        self.y = y
        self.text = text
        self.color = color
        self.size = size

class Circle:
    def __init__(self, x, y, r, border_color, fill_color, label=""):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label

class Arrow1:
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
    
class Arrow2:
    def __init__(self, x, y, l1, l2, w1, w2, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.l1 = l1
        self.l2 = l2
        self.w1 = w1
        self.w2 = w2
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        l1, l2, w1, w2 = self.l1, self.l2, self.w1, self.w2

        p = [
            (l1/2, 0),
            (l2-l1/2, w1/2),
            (l2-l1/2, w2/2),
            (-l1/2, w2/2),
            (-l1/2, -w2/2),
            (l2-l1/2, -w2/2),
            (l2-l1/2, -w1/2)
        ]
        p = np.array(p)
        angle = self.rotation * math.pi / 180
        p = np.dot(p, np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]).T)
        p += np.array([self.x, self.y])
        return p
    
class Arrow3:
    def __init__(self, x, y, l, w, d, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        self.d = d
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        l, w, d = self.l, self.w, self.d

        p = [
            (l/2, 0),
            (d-l/2, w/2),
            (-l/2, w/2),
            (l/2-d, 0),
            (-l/2, -w/2),
            (d-l/2, -w/2)
        ]
        p = np.array(p)
        angle = self.rotation * math.pi / 180
        p = np.dot(p, np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]).T)
        p += np.array([self.x, self.y])
        return p
    
class Diagram:
    def __init__(self):
        self.arrows = []
        self.texts = []
        self.circles = []
        self.entities = []

def random_color():
    return np.random.choice(["black", "blue", "red", "green", "yellow", "purple", "orange", "brown", "pink", "cyan"])

def random_arrow1(diagram):
    x = np.random.uniform(0.2, 0.8)
    y = np.random.uniform(0.2, 0.8)
    l = np.random.uniform(0.1, 0.2)
    w = np.random.uniform(0.1, 0.2)
    border_color = random_color()
    fill_color = random_color()
    label = ""
    rotation = np.random.randint(0, 360)
    arrow = Arrow1(x, y, l, w, border_color, fill_color, label, rotation)
    diagram.arrows.append(arrow)
    return arrow

def random_arrow2(diagram):
    x = np.random.uniform(0.2, 0.8)
    y = np.random.uniform(0.2, 0.8)
    l1 = np.random.uniform(0.1, 0.2)
    l2 = np.random.uniform(0, l1) * 0.7
    w1 = np.random.uniform(0.1, 0.2)
    w2 = np.random.uniform(0, w1) * 0.7
    border_color = random_color()
    fill_color = random_color()
    label = ""
    rotation = np.random.randint(0, 360)
    arrow = Arrow2(x, y, l1, l2, w1, w2, border_color, fill_color, label, rotation)
    diagram.arrows.append(arrow)
    return arrow

def random_arrow3(diagram):
    x = np.random.uniform(0.2, 0.8)
    y = np.random.uniform(0.2, 0.8)
    l = np.random.uniform(0.1, 0.2)
    w = np.random.uniform(0.1, 0.2)
    d = np.random.uniform(0, l) * 0.7
    border_color = random_color()
    fill_color = random_color()
    label = ""
    rotation = np.random.randint(0, 360)
    arrow = Arrow3(x, y, l, w, d, border_color, fill_color, label, rotation)
    diagram.arrows.append(arrow)
    return arrow

def random_arrow_generator():
    return random.choice([random_arrow1, random_arrow2, random_arrow3])

def angle_between(angle1, angle2):
    return min(abs(angle1 - angle2), 360 - abs(angle1 - angle2))


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

def direction1(diagram):
    n = random.randint(3, 5)
    rand = random.randint(0, 1) # 0: don't add noise, 1: add noise

    arrows = []
    for _ in range(n):
        arrows.append(random_arrow_generator()(diagram))

    if random.randint(0, 1):
        positions = select_coordinates(n, 0.2)
        random.shuffle(positions)
    else:
        positions = [((i + 1) / (n + 1), 0.5) for i in range(n)]
    labels = [i + 1 for i in range(n)]

    dir1 = random.random() * 360
    dir2 = random.random() * 360

    while angle_between(dir1, dir2) < 90:
        dir2 = random.random() * 360

    for i, arrow in enumerate(arrows):
        noise = random.uniform(-10, 10) if rand else 0
        arrow.rotation = dir2 + noise
        arrow.x, arrow.y = positions[i]
        arrow.label = str(labels[i])

    answer = random.randint(0, n - 1)

    arrows[answer].rotation = dir1

    diagram.entities.append(('direction1', n, str(labels[answer]), rand))

def direction2(diagram):
    directions = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
    direction = random.choice(directions)
    angle = {
        'up': 90,
        'down': 270,
        'left': 180,
        'right': 0,
        'up-left': 135,
        'up-right': 45,
        'down-left': 225,
        'down-right': 315
    }[direction]

    arrow = random_arrow_generator()(diagram)
    arrow.rotation = angle

    diagram.entities.append(('direction2', direction))

def direction3(diagram):
    n = random.randint(3, 5)

    directions = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']
    direction = random.choice(directions)
    angle = {
        'up': 90,
        'down': 270,
        'left': 180,
        'right': 0,
        'up-left': 135,
        'up-right': 45,
        'down-left': 225,
        'down-right': 315
    }[direction]

    arrows = []
    random_arrow = random_arrow_generator()
    for _ in range(n):
        arrows.append(random_arrow(diagram))

    if random.randint(0, 1):
        positions = select_coordinates(n, 0.2)
        random.shuffle(positions)
    else:
        positions = [((i + 1) / (n + 1), 0.5) for i in range(n)]
    labels = [i + 1 for i in range(n)]

    for i, arrow in enumerate(arrows):
        angle2 = random.random() * 360
        while angle_between(angle, angle2) < 90:
            angle2 = random.random() * 360
        arrow.rotation = angle2
        arrow.x, arrow.y = positions[i]
        arrow.label = str(labels[i])

    answer = random.randint(0, n - 1)

    arrows[answer].rotation = angle

    diagram.entities.append(('direction3', n, direction, str(labels[answer])))

def direction4(diagram):
    type = random.choice(['diagonal', 'cross'])

    if type == 'diagonal':
        positions = [
            (0.25, 0.25),
            (0.75, 0.25),
            (0.25, 0.75),
            (0.75, 0.75)
        ]
        answer_index = random.randint(0, 3)
        direction = ['down-left', 'down-right', 'up-left', 'up-right'][answer_index]
        angle = {
            'up-left': 135,
            'up-right': 45,
            'down-left': 225,
            'down-right': 315
        }[direction]
    else:
        positions = [
            (0.5, 0.25),
            (0.5, 0.75),
            (0.25, 0.5),
            (0.75, 0.5)
        ]
        answer_index = random.randint(0, 3)
        direction = ['down', 'up', 'left', 'right'][answer_index]
        angle = {
            'up': 90,
            'down': 270,
            'left': 180,
            'right': 0
        }[direction]

    arrow = random_arrow_generator()(diagram)
    arrow.rotation = angle
    arrow.x, arrow.y = 0.5, 0.5

    object_type = random.choice(['alphabet', 'number', 'color', 'direction']) if type == 'cross' else random.choice(['alphabet', 'number', 'color'])
    
    negative_index = random.randint(0, 3)
    while negative_index == answer_index:
        negative_index = random.randint(0, 3)

    if object_type == 'alphabet':
        texts = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)
        answer = texts[answer_index]
        negative_answer = texts[negative_index]
        for i, text in enumerate(texts):
            diagram.texts.append(Text(positions[i][0], positions[i][1], text, 'black'))
    elif object_type == 'number':
        numbers = random.sample(range(1, 21), 4)
        answer = str(numbers[answer_index])
        negative_answer = str(numbers[negative_index])
        for i, number in enumerate(numbers):
            diagram.texts.append(Text(positions[i][0], positions[i][1], str(number), 'black'))
    elif object_type == 'color':
        colors = random.sample(['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown', 'pink', 'cyan'], 4)
        answer = colors[answer_index]
        negative_answer = colors[negative_index]
        for i, color in enumerate(colors):
            diagram.circles.append(Circle(positions[i][0], positions[i][1], 0.05, 'black', color))
    elif object_type == 'direction':
        directions = ['down', 'up', 'left', 'right']
        if random.randint(0, 1):
            random.shuffle(directions)
        answer = directions[answer_index]
        negative_answer = directions[negative_index]
        for i, direction in enumerate(directions):
            diagram.texts.append(Text(positions[i][0], positions[i][1], direction, 'black'))

    diagram.entities.append(('direction4', object_type, answer, negative_answer))


def direction5(diagram):
    type = random.choice(['diagonal', 'cross'])

    if type == 'diagonal':
        positions = [
            (0.25, 0.25),
            (0.75, 0.25),
            (0.25, 0.75),
            (0.75, 0.75)
        ]
        answer_index1 = random.randint(0, 1)
        answer_index2 = 3 - answer_index1
        direction = ['down-left', 'down-right', 'up-left', 'up-right'][answer_index1]
        angle = {
            'up-left': 135,
            'up-right': 45,
            'down-left': 225,
            'down-right': 315
        }[direction]
    else:
        positions = [
            (0.5, 0.25),
            (0.5, 0.75),
            (0.25, 0.5),
            (0.75, 0.5)
        ]
        answer_index1 = random.randint(0, 1) * 2
        answer_index2 = answer_index1 + 1
        direction = ['down', 'up', 'left', 'right'][answer_index1]
        angle = {
            'up': 90,
            'down': 270,
            'left': 180,
            'right': 0
        }[direction]

    arrow1 = random_arrow1(diagram)
    arrow1.rotation = angle
    arrow1.x, arrow1.y = np.array([0.5, 0.5]) + np.array([np.cos(angle * math.pi / 180), np.sin(angle * math.pi / 180)]) * 0.05

    arrow2 = random_arrow1(diagram)
    arrow2.rotation = angle + 180
    arrow2.x, arrow2.y = np.array([0.5, 0.5]) - np.array([np.cos(angle * math.pi / 180), np.sin(angle * math.pi / 180)]) * 0.05
    arrow2.l = arrow1.l
    arrow2.w = arrow1.w
    arrow2.fill_color = arrow1.fill_color

    arrow1.border_color = arrow2.border_color = 'none'

    object_type = random.choice(['alphabet', 'number', 'color', 'direction']) if type == 'cross' else random.choice(['alphabet', 'number', 'color'])

    if object_type == 'alphabet':
        texts = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4)
        answer1 = texts[answer_index1]
        answer2 = texts[answer_index2]
        for i, text in enumerate(texts):
            diagram.texts.append(Text(positions[i][0], positions[i][1], text, 'black'))
    elif object_type == 'number':
        numbers = random.sample(range(1, 21), 4)
        answer1 = str(numbers[answer_index1])
        answer2 = str(numbers[answer_index2])
        for i, number in enumerate(numbers):
            diagram.texts.append(Text(positions[i][0], positions[i][1], str(number), 'black'))
    elif object_type == 'color':
        colors = random.sample(['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown', 'pink', 'cyan'], 4)
        answer1 = colors[answer_index1]
        answer2 = colors[answer_index2]
        for i, color in enumerate(colors):
            diagram.circles.append(Circle(positions[i][0], positions[i][1], 0.05, 'black', color))
    elif object_type == 'direction':
        directions = ['down', 'up', 'left', 'right']
        if random.randint(0, 1):
            random.shuffle(directions)
        answer1 = directions[answer_index1]
        answer2 = directions[answer_index2]
        for i, direction in enumerate(directions):
            diagram.texts.append(Text(positions[i][0], positions[i][1], direction, 'black'))

    if random.randint(0, 1):
        answer1, answer2 = answer2, answer1

    diagram.entities.append(('direction5', object_type, answer1, answer2))

def direction6(diagram):
    n = random.randint(3, 5)
    object_type = random.choice(['alphabet', 'number', 'color'])

    positions = select_coordinates(n, 0.2)
    random.shuffle(positions)

    objects = []

    if object_type == 'alphabet':
        texts = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', n)
        answer = texts[0]
        negative_answer = texts[1]
        for i, text in enumerate(texts):
            objects.append(Text(positions[i][0], positions[i][1], text, 'black'))
        diagram.texts.extend(objects)
    elif object_type == 'number':
        numbers = random.sample(range(1, 21), n)
        answer = str(numbers[0])
        negative_answer = str(numbers[1])
        for i, number in enumerate(numbers):
            objects.append(Text(positions[i][0], positions[i][1], str(number), 'black'))
        diagram.texts.extend(objects)
    elif object_type == 'color':
        colors = random.sample(['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown', 'pink', 'cyan'], n)
        answer = colors[0]
        negative_answer = colors[1]
        for i, color in enumerate(colors):
            objects.append(Circle(positions[i][0], positions[i][1], 0.05, 'black', color))
        diagram.circles.extend(objects)
    
    arrow = Arrow1(0.5, 0.5, 0.1, 0.05, "black", "none")
    diagram.arrows.append(arrow)

    x, y = objects[0].x, objects[0].y
    p = np.array([x, y])
    theta = random.uniform(0, 2 * math.pi)
    arrow_position = p + np.array([math.cos(theta), math.sin(theta)]) * 0.2
    arrow.x, arrow.y = arrow_position
    rotation = (theta + math.pi) * 180 / math.pi
    arrow.rotation = rotation

    diagram.entities.append(('direction6', object_type, answer, negative_answer))



def direction7(diagram):
    arrow = random_arrow1(diagram)
    arrow.w *= 2
    arrow.l *= 5

    start = np.array([arrow.x, arrow.y]) - arrow.l / 2 * np.array([math.cos(arrow.rotation * math.pi / 180), math.sin(arrow.rotation * math.pi / 180)])
    end = np.array([arrow.x, arrow.y]) + arrow.l / 6 * np.array([math.cos(arrow.rotation * math.pi / 180), math.sin(arrow.rotation * math.pi / 180)])

    if random.randint(0, 1):
        normal = np.array([-math.sin(arrow.rotation * math.pi / 180), math.cos(arrow.rotation * math.pi / 180)])
        normal /= np.linalg.norm(normal)

        if random.randint(0, 1):
            normal *= -1

        start += normal * arrow.w / 2
        end += normal * arrow.w / 2

    n = random.randint(3, 5)
    text_type = random.choice(['alphabet', 'number'])

    if text_type == 'alphabet':
        alphabets = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', n)
    else:
        alphabets = random.sample(range(1, 9), n)
        alphabets = [str(i) for i in alphabets]

    for i in range(n):
        t = (i + 1) / (n + 1)
        x = start[0] * (1 - t) + end[0] * t
        y = start[1] * (1 - t) + end[1] * t
        diagram.texts.append(Text(x, y, alphabets[i], 'black', 8))

    diagram.entities.append(('direction7', text_type, alphabets))

def direction8(diagram):
    random_arrow = random_arrow_generator()
    arrow1 = random_arrow(diagram)

    arrow1.x = arrow1.y = 0.5
    arrow1.border_color = 'none'

    arrow2 = random_arrow(diagram)

    while arrow2.fill_color == arrow1.fill_color:
        diagram.arrows.remove(arrow2)
        arrow2 = random_arrow(diagram)

    relative_direction = ['same direction', 'opposite direction', 'left', 'right']
    direction = random.choice(relative_direction)
    angle = {
        'same direction': 0,
        'opposite direction': 180,
        'left': 90,
        'right': 270
    }[direction]

    arrow2.x, arrow2.y = np.array([0.5, 0.5]) + np.array([np.cos(arrow1.rotation * math.pi / 180), np.sin(arrow1.rotation * math.pi / 180)]) * 0.2
    arrow2.rotation = arrow1.rotation + angle
    arrow2.border_color = 'none'

    diagram.entities.append(('direction8', arrow1.fill_color, arrow2.fill_color, direction))

    
def direction9(diagram):
    direction = random.choice(['up-left', 'up-right', 'down-left', 'down-right'])
    angle = {
        'up-left': 135,
        'up-right': 45,
        'down-left': 225,
        'down-right': 315
    }[direction]

    arrow = random_arrow1(diagram)
    arrow.rotation = angle

    diagram.entities.append(('direction9', direction))

def direction10(diagram):
    arrows = []
    n = random.randint(4, 6)
    positions = select_coordinates(n, 0.2)
    random.shuffle(positions)
    labels = [i + 1 for i in range(n)]

    for i in range(n):
        arrow = random_arrow1(diagram)
        arrow.x, arrow.y = positions[i]
        arrow.label = str(labels[i])
        arrow.rotation = np.arctan2(arrow.y - 0.5, arrow.x - 0.5) * 180 / math.pi
        arrows.append(arrow)

    answer_index = random.randint(0, n - 1)

    arrows[answer_index].rotation = arrows[answer_index].rotation + 180

    for i in range(1, 8):
        diagram.circles.append(Circle(0.5, 0.5, 0.1 * i, 'lightgray', 'none'))

    q_type = random.choice(['in', 'out'])

    if q_type == 'out':
        for arrow in arrows:
            arrow.rotation += 180

    diagram.entities.append(('direction10', q_type, str(labels[answer_index])))


rules = [direction1, direction2, direction3, direction4, direction5, direction6, direction7, direction8, direction9, direction10]