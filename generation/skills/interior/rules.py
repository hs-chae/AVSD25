import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
import math
import shapely
from shapely.geometry import Polygon as ShapelyPolygon, MultiPolygon
from shapely.geometry import Point as ShapelyPoint

point_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_labels = list("1234567890")
func_labels = list("abcdefghijklmnopqrstuvwxyz")
color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

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
    def __init__(self, xy, width, height, edgecolor, facecolor, label=None, alpha=1):
        self.xy = xy  # (x, y)
        self.width = width
        self.height = height
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha
        self.patch = patches.Rectangle(self.xy, self.width, self.height,
                                       edgecolor=self.edgecolor, facecolor=self.facecolor, 
                                       alpha=self.alpha, label=self.label)
        self.shape_type = "rectangle"

    def update_patch(self):
        self.patch = patches.Rectangle(self.xy, self.width, self.height,
                                       edgecolor=self.edgecolor, facecolor=self.facecolor, 
                                       alpha=self.alpha, label=self.label) 


    def plot(self, ax, tc, set_visible = True):
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
                                     facecolor=self.facecolor, alpha=self.alpha, label=self.label)

    def plot(self, ax, tc, set_visible = True):
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
            self.xy, self.numVertices, radius=self.radius,  # 위치, 꼭짓점 수, 반지름
            edgecolor=self.edgecolor,          # 선 색
            facecolor=self.facecolor,          # 채우기 색
            alpha=self.alpha,                  # 투명도
            label=self.label
        )
        self.shape_type = "regular polygon"
    
    def update_patch(self):
        self.patch = patches.RegularPolygon(
            self.xy, self.numVertices, radius=self.radius,  # 위치, 꼭짓점 수, 반지름
            edgecolor=self.edgecolor,          # 선 색
            facecolor=self.facecolor,          # 채우기 색
            alpha=self.alpha,                  # 투명도
            label=self.label
        )
    
    def plot(self, ax, tc, set_visible = True):
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
        
        # 스케일 조정 뒤 평행 이동
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

class ArbitraryPolygon:
    def __init__(self, num_points=5, x_range=(0,100), y_range=(0,100), color = None):
        self.points = []
        for _ in range(num_points):
            x = random.uniform(*x_range)
            y = random.uniform(*y_range)
            self.points.append((x, y))

        cx = sum(p[0] for p in self.points)/num_points
        cy = sum(p[1] for p in self.points)/num_points

        angles = [math.atan2(p[1]-cy, p[0]-cx) for p in self.points]
        sorted_points = [p for _, p in sorted(zip(angles, self.points), key=lambda x: x[0])]

        if color == None:
            self.color = random.choice(color_list)
        else:
            self.color = color
        
        self.patch = ShapelyPolygon(sorted_points)
        self.shape_type = "arbitrary polygon"
    
    def plot(self, ax, tc, set_visible = True):
        x, y = self.patch.exterior.xy
        line = ax.plot(x, y, color=self.color, linewidth=2)
        line[0].set_visible(set_visible)
        for hole in self.patch.interiors:
            hx, hy = hole.xy
            line = ax.plot(hx, hy, color=self.color, linewidth=2)
            line[0].set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        poly = self.patch

        minx, miny, maxx, maxy = poly.bounds
        shape_w = maxx - minx
        shape_h = maxy - miny
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)

        cx = (minx + maxx) / 2
        cy = (miny + maxy) / 2
        
        from shapely.affinity import scale, translate
        
        scaled_poly = scale(poly, xfact=scale_factor, yfact=scale_factor, origin=(cx, cy))
        
        minx, miny, maxx, maxy = scaled_poly.bounds
        
        shift_x = 0
        shift_y = 0
        if minx < xlim[0]:
            shift_x = xlim[0] - minx
        elif maxx > xlim[1]:
            shift_x = xlim[1] - maxx
        
        if miny < ylim[0]:
            shift_y = ylim[0] - miny
        elif maxy > ylim[1]:
            shift_y = ylim[1] - maxy
        
        regulated_poly = translate(scaled_poly, xoff=shift_x, yoff=shift_y)
        
        self.patch = regulated_poly

