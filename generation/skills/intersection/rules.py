import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
import math
from matplotlib.path import Path
import shapely
from shapely.geometry import Polygon as ShapelyPolygon, MultiPolygon
import copy

point_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_labels = list("1234567890")
func_labels = list("abcdefghijklmnopqrstuvwxyz")
color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

def find_intersections(func1, func2, resolution=1000):
    x_min = max(min(func1.x), min(func2.x))
    x_max = min(max(func1.x), max(func2.x))
    
    x_values = np.linspace(x_min, x_max, resolution)

    y1 = np.interp(x_values, func1.x, func1.y)
    y2 = np.interp(x_values, func2.x, func2.y)

    differences = y1 - y2
    sign_changes = np.where(np.diff(np.sign(differences)))[0]
    
    return len(sign_changes)

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

    def create_polynomial_from_zeros(self, zeros):
        coefficients = [random.uniform(-5, 5)]
        for zero in zeros:
            coefficients = np.convolve(coefficients, [1, -zero]) 
        return coefficients

    def poly_function(self):
        num_zeros = random.randint(3, 6)
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
        line = ax.plot(self.x, self.y, color=self.line_color, linewidth=2)
        line[0].set_visible(set_visible)
    
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
        line = ax.plot(self.x, self.y, color=self.line_color, linewidth=2)
        line[0].set_visible(set_visible)
        
    def translation(self, diff, line_color):
        self.y = [i-diff for i in self.y]
        self.intercept = self.y[0] - self.slope * self.x[0]
        self.line_color = line_color

class Point:
    def __init__(self, x, y, label = "", color = "black"):
        self.x = x
        self.y = y
        self.label = label
        self.color = color
    
    def plot(self, ax, tc, set_visible = True):
        ax.scatter(self.x, self.y, color = self.color).set_visible(set_visible)
        tc.append(self.x, self.y, self.label)

def generate_segment_and_curve_with_min_intersections(min_intersections=2, max_tries=1000):
    for _ in range(max_tries):
        func1 = RandomLineSegment(-random.randint(3,10), random.randint(3,10), 
                                  line_color=random.choice(color_list))
        func2 = RandomCurve(-random.randint(3,10), random.randint(3,10), 
                            line_color=random.choice(color_list))
        count = find_intersections(func1, func2)
        if count >= min_intersections:
            return func1, func2
    return func1, func2

class Triangle:
    def __init__(self, triangle_points, edgecolor, facecolor, label=None, alpha=1):
        self.points = triangle_points
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha
        self.patch = patches.Polygon(self.points, closed=True, edgecolor=self.edgecolor,
                                     facecolor=self.facecolor, alpha=self.alpha, label=self.label)
        self.shape_type = "triangle"
    
    def update_patch(self):
        self.patch = patches.Polygon(self.points, closed=True, edgecolor=self.edgecolor,
                                     facecolor=self.facecolor, alpha=self.alpha, label=self.label)
    
    def plot(self, ax, tc, set_visible = True):
        self.update_patch()
        ax.add_patch(self.patch).set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        x_vals = [p[0] for p in self.points]
        y_vals = [p[1] for p in self.points]
        
        x_min, x_max = min(x_vals), max(x_vals)
        y_min, y_max = min(y_vals), max(y_vals)
        
        shape_w = x_max - x_min
        shape_h = y_max - y_min
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)
        
        cx = (x_min + x_max) / 2
        cy = (y_min + y_max) / 2
        
        scaled_points = []
        for (px, py) in self.points:
            scaled_x = cx + (px - cx)*scale_factor
            scaled_y = cy + (py - cy)*scale_factor
            scaled_points.append((scaled_x, scaled_y))
        
        x_vals = [p[0] for p in scaled_points]
        y_vals = [p[1] for p in scaled_points]
        x_min, x_max = min(x_vals), max(x_vals)
        y_min, y_max = min(y_vals), max(y_vals)
        
        shift_x = 0
        shift_y = 0
        if x_min < xlim[0]:
            shift_x = xlim[0] - x_min
        elif x_max > xlim[1]:
            shift_x = xlim[1] - x_max
        
        if y_min < ylim[0]:
            shift_y = ylim[0] - y_min
        elif y_max > ylim[1]:
            shift_y = ylim[1] - y_max
        
        regulated_points = [(p[0] + shift_x, p[1] + shift_y) for p in scaled_points]
        
        self.points = regulated_points
        self.patch = patches.Polygon(self.points, closed=True, 
                                     edgecolor=self.edgecolor,
                                     facecolor=self.facecolor, 
                                     alpha=self.alpha, 
                                     label=self.label)

