import matplotlib.pyplot as plt
import numpy as np
from labels import *
import random
import math
import json

def random_angle():
    return np.random.uniform(np.pi/9, 17/9*np.pi)

def rotate_vector(vector, angle):
    return np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]) @ np.array(vector)


def random_coord(start = 10, end = 990):
    return np.random.uniform(start, end)


def line_already_in(diagram, point1, point2):
    for line in diagram.lines:
        if (line.point1 == point1 and line.point2 == point2) or (line.point1 == point2 and line.point2 == point1):
            return True
    return False

def label_point(diagram):
    ind = 0
    while True:
        label = random.choice(capitals.candidates)
        if label not in [point.label for point in diagram.points]:
            return label
        if ind > 200:
            raise ValueError(f'No possible label found with currently {len(diagram.points)} points of list : {[point.label for point in diagram.points]}')


        ind+=1

def random_length():
    if random.random() < 0.5:
        return random.choice(small_letters.candidates)
    else:
        return int(random.uniform(1, 30))


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

        # for line in self.lines:
        #     for point in line.passing_points:
        #         assert point in self.points
        #
        # for triangle in self.triangles:
        #     for point in triangle.vertices:
        #         assert point in self.points




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

    if len(label) == 0:
        diagram.entities.append(('line', [diagram.points[-2].label, diagram.points[-1].label]))
    else:
        diagram.entities.append(('labelled_line', [diagram.points[-2].label, diagram.points[-1].label, label]))


    diagram.lines.append(Line(diagram.points[-2], diagram.points[-1], label))

    # diagram.entities.extend([f'{label} : Line({label1}{label2})'])
    return diagram

def add_free_point_with_line(diagram : Diagram):
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
    if len(label) == 0:
        diagram.entities.append(('line', [diagram.points[-2], diagram.points[-1]]))
    else:
        diagram.entities.append(('labelled_line', [diagram.points[-2].label, diagram.points[-1].label, label_l]))




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
                raise ValueError('No possible line found')
            elif already_in: print('already in')
            else: break

            ind += 1


        label = random.choice(small_letters.candidates.extend(["","","","","",""]))
        diagram.lines.append(Line(point1, point2, label))
        if len(label) == 0 :
            diagram.entities.append(('line', [point1.label, point2.label]))
        else:
            diagram.entities.append(('labelled_line', [point1.label, point2.label,label]))


        return diagram
    except: return diagram

def add_infinite_line(diagram : Diagram):

    point1, point2 = random.sample(diagram.points, 2)
    label = ''
    diagram.lines.append(Line(point1, point2, label, infinite=True))
    diagram.entities.append(('infinite_line',[point1.label, point2.label]))
    return diagram


def add_circle(diagram : Diagram, radius = None):

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
    diagram.entities.append(('circle', [f'{center.label}', f'{different_pt_label}']))
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

    d.points.append(center)
    d.circles.append(Circle(center, radius, f'({center.label},{radius})'))
    d.entities.append(('circle',[f'{center.label}',f'{label_point(d)}']))

    return d

def add_triangle(diagram : Diagram):
    point1, point2, point3 = random.sample(diagram.points, 3)
    label = random.choice(small_letters.candidates)
    diagram.triangles.append(Triangle(point1, point2, point3, label))
    diagram.entities.append(('triangle', [point1.label, point2.label, point3.label]))
    return diagram


def add_free_triangle(diagram: Diagram):
    A_x, A_y, B_x, B_y, C_x, C_y = random_coord(), random_coord(), random_coord(), random_coord(), random_coord(), random_coord()
    A_label = label_point(diagram)
    while True:
        B_label = label_point(diagram)
        if B_label != A_label:
            break
    while True:
        C_label = label_point(diagram)
        if C_label != A_label and C_label != B_label:
            break

    A,B,C = Point(A_x, A_y, A_label), Point(B_x, B_y, B_label), Point(C_x, C_y, C_label)
    diagram.points.extend([A,B,C])
    diagram.lines.extend([Line(A, B, ''), Line(B, C, ''), Line(C, A, '')])
    diagram.entities.append(('triangle', [A.label, B.label, C.label]))
    return diagram

def angle_bisector(diagram: Diagram):
    if len(diagram.points) < 3:
        return diagram

    ind = 0
    while True:
        A, B, C = random.sample(diagram.points, 3)

        # Calculate direction vectors BA and BC
        vector_BA = (A.x - B.x, A.y - B.y)
        vector_BC = (C.x - B.x, C.y - B.y)

        # Normalize the vectors to get unit vectors
        unit_BA = normalize(vector_BA)
        unit_BC = normalize(vector_BC)
        if unit_BA[0]*unit_BC[0] + unit_BA[1]*unit_BC[1] > 0.86:
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

    # Calculate midpoints of AB and BC
    line = random.choice(diagram.lines)
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
    if assert_coord_in_range(Xx + radius, Xy + radius) and assert_coord_in_range(Xx - radius, Xy - radius):
        pass
    else: return diagram

    circumcenter = Point(Xx, Xy, new_label)
    diagram.points.extend([C, circumcenter])
    diagram.lines.extend([Line(B, C, ''), Line(C, A, '')])
    # diagram.entities.append(f'Circumcenter Point({new_label})')

    diagram.circles.append(Circle(circumcenter, radius, ''))
    # diagram.entities.append(f'Circumscriber Circle({circumcenter.label},{radius}) for triangle {A.label}{B.label}{C.label}')
    diagram.entities.append(('circle_center', [A.label, B.label, C.label, circumcenter.label]))

    return diagram


def eq_quadrilateral(diagram: Diagram):
    try:
        # Randomly select three points
        A, B, C = random.sample(diagram.points, 3)

        # Calculate D such that AD = BC
        AD_length = ((B.x - C.x) ** 2 + (B.y - C.y) ** 2) ** 0.5
        angle_ABC = np.arctan2(C.y - B.y, C.x - B.x)
        angle_BAD = angle_ABC + np.pi  # Opposite direction

        Dx = A.x - AD_length * np.cos(angle_BAD)
        Dy = A.y - AD_length * np.sin(angle_BAD)
        assert assert_coord_in_range(Dx, Dy)

        # Create point D
        D_label = label_point(diagram)

        D = Point(Dx, Dy, D_label)
        diagram.points.append(D)
        # diagram.entities.append(f'Point({D.label})')

        AB_exists = False
        BC_exists = False
        #Check if lines are already in the diagram
        for line in diagram.lines:
            if (line.point1 == B and line.point2 == C) or (line.point1 == C and line.point2 == B):
                label_BC = line.label
                BC_exits = True
                break

        # Add lines to form the quadrilateral
        diagram.lines.extend([
            Line(A, B, label=""),
            Line(B, C, label=""),
            Line(C, D, label=""),
            Line(D, A, label=label_BC if BC_exists else "")
        ])

        # diagram.entities.append(f'Line({A.label}{B.label})') if not AB_exists else None
        # diagram.entities.append(f'Line({B.label}{C.label})') if not BC_exists else None
        # diagram.entities.append(f'Line({C.label}{D.label})')
        # diagram.entities.append(f'Line({D.label}{A.label}' if not BC_exists else f'{label_BC} : Line({D.label}{A.label})')
        # diagram.entities.append(f'Equilateral Quadrilateral({A.label}{B.label}{C.label}{D.label})')
        diagram.entities.append(('equilateral_quadrilateral', [A.label, B.label, C.label, D.label]))
        return diagram
    except:
        return diagram


def eq_trapezoid(diagram: Diagram):
    try:
        # Randomly select two points A, B to form the base AB of the trapezoid
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
        assert assert_coord_in_range(Dx, Dy) and assert_coord_in_range(Cx, Cy)

        # Create points C and D
        C_label, D_label = random.sample(capitals.candidates, 2)
        C = Point(Cx, Cy, C_label)
        D = Point(Dx, Dy, D_label)
        diagram.points.extend([C, D])

        # Add lines to form the trapezoid
        diagram.lines.extend([
            Line(A, B, label=""),  # Base AB
            Line(B, C, label=""),  # Side BC
            Line(C, D, label=""),  # Top CD, parallel to AB
            Line(D, A, label="")   # Side AD
        ])

        # diagram.entities.extend([
        #     f'Point({C.label})', f'Point({D.label})',
        #     f'Line({A.label}{B.label})', f'Line({B.label}{C.label})',
        #     f'Line({C.label}{D.label})', f'Line({D.label}{A.label})',
        #     f'Equilateral Trapezoid({A.label}{B.label}{C.label}{D.label})'
        # ])
        diagram.entities.append(('equilateral_trapezoid', [A.label, B.label, C.label, D.label]))
        return diagram
    except Exception as e:
        print(f"Error constructing equilateral trapezoid: {e}")
        return diagram


def eqtriangle(diagram: Diagram):
    # Calculate the length of BC
    B,C = random.sample(diagram.points, 2)

    BC_length = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)

    # Angle of line BC with the horizontal
    angle_BC = np.arctan2(C.y - B.y, C.x - B.x)

    # Calculate the positions for X
    # Adding 60 degrees (π/3 radians) for one position
    is_equilateral = random_coord() < 500
    if is_equilateral:
        randang = np.pi/3
    else:
        randang = random.uniform(np.pi/9, np.pi / 2.5)
    angle_X1 = angle_BC + randang
    X1_x = B.x + BC_length * np.cos(angle_X1)
    X1_y = B.y + BC_length * np.sin(angle_X1)

    assert assert_coord_in_range(X1_x, X1_y)

    # Subtracting 60 degrees (π/3 radians) for the other position
    angle_X2 = angle_BC - randang
    X2_x = B.x + BC_length * np.cos(angle_X2)
    X2_y = B.y + BC_length * np.sin(angle_X2)

    # Choose one of the positions for X (for example, the first one)
    X_label = label_point(diagram)
    X = Point(X1_x, X1_y, X_label)
    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label})')

    # Add lines to form the equilateral triangle
    diagram.lines.extend([
        Line(B, C, label=""),
        Line(C, X, label=""),
        Line(X, B, label="")
    ])

    # label = f'Equilateral Triangle({X.label}{B.label}{C.label}) with length {int(BC_length)}' if is_equilateral else f'Isosceles Triangle({X.label}{B.label}{C.label})'
    # diagram.entities.append(label)
    if is_equilateral:
        diagram.entities.append(('equilateral_triangle', [X.label, B.label, C.label]))
    else :
        diagram.entities.append(('isosceles_triangle', [X.label, B.label, C.label]))
    return diagram


