import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
import math

point_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_labels = list("1234567890")
func_labels = list("abcdefghijklmnopqrstuvwxyz")
color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

class RandomCurve:
    def __init__(self, start, end, line_color = 'black'):
        self.func = None
        self.start = start
        self.end = end
        self.x = None
        self.y = None
        self.line_color = line_color
        self.get_interval()

    def create_polynomial_from_zeros(self, zeros):
        coefficients = [random.uniform(-5, 5)]
        for zero in zeros:
            coefficients = np.convolve(coefficients, [1, -zero]) 
        return coefficients

    def poly_function(self):
        num_zeros = random.randint(2, 6)
        zeros = [random.randint(self.start+1, self.end-1) for _ in range(num_zeros)]
        coefficients = self.create_polynomial_from_zeros(zeros)
        def f(x):
            return sum(coefficients[i] * x**(len(coefficients) - 1 - i) for i in range(len(coefficients)))
        self.func = f

    def second_derivative(self):
        return np.gradient(np.gradient(self.y, self.x), self.x)
        
    def plot(self, ax):
        ax.plot(self.x, self.y, color=self.line_color, linewidth=2)

    def get_interval(self):
        self.x = np.linspace(self.start, self.end, 800)
        self.poly_function()
        self.y = self.func(self.x)
        max_y = max(self.y)
        min_y = min(self.y)
        self.y = (self.end - self.start)/(max_y-min_y)*(self.y-min_y)+self.start

class RandomLineSegment:
    def __init__(self, start, end, line_color = 'black'):
        self.start = start
        self.end = end
        self.x = None
        self.y = None
        self.line_color = line_color

        if random.randint(1, 2) == 1:
            self.x = [start, end]
            self.y = sorted([random.uniform(start, end), random.uniform(start, end)])
        else:
            self.y = [start, end]
            self.x = sorted([random.uniform(start, end), random.uniform(start, end)])
    
    def plot(self, ax):
        ax.plot(self.x, self.y, color=self.line_color, linewidth=2)

class Circle:
    def __init__(self, xy, radius, edgecolor, label=None):
        self.xy = xy
        self.radius = radius
        self.edgecolor = edgecolor
        self.facecolor = "none"
        self.label = label
        self.patch = patches.Circle(self.xy, self.radius, edgecolor=self.edgecolor, 
                                    facecolor=self.facecolor, label=self.label)
        self.shape_type = "circle"
    
    def plot(self, ax):
        ax.add_patch(self.patch)

class Diagram:
    def __init__(self,components = None,entities=None,background_color='white',labels=None,colors=None):
        self.components = components if components is not None else []
        self.entities = entities if entities is not None else []
        self.background_color = background_color
        self.labels = labels if labels is not None else []
        self.colors = colors if colors is not None else []

def curvature1(diagram, ax, tc):
    num_straight_lines = random.randint(1, 5)
    num_curves = random.randint(1, 5)
    line_color_list = random.sample(color_list, num_straight_lines + num_curves)
    answer = line_color_list[0:num_straight_lines]

    for idx in range(num_straight_lines):
        func = RandomLineSegment(-10, 10, line_color = line_color_list[idx])
        diagram.components.append(("line", func))
        func.plot(ax)

    for idx in range(num_straight_lines, num_straight_lines+num_curves):
        func = RandomCurve(-10, 10, line_color = line_color_list[idx])
        diagram.components.append(("curve", func))
        func.plot(ax)
    
    random.shuffle(line_color_list)
    diagram.entities.append(("curvature1", ["/".join(line_color_list), ", ".join(line_color_list), ", ".join(answer)]))
    return diagram

def curvature2(diagram, ax, tc):
    num_straight_lines = random.randint(1, 5)
    num_curves = random.randint(1, 5)
    line_color_list = random.sample(color_list, num_straight_lines + num_curves)
    answer = line_color_list[0:num_curves]

    for idx in range(num_curves):
        func = RandomCurve(-10, 10, line_color = line_color_list[idx])
        diagram.components.append(("curve", func))
        func.plot(ax)

    for idx in range(num_curves, num_straight_lines+num_curves):
        func = RandomLineSegment(-10, 10, line_color = line_color_list[idx])
        diagram.components.append(("line", func))
        func.plot(ax)
    
    random.shuffle(line_color_list)
    diagram.entities.append(("curvature2", ["/".join(line_color_list), ", ".join(line_color_list), ", ".join(answer)]))
    return diagram