class Grid:
    def __init__(self, width, height, color='black', one_length=12, box_height=15):
        idx = 1
        self.width = width
        self.height = height
        self.color = color
        self.one_length = one_length
        self.box_height = box_height
        self.text_x = random.uniform(0.1, 2)
        self.text_y = one_length + random.uniform(0.4, 1) * ((self.box_height - self.one_length)/3)
        self.make_info_list()
        self.shape_type = "grid"
    
    def make_info_list(self):
        self.linelist = []
        self.pointdict = {}
        self.centerdict = {}
        self.textdict = {}
        idx = 1
        for j in range(self.height-1, -1, -1):
            for i in range(self.width):
                self.linelist.append(((self.one_length*i, self.one_length*i+self.one_length), (self.box_height*j, self.box_height*j)))
                self.linelist.append(((self.one_length*i, self.one_length*i+self.one_length), (self.box_height*j, self.box_height*j)))
                self.linelist.append(((self.one_length*i, self.one_length*i+self.one_length), (self.box_height*j+self.one_length, self.box_height*j+self.one_length)))
                self.linelist.append(((self.one_length*i, self.one_length*i+self.one_length), (self.box_height*j+self.box_height, self.box_height*j+self.box_height)))
                self.linelist.append(((self.one_length*i, self.one_length*i), (self.box_height*j, self.box_height*j+self.box_height)))
                self.linelist.append(((self.one_length*i+self.one_length, self.one_length*i+self.one_length), (self.box_height*j, self.box_height*j+self.box_height)))
                self.textdict[idx] = (self.one_length*i+self.text_x, self.box_height*j+self.text_y)
                self.pointdict[idx] = []
                self.pointdict[idx].append((self.one_length*i, self.box_height*j))
                self.pointdict[idx].append((self.one_length*(i+1), self.box_height*j))
                self.pointdict[idx].append((self.one_length*i, self.box_height*j+self.one_length))
                self.pointdict[idx].append((self.one_length*(i+1), self.box_height*j+self.one_length))
                self.pointdict[idx].append((self.one_length*i, self.box_height*(j+1)))
                self.pointdict[idx].append((self.one_length*(i+1), self.box_height*(j+1)))
                self.centerdict[idx] = (self.one_length*(i+0.5), self.box_height*j+self.one_length*0.5)
                idx += 1
    
    def plot(self, ax, tc, set_visible = True):
        for one_line in self.linelist:
            line = ax.plot(one_line[0], one_line[1], color=self.color)
            line[0].set_visible(set_visible)
        for idx in self.textdict:
            tc.append(self.textdict[idx][0], self.textdict[idx][1], f"Area {idx}")
        ax.axis('off')

class Point:
    def __init__(self, label, x, y, color='black', alpha=1, size=20):
        self.label = label
        self.x = x
        self.y = y
        self.color = color
        self.alpha = alpha
        self.size = size
        self.shape_type = "point"
    
    def plot(self, ax, tc, set_visible = True):
        ax.scatter(self.x, self.y, c=self.color, alpha=self.alpha, s=self.size).set_visible(set_visible)
        if self.label:
            tc.append(self.x, self.y, self.label, ha='right', va='bottom')

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

def to_shapely(obj):
    if isinstance(obj, shapely.geometry.base.BaseGeometry):
        return obj
    import matplotlib.patches as mpatches
    from matplotlib.path import Path

    if isinstance(obj, mpatches.Patch):
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
    
    if shape1 is None or shape2 is None:
        return "No intersection or containment"
    
    if shape1.contains(shape2):
        return "Patch1 contains Patch2"
    elif shape2.contains(shape1):
        return "Patch2 contains Patch1"
    elif shape1.intersects(shape2):
        return "Patch1 and Patch2 intersect"
    else:
        return "No intersection or containment"

def generate_random_shape(shape=None, edgecolor = None, facecolor = None, color = None, xlim=(0, 100), ylim=(0, 100), alpha = 1):
    shape_list = ["triangle", "rectangle", "parallelogram", "circle", "ellipse", "regular polygon", "arbitrary polygon"]
    if (shape == None) or (type(shape) != str) or (shape.lower() not in shape_list):
        shape = random.choice(shape_list)
    
    if (color != None):
        edgecolor = color
        facecolor = color
    
    else:
        if (edgecolor == None):
            edgecolor = random.choice(edgecolor_list)
        if (facecolor == None):
            facecolor = random.choice(facecolor_list)
    
    if shape == "triangle":
        x1, y1 = random.uniform(*xlim), random.uniform(*ylim)
        x2, y2 = x1 + random.uniform(10, 40), y1
        x3, y3 = x1 + random.uniform(10, 40), y1 + random.uniform(10, 40)
        points = [(x1, y1), (x2, y2), (x3, y3)]
        return Triangle(points, edgecolor, facecolor, alpha = alpha)
    
    elif shape == "rectangle":
        x, y = random.uniform(*xlim), random.uniform(*ylim)
        width, height = random.uniform(10, 50), random.uniform(10, 50)
        return Rectangle((x, y), width, height, edgecolor, facecolor, alpha = alpha)
    
    elif shape == "parallelogram":
        start_x, start_y = random.uniform(*xlim), random.uniform(*ylim)
        vector1 = np.array([random.uniform(10, 50), 0])
        vector2 = np.array([random.uniform(10, 50), random.uniform(10, 50)])
        return Parallelogram(np.array([start_x, start_y]), vector1, vector2, edgecolor, facecolor, alpha = alpha)
    
    elif shape == "circle":
        cx, cy = random.uniform(*xlim), random.uniform(*ylim)
        radius = random.uniform(5, 30)
        return Circle((cx, cy), radius, edgecolor, facecolor, alpha = alpha)
    
    elif shape == "ellipse":
        cx, cy = random.uniform(*xlim), random.uniform(*ylim)
        width, height = random.uniform(10, 50), random.uniform(10, 50)
        angle = random.uniform(0, 360)
        return Ellipse((cx, cy), width, height, edgecolor, facecolor, angle, alpha = alpha)
    
    elif shape == "regular polygon":
        cx, cy = random.uniform(*xlim), random.uniform(*ylim)
        num_vertices = random.randint(3, 8)
        radius = random.uniform(5, 30)
        orientation = random.uniform(0, 360)
        return RegularPolygon((cx, cy), num_vertices, radius, edgecolor, facecolor, orientation, alpha = alpha)
    
    else:  # "arbitrary polygon"
        num_points = random.randint(3, 10)
        return ArbitraryPolygon(num_points=num_points, x_range=xlim, y_range=ylim, color = edgecolor)