def eqdia_quadrilateral(diagram: Diagram):
    # Randomly select two points A and B
    A, B = random.sample(diagram.points, 2)

    # Calculate the length of AB and its angle θ from the horizontal
    AB_length = np.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
    theta = np.arctan2(B.y - A.y, B.x - A.x)
    if theta < 0:
        theta += np.pi

    # Choose a random angle α and length for AC and BD
    alpha = random.uniform(np.pi/9, np.pi / 2.5)  # α from 0 to 60 degrees


    AC_BD_length = random.uniform(0.5 * AB_length, 3 * AB_length)

    # Calculate coordinates for C using angle α and length AC
    angle_AC = theta + alpha  # Angle for AC based on θ and α
    C_x = A.x + AC_BD_length * np.cos(angle_AC)
    C_y = A.y + AC_BD_length * np.sin(angle_AC)

    # Ensure C is within valid range
    assert assert_coord_in_range(C_x, C_y)

    # Calculate coordinates for D using angle α and length BD
    angle_BD = theta + np.pi - alpha  # Angle for BD based on θ and α
    D_x = B.x + AC_BD_length * np.cos(angle_BD)
    D_y = B.y + AC_BD_length * np.sin(angle_BD)

    # Ensure D is within valid range
    assert assert_coord_in_range(D_x, D_y)

    # Define points C and D
    C_label, D_label = random.sample(capitals.candidates, 2)
    C = Point(C_x, C_y, C_label)
    D = Point(D_x, D_y, D_label)
    diagram.points.extend([C, D])

    # Add points as entities
    # diagram.entities.extend([f'Point({C.label})', f'Point({D.label})'])


    tcks = random.randint(1,3)
    # Add lines to form the quadrilateral
    diagram.lines.extend([
        Line(A, B, label=""),
        Line(B, C, label=""),
        Line(C, D, label=""),
        Line(D, A, label=""),
        Line(A,C, label="", tickmarks=tcks),
        Line(B,D, label="", tickmarks=tcks)
    ])

    # Label the quadrilateral
    # label = f'Quadrilateral({A.label}{B.label}{C.label}{D.label}) with {A.label}{C.label}={B.lable}{D.label}'
    # diagram.entities.append(label)
    diagram.entities.append(('eqdia', [A.label, B.label, C.label, D.label]))
    return diagram


def eqdistance(diagram: Diagram):
    A,B,C = random.sample(diagram.points, 3)

    # Calculate the length of BC
    BC_length = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)

    # Choose a random direction for AX; theta is the angle from the horizontal
    theta = random.uniform(0, 2 * np.pi)  # Angle in radians

    # Calculate the coordinates for X such that the distance AX equals BC's length
    X_x = A.x + BC_length * np.cos(theta)
    X_y = A.y + BC_length * np.sin(theta)

    # Ensure X is within a valid range, if there's such a constraint
    assert assert_coord_in_range(X_x, X_y)

    tk = random.randint(1,4)
    diagram.lines.append(Line(B, C, label="", tickmarks=tk))

    X_label = label_point(diagram)
    X = Point(X_x, X_y, X_label)

    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label})')
    diagram.lines.append(Line(A, X, label="", tickmarks=tk))
    # diagram.entities.append(f'Line({A.label}{X.label}) such that {A.label}{X.label}={B.label}{C.label}')
    diagram.entities.append(('eqdistance', [A.label, B.label, C.label, X.label]))
    return diagram


def foot(diagram, A: Point = None, B: Point = None, C: Point = None):
    if A is None:
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
    assert assert_coord_in_range(X_x, X_y)

    # if not line_already_in(diagram, B, C):
    #     diagram.lines.append(Line(B, C, label=""))
    #     diagram.entities.append(f'Line({B.label}{C.label})')


    # Update the diagram with the new point and potentially the line AX for clarity
    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label}) : foot of {A.label} to {B.label}{C.label}')
    diagram.lines.append(Line(A, X, label=""))

    # Optionally, label the perpendicular line AX if needed
    # diagram.entities.append(f'Line({A.label}{X.label}), perpendicular to {B.label}{C.label})')
    diagram.entities.append(('foot', [A.label, B.label, C.label, X.label]))
    diagram.perpendiculars.append((Line(A, X, label=""), Line(B, C, label=""), X))

    return diagram

def incenter(diagram: Diagram):
    # Randomly select three points A, B, and C
    A, B, C = random.sample(diagram.points, 3)

    length_AB = np.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
    length_BC = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)
    length_CA = np.sqrt((A.x - C.x) ** 2 + (A.y - C.y) ** 2)

    X_x = (length_BC * A.x + length_CA * B.x + length_AB * C.x) / (length_AB + length_BC + length_CA)
    X_y = (length_BC * A.y + length_CA * B.y + length_AB * C.y) / (length_AB + length_BC + length_CA)
    assert assert_coord_in_range(X_x, X_y)
    X_label = label_point(diagram)
    X = Point(X_x, X_y, X_label)

    #radius of the incircle
    s = (length_AB + length_BC + length_CA) / 2
    radius = (s * (s - length_AB) * (s - length_BC) * (s - length_CA)) ** 0.5 / s

    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])

    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label}) : incenter of {A.label}{B.label}{C.label}')


    diagram.circles.append(Circle(X, radius, ''))
    # diagram.entities.append(f'Incircle({X.label},{radius}) for triangle {A.label}{B.label}{C.label}')
    diagram.entities.append(('incenter', [A.label, B.label, C.label, X.label, f'{radius}']))
    return diagram

def incenter2(diagram: Diagram):
    # Randomly select three points A, B, and C
    A, B, C = random.sample(diagram.points, 3)

    length_AB = np.sqrt((B.x - A.x) ** 2 + (B.y - A.y) ** 2)
    length_BC = np.sqrt((C.x - B.x) ** 2 + (C.y - B.y) ** 2)
    length_CA = np.sqrt((A.x - C.x) ** 2 + (A.y - C.y) ** 2)

    X_x = (length_BC * A.x + length_CA * B.x + length_AB * C.x) / (length_AB + length_BC + length_CA)
    X_y = (length_BC * A.y + length_CA * B.y + length_AB * C.y) / (length_AB + length_BC + length_CA)
    assert assert_coord_in_range(X_x, X_y)
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
    diagram.points.extend([touch_AB, touch_BC, touch_CA])
    # diagram.entities.extend(
        # [f'touchPoint({touch_AB.label})', f'touchPoint({touch_BC.label})', f'touchPoint({touch_CA.label})'])

    diagram.circles.append(Circle(X, radius, f'Incenter Circle({X.label},{radius})'))

    # diagram.entities.append(f'Incircle({X.label},{radius}) for triangle {A.label}{B.label}{C.label}, with touchpoints {touch_AB.label}, {touch_BC.label}, {touch_CA.label}')
    diagram.entities.append(('incenter2', [A.label, B.label, C.label, X.label, f'{radius}', touch_AB.label, touch_BC.label, touch_CA.label]))
    diagram.perpendiculars.append((Line(X, touch_AB, ''), Line(A, B, ''), touch_AB))
    diagram.perpendiculars.append((Line(X, touch_BC, ''), Line(B, C, ''), touch_BC))
    diagram.perpendiculars.append((Line(X, touch_CA, ''), Line(C, A, ''), touch_CA))

    return diagram

def midpoint(diagram: Diagram, line = None):
    A, B = random.sample(diagram.points, 2)

    X_x = (A.x + B.x) / 2
    X_y = (A.y + B.y) / 2

    X_label = label_point(diagram)

    X = Point(X_x, X_y, X_label)

    tk = random.randint(1,5)
    diagram.lines.append(Line(A, X, label="", tickmarks=tk))
    diagram.lines.append(Line(X, B, label="", tickmarks=tk))


    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label}) : midpoint of Line({A.label}{B.label})')
    diagram.entities.append(('midpoint', [A.label, B.label, X.label]))
    return diagram

def perp_line(diagram):
    l = random.choice(diagram.lines)
    A = l.point1
    B = l.point2
    length_AB = ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5

    perp_vector = (B.y - A.y, A.x - B.x)

    ind = 0
    while True:
        length = random.uniform(-1.5, 1.5) * length_AB
        C_x = A.x + perp_vector[0] * length
        C_y = A.y + perp_vector[1] * length
        if assert_coord_in_range(C_x, C_y):
            break
        if ind > 30:
            return diagram
        ind = ind + 1
    ind = 0
    C_label = label_point(diagram)
    C = Point(C_x, C_y, C_label)
    diagram.points.append(C)

    ind = 0
    while True:
        label = random.choice(small_letters.candidates)
        if label not in [line.label for line in diagram.lines]:
            break
        if ind > 30:
            return diagram
        ind = ind + 1

    diagram.lines.append(Line(A, C, label))
    # diagram.entities.append(f'Line({A.label}{C.label}) perpendicular to Line({A.label}{B.label})')
    diagram.entities.append(('perp_line', [A.label, B.label, C.label]))
    diagram.perpendiculars.append( ( Line(A, C, label), l, C) )
    return diagram