class Rectangle:
    def __init__(self, xy, width, height, edgecolor, facecolor, label=None, alpha=1, angle = 0.0):
        self.xy = xy  
        self.width = width
        self.height = height
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha
        self.angle = angle
        self.patch = patches.Rectangle(self.xy, self.width, self.height,
                                       edgecolor=self.edgecolor, facecolor=self.facecolor, 
                                       alpha=self.alpha, label=self.label, angle = self.angle)
        self.shape_type = "rectangle"
    
    def update_patch(self):
        self.patch = patches.Rectangle(self.xy, self.width, self.height,
                                       edgecolor=self.edgecolor, facecolor=self.facecolor, 
                                       alpha=self.alpha, label=self.label, angle = self.angle)
    
    def plot(self, ax, tc, set_visible = True):
        self.update_patch()
        ax.add_patch(self.patch).set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        x_min = self.xy[0]
        y_min = self.xy[1]
        x_max = x_min + self.width
        y_max = y_min + self.height
        
        shape_w = self.width
        shape_h = self.height
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)
        

        cx = (x_min + x_max)/2
        cy = (y_min + y_max)/2
        
        new_w = shape_w * scale_factor
        new_h = shape_h * scale_factor
        
        new_x_min = cx - new_w/2
        new_x_max = cx + new_w/2
        new_y_min = cy - new_h/2
        new_y_max = cy + new_h/2
        
        shift_x = 0
        shift_y = 0
        if new_x_min < xlim[0]:
            shift_x = xlim[0] - new_x_min
        elif new_x_max > xlim[1]:
            shift_x = xlim[1] - new_x_max
        
        if new_y_min < ylim[0]:
            shift_y = ylim[0] - new_y_min
        elif new_y_max > ylim[1]:
            shift_y = ylim[1] - new_y_max
        
        regulated_x = new_x_min + shift_x
        regulated_y = new_y_min + shift_y
        
        self.xy = (regulated_x, regulated_y)
        self.width = new_w
        self.height = new_h
        
        self.patch = patches.Rectangle(self.xy, self.width, self.height,
                                       edgecolor=self.edgecolor,
                                       facecolor=self.facecolor,
                                       alpha=self.alpha,
                                       label=self.label)

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
        self.patch = patches.Polygon(self.points, closed=True, edgecolor=self.edgecolor,
                                     facecolor=self.facecolor, alpha=self.alpha, 
                                     label=self.label)
        self.shape_type = "parallelogram"
    
    def update_patch(self):
        self.patch = patches.Polygon(self.points, closed=True, edgecolor=self.edgecolor,
                                     facecolor=self.facecolor, alpha=self.alpha, 
                                     label=self.label)
    
    def plot(self, ax, tc, set_visible = True):
        self.update_patch()
        ax.add_patch(self.patch).set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        x_vals = [p[0] for p in self.points]
        y_vals = [p[1] for p in self.points]
        
        x_min, x_max = min(x_vals), max(x_vals)
        y_min, y_max = min(y_vals), max(y_vals)
        
        shape_w = x_max - x_min
        shape_h = y_max - y_min
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)
        
        cx = (x_min + x_max)/2
        cy = (y_min + y_max)/2
        
        scaled_points = []
        for (px, py) in self.points:
            sx = cx + (px - cx)*scale_factor
            sy = cy + (py - cy)*scale_factor
            scaled_points.append((sx, sy))
        
        x_vals = [p[0] for p in scaled_points]
        y_vals = [p[1] for p in scaled_points]
        
        x_min, x_max = min(x_vals), max(x_vals)
        y_min, y_max = min(y_vals), max(y_vals)
        
        shift_x, shift_y = 0, 0
        if x_min < xlim[0]:
            shift_x = xlim[0] - x_min
        elif x_max > xlim[1]:
            shift_x = xlim[1] - x_max
        
        if y_min < ylim[0]:
            shift_y = ylim[0] - y_min
        elif y_max > ylim[1]:
            shift_y = ylim[1] - y_max
        
        regulated_points = [(p[0] + shift_x, p[1] + shift_y) for p in scaled_points]
        
        self.points = np.array(regulated_points)
        self.patch = patches.Polygon(self.points, closed=True,
                                     edgecolor=self.edgecolor,
                                     facecolor=self.facecolor,
                                     alpha=self.alpha,
                                     label=self.label)


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
        ax.add_patch(self.patch).set_visible(set_visible)
    
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
        self.patch = patches.Ellipse(self.xy, self.width, self.height,
                                     edgecolor=self.edgecolor, facecolor=self.facecolor, 
                                     alpha=self.alpha, label=self.label)
        self.shape_type = "ellipse"
    
    def update_patch(self):
        self.patch = patches.Ellipse(self.xy, self.width, self.height,
                                     edgecolor=self.edgecolor, facecolor=self.facecolor, 
                                     alpha=self.alpha, label=self.label)
    
    def plot(self, ax, tc, set_visible = True):
        self.update_patch()
        ax.add_patch(self.patch).set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        cx, cy = self.xy
        w, h = self.width, self.height
        
        x_min = cx - w/2
        x_max = cx + w/2
        y_min = cy - h/2
        y_max = cy + h/2
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        shape_w = w
        shape_h = h
        
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)
        
        new_w = w * scale_factor
        new_h = h * scale_factor
        
        x_min = cx - new_w/2
        x_max = cx + new_w/2
        y_min = cy - new_h/2
        y_max = cy + new_h/2
        
        shift_x = 0
        shift_y = 0
        
        if x_min < xlim[0]:
            shift_x = xlim[0] - x_min
        elif x_max > xlim[1]:
            shift_x = xlim[1] - x_max
        
        if y_min < ylim[0]:
            shift_y = ylim[0] - y_min
        elif y_max > ylim[1]:
            shift_y = ylim[1] - y_max
        
        regulated_cx = cx + shift_x
        regulated_cy = cy + shift_y
        
        self.xy = (regulated_cx, regulated_cy)
        self.width = new_w
        self.height = new_h
        
        self.patch = patches.Ellipse(self.xy, self.width, self.height,
                                     edgecolor=self.edgecolor,
                                     facecolor=self.facecolor,
                                     alpha=self.alpha,
                                     label=self.label)