def check_point_inside_shape(shape, point):    
    if isinstance(point, Point):
        px, py = point.x, point.y
    else:
        px, py = point 
    
    shape_type = shape.shape_type.lower()
    
    if shape_type == "triangle":
        polygon = ShapelyPolygon(shape.points)
        return polygon.contains(ShapelyPoint(px, py))
    
    elif shape_type == "rectangle":
        x, y = shape.xy
        w, h = shape.width, shape.height
        rect_points = [
            (x,       y),
            (x + w,   y),
            (x + w,   y + h),
            (x,       y + h)
        ]
        polygon = ShapelyPolygon(rect_points)
        return polygon.contains(ShapelyPoint(px, py))
    
    elif shape_type == "parallelogram":
        polygon = ShapelyPolygon(shape.points)
        return polygon.contains(ShapelyPoint(px, py))

    elif shape_type == "circle":
        cx, cy = shape.xy
        r = shape.radius
        dist = ((px - cx)**2 + (py - cy)**2)**0.5
        return (dist <= r)
    
    elif shape_type == "ellipse":
        cx, cy = shape.xy
        w, h = shape.width, shape.height
        rx = w / 2.0
        ry = h / 2.0
        val = ((px - cx)**2) / (rx**2) + ((py - cy)**2) / (ry**2)
        return (val <= 1.0)
    
    elif shape_type == "regular polygon":
        import math
        cx, cy = shape.xy
        r = shape.radius
        num_v = shape.numVertices
        theta0 = shape.orientation 
        vertices = []
        for i in range(num_v):
            angle = theta0 + 2 * math.pi * i / num_v
            vx = cx + r * math.cos(angle)
            vy = cy + r * math.sin(angle)
            vertices.append((vx, vy))
        polygon = ShapelyPolygon(vertices)
        return polygon.contains(ShapelyPoint(px, py))
    
    elif shape_type == "arbitrary polygon":
        return shape.patch.contains(ShapelyPoint(px, py))
    
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")

def make_point_outside(shape_instance, label = "", color = "black", xlim = (0, 100), ylim = (0, 100)):
    check = True
    trial = 0
    limit = 10000
    while check:
        x = random.randint(xlim[0], xlim[1])
        y = random.randint(ylim[0], ylim[1])
        p = Point(label, x, y, color = color)
        check = check_point_inside_shape(shape_instance, p)
        trial += 1
        if trial > limit:
            raise
    return p

def make_point_inside(shape_instance, label = "", color = "black", xlim = (0, 100), ylim = (0, 100)):
    check = False
    trial = 0
    limit = 10000
    while not check:
        x = random.randint(xlim[0], xlim[1])
        y = random.randint(ylim[0], ylim[1])
        p = Point(label, x, y, color = color)
        check = check_point_inside_shape(shape_instance, p)
        trial += 1
        if trial > limit:
            raise
    return p