def circle_proj(diagram: Diagram, circle = None):
    # Randomly select a circle and a point on the circle
    if circle is None:
        circle = random.choice(diagram.circles)
    center = circle.center
    radius = circle.radius
    point = random.choice(diagram.points)

    vector = (point.x - center.x, point.y - center.y)
    distance = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    assert distance > 1.1 * radius

    # Normalize the vector
    unit_vector = normalize(vector)

    # Calculate the tangent point
    tangent_x = center.x + radius * unit_vector[0]
    tangent_y = center.y + radius * unit_vector[1]

    tangent_label = label_point(diagram)

    tangent_point = Point(tangent_x, tangent_y, tangent_label)

    # Add the tangent point to the diagram
    diagram.points.append(tangent_point)
    diagram.lines.append(Line(center,point, label=""))
    # diagram.entities.append(f'Point({tangent_label}) projected from Point{point.label} to Circle({center.label},{radius})')
    diagram.entities.append(('circle_proj', [point.label, center.label, f'{radius}', tangent_label]))

    return diagram



def mirror(diagram : Diagram):
    # given A, O, find B such that O is the midpoint of AB

    A, O = random.sample(diagram.points, 2)
    if A == O:
        return diagram
    vector = (O.x - A.x, O.y - A.y)

    B_x = O.x + vector[0]
    B_y = O.y + vector[1]

    assert assert_coord_in_range(B_x, B_y)

    B_label = label_point(diagram)

    B = Point(B_x, B_y, B_label)

    tk = random.randint(1,5)
    diagram.lines.append(Line(A, O, label="", tickmarks=tk))
    diagram.lines.append(Line(O, B, label="", tickmarks=tk))

    diagram.points.append(B)
    # diagram.entities.append(f'Point({B.label}) : mirror of {A.label} over {O.label}')
    diagram.entities.append(('mirror', [A.label, O.label, B.label]))
    return diagram

def right_iso(diagram: Diagram):
    #given A, B, find C such that ABC is a right isosceles triangle
    A, B = random.sample(diagram.points, 2)
    if A == B:
        return diagram

    vector = (B.x - A.x, B.y - A.y)

    if assert_coord_in_range(A.x + vector[1], A.y - vector[0]):
        C_x, C_y = A.x + vector[1], A.y - vector[0]
    else:
        C_x, C_y = A.x - vector[1], A.y + vector[0]

    assert assert_coord_in_range(C_x, C_y)

    ind = 0
    C_label = label_point(diagram)
    C = Point(C_x, C_y, C_label)
    diagram.points.append(C)

    tk = random.randint(0,5)

    diagram.lines.extend([Line(A, B, label="", tickmarks=tk), Line(B, C, label=""), Line(C, A, label="", tickmarks=tk)])
    # diagram.entities.append(f'Right Equilateral Triangle({B.label}{A.label}{C.label})')
    diagram.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
    diagram.entities.append(('right_iso', [A.label, B.label, C.label]))

    return diagram

def on_bline(diagram: Diagram):
    #"X = on_bline(X, A, B)": { "Description": "Construct X on the perpendicular bisector of AB" },
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

    assert assert_coord_in_range(X_x, X_y)
    assert assert_coord_in_range(O.x + radius, O.y + radius) and assert_coord_in_range(O.x - radius,
                                                                                                 O.y - radius)
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
    A, B = random.sample(diagram.points, 2)
    vector = (B.x - A.x, B.y - A.y)
    X_label = label_point(diagram)
    diagram.lines.append(Line(A, B, label="",infinite=True))
    ind = 0
    while True:
        scale = random.uniform(1.1, 3)
        X_x = A.x + scale * vector[0]
        X_y = A.y + scale * vector[1]
        if assert_coord_in_range(X_x, X_y):
            break
        if ind > 30:
            return diagram
        ind = ind + 1
    X = Point(X_x, X_y, X_label)
    diagram.points.append(X)
    # diagram.entities.append(f'Point({X.label}) on Line({A.label}{B.label})')
    diagram.entities.append(('on_line', [A.label, B.label, X.label]))

    return diagram

def on_pline(diagram: Diagram):
    #"X = on_pline(A, B, C)": { "Description": "Construct X such that XA is parallel to BC" },
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

    tk = random.randint(1,5)
    diagram.lines.append(Line(A, B, label="", tickmarks=tk))
    diagram.lines.append(Line(C, X, label="", tickmarks=tk))

    # diagram.entities.append(f'Line({C.label}{X.label}) parallel to Line({A.label}{B.label})')
    diagram.entities.append(('on_pline', [A.label, B.label, C.label, X.label]))
    return diagram

def parallelogram(diagram: Diagram):
    #"X = parallelogram(A, B, C)": { "Description": "Construct X such that ABCX is a parallelogram" },
    A, B, C = random.sample(diagram.points, 3)
    vector = (B.x - A.x, B.y - A.y)
    D_x = C.x - vector[0]
    D_y = C.y - vector[1]
    assert assert_coord_in_range(D_x, D_y)

    D_label = label_point(diagram)

    D = Point(D_x, D_y, D_label)
    diagram.points.append(D)
    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
    # diagram.entities.append(f'Parallelogram({A.label}{B.label}{C.label}{D.label})')
    diagram.entities.append(('parallelogram', [A.label, B.label, C.label, D.label]))
    return diagram



def pentagon(diagram: Diagram):
    #"Pentagon(A, B, C, D, E)": { "Description": "Construct a pentagon with vertices A, B, C, D, E" },
    randnum = random.randint(0, 3)
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
    assert len(points) == 5

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

def trapezoid(diagram : Diagram):
    A , B = random.sample(diagram.points, 2)
    vector = (B.x - A.x, B.y - A.y)
    while True:
        C_x, C_y = random_coord(), random_coord()
        C_label = label_point(diagram)
        if assert_coord_in_range(C_x, C_y):
            break
    C = Point(C_x, C_y, C_label)

    ind  = 0
    while True:
        scale = random.uniform(0.5, 3)
        D_x = C.x + scale * vector[0]
        D_y = C.y + scale * vector[1]
        D_label = label_point(diagram)
        if assert_coord_in_range(D_x, D_y) and D_label != C_label:
            break
        ind += 1
        if ind > 10 :
            return diagram
    D = Point(D_x, D_y, D_label)

    tk = random.randint(1,5)

    diagram.points.extend([C, D])
    diagram.lines.extend([Line(A, B, label="", tickmarks=tk), Line(B, D, label=""), Line(C, D, label="", tickmarks=tk), Line(C, A, label="")])
    # diagram.entities.append(f'Trapezoid({A.label}{B.label}{C.label}{D.label})')
    diagram.entities.append(('trapezoid', [A.label, B.label, C.label, D.label]))
    return diagram

def r_triangle(diagram):
    A, B = random.sample(diagram.points, 2)
    perp_vector = (B.y - A.y, A.x - B.x)
    ind = 0
    while True:
        scale = random.uniform(-4, 4)
        C_x = A.x + scale * perp_vector[0]
        C_y = A.y + scale * perp_vector[1]
        C_label = label_point(diagram)
        if assert_coord_in_range(C_x, C_y):
            break
        if ind > 30:
            return diagram
        ind+=1

    C = Point(C_x, C_y, C_label)
    diagram.points.append(C)

    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])
    # diagram.entities.append(f'Right Triangle({A.label}{B.label}{C.label})')
    diagram.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
    diagram.entities.append(('r_triangle', [A.label, B.label, C.label]))
    return diagram


def rectangle(diagram):
    A, B = random.sample(diagram.points, 2)
    vector = (B.x - A.x, B.y - A.y)
    perp_vector = (vector[1], -vector[0])
    ind = 0
    while True:
        scale = random.uniform(-4, 4)
        C_x = B.x + scale * perp_vector[0]
        C_y = B.y + scale * perp_vector[1]
        D_x = A.x + scale * perp_vector[0]
        D_y = A.y + scale * perp_vector[1]
        C_label = label_point(diagram)
        D_label = label_point(diagram)
        if assert_coord_in_range(C_x, C_y) and assert_coord_in_range(D_x, D_y) and D_label != C_label:
            break
        if ind>30:
            return diagram
        ind +=1
    C = Point(C_x, C_y, C_label)
    D = Point(D_x, D_y, D_label)
    diagram.points.extend([C, D])

    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
    # diagram.entities.append(f'Rectangle({A.label}{B.label}{C.label}{D.label})')
    diagram.entities.append(('rectangle', [A.label, B.label, C.label, D.label]))
    diagram.perpendiculars.append((Line(A, B, label=""), Line(A, D, label=""), A))
    diagram.perpendiculars.append((Line(B, C, label=""), Line(B, A, label=""), B))
    diagram.perpendiculars.append((Line(C, D, label=""), Line(C, B, label=""), C))
    diagram.perpendiculars.append((Line(D, A, label=""), Line(D, C, label=""), D))

    return diagram

def reflect(diagram):
    #"X = reflect(A, B, C)": { "Description": "Construct X as the reflection of A about BC" },
    A, B, C = random.sample(diagram.points, 3)
    vec_BC = (C.x - B.x, C.y - B.y)
    vec_BA = (A.x - B.x, A.y - B.y)
    foot_x = B.x + np.dot(vec_BC, vec_BA) / np.dot(vec_BC, vec_BC) * vec_BC[0]
    foot_y = B.y + np.dot(vec_BC, vec_BA) / np.dot(vec_BC, vec_BC) * vec_BC[1]
    X_x = A.x + 2 * (foot_x - A.x)
    X_y = A.y + 2 * (foot_y - A.y)

    assert assert_coord_in_range(X_x, X_y)

    X_label = label_point(diagram)
    X = Point(X_x, X_y, X_label)
    diagram.points.append(X)

    diagram.lines.extend([Line(A, X, label=""), Line(B, C, label="", infinite=True)])
    # diagram.entities.append(f'Point({X.label}) : reflection of {A.label} over Line({B.label}{C.label})')
    diagram.entities.append(('reflect', [A.label, B.label, C.label, X.label]))
    return diagram

