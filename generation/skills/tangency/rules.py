import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
import math
from matplotlib.path import Path
import shapely
from shapely.geometry import Polygon as ShapelyPolygon, MultiPolygon
import copy
import matplotlib.ticker as ticker
from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.setitimer(signal.ITIMER_REAL,seconds) #used timer instead of alarm
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator

point_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_labels = list("1234567890")
func_labels = list("abcdefghijklmnopqrstuvwxyz")
color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

class Diagram:
    def __init__(self,components = None,entities=None,background_color='white',labels=None,colors=None):
        self.components = components if components is not None else []
        self.entities = entities if entities is not None else []
        self.background_color = background_color
        self.labels = labels if labels is not None else []
        self.colors = colors if colors is not None else []

class RandomCurve:
    def __init__(self, start, end, line_color='black'):
        self.func = None
        self.start = start
        self.end = end
        self.x = None
        self.y = None
        self.line_color = line_color
        self.get_interval()
        self.type_str = "curve"
        self._coeffs = None  
        self._create_polynomial()
        self._sample_curve()

    def _create_polynomial(self):
        degree = random.randint(2, 10)
        self._coeffs = [random.uniform(-5, 5) for _ in range(degree+1)]

    def _f(self, x):
        return sum( coeff * (x**(len(self._coeffs)-1 - i)) 
                    for i, coeff in enumerate(self._coeffs) )

    def _sample_curve(self):
        self.x = np.linspace(self.start, self.end, 800)
        raw_y = np.array([self._f(val) for val in self.x])

        min_y, max_y = raw_y.min(), raw_y.max()
        if abs(max_y - min_y) < 1e-10:
            raw_y += 1.0
            min_y, max_y = raw_y.min(), raw_y.max()

        scale = (self.end - self.start) / (max_y - min_y)
        self.y = scale * (raw_y - min_y) + self.start

    def derivative(self, x):
        n = len(self._coeffs) - 1  
        derivative_coeffs = []
        for i, c in enumerate(self._coeffs):
            power = n - i  
            if power > 0:
                derivative_coeffs.append(power * c * (x ** (power - 1)))
        return sum(derivative_coeffs)

    def create_polynomial_from_zeros(self, zeros):
        coefficients = [random.uniform(-5, 5)]
        for zero in zeros:
            coefficients = np.convolve(coefficients, [1, -zero]) 
        return coefficients

    def poly_function(self):
        num_zeros = random.randint(2, 9)
        zeros = [random.uniform(self.start+0.5, self.end-0.5) for _ in range(num_zeros)]
        self.coefficients = self.create_polynomial_from_zeros(zeros)
        
        def f(x):
            return sum(self.coefficients[i] * x**(len(self.coefficients) - 1 - i) for i in range(len(self.coefficients)))
        self.func = f

    def get_interval(self):
        self.x = np.linspace(self.start, self.end, 800)
        self.poly_function()
        self.y = self.func(self.x)
        
        max_y = max(self.y)
        min_y = min(self.y)
        if max_y == min_y:
            max_y += 1
            min_y -= 1
        self.y = (self.end - self.start) / (max_y - min_y) * (self.y - min_y) + self.start

    def plot(self, ax, tc, set_visible = True):
        line, = ax.plot(self.x, self.y, color=self.line_color, linewidth=2)
        line.set_visible(set_visible)
    
    def translation(self, diff, line_color):
        self.y = [i-diff for i in self.y]
        def f2(x):
            return self.func(x)-2
        self.func = f2
        self.line_color = line_color

class RandomLineSegment:
    def __init__(self, start, end, line_color='black'):
        self.start = start
        self.end = end
        self.line_color = line_color
        
        x1, x2 = sorted([start, end])
        y_const = random.uniform(start, end)
        self.x = [x1, x2]
        self.y = [y_const, y_const]
        
        self.slope = 0
        self.intercept = y_const

        self.type_str = "line segment"

    def func(self, x):
        return self.slope * x + self.intercept
    
    def plot(self, ax, tc, set_visible = True):
        line, = ax.plot(self.x, self.y, color=self.line_color, linewidth=2)
        line.set_visible(set_visible)
        
    def translation(self, diff, line_color):
        self.y = [i-diff for i in self.y]
        self.intercept = self.y[0] - self.slope * self.x[0]
        self.line_color = line_color

