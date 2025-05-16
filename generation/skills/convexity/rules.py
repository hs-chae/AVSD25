import numpy as np
import matplotlib.pyplot as plt
import random

from scipy.spatial import ConvexHull
from shapely.geometry import Polygon
from matplotlib.patches import Rectangle

point_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_labels = list("1234567890")
func_labels = list("abcdefghijklmnopqrstuvwxyz")
color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

def rescale_and_quantize(x, y, target_points=500, x_range=(-10, 10), y_range=(-10, 10)):
    x_min, x_max = min(x), max(x)
    y_min, y_max = min(y), max(y)
    
    x_rescaled = (x - x_min) / (x_max - x_min)
    y_rescaled = (y - y_min) / (y_max - y_min)
    
    x_scaled = x_rescaled * (x_range[1] - x_range[0]) + x_range[0]
    y_scaled = y_rescaled * (y_range[1] - y_range[0]) + y_range[0]
    
    indices = np.linspace(0, len(x_scaled) - 1, target_points).astype(int)
    x_quantized = x_scaled[indices]
    y_quantized = y_scaled[indices]
    
    return x_quantized, y_quantized


# convex, concave lens
class Lens:
    def __init__(self, convex_concave, udlr = None, start = 1, end = 30, lens_color = None, label = None):
        if udlr == None:
            self.generate_random_udlr(start, end)
        else:
            self.udlr = udlr
        self.up = self.udlr[3]
        self.down = self.udlr[0]
        self.left = self.udlr[1]
        self.right = self.udlr[2]
        self.is_same = random.choice([True, False])
        self.label = label
        self.convex_concave = convex_concave
        self.color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
        if convex_concave == "concave":
            self.make_concave_lens()
        else:
            self.make_convex_lens()
        if lens_color:
            self.lens_color = lens_color
        else:
            self.lens_color = random.choice(self.color_list)
        return
    
    def make_concave_lens(self):
        self.middle = (self.left+self.right)/2
        diff = self.middle-self.left

        k1 = random.uniform(0.01*diff, diff)
        if self.is_same:
            k2 = -k1
        else:
            k2 = random.uniform(-1*diff, -0.01*diff)

        def left_lens(y):
            return -1*(y-self.up)*(y-self.down)*4*k1/((self.up-self.down)**2)+self.left

        def right_lens(y):
            return -1*(y-self.up)*(y-self.down)*4*k2/((self.up-self.down)**2)+self.right

        self.left_lens_y = np.linspace(self.down, self.up, 100)
        self.left_lens_x = left_lens(self.left_lens_y)
        self.right_lens_y = np.linspace(self.down, self.up, 100)
        self.right_lens_x = right_lens(self.right_lens_y)

    def make_convex_lens(self):
        self.up = self.udlr[3]
        self.down = self.udlr[0]
        self.left = self.udlr[1]
        self.right = self.udlr[2]
        self.middle = (self.left+self.right)/2
        diff = self.middle-self.left

        k1 = -1 * random.uniform(0.01*diff, diff)
        if self.is_same:
            k2 = -k1
        else:
            k2 = -1 * random.uniform(-1*diff, -0.01*diff)
        
        self.udlr = list(self.udlr)
        self.left, self.udlr[1] = self.left-k1, self.left-k1
        self.right, self.udlr[2] = self.right+k2, self.right+k2
        self.udlr = tuple(self.udlr)

        def left_lens(y):
            return -1*(y-self.up)*(y-self.down)*4*k1/((self.up-self.down)**2)+self.left

        def right_lens(y):
            return -1*(y-self.up)*(y-self.down)*4*k2/((self.up-self.down)**2)+self.right

        self.left_lens_y = np.linspace(self.down, self.up, 100)
        self.left_lens_x = left_lens(self.left_lens_y)
        self.right_lens_y = np.linspace(self.down, self.up, 100)
        self.right_lens_x = right_lens(self.right_lens_y)

    def plot(self, ax, tc, set_visible=True):
        line = ax.plot(self.left_lens_x, self.left_lens_y, c = self.lens_color)
        line[0].set_visible(set_visible)
        line = ax.plot(self.right_lens_x, self.right_lens_y, c = self.lens_color)
        line[0].set_visible(set_visible)
        line = ax.plot([self.left, self.right], [self.up, self.up], c = self.lens_color)
        line[0].set_visible(set_visible)
        line = ax.plot([self.left, self.right], [self.down, self.down], c = self.lens_color)
        line[0].set_visible(set_visible)
        if self.label:
            tc.append(self.middle, self.up + 0.5, self.label, c = random.choice(self.color_list))
        ax.axis('equal')
        ax.axis('off')

    def generate_random_udlr(self, start = 1, end = 30):
        while True:
            udlr = random.sample(range(start, end), 4)
            udlr.sort()
            if (udlr[3] - udlr[0]) > 2*(udlr[2]-udlr[1]):
                break
        self.udlr = udlr