# 도형 ** 안에 있는 점(label)
def interior1(diagram):
    # one shape
    point_candidates = []
    answer_point = []

    shape = random.choice(["triangle", "rectangle", "parallelogram", "circle", "ellipse"])
    shape_main = generate_random_shape(shape = shape, alpha = random.uniform(0.1, 0.7))
    shape_main.regulate(sorted([random.choice((0, 70)), random.choice((30, 100))]), sorted([random.choice((0, 70)), random.choice((30, 100))]))
    diagram.components.append(shape_main)

    if random.randint(1, 2) == 1: 
        num_shapes = random.randint(1, 4)
        shape_list = ["triangle", "rectangle", "parallelogram", "circle", "ellipse"]
        shape_list.remove(shape_main.shape_type)
        for _ in range(num_shapes):
            new_shape_type = shape_list.pop()
            new_shape = generate_random_shape(shape = new_shape_type, alpha = random.uniform(0.1, 0.7))
            new_shape.regulate(sorted([random.choice((0, 70)), random.choice((30, 100))]), sorted([random.choice((0, 70)), random.choice((30, 100))]))
            diagram.components.append(new_shape)
    
    num_point_inside = random.choice([1, 1, 1, 1, 1, 1, 2, 3, 4, 5])
    num_point_outside = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    label_list = random.sample(point_labels, num_point_inside+num_point_outside)

    for _ in range(num_point_inside):
        new_label = label_list.pop()
        new_point = make_point_inside(shape_main, label = new_label, color = random.choice(color_list))
        diagram.components.append(new_point)
        diagram.labels.append(new_label)
        point_candidates.append(new_label)
        answer_point.append(new_label)

    for _ in range(num_point_outside):
        new_label = label_list.pop()
        new_point = make_point_outside(shape_main, label = new_label, color = random.choice(color_list))
        diagram.components.append(new_point)
        diagram.labels.append(new_label)
        point_candidates.append(new_label)
    
    random.shuffle(point_candidates)
        
    diagram.entities.append(("interior1", [shape, "/".join(point_candidates), ", ".join(point_candidates), ", ".join(answer_point)]))
    return diagram

# 도형 ** 밖에 있는 점(label)
def interior2(diagram):
    # one shape
    point_candidates = []
    answer_point = []

    shape = random.choice(["triangle", "rectangle", "parallelogram", "circle", "ellipse"])
    shape_main = generate_random_shape(shape = shape, alpha = random.uniform(0.1, 0.7))
    shape_main.regulate(sorted([random.choice((0, 70)), random.choice((30, 100))]), sorted([random.choice((0, 70)), random.choice((30, 100))]))
    diagram.components.append(shape_main)

    if random.randint(1, 2) == 1:
        num_shapes = random.randint(1, 4)
        shape_list = ["triangle", "rectangle", "parallelogram", "circle", "ellipse"]
        shape_list.remove(shape_main.shape_type)
        for _ in range(num_shapes):
            new_shape_type = shape_list.pop()
            new_shape = generate_random_shape(shape = new_shape_type, alpha = random.uniform(0.1, 0.7))
            new_shape.regulate(sorted([random.choice((0, 70)), random.choice((30, 100))]), sorted([random.choice((0, 70)), random.choice((30, 100))]))
            diagram.components.append(new_shape)
    
    num_point_outside = random.choice([1, 1, 1, 1, 1, 1, 2, 3, 4, 5])
    num_point_inside = random.choice([1, 2, 3, 4, 5])
    label_list = random.sample(point_labels, num_point_inside+num_point_outside)

    for _ in range(num_point_outside):
        new_label = label_list.pop()
        new_point = make_point_outside(shape_main, label = new_label, color = random.choice(color_list))
        diagram.components.append(new_point)
        diagram.labels.append(new_label)
        point_candidates.append(new_label)
        answer_point.append(new_label)

    for _ in range(num_point_inside):
        new_label = label_list.pop()
        new_point = make_point_inside(shape_main, label = new_label, color = random.choice(color_list))
        diagram.components.append(new_point)
        diagram.labels.append(new_label)
        point_candidates.append(new_label)
    
    random.shuffle(point_candidates)
        
    diagram.entities.append(("interior2", [shape, "/".join(point_candidates), ", ".join(point_candidates), ", ".join(answer_point)]))
    return diagram

def interior3(diagram):
    # one shape
    point_candidates = []
    answer_point = []

    shape = random.choice(["triangle", "rectangle", "parallelogram", "circle", "ellipse"])
    shape_main = generate_random_shape(shape = shape, alpha = random.uniform(0.1, 0.7))
    shape_main.regulate(sorted([random.choice((0, 70)), random.choice((30, 100))]), sorted([random.choice((0, 70)), random.choice((30, 100))]))
    diagram.components.append(shape_main)

    if random.randint(1, 2) == 1:
        num_shapes = random.randint(1, 4)
        shape_list = ["triangle", "rectangle", "parallelogram", "circle", "ellipse"]
        shape_list.remove(shape_main.shape_type)
        for _ in range(num_shapes):
            new_shape_type = shape_list.pop()
            new_shape = generate_random_shape(shape = new_shape_type, alpha = random.uniform(0.1, 0.7))
            new_shape.regulate(sorted([random.choice((0, 70)), random.choice((30, 100))]), sorted([random.choice((0, 70)), random.choice((30, 100))]))
            diagram.components.append(new_shape)
    
    num_point_inside = random.choice([1, 1, 1, 1, 1, 1, 2, 3, 4, 5])
    num_point_outside = random.choice([1, 2, 3, 4, 5])
    using_color_list = random.sample(color_list, num_point_inside+num_point_outside)

    for _ in range(num_point_inside):
        new_color = using_color_list.pop()
        new_point = make_point_inside(shape_main, color = new_color)
        diagram.components.append(new_point)
        diagram.colors.append(new_color)
        point_candidates.append(new_color)
        answer_point.append(new_color)

    for _ in range(num_point_outside):
        new_color = using_color_list.pop()
        new_point = make_point_outside(shape_main, color = new_color)
        diagram.components.append(new_point)
        diagram.colors.append(new_color)
        point_candidates.append(new_color)
    
    random.shuffle(point_candidates)
        
    diagram.entities.append(("interior3", [shape, "/".join(point_candidates), ", ".join(point_candidates), ", ".join(answer_point)]))
    return diagram