class RegularPolygon:
    def __init__(self, xy, numVertices, radius, edgecolor, facecolor, orientation=0, label=None, alpha=1):
        self.xy = xy  # (cx, cy)
        self.numVertices = numVertices
        self.radius = radius
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.orientation = orientation
        self.label = label
        self.alpha = alpha
        self.patch = patches.RegularPolygon(
            self.xy, self.numVertices, radius=self.radius,
            edgecolor=self.edgecolor,         
            facecolor=self.facecolor,        
            alpha=self.alpha,            
            label=self.label
        )
        self.shape_type = "regular polygon"
    
    def update_patch(self):
        self.patch = patches.RegularPolygon(
            self.xy, self.numVertices, radius=self.radius,  
            edgecolor=self.edgecolor,       
            facecolor=self.facecolor,      
            alpha=self.alpha,             
            label=self.label
        )
    
    def plot(self, ax, tc, set_visible = True):
        self.update_patch()
        ax.add_patch(self.patch).set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        cx, cy = self.xy
        r = self.radius
        
        x_min = cx - r
        x_max = cx + r
        y_min = cy - r
        y_max = cy + r
        
        shape_w = x_max - x_min
        shape_h = y_max - y_min
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)
        
        new_r = r * scale_factor
        
        x_min = cx - new_r
        x_max = cx + new_r
        y_min = cy - new_r
        y_max = cy + new_r
        
        shift_x, shift_y = 0, 0
        if x_min < xlim[0]:
            shift_x = xlim[0] - x_min
        elif x_max > xlim[1]:
            shift_x = xlim[1] - x_max
        
        if y_min < ylim[0]:
            shift_y = ylim[0] - y_min
        elif y_max > ylim[1]:
            shift_y = ylim[1] - y_max
        
        regulated_cx = cx + shift_x
        regulated_cy = cy + shift_y
        
        self.xy = (regulated_cx, regulated_cy)
        self.radius = new_r
        
        self.patch = patches.RegularPolygon(
            self.xy, 
            self.numVertices, 
            radius=self.radius,
            orientation=self.orientation,
            edgecolor=self.edgecolor,
            facecolor=self.facecolor,
            alpha=self.alpha,
            label=self.label
        )