class SlopeLineSegment:
    def __init__(self, x1, y1, x2, y2, line_color='black'):
        self.x = np.array([x1, x2])
        self.y = [y1, y2]
        dx = x2 - x1
        dy = y2 - y1
        if abs(dx) < 1e-10: 
            self.slope = None
            self.intercept = None
        else:
            self.slope = dy / dx
            self.intercept = y1 - self.slope * x1

        self.line_color = line_color
        self.type_str = "line segment"
    
    def func(self, x):
        return self.slope * x + self.intercept

    def plot(self, ax, tc, set_visible = True):
        line, = ax.plot(self.x, self.y, color=self.line_color, linewidth=2)
        line.set_visible(set_visible)

class Point:
    def __init__(self, x, y, label = "", color = "black"):
        self.x = x
        self.y = y
        self.label = label
        self.color = color
    
    def plot(self, ax, tc, set_visible = True):
        scatter = ax.scatter(self.x, self.y, color = self.color)
        scatter.set_visible(set_visible)
        tc.append(self.x, self.y, self.label)

class Line:
    def __init__(self, slope, intercept, color="black"):
        self.slope = slope
        self.intercept = intercept
        self.color = color
    
    def plot(self, ax, tc, xlim=(-7, 7), set_visible = True):
        x_vals = np.linspace(xlim[0], xlim[1], 200)
        y_vals = self.slope * x_vals + self.intercept
        line = ax.plot(x_vals, y_vals, color=self.color, linewidth=2)
        line[0].set_visible(set_visible)

class Circle:
    def __init__(self, xy, radius, edgecolor, facecolor, label=None, alpha=1):
        self.xy = xy
        self.radius = radius
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha
        self.patch = patches.Circle(self.xy, self.radius, edgecolor=self.edgecolor, 
                                    facecolor=self.facecolor, alpha=self.alpha, label=self.label)
        self.shape_type = "circle"
    
    def update_patch(self):
        self.patch = patches.Circle(self.xy, self.radius, edgecolor=self.edgecolor, 
                                    facecolor=self.facecolor, alpha=self.alpha, label=self.label)
    
    def plot(self, ax, tc, set_visible = True):
        self.update_patch()
        patch = ax.add_patch(self.patch)
        patch.set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        cx, cy = self.xy
        r = self.radius
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        box_w = 2*r
        box_h = 2*r
        
        scale_factor = 1.0
        if box_w > region_w or box_h > region_h:
            scale_factor = min(region_w / box_w, region_h / box_h)
        
        new_r = r * scale_factor
        
        shift_x = 0
        shift_y = 0
        
        x_min = cx - new_r
        x_max = cx + new_r
        if x_min < xlim[0]:
            shift_x = xlim[0] - x_min
        elif x_max > xlim[1]:
            shift_x = xlim[1] - x_max
        
        y_min = cy - new_r
        y_max = cy + new_r
        if y_min < ylim[0]:
            shift_y = ylim[0] - y_min
        elif y_max > ylim[1]:
            shift_y = ylim[1] - y_max
        
        regulated_cx = cx + shift_x
        regulated_cy = cy + shift_y
        
        self.xy = (regulated_cx, regulated_cy)
        self.radius = new_r
        
        self.patch = patches.Circle(self.xy, self.radius,
                                    edgecolor=self.edgecolor,
                                    facecolor=self.facecolor,
                                    alpha=self.alpha,
                                    label=self.label)