def interior4(diagram):
    point_candidates = []
    answer_point = []

    shape = random.choice(["triangle", "rectangle", "parallelogram", "circle", "ellipse"])
    shape_main = generate_random_shape(shape = shape, alpha = random.uniform(0.1, 0.7))
    shape_main.regulate(sorted([random.choice((0, 70)), random.choice((30, 100))]), sorted([random.choice((0, 70)), random.choice((30, 100))]))
    diagram.components.append(shape_main)

    if random.randint(1, 2) == 1:
        num_shapes = random.randint(1, 4)
        shape_list = ["triangle", "rectangle", "parallelogram", "circle", "ellipse"]
        shape_list.remove(shape_main.shape_type)
        for _ in range(num_shapes):
            new_shape_type = shape_list.pop()
            new_shape = generate_random_shape(shape = new_shape_type, alpha = random.uniform(0.1, 0.7))
            new_shape.regulate(sorted([random.choice((0, 70)), random.choice((30, 100))]), sorted([random.choice((0, 70)), random.choice((30, 100))]))
            diagram.components.append(new_shape)
    
    num_point_outside = random.choice([1, 1, 1, 1, 1, 1, 2, 3, 4, 5])
    num_point_inside = random.choice([1, 2, 3, 4, 5])
    using_color_list = random.sample(color_list, num_point_inside+num_point_outside)

    for _ in range(num_point_outside):
        new_color = using_color_list.pop()
        new_point = make_point_outside(shape_main, color = new_color)
        diagram.components.append(new_point)
        diagram.colors.append(new_color)
        point_candidates.append(new_color)
        answer_point.append(new_color)

    for _ in range(num_point_inside):
        new_color = using_color_list.pop()
        new_point = make_point_inside(shape_main, color = new_color)
        diagram.components.append(new_point)
        diagram.colors.append(new_color)
        point_candidates.append(new_color)
    
    random.shuffle(point_candidates)
        
    diagram.entities.append(("interior4", [shape, "/".join(point_candidates), ", ".join(point_candidates), ", ".join(answer_point)]))
    return diagram

unique_shapes = ["triangle", "rectangle", "parallelogram", "circle", "ellipse"]


def place_shape_inside(main_poly, candidate_type, xlim, ylim, max_try=10000):
    attempt = 0
    while attempt < max_try:
        new_shape = generate_random_shape(shape=candidate_type, alpha=random.uniform(0.1, 0.7))
        new_shape.regulate(xlim, ylim)

        candidate_poly = to_shapely(new_shape.patch)
        if main_poly.contains(candidate_poly):
            return new_shape
        attempt += 1

    return None


def place_shape_outside(main_poly, candidate_type, xlim, ylim, max_try=1000):
    attempt = 0
    while attempt < max_try:
        new_shape = generate_random_shape(shape=candidate_type, alpha=random.uniform(0.1, 0.7))
        new_shape.regulate(xlim, ylim)

        candidate_poly = to_shapely(new_shape.patch)
        if not main_poly.intersects(candidate_poly):
            return new_shape
        attempt += 1
    return None


def interior5(diagram):
    main_shape_type = random.choice(unique_shapes)
    shape_main = generate_random_shape(shape=main_shape_type, alpha=random.uniform(0.1, 0.7))
    
    xlim = (0, 60)
    ylim = (0, 60)
    shape_main.regulate(xlim, ylim)
    diagram.components.append(shape_main)
    
    main_poly = to_shapely(shape_main.patch)

    min_inside = random.randint(1, 2)  
    min_total  = random.randint(2, 4)   

    used_shapes = set([main_shape_type]) 
    final_list = []  

    shape_candidates = [s for s in unique_shapes if s not in used_shapes]
    random.shuffle(shape_candidates)

    inside_count = 0
    while inside_count < min_inside and shape_candidates:
        ctype = shape_candidates.pop()  
        placed = place_shape_inside(main_poly, ctype, xlim, ylim)
        if placed is not None:
            final_list.append((ctype, placed))
            used_shapes.add(ctype)
            inside_count += 1

    while len(final_list) < (min_total - inside_count) + inside_count and shape_candidates:
        ctype = shape_candidates.pop()
        new_shape = generate_random_shape(shape=ctype, alpha=random.uniform(0.1, 0.7))
        new_shape.regulate(xlim, ylim)
        final_list.append((ctype, new_shape))
        used_shapes.add(ctype)

    for ctype, obj in final_list:
        diagram.components.append(obj)

    inside_filtered = []
    for ctype, obj in final_list:
        if main_poly.contains(to_shapely(obj.patch)):
            inside_filtered.append(ctype)

    answer = ", ".join(inside_filtered) if inside_filtered else "Nothing"

    shape_candidates_out = [fs[0] for fs in final_list]  
    diagram.entities.append((
        "interior5",
        [
            main_shape_type,
            "/".join(shape_candidates_out),
            ", ".join(shape_candidates_out),
            answer
        ]
    ))
    return diagram


