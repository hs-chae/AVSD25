import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import math
import shapely
from shapely.geometry import Polygon as ShapelyPolygon, MultiPolygon
import copy

from matplotlib import patheffects
def withStroke(**kwargs):
    return patheffects.Stroke(**kwargs)

# If you have a custom fontsize() function, define it here or replace with a constant
def fontsize():
    return 12

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
    
    def plot(self, idx, ax, tc, set_visible=True):
        patch = ax[idx].add_patch(self.patch)
        patch.set_visible(set_visible)
    
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
            sx = cx + (px - cx)*scale_factor
            sy = cy + (py - cy)*scale_factor
            scaled_points.append((sx, sy))
        
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
        self.update_patch()

    def rotation(self, angle, center=None):
        if center is None:
            x_vals = [p[0] for p in self.points]
            y_vals = [p[1] for p in self.points]
            cx = sum(x_vals) / 3
            cy = sum(y_vals) / 3
        else:
            cx, cy = center
        
        rad = math.radians(angle)
        
        rotated_points = []
        for (px, py) in self.points:
            tx = px - cx
            ty = py - cy
            rx = tx * math.cos(rad) - ty * math.sin(rad)
            ry = tx * math.sin(rad) + ty * math.cos(rad)
            rotated_points.append((rx + cx, ry + cy))
        
        self.points = rotated_points
        self.update_patch()
    
    def translation(self, movement_x, movement_y):
        translated_points = []
        for (px, py) in self.points:
            translated_points.append((px + movement_x, py + movement_y))
        
        self.points = translated_points
        self.update_patch()

    def flip(self):
        flip_dir = random.choice(["horizontal", "vertical"])
        
        x_vals = [p[0] for p in self.points]
        y_vals = [p[1] for p in self.points]
        x_min, x_max = min(x_vals), max(x_vals)
        y_min, y_max = min(y_vals), max(y_vals)
        
        cx = (x_min + x_max) / 2
        cy = (y_min + y_max) / 2
        
        flipped_points = []
        for (px, py) in self.points:
            if flip_dir == "horizontal":
                new_py = 2*cy - py
                flipped_points.append((px, new_py))
            else:
                new_px = 2*cx - px
                flipped_points.append((new_px, py))
        
        self.points = flipped_points
        self.update_patch()