# convex, concave shape
class Shape:
    def __init__(self, convex_concave, num_points = None, xlim=(0, 100), ylim=(0, 100), facecolor = None, edgecolor = None, label = None):
        facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
        edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
        self.xlim = xlim
        self.ylim = ylim
        self.label = label

        if facecolor:
            self.facecolor = facecolor
        else:
            self.facecolor = random.choice(facecolor_list)

        if edgecolor:
            self.edgecolor = edgecolor
        else:
            self.edgecolor = random.choice(edgecolor_list)
        
        self.convex_concave = convex_concave
        if convex_concave == "convex":
            if num_points:
                self.num_points = num_points
            else:
                self.num_points = random.randint(3, 30)
            self.generate_convex_shape()
        else:
            if num_points:
                self.num_points = num_points
            else:
                self.num_points = random.randint(4, 10)
            self.generate_concave_shape()

    def generate_convex_shape(self):
        trial = 0
        while trial < 100:
            try:
                rng = np.random.default_rng()
                points = rng.random((self.num_points, 2)) *random.randint(self.xlim[0], self.xlim[1]) 
                hull = ConvexHull(points)
                self.x = points[np.append(hull.vertices, hull.vertices[0:1]),0]
                self.y = points[np.append(hull.vertices, hull.vertices[0:1]),1]
                self.regularize()
                break
            except:
                trial += 1

    def generate_random_points(self):
        points = [(random.randint(self.xlim[0], self.xlim[1]), random.randint(self.ylim[0], self.ylim[1])) for _ in range(self.num_points)]
        random.shuffle(points)
        return points

    def generate_concave_shape(self):
        trial = 0
        while True:
            try:
                points = self.generate_random_points()
                polygon = Polygon(points)
                if polygon.is_valid and polygon.area > 0:
                    if polygon.convex_hull.equals(polygon) == False:
                        self.x, self.y = polygon.exterior.xy
                        break
            except:
                trial += 1
                if trial > 1000:
                    raise
        self.regularize()

    def regularize(self):
        a, b = self.xlim
        c, d = self.ylim
        
        x_min, x_max = min(self.x), max(self.x)
        y_min, y_max = min(self.y), max(self.y)
        
        self.x = [(xi - x_min) / (x_max - x_min) * (b - a) + a for xi in self.x]
        self.y = [(yi - y_min) / (y_max - y_min) * (d - c) + c for yi in self.y]
    
    def plot(self, ax, tc, set_visible = True):
        fill = ax.fill(self.x, self.y, alpha=random.random()/2, color=self.facecolor)
        fill[0].set_visible(set_visible)
        line = ax.plot(self.x, self.y, color=(self.edgecolor))
        line[0].set_visible(set_visible)
        if self.label:
            if random.randint(0, 1) == 1:
                tc.append(np.mean(self.xlim), np.mean(self.ylim), self.label, c = random.choice(color_list))
            else:
                i = random.randint(0, len(self.x)-1)
                tc.append(self.x[i], self.y[i], self.label)
        ax.axis('off')


class OneFunction:
    def __init__(self, convex_concave, color = None):
        self.func = None
        self.convex_concave = convex_concave
        if convex_concave == "convex":
            self.make_convex_ftn()
        else:
            self.make_concave_ftn()
        self.x = np.linspace(-10, 10, 400)
        self.y = self.func(self.x)
        max_y = max(self.y)
        min_y = min(self.y)
        self.y = 20/(max_y-min_y)*(self.y-min_y)-10
        self.x, self.y = rescale_and_quantize(self.x, self.y, target_points=400)
        if color:
            self.line_color = color
        else:
            color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
            self.line_color = random.choice(color_list)
        return
    
    def make_convex_ftn(self):
        convex_functions = [
            lambda x: x**2,
            lambda x: (x - 1)**2,
            lambda x: (x + 2)**2,
            lambda x: x**4,
            lambda x: x**2 + x**4,
            lambda x: np.exp(x), 
            lambda x: x**2 + 5,
            lambda x: 0.5 * x**2,
            lambda x: x**2 + np.exp(x),
            lambda x: np.log(1 + np.exp(x)),  
            lambda x: 2 * x**2,
            lambda x: 3 * x**2 + 2 * x + 1,  
            lambda x: (x - 1)**4 + 3,
            lambda x: (x + 1)**4,
            lambda x: np.exp(0.5 * x),      
            lambda x: 4 * x**2 + 2,
            lambda x: x**2 + 10 * x + 50,   
            lambda x: (x**2 + 1)**2,         
            lambda x: (x + 3)**2,            
            lambda x: 1 + 0.3 * x**2         
        ]
        self.func = random.choice(convex_functions)
        return
    
    def make_concave_ftn(self):
        concave_functions = [
            lambda x: -x**2,
            lambda x: -(x + 1)**2,
            lambda x: -(x - 2)**2,
            lambda x: -x**4,
            lambda x: -(x**2 + x**4),
            lambda x: -np.exp(x),         
            lambda x: -(x**2 + 5),
            lambda x: -0.5 * x**2,
            lambda x: -(x**2 + np.exp(x)),
            lambda x: -np.log(1 + np.exp(x)), 
            lambda x: -2 * x**2,
            lambda x: -(3 * x**2 + 2 * x + 1), 
            lambda x: -((x - 1)**4 + 3),
            lambda x: -((x + 1)**4),
            lambda x: -np.exp(0.5 * x),
            lambda x: -(4 * x**2 + 2),
            lambda x: -(x**2 + 10 * x + 50),
            lambda x: -((x**2 + 1)**2),
            lambda x: -((x + 3)**2),
            lambda x: 5 - 0.3 * x**2   
        ]
        self.func = random.choice(concave_functions)
        return
    
    def plot(self, ax, tc, set_visible = True):
        line = ax.plot(self.x, self.y, color = self.line_color)
        line[0].set_visible(set_visible)

        if random.randint(1, 2) == 1:
            ax.set_xlabel("x")
            ax.set_ylabel("y")

        if (random.randint(1, 2) == 1) and (set_visible):
            ax.grid(True)
        else:
            ax.grid(False)

        if random.randint(1, 2) == 1:
            ax.axis('off')