class Polynomial:
    def __init__(self, start, end, zeros, line_color = None):
        if line_color == None:
            if random.randint(1, 2) == 1:
                line_color = "black"
            else:
                line_color = random.choice(color_list)
        self.func = None
        self.start = start
        self.end = end
        self.x = None
        self.y = None
        self.line_color = line_color
        self.zeros = zeros
        self.num_zeros = len(self.zeros)
        self.get_interval()

    def create_polynomial_from_zeros(self):
        coefficients = [random.uniform(-5, 5)]
        for zero in self.zeros:
            coefficients = np.convolve(coefficients, [1, -zero]) 
        return coefficients

    def poly_function(self):
        coefficients = self.create_polynomial_from_zeros()
        def f(x):
            return sum(coefficients[i] * x**(len(coefficients) - 1 - i) for i in range(len(coefficients)))
        self.func = f

    def second_derivative(self):
        return np.gradient(np.gradient(self.y, self.x), self.x)
        
    def plot(self, ax, tc, set_visible = True):
        line = ax.plot(self.x, self.y, color=self.line_color, linewidth=2)
        line[0].set_visible(set_visible)

        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_visible(set_visible)
        ax.spines['bottom'].set_visible(set_visible)
        ax.spines['right'].set_visible(set_visible)
        ax.spines['top'].set_visible(set_visible)
        def skip_zero_label(val, pos):
            if val == 0:
                return ''
            return str(int(val)) 
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(skip_zero_label))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(skip_zero_label))
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_visible(set_visible)
        ax.yaxis.set_visible(set_visible)
        tc.append(0, 0, '0', ha='right', va='top')
        ax.grid(visible=(random.randint(1, 2) == 1) and set_visible)

    def get_interval(self):
        self.x = np.linspace(self.start, self.end, 800)
        self.poly_function()
        self.y = self.func(self.x)
        max_y = max(abs(min(self.y)), abs(max(self.y)))
        max_criteria = max(abs(self.start), abs(self.end))
        def f(x):
            return self.func(x)*max_criteria/max_y
        self.regulated_func = f
        self.y = np.array([val*max_criteria/max_y for val in self.y])


def generate_random_circle(edgecolor = None, facecolor = None, color = None, xlim=(0, 100), ylim=(0, 100), alpha = 1):    
    if (color != None):
        edgecolor = color
        facecolor = color
    
    else:
        if (edgecolor == None):
            edgecolor = random.choice(edgecolor_list)
        if (facecolor == None):
            facecolor = random.choice(facecolor_list)

    cx, cy = random.uniform(*xlim), random.uniform(*ylim)
    radius = random.uniform(5, 50)
    return Circle((cx, cy), radius, edgecolor, facecolor, alpha = alpha)

def get_random_tangent_line_segment(curve, line_color='red', segment_width=2.0):
    idx = random.randint(0, len(curve.x) - 1)
    
    x0 = curve.x[idx]
    y0 = curve.y[idx]
    
    dy = np.gradient(curve.y, curve.x)
    slope = dy[idx]

    half_w = segment_width * 0.5
    x1 = x0 - half_w
    x2 = x0 + half_w

    y1 = slope*(x1 - x0) + y0
    y2 = slope*(x2 - x0) + y0

    tangent_segment = SlopeLineSegment(x1, y1, x2, y2, line_color=line_color)

    return tangent_segment, x0, y0

def generate_two_tangent_curves(start=-5, end=5, c=None):
    color1, color2 = random.sample(color_list, 2)

    curve1 = RandomCurve(start, end, line_color=color1)
    
    x0 = random.uniform(start, end)
    y0 = None

    def f1(x):
        return np.interp(x, curve1.x, curve1.y)

    y0 = f1(x0)
    
    if c is None:
        c = random.uniform(-1.0, 1.0)
        while abs(c) < 1e-5:
            c = random.uniform(-1.0, 1.0)
    
    x2 = curve1.x.copy() 
    y2 = []
    for xx in x2:
        y2.append( f1(xx) + c*((xx - x0)**2) )
    y2 = np.array(y2)

    curve2 = RandomCurve(start, end, line_color=color2)
    curve2.x = x2
    curve2.y = y2
    
    return curve1, curve2, x0

def generate_random_tangent_circle_and_line(xlim=(0, 100), ylim=(0, 100)):
    edgecolor, line_color = random.sample(color_list, 2)
    if random.randint(1, 2) == 1:
        facecolor = edgecolor
    else:
        facecolor = "none"

    cx = random.uniform(xlim[0]+10, xlim[1]-10)
    cy = random.uniform(ylim[0]+10, ylim[1]-10)
    r = random.uniform(5, 15)  # 반지름 5~15 사이
    
    if facecolor != "none":
        circle_obj = Circle(
            xy=(cx, cy),
            radius=r,
            edgecolor=edgecolor,
            facecolor=facecolor,
            alpha=random.random()
        )
    else:
        circle_obj = Circle(
            xy=(cx, cy),
            radius=r,
            edgecolor=edgecolor,
            facecolor=facecolor,
        )

    circle_obj.regulate(xlim, ylim)
    
    m = random.uniform(-2, 2) 
    
    sign = random.choice([-1, 1])
    dist_factor = circle_obj.radius * math.sqrt(m**2 + 1)
    
    b = (circle_obj.xy[1] - m*circle_obj.xy[0]) + sign*dist_factor
    
    line_obj = Line(slope=m, intercept=b, color=line_color)
    
    return circle_obj, line_obj