class Rectangle:
    def __init__(self, xy, width, height, edgecolor, facecolor, label=None, alpha=1, angle=0.0):
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
                                       alpha=self.alpha, label=self.label, angle=self.angle)
        self.shape_type = "rectangle"
    
    def update_patch(self):
        self.patch = patches.Rectangle(self.xy, self.width, self.height,
                                       edgecolor=self.edgecolor, facecolor=self.facecolor,
                                       alpha=self.alpha, label=self.label, angle=self.angle)
    
    def plot(self, idx, ax, tc, set_visible=True):
        patch = ax[idx].add_patch(self.patch)
        patch.set_visible(set_visible)
    
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
        
        self.update_patch()
    
    def rotation(self, angle, center=None):
        if center is None:
            self.angle += angle
        else:
            x0, y0 = self.xy
            corners = [
                (x0,              y0),
                (x0 + self.width, y0),
                (x0 + self.width, y0 + self.height),
                (x0,              y0 + self.height),
            ]
            cx, cy = center
            rad = math.radians(angle)
            rotated_corners = []
            for (px, py) in corners:
                tx = px - cx
                ty = py - cy
                rx = tx * math.cos(rad) - ty * math.sin(rad)
                ry = tx * math.sin(rad) + ty * math.cos(rad)
                rotated_corners.append((rx + cx, ry + cy))
            
            xs = [c[0] for c in rotated_corners]
            ys = [c[1] for c in rotated_corners]
            new_x_min, new_x_max = min(xs), max(xs)
            new_y_min, new_y_max = min(ys), max(ys)
            
            self.xy = (new_x_min, new_y_min)
            self.width = (new_x_max - new_x_min)
            self.height = (new_y_max - new_y_min)
            self.angle = 0
        
        self.update_patch()
    
    def translation(self, movement_x, movement_y):
        x0, y0 = self.xy
        self.xy = (x0 + movement_x, y0 + movement_y)
        self.update_patch()

    def flip(self):
        flip_dir = random.choice(["horizontal", "vertical"])
        
        x0, y0 = self.xy
        corners = [
            (x0,              y0),
            (x0 + self.width, y0),
            (x0 + self.width, y0 + self.height),
            (x0,              y0 + self.height),
        ]
        
        xs = [c[0] for c in corners]
        ys = [c[1] for c in corners]
        cx = (min(xs) + max(xs)) / 2
        cy = (min(ys) + max(ys)) / 2
        
        flipped_corners = []
        for (px, py) in corners:
            if flip_dir == "horizontal":
                new_py = 2*cy - py
                flipped_corners.append((px, new_py))
            else:
                new_px = 2*cx - px
                flipped_corners.append((new_px, py))
        
        xs_new = [fc[0] for fc in flipped_corners]
        ys_new = [fc[1] for fc in flipped_corners]
        new_x_min, new_x_max = min(xs_new), max(xs_new)
        new_y_min, new_y_max = min(ys_new), max(ys_new)
        
        self.xy = (new_x_min, new_y_min)
        self.width = new_x_max - new_x_min
        self.height = new_y_max - new_y_min

        self.update_patch()


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
                                     facecolor=self.facecolor, alpha=self.alpha, label=self.label)
        self.shape_type = "parallelogram"
    
    def update_patch(self):
        self.patch = patches.Polygon(self.points, closed=True, edgecolor=self.edgecolor,
                                     facecolor=self.facecolor, alpha=self.alpha, label=self.label)
    
    def plot(self, idx, ax, tc, set_visible=True):
        patch = ax[idx].add_patch(self.patch)
        patch.set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        x_vals = self.points[:,0]
        y_vals = self.points[:,1]
        
        x_min, x_max = np.min(x_vals), np.max(x_vals)
        y_min, y_max = np.min(y_vals), np.max(y_vals)
        
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
        
        scaled_points = np.array(scaled_points)
        x_vals = scaled_points[:,0]
        y_vals = scaled_points[:,1]
        
        x_min, x_max = np.min(x_vals), np.max(x_vals)
        y_min, y_max = np.min(y_vals), np.max(y_vals)
        
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
        self.update_patch()
    
    def rotation(self, angle, center=None):
        if center is None:
            x_vals = self.points[:,0]
            y_vals = self.points[:,1]
            x_min, x_max = x_vals.min(), x_vals.max()
            y_min, y_max = y_vals.min(), y_vals.max()
            cx = (x_min + x_max) / 2
            cy = (y_min + y_max) / 2
        else:
            cx, cy = center
        
        rad = math.radians(angle)
        
        rotated_points = []
        for (px, py) in self.points:
            tx = px - cx
            ty = py - cy
            rx = tx * math.cos(rad) - ty * math.sin(rad)
            ry = tx * math.sin(rad) + ty * math.cos(rad)
            rotated_points.append((rx + cx, ry + cy))
        
        self.points = np.array(rotated_points)
        self.update_patch()
    
    def translation(self, movement_x, movement_y):
        translated_points = []
        for (px, py) in self.points:
            translated_points.append((px + movement_x, py + movement_y))
        
        self.points = np.array(translated_points)
        self.update_patch()

    def flip(self):
        flip_dir = random.choice(["horizontal", "vertical"])
        
        x_vals = self.points[:,0]
        y_vals = self.points[:,1]
        x_min, x_max = x_vals.min(), x_vals.max()
        y_min, y_max = y_vals.min(), y_vals.max()
        cx = (x_min + x_max) / 2
        cy = (y_min + y_max) / 2
        
        flipped_points = []
        for (px, py) in self.points:
            if flip_dir == "horizontal":
                new_py = 2*cy - py
                flipped_points.append((px, new_py))
            else:
                new_px = 2*cx - px
                flipped_points.append((new_px, py))
        
        self.points = np.array(flipped_points)
        self.update_patch()


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
            self.xy,
            self.numVertices,
            radius=self.radius,
            orientation=self.orientation,
            edgecolor=self.edgecolor,
            facecolor=self.facecolor,
            alpha=self.alpha,
            label=self.label
        )
        self.shape_type = f"regular {numVertices}-gon"
    
    def update_patch(self):
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
    
    def plot(self, idx, ax, tc, set_visible=True):
        patch = ax[idx].add_patch(self.patch)
        patch.set_visible(set_visible)
    
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
        
        self.update_patch()
    
    def rotation(self, angle, center=None):
        rad = math.radians(angle)
        self.orientation += rad
        
        if center is not None:
            cx, cy = center
            x0, y0 = self.xy
            dx = x0 - cx
            dy = y0 - cy
            rx = dx*math.cos(rad) - dy*math.sin(rad)
            ry = dx*math.sin(rad) + dy*math.cos(rad)
            self.xy = (cx + rx, cy + ry)
        
        self.update_patch()
    
    def translation(self, movement_x, movement_y):
        cx, cy = self.xy
        self.xy = (cx + movement_x, cy + movement_y)
        self.update_patch()

    def flip(self):
        flip_dir = random.choice(["horizontal", "vertical"])
        # Just invert orientation for simplicity (like reflecting the shape).
        self.orientation = -self.orientation
        self.update_patch()