class FunctionRectangle:
    def __init__(self, start, end):
        self.func = None
        self.start = start
        self.end = end
        self.x = None
        self.y = None
        self.intervals = []
        self.info_dict = {}
        facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
        edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
        textcolor_list = ["black", "red", "blue", "green", "orange", "purple", "pink", "brown", "cyan"]

        while True:
            edgecolor = random.choice(edgecolor_list)
            facecolor = random.choice(facecolor_list)
            textcolor = random.choice(textcolor_list)
            if len(set([edgecolor, facecolor, textcolor])) == 3:
                break
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.textcolor = textcolor
        while True:
            self.get_interval()
            if len(self.intervals) > 2:
                break
        if random.randint(1, 2) == 1:
            self.label_list = random.sample(random.choice([point_labels, num_labels, func_labels]), len(self.intervals))
            self.type_label = 1
        else:
            self.label_list = [i for i in range(1, len(self.intervals)+1)]
            self.type_label = 2
        self.get_info_dict()
        return

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

    def find_convex_concave_intervals(self):
        d2 = self.second_derivative() 
        self.intervals = []
        sign_prev = np.sign(d2[0])
        start_idx = 0
        
        for i in range(1, len(self.x)):
            sign_now = np.sign(d2[i])
            if sign_now != sign_prev:
                if sign_prev != 0:
                    self.intervals.append((self.x[start_idx], self.x[i], sign_prev))
                start_idx = i
                sign_prev = sign_now
        
        if sign_prev != 0:
            self.intervals.append((self.x[start_idx], self.x[-1], sign_prev))
    
    def get_info_dict(self):
        self.info_dict = {"concave":[], "convex":[]}
        self.options = []
        ratio = 0.5
        while (0.2<ratio<0.8):
            ratio = random.random()

        for idx, (start_x, end_x, s) in enumerate(self.intervals, start=1):
            if s > 0:
                self.info_dict["convex"].append(self.label_list[idx-1])
            else:
                self.info_dict["concave"].append(self.label_list[idx-1])
            self.options.append(self.label_list[idx-1])
        if self.type_label == 1:
            random.shuffle(self.options)
        
    def plot(self, ax, tc, set_visible = True):
        line = ax.plot(self.x, self.y, color='black', linewidth=2)
        line[0].set_visible(set_visible)
        
        y_min, y_max = self.y.min(), self.y.max()
        total_height = y_max - y_min
        ratio = 0.5
        while (0.2<ratio<0.8):
            ratio = random.random()

        for idx, (start_x, end_x, s) in enumerate(self.intervals, start=1):

            label_text = self.label_list[idx-1]
            width = end_x - start_x
            text_y = y_min + total_height * ratio
            
            rect = Rectangle(
                (start_x, y_min),  
                width,             
                total_height,      
                edgecolor = self.edgecolor,
                facecolor = self.facecolor,
                alpha = 0.1
            )
            ax.add_patch(rect).set_visible(set_visible)
            
            mid_x = (start_x + end_x) / 2
            tc.append(mid_x, text_y, label_text, color=self.textcolor,
                    ha='center', va='top')

        ax.axis('off')

    def get_interval(self):
        self.x = np.linspace(self.start, self.end, 800)
        self.poly_function()
        self.y = self.func(self.x)
        max_y = max(self.y)
        min_y = min(self.y)
        self.x, self.y = rescale_and_quantize(self.x, self.y, target_points=800)
        self.find_convex_concave_intervals()

class FunctionPoint:
    def __init__(self, start, end):
        self.func = None
        self.start = start
        self.end = end
        self.x = None
        self.y = None
        self.intervals = []
        self.info_dict = {}
        facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
        edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
        textcolor_list = ["black", "red", "blue", "green", "orange", "purple", "pink", "brown", "cyan"]

        while True:
            edgecolor = random.choice(edgecolor_list)
            facecolor = random.choice(facecolor_list)
            textcolor = random.choice(textcolor_list)
            if len(set([edgecolor, facecolor, textcolor])) == 3:
                break
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.textcolor = textcolor
        while True:
            self.get_interval()
            if len(self.intervals) > 2:
                break
        if random.randint(1, 2) == 1:
            self.label_list = random.sample(random.choice([point_labels, num_labels, func_labels]), len(self.intervals))
        else:
            self.label_list = [i for i in range(1, len(self.intervals)+1)]
        self.get_info_dict()

    def create_polynomial_from_zeros(self, zeros):
        coefficients = [random.uniform(-3, 3)]
        for zero in zeros:
            coefficients = np.convolve(coefficients, [1, -zero]) 
        return coefficients


    def poly_function(self):
        num_zeros = random.randint(2, 6)
        zeros = [random.uniform(self.start+0.1, self.end-0.1) for _ in range(num_zeros)]
        coefficients = self.create_polynomial_from_zeros(zeros)
        def f(x):
            return sum(coefficients[i] * x**(len(coefficients) - 1 - i) for i in range(len(coefficients)))
        self.func = f

    def second_derivative(self):
        return np.gradient(np.gradient(self.y, self.x), self.x)

    def find_convex_concave_intervals(self):
        d2 = self.second_derivative() 
        self.intervals = []
        sign_prev = np.sign(d2[0])
        start_idx = 0
        
        for i in range(1, len(self.x)):
            sign_now = np.sign(d2[i])
            if sign_now != sign_prev:
                if sign_prev != 0:
                    self.intervals.append((self.x[start_idx], self.x[i], sign_prev))
                start_idx = i
                sign_prev = sign_now
        
        if sign_prev != 0:
            self.intervals.append((self.x[start_idx], self.x[-1], sign_prev))
    
    def get_info_dict(self):
        self.info_dict = {"concave":[], "convex":[]}
        self.options = []
        ratio = 0.5
        while (0.2<ratio<0.8):
            ratio = random.random()

        for idx, (start_x, end_x, s) in enumerate(self.intervals, start=1):
            if idx == 1:
                new_string = f"Before {self.label_list[idx-1]}"
            elif idx == len(self.intervals):
                new_string = f"After {self.label_list[idx-2]}"
            else:
                new_string = f"Between {self.label_list[idx-2]} and {self.label_list[idx-1]}"
            
            self.options.append(new_string)

            if s > 0:
                self.info_dict["convex"].append(new_string)
            else:
                self.info_dict["concave"].append(new_string)
        
    def plot(self, ax, tc, set_visible = True):
        line = ax.plot(self.x, self.y, color='black', linewidth=2)
        line[0].set_visible(set_visible)
        
        y_min, y_max = self.y.min(), self.y.max()
        ratio = 0.5
        while (0.2<ratio<0.8):
            ratio = random.random()

        for idx, (start_x, end_x, s) in enumerate(self.intervals, start=1):
            label_text = self.label_list[idx-1]
            if idx != len(self.intervals):
                end_y = self.y[np.where(self.x==end_x)[0][0]]
                ax.scatter(end_x, end_y, color = "red").set_visible(set_visible)
                tc.append(end_x, end_y, label_text, color=self.textcolor,
                        ha='center', va='top')

        ax.axis('off')

    def get_interval(self):
        self.x = np.linspace(self.start, self.end, 800)
        self.poly_function()
        self.y = self.func(self.x)
        max_y = max(self.y)
        min_y = min(self.y)
        self.x, self.y = rescale_and_quantize(self.x, self.y, target_points=800)
        self.find_convex_concave_intervals()