def to_shapely(obj):
    if isinstance(obj, shapely.geometry.base.BaseGeometry):
        return obj

    if isinstance(obj, patches.Patch):
        path = obj.get_path()                
        transform = obj.get_patch_transform()
        path_in_data = transform.transform_path(path) 
        poly_verts_list = path_in_data.to_polygons()
        polygons = []
        for verts in poly_verts_list:
            if len(verts) >= 3: 
                polygons.append(ShapelyPolygon(verts))
        if len(polygons) == 1:
            return polygons[0]
        elif len(polygons) > 1:
            return MultiPolygon(polygons)
        else:
            return None

    raise TypeError(f"Unsupported object type: {type(obj)}")

def check_relationship(obj1, obj2):
    shape1 = to_shapely(obj1)
    shape2 = to_shapely(obj2)
    
    if shape1.intersects(shape2):
        return "Patch1 and Patch2 intersect"
    else:
        return "Patch1 and Patch2 does not intersect"

def generate_random_shape(shape=None, edgecolor = None, color = None, xlim=(0, 100), ylim=(0, 100), alpha = 1):
    shape_list = ["triangle", "rectangle", "parallelogram", "circle", "ellipse", "regular polygon"]
    if (shape == None) or (type(shape) != str) or (shape.lower() not in shape_list):
        shape = random.choice(shape_list)
    
    if (color != None):
        edgecolor = color
    
    else:
        if (edgecolor == None):
            edgecolor = random.choice(edgecolor_list)
    
    facecolor = "none"
    
    if shape == "triangle":
        x1, y1 = random.uniform(*xlim), random.uniform(*ylim)
        x2, y2 = x1 + random.uniform(10, 80), y1
        x3, y3 = x1 + random.uniform(10, 80), y1 + random.uniform(10, 80)
        points = [(x1, y1), (x2, y2), (x3, y3)]
        return Triangle(points, edgecolor, facecolor, alpha = alpha)
    
    elif shape == "rectangle":
        x, y = random.uniform(*xlim), random.uniform(*ylim)
        width, height = random.uniform(10, 80), random.uniform(10, 80)
        return Rectangle((x, y), width, height, edgecolor, facecolor, alpha = alpha)
    
    elif shape == "parallelogram":
        start_x, start_y = random.uniform(*xlim), random.uniform(*ylim)
        vector1 = np.array([random.uniform(10, 80), 0])
        vector2 = np.array([random.uniform(10, 80), random.uniform(10, 80)])
        return Parallelogram(np.array([start_x, start_y]), vector1, vector2, edgecolor, facecolor, alpha = alpha)
    
    elif shape == "circle":
        cx, cy = random.uniform(*xlim), random.uniform(*ylim)
        radius = random.uniform(5, 50)
        return Circle((cx, cy), radius, edgecolor, facecolor, alpha = alpha)
    
    elif shape == "ellipse":
        cx, cy = random.uniform(*xlim), random.uniform(*ylim)
        width, height = random.uniform(10, 80), random.uniform(10, 80)
        angle = random.uniform(0, 360)
        return Ellipse((cx, cy), width, height, edgecolor, facecolor, angle, alpha = alpha)
    
    else:
        cx, cy = random.uniform(*xlim), random.uniform(*ylim)
        num_vertices = random.randint(3, 8)
        radius = random.uniform(5, 50)
        orientation = random.uniform(0, 360)
        return RegularPolygon((cx, cy), num_vertices, radius, edgecolor, facecolor, orientation, alpha = alpha)

class Diagram:
    def __init__(self,components = None,entities=None,background_color='white',labels=None,colors=None):
        self.components = components if components is not None else []
        self.entities = entities if entities is not None else []
        self.background_color = background_color
        self.labels = labels if labels is not None else []
        self.colors = colors if colors is not None else []