def generate_non_tangent_circle_and_line(xlim=(-5, 5), ylim=(-5, 5)):
    edgecolor, line_color = random.sample(color_list, 2)
    facecolor = edgecolor if random.randint(1, 2) == 1 else "none"

    while True:
        cx = random.uniform(xlim[0] + 1, xlim[1] - 1)
        cy = random.uniform(ylim[0] + 1, ylim[1] - 1)
        r = random.uniform(0.5, 3)
        if (cx+r<xlim[1]) & (cy+r<xlim[1]) & (cx-r<xlim[0]) & (cy-r<xlim[0]):
            break

    if facecolor != "none":
        circle_obj = Circle(
            xy=(cx, cy),
            radius=r,
            edgecolor=edgecolor,
            facecolor=facecolor,
            alpha=random.random()
        )
    else:
        circle_obj = Circle(
            xy=(cx, cy),
            radius=r,
            edgecolor=edgecolor,
            facecolor=facecolor,
        )
    circle_obj.regulate(xlim, ylim)

    while True:
        m = random.uniform(-2, 2) 
        b = random.uniform(ylim[0], ylim[1])

        distance = abs(m * cx - cy + b) / math.sqrt(m**2 + 1)

        if abs(distance - r) > 1e-2:
            break

    line_obj = Line(slope=m, intercept=b, color=line_color)

    return circle_obj, line_obj


def guaranteed_nontangent_curves(start=-5, end=5):
    color1, color2 = random.sample(color_list, 2)
    while True:
        curve1 = RandomCurve(start, end, line_color = color1)
        curve2 = RandomCurve(start, end, line_color = color2)
        
        f1_vals = curve1.y
        f2_vals = curve2.y
        diff_vals = f1_vals - f2_vals

        sign_changes = []
        for i in range(len(diff_vals) - 1):
            if diff_vals[i] * diff_vals[i+1] < 0:
                sign_changes.append(i)
        
        is_tangent = False
        for idx in sign_changes:
            xL = curve1.x[idx]
            xR = curve1.x[idx+1]
            mid_x = 0.5*(xL + xR)
            dy1 = curve1.derivative(mid_x)
            dy2 = curve2.derivative(mid_x)
            if abs(dy1 - dy2) < 1e-2:
                is_tangent = True
                break
        
        if not is_tangent:
            return curve1, curve2

## idea : 곡선과 직선이 접하는가? (접하는 상황, perturbation은 선의 색, 직선의 각도)
@timeout(10)
def tangency1(diagram):
    components = []
    entity = ("tangency1", [])

    two_colors = random.sample(color_list, 2)

    curve = RandomCurve(start=-5, end=5, line_color=two_colors[0])
    components.append(curve)

    tangent_line, x0, y0 = get_random_tangent_line_segment(curve, line_color=two_colors[1], segment_width=3.0)
    components.append(tangent_line)

    num_points = random.randint(2, 10)
    label_list = random.sample(point_labels, num_points)

    if random.randint(1, 2) == 1:
        contact_point = Point(x0, y0, label=label_list[0], color=random.choice(color_list))
        components.append(contact_point)
    
    if random.randint(1, 2) == 1:
        for i in range(1, num_points):
            random_point = Point(random.uniform(-5, 5), random.uniform(-5, 5), label=label_list[i], color=random.choice(color_list))
            components.append(random_point)

    diagram.components.extend(components)
    diagram.entities.append(entity)
    
    return diagram