class Point:
    def __init__(self, label, x, y, color='black', alpha=1, size=20):
        self.label = label
        self.x = x
        self.y = y
        self.color = color
        self.alpha = alpha
        self.size = size
    
    def plot(self, ax, tc, set_visible=True):
        scatter = ax.scatter(self.x, self.y, color=self.color)
        scatter.set_visible(set_visible)
        tc.append(self.x, self.y, self.label)

class Diagram:
    def __init__(self,components = None,entities=None,background_color='white',labels=None,colors=None):
        self.components = components if components is not None else []
        self.entities = entities if entities is not None else []
        self.background_color = background_color
        self.labels = labels if labels is not None else []
        self.colors = colors if colors is not None else []

def make_point_label(diagram):
    trial = 0
    while trial < 10000:
        new_label = random.choice(point_labels)
        if new_label not in diagram.labels:
            return new_label
        trial += 1
    raise

# 아이디어 : concave/convex 도형 1개
def convexity1(diagram):
    convex_concave = random.choice(['convex', 'concave'])
    shape1 = Shape(convex_concave)
    diagram.components.append(shape1)
    if random.randint(1, 2) == 1:
        num_points = random.randint(1, 10)
        if random.randint(1, 2) == 1:
            for _ in range(num_points):
                new_label = ""
                new_point = Point(new_label, random.uniform(0, 100), random.uniform(0, 100), color = random.choice(color_list), alpha = random.random(), size = random.randint(10, 30))
                diagram.components.append(new_point)
                diagram.labels.append(new_label)
        else:
            for _ in range(num_points):
                if random.randint(1, 2) == 1:
                    new_label = make_point_label(diagram)
                    diagram.labels.append(new_label)
                else:
                    new_label = ""
                new_point = Point(new_label, random.uniform(0, 100), random.uniform(0, 100), color = random.choice(color_list), alpha = random.random(), size = random.randint(10, 30))
                diagram.components.append(new_point)
    diagram.entities.append(("convexity1", ["polygon", convex_concave]))
    return diagram

# 아이디어 : concave/convex인 도형 하나 골라 그 label로 답하기
def convexity2(diagram):
    option_list = []
    answer_label = ""
    num_shapes = random.choice([2, 4, 6, 8, 9])
    lim_list = [(0, 40), (50, 90), (100, 140), (150, 190)]
    if num_shapes == 2:
        if random.randint(1, 2) == 1:
            x_max = 1
            y_max = 2
        else:
            x_max = 2
            y_max = 1
    elif num_shapes == 4:
        x_max = 2
        y_max = 2
    elif num_shapes == 6:
        if random.randint(1, 2) == 1:
            x_max = 2
            y_max = 3
        else:
            x_max = 3
            y_max = 2
    elif num_shapes == 8:
        if random.randint(1, 2) == 1:
            x_max = 4
            y_max = 2
        else:
            x_max = 2
            y_max = 4
    else:
        x_max = 3
        y_max = 3

    xlim_list = lim_list[:x_max]
    ylim_list = lim_list[:y_max]

    answer_x = random.randint(0, x_max-1)
    answer_y = random.randint(0, y_max-1)
    convex_concave = random.choice(['convex', 'concave'])
    if convex_concave == 'concave':
        other_type = 'convex' 
    else:
        other_type = 'concave'
    label_add = np.array(random.sample(random.choice([point_labels, num_labels]), num_shapes)).reshape(x_max, y_max)
    
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            label = "shape"+label_add[x_idx, y_idx]
            if (x_idx == answer_x) and (y_idx == answer_y):
                new_shape = Shape(convex_concave, num_points = None, xlim=xlim_list[x_idx], ylim=ylim_list[y_idx], label = label)
                answer_label = label_add[x_idx, y_idx]
            else:
                new_shape = Shape(other_type, num_points = None, xlim=xlim_list[x_idx], ylim=ylim_list[y_idx], label = label)
            diagram.components.append(new_shape)
            option_list.append(label)
            diagram.labels.append(label)
    random.shuffle(option_list)
    diagram.entities.append(("convexity2", ["polygon", convex_concave, "/".join(option_list), ", ".join(option_list), answer_label]))
    return diagram