# def angle(diagram : Diagram, angle = None):
#     if angle is None:
#         angle = random.uniform(np.pi/6, np.pi)
#     l = random.choice(diagram.lines)
#     A, B = l.point1, l.point2
#
#     #Construct X such that angle ABX = angle
#     vec_AB = (B.x - A.x, B.y - A.y)
#     vec_AX_unscaled = (vec_AB[0]*np.cos(angle) - vec_AB[1]*np.sin(angle), vec_AB[0]*np.sin(angle) + vec_AB[1]*np.cos(angle))
#     ind = 0
#     while True:
#         scale = random.uniform(0.5, 3)
#         X_x = A.x + scale * vec_AX_unscaled[0]
#         X_y = A.y + scale * vec_AX_unscaled[1]
#         if assert_coord_in_range(X_x, X_y):
#             break
#         ind +=1
#         if ind > 10 :
#             return diagram
#
#     while True:
#         X_label = random.choice(capitals.candidates)
#         if X_label not in [point.label for point in diagram.points]:
#             break
#
#     X = Point(X_x, X_y, X_label)
#     diagram.points.append(X)
#
#     diagram.lines.append(Line(A, X, label=""))
#
#
#     # diagram.entities.append(f'Point({X.label}) such that angle {B.label}{A.label}{X.label} = {angle}')
#     diagram.entities.append(('angle', [A.label, B.label, X.label, angle]))
#     return diagram

def square(diagram):
    l = random.choice(diagram.lines)
    A, B = l.point1, l.point2
    vector = random.choice( [(B.x - A.x, B.y - A.y), (A.x - B.x, A.y - B.y)])


    perp_vector = (vector[1], -vector[0])
    C_x, C_y = A.x + perp_vector[0], A.y +perp_vector[1]
    D_x, D_y = B.x + perp_vector[0], B.y + perp_vector[1]
    if not (assert_coord_in_range(C_x, C_y) and assert_coord_in_range(D_x, D_y)):
        C_x, C_y = A.x - perp_vector[0], A.y -  perp_vector[1]
        D_x, D_y = B.x - perp_vector[0], B.y -  perp_vector[1]
        if not (assert_coord_in_range(C_x, C_y) and assert_coord_in_range(D_x, D_y)):
            return diagram

    lable_C = label_point(diagram)
    label_D = label_point(diagram)
    C = Point(C_x, C_y, lable_C)
    D = Point(D_x, D_y, label_D)
    diagram.points.extend([C, D])

    tk = random.choice([1,2,3,4,5,0,0,0,0,0,0])

    diagram.lines.extend([Line(A, B, label="", tickmarks=tk), Line(B, D, label="", tickmarks=tk),
                          Line(C, D, label="", tickmarks=tk), Line(C, A, label="",tickmarks=tk)])

    # diagram.entities.append(f'Square({A.label}{B.label}{D.label}{C.label})')
    diagram.entities.append(('square', [A.label, B.label, D.label,C.label]))
    diagram.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
    diagram.perpendiculars.append((Line(D, C, label=""), Line(D, B, label=""), D))
    diagram.perpendiculars.append((Line(A, B, label=""), Line(B, D, label=""), B))
    diagram.perpendiculars.append((Line(C, D, label=""), Line(C, A, label=""), C))
    print(f"A B C D label : {A.label} {B.label} {C.label} {D.label}")
    return diagram


def init_square(diagram):
    #"A, B, C, D = init_square()": { "Description": "Construct square ABCD" },
    A = Point( random_coord(), random_coord(), label_point(diagram))
    B = Point( random_coord(), random_coord(), label_point(diagram))

    vector = (B.x - A.x, B.y - A.y)
    len = (vector[0] ** 2 + vector[1] ** 2) ** 0.5

    perp_vector = (vector[1], -vector[0])
    C_x, C_y = A.x + perp_vector[0], A.y + perp_vector[1]
    D_x, D_y = B.x + perp_vector[0], B.y + perp_vector[1]
    if not (assert_coord_in_range(C_x, C_y) and assert_coord_in_range(D_x, D_y)):
        C_x, C_y = A.x - perp_vector[0], A.y - perp_vector[1]
        D_x, D_y = B.x - perp_vector[0], B.y - perp_vector[1]
        if not (assert_coord_in_range(C_x, C_y) and assert_coord_in_range(D_x, D_y)):
            return diagram

    lable_C = label_point(diagram)
    label_D = label_point(diagram)
    C = Point(C_x, C_y, lable_C)
    D = Point(D_x, D_y, label_D)
    diagram.points.extend([A,B,C, D])

    tk = random.choice([1,2,3,4,5,0,0,0,0,0,0])

    diagram.lines.extend([Line(A, B, label="", tickmarks=tk), Line(B, D, label="", tickmarks=tk),
                          Line(C, D, label="", tickmarks=tk), Line(C, A, label="", tickmarks=tk)])

    # diagram.entities.append(f'Square({A.label}{B.label}{D.label}{C.label})')
    diagram.entities.append(('square', [A.label, B.label, D.label,C.label]))
    diagram.perpendiculars.append((Line(A, B, label=""), Line(A, C, label=""), A))
    diagram.perpendiculars.append((Line(D, C, label=""), Line(D, B, label=""), D))
    diagram.perpendiculars.append((Line(A, B, label=""), Line(B, D, label=""), B))
    diagram.perpendiculars.append((Line(C, D, label=""), Line(C, A, label=""), C))

    return diagram

def init_triangle(diagram):
    A = Point(random_coord(), random_coord(), label_point(diagram))
    while True:
        B = Point(random_coord(), random_coord(), label_point(diagram))
        if B.label != A.label:
            break
    while True:
        C = Point(random_coord(), random_coord(), label_point(diagram))
        if C.label != A.label and C.label != B.label:
            break

    diagram.points.extend([A, B, C])
    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])
    # diagram.entities.append(f'Triangle({A.label}{B.label}{C.label})')
    diagram.entities.append(('triangle', [A.label, B.label, C.label]))
    return diagram

def init_triangle_ratio(diagram):
    #construct triangle ABC with AB : BC = 1: 2
    B = Point(random_coord(), random_coord(), label_point(diagram))
    while True:
        length = random.uniform(50 , 300)
        angle1 = random_angle()
        angle2 = random_angle()
        ratio = random.randint(1, 4)

        A_x = B.x + length * np.cos(angle1)
        A_y = B.y + length * np.sin(angle1)
        C_x = B.x + ratio*length * np.cos(angle2)
        C_y = B.y + ratio*length * np.sin(angle2)

        if assert_coord_in_range(A_x, A_y) and assert_coord_in_range(C_x, C_y):
            break

    A = Point(A_x, A_y, label_point(diagram))
    C = Point(C_x, C_y, label_point(diagram))

    diagram.points.extend([A, B, C])
    diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label="")])
    diagram.entities.append(('triangle12', [A.label, B.label, C.label, f'{ratio}']))
    return diagram

def tangent(diagram):
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
    print("perp_vec = ", perp_vec)
    ind = 0
    while True:
        scale = random.uniform(-3, 3)

        perp_vec[0] = scale * perp_vec[0]
        perp_vec[1] = scale * perp_vec[1]
        new_label = label_point(diagram)

        if ind > 100:
            return diagram
        if assert_coord_in_range(point.x+perp_vec[0], point.y+perp_vec[1]):
            break
        ind +=1



    assert assert_coord_in_range(point.x+perp_vec[0], point.y+perp_vec[1])
    rand = random.choice([True, False])
    if rand :
        is_inf, inf_label = (True,f'Infinite tangent line at {T_label}')
        diagram.entities.append(('inf_tangent', [center.label, T_label]))

    else:
        is_inf, inf_label = (False, f'Line({T_label}{new_label}) tangent')
        diagram.points.append(Point(point.x + perp_vec[0], point.y + perp_vec[1], new_label))
        diagram.entities.append(('tangent', [center.label, T_label, new_label]))


    diagram.points.append(point)
    diagram.lines.append(Line(center, point, label=""))
    diagram.lines.append(Line(point, Point(point.x + perp_vec[0], point.y + perp_vec[1], ""), label="", infinite=is_inf))
    # diagram.entities.append(inf_label + f' to Circle({center.label},{radius})')

    return diagram


def trisect(diagram):
    while True:
        p1_x, p1_y = random_coord(), random_coord()
        if assert_coord_in_range(p1_x, p1_y):
            break
    ang0 = random_angle()
    ang = random.uniform(np.pi/8, np.pi/4)

    ind = 0
    while True:
        length1, length2, length3, length4 = random.uniform(50 , 500), random.uniform(50 , 500), random.uniform(50 , 500), random.uniform(50 , 500)
        p2_x, p2_y = p1_x + length1 * np.cos(ang0), p1_y + length1 * np.sin(ang0)
        p3_x, p3_y = p2_x + length2 * np.cos(ang0+ang), p2_y + length2 * np.sin(ang0+ang)
        p4_x, p4_y = p3_x + length3 * np.cos(ang0+2*ang), p3_y + length3 * np.sin(ang0+2*ang)
        p5_x, p5_y = p4_x + length4 * np.cos(ang0+3*ang), p4_y + length4 * np.sin(ang0+3*ang)
        if assert_coord_in_range(p2_x, p2_y) and assert_coord_in_range(p3_x, p3_y) and assert_coord_in_range(p4_x, p4_y) and assert_coord_in_range(p5_x, p5_y):
            break
        ind += 1
        if ind > 30:
            return diagram


    p1 = Point(p1_x, p1_y, label_point(diagram))
    while True:
        p2_label = label_point(diagram)
        if p2_label != p1.label:
            p2 = Point(p2_x, p2_y, p2_label)
            break

    while True:
        p3_label = label_point(diagram)
        if p3_label != p1.label and p3_label != p2.label:
            p3 = Point(p3_x, p3_y, p3_label)
            break
    while True:
        p4_label = label_point(diagram)
        if p4_label != p1.label and p4_label != p2.label and p4_label != p3.label:
            p4 = Point(p4_x, p4_y, p4_label)
            break
    while True:
        p5_label = label_point(diagram)
        if p5_label != p1.label and p5_label != p2.label and p5_label != p3.label and p5_label != p4.label:
            p5 = Point(p5_x, p5_y, p5_label)
            break


    diagram.points.extend([p1, p2, p3, p4, p5])
    diagram.lines.extend([Line(p1, p2, label=""), Line(p1, p3, label=""), Line(p1, p4, label=""), Line(p1, p5, label="")])
    # diagram.entities.append(f'Line({p1.label}{p3.label}) and Line({p1.label}{p4.label}) trisects angle {p5.label}{p1.label}{p2.label}')
    diagram.entities.append(('trisect', [p1.label, p2.label, p3.label, p4.label, p5.label]))
    return diagram


