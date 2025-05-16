import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
import math
import shapely
from shapely.geometry import Polygon as ShapelyPolygon, MultiPolygon
import copy

point_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_labels = list("1234567890")
func_labels = list("abcdefghijklmnopqrstuvwxyz")
color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

class Triangle:
    def __init__(self, triangle_points, edgecolor, facecolor, label=None, alpha=1):
        self.points = triangle_points  # [(x1, y1), (x2, y2), (x3, y3)]
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
    
    def plot(self, ax, tc):
        ax.add_patch(self.patch)
    
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
        self.xy = xy  # (x, y)
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
    
    def plot(self, ax, tc):
        ax.add_patch(self.patch)
    
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
    
    def plot(self, ax, tc):
        ax.add_patch(self.patch)
    
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
    
    def plot(self, ax, tc):
        ax.add_patch(self.patch)
    
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
    
    def plot(self, ax, tc):
        ax.add_patch(self.patch)
    
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
    
    def plot(self, ax, tc):
        ax.add_patch(self.patch)
    
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

class Point:
    def __init__(self, x, y, label = "", color = "black"):
        self.x = x
        self.y = y
        self.label = label
        self.color = color
    
    def plot(self, ax, tc):
        ax.scatter(self.x, self.y, color = self.color)
        tc.append(self.x, self.y, self.label)


class Line:
    def __init__(self, point1, point2, label = None, color = "black"):
        self.points = [point1, point2]
        self.color = color
        self.show_label = False

        if label is not None:
            self.label = label
            self.show_label = True
        elif (point1.label != "") and (point2.label != ""):
            if random.randint(1, 2) == 1:
                self.label = point1.label + point2.label
            else:
                self.label = point2.label + point1.label
        else:
            self.label = ""
    
    def plot(self, ax, tc):
        x1 = self.points[0].x
        y1 = self.points[0].y
        x2 = self.points[1].x
        y2 = self.points[1].y
        x_mid = (x1 + x2) / 2
        y_mid = (y1 + y2) / 2
        ax.plot((x1, x2), (y1, y2), color=self.color)
        if self.show_label:
            tc.append(x_mid, y_mid, self.label)

class OneCell:
    def __init__(self, idx, label = None):
        self.idx = idx
        if label is None:
            self.label = str(self.idx)
        else:
            self.label = str(label)
        self.points = {"upper_left":None, "upper_right":None, "lower_left":None, "lower_right":None}
        self.lines = {"upper":None, "lower":None, "left":None, "right":None}
        self.neighbor_cells = {"upper":None, "lower":None, "left":None, "right":None}
        self.middle = None
    
    def update_point(self, point_info):
        self.points = point_info
        x_min = self.points["lower_left"].x
        y_min = self.points["lower_left"].y
        x_max = self.points["upper_right"].x
        y_max = self.points["upper_right"].y
        self.middle = ((x_min + x_max) / 2, (y_min + y_max) / 2)
    
    def update_lines(self, line_info):
        self.lines = line_info
    
    def share_side(self, place, cell_instance):
        if place in ["upper", "lower", "left", "right"]:
            self.neighbor_cells[place] = cell_instance
    
    def plot(self, ax, tc):
        if self.middle is not None:
            tc.append(self.middle[0], self.middle[1], self.label)