def interior6(diagram):
    main_shape_type = random.choice(unique_shapes)
    shape_main = generate_random_shape(shape=main_shape_type, alpha=random.uniform(0.1, 0.7))

    xlim = (0, 60)
    ylim = (0, 60)
    shape_main.regulate(xlim, ylim)
    diagram.components.append(shape_main)

    main_poly = to_shapely(shape_main.patch)

    min_outside = random.randint(1, 2)
    min_total   = random.randint(2, 4)

    used_shapes = set([main_shape_type])
    final_list = []

    shape_candidates = [s for s in unique_shapes if s not in used_shapes]
    random.shuffle(shape_candidates)

    outside_count = 0
    while outside_count < min_outside and shape_candidates:
        ctype = shape_candidates.pop()
        placed = place_shape_outside(main_poly, ctype, xlim, ylim)
        if placed is not None:
            final_list.append((ctype, placed))
            used_shapes.add(ctype)
            outside_count += 1

    while len(final_list) < min_total and shape_candidates:
        ctype = shape_candidates.pop()
        new_shape = generate_random_shape(shape=ctype, alpha=random.uniform(0.1, 0.7))
        new_shape.regulate(xlim, ylim)
        final_list.append((ctype, new_shape))
        used_shapes.add(ctype)

    for ctype, obj in final_list:
        diagram.components.append(obj)

    outside_filtered = []
    for ctype, obj in final_list:
        if not main_poly.intersects(to_shapely(obj.patch)):
            outside_filtered.append(ctype)

    answer = ", ".join(outside_filtered) if outside_filtered else "Nothing"

    shape_candidates_out = [fs[0] for fs in final_list]
    diagram.entities.append((
        "interior6",
        [
            main_shape_type,
            "/".join(shape_candidates_out),
            ", ".join(shape_candidates_out),
            answer
        ]
    ))
    return diagram


def place_shape_inside_color(main_poly, candidate_type, candidate_color, xlim, ylim, max_try=10000):
    attempt = 0
    while attempt < max_try:
        new_shape = generate_random_shape(
            shape=candidate_type,
            color=candidate_color,
            alpha=random.uniform(0.1, 0.7)
        )
        new_shape.regulate(xlim, ylim)
        if main_poly.contains(to_shapely(new_shape.patch)):
            return new_shape
        attempt += 1
    return None


def place_shape_outside_color(main_poly, candidate_type, candidate_color, xlim, ylim, max_try=1000):
    attempt = 0
    while attempt < max_try:
        new_shape = generate_random_shape(
            shape=candidate_type,
            color=candidate_color,
            alpha=random.uniform(0.1, 0.7)
        )
        new_shape.regulate(xlim, ylim)
        if not main_poly.intersects(to_shapely(new_shape.patch)):
            return new_shape
        attempt += 1
    return None


def interior7(diagram):
    shape_main_type = random.choice(unique_shapes)
    shape_main = generate_random_shape(shape=shape_main_type, alpha=random.uniform(0.1, 0.7))

    xlim = (0, 60)
    ylim = (0, 60)
    shape_main.regulate(xlim, ylim)
    diagram.components.append(shape_main)

    main_poly = to_shapely(shape_main.patch)

    min_inside = random.randint(1, 2)
    min_total  = random.randint(2, 4)

    final_list = []  
    inside_count = 0

    color_candidates = color_list[:]
    random.shuffle(color_candidates)

    while inside_count < min_inside and color_candidates:
        ccolor = color_candidates.pop()
        ctype  = random.choice(unique_shapes) 
        placed = place_shape_inside_color(main_poly, ctype, ccolor, xlim, ylim)
        if placed is not None:
            final_list.append((ccolor, placed))
            inside_count += 1

    while len(final_list) < min_total and color_candidates:
        ccolor = color_candidates.pop()
        ctype  = random.choice(unique_shapes)
        new_shape = generate_random_shape(shape=ctype, color=ccolor, alpha=random.uniform(0.1, 0.7))
        new_shape.regulate(xlim, ylim)
        final_list.append((ccolor, new_shape))

    for ccolor, obj in final_list:
        diagram.components.append(obj)

    inside_filtered = []
    for ccolor, obj in final_list:
        if main_poly.contains(to_shapely(obj.patch)):
            inside_filtered.append(ccolor)

    answer = ", ".join(inside_filtered) if inside_filtered else "Nothing"

    shape_candidates_out = [fs[0] for fs in final_list] 
    diagram.entities.append((
        "interior7",
        [
            shape_main_type,
            "/".join(shape_candidates_out),
            ", ".join(shape_candidates_out),
            answer
        ]
    ))
    return diagram