def trisegment(d):
    l = random.choice(d.lines)
    A, B = l.point
    1, l.point2
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

    tk = random.randint(1,5)
    d.lines.extend([Line(A, p1, label="", tickmarks=tk), Line(p1, p2, label="", tickmarks=tk), Line(p2, B, label="", tickmarks=tk)])
    # d.entities.append(f'Line({A.label}{p1.label}) = Line({p1.label}{p2.label}) = Line({p2.label}{B.label})')
    d.entities.append(('trisegment', [A.label, B.label, p1.label, p2.label]))
    return d

def c_tangent(d):
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

    p1_x, p1_y = c1_center.x + c1_radius * np.cos(angle + angle0), c1_center.y + c1_radius * np.sin(angle+angle0)
    p2_x, p2_y = c1_center.x + c1_radius * np.cos(-angle + angle0), c1_center.y + c1_radius * np.sin(-angle+angle0)

    label = label_point(d)
    p1_label = label + '1'
    p2_label = label + '2'
    P_label = label_point(d)
    assert P_label != label


    p1 = Point(p1_x, p1_y, p1_label)
    p2 = Point(p2_x, p2_y, p2_label)
    P = Point(x, y, P_label)
    d.points.extend([p1, p2, P])
    d.lines.extend([Line(p1, P, label=""), Line(p2, P, label=""),])
    # d.entities.append(f'Line({p1.label}{P.label}) and Line({p2.label}{P.label}) are tangent to Circle({c1_center.label},{c1_radius})')
    if random.choice([True, False]):
        x,y,l = add_radius(c1_center.x, c1_center.y, c1_radius)
        d.lines.append(Line(c1_center, Point(x,y,""), label=l, dotted=True))
        d.entities.append(('c_tangent_with_r', [c1_center.label, l, p1.label, p2.label, P.label]))
    else:
           d.entities.append(('c_tangent', [c1_center.label, p1.label, p2.label, P.label]))
    return d


def cc_tangent(d):

    ind = 0
    while True:
        c1_center = random.choice(d.points)
        c1_radius = random.uniform(100, 400)
        if assert_coord_in_range(c1_center.x + c1_radius, c1_center.y + c1_radius) and assert_coord_in_range(c1_center.x - c1_radius, c1_center.y - c1_radius):
            break
        if ind > 100:
            return d
        ind += 1

    ind = 0
    while True:
        # x, y = random_coord(), random_coord()
        # length = np.linalg.norm([x - c1_center.x, y - c1_center.y])
        # if length > 2 * c1_radius:
        #     break
        angle = random_angle()
        distance = random.uniform(2, 5) * c1_radius
        x = c1_center.x + distance * np.cos(angle)
        y = c1_center.y + distance * np.sin(angle)
        if assert_coord_in_range(x,y):
            break
        if ind > 100:
            return d
        ind += 1

    angle0 = np.arctan((y - c1_center.y) / (x - c1_center.x))
    if x < c1_center.x:
        angle0 += np.pi
    angle = np.arccos(c1_radius / distance)

    p1_x, p1_y = c1_center.x + c1_radius * np.cos(angle + angle0), c1_center.y + c1_radius * np.sin(angle + angle0)
    p2_x, p2_y = c1_center.x + c1_radius * np.cos(-angle + angle0), c1_center.y + c1_radius * np.sin(-angle + angle0)

    label = label_point(d)
    p1_label = label + '1'
    p2_label = label + '2'
    P_label = label_point(d)
    assert P_label != label

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

def cc_tangent_one(d):
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius
    ind = 0
    while True:
        x, y = random_coord(), random_coord()
        length = np.linalg.norm([x - c1_center.x, y - c1_center.y])
        if length > 5 * c1_radius:
            break
        if ind > 100:
            return d
        ind += 1

    angle0 = np.arctan((y - c1_center.y) / (x - c1_center.x))
    if x < c1_center.x:
        angle0 += np.pi
    angle = np.arccos(c1_radius / length)

    p1_x, p1_y = c1_center.x + c1_radius * np.cos(angle + angle0), c1_center.y + c1_radius * np.sin(angle + angle0)


    label = label_point(d)
    p1_label = label + '1'

    P_label = label_point(d)
    assert P_label != label

    p1 = Point(p1_x, p1_y, p1_label)

    P = Point(x, y, P_label)

    vec_x, vec_y = c1_center.x - x, c1_center.y - y
    while True:
        scale = random. uniform(0.2, 1)
        x1, y1 = x + scale * vec_x, y + scale * vec_y
        rad_1 = c1_radius * scale
        if np.linalg.norm([x1 - c1_center.x, y1 - c1_center.y]) > c1_radius + rad_1:
            break
    c2_center = Point(x1, y1, label_point(d))
    c2 = Circle(c2_center, rad_1, '')
    t1_x, t1_y = scale * (p1_x - x) + x, scale * (p1_y - y) + y

    t_label = label_point(d)
    t1 = Point(t1_x, t1_y, t_label + '1')

    d.points.extend([t1])
    d.points.append(c2.center)
    d.circles.append(c2)

    d.points.extend([p1, P])
    d.lines.extend([Line(p1, P, label="") ])
    # d.entities.append(
    #     f'Line({p1.label}{P.label}) is tangent to both Circle({c1_center.label},{c1_radius}) and Circle({c2_center.label},{rad_1})')
    d.entities.append(('cc_tangent_one', [c1_center.label, f'{c1_radius}', c2_center.label, f'{rad_1}', p1.label, P.label]))
    return d

def parallel(d):
    l = random.choice(d.lines)
    A, B = l.point1, l.point2

    vector = (B.x - A.x, B.y - A.y)

    tk = random.randint(0,5)

    while True:
        scale = random.uniform(-3, 3)
        x,y = random_coord(), random_coord()
        if assert_coord_in_range(x+vector[0]*scale, y+vector[1]*scale):
            break

    while True:

        C = Point(x+vector[0]*scale, y+vector[1]*scale, label_point(d))
        D = Point(x, y, label_point(d))
        if C.label != D.label:
            break

    d.points.extend([C, D])
    d.lines.append(Line(C, D, label="", infinite=random.choice([True, False]), tickmarks=tk))
    d.lines.append(Line(A, B, label="", tickmarks=tk))
    # d.entities.append(f'Line({C.label}{D.label}) parallel to Line({A.label}{B.label})')
    d.entities.append(('parallel', [A.label, B.label, C.label, D.label]))
    return d

def intersect_ll(d):
    l = random.choice(d.lines)
    A, B = l.point1, l.point2
    vec = (B.x - A.x, B.y - A.y)
    scale = random.uniform(0.15, 0.85)

    x, y = A.x + scale * vec[0], A.y + scale * vec[1]
    label = label_point(d)
    P = Point(x, y, label)

    C_x, C_y = random_coord(), random_coord()
    vec_PC = (C_x - P.x, C_y - P.y)
    ind = 0
    while True:
        scale = random.uniform(-3, 0)
        D_x, D_y = P.x + scale * vec_PC[0], P.y + scale * vec_PC[1]
        if assert_coord_in_range(D_x, D_y):
            break
        if ind > 10:
            return d
        ind += 1

    ind = 0
    while True:
        C_label = label_point(d)
        D_label = label_point(d)
        if C_label != D_label and label != C_label and label != D_label:
            break
        if ind > 10:
            return d
        ind += 1
    C = Point(C_x, C_y, C_label)
    D = Point(D_x, D_y, D_label)

    d.points.extend([P, C, D])
    d.lines.append(Line(D, C, label="", infinite = random.choice([True, False])))
    # d.entities.append(f'Line({C.label}{D.label}) intersects Line({A.label}{B.label}) at {P.label}')
    d.entities.append(('intersect_ll', [A.label, B.label, C.label, D.label, P.label]))
    return d

def intersect_cl(d):
    c = random.choice(d.circles)
    center = c.center
    radius = c.radius

    ang0 = random_angle()
    ang1 = random.uniform(np.pi/4, 7*np.pi/4)

    x0, y0 = center.x + radius * np.cos(ang0), center.y + radius * np.sin(ang0)
    x1, y1 = center.x + radius * np.cos(ang1+ang0), center.y + radius * np.sin(ang1+ang0)
    vec= (x1 - x0, y1 - y0)

    ind = 0
    while True:
        scale0, scale1 = random.uniform(-5, -0.2), random.uniform(1.2, 5)
        X0, Y0 = x0 + scale0 * vec[0], y0 + scale0 * vec[1]
        X1, Y1 = x0 + scale1 * vec[0], y0 + scale1 * vec[1]
        if assert_coord_in_range(X0, Y0) and assert_coord_in_range(X1, Y1):
            break
        if ind > 10:
            return d
        ind +=1
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
    # d.entities.append(f'Line({P0.label}{P1.label}) intersects Circle({center.label},{radius}) at {p0.label} and {p1.label}')
    d.entities.append(('intersect_cl', [center.label, f'{radius}', p0.label, p1.label, P0.label, P1.label]))
    return d