class Table:
    def __init__(self, color="black"):
        self.width = 0
        self.height = 0
        self.point_dict = {}
        self.cell_dict = {}
        self.line_dict = {}
        
        self.make_cell()
        self.generate_line_info(color)
        self.connect_cell_point_line()
        self.connect_cells()

    def make_cell(self):
        width = random.randint(2, 5)
        height = random.randint(2, 5)

        while (width + 1) * (height + 1) > 26:
            width = random.randint(2, 5)
            height = random.randint(2, 5)
        
        self.width = width
        self.height = height
        
        point_to_use = random.sample(point_labels, (width + 1) * (height + 1))
        point_color = random.choice(["none", "black"])
        idx = 0
        one_width = random.uniform(1, 10)
        one_height = random.uniform(1, 10)

        self.point_dict = {}
        self.cell_dict = {}

        for j in range(height, -1, -1):
            for i in range(width+1):
                new_point = Point(one_width*i, one_height*j, 
                                  label=point_to_use.pop(), 
                                  color=point_color)
                self.point_dict[(i, j)] = new_point
                if (j < height) and (i < width):
                    self.cell_dict[idx] = OneCell(idx)
                    idx += 1
    
    def generate_line_info(self, color):
        self.line_dict = {}
        if color == "random":
            for i in range(self.width):
                for j in range(self.height):
                    line_color = random.choice(color_list)
                    l1 = Line(self.point_dict[(i, j)], self.point_dict[(i, j+1)], color=line_color)
                    self.line_dict[((i, j), (i, j+1))] = l1

                    line_color = random.choice(color_list)
                    l2 = Line(self.point_dict[(i, j)], self.point_dict[(i+1, j)], color=line_color)
                    self.line_dict[((i, j), (i+1, j))] = l2

            j = self.height
            for i in range(self.width):
                line_color = random.choice(color_list)
                l2 = Line(self.point_dict[(i, j)], self.point_dict[(i+1, j)], color=line_color)
                self.line_dict[((i, j), (i+1, j))] = l2

            i = self.width
            for j in range(self.height):
                line_color = random.choice(color_list)
                l1 = Line(self.point_dict[(i, j)], self.point_dict[(i, j+1)], color=line_color)
                self.line_dict[((i, j), (i, j+1))] = l1
        else:
            line_color = color
            for i in range(self.width):
                for j in range(self.height):
                    l1 = Line(self.point_dict[(i, j)], self.point_dict[(i, j+1)], color=line_color)
                    self.line_dict[((i, j), (i, j+1))] = l1

                    l2 = Line(self.point_dict[(i, j)], self.point_dict[(i+1, j)], color=line_color)
                    self.line_dict[((i, j), (i+1, j))] = l2

            j = self.height
            for i in range(self.width):
                l2 = Line(self.point_dict[(i, j)], self.point_dict[(i+1, j)], color=line_color)
                self.line_dict[((i, j), (i+1, j))] = l2

            i = self.width
            for j in range(self.height):
                l1 = Line(self.point_dict[(i, j)], self.point_dict[(i, j+1)], color=line_color)
                self.line_dict[((i, j), (i, j+1))] = l1
    
    def connect_cell_point_line(self):
        idx = 0
        for j in range(self.height, -1, -1):
            for i in range(self.width+1):
                if (j < self.height) and (i < self.width):
                    area_point_dict = {
                        "upper_left": self.point_dict[(i, j+1)],
                        "upper_right": self.point_dict[(i+1, j+1)],
                        "lower_left": self.point_dict[(i, j)],
                        "lower_right": self.point_dict[(i+1, j)]
                    }
                    area_line_dict = {
                        "upper": self.line_dict[((i, j+1), (i+1, j+1))],
                        "lower": self.line_dict[((i, j), (i+1, j))],
                        "left": self.line_dict[((i, j), (i, j+1))],
                        "right": self.line_dict[((i+1, j), (i+1, j+1))]
                    }
                    self.cell_dict[idx].update_point(area_point_dict)
                    self.cell_dict[idx].update_lines(area_line_dict)
                    idx += 1

    def connect_cells(self):
        num_boxes = self.width * self.height
        for idx in range(num_boxes):
            if idx >= self.width:
                self.cell_dict[idx].share_side("upper", self.cell_dict[idx-self.width])
            if (num_boxes - 1 - idx) >= self.width:
                self.cell_dict[idx].share_side("lower", self.cell_dict[idx+self.width])
            if (idx % self.width != 0):
                self.cell_dict[idx].share_side("left", self.cell_dict[idx-1])
            if (idx % self.width != (self.width - 1)):
                self.cell_dict[idx].share_side("right", self.cell_dict[idx+1])

    def plot(self, ax, tc):
        for one_point in self.point_dict.values():
            one_point.plot(ax, tc)
        for one_line in self.line_dict.values():
            one_line.plot(ax, tc)
        for one_cell in self.cell_dict.values():
            one_cell.plot(ax, tc)

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
    shape_list = ["triangle", "rectangle", "parallelogram", "circle", "ellipse", "regular polygon"]
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


# ** 색 선이 정확하게 ** 색으로 칠해진 영역의 boundary가 되는가? (맞는 경우)
def boundary1(diagram):
    x = 100
    y = 0

    while not (-30<(x-y)<30):
        x = random.randint(2, 100)
        y = random.randint(2, 100)

    color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
    edgecolor = random.choice(color_list)
    facecolor = random.choice(color_list)

    r1 = Rectangle((0, 0), x, y, "none", facecolor, alpha = random.uniform(0.2, 0.5), angle = 0.0)
    r2 = Rectangle((0, 0), x, y, edgecolor, "none", alpha = random.uniform(0.8, 1), angle = 0)

    diagram.components.append(r1)
    diagram.components.append(r2)
    diagram.entities.append(("boundary1", ["rectangle", facecolor, edgecolor]))
    return diagram