# 유형 설명 : 두 선이 만나는가? (만난다, label)
def intersection1_2(diagram):
    if random.randint(1, 2) == 1:
        func1 = RandomLineSegment(-random.randint(3, 10), random.randint(3, 10), line_color = random.choice(color_list))
        type1 = "line segment"
    else:
        func1 = RandomCurve(-random.randint(3, 10), random.randint(3, 10), line_color = random.choice(color_list))
        type1 = "curve"

    if random.randint(1, 2) == 1:
        func2 = RandomLineSegment(-random.randint(3, 10), random.randint(3, 10), line_color = random.choice(color_list))
        type2 = "line segment"
    else:
        func2 = RandomCurve(-random.randint(3, 10), random.randint(3, 10), line_color = random.choice(color_list))
        type2 = "curve"
    
    label11, label12, label21, label22 = random.sample(point_labels, 4)

    if random.randint(1, 2) == 1:
        p1 = Point(func1.x[0], func1.y[0], label = label11)
        p2 = Point(func1.x[-1], func1.y[-1], label = label12)
    else:
        p1 = Point(func1.x[0], func1.y[0], label = label12)
        p2 = Point(func1.x[-1], func1.y[-1], label = label11)
    if random.randint(1, 2) == 1:
        p3 = Point(func2.x[0], func2.y[0], label = label21)
        p4 = Point(func2.x[-1], func2.y[-1], label = label22)
    else:
        p3 = Point(func2.x[0], func2.y[0], label = label22)
        p4 = Point(func2.x[-1], func2.y[-1], label = label21)

    components = [func1, func2, p1, p2, p3, p4]
    
    if find_intersections(func1, func2) == 0:
        entities = ("intersection2", [type1, label11, label12, type2, label21, label22])
    else:
        entities = ("intersection1", [type1, label11, label12, type2, label21, label22])

    diagram.components.extend(components)
    diagram.entities.append(entities)
    return diagram


# 유형 설명 : 두 선이 만나는가? (만나면 intersection3, 안 만나면 intersection4, color)
def intersection3_4(diagram):
    random_colors = random.sample(color_list, 2)
    if random.randint(1, 2) == 1:
        func1 = RandomLineSegment(-random.randint(3, 10), random.randint(3, 10), line_color = random_colors[0])
        type1 = "line segment"
    else:
        func1 = RandomCurve(-random.randint(3, 10), random.randint(3, 10), line_color = random_colors[0])
        type1 = "curve"

    if random.randint(1, 2) == 1:
        func2 = RandomLineSegment(-random.randint(3, 10), random.randint(3, 10), line_color = random_colors[1])
        type2 = "line segment"
    else:
        func2 = RandomCurve(-random.randint(3, 10), random.randint(3, 10), line_color = random_colors[1])
        type2 = "curve"
    
    if random.randint(1, 2) == 1:
        components = [func1, func2]
    else:
        label11, label12, label21, label22 = random.sample(point_labels, 4)

        if random.randint(1, 2) == 1:
            p1 = Point(func1.x[0], func1.y[0], label = label11)
            p2 = Point(func1.x[-1], func1.y[-1], label = label12)
        else:
            p1 = Point(func1.x[0], func1.y[0], label = label12)
            p2 = Point(func1.x[-1], func1.y[-1], label = label11)
        if random.randint(1, 2) == 1:
            p3 = Point(func2.x[0], func2.y[0], label = label21)
            p4 = Point(func2.x[-1], func2.y[-1], label = label22)
        else:
            p3 = Point(func2.x[0], func2.y[0], label = label22)
            p4 = Point(func2.x[-1], func2.y[-1], label = label21)

        components = [func1, func2, p1, p2, p3, p4]

    if find_intersections(func1, func2) == 0:
        entities = ("intersection4", [type1, random_colors[0], type2, random_colors[1]])
    else:
        entities = ("intersection3", [type1, random_colors[0], type2, random_colors[1]])

    diagram.components.extend(components)
    diagram.entities.append(entities)
    return diagram