def interior8(diagram):
    shape_main_type = random.choice(unique_shapes)
    shape_main = generate_random_shape(shape=shape_main_type, alpha=random.uniform(0.1, 0.7))

    xlim = (0, 60)
    ylim = (0, 60)
    shape_main.regulate(xlim, ylim)
    diagram.components.append(shape_main)
    main_poly = to_shapely(shape_main.patch)

    min_outside = random.randint(1, 2)
    min_total   = random.randint(2, 4)

    final_list = []
    outside_count = 0

    color_candidates = color_list[:]
    random.shuffle(color_candidates)

    while outside_count < min_outside and color_candidates:
        ccolor = color_candidates.pop()
        ctype  = random.choice(unique_shapes)
        placed = place_shape_outside_color(main_poly, ctype, ccolor, xlim, ylim)
        if placed is not None:
            final_list.append((ccolor, placed))
            outside_count += 1

    while len(final_list) < min_total and color_candidates:
        ccolor = color_candidates.pop()
        ctype  = random.choice(unique_shapes)
        new_shape = generate_random_shape(shape=ctype, color=ccolor, alpha=random.uniform(0.1, 0.7))
        new_shape.regulate(xlim, ylim)
        final_list.append((ccolor, new_shape))

    for ccolor, obj in final_list:
        diagram.components.append(obj)

    outside_filtered = []
    for ccolor, obj in final_list:
        if not main_poly.intersects(to_shapely(obj.patch)):
            outside_filtered.append(ccolor)

    answer = ", ".join(outside_filtered) if outside_filtered else "Nothing"

    shape_candidates_out = [fs[0] for fs in final_list]
    diagram.entities.append((
        "interior8",
        [
            shape_main_type,
            "/".join(shape_candidates_out),
            ", ".join(shape_candidates_out),
            answer
        ]
    ))
    return diagram



# ** 번 영역에 있는 점(label)
def interior9(diagram):
    candidate = ["Nothing"]
    answer = []

    width = 0
    height = 0
    while width + height < 3:
        width = random.randint(1, 5)
        height = random.randint(1, 5)

    g = Grid( width, height)
    diagram.components.append(g)
    area_answer = random.randint(1, width*height)

    num_point = random.randint(0, 26)
    area_point_dict = {area:0 for area in range(1, width*height+1)}
    for _ in range(num_point):
        area = random.randint(1, width*height)
        area_point_dict[area] += 1

    label_list = random.sample(point_labels, num_point)

    for idx in range(1, width*height+1):
        x_min, y_min = g.pointdict[idx][0]
        x_max, y_max = g.pointdict[idx][3]
        x_margin = (x_max-x_min)/100
        y_margin = (y_max-y_min)/100
        while area_point_dict[idx] > 0:
            x = random.uniform(x_min+x_margin, x_max-x_margin)
            y = random.uniform(y_min+y_margin, y_max-y_margin)
            label = label_list.pop()
            p = Point(label, x, y, color = random.choice(color_list))
            diagram.components.append(p)
            area_point_dict[idx] -= 1
            candidate.append(label)
            if idx == area_answer:
                answer.append(label)

    if answer:
        diagram.entities.append(("interior9", [str(area_answer), "/".join(candidate), ", ".join(candidate), ", ".join(answer)]))
    else:
        diagram.entities.append(("interior9", [str(area_answer), "/".join(candidate), ", ".join(candidate), "Nothing"]))

    return diagram

# ** 번 영역에 있는 점(color)
def interior10(diagram):
    candidate = ["Nothing"]
    answer = []

    width = 0
    height = 0
    while width + height < 3:
        width = random.randint(1, 5)
        height = random.randint(1, 5)

    g = Grid( width, height)
    diagram.components.append(g)
    area_answer = random.randint(1, width*height)

    num_point = random.randint(0, 10)
    area_point_dict = {area:0 for area in range(1, width*height+1)}
    for _ in range(num_point):
        area = random.randint(1, width*height)
        area_point_dict[area] += 1

    using_color_list = random.sample(color_list, num_point)
    label_list = random.sample(point_labels, num_point)

    for idx in range(1, width*height+1):
        x_min, y_min = g.pointdict[idx][0]
        x_max, y_max = g.pointdict[idx][3]
        x_margin = (x_max-x_min)/100
        y_margin = (y_max-y_min)/100
        while area_point_dict[idx] > 0:
            x = random.uniform(x_min+x_margin, x_max-x_margin)
            y = random.uniform(y_min+y_margin, y_max-y_margin)
            color = using_color_list.pop()
            if random.randint(1, 2) == 1:
                label = ""
            else:
                label = label_list.pop()
            p = Point(label, x, y, color = color)
            diagram.components.append(p)
            area_point_dict[idx] -= 1
            candidate.append(color)
            if idx == area_answer:
                answer.append(color)

    if answer:
        diagram.entities.append(("interior10", [str(area_answer), "/".join(candidate), ", ".join(candidate), ", ".join(answer)]))
    else:
        diagram.entities.append(("interior10", [str(area_answer), "/".join(candidate), ", ".join(candidate), "Nothing"]))

    return diagram