# 아이디어 : concave/convex인 도형 하나 골라 그 color로 답하기
def convexity3(diagram):
    option_list = []
    answer_color = ""
    num_shapes = random.choice([2, 4, 6, 8, 9])
    lim_list = [(0, 40), (50, 90), (100, 140), (150, 190)]
    if num_shapes == 2:
        if random.randint(1, 2) == 1:
            x_max = 1
            y_max = 2
        else:
            x_max = 2
            y_max = 1
    elif num_shapes == 4:
        x_max = 2
        y_max = 2
    elif num_shapes == 6:
        if random.randint(1, 2) == 1:
            x_max = 2
            y_max = 3
        else:
            x_max = 3
            y_max = 2
    elif num_shapes == 8:
        if random.randint(1, 2) == 1:
            x_max = 4
            y_max = 2
        else:
            x_max = 2
            y_max = 4
    else:
        x_max = 3
        y_max = 3

    xlim_list = lim_list[:x_max]
    ylim_list = lim_list[:y_max]

    answer_x = random.randint(0, x_max-1)
    answer_y = random.randint(0, y_max-1)
    convex_concave = random.choice(['convex', 'concave'])
    if convex_concave == 'concave':
        other_type = 'convex' 
    else:
        other_type = 'concave'
    color_add = np.array(random.sample(color_list, num_shapes)).reshape(x_max, y_max)

    if random.choice([True, False]):
        label_add = np.array(random.sample(random.choice([point_labels, num_labels]), num_shapes)).reshape(x_max, y_max)
    else:
        label_add = np.array([None]*(x_max*y_max)).reshape(x_max, y_max)
    
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            color = color_add[x_idx, y_idx]
            if label_add[x_idx, y_idx] != None:
                label = "shape"+label_add[x_idx, y_idx]
            else:
                label = None
            if (x_idx == answer_x) and (y_idx == answer_y):
                new_shape = Shape(convex_concave, num_points = None, xlim=xlim_list[x_idx], ylim=ylim_list[y_idx], facecolor = color, edgecolor = color, label = label)
                answer_color = color_add[x_idx, y_idx]
            else:
                new_shape = Shape(other_type, num_points = None, xlim=xlim_list[x_idx], ylim=ylim_list[y_idx], facecolor = color, edgecolor = color, label = label)
            diagram.components.append(new_shape)
            option_list.append(color)
            diagram.colors.append(color)
    random.shuffle(option_list)
    diagram.entities.append(("convexity3", ["polygon", convex_concave, "/".join(option_list), ", ".join(option_list), answer_color]))
    return diagram

# 아이디어 : concave/convex인 도형 모두 골라 그 label로 답하기
def convexity4(diagram):
    option_list = []
    answer_labels = []
    num_shapes = random.choice([4, 6, 8, 9])
    lim_list = [(0, 40), (50, 90), (100, 140), (150, 190)]
    if num_shapes == 2:
        if random.randint(1, 2) == 1:
            x_max = 1
            y_max = 2
        else:
            x_max = 2
            y_max = 1
    elif num_shapes == 4:
        x_max = 2
        y_max = 2
    elif num_shapes == 6:
        if random.randint(1, 2) == 1:
            x_max = 2
            y_max = 3
        else:
            x_max = 3
            y_max = 2
    elif num_shapes == 8:
        if random.randint(1, 2) == 1:
            x_max = 4
            y_max = 2
        else:
            x_max = 2
            y_max = 4
    else:
        x_max = 3
        y_max = 3

    xlim_list = lim_list[:x_max]
    ylim_list = lim_list[:y_max]

    num_answer = random.randint(2, num_shapes-1)
    answer_list = []
    while len(answer_list) < num_answer:
        x = random.randint(0, x_max-1)
        y = random.randint(0, y_max-1)
        if (x, y) not in answer_list:
            answer_list.append((x, y))

    convex_concave = random.choice(['convex', 'concave'])
    if convex_concave == 'concave':
        other_type = 'convex' 
    else:
        other_type = 'concave'
    label_add = np.array(random.sample(random.choice([point_labels, num_labels]), num_shapes)).reshape(x_max, y_max)
    
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            label = "shape"+label_add[x_idx, y_idx]
            if (x_idx, y_idx) in answer_list:
                new_shape = Shape(convex_concave, num_points = None, xlim=xlim_list[x_idx], ylim=ylim_list[y_idx], label = label)
                answer_labels.append(label_add[x_idx, y_idx])
            else:
                new_shape = Shape(other_type, num_points = None, xlim=xlim_list[x_idx], ylim=ylim_list[y_idx], label = label)
            diagram.components.append(new_shape)
            option_list.append(label)
            diagram.labels.append(label)
    random.shuffle(option_list)
    diagram.entities.append(("convexity4", ["polygon", convex_concave, "/".join(option_list), ", ".join(option_list), ", ".join(answer_labels)]))
    return diagram