def intersect_cc(d):
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius

    c2_radius = random.uniform(0.75, 3) * c1_radius
    ind = 0
    while True:
        angle = random_angle()
        scale = random.uniform(1.25, 5)
        x, y = c1_center.x + scale * c1_radius * np.cos(angle), c1_center.y + scale * c1_radius * np.sin(angle)
        if assert_coord_in_range(x, y) and np.linalg.norm([x - c1_center.x, y - c1_center.y]) < c1_radius + c2_radius:
            if assert_coord_in_range(x + c2_radius, y+ c2_radius) and assert_coord_in_range(x - c2_radius, y - c2_radius):
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
    # d.entities.append(f'Circle({c1_center.label},{c1_radius}) intersects Circle({c2_center.label},{c2_radius}) at {p1.label} and {p2.label}')
    d.entities.append(('intersect_cc', [c1_center.label, f'{c1_radius}', c2_center.label, f'{c2_radius}', p1.label, p2.label]))
    return d



def touches_cc(d):
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius


    ind = 0
    while True:
        angle = random_angle()
        c2_radius = random.uniform(0.75, 3) * c1_radius
        scale = c1_radius + c2_radius
        x, y = c1_center.x + scale *  np.cos(angle), c1_center.y + scale * np.sin(angle)
        if assert_coord_in_range(x, y):
            if assert_coord_in_range(x + c2_radius, y+ c2_radius) and assert_coord_in_range(x - c2_radius, y - c2_radius):
                break
        if ind > 30:
            return d
        ind += 1

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

def touches_clc(d):
    c1 = random.choice(d.circles)
    c1_center = c1.center
    c1_radius = c1.radius

    ind = 0
    while True:
        angle = random_angle()
        c2_radius = random.uniform(0.75, 3) * c1_radius
        scale = c1_radius + c2_radius
        x, y = c1_center.x + scale * np.cos(angle), c1_center.y + scale * np.sin(angle)
        if assert_coord_in_range(x, y):
            if assert_coord_in_range(x + c2_radius, y + c2_radius) and assert_coord_in_range(x - c2_radius,
                                                                                             y - c2_radius):
                break
        if ind > 30:
            return d
        ind += 1

    c2_label = label_point(d)
    c2_center = Point(x, y, c2_label)
    c2 = Circle(c2_center, c2_radius, '')

    while True:
        label = label_point(d)
        if label != c2_label:
            break
    touchpoint = Point(c1_center.x + c1_radius * np.cos(angle), c1_center.y + c1_radius * np.sin(angle), label)
    perp_vec = normalize((c1_center.y - touchpoint.y, touchpoint.x - c1_center.x))
    ind=0



    while True:
        scale1 = random.uniform(50, 200)
        scale2 = random.uniform(50, 200)
        x1, y1 = touchpoint.x + scale1 * perp_vec[0], touchpoint.y + scale1 * perp_vec[1]
        x2, y2 = touchpoint.x - scale2 * perp_vec[0], touchpoint.y - scale2 * perp_vec[1]
        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break
        if ind > 30:
            return d
        ind += 1
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


def touches_cc2(d):
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
    # d.entities.append(
    #     f'Circle({c1_center.label},{c1_radius}) touches Circle({c2_center.label},{c2_radius}) inside, at {touchpoint.label}')
    d.entities.append(('touches_cc2', [c1_center.label, f'{c1_radius}', c2_center.label, f'{c2_radius}', touchpoint.label]))
    return d

def touches_clc2(d):

    A_x, A_y = random_coord(), random_coord()
    B_x, B_y = random_coord(), random_coord()
    vector = (B_x - A_x, B_y - A_y)
    perp_vec = normalize((vector[1], -vector[0]))

    scale1, scale2 = random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)
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
    while True:
        c1_radius = random.uniform(50, 500)
        c2_radius = random.uniform(50, 500)
        c1_x, c1_y = x1 + c1_radius * perp_vec[0], y1 + c1_radius * perp_vec[1]
        c2_x, c2_y = x2 - c2_radius * perp_vec[0], y2 - c2_radius * perp_vec[1]
        if assert_coord_in_range(c1_x+ c1_radius, c1_y+ c1_radius) and assert_coord_in_range(c1_x - c1_radius, c1_y - c2_radius):
            if assert_coord_in_range(c2_x + c2_radius, c2_y + c2_radius) and assert_coord_in_range(c2_x - c2_radius, c2_y - c2_radius):
                break

        if ind > 30:
            return d
        ind += 1

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
    d.lines.append(Line(p1, p2, label="", infinite=True))
    # d.entities.append(f'Circle({c1_center.label},{c1_radius}) and Circle({c2_center.label},{c2_radius}) touching the same line at {p1.label} and {p2.label}')
    d.entities.append(('touches_clc2', [c1_center.label, f'{c1_radius}', c2_center.label, f'{c2_radius}', p1.label, p2.label]))
    return d


def rhombus(d):
    l = random.choice(d.lines)
    A, B = l.point1, l.point2
    vector = (B.x - A.x, B.y - A.y)
    center_x,  center_y, center_label = (A.x+B.x)/2, (A.y+B.y)/2, label_point(d)

    perp_vec = (vector[1], -vector[0])

    ind =0
    while True:
        scale = random.uniform(1/3, 3)
        C_x, C_y = center_x + scale * perp_vec[0], center_y + scale * perp_vec[1]
        D_x, D_y = center_x - scale * perp_vec[0], center_y - scale * perp_vec[1]
        if assert_coord_in_range(C_x, C_y) and assert_coord_in_range(D_x, D_y):
            break
        if ind > 30:
            return d
        ind += 1

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
    # d.entities.append(f'Rhombus({A.label}{C.label}{B.label}{D.label}) with center {center.label}')
    d.entities.append(('rhombus', [A.label, B.label, C.label, D.label, center.label]))
    if random_coord() > 500:
        d.lines.extend([Line(A, C, label=""), Line(B, D, label="")])
        d.perpendiculars.append((Line(A, B, label=""), Line(D, C, label=""), center))

    return d


def random_square(d):
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


def convex_square(d):
    while True:
        P_x, P_y, r = random_coord(), random_coord(), random.uniform(200, 500)
        if assert_coord_in_range(P_x + r, P_y + r) and assert_coord_in_range(P_x - r, P_y - r):
            break

    angle1, angle2, angle3, angle4 = random_angle(), random_angle(), random_angle(), random_angle()
    #sort angles
    angles = [angle1, angle2, angle3, angle4]
    angles.sort()
    angle1, angle2, angle3, angle4 = angles
    A_x, A_y = P_x + r * np.cos(angle1), P_y + r * np.sin(angle1)
    B_x, B_y = P_x + r * np.cos(angle2), P_y + r * np.sin(angle2)
    C_x, C_y = P_x + r * np.cos(angle3), P_y + r * np.sin(angle3)
    D_x, D_y = P_x + r * np.cos(angle4), P_y + r * np.sin(angle4)

    while True:
        A_label, B_label, C_label, D_label = label_point(d), label_point(d), label_point(d), label_point(d)
        if (A_label != B_label and A_label != C_label and A_label != D_label and B_label != C_label and
                B_label != D_label and C_label != D_label):
            break

    A = Point(A_x, A_y, A_label)
    B = Point(B_x, B_y, B_label)
    C = Point(C_x, C_y, C_label)
    D = Point(D_x, D_y, D_label)

    d.points.extend([A, B, C, D])
    d.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
    # d.entities.append(f'Square({A.label}{B.label}{C.label}{D.label})')
    d.entities.append(('convex_quadrilateral', [A.label, B.label, C.label, D.label]))
    return d



def connect_center(d):
    c = random.choice(d.circles)
    center = c.center
    radius = c.radius
    ind = 0
    while True:
        x, y = random_coord(), random_coord()
        length = random.uniform(0.5, 3) * radius
        if assert_coord_in_range(x+length, y+length) and assert_coord_in_range(x-length, y-length):
            break

    c2_label = label_point(d)
    c2_center = Point(x, y, c2_label)
    c2 = Circle(c2_center, radius, '')

    d.points.append(c2_center)
    d.circles.append(c2)
    d.lines.append(Line(center, c2_center, label=""))
    # d.entities.append(f'The centers of Circle({center.label},{radius}) and Circle({c2_center.label},{radius}) are connected with a line')
    d.entities.append(('connect_center', [center.label, f'{center.label}', c2_center.label, f'{radius}']))


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

    d.curves.append(Curve(x, y, label=""))
    # d.entities.append(f'Parabola with vertex ({b},{c})')
    d.entities.append(('parabola', [f'({b},{c})']))
    return d

def parabola_tangent(d):
    a = random.uniform(0, 0.1)
    b = int(random.uniform(200, 800))
    c = int(random.uniform(200, 800))

    t = np.linspace(0, 1000, 1000)
    x0 = t
    y0 = a * (t - b) ** 2 + c

    while True:
        x1 = random.uniform(b-150, b+150)
        y1 = a * (x1 - b) ** 2 + c
        if assert_coord_in_range(x1, y1):
            break
    x2, y2 = (x1+1, y1+2 * a * (x1 - b))

    angle = random_angle()
    x = (x0 - 500) * np.cos(angle) - (y0 - 500) * np.sin(angle) + 500
    y = (x0 - 500) * np.sin(angle) + (y0 - 500) * np.cos(angle) + 500

    p1_x, p1_y = (x1-500)*np.cos(angle) - (y1-500)*np.sin(angle) + 500, (x1-500)*np.sin(angle) + (y1-500)*np.cos(angle) + 500
    p2_x, p2_y = (x2-500)*np.cos(angle) - (y2-500)*np.sin(angle) + 500, (x2-500)*np.sin(angle) + (y2-500)*np.cos(angle) + 500
    p1_label = label_point(d)

    P1 = Point(p1_x, p1_y, p1_label)
    P2 = Point(p2_x, p2_y, "")
    d.points.append(P1)
    d.lines.append(Line(P1, P2, label="",infinite=True))
    d.curves.append(Curve(x, y, label=""))
    # d.entities.append(f'Parabola with vertex ({b},{c}), with tangent line at point {P1.label}')
    d.entities.append(('parabola_tangent', [f'({b},{c})', P1.label]))
    return d