#  ** 색 선이 정확하게 ** 색으로 칠해진 영역의 boundary가 되는가? (아닌 경우)
def boundary2(diagram):
    x = 100
    y = 0

    while not (-30<(x-y)<30):
        x = random.randint(2, 100)
        y = random.randint(2, 100)

    color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
    edgecolor = random.choice(color_list)
    facecolor = random.choice(color_list)

    r1 = Rectangle((0, 0), x, y, "none", facecolor, alpha = random.uniform(0.2, 0.5), angle = 0.0)
    r2 = Rectangle((random.uniform(-1, 1), random.uniform(-1, 1)), x+random.uniform(-1, 1), y+random.uniform(-1, 1), edgecolor, "none", alpha = random.uniform(0.8, 1), angle = random.randint(-5, 5))

    diagram.components.append(r1)
    diagram.components.append(r2)
    diagram.entities.append(("boundary2", ["rectangle", facecolor, edgecolor]))
    return diagram

# 내부와 색이 다른 boundary가 명시적으로 그려져있는가?
def boundary3(diagram):
    new_shape = generate_random_shape()

    new_shape.edgecolor = random.choice(color_list)
    new_shape.facecolor = random.choice(color_list)
    while new_shape.edgecolor == new_shape.facecolor:
        new_shape.facecolor = random.choice(color_list)
    new_shape.update_patch()

    diagram.components.append(new_shape)
    diagram.entities.append(("boundary3", [new_shape.shape_type, new_shape.facecolor, new_shape.edgecolor]))

    return diagram

# 내부와 색이 다른 boundary가 명시적으로 그려져있는가?
def boundary4(diagram):
    new_shape = generate_random_shape()

    new_shape.edgecolor = random.choice(color_list)
    new_shape.facecolor = new_shape.edgecolor
    new_shape.update_patch()

    diagram.components.append(new_shape)
    diagram.entities.append(("boundary4", [new_shape.shape_type, new_shape.facecolor, new_shape.edgecolor]))

    return diagram


# 영역 1과 영역 2의 경계가 되는 선의 이름은?
def boundary5(diagram):
    color = random.choice(["random", "random", "random", "black", "black"]+color_list)
    t = Table(color = color)
    area_list = list(map(str, list(t.cell_dict.keys())))
    line_list = [str(i.label) for i in t.line_dict.values()]
    one_cell = random.choice(t.cell_dict)
    area1 = one_cell.idx
    neighbor_list = [one_element for one_element in one_cell.neighbor_cells if one_cell.neighbor_cells[one_element] is not None]
    place_key = random.choice(neighbor_list)
    neighbor = one_cell.neighbor_cells[place_key]
    answer = one_cell.lines[place_key].label
    area2 = neighbor.idx
    diagram.components.append(t)
    diagram.entities.append(("boundary5", ["/".join(area_list), ", ".join(area_list), str(area1), str(area2), answer, ", ".join(line_list)]))
    return diagram


# 가장 바깥쪽 boundary의 색은?
def boundary6(diagram):
    num_shapes = random.randint(2, 6)
    trial = 0
    option_list = random.sample(color_list, num_shapes)

    while True:
        trial += 1
        shape_list = []
        color_to_use = copy.deepcopy(option_list)

        regulate = [(0, 1)] + sorted(random.sample([(i/100, 1-i/100) for i in range(5, 50, 5)], num_shapes-1))
        answer = ""

        for idx in range(num_shapes):
            if idx == 0:
                new_shape = generate_random_shape(edgecolor = "none", facecolor = color_to_use.pop())
                # new_shape.regulate((-100, -99), (-100, -99))
                answer = new_shape.facecolor
            else:
                new_shape = copy.deepcopy(new_shape)
                new_shape.facecolor = color_to_use.pop()
            r_min, r_max = regulate[idx]
            new_shape.regulate((r_min*100, r_max*100), (r_min*100, r_max*100))
            shape_list.append(new_shape)
        
        signal = True
        for idx1 in range(len(shape_list)):
            for idx2 in range(idx1+1, len(shape_list)):
                if "contains" not in check_relationship(shape_list[idx1].patch, shape_list[idx2].patch):
                    signal = False
        
        if signal:
            break

        if trial > 1000:
            raise
    
    diagram.components.extend(shape_list)
    diagram.entities.append(("boundary6", [new_shape.shape_type, "/".join(option_list), ", ".join(option_list), answer]))
    return diagram

rules = [
    boundary1,
    boundary2,
    boundary3,
    boundary4,
    boundary5,
    boundary6
]