# 아이디어 : concave/convex인 도형 모두 골라 그 color로 답하기
def convexity5(diagram):
    option_list = []
    answer_colors = []
    num_shapes = random.choice([4, 6, 8, 9])
    lim_list = [(0, 40), (50, 90), (100, 140), (150, 190)]
    if num_shapes == 2:
        if random.randint(1, 2) == 1:
            x_max = 1
            y_max = 2
        else:
            x_max = 2
            y_max = 1
    elif num_shapes == 4:
        x_max = 2
        y_max = 2
    elif num_shapes == 6:
        if random.randint(1, 2) == 1:
            x_max = 2
            y_max = 3
        else:
            x_max = 3
            y_max = 2
    elif num_shapes == 8:
        if random.randint(1, 2) == 1:
            x_max = 4
            y_max = 2
        else:
            x_max = 2
            y_max = 4
    else:
        x_max = 3
        y_max = 3

    xlim_list = lim_list[:x_max]
    ylim_list = lim_list[:y_max]

    num_answer = random.randint(2, num_shapes-1)
    answer_list = []
    while len(answer_list) < num_answer:
        x = random.randint(0, x_max-1)
        y = random.randint(0, y_max-1)
        if (x, y) not in answer_list:
            answer_list.append((x, y))

    answer_x = random.randint(0, x_max-1)
    answer_y = random.randint(0, y_max-1)
    convex_concave = random.choice(['convex', 'concave'])
    if convex_concave == 'concave':
        other_type = 'convex' 
    else:
        other_type = 'concave'
    color_add = np.array(random.sample(color_list, num_shapes)).reshape(x_max, y_max)

    if random.choice([True, False]):
        label_add = np.array(random.sample(random.choice([point_labels, num_labels]), num_shapes)).reshape(x_max, y_max)
    else:
        label_add = np.array([None]*(x_max*y_max)).reshape(x_max, y_max)
    
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            color = color_add[x_idx, y_idx]
            if label_add[x_idx, y_idx] != None:
                label = "shape"+label_add[x_idx, y_idx]
            else:
                label = None
            if (x_idx, y_idx) in answer_list:
                new_shape = Shape(convex_concave, num_points = None, xlim=xlim_list[x_idx], ylim=ylim_list[y_idx], facecolor = color, edgecolor = color, label = label)
                answer_colors.append(color_add[x_idx, y_idx])
            else:
                new_shape = Shape(other_type, num_points = None, xlim=xlim_list[x_idx], ylim=ylim_list[y_idx], facecolor = color, edgecolor = color, label = label)
            diagram.components.append(new_shape)
            option_list.append(color)
            diagram.colors.append(color)
    random.shuffle(option_list)
    diagram.entities.append(("convexity5", ["polygon", convex_concave, "/".join(option_list), ", ".join(option_list), ", ".join(answer_colors)]))
    return diagram

# 아이디어 : concave/convex function 1개
def convexity6(diagram):
    convex_concave = random.choice(['convex', 'concave'])
    func1 = OneFunction(convex_concave)
    diagram.components.append(func1)
    if random.randint(1, 2) == 1:
        num_points = random.randint(1, 10)
        if random.randint(1, 2) == 1:
            for _ in range(num_points):
                new_label = ""
                new_point = Point(new_label, random.uniform(0, 30), random.uniform(0, 30), color = random.choice(color_list), alpha = random.random(), size = random.randint(10, 30))
                diagram.components.append(new_point)
                diagram.labels.append(new_label)
        else:
            for _ in range(num_points):
                if random.randint(1, 2) == 1:
                    new_label = make_point_label(diagram)
                    diagram.labels.append(new_label)
                else:
                    new_label = ""
                new_point = Point(new_label, random.uniform(0, 30), random.uniform(0, 30), color = random.choice(color_list), alpha = random.random(), size = random.randint(10, 30))
                diagram.components.append(new_point)
    diagram.entities.append(("convexity6", ["function", convex_concave]))
    return diagram

# 아이디어 : 네모로 칠해진 영역 중에서 하나의 함수에서 concave/convex인 영역 고르기
def convexity7(diagram):
    func = FunctionRectangle(-10, 10)
    convex_concave = random.choice(['convex', 'concave'])
    diagram.components.append(func)
    diagram.entities.append(("convexity7", ["function", convex_concave, "/".join(map(str, func.options)), ", ".join(map(str, func.options)), ", ".join(map(str, func.info_dict[convex_concave]))]))
    return diagram

# 아이디어 : 점을 기준으로 나뉜 영역 중에서 하나의 함수에서 concave/convex인 영역 고르기
def convexity8(diagram):
    func = FunctionPoint(-10, 10)
    convex_concave = random.choice(['convex', 'concave'])
    diagram.components.append(func)
    diagram.entities.append(("convexity8", ["function", convex_concave, "/".join(map(str, func.options)), ", ".join(map(str, func.options)), ", ".join(map(str, func.info_dict[convex_concave]))]))

# 아이디어 : concave/convex 렌즈 1개
def convexity9(diagram):
    convex_concave = random.choice(['convex', 'concave'])
    lens1 = Lens(convex_concave)
    diagram.components.append(lens1)
    if random.randint(1, 2) == 1:
        num_points = random.randint(1, 10)
        if random.randint(1, 2) == 1:
            for _ in range(num_points):
                new_label = ""
                new_point = Point(new_label, random.uniform(lens1.left, lens1.right), random.uniform(lens1.down, lens1.up), color = random.choice(color_list), alpha = random.random(), size = random.randint(10, 30))
                diagram.components.append(new_point)
                diagram.labels.append(new_label)
        else:
            for _ in range(num_points):
                if random.randint(1, 2) == 1:
                    new_label = make_point_label(diagram)
                    diagram.labels.append(new_label)
                else:
                    new_label = ""
                new_point = Point(new_label, random.uniform(0, 100), random.uniform(0, 100), color = random.choice(color_list), alpha = random.random(), size = random.randint(10, 30))
                diagram.components.append(new_point)
    diagram.entities.append(("convexity9", ["lens", convex_concave]))
    return diagram