def parab_line_intersect(d):
    a = random.uniform(0, 0.1)
    b = int(random.uniform(200, 800))
    c = int(random.uniform(200, 800))

    t = np.linspace(0, 1000, 1000)
    x0 = t
    y0 = a * (t - b) ** 2 + c

    while True:
        x1 = random.uniform(b, b + 200)
        y1 = a * (x1 - b) ** 2 + c

        x2 = random.uniform(b - 200, b)
        y2 = a * (x2 - b) ** 2 + c

        if assert_coord_in_range(x1, y1) and assert_coord_in_range(x2, y2):
            break

    angle = random_angle()
    x = (x0 - 500) * np.cos(angle) - (y0 - 500) * np.sin(angle) + 500
    y = (x0 - 500) * np.sin(angle) + (y0 - 500) * np.cos(angle) + 500

    p1_x, p1_y = (x1 - 500) * np.cos(angle) - (y1 - 500) * np.sin(angle) + 500, (x1 - 500) * np.sin(angle) + (
                y1 - 500) * np.cos(angle) + 500
    p2_x, p2_y = (x2 - 500) * np.cos(angle) - (y2 - 500) * np.sin(angle) + 500, (x2 - 500) * np.sin(angle) + (
                y2 - 500) * np.cos(angle) + 500
    p1_label = label_point(d)
    while True:
        p2_label = label_point(d)
        if p2_label != p1_label:
            break

    P1 = Point(p1_x, p1_y, p1_label)
    P2 = Point(p2_x, p2_y, p2_label)
    d.points.extend([P1, P2])
    d.lines.append(Line(P1, P2, label="", infinite=True))
    d.curves.append(Curve(x, y, label=""))
    # d.entities.append(f'A parabola and a line intersects at points {P1.label} and {P2.label}')
    d.entities.append(('parab_line_intersect', [P1.label, P2.label]))
    return d

def ellipse(d):
    t = np.linspace(0, 2 * np.pi, 1000)

    while True:
        x,y = int(random_coord()), int(random_coord())
        length1 = int(random.uniform(100, 400))
        angle1 = random_angle()
        length2 = int(random.uniform(1.5, 3) * length1)
        # angle2 = angle1 + np.pi/2

        x0 =  length1 * np.cos(t)
        y0 =  length2 * np.sin(t)

        if assert_coord_in_range(x+length2, y+length2) and assert_coord_in_range(x-length2, y-length2):
            break

    x1 = np.cos(angle1) * x0 - np.sin(angle1) * y0 + x
    y1 = np.sin(angle1) * x0 + np.cos(angle1) * y0 + y

    d.curves.append(Curve(x1, y1, label="ellipse"))
    # d.entities.append(f'Ellipse with center ({x},{y}) and semi-major axis {length2} and semi-minor axis {length1}')
    d.entities.append(('ellipse', [f'({x},{y})', f'{length2}', f'{length1}']))
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

def triangle_with_height(d):
    A_x, A_y = random_coord(), random_coord()
    B_x, B_y = random_coord(), random_coord()
    id = 0
    while True:
        A_label, B_label = label_point(d), label_point(d)
        if A_label != B_label:
            break
        if id > 10:
            return d
        id += 1

    vec = (B_x - A_x, B_y - A_y)
    ratio = random.uniform(0.1, 0.9)
    P_x, P_y = A_x + ratio * vec[0], A_y + ratio * vec[1]
    perp_vec = (vec[1], -vec[0])

    id = 0
    while True:
        scale = random.uniform(0.25, 5) * random.choice([-1, 1])
        C_x, C_y = P_x + scale * perp_vec[0], P_y + scale * perp_vec[1]
        if assert_coord_in_range(C_x, C_y):
            break

        if id > 30:
            return d
        id += 1

    id = 0
    while True:
        C_label = label_point(d)
        if C_label != A_label and C_label != B_label:
            break
        if id > 30:
            return d
        id += 1
    C = Point(C_x, C_y, C_label)
    A = Point(A_x, A_y, A_label)
    B = Point(B_x, B_y, B_label)
    d.points.extend([A, B, C])
    P = Point(P_x, P_y, '')
    length = random_length()
    dashed_line = Line(P, C, label=length, dotted=True)
    d.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, A, label=""),
                    dashed_line])
    # d.entities.append(f'Triangle({A.label}{B.label}{C.label}) with height {length} from {C.label} to Line({A.label}{B.label})')
    d.entities.append(('triangle_with_height', [A.label, B.label, C.label, P.label, f'{length}']))
    d.perpendiculars.append((Line(A, B, label=""), dashed_line, P))

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
    d.lines.append(Line(center, P, label=length, dotted=random.choice([True, False])))
    # d.entities.append(f'Circle with center {center.label} and radius {length}')
    d.entities.append(('circle_with_radius', [center.label, f'{length}']))
    return d

def incenter3(diagram: Diagram):
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
    assert assert_coord_in_range(X_x, X_y)
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


def circular_sector(d):

    while True:
        x, y = random_coord(), random_coord()
        radius = random.randint(150, 500)
        if assert_coord_in_range(x + radius, y + radius) and assert_coord_in_range(x - radius, y - radius):
            break

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



    d.points.extend([center, start_point, end_point])
    d.lines.extend([Line(center, start_point, label=""), Line(center, end_point, label="")])
    # d.entities.append(f'Circular sector with center {center.label}, radius {radius} and angle {label}')

    d.angles.append((Line(center, start_point, label=""), Line(center, end_point, label=""), center, label))
    return d

def semicircle(d):
    angle = np.pi

    while True:
        x, y = random_coord(), random_coord()
        radius = random.randint(150, 500)
        if assert_coord_in_range(x + radius, y + radius) and assert_coord_in_range(x - radius, y - radius):
            break

    center = Point(x, y, label_point(d))

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
    d.points.extend([center, start_point, end_point])
    d.lines.extend([Line(center, start_point, label="")])
    # d.entities.append(f'Semi-circle with center {center.label} with radius {radius}')

    return d

# def circle_perpendicular_bisector(d):
#     while True:
#         center = Point(random_coord(), random_coord(), label_point(d))
#         radius = int(random.uniform(150, 500))
#         if assert_coord_in_range(center.x + radius, center.y + radius) and assert_coord_in_range(center.x - radius, center.y - radius):
#             break
#
#     circle = Circle(center, radius, '')
#     angle = random_angle()
#     x, y = center.x + radius * np.cos(angle), center.y + radius * np.sin(angle)
#     P = Point(x, y, "")
#     length = random_length()
#     d.points.append(center)
#     d.circles.append(circle)
#     d.lines.append(Line(center, P, label=length, dotted=True))
#     d.entities.append(f'Circle with center {center.label} and radius {length}')
#     return d

def l_in_c(d):
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
    # d.entities.append(f'Line({p1.label}{p2.label}) inside Circle({center.label},{radius})')
    d.entities.append(('l_in_c', [center.label, f'{radius}', p1.label, p2.label]))
    return d

def l_out_c(d):
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

def o_in_o(d):
    return d

def o_out_o(d):
    return d

def o_on_o(d):
    return d
def o_left_o(d):
    return d

def o_right_o(d):
    return d

def ll_angle(d):
    ind = 0
    while True:
        interpt_x, interpt_y = random_coord(), random_coord()
        angle1 = random_angle()
        angle2 = random.uniform(angle1 + np.pi / 6, angle1 + np.pi /2)
        leng = [random.uniform(100,500) for _ in range(4)]
        x11, y11 = interpt_x + leng[0] * np.cos(angle1), interpt_y + leng[0] * np.sin(angle1)
        x12, y12 = interpt_x - leng[1] * np.cos(angle1), interpt_y - leng[1] * np.sin(angle1)
        x21, y21 = interpt_x + leng[2] * np.cos(angle2), interpt_y + leng[2] * np.sin(angle2)
        x22, y22 = interpt_x - leng[3] * np.cos(angle2), interpt_y - leng[3] * np.sin(angle2)
        if assert_coord_in_range(x11, y11) and assert_coord_in_range(x12, y12) and assert_coord_in_range(x21, y21) and assert_coord_in_range(x22, y22):
            break
        if ind > 30:
            return d
        ind += 1

    angle_label = random.choice(angle_letters.candidates)
    angle_number = f"{int(math.degrees(angle1-angle2))}°" if angle1-angle2 >  0 else f"{int(math.degrees(angle2-angle1))}°"

    label = random.choice([angle_label, angle_number])

    while True:
        label11 = label_point(d)
        label12 = label_point(d)
        label21 = label_point(d)
        label22 = label_point(d)
        if label11 != label12 and label11 != label21 and label11 != label22 and label12 != label21 and label12 != label22 and label21 != label22:
            break


    p11, p12, p21, p22, interpt = Point(x11, y11, label11), Point(x12, y12, label12), Point(x21, y21, label21), Point(x22, y22, label22), Point(interpt_x, interpt_y, "")
    d.points.extend([p11, p12, p21, p22 ])
    d.lines.extend([Line(p11,p12, label=""), Line(p21,p22, label="")])
    # d.entities.append(f'Line({p11.label}{p12.label}) and Line({p21.label}{p22.label}) intersect with angle {label}')
    d.entities.append(('ll_angle', [p11.label, p12.label, p21.label, p22.label, interpt.label, label]))
    d.angles.append((Line(p11,p12, label=""), Line(p21,p22, label=""), interpt, label))
    return d