## idea : 곡선과 직선이 접하는가? (접하지 않는 상황, perturbation은 선의 색)
@timeout(10)
def tangency2(diagram):
    components = []
    entity = ("tangency2", [])

    two_colors = random.sample(color_list, 2)

    curve = RandomCurve(start=-5, end=5, line_color=two_colors[0])
    components.append(curve)

    tangent_line, x0, y0 = get_random_tangent_line_segment(curve, line_color=two_colors[1], segment_width=3.0)

    if random.randint(1, 2) == 1:
        scale = 1
        while (0.8<scale<1.2):
            scale = random.uniform(0, 3)
        sign = random.choice([-1, 1])
        past_slope = tangent_line.slope
        tangent_line.slope = tangent_line.slope * scale * sign
        tangent_line.intercept = y0 - tangent_line.slope * x0 + random.uniform(-1, 1)

    else:
        scale = 1
        while (-0.7<scale<0.3):
            scale = random.uniform(-5, 5)
        tangent_line.intercept = tangent_line.intercept+scale
    tangent_line.y = tangent_line.func(tangent_line.x)


    components.append(tangent_line)

    if random.randint(1, 2) == 1:
        num_points = random.randint(1, 10)
        label_list = random.sample(point_labels, num_points)
        for i in range(num_points):
            random_point = Point(random.uniform(-5, 5), random.uniform(-5, 5), label=label_list[i], color=random.choice(color_list))
            components.append(random_point)

    diagram.components.extend(components)
    diagram.entities.append(entity)
    return diagram

## idea : 곡선과 곡선이 접하는가? (접하는 상황, perturbation은 선의 색 2가지)
@timeout(10)
def tangency3(diagram):
    components = []
    entity = ("tangency3", [])

    curve1, curve2, x0 = generate_two_tangent_curves(start=-5, end=5)
    components.append(curve1)
    components.append(curve2)
    
    num_points = random.randint(2, 10)
    label_list = random.sample(point_labels, num_points)

    if random.randint(1, 2) == 1:
        y0 = np.interp(x0, curve1.x, curve1.y)
        contact_point = Point(x0, y0, label=label_list[0], color=random.choice(color_list))
        components.append(contact_point)
    
    if random.randint(1, 2) == 1:
        for i in range(1, num_points):
            random_point = Point(random.uniform(-5, 5), random.uniform(-5, 5), label=label_list[i], color=random.choice(color_list))
            components.append(random_point)

    diagram.components.extend(components)
    diagram.entities.append(entity)
    return diagram

## idea : 곡선과 곡선이 접하는가? (접하지 않는 상황, perturbation은 선의 색)
@timeout(10)
def tangency4(diagram):
    components = []
    entity = ("tangency4", [])

    curve1, curve2 = guaranteed_nontangent_curves()
    components.append(curve1)
    components.append(curve2)

    if random.randint(1, 2) == 1:
        num_points = random.randint(1, 10)
        label_list = random.sample(point_labels, num_points)
        for i in range(num_points):
            random_point = Point(random.uniform(-5, 5), random.uniform(-5, 5), label=label_list[i], color=random.choice(color_list))
            components.append(random_point)

    diagram.components.extend(components)
    diagram.entities.append(entity)
    return diagram


## idea : 도형과 직선이 접하는가? (접하는 상황, perturbation은 선의 색)
@timeout(10)
def tangency5(diagram):
    components = []
    entity = ("tangency5", ['shape'])

    circle_obj, line_obj = generate_random_tangent_circle_and_line((-5, 5), (-5, 5))
    components.append(circle_obj)
    components.append(line_obj)

    diagram.components.extend(components)
    diagram.entities.append(entity)
    return diagram

## idea : 도형과 직선이 접하는가? (접하지 않는 상황, perturbation은 선의 색)
@timeout(10)
def tangency6(diagram):
    components = []
    entity = ("tangency6", [])

    circle_obj, line_obj = generate_non_tangent_circle_and_line()
    components.append(circle_obj)
    components.append(line_obj)

    diagram.components.extend(components)
    diagram.entities.append(entity)
    return diagram