class RandomPath:
    def __init__(self, num_points=6, edgecolor='black', facecolor='none', label=None, alpha=1):
        self.num_points = num_points
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha
        
        vertices = [(random.uniform(-5, 5), random.uniform(-5, 5))
                    for _ in range(self.num_points)]
        
        center = np.mean(vertices, axis=0)
        angles = [math.atan2(v[1] - center[1], v[0] - center[0]) for v in vertices]
        sorted_vertices = [v for _, v in sorted(zip(angles, vertices))]
        sorted_vertices.append(sorted_vertices[0])
        
        codes = [Path.MOVETO] + [Path.LINETO] * (self.num_points - 1) + [Path.CLOSEPOLY]
        
        self.vertices = sorted_vertices
        self.codes = codes
        self.path = Path(self.vertices, self.codes)
        
        self.patch = PathPatch(self.path,
                               edgecolor=self.edgecolor,
                               facecolor=self.facecolor,
                               alpha=self.alpha,
                               label=self.label)
        self.shape_type = "shape"
        
        self.regulate((0, 100), (0, 100))

    def update_patch(self):
        self.path = Path(self.vertices, self.codes)
        self.patch = PathPatch(self.path,
                               edgecolor=self.edgecolor,
                               facecolor=self.facecolor,
                               alpha=self.alpha,
                               label=self.label)

    def plot(self, idx, ax, tc, set_visible=True):
        patch = ax[idx].add_patch(self.patch)
        patch.set_visible(set_visible)

    def regulate(self, xlim, ylim):
        xs = [p[0] for p in self.vertices]
        ys = [p[1] for p in self.vertices]
        
        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)
        
        shape_w = x_max - x_min
        shape_h = y_max - y_min
        
        region_w = xlim[1] - xlim[0]  # 100
        region_h = ylim[1] - ylim[0]  # 100

        if shape_w == 0 or shape_h == 0:
            return
        
        scale_fit_w = region_w / shape_w
        scale_fit_h = region_h / shape_h
        maxScaleToFit = min(scale_fit_w, scale_fit_h) 

        minScaleForOneThird_w = (region_w/3) / shape_w
        minScaleForOneThird_h = (region_h/3) / shape_h
        minScaleToMeetOneThird = max(minScaleForOneThird_w, minScaleForOneThird_h)

        if minScaleToMeetOneThird <= maxScaleToFit:
            scale_factor = maxScaleToFit
        else:
            scale_factor = maxScaleToFit

        cx = (x_min + x_max) / 2
        cy = (y_min + y_max) / 2
        
        scaled_vertices = []
        for (px, py) in self.vertices:
            sx = cx + (px - cx)*scale_factor
            sy = cy + (py - cy)*scale_factor
            scaled_vertices.append((sx, sy))
        
        xs_s = [p[0] for p in scaled_vertices]
        ys_s = [p[1] for p in scaled_vertices]
        
        x_min_s, x_max_s = min(xs_s), max(xs_s)
        y_min_s, y_max_s = min(ys_s), max(ys_s)
        
        shift_x, shift_y = 0, 0
        if x_min_s < xlim[0]:
            shift_x = xlim[0] - x_min_s
        elif x_max_s > xlim[1]:
            shift_x = xlim[1] - x_max_s
        
        if y_min_s < ylim[0]:
            shift_y = ylim[0] - y_min_s
        elif y_max_s > ylim[1]:
            shift_y = ylim[1] - y_max_s
        
        regulated_vertices = [(p[0] + shift_x, p[1] + shift_y) for p in scaled_vertices]
        
        self.vertices = regulated_vertices
        self.update_patch()

    def rotation(self, angle, center=None):
        if center is None:
            xs = [p[0] for p in self.vertices]
            ys = [p[1] for p in self.vertices]
            cx = (min(xs) + max(xs)) / 2
            cy = (min(ys) + max(ys)) / 2
        else:
            cx, cy = center
        
        rad = math.radians(angle)
        
        rotated_vertices = []
        for (px, py) in self.vertices:
            tx, ty = px - cx, py - cy
            rx = tx*math.cos(rad) - ty*math.sin(rad)
            ry = tx*math.sin(rad) + ty*math.cos(rad)
            rotated_vertices.append((rx + cx, ry + cy))
        
        self.vertices = rotated_vertices
        self.update_patch()
    
    def translation(self, movement_x, movement_y):
        translated_vertices = []
        for (px, py) in self.vertices:
            translated_vertices.append((px + movement_x, py + movement_y))
        
        self.vertices = translated_vertices
        self.update_patch()

    def flip(self):
        flip_dir = random.choice(["horizontal", "vertical"])
        
        xs = [p[0] for p in self.vertices]
        ys = [p[1] for p in self.vertices]
        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)
        
        cx = (x_min + x_max) / 2
        cy = (y_min + y_max) / 2
        
        flipped_vertices = []
        for (px, py) in self.vertices:
            if flip_dir == "horizontal":
                new_py = 2*cy - py
                flipped_vertices.append((px, new_py))
            else:
                new_px = 2*cx - px
                flipped_vertices.append((new_px, py))
        
        self.vertices = flipped_vertices
        self.update_patch()