#
# def parallel_0(d):
#     l = random.choice(d.lines)
#     A, B = l.point1, l.point2
#
#     vector = (B.x - A.x, B.y - A.y)
#
#     # tk = random.randint(0,5)
#
#     while True:
#         scale = random.uniform(-5, 5)
#         x,y = random_coord(), random_coord()
#         if assert_coord_in_range(x+vector[0]*scale, y+vector[1]*scale):
#             break
#
#     while True:
#
#         C = Point(x+vector[0]*scale, y+vector[1]*scale, label_point(d))
#         D = Point(x, y, label_point(d))
#         if C.label != D.label:
#             break
#
#     d.points.extend([C, D])
#     d.lines.append(Line(C, D, label=""))
#     d.lines.append(Line(A, B, label=""))
#     # d.entities.append(f'Line({C.label}{D.label}) parallel to Line({A.label}{B.label})')
#     d.entities.append(('parallel', [A.label, B.label, C.label, D.label]))
#     return d
#
# def parallel_1(d):
#     # l = random.choice(d.lines)
#     # A, B = l.point1, l.point2
#
#     A = Point(random_coord(), random_coord(), label_point(d))
#     B = Point(random_coord(), random_coord(), label_point(d))
#
#
#
#     #define numpy vector of difference of A, B
#     AB_diff = np.array([B.x - A.x, B.y - A.y])
#
#     # tk = random.randint(0,5)
#     num_not_prl = random.randint(1, 5)
#
#     new_points_0 = []
#     new_points_1 = []
#     new_lines = []
#     new_labels = []
#
#
#
#     #Generate a parallel line
#     while True:
#         scale = random.uniform(-5, 5)
#         x, y = random_coord(), random_coord()
#         vector = AB_diff
#         x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
#         if assert_coord_in_range(x_end, y_end):
#             break
#
#     while True:
#         label0 = label_point(d)
#         if label0 not in new_labels:
#             new_labels.append(label0)
#             break
#
#     while True:
#         label1 = label_point(d)
#         if label1 not in new_labels:
#             new_labels.append(label1)
#             break
#
#     C = Point(x, y, label0)
#     D = Point(x_end, y_end, label1)
#
#
#     new_lines.append(Line(C, D, label=""))
#
#
#
#     #Generate non-parallel lines
#     for j in range(num_not_prl):
#         while True:
#             angle = random_angle()
#             scale = random.uniform(-5, 5)
#             x,y = random_coord(), random_coord()
#             vector = rotate_vector(AB_diff, angle)
#             x_end, y_end = x + vector[0]*scale, y + vector[1]*scale
#             if assert_coord_in_range(x_end, y_end):
#                 break
#
#         while True:
#             label0 = label_point(d)
#             if label0 not in new_labels:
#                 new_labels.append(label0)
#                 break
#
#         while True:
#             label1 = label_point(d)
#             if label1 not in new_labels:
#                 new_labels.append(label1)
#                 break
#
#         new_points_0.append(Point(x, y, label0))
#         new_points_1.append(Point(x_end, y_end, label1))
#         new_lines.append(Line(new_points_0[-1], new_points_1[-1], label=""))
#
#
#     d.points.extend([A, B])
#     d.lines.append(Line(A, B, label=""))
#     d.points.extend([C, D])
#
#     d.points.extend(new_points_0)
#     d.points.extend(new_points_1)
#     d.lines.extend(new_lines)
#
#     d.entities.append(('parallel_1', [A.label, B.label, C.label, D.label] + [p.label for p in new_points_0] + [p.label for p in new_points_1], len(new_points_0)))
#
#     return d
#
#
# def parallel_2(d):
#
#     A = Point(random_coord(), random_coord(), label_point(d))
#     B = Point(random_coord(), random_coord(), label_point(d))
#     # define numpy vector of difference of A, B
#     AB_diff = np.array([B.x - A.x, B.y - A.y])
#
#
#     num_prl = random.randint(1, 5)
#     num_not_prl = random.randint(1, 5)
#
#     prl_points_0 = []
#     prl_points_1 = []
#     non_prl_points_0 = []
#     non_prl_points_1 = []
#     new_lines = []
#     new_labels = []
#
#     #Generate parallel lines
#     for i in range(num_prl):
#         while True:
#             scale = random.uniform(-5, 5)
#             x, y = random_coord(), random_coord()
#             vector = AB_diff
#             x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
#             if assert_coord_in_range(x_end, y_end):
#                 break
#
#         while True:
#             label_0 = label_point(d)
#             if label_0 not in new_labels:
#                 new_labels.append(label_0)
#                 break
#
#         while True:
#             label_1 = label_point(d)
#             if label_1 not in new_labels:
#                 new_labels.append(label_1)
#                 break
#
#         prl_points_0.append(Point(x, y, label_0))
#         prl_points_1.append(Point(x_end, y_end, label_1))
#         new_lines.append(Line(prl_points_0[-1], prl_points_1[-1], label=""))
#
#
#     #Generate non-parallel lines
#     for j in range(num_not_prl):
#         while True:
#             scale = random.uniform(-5, 5)
#             angle = random_angle()
#             x, y = random_coord(), random_coord()
#             vector = rotate_vector(AB_diff, angle)
#             x_end, y_end = x + vector[0] * scale, y + vector[1] * scale
#             if assert_coord_in_range(x_end, y_end):
#                 break
#
#         while True:
#             label_0 = label_point(d)
#             if label_0 not in new_labels:
#                 new_labels.append(label_0)
#                 break
#
#         while True:
#             label_1 = label_point(d)
#             if label_1 not in new_labels:
#                 new_labels.append(label_1)
#                 break
#
#         non_prl_points_0.append(Point(x, y, label_0))
#         non_prl_points_1.append(Point(x_end, y_end, label_1))
#         new_lines.append(Line(non_prl_points_0[-1], non_prl_points_1[-1], label=""))
#
#     d.points.extend([A, B])
#     d.lines.append(Line(A, B, label=""))
#     d.points.extend(prl_points_0)
#     d.points.extend(prl_points_1)
#     d.points.extend(non_prl_points_0)
#     d.points.extend(non_prl_points_1)
#     d.lines.extend(new_lines)
#
#     d.entities.append(('parallel_2', A.label, B.label, num_prl, num_not_prl))
#     print(f"Parallel_2 : {A.label}{B.label}, {num_prl}, {num_not_prl}")
#     return d
#
#
#
#
# def parallel_3(diagram):
#     #"X = parallelogram(A, B, C)": { "Description": "Construct X such that ABCX is a parallelogram" },
#     while len(diagram.points)< 3:
#         diagram = add_free_point(diagram)
#
#     A, B, C = random.sample(diagram.points, 3)
#     vector = (B.x - A.x, B.y - A.y)
#     D_x = C.x - vector[0]
#     D_y = C.y - vector[1]
#     assert assert_coord_in_range(D_x, D_y)
#
#     D_label = label_point(diagram)
#
#     D = Point(D_x, D_y, D_label)
#     diagram.points.append(D)
#     diagram.lines.extend([Line(A, B, label=""), Line(B, C, label=""), Line(C, D, label=""), Line(D, A, label="")])
#     # diagram.entities.append(f'Parallelogram({A.label}{B.label}{C.label}{D.label})')
#     diagram.entities.append(('parallel_3', [A.label, B.label, C.label, D.label]))
#     return diagram
#
# def parallel_4(diagram: Diagram):
#
#     while len(diagram.points) < 2:
#         diagram = add_free_point(diagram)
#     # Randomly select two points A, B to form the base AB of the trapezoid
#     A, B = random.sample(diagram.points, 2)
#
#     # Calculate the directional vector for AB and its perpendicular
#     AB_vector = (B.x - A.x, B.y - A.y)
#     perp_AB = (-AB_vector[1], AB_vector[0])  # Rotate AB_vector by 90 degrees to get perpendicular
#
#     # Normalize the perpendicular vector
#     perp_AB_normalized = normalize(perp_AB)
#
#     # Select a random angle θ < π/2 for rotation
#     theta = random.uniform(0, np.pi / 6)
#
#     # Calculate the direction for AD by rotating the perpendicular direction by θ
#     AD_direction = (perp_AB_normalized[0] * np.cos(theta) - perp_AB_normalized[1] * np.sin(theta),
#                     perp_AB_normalized[0] * np.sin(theta) + perp_AB_normalized[1] * np.cos(theta))
#
#     # Calculate the direction for BC by rotating the perpendicular direction by -θ
#     BC_direction = (perp_AB_normalized[0] * np.cos(-theta) - perp_AB_normalized[1] * np.sin(-theta),
#                     perp_AB_normalized[0] * np.sin(-theta) + perp_AB_normalized[1] * np.cos(-theta))
#
#     # Decide on a length for AD and BC
#     leg_length = random.uniform(50, 400)  # Example range for the leg length
#
#     # Calculate points D and C using the determined directions and length
#     Dx, Dy = A.x + AD_direction[0] * leg_length, A.y + AD_direction[1] * leg_length
#     Cx, Cy = B.x + BC_direction[0] * leg_length, B.y + BC_direction[1] * leg_length
#
#     # Check if D and C are within the diagram range
#     assert assert_coord_in_range(Dx, Dy) and assert_coord_in_range(Cx, Cy)
#
#     # Create points C and D
#     C_label, D_label = random.sample(capitals.candidates, 2)
#     C = Point(Cx, Cy, C_label)
#     D = Point(Dx, Dy, D_label)
#     diagram.points.extend([C, D])
#
#     # Add lines to form the trapezoid
#     diagram.lines.extend([
#         Line(A, B, label=""),  # Base AB
#         Line(B, C, label=""),  # Side BC
#         Line(C, D, label=""),  # Top CD, parallel to AB
#         Line(D, A, label="")   # Side AD
#     ])
#
#     # diagram.entities.extend([
#     #     f'Point({C.label})', f'Point({D.label})',
#     #     f'Line({A.label}{B.label})', f'Line({B.label}{C.label})',
#     #     f'Line({C.label}{D.label})', f'Line({D.label}{A.label})',
#     #     f'Equilateral Trapezoid({A.label}{B.label}{C.label}{D.label})'
#     # ])
#     diagram.entities.append(('parallel_4', [A.label, B.label, C.label, D.label]))
#     # print(f"=====A,B,C,D : {A.label}{B.label}{C.label}{D.label}")
#     return diagram