## idea : 직선과 곡선의 교점 중에서 접점을 모두 찾아서 답하라.
@timeout(10)
def tangency7(diagram):
    components = []
    answer = []
    option = []

    x_list = []
    poly_degree = random.choice([3, 3, 3, 3, 4, 4, 5])
    one_answer = random.choice([True, True, True, False])

    while True:
        x_list = sorted([random.randint(-16, 16)/3 for i in range(random.randint(3, 6))])
        if len(set(x_list)) != len(x_list):
            if max(x_list) - min(x_list) > 9:
                min_diff_count = 0
                semi_min_diff_count = 0
                for i in range(len(x_list)-1):
                    if 0 < np.abs(x_list[i+1] - x_list[i]) <= 1:
                        if np.abs(x_list[i+1] - x_list[i]) < 0.5:
                            min_diff_count += 1
                        semi_min_diff_count += 1
                if (min_diff_count == 0) and (semi_min_diff_count<2):
                    if len(set(x_list)) < poly_degree:
                        break
                    elif one_answer:
                        break
                    else:
                        if (len(x_list)-len(set(x_list)) > 1):
                            break

    p1 = Polynomial(-6, 6, x_list)
    line_choice = random.choice([True, False])
    if line_choice:
        p1.x = np.linspace(p1.start, p1.end, 800)
        slope = random.uniform(-2, 2)
        y_intercept = random.uniform(-2, 2)
        p1.y = p1.y + slope*p1.x + y_intercept
    components.append(p1)

    unique_x = list(set(x_list))
    while True:
        option = random.sample(point_labels, len(unique_x))
        if 'O' not in option:
            break

    answer = []
    for idx in range(len(unique_x)):
        x = unique_x[idx]
        y = 0
        if line_choice:
            y += (slope * x + y_intercept)
        new_point = Point(x, y, label=option[idx], color=random.choice(color_list))
        components.append(new_point)
        if x_list.count(x) > 1:
            answer.append(option[idx])    
    
    if line_choice:
        components.append(Line(slope, y_intercept, color=random.choice(color_list)))
    else:
        components.append(Line(0, 0, color=random.choice(color_list)))

    random.shuffle(option)
    random.shuffle(answer)
    
    entity = ("tangency7", [", ".join(answer), "/".join(option), ", ".join(option)])
    diagram.components.extend(components)
    diagram.entities.append(entity)
    return diagram

## idea : 곡선과 곡선의 교점 중 접점을 모두 찾아서 답하라.
@timeout(10)
def tangency8(diagram):
    components = []
    answer = []
    option = []

    x_list = []
    poly_degree = random.choice([3, 3, 3, 3, 4, 4, 5])
    one_answer = random.choice([True, True, True, False])

    while True:
        x_list = sorted([random.randint(-16, 16)/3 for i in range(random.randint(3, 6))])
        if len(set(x_list)) != len(x_list):
            if max(x_list) - min(x_list) > 9:
                min_diff_count = 0
                semi_min_diff_count = 0
                for i in range(len(x_list)-1):
                    if 0 < np.abs(x_list[i+1] - x_list[i]) <= 1:
                        if np.abs(x_list[i+1] - x_list[i]) < 0.5:
                            min_diff_count += 1
                        semi_min_diff_count += 1
                if (min_diff_count == 0) and (semi_min_diff_count<2):
                    if len(set(x_list)) < poly_degree:
                        break
                    elif one_answer:
                        break
                    else:
                        if (len(x_list)-len(set(x_list)) > 1):
                            break
    
    x_list2 = copy.deepcopy(x_list)
    for x in x_list:
        if x_list.count(x) < 2:
            if random.randint(1, 3) == 1:
                x_list2.append(x)
                if random.randint(1, 2) == 1:
                    x_list2.append(x)

    while True:
        p1 = Polynomial(-6, 6, x_list)
        p2 = Polynomial(-6, 6, x_list2)
        if np.abs(p1.y[0] - p2.y[0]) > 1e-3:
            break

    color1, color2 = random.sample(color_list, 2)
    p1.line_color = color1
    p2.line_color = color2

    line_choice = random.choice([True, False])
    if line_choice:
        slope = random.uniform(-2, 2)
        y_intercept = random.uniform(-2, 2)
        p1.y = p1.y + slope*p1.x + y_intercept
        p2.y = p2.y + slope*p2.x + y_intercept

    components.append(p1)
    components.append(p2)

    unique_x = list(set(x_list))
    while True:
        option = random.sample(point_labels, len(unique_x))
        if 'O' not in option:
            break

    answer = []
    for idx in range(len(unique_x)):
        x = unique_x[idx]
        y = 0
        if line_choice:
            y += (slope * x + y_intercept)
        new_point = Point(x, y, label=option[idx], color=random.choice(color_list))
        components.append(new_point)
        if x_list.count(x) > 1:
            answer.append(option[idx])

    random.shuffle(option)
    random.shuffle(answer)
    
    entity = ("tangency8", [", ".join(answer), "/".join(option), ", ".join(option)])
    diagram.components.extend(components)
    diagram.entities.append(entity)
    return diagram