class Point:
    def __init__(self, x, y, label="", color="black"):
        self.x = x
        self.y = y
        self.label = label
        self.color = color
    
    def plot(self, idx, ax, tc, set_visible=True):
        scatter = ax[idx].scatter(self.x, self.y, s=3, color=self.color)
        scatter.set_visible(set_visible)
        tc[idx].append(self.x, self.y, self.label)


class Diagram:
    def __init__(self, components=None, entities=None, background_color='white',
                 labels=None, colors=None):
        self.components = components if components is not None else []
        self.entities = entities if entities is not None else []
        self.background_color = background_color
        self.labels = labels if labels is not None else []
        self.colors = colors if colors is not None else []
        self.additional_info = []


def generate_random_shape1(max_random_path=10, shape=None, shape_list=None,
                           edgecolor=None, facecolor=None, color=None,
                           xlim=(0, 100), ylim=(0, 100), alpha=1, label=None):
    if shape_list is None:
        shape_list = ["triangle", "rectangle", "parallelogram", "regular polygon", "random path"]
    
    if (shape is None) or (not isinstance(shape, str)) or (shape.lower() not in shape_list):
        shape = random.choice(shape_list)
    
    if color is not None:
        edgecolor = color
        facecolor = color
    else:
        if edgecolor is None:
            edgecolor = random.choice(edgecolor_list)
        if facecolor is None:
            facecolor = random.choice(facecolor_list)
    
    if shape == "triangle":
        x1, y1 = random.uniform(*xlim), random.uniform(*ylim)
        x2, y2 = x1 + random.uniform(10, 40), y1
        x3, y3 = x1 + random.uniform(10, 40), y1 + random.uniform(10, 40)
        points = [(x1, y1), (x2, y2), (x3, y3)]
        shp = Triangle(points, edgecolor, facecolor, alpha=alpha)
    
    elif shape == "rectangle":
        x, y = random.uniform(*xlim), random.uniform(*ylim)
        width, height = random.uniform(10, 50), random.uniform(10, 50)
        shp = Rectangle((x, y), width, height, edgecolor, facecolor, alpha=alpha)
    
    elif shape == "parallelogram":
        start_x, start_y = random.uniform(*xlim), random.uniform(*ylim)
        vector1 = np.array([random.uniform(10, 50), 0])
        vector2 = np.array([random.uniform(10, 50), random.uniform(10, 50)])
        shp = Parallelogram(np.array([start_x, start_y]), vector1, vector2,
                            edgecolor, facecolor, alpha=alpha)
    
    elif shape == "random path":
        shp = RandomPath(num_points=random.randint(4, max_random_path),
                         edgecolor=edgecolor, facecolor=facecolor, alpha=alpha)
    else:
        cx, cy = random.uniform(*xlim), random.uniform(*ylim)
        num_vertices = random.randint(3, 8)
        radius = random.uniform(5, 30)
        orientation = random.uniform(0, 360)
        shp = RegularPolygon((cx, cy), num_vertices, radius,
                             edgecolor, facecolor,
                             orientation=math.radians(orientation),
                             alpha=alpha)
    
    shp.regulate(xlim, ylim)
    return shp


