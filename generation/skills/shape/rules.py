import random
import math
import numpy as np

class Circle:
    def __init__(self, x, y, r, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label

class EquilateralTriangle:
    def __init__(self, x, y, r, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [(self.x, self.y + self.r), (self.x - self.r * 3**0.5 / 2, self.y - self.r / 2), (self.x + self.r * 3**0.5 / 2, self.y - self.r / 2)]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Rectangle:
    def __init__(self, x, y, width, height, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [
            (self.x - self.width / 2, self.y - self.height / 2), 
            (self.x + self.width / 2, self.y - self.height / 2), 
            (self.x + self.width / 2, self.y + self.height / 2), 
            (self.x - self.width / 2, self.y + self.height / 2)
        ]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Square:
    def __init__(self, x, y, a, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.a = a
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [
            (self.x - self.a / 2, self.y - self.a / 2), 
            (self.x + self.a / 2, self.y - self.a / 2), 
            (self.x + self.a / 2, self.y + self.a / 2), 
            (self.x - self.a / 2, self.y + self.a / 2)
        ]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Trapezoid:
    def __init__(self, x, y, a, b, h, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.h = h
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [
            (self.x - self.a / 2, self.y - self.h / 2), 
            (self.x + self.a / 2, self.y - self.h / 2), 
            (self.x + self.b / 2, self.y + self.h / 2), 
            (self.x - self.b / 2, self.y + self.h / 2)
        ]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Parallelogram:
    def __init__(self, x, y, a, b, h, border_color, fill_color, label="", rotation=0):
        if a < b:
            a, b = b, a
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.h = h
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [
            (self.x - self.a / 2, self.y - self.h / 2), 
            (self.x + self.a / 2 - self.b, self.y - self.h / 2), 
            (self.x + self.a / 2, self.y + self.h / 2), 
            (self.x - self.a / 2 + self.b, self.y + self.h / 2)
        ]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Star:
    def __init__(self, x, y, r, n, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.n = n
        self.rotation = rotation
    
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
        
        p = np.array(points)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Heart:
    def __init__(self, x, y, r, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.r = r / 10
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation
    
    def points(self):
        p = [
            (
                self.x + self.r * (16 * math.sin(t)**3), 
                self.y + self.r * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))  # Reverse the sign
            )
            for t in [i * 2 * math.pi / 100 for i in range(100)]
        ]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Diamond:
    def __init__(self, x, y, a, b, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [
            (self.x - self.a / 2, self.y), 
            (self.x, self.y - self.b / 2), 
            (self.x + self.a / 2, self.y), 
            (self.x, self.y + self.b / 2)
        ]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Pentagon:
    def __init__(self, x, y, r, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [(self.x - self.r * math.sin(2 * math.pi * i / 5), self.y + self.r * math.cos(2 * math.pi * i / 5)) for i in range(5)]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Hexagon:
    def __init__(self, x, y, r, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [(self.x - self.r * math.sin(2 * math.pi * i / 6), self.y + self.r * math.cos(2 * math.pi * i / 6)) for i in range(6)]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Heptagon:
    def __init__(self, x, y, r, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [(self.x - self.r * math.sin(2 * math.pi * i / 7), self.y + self.r * math.cos(2 * math.pi * i / 7)) for i in range(7)]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class Octagon:
    def __init__(self, x, y, r, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.r = r
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [(self.x - self.r * math.sin(2 * math.pi * i / 8), self.y + self.r * math.cos(2 * math.pi * i / 8)) for i in range(8)]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p

class Plus:
    def __init__(self, x, y, r, t, border_color, fill_color, label="", rotation=0):
        if r < t:
            r, t = t, r
        self.x = x
        self.y = y
        self.r = r
        self.t = t
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label

    def points(self):
        x = self.x
        y = self.y

        r = self.r
        t = self.t

        return [
            (x+r, y+t),
            (x+t, y+t),
            (x+t, y+r),
            (x-t, y+r),
            (x-t, y+t),
            (x-r, y+t),
            (x-r, y-t),
            (x-t, y-t),
            (x-t, y-r),
            (x+t, y-r),
            (x+t, y-t),
            (x+r, y-t)
        ]
    
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

class IsoscelesTriangle:
    def __init__(self, x, y, a, h, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.a = a
        self.h = h
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [
            (self.x, self.y + self.h / 2), 
            (self.x - self.a / 2, self.y - self.h / 2), 
            (self.x + self.a / 2, self.y - self.h / 2)
        ]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p
    
class RightTriangle:
    def __init__(self, x, y, a, b, border_color, fill_color, label="", rotation=0):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.border_color = border_color
        self.fill_color = fill_color
        self.label = label
        self.rotation = rotation

    def points(self):
        p = [
            (self.x - self.a / 2, self.y - self.b / 2), 
            (self.x + self.a / 2, self.y - self.b / 2), 
            (self.x - self.a / 2, self.y + self.b / 2)
        ]
        p = np.array(p)
        p -= np.array([self.x, self.y])
        angle = self.rotation * math.pi / 180
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        p = np.dot(p, rotation_matrix.T)
        p += np.array([self.x, self.y])
        return p

class Diagram:
    def __init__(self):
        self.shapes = []
        self.entities = []

def random_position():
    return random.uniform(0.2, 0.8), random.uniform(0.2, 0.8)

def random_color():
    return random.choice(["red", "green", "blue", "yellow", "purple", "orange", "black"])

def random_capitals(n):
    return random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", n)

def random_lowercases(n):
    return random.sample("abcdefghijklmnopqrstuvwxyz", n)

def random_size():
    return random.random() / 5 + 0.1

def random_circle(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Circle(x, y, r, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_equilateral_triangle(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = EquilateralTriangle(x, y, r, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_rectangle(diagram, max_size=float('inf')):
    x, y = random_position()
    width = min(random_size(), max_size * 2 ** 0.5)
    height = min(random_size(), max_size * 2 ** 0.5)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Rectangle(x, y, width, height, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_square(diagram, max_size=float('inf')):
    x, y = random_position()
    a = min(random_size(), max_size * 2 ** 0.5)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Square(x, y, a, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_trapezoid(diagram, max_size=float('inf')):
    x, y = random_position()
    a = min(random_size(), max_size * 2 ** 0.5)
    b = min(random_size(), max_size * 2 ** 0.5)
    h = min(random_size(), max_size * 2 ** 0.5)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Trapezoid(x, y, a, b, h, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_parallelogram(diagram, max_size=float('inf')):
    x, y = random_position()
    a = min(random_size(), max_size * 2 ** 0.5)
    b = min(random_size(), max_size * 2 ** 0.5)
    while abs(a - b) < 0.1:
        a = random_size()
        b = random_size()
    h = random_size()
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Parallelogram(x, y, a, b, h, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_star(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size)
    n = random.randint(5, 6)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Star(x, y, r, n, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_heart(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size / 2)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Heart(x, y, r, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_diamond(diagram, max_size=float('inf')):
    x, y = random_position()
    a = min(random_size(), max_size)
    b = min(random_size(), max_size)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Diamond(x, y, a, b, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_pentagon(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Pentagon(x, y, r, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_hexagon(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Hexagon(x, y, r, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_heptagon(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Heptagon(x, y, r, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_octagon(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Octagon(x, y, r, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_plus(diagram, max_size=float('inf')):
    x, y = random_position()
    r = min(random_size(), max_size)
    t = min(random_size(), r / 2)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Plus(x, y, r, t, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_arrow(diagram, max_size=float('inf')):
    rotation = random.randint(0, 360)
    x, y = random_position()
    l = min(random_size(), max_size)
    w = min(random_size(), max_size / 4)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = Arrow(x, y, l, w, border_color, fill_color, rotation=rotation)
    diagram.shapes.append(shape)
    return shape

def random_isosceles_triangle(diagram, max_size=float('inf')):
    x, y = random_position()
    a = min(random_size(), max_size * 2 ** 0.5)
    h = min(random_size(), max_size * 2 ** 0.5)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = IsoscelesTriangle(x, y, a, h, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_right_triangle(diagram, max_size=float('inf')):
    x, y = random_position()
    a = min(random_size(), max_size)
    b = min(random_size(), max_size)
    border_color = random_color()
    fill_color = random_color()
    if border_color == fill_color == "white":
        border_color = "black"
    shape = RightTriangle(x, y, a, b, border_color, fill_color)
    diagram.shapes.append(shape)
    return shape

def random_shape(diagram, max_size=float('inf')):
    return random.choice([
        random_circle, 
        random_equilateral_triangle, 
        random_rectangle, 
        random_square, 
        random_trapezoid, 
        random_parallelogram, 
        random_star, 
        random_heart, 
        random_diamond, 
        random_pentagon, 
        random_hexagon, 
        random_heptagon, 
        random_plus,
        random_arrow,  
        random_isosceles_triangle, 
        random_right_triangle
    ])(diagram, max_size)

def random_shape_excecpt_arrow(diagram, max_size=float('inf')):
    return random.choice([
        random_circle, 
        random_equilateral_triangle, 
        random_rectangle, 
        random_square, 
        random_trapezoid, 
        random_parallelogram, 
        random_star, 
        random_heart, 
        random_diamond, 
        random_pentagon, 
        random_hexagon, 
        random_heptagon, 
        random_plus,
        random_isosceles_triangle, 
        random_right_triangle
    ])(diagram, max_size)

def shape1(diagram):
    shape = random_shape(diagram)
    if not isinstance(shape, Arrow):
        rotation = random.choice([0, random.randint(0, 360)])
        shape.rotation = rotation
    diagram.entities.append(("shape1", shape))
    return shape

def shape2(diagram):
    shapes = [random_shape(diagram, max_size=0.2) for _ in range(3)]

    x = [0.1, 0.5, 0.9]
    y = [0.5] * 3

    for i, shape in enumerate(shapes):
        shape.x = x[i]
        shape.y = y[i]

    rand = random.randint(0, 2)     # 0: border only, 1: fill only, 2: both

    if rand == 0:
        for shape in shapes:
            shape.fill_color = "white"
        if random.randint(0, 1):
            color = random.choice(['black', random_color()])
            for shape in shapes:
                shape.border_color = color
    elif rand == 1:
        for shape in shapes:
            shape.border_color = "white"
        if random.randint(0, 1):
            color = random.choice(['black', random_color()])
            for shape in shapes:
                shape.fill_color = color
    else:
        if random.randint(0, 1):
            color = random.choice(['black', random_color()])
            for shape in shapes:
                shape.border_color = color
        if random.randint(0, 1):
            color = random.choice(['black', random_color()])
            for shape in shapes:
                shape.fill_color = color

    if random.randint(0, 1):
        for shape in shapes:
            shape.rotation = random.randint(0, 360)

    diagram.entities.append(("shape2", shapes))

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

def shape3(diagram):
    n = random.randint(1, 3)
    dummy = random.randint(2, 4)

    max_size = 0.1

    random_generator = random.choice([
        random_circle, 
        random_equilateral_triangle, 
        random_rectangle, 
        random_square, 
        random_trapezoid, 
        random_parallelogram, 
        random_star, 
        random_heart, 
        random_diamond, 
        random_pentagon, 
        random_hexagon, 
        random_heptagon, 
        random_plus,
        random_arrow,  
        random_isosceles_triangle, 
        random_right_triangle
    ])
    shapes = [random_generator(diagram, max_size) for _ in range(n)]
    shapes.extend([random_shape(diagram, max_size) for _ in range(dummy)])

    rand = random.randint(0, 1)     # 0: border only, 1: fill only

    if rand == 0:
        for shape in shapes:
            shape.fill_color = "none"
        if random.randint(0, 1):
            color = random.choice(['black', random_color()])
            for shape in shapes:
                shape.border_color = color
        if random.randint(0, 1):
            positions = select_coordinates(n + dummy, 0.2)
            for i, shape in enumerate(shapes):
                shape.x = positions[i][0]
                shape.y = positions[i][1]
    elif rand == 1:
        for shape in shapes:
            shape.border_color = "none"
        if random.randint(0, 1):
            color = random.choice(['black', random_color()])
            for shape in shapes:
                shape.fill_color = color
        positions = select_coordinates(n + dummy, 0.2)
        for i, shape in enumerate(shapes):
            shape.x = positions[i][0]
            shape.y = positions[i][1]

    if random.randint(0, 1):
        for shape in shapes:
            shape.rotation = random.randint(0, 360)

    diagram.entities.append(("shape3", shapes))

def shape4(diagram):
    n = random.randint(3, 7)
    shapes = [random_shape(diagram, max_size=0.2) for _ in range(n)]
    rand = random.randint(0, 1)     # 0: all different, 1: one different

    if rand == 0:
        colors = random.sample(["red", "green", "blue", "yellow", "purple", "orange", "black"], n)
    else:
        color = random_color()
        another_color = random_color()
        while another_color == color:
            another_color = random_color()
        colors = [color] + [another_color] * (n - 1)

    if random.randint(0, 1):
        for shape, color in zip(shapes, colors):
            shape.fill_color = "none"
            shape.border_color = color
    else:
        for shape, color in zip(shapes, colors):
            shape.border_color = "none"
            shape.fill_color = color
        positions = select_coordinates(n, 0.3)
        for i, shape in enumerate(shapes):
            shape.x = positions[i][0]
            shape.y = positions[i][1]

    if random.randint(0, 1):
        for shape in shapes:
            shape.rotation = random.randint(0, 360)

    diagram.entities.append(("shape4", shapes, rand))

def shape5(diagram):
    n = random.randint(3, 7)
    shapes = [random_shape(diagram, max_size=0.2) for _ in range(n)]

    colors = [random_color()] * n

    if random.randint(0, 1):
        for shape, color in zip(shapes, colors):
            shape.fill_color = "none"
            shape.border_color = color
    else:
        for shape, color in zip(shapes, colors):
            shape.border_color = "none"
            shape.fill_color = color
    positions = select_coordinates(n, 0.3)
    for i, shape in enumerate(shapes):
        shape.x = positions[i][0]
        shape.y = positions[i][1]

    rand = random.randint(0, 1)     # 0: number label, 1: alphabet label
    if rand == 0:
        for i, shape in enumerate(shapes):
            shape.label = str(i + 1)
    else:
        labels = random_capitals(n)
        for shape, label in zip(shapes, labels):
            shape.label = label
    
    diagram.entities.append(("shape5", shapes))

def shape6(diagram):
    n = random.randint(3, 7)
    shapes = [random_shape_excecpt_arrow(diagram, max_size=0.1) for _ in range(n)]

    while all(shapes[i].__class__ == shapes[i + 1].__class__ for i in range(n - 1)):
        for _ in range(n):
            diagram.shapes.pop()
        shapes = [random_shape_excecpt_arrow(diagram, max_size=0.1) for _ in range(n)]

    centers = select_coordinates(n, 0.35)

    for i, shape in enumerate(shapes):
        shape.x = centers[i][0]
        shape.y = centers[i][1]

    rand = random.randint(0, 1)     # 0: border only, 1: fill only

    if rand == 0:
        for shape in shapes:
            shape.fill_color = "none"
        color = random.choice(['black', random_color()])
        for shape in shapes:
            shape.border_color = color
    elif rand == 1:
        border_color = random.choice(['black', 'none'])
        for shape in shapes:
            shape.border_color = border_color
        color = random_color()
        for shape in shapes:
            shape.fill_color = color

    if random.randint(0, 1):
        for shape in shapes:
            shape.rotation = random.randint(0, 360)

    random.shuffle(shapes)

    arrow = Arrow(0.5, 0.5, 0.1, 0.05, "black", "none")
    diagram.shapes.append(arrow)

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

    diagram.entities.append(("shape6", shapes))

def shape7(diagram):
    shape = random.choice([random_pentagon, random_hexagon, random_heptagon, random_octagon])(diagram)
    shape.rotation = random.randint(0, 360)
    diagram.entities.append(("shape7", shape))

def shape8(diagram):
    line_color = random.choice(['black', random_color()])
    line = Rectangle(0.5, 0.5, 0.01, 2, "none", line_color)
    diagram.shapes.append(line)

    n = random.randint(2, 3)

    positions1 = select_coordinates(n, 0.6)
    positions2 = select_coordinates(n, 0.6)

    for i in range(n):
        positions1[i] = (positions1[i][0] / 3, positions1[i][1])
        positions2[i] = (1 - positions2[i][0] / 3, positions2[i][1])

    random.shuffle(positions1)
    random.shuffle(positions2)

    random_shape_pool = [
        random_circle, 
        random_equilateral_triangle, 
        random_rectangle, 
        random_square, 
        random_trapezoid, 
        random_parallelogram, 
        random_star, 
        random_heart, 
        random_diamond, 
        random_pentagon, 
        random_hexagon, 
        random_heptagon, 
        random_plus,
        random_isosceles_triangle, 
        random_right_triangle,
        random_arrow,
        random_octagon
    ]

    random.shuffle(random_shape_pool)

    shapes = []

    shape = random_shape_pool[0](diagram, max_size=0.2)
    shape.x, shape.y = positions1[0]
    shapes.append(shape)

    shape = random_shape_pool[0](diagram, max_size=0.2)
    shape.x, shape.y = positions2[0]
    shapes.append(shape)

    for i in range(1, n):
        shape = random_shape_pool[2 * i - 1](diagram, max_size=0.1)
        shape.x, shape.y = positions1[i]
        shapes.append(shape)

        shape = random_shape_pool[2 * i](diagram, max_size=0.2)
        shape.x, shape.y = positions2[i]
        shapes.append(shape)

    if random.randint(0, 1):
        for shape in shapes:
            shape.rotation = random.randint(0, 360)

    if random.randint(0, 1):
        color = random_color()
        for shape in shapes:
            shape.fill_color = color
            shape.border_color = 'none'
    else:
        color = random.choice(['black', random_color()])
        for shape in shapes:
            shape.fill_color = 'none'
            shape.border_color = color

    diagram.entities.append(("shape8", shapes))

def shape9(diagram):
    n = random.randint(3, 5)
    positions = select_coordinates(n, 0.4)

    colors = [random_color() for _ in range(n)]

    while len(set(colors)) != n and colors[0] == 'black':
        colors = [random_color() for _ in range(n)]

    colors[0] = random.choice(['white', colors[0]])

    background = Rectangle(0.5, 0.5, 2, 2, 'none', colors[0])
    diagram.shapes.append(background)

    shapes = [random_shape(diagram, max_size=0.1) for _ in range(n)]

    while all(shapes[i].__class__ == shapes[i + 1].__class__ for i in range(n - 1)):
        for _ in range(n):
            diagram.shapes.pop()
        shapes = [random_shape_excecpt_arrow(diagram, max_size=0.1) for _ in range(n)]

    random.shuffle(shapes)

    for i in range(1, n):
        shapes[i].x, shapes[i].y = positions[i]
        shapes[i].fill_color = colors[i]
        shapes[i].border_color = 'black'

    shapes[0].x, shapes[0].y = positions[0]
    shapes[0].fill_color = 'none'
    shapes[0].border_color = 'black'

    diagram.entities.append(("shape9", shapes, background))

        
rules = [shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8, shape9]