# 유형 설명 : 두 선의 교점의 개수는?(label)
def intersection5(diagram):
    func1, func2 = generate_segment_and_curve_with_min_intersections(min_intersections=random.randint(2, 5))
    type1 = func1.type_str
    type2 = func2.type_str

    label11, label12, label21, label22 = random.sample(point_labels, 4)

    if random.randint(1, 2) == 1:
        p1 = Point(func1.x[0], func1.y[0], label = label11)
        p2 = Point(func1.x[-1], func1.y[-1], label = label12)
    else:
        p1 = Point(func1.x[0], func1.y[0], label = label12)
        p2 = Point(func1.x[-1], func1.y[-1], label = label11)
    if random.randint(1, 2) == 1:
        p3 = Point(func2.x[0], func2.y[0], label = label21)
        p4 = Point(func2.x[-1], func2.y[-1], label = label22)
    else:
        p3 = Point(func2.x[0], func2.y[0], label = label22)
        p4 = Point(func2.x[-1], func2.y[-1], label = label21)

    components = [func1, func2, p1, p2, p3, p4]

    answer = find_intersections(func1, func2)

    while True:
        min_option = random.randint(0, answer)
        max_option = random.randint(answer, 15)
        if min_option < max_option:
            break
    options = [str(i) for i in range(min_option, max_option)]
    
    option_slash = "/".join(options)
    option_comma = ", ".join(options)
    entities = ("intersection5", [type1, label11, label12, type2, label21, label22, str(answer), option_slash, option_comma])

    diagram.components.extend(components)
    diagram.entities.append(entities)
    return diagram


# 유형 설명 : 두 선의 교점의 개수는?(color)
def intersection6(diagram):
    func1, func2 = generate_segment_and_curve_with_min_intersections(min_intersections=random.randint(2, 5))
    type1 = func1.type_str
    type2 = func2.type_str

    color1, color2 = random.sample(color_list, 2)
    func1.line_color = color1
    func2.line_color = color2

    if random.randint(1, 2) == 1:
        components = [func1, func2]
    else:
        label11, label12, label21, label22 = random.sample(point_labels, 4)

        if random.randint(1, 2) == 1:
            p1 = Point(func1.x[0], func1.y[0], label = label11)
            p2 = Point(func1.x[-1], func1.y[-1], label = label12)
        else:
            p1 = Point(func1.x[0], func1.y[0], label = label12)
            p2 = Point(func1.x[-1], func1.y[-1], label = label11)
        if random.randint(1, 2) == 1:
            p3 = Point(func2.x[0], func2.y[0], label = label21)
            p4 = Point(func2.x[-1], func2.y[-1], label = label22)
        else:
            p3 = Point(func2.x[0], func2.y[0], label = label22)
            p4 = Point(func2.x[-1], func2.y[-1], label = label21)

        components = [func1, func2, p1, p2, p3, p4]

    answer = find_intersections(func1, func2)

    while True:
        min_option = random.randint(0, answer)
        max_option = random.randint(answer, 15)
        if min_option < max_option:
            break

    options = [str(i) for i in range(min_option, max_option)]
    
    option_slash = "/".join(options)
    option_comma = ", ".join(options)
    entities = ("intersection6", [type1, color1, type2, color2, str(answer), option_slash, option_comma])

    diagram.components.extend(components)
    diagram.entities.append(entities)
    return diagram


# 유형 설명 : 곡선 하나 주고, 수평선으로 선분 여러개 준 다음에, 곡선과 교점의 개수가 가장 많은 선분 고르기
def intersection7(diagram):
    num_lines = random.randint(3, 9)
    add_list = sorted(random.sample([i for i in range(-5, 10)], num_lines))
    new_color_list = random.sample(color_list, num_lines+1)

    max_count = 5
    criteria = random.choice([1, 1, 1, 1, 1, 2, 2, 2, 3])

    while True:
        func1 = RandomLineSegment(-random.randint(3, 10), random.randint(3, 10), line_color = random.choice(color_list))
        func_list = []

        for idx in range(num_lines):
            func2 = copy.deepcopy(func1)
            func2.translation(add_list[idx], new_color_list[idx])
            func_list.append(func2)

        curve = RandomCurve(-random.randint(3, 10), random.randint(3, 10), line_color = new_color_list[-1])

        max_count = 0
        max_val = -1
        max_color_list = []
        for one_func in func_list:
            intersection_count = find_intersections(one_func, curve)
            if max_val < intersection_count:
                max_val = intersection_count
                max_count = 1
                max_color_list = [one_func.line_color]
            elif max_val == intersection_count:
                max_count += 1
                max_color_list.append(one_func.line_color)
        if max_count <= criteria:
            break

    curve_color = new_color_list[-1]
    line_color = new_color_list[:-1]
    random.shuffle(line_color)
    option_slash = "/".join(line_color)
    option_comma = ", ".join(line_color)
    answer = ", ".join(max_color_list)
    entities = ("intersection7", [curve_color, option_slash, option_comma, answer])
    diagram.components.extend(func_list)
    diagram.components.append(curve)
    diagram.entities.append(entities)
    return diagram