class TextCollection:
    def __init__(self):
        self.texts = []

    def append(self, x, y, text, **kwargs):
        self.texts.append((x, y, text, kwargs))

    def draw(self, img, set_visible=True):
        size = fontsize()
        for (x, y, text_str, kwargs) in self.texts:
            if 'fontsize' not in kwargs:
                kwargs['fontsize'] = size
            txt = img.text(x, y, text_str, **kwargs)
            txt.set_visible(set_visible)
            if set_visible:
                txt.set_path_effects([
                    withStroke(linewidth=2, foreground='white'),
                    withStroke(linewidth=0, foreground='none')
                ])


def congruence1(diagram):
    if random.randint(1, 2) == 1:
        shape1 = generate_random_shape1(shape="triangle")
    else:
        shape1 = generate_random_shape1()
    type_of_shape = shape1.shape_type
    
    diagram.components.append((0, shape1))
    
    shape2 = copy.deepcopy(shape1)
    shape2.update_patch()
    
    choice = random.randint(1, 3)
    if choice in [1, 3]:
        shape2.flip()
    if choice in [1, 2]:
        shape2.rotation(random.randint(10, 350))
    
    diagram.components.append((1, shape2))
    diagram.entities.append(("congruence1", [type_of_shape]))
    return diagram


def congruence2(diagram):
    if random.randint(1, 2) == 1:
        if random.randint(1, 2) == 1:
            shape1 = generate_random_shape1(shape="triangle")
        else:
            shape1 = generate_random_shape1(shape_list=["triangle", "rectangle", "parallelogram"])
        type_of_shape = shape1.shape_type
        
        diagram.components.append((0, shape1))

        shape2 = copy.deepcopy(shape1)
        shape2.update_patch()

        if type_of_shape == "triangle":
            new_points = []
            for i in range(2):
                one_point = [0, 0]
                for j in range(2):
                    one_point[j] = shape2.points[i][j] + random.random()
                new_points.append(tuple(one_point))
            new_points.append(shape2.points[2])
            shape2.points = tuple(new_points)
            shape2.update_patch()

        elif type_of_shape == "rectangle":
            shape2.width += random.random() * 2
            shape2.height += random.random() * 2
            shape2.update_patch()

        elif type_of_shape == "parallelogram":
            type_of_shape = "shape"
            new_pts = []
            for i in range(3):
                one_point = [0, 0]
                for j in range(2):
                    one_point[j] = shape2.points[i][j] + random.random()
                new_pts.append(tuple(one_point))
            new_pts.append(tuple(shape2.points[3]))
            shape2.points = np.array(new_pts)
            shape2.update_patch()

        choice = random.randint(1, 3)
        if choice in [1, 3]:
            shape2.flip()
        if choice in [1, 2]:
            shape2.rotation(random.randint(10, 350))
        
        diagram.components.append((1, shape2))

    else:
        if random.randint(1, 2) == 1:
            shape1 = generate_random_shape1(shape="triangle")
        else:
            shape1 = generate_random_shape1(shape_list=["triangle", "rectangle", "parallelogram"])
        type_of_shape = shape1.shape_type
        
        diagram.components.append((0, shape1))

        if random.randint(1, 3) == 1:
            type_of_shape = "shape"  
            shape2 = generate_random_shape1()
            diagram.components.append((1, shape2))
        else:
            shape2 = generate_random_shape1(shape=type_of_shape)
            diagram.components.append((1, shape2))
    
    diagram.entities.append(("congruence2", [type_of_shape]))
    return diagram