# ** 번 영역에 있는 도형(type)
def interior11(diagram):
    candidate = ["Nothing"]
    answer = []

    width = 0
    height = 0
    while not (2 <= (width*height) <=5) :
        width = random.randint(1, 5)
        height = random.randint(1, 5)

    g = Grid( width, height)
    diagram.components.append(g)
    area_answer = random.randint(1, width*height)

    num_point = random.randint(1, width*height)
    area_point_dict = {area:0 for area in range(1, width*height+1)}
    for _ in range(num_point):
        while True:
            area = random.randint(1, width*height)
            if area_point_dict[area] == 0:
                area_point_dict[area] = 1
                break

    type_list = random.sample(["triangle", "rectangle", "parallelogram", "circle", "ellipse"], num_point)

    for idx in range(1, width*height+1):
        x_min, y_min = g.pointdict[idx][0]
        x_max, y_max = g.pointdict[idx][3]
        x_margin = (x_max-x_min)/50
        y_margin = (y_max-y_min)/50
        while area_point_dict[idx] > 0:
            x = random.uniform(x_min+x_margin, x_max-x_margin)
            y = random.uniform(y_min+y_margin, y_max-y_margin)
            shape_type = type_list.pop()
            
            p = generate_random_shape(shape = shape_type, alpha = random.uniform(0.1, 0.7))
            p.regulate((x_min+x_margin, x_max-x_margin), (y_min+y_margin, y_max-y_margin))

            diagram.components.append(p)
            area_point_dict[idx] -= 1
            candidate.append(shape_type)
            if idx == area_answer:
                answer.append(shape_type)

    if answer:
        diagram.entities.append(("interior11", [str(area_answer), "/".join(candidate), ", ".join(candidate), ", ".join(answer)]))
    else:
        diagram.entities.append(("interior11", [str(area_answer), "/".join(candidate), ", ".join(candidate), "Nothing"]))

    return diagram

# ** 번 영역에 있는 도형(color)
def interior12(diagram):
    candidate = ["Nothing"]
    answer = []

    width = 0
    height = 0
    while not (2 <= (width*height) <=5) :
        width = random.randint(1, 5)
        height = random.randint(1, 5)

    g = Grid( width, height)
    diagram.components.append(g)
    area_answer = random.randint(1, width*height)

    num_point = random.randint(1, width*height)
    area_point_dict = {area:0 for area in range(1, width*height+1)}
    for _ in range(num_point):
        while True:
            area = random.randint(1, width*height)
            if area_point_dict[area] == 0:
                area_point_dict[area] = 1
                break

    type_list = random.sample(["triangle", "rectangle", "parallelogram", "circle", "ellipse", "regular polygon", "arbitrary polygon"]*3, num_point)
    using_color_list = random.sample(color_list, num_point)

    for idx in range(1, width*height+1):
        x_min, y_min = g.pointdict[idx][0]
        x_max, y_max = g.pointdict[idx][3]
        x_margin = (x_max-x_min)/50
        y_margin = (y_max-y_min)/50
        while area_point_dict[idx] > 0:
            x = random.uniform(x_min+x_margin, x_max-x_margin)
            y = random.uniform(y_min+y_margin, y_max-y_margin)
            shape_type = type_list.pop()
            color = using_color_list.pop()
            p = generate_random_shape(shape = shape_type, alpha = random.uniform(0.1, 0.7), color = color)
            p.regulate((x_min+x_margin, x_max-x_margin), (y_min+y_margin, y_max-y_margin))

            diagram.components.append(p)
            area_point_dict[idx] -= 1
            candidate.append(color)
            if idx == area_answer:
                answer.append(color)

    if answer:
        diagram.entities.append(("interior12", [str(area_answer), "/".join(candidate), ", ".join(candidate), ", ".join(answer)]))
    else:
        diagram.entities.append(("interior12", [str(area_answer), "/".join(candidate), ", ".join(candidate), "Nothing"]))

    return diagram

rules = [
    interior1,
    interior2,
    interior3,
    interior4,
    interior5,
    interior6,
    interior7,
    interior8,
    interior9,
    interior10,
    interior11,
    interior12
]