# 유형 설명 : 다른 색 선 or 유일하게 곡선인 선 l 하나 주고, 평행한 선분 여러개 준 다음에, 선 l과 만나는 선분의 개수 구하기
def intersection8(diagram):
    num_lines = random.randint(3, 9)
    add_list = sorted(random.sample([i for i in range(-5, 10)], num_lines))
    new_color_list = random.sample(color_list, num_lines+1)

    func1 = RandomLineSegment(-random.randint(3, 10), random.randint(3, 10), line_color = random.choice(color_list))
    func_list = []

    for idx in range(num_lines):
        func2 = copy.deepcopy(func1)
        func2.translation(add_list[idx], new_color_list[idx])
        func_list.append(func2)

    curve = RandomCurve(-random.randint(3, 10), random.randint(3, 10), line_color = new_color_list[-1])

    answer = 0
    for one_func in func_list:
        intersection_count = find_intersections(one_func, curve)
        if intersection_count > 0:
            answer += 1

    curve_color = new_color_list[-1]
    line_color = new_color_list[:-1]
    random.shuffle(line_color)
    option_slash = "/".join(line_color)
    option_comma = ", ".join(line_color)
    answer = str(answer)
    entities = ("intersection8", [curve_color, option_slash, option_comma, answer])
    diagram.components.extend(func_list)
    diagram.components.append(curve)
    diagram.entities.append(entities)
    return diagram


# 유형 설명 : 직선 하나 주고, 곡선 여러개 준 다음에, 직선과 교점의 개수가 가장 많은 곡선 고르기
def intersection9(diagram):
    num_lines = random.randint(3, 9)
    add_list = sorted(random.sample([i for i in range(-5, 10)], num_lines))
    new_color_list = random.sample(color_list, num_lines+1)

    max_count = 5
    criteria = random.choice([1, 1, 1, 1, 1, 2, 2, 2, 3])

    while True:
        func1 = RandomCurve(-random.randint(3, 10), random.randint(3, 10), line_color = random.choice(color_list))
        func_list = []

        for idx in range(num_lines):
            func2 = copy.deepcopy(func1)
            func2.translation(add_list[idx], new_color_list[idx])
            func_list.append(func2)

        curve = RandomLineSegment(-random.randint(3, 10), random.randint(3, 10), line_color = new_color_list[-1])

        max_count = 0
        max_val = -1
        max_color_list = []
        for one_func in func_list:
            intersection_count = find_intersections(one_func, curve)
            if max_val < intersection_count:
                max_val = intersection_count
                max_count = 1
                max_color_list = [one_func.line_color]
            elif max_val == intersection_count:
                max_count += 1
                max_color_list.append(one_func.line_color)
        if max_count <= criteria:
            break

    curve_color = new_color_list[-1]
    line_color = new_color_list[:-1]
    random.shuffle(line_color)
    option_slash = "/".join(line_color)
    option_comma = ", ".join(line_color)
    answer = ", ".join(max_color_list)
    entities = ("intersection9", [curve_color, option_slash, option_comma, answer])
    diagram.components.extend(func_list)
    diagram.components.append(curve)
    diagram.entities.append(entities)
    # diagram.components.append()
    # diagram.entities.append(("intersection9", [line_color, option_slash, option_comma, answer]))
    return diagram