def congruence3(diagram):
    random_labels = random.sample(point_labels, 26)
    if random.randint(1, 2) == 1:
        random_colors = ['black' for _ in range(26)]
    else:
        random_colors = [random.choice(color_list) for _ in range(26)]

    if random.randint(1, 5) == 1:
        shape1 = generate_random_shape1(shape="random path", max_random_path=7)
    else:
        shape1 = generate_random_shape1(shape="triangle")
    shape_type = shape1.shape_type
    
    shape1.update_patch()
    diagram.components.append((0, shape1))

    first_point_list = []
    first_label_list = []
    if shape_type == "shape":
        for idx in range(len(shape1.vertices)):
            lab = random_labels.pop()
            col = random_colors.pop()
            x, y = shape1.vertices[idx]
            pnt = Point(x, y, label=lab, color=col)
            first_point_list.append(pnt)
            first_label_list.append(lab)
    else:
        pts = shape1.points
        for idx in range(len(pts)):
            lab = random_labels.pop()
            col = random_colors.pop()
            x, y = pts[idx]
            pnt = Point(x, y, label=lab, color=col)
            first_point_list.append(pnt)
            first_label_list.append(lab)

    for p in first_point_list:
        diagram.components.append((0, p))

    shape2 = copy.deepcopy(shape1)
    shape2.update_patch()

    choice = random.randint(1, 3)
    if choice in [1, 3]:
        shape2.flip()
    if choice in [1, 2]:
        shape2.rotation(random.randint(10, 350))

    diagram.components.append((1, shape2))

    second_point_list = []
    second_label_list = []
    if shape_type == "shape":
        for idx in range(len(shape2.vertices)):
            lab = random_labels.pop()
            col = random_colors.pop()
            x, y = shape2.vertices[idx]
            pnt = Point(x, y, label=lab, color=col)
            second_point_list.append(pnt)
            second_label_list.append(lab)
    else:
        pts2 = shape2.points
        for idx in range(len(pts2)):
            lab = random_labels.pop()
            col = random_colors.pop()
            x, y = pts2[idx]
            pnt = Point(x, y, label=lab, color=col)
            second_point_list.append(pnt)
            second_label_list.append(lab)
    
    for p in second_point_list:
        diagram.components.append((1, p))
    
    first_line_list = [first_label_list[idx] + first_label_list[idx+1]
                       for idx in range(-1, len(first_label_list)-1)]
    second_line_list = [second_label_list[idx] + second_label_list[idx+1]
                        for idx in range(-1, len(second_label_list)-1)]

    if random.randint(1, 2) == 1:
        idx = random.randint(0, len(first_label_list)-1)
        diagram.entities.append((
            "congruence3",
            [shape_type,
             first_line_list[idx],
             '/'.join(second_line_list),
             ', '.join(second_line_list),
             second_line_list[idx]]
        ))
    else:
        idx = random.randint(0, len(first_label_list)-1)
        diagram.entities.append((
            "congruence3",
            [shape_type,
             second_line_list[idx],
             '/'.join(first_line_list),
             ', '.join(first_line_list),
             first_line_list[idx]]
        ))
    
    diagram.additional_info.append(first_line_list)
    diagram.additional_info.append(second_line_list)

    return diagram