# 아이디어 : concave/convex인 렌즈 하나 골라 그 label로 답하기
def convexity10(diagram):
    option_list = []
    answer_label = ""
    num_shapes = random.choice([2, 4, 6, 8, 9])
    lim_list = [(0, 40), (50, 90), (100, 140), (150, 190)]
    if num_shapes == 2:
        if random.randint(1, 2) == 1:
            x_max = 1
            y_max = 2
        else:
            x_max = 2
            y_max = 1
    elif num_shapes == 4:
        x_max = 2
        y_max = 2
    elif num_shapes == 6:
        if random.randint(1, 2) == 1:
            x_max = 2
            y_max = 3
        else:
            x_max = 3
            y_max = 2
    elif num_shapes == 8:
        if random.randint(1, 2) == 1:
            x_max = 4
            y_max = 2
        else:
            x_max = 2
            y_max = 4
    else:
        x_max = 3
        y_max = 3

    xlim_list = []
    for i in range(x_max):
        a = 0
        b = 0
        while -3 < (a-b) < 3:
            a = random.randint(lim_list[i][0], lim_list[i][1])
            b = random.randint(lim_list[i][0], lim_list[i][1])
        xlim_list.append((min(a, b), max(a, b)))
    ylim_list = lim_list[:y_max]

    answer_x = random.randint(0, x_max-1)
    answer_y = random.randint(0, y_max-1)
    convex_concave = random.choice(['convex', 'concave'])
    if convex_concave == 'concave':
        other_type = 'convex' 
    else:
        other_type = 'concave'
    label_add = np.array(random.sample(random.choice([point_labels, num_labels]), num_shapes)).reshape(x_max, y_max)
    
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            label = "shape"+label_add[x_idx, y_idx]
            udlr = (ylim_list[y_idx][0], xlim_list[x_idx][0], xlim_list[x_idx][1], ylim_list[y_idx][1])
            if (x_idx == answer_x) and (y_idx == answer_y):
                new_shape = Lens(convex_concave, udlr = udlr, label = label)
                answer_label = label_add[x_idx, y_idx]
            else:
                new_shape = Lens(other_type, udlr = udlr, label = label)
            diagram.components.append(new_shape)
            option_list.append(label)
            diagram.labels.append(label)
    random.shuffle(option_list)
    diagram.entities.append(("convexity10", ["lens", convex_concave, "/".join(option_list), ", ".join(option_list), answer_label]))
    return diagram

# 아이디어 : concave/convex인 렌즈 하나 골라 그 color로 답하기
def convexity11(diagram):
    option_list = []
    answer_color = ""
    num_shapes = random.choice([2, 4, 6, 8, 9])
    lim_list = [(0, 40), (50, 90), (100, 140), (150, 190)]
    if num_shapes == 2:
        if random.randint(1, 2) == 1:
            x_max = 1
            y_max = 2
        else:
            x_max = 2
            y_max = 1
    elif num_shapes == 4:
        x_max = 2
        y_max = 2
    elif num_shapes == 6:
        if random.randint(1, 2) == 1:
            x_max = 2
            y_max = 3
        else:
            x_max = 3
            y_max = 2
    elif num_shapes == 8:
        if random.randint(1, 2) == 1:
            x_max = 4
            y_max = 2
        else:
            x_max = 2
            y_max = 4
    else:
        x_max = 3
        y_max = 3

    xlim_list = []
    for i in range(x_max):
        a = 0
        b = 0
        while -3 < (a-b) < 3:
            a = random.randint(lim_list[i][0], lim_list[i][1])
            b = random.randint(lim_list[i][0], lim_list[i][1])
        xlim_list.append((min(a, b), max(a, b)))
    ylim_list = lim_list[:y_max]

    answer_x = random.randint(0, x_max-1)
    answer_y = random.randint(0, y_max-1)
    convex_concave = random.choice(['convex', 'concave'])
    if convex_concave == 'concave':
        other_type = 'convex' 
    else:
        other_type = 'concave'
    color_add = np.array(random.sample(color_list, num_shapes)).reshape(x_max, y_max)

    if random.choice([True, False]):
        label_add = np.array(random.sample(random.choice([point_labels, num_labels]), num_shapes)).reshape(x_max, y_max)
    else:
        label_add = np.array([None]*(x_max*y_max)).reshape(x_max, y_max)
    
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            color = color_add[x_idx, y_idx]
            udlr = (ylim_list[y_idx][0], xlim_list[x_idx][0], xlim_list[x_idx][1], ylim_list[y_idx][1])
            if label_add[x_idx, y_idx] != None:
                label = "shape"+label_add[x_idx, y_idx]
            else:
                label = None
            if (x_idx == answer_x) and (y_idx == answer_y):
                new_shape = Lens(convex_concave, udlr = udlr, lens_color = color, label = label)
                answer_color = color_add[x_idx, y_idx]
            else:
                new_shape = Lens(other_type, udlr = udlr, lens_color = color, label = label)
            diagram.components.append(new_shape)
            option_list.append(color)
            diagram.colors.append(color)
    random.shuffle(option_list)
    diagram.entities.append(("convexity11", ["lens", convex_concave, "/".join(option_list), ", ".join(option_list), answer_color]))
    return diagram