def curvature3(diagram, ax, tc):
    num_arcs = random.randint(1, 5)
    num_others = random.randint(1, 5)

    line_color_list = random.sample(color_list, num_arcs + num_others)
    
    answer_arcs = line_color_list[:num_arcs]

    for idx in range(num_arcs):
        center_x = random.randint(-8, 8)
        center_y = random.randint(-8, 8)
        radius = random.uniform(2, 8)
        theta1 = random.uniform(0, 180)
        theta2 = theta1 + random.uniform(60, 180)
        
        arc_patch = patches.Arc(
            xy=(center_x, center_y),
            width=2*radius,  
            height=2*radius,
            angle=0,        
            theta1=theta1,  
            theta2=theta2,   
            edgecolor=line_color_list[idx],
            linewidth=2
        )
        ax.add_patch(arc_patch)
        diagram.components.append(("arc", arc_patch))
    
    for idx in range(num_arcs, num_arcs + num_others):
        if random.random() < 0.5:
            func = RandomLineSegment(-10, 10, line_color=line_color_list[idx])
            func.plot(ax)
            diagram.components.append(("line", func))
        else:
            func = RandomCurve(-10, 10, line_color=line_color_list[idx])
            func.plot(ax)
            diagram.components.append(("curve", func))
    
    random.shuffle(line_color_list)

    diagram.entities.append(("curvature3", ["/".join(line_color_list), ", ".join(line_color_list), ", ".join(answer_arcs)]))
    return diagram

def curvature4(diagram, ax, tc):
    num_circles = random.choice([2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9, 10])
    random_color_list = random.sample(color_list, num_circles)
    radius_list = sorted(random.sample([i for i in range(1, 21)], num_circles))
    answer = random_color_list[0]

    for idx in range(num_circles):
        c = Circle((random.randint(-10, 10), random.randint(-10, 10)), radius_list[idx], random_color_list[idx])
        c.plot(ax)
        diagram.components.append(c)

    random.shuffle(random_color_list)

    diagram.entities.append(("curvature4", ["/".join(random_color_list), ", ".join(random_color_list), answer]))
    return diagram

def curvature5(diagram, ax, tc):
    num_circles = random.choice([2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9, 10])
    random_color_list = random.sample(color_list, num_circles)
    radius_list = sorted(random.sample([i for i in range(1, 21)], num_circles))
    answer = random_color_list[-1]

    for idx in range(num_circles):
        c = Circle((random.randint(-10, 10), random.randint(-10, 10)), radius_list[idx], random_color_list[idx])
        c.plot(ax)
        diagram.components.append(c)

    random.shuffle(random_color_list)

    diagram.entities.append(("curvature5", ["/".join(random_color_list), ", ".join(random_color_list), answer]))
    return diagram

def curvature6(diagram, ax, tc):
    curve = RandomCurve(-10, 10, line_color="black")
    curve.plot(ax)

    num_points = random.randint(3, 7)
    indices = sorted(random.sample(range(len(curve.x)), num_points)) 

    dy = np.gradient(curve.y, curve.x)
    ddy = np.gradient(dy, curve.x)
    curvature_values = np.abs(ddy) / (1 + dy**2)**1.5

    chosen_labels = random.sample(point_labels, num_points)
    point_coords = []
    for i, idx in enumerate(indices):
        px, py = curve.x[idx], curve.y[idx]
        ax.plot(px, py, 'o', color='red')
        tc.append(px+0.2, py+0.2, chosen_labels[i])
        point_coords.append((px, py))

    chosen_curvatures = [curvature_values[idx] for idx in indices]
    max_curv_idx = np.argmax(chosen_curvatures)
    answer_label = chosen_labels[max_curv_idx]

    diagram.components.append(
        {
            chosen_labels[i]: chosen_curvatures[i] 
            for i in range(num_points)
        }
    )
    diagram.entities.append(("curvature6", ["/".join(chosen_labels), ", ".join(chosen_labels), answer_label]))
    return diagram


def curvature7(diagram, ax, tc):
    curve = RandomCurve(-10, 10, line_color="black")
    curve.plot(ax)

    num_points = random.randint(3, 7)
    indices = sorted(random.sample(range(0, len(curve.x), 5), num_points)) 

    dy = np.gradient(curve.y, curve.x)
    ddy = np.gradient(dy, curve.x)
    curvature_values = np.abs(ddy) / (1 + dy**2)**1.5

    chosen_labels = random.sample(point_labels, num_points)
    point_coords = []
    for i, idx in enumerate(indices):
        px, py = curve.x[idx], curve.y[idx]
        ax.plot(px, py, 'o', color='red')
        tc.append(px+0.2, py+0.2, chosen_labels[i])
        point_coords.append((px, py))

    chosen_curvatures = [curvature_values[idx] for idx in indices]
    max_curv_idx = np.argmin(chosen_curvatures)
    answer_label = chosen_labels[max_curv_idx]

    diagram.components.append({chosen_labels[idx]:chosen_curvatures[idx] for idx in range(num_points)})

    diagram.entities.append(("curvature7", ["/".join(chosen_labels), ", ".join(chosen_labels), answer_label]))
    return diagram


rules = [
    curvature1,
    curvature2,
    curvature3,
    curvature4,
    curvature5,
    curvature6,
    curvature7
]