# 유형 설명 : 다른 색 선 or 유일하게 straight line인 선 l 하나 주고, 평행한 곡선 여러개 준 다음에, 선 l과 만나는 곡선의 개수 구하기
def intersection10(diagram):
    num_lines = random.randint(3, 9)
    add_list = sorted(random.sample([i for i in range(-5, 10)], num_lines))
    new_color_list = random.sample(color_list, num_lines+1)

    func1 = RandomCurve(-random.randint(3, 10), random.randint(3, 10), line_color = random.choice(color_list))
    func_list = []

    for idx in range(num_lines):
        func2 = copy.deepcopy(func1)
        func2.translation(add_list[idx], new_color_list[idx])
        func_list.append(func2)

    curve = RandomLineSegment(-random.randint(3, 10), random.randint(3, 10), line_color = new_color_list[-1])

    answer = 0
    for one_func in func_list:
        intersection_count = find_intersections(one_func, curve)
        if intersection_count > 0:
            answer += 1

    curve_color = new_color_list[-1]
    line_color = new_color_list[:-1]
    random.shuffle(line_color)
    option_slash = "/".join(line_color)
    option_comma = ", ".join(line_color)
    answer = str(answer)
    entities = ("intersection10", [curve_color, option_slash, option_comma, answer])
    diagram.components.extend(func_list)
    diagram.components.append(curve)
    diagram.entities.append(entities)
    # diagram.components.append()
    # diagram.entities.append(("intersection10", [line_color, option_slash, option_comma, answer]))
    return diagram


# 유형 설명 : 두 도형의 boundary가 만나는가? (만나면 intersection11, 안 만나면 intersection12)
def intersection11_12(diagram):
    shape1 = generate_random_shape()
    shape2 = generate_random_shape()
    components = [shape1, shape2]

    if check_relationship(shape1.patch, shape2.patch) == "Patch1 and Patch2 intersect":
        entities = ("intersection11", [])
    else:
        entities = ("intersection12", [])

    diagram.components.extend(components)
    diagram.entities.append(entities)
    return diagram


# 유형 설명 : 두 도형의 boundary의 교점의 개수
def intersection13(diagram, max_tries=100):
    for _ in range(max_tries):
        shape1 = generate_random_shape()
        shape2 = generate_random_shape()

        shapely1 = to_shapely(shape1.patch)  
        shapely2 = to_shapely(shape2.patch)

        b1 = shapely1.boundary
        b2 = shapely2.boundary
        inter = b1.intersection(b2)

        if inter.is_empty:
            num_points = 0
        else:
            all_points = []
            skip_case = False

            def collect_points(geom):
                nonlocal skip_case
                if geom.is_empty:
                    return
                if geom.geom_type == 'Point':
                    all_points.append(geom)
                elif geom.geom_type == 'MultiPoint':
                    for g in geom.geoms:
                        all_points.append(g)
                elif geom.geom_type in ('LineString', 'LinearRing', 'Polygon'):
                    skip_case = True
                elif geom.geom_type in ('MultiLineString', 'MultiPolygon', 'GeometryCollection'):
                    for g2 in geom.geoms:
                        collect_points(g2)
                else:
                    skip_case = True

            collect_points(inter)

            if skip_case:
                continue

            unique_coords = set((round(pt.x, 7), round(pt.y, 7)) for pt in all_points)
            num_points = len(unique_coords)

        answer = num_points
        if answer == 0:
            continue
        for _2 in range(100):
            min_option = random.randint(0, answer)
            max_option = random.randint(answer, answer + 8) 
            if min_option < max_option:
                break
        options = list(range(min_option, max_option))
        options_str = [str(opt) for opt in options]
        option_slash = "/".join(options_str)
        option_comma = ", ".join(options_str)

        diagram.components.extend([shape1, shape2])
        diagram.entities.append(
            ("intersection13", [str(answer), option_slash, option_comma])
        )

        return diagram

    shape1 = generate_random_shape()
    shape2 = generate_random_shape()
    diagram.components.extend([shape1, shape2])
    random_choice = random.randint(2, 5)
    if random_choice == 2:
        diagram.entities.append(("intersection13", ["0", "0/1/2", "0, 1, 2"]))
    elif random_choice == 3:
        diagram.entities.append(("intersection13", ["0", "0/1/2/3", "0, 1, 2, 3"]))
    elif random_choice == 4:
        diagram.entities.append(("intersection13", ["0", "0/1/2/3/4", "0, 1, 2, 3, 4"]))
    else:
        diagram.entities.append(("intersection13", ["0", "0/1/2/3/4/5", "0, 1, 2, 3, 4, 5"]))
    return diagram


rules = [
    intersection1_2,
    intersection3_4,
    intersection5,
    intersection6,
    intersection7,
    intersection8,
    intersection9,
    intersection10,
    intersection11_12,
    intersection13
]