# 아이디어 : concave/convex인 렌즈 모두 골라 그 label로 답하기
def convexity12(diagram):
    option_list = []
    answer_labels = []
    num_shapes = random.choice([4, 6, 8, 9])
    lim_list = [(0, 40), (50, 90), (100, 140), (150, 190)]
    if num_shapes == 2:
        if random.randint(1, 2) == 1:
            x_max = 1
            y_max = 2
        else:
            x_max = 2
            y_max = 1
    elif num_shapes == 4:
        x_max = 2
        y_max = 2
    elif num_shapes == 6:
        if random.randint(1, 2) == 1:
            x_max = 2
            y_max = 3
        else:
            x_max = 3
            y_max = 2
    elif num_shapes == 8:
        if random.randint(1, 2) == 1:
            x_max = 4
            y_max = 2
        else:
            x_max = 2
            y_max = 4
    else:
        x_max = 3
        y_max = 3

    xlim_list = []
    for i in range(x_max):
        a = 0
        b = 0
        while -3 < (a-b) < 3:
            a = random.randint(lim_list[i][0], lim_list[i][1])
            b = random.randint(lim_list[i][0], lim_list[i][1])
        xlim_list.append((min(a, b), max(a, b)))
    ylim_list = lim_list[:y_max]

    num_answer = random.randint(2, num_shapes-1)
    answer_list = []
    while len(answer_list) < num_answer:
        x = random.randint(0, x_max-1)
        y = random.randint(0, y_max-1)
        if (x, y) not in answer_list:
            answer_list.append((x, y))

    convex_concave = random.choice(['convex', 'concave'])
    if convex_concave == 'concave':
        other_type = 'convex' 
    else:
        other_type = 'concave'
    label_add = np.array(random.sample(random.choice([point_labels, num_labels]), num_shapes)).reshape(x_max, y_max)
    
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            label = "shape"+label_add[x_idx, y_idx]
            udlr = (ylim_list[y_idx][0], xlim_list[x_idx][0], xlim_list[x_idx][1], ylim_list[y_idx][1])
            if (x_idx, y_idx) in answer_list:
                new_shape = Lens(convex_concave, udlr = udlr, label = label)
                answer_labels.append(label_add[x_idx, y_idx])
            else:
                new_shape = Lens(other_type, udlr = udlr, label = label)
            diagram.components.append(new_shape)
            option_list.append(label)
            diagram.labels.append(label)
    random.shuffle(option_list)
    diagram.entities.append(("convexity12", ["lens", convex_concave, "/".join(option_list), ", ".join(option_list), ", ".join(answer_labels)]))
    return diagram    

# 아이디어 : concave/convex인 렌즈 모두 골라 그 color로 답하기
def convexity13(diagram):
    option_list = []
    answer_colors = []
    num_shapes = random.choice([4, 6, 8, 9])
    lim_list = [(0, 40), (50, 90), (100, 140), (150, 190)]
    if num_shapes == 2:
        if random.randint(1, 2) == 1:
            x_max = 1
            y_max = 2
        else:
            x_max = 2
            y_max = 1
    elif num_shapes == 4:
        x_max = 2
        y_max = 2
    elif num_shapes == 6:
        if random.randint(1, 2) == 1:
            x_max = 2
            y_max = 3
        else:
            x_max = 3
            y_max = 2
    elif num_shapes == 8:
        if random.randint(1, 2) == 1:
            x_max = 4
            y_max = 2
        else:
            x_max = 2
            y_max = 4
    else:
        x_max = 3
        y_max = 3

    xlim_list = []
    for i in range(x_max):
        a = 0
        b = 0
        while -3 < (a-b) < 3:
            a = random.randint(lim_list[i][0], lim_list[i][1])
            b = random.randint(lim_list[i][0], lim_list[i][1])
        xlim_list.append((min(a, b), max(a, b)))
    ylim_list = lim_list[:y_max]

    num_answer = random.randint(2, num_shapes-1)
    answer_list = []
    while len(answer_list) < num_answer:
        x = random.randint(0, x_max-1)
        y = random.randint(0, y_max-1)
        if (x, y) not in answer_list:
            answer_list.append((x, y))

    answer_x = random.randint(0, x_max-1)
    answer_y = random.randint(0, y_max-1)
    convex_concave = random.choice(['convex', 'concave'])
    if convex_concave == 'concave':
        other_type = 'convex' 
    else:
        other_type = 'concave'
    color_add = np.array(random.sample(color_list, num_shapes)).reshape(x_max, y_max)

    if random.choice([True, False]):
        label_add = np.array(random.sample(random.choice([point_labels, num_labels]), num_shapes)).reshape(x_max, y_max)
    else:
        label_add = np.array([None]*(x_max*y_max)).reshape(x_max, y_max)
    
    for x_idx in range(x_max):
        for y_idx in range(y_max):
            color = color_add[x_idx, y_idx]
            udlr = (ylim_list[y_idx][0], xlim_list[x_idx][0], xlim_list[x_idx][1], ylim_list[y_idx][1])
            if label_add[x_idx, y_idx] != None:
                label = "shape"+label_add[x_idx, y_idx]
            else:
                label = None
            if (x_idx, y_idx) in answer_list:
                new_shape = Lens(convex_concave, udlr = udlr, lens_color = color, label = label)
                answer_colors.append(color_add[x_idx, y_idx])
            else:
                new_shape = Lens(other_type, udlr = udlr, lens_color = color, label = label)
            diagram.components.append(new_shape)
            option_list.append(color)
            diagram.colors.append(color)
    random.shuffle(option_list)
    diagram.entities.append(("convexity13", ["lens", convex_concave, "/".join(option_list), ", ".join(option_list), ", ".join(answer_colors)]))
    return diagram

rules = [
    convexity1,
    convexity2,
    convexity3,
    convexity4,
    convexity5,
    convexity6,
    convexity7,
    convexity8,
    convexity9,
    convexity10,
    convexity11,
    convexity12,
    convexity13
]