## idea : 특정 점 A에서 ~색 직선에 접하는 곡선을 모두 골라라.
@timeout(10)
def tangency9(diagram):
    components = []

    num_curves = random.choice([2, 2, 2, 2, 2, 3, 3, 3, 4])
    option = random.sample(color_list, num_curves+1)
    line_color = option[-1]
    option = option[:-1]
    if num_curves == 2:
        num_answers = 1
    else:
        num_answers = random.choice([1, 1, 1, 2])
    answer = option[:num_answers]

    trial = 0
    while True:
        candidate_list = random.sample([i/3 for i in range(-16, 16)], random.randint(2, 4))
        if max(candidate_list) - min(candidate_list) > 9:
            min_diff_count = 0
            semi_min_diff_count = 0
            for i in range(len(candidate_list)-1):
                if 0 < np.abs(candidate_list[i+1] - candidate_list[i]) <= 1:
                    if np.abs(candidate_list[i+1] - candidate_list[i]) < 0.5:
                        min_diff_count += 1
                    semi_min_diff_count += 1
            if (min_diff_count == 0) and (semi_min_diff_count<2):
                break
        if trial > 10000:
            break
        trial += 1

    label_list = random.sample(point_labels, len(candidate_list))
    label_point = label_list[0]
    
    line_choice = random.choice([True, False])
    if line_choice:
        slope = random.uniform(-2, 2)
        y_intercept = random.uniform(-2, 2)
    
    if line_choice:
        line = Line(slope, y_intercept, color=line_color)
        components.append(line)
    else:
        line = Line(0, 0, color=line_color)
        components.append(line)
    
    for idx in range(len(candidate_list)):
        x = candidate_list[idx]
        label = label_list[idx]
        y = line.slope * x + line.intercept
        new_point = Point(x, y, label=label, color=random.choice(color_list))
        components.append(new_point)
    
    start_y = []
    for idx in range(num_answers):
        trial = 0
        while True:
            x_dict = {i:random.randint(0, 2) for i in candidate_list}
            x_dict[candidate_list[0]] = random.choice([2, 2, 2, 3, 4])
            x_list = []
            for x in x_dict:
                for _ in range(x_dict[x]):
                    x_list.append(x)
            p1 = Polynomial(-6, 6, x_list)
            p1.line_color = option[idx]
            if round(p1.y[0], 3) not in start_y:
                break
            if trial > 10000:
                break
            trial += 1
        start_y.append(round(p1.y[0], 3))
        if line_choice:
            p1.y = p1.y + slope*p1.x + y_intercept
        components.append(p1)
    
    start_y = []
    for idx in range(num_answers, num_curves):
        trial = 0
        while True:
            x_dict = {i:random.randint(0, 2) for i in candidate_list}
            x_dict[candidate_list[0]] = 1
            x_list = []
            for x in x_dict:
                for _ in range(x_dict[x]):
                    x_list.append(x)
            p1 = Polynomial(-6, 6, x_list)
            p1.line_color = option[idx]
            if round(p1.y[0], 3) not in start_y:
                break
            if trial > 10000:
                break
            trial += 1
        start_y.append(round(p1.y[0], 3))
        if line_choice:
            p1.y = p1.y + slope*p1.x + y_intercept
        components.append(p1)

    random.shuffle(option)
    random.shuffle(answer)
    entity = ("tangency9", [str(num_curves), label_point, line_color, ", ".join(answer), "/".join(option), ", ".join(option)])
    diagram.components.extend(components)
    diagram.entities.append(entity)
    return diagram


rules = [
    tangency1,
    tangency2,
    tangency3,
    tangency4,
    tangency5,
    tangency6,
    tangency7,
    tangency8,
    tangency9
]