def congruence4(diagram):
    random_labels = random.sample(point_labels, 26)
    if random.randint(1, 2) == 1:
        random_colors = ['black' for _ in range(26)]
    else:
        random_colors = [random.choice(color_list) for _ in range(26)]

    if random.randint(1, 5) == 1:
        shape1 = generate_random_shape1(shape="random path", max_random_path=7)
    else:
        shape1 = generate_random_shape1(shape="triangle")
    shape_type = shape1.shape_type
    
    shape1.update_patch()
    diagram.components.append((0, shape1))

    first_point_list = []
    first_label_list = []
    if shape_type == "shape":
        for idx in range(len(shape1.vertices)):
            lab = random_labels.pop()
            col = random_colors.pop()
            x, y = shape1.vertices[idx]
            pnt = Point(x, y, label=lab, color=col)
            first_point_list.append(pnt)
            first_label_list.append(lab)
    else:
        pts = shape1.points
        for idx in range(len(pts)):
            lab = random_labels.pop()
            col = random_colors.pop()
            x, y = pts[idx]
            pnt = Point(x, y, label=lab, color=col)
            first_point_list.append(pnt)
            first_label_list.append(lab)

    for p in first_point_list:
        diagram.components.append((0, p))

    shape2 = copy.deepcopy(shape1)
    shape2.update_patch()

    choice = random.randint(1, 3)
    if choice in [1, 3]:
        shape2.flip()
    if choice in [1, 2]:
        shape2.rotation(random.randint(10, 350))

    diagram.components.append((1, shape2))

    second_point_list = []
    second_label_list = []
    if shape_type == "shape":
        for idx in range(len(shape2.vertices)):
            lab = random_labels.pop()
            col = random_colors.pop()
            x, y = shape2.vertices[idx]
            pnt = Point(x, y, label=lab, color=col)
            second_point_list.append(pnt)
            second_label_list.append(lab)
    else:
        pts2 = shape2.points
        for idx in range(len(pts2)):
            lab = random_labels.pop()
            col = random_colors.pop()
            x, y = pts2[idx]
            pnt = Point(x, y, label=lab, color=col)
            second_point_list.append(pnt)
            second_label_list.append(lab)

    for p in second_point_list:
        diagram.components.append((1, p))

    if random.randint(1, 2) == 1:
        idx = random.randint(0, len(first_label_list)-1)
        diagram.entities.append((
            "congruence4",
            [shape_type,
             first_label_list[idx],
             '/'.join(second_label_list),
             ', '.join(second_label_list),
             second_label_list[idx]]
        ))
    else:
        idx = random.randint(0, len(first_label_list)-1)
        diagram.entities.append((
            "congruence4",
            [shape_type,
             second_label_list[idx],
             '/'.join(first_label_list),
             ', '.join(first_label_list),
             first_label_list[idx]]
        ))
    
    diagram.additional_info.append(first_label_list)
    diagram.additional_info.append(second_label_list)

    return diagram


rules = [
    congruence1,
    congruence2,
    congruence3,
    congruence4
]

