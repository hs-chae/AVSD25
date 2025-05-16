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
from scipy.interpolate import make_interp_spline
import networkx as nx

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

def rotate_point(p, theta):
    """원점을 기준으로 점 p=(x,y)를 theta만큼 회전시켜 반환."""
    c, s = np.cos(theta), np.sin(theta)
    x, y = p
    return np.array([c*x - s*y, s*x + c*y])

def generate_random_curvy_path(
    A, B, 
    n_wiggles=5,         
    amplitude_range=(0.5, 2.0),  
    resolution=200      
):

    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    AB = B - A
    
    dist_AB = np.linalg.norm(AB)
    if dist_AB < 1e-9:
        return np.array([A, B])
    
    theta = -np.arctan2(AB[1], AB[0])  
    

    B_rot = rotate_point(AB, theta)  
    
    t_control = np.linspace(0, 1, n_wiggles + 2) 
    x_control = dist_AB * t_control 
    
    y_control = np.zeros_like(x_control)
    for i in range(1, len(y_control) - 1):
        amp = np.random.uniform(*amplitude_range)
        sign = 1 if np.random.rand() < 0.5 else -1
        y_control[i] = sign * amp
    
    spline = make_interp_spline(x_control, y_control, k=3)  
    x_smooth = np.linspace(0, dist_AB, resolution)
    y_smooth = spline(x_smooth) 

    path_rot = np.stack([x_smooth, y_smooth], axis=1) 
    path = []
    for p_rot in path_rot:
        p_original = rotate_point(p_rot, -theta) + A
        path.append(p_original)
    path = np.array(path)
    return path

class Point:
    def __init__(self, x, y, label = "", color = "black"):
        self.x = x
        self.y = y
        self.label = label
        self.color = color
    
    def plot(self, ax, tc, set_visible = True):
        ax.scatter(self.x, self.y, color = self.color).set_visible(set_visible)
        tc.append(self.x, self.y, self.label)

class Path:
    def __init__(self, connected = True, point_label_available = True):
        self.point_color, self.line_color = random.sample(color_list, 2)
        self.other_color = 'none'
        
        self.generate_random_point(point_label_available)

        resolution = random.randint(300, 700)
        if random.randint(1, 2) == 1:
            n_wiggles = random.randint(3, 10)
        else:
            n_wiggles = random.randint(10, 30)

        trial = 0
        while True:
            path = generate_random_curvy_path(self.A, self.B, n_wiggles=n_wiggles, amplitude_range=(random.randint(1, 3), random.randint(5, 10)), resolution=resolution)
            num_color = random.randint(1000, 10000)
            num_none = random.randint(50, 900)
            line_color_list = random.sample([self.line_color]*num_color+[self.other_color]*num_none, (resolution*8)//10)
            self.line_width = random.randint(1, 5)
            self.check_connected = True
            self.path_plot_info = []
            self.path_plot_info.append({'x':path[:resolution//10+1,0], 'y':path[:resolution//10+1,1], 'color':self.line_color})
            for idx in range(resolution//10, (resolution*9)//10, 10):
                self.path_plot_info.append({'x':path[idx:idx+11,0], 'y':path[idx:idx+11,1], 'color':line_color_list[idx//10-3]})
                if line_color_list[idx//10-3] != self.line_color:
                    self.check_connected = False
            self.path_plot_info.append({'x':path[(resolution*9)//10:,0], 'y':path[(resolution*9)//10:,1], 'color':self.line_color})
            if self.check_connected == connected:
                break
            trial += 1
            if trial > 10000:
                raise
    
    def plot(self, ax, tc, set_visible = True):
        for idx in range(len(self.path_plot_info)):
            x = self.path_plot_info[idx]['x']
            y = self.path_plot_info[idx]['y']
            color = self.path_plot_info[idx]['color']
            line = ax.plot(x, y, color = color, ls = '-', lw = self.line_width)  
            line[0].set_visible(set_visible)
        self.point_start.plot(ax, tc, set_visible = set_visible)
        self.point_end.plot(ax, tc, set_visible = set_visible)
    
    def generate_random_point(self, point_label_available):
        self.generate_random_point_coord()
        if point_label_available:
            self.label_start, self.label_end = random.sample(point_labels, 2)
        else:
            self.label_start, self.label_end = "", ""
        self.point_start = Point(self.A[0], self.A[1], label = self.label_start, color = self.point_color)
        self.point_end = Point(self.B[0], self.B[1], label = self.label_end, color = self.point_color)
    
    def generate_random_point_coord(self):
        option = random.randint(1, 3)
        if option == 1:
            trial = 0
            while True:
                start_x = random.uniform(0, 8)
                start_y = random.uniform(0, 8)
                end_x = random.uniform(0, 8)
                end_y = random.uniform(0, 8)
                if ((end_x-start_x)**2+(end_y-start_y)**2) > 50:
                    break
                trial += 1
                if trial > 1000:
                    raise
        elif option == 2:
            start_x, start_y, end_x, end_y = 0, 0, 8, 0
        else:
            start_x, start_y, end_x, end_y = 0, 0, 0, 8
        
        self.A = (start_x, start_y)
        self.B = (end_x, end_y)

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
    
    def plot(self, ax, tc, set_visible = True):
        self.update_patch()
        patch = ax.add_patch(self.patch)
        patch.set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        """
        삼각형이 xlim, ylim 범위 안에 들어오도록 스케일 & 평행이동해 self.patch 재생성
        """
        x_vals = [p[0] for p in self.points]
        y_vals = [p[1] for p in self.points]
        
        x_min, x_max = min(x_vals), max(x_vals)
        y_min, y_max = min(y_vals), max(y_vals)
        
        shape_w = x_max - x_min
        shape_h = y_max - y_min
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        # 스케일 팩터 계산 (너무 큰 경우 줄이기)
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)
        
        # 중심좌표
        cx = (x_min + x_max) / 2
        cy = (y_min + y_max) / 2
        
        # 스케일링 (도형의 중심을 기준으로)
        scaled_points = []
        for (px, py) in self.points:
            scaled_x = cx + (px - cx)*scale_factor
            scaled_y = cy + (py - cy)*scale_factor
            scaled_points.append((scaled_x, scaled_y))
        
        # 스케일링 후 bounding box 재계산
        x_vals = [p[0] for p in scaled_points]
        y_vals = [p[1] for p in scaled_points]
        x_min, x_max = min(x_vals), max(x_vals)
        y_min, y_max = min(y_vals), max(y_vals)
        
        # 평행 이동량 계산
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
        
        # 이동 적용
        regulated_points = [(p[0] + shift_x, p[1] + shift_y) for p in scaled_points]
        
        # patch 갱신
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
    
    def plot(self, ax, tc, set_visible = True):
        self.update_patch()
        patch = ax.add_patch(self.patch)
        patch.set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        """
        사각형이 xlim, ylim 범위 안에 들어오도록 스케일 & 평행이동해 self.patch 재생성
        """
        # 현재 bounding box
        x_min = self.xy[0]
        y_min = self.xy[1]
        x_max = x_min + self.width
        y_max = y_min + self.height
        
        shape_w = self.width
        shape_h = self.height
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        # 스케일 팩터
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)
        
        # 중심
        cx = (x_min + x_max)/2
        cy = (y_min + y_max)/2
        
        # (x_min, y_min)을 중심기준 스케일한다고 할 경우,
        # 사각형은 꼭짓점 4개 중 하나만 갖고 있어도 되지만
        # 여기서는 "중심을 기준"으로 스케일한다고 가정
        new_w = shape_w * scale_factor
        new_h = shape_h * scale_factor
        
        new_x_min = cx - new_w/2
        new_x_max = cx + new_w/2
        new_y_min = cy - new_h/2
        new_y_max = cy + new_h/2
        
        # 평행 이동
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
        
        # patch 갱신
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
        patch = ax.add_patch(self.patch)
        patch.set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        """
        평행사변형이 xlim, ylim 범위 안에 들어오도록 스케일 & 평행이동
        """
        x_vals = [p[0] for p in self.points]
        y_vals = [p[1] for p in self.points]
        
        x_min, x_max = min(x_vals), max(x_vals)
        y_min, y_max = min(y_vals), max(y_vals)
        
        shape_w = x_max - x_min
        shape_h = y_max - y_min
        
        region_w = xlim[1] - xlim[0]
        region_h = ylim[1] - ylim[0]
        
        # 스케일
        scale_factor = 1.0
        if shape_w > region_w or shape_h > region_h:
            scale_factor = min(region_w / shape_w, region_h / shape_h)
        
        cx = (x_min + x_max)/2
        cy = (y_min + y_max)/2
        
        # 스케일 & 이동
        scaled_points = []
        for (px, py) in self.points:
            sx = cx + (px - cx)*scale_factor
            sy = cy + (py - cy)*scale_factor
            scaled_points.append((sx, sy))
        
        # 다시 bounding box
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
        patch = ax.add_patch(self.patch)
        patch.set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        """
        원이 xlim, ylim 범위 안에 들어가도록 스케일 & 평행이동
        """
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
        patch = ax.add_patch(self.patch)
        patch.set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        """
        타원이 xlim, ylim 범위 안에 들어가도록 스케일 & 평행이동
        """
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
        patch = ax.add_patch(self.patch)
        patch.set_visible(set_visible)
    
    def regulate(self, xlim, ylim):
        """
        정다각형이 xlim, ylim 범위 안에 들어가도록 스케일 & 평행이동
        """
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

class Island:
    def find_islands(self):
        n = len(self.matrix)
        visited = [False] * n
        self.islands = []
        
        def dfs(node, current_island):
            visited[node] = True
            current_island.append(node)
            for neighbor in range(n):
                if self.matrix[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor, current_island)
        
        for node in range(n):
            if not visited[node]:
                current_island = []
                dfs(node, current_island)
                self.islands.append(current_island)
        
        return self.islands

    def plot(self, ax, tc, set_visible = True):
        n = len(self.matrix)
        G = nx.Graph()
        
        # 노드 추가
        for i in range(n):
            G.add_node(i)
        
        # 간선 추가 (무방향 그래프이므로 i < j 조건 사용)
        for i in range(n):
            for j in range(i+1, n):
                if self.matrix[i][j] == 1:
                    G.add_edge(i, j)
        
        # 각 연결 요소에 대해 색상 할당 (색상이 부족할 경우 순환 사용)
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive']
        color_map = {}
        random_choice = random.randint(1, 5)
        if random_choice < 3:
            for idx, island in enumerate(self.islands):
                for node in island:
                    # color_map[node] = colors[idx % len(colors)]
                    color_map[node] = random.choice(colors)
        elif random_choice < 5:
            fixed_color = random.choice(colors)
            for idx, island in enumerate(self.islands):
                for node in island:
                    color_map[node] = fixed_color
        else:
            for idx, island in enumerate(self.islands):
                for node in island:
                    color_map[node] = colors[idx % len(colors)]

        node_colors = [color_map.get(node, 'black') for node in G.nodes()]
        
        # 3x3 그리드에 노드 배치: x 좌표는 node % 3, y 좌표는 2 - node // 3
        pos = {i: (i % 3, 2 - i//3) for i in range(n)}
        
        # 그래프 그리기
        # nx.draw(G, pos = pos, ax = ax, with_labels=False, node_color=node_colors, node_size=600, font_color='white')
        nodes = nx.draw_networkx_nodes(G, pos=pos, ax=ax, node_color=node_colors, node_size=600)
        edges = nx.draw_networkx_edges(G, pos=pos, ax=ax)
        nodes.set_visible(set_visible)
        edges.set_visible(set_visible) 

        if random.randint(1, 2) == 1:
            for i in range(n):
                tc.append(i % 3 - 0.02, 2 - i//3 - 0.02, self.text[i])
        elif random.randint(1, 2) == 1:
            dx = random.uniform(0, 0.07)
            dy = random.uniform(0, 0.07)
            for i in range(n):
                tc.append(i % 3 - dx, 2 - i//3 - dy, self.text[i])
        else:
            for i in range(n):
                dx = random.uniform(0, 0.07)
                dy = random.uniform(0, 0.07)      
                tc.append(i % 3 - dx, 2 - i//3 - dy, self.text[i])      

    def generate_matrix(self):
        n = 9
        # 초기에는 모든 원소를 0으로 채운 9x9 행렬 생성
        matrix = [[0] * n for _ in range(n)]
        
        # 강제로 0으로 설정할 위치 (상대적으로 한쪽만 지정하면 대칭을 위해 반대쪽도 적용)
        forced_zero = {(0, 8), (2, 6), (0, 6), (1, 7), (2, 8), (0, 2), (3, 5), (6, 8)}
        value_list = [0]*random.randint(1, 10)+[1]
        # 상삼각 행렬(대각선 위의 원소)만 랜덤하게 채우고 대칭성 부여
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) in forced_zero:
                    value = 0
                else:
                    value = random.choice(value_list)
                matrix[i][j] = value
                matrix[j][i] = value  # 대칭성 부여
        self.matrix = matrix    

    def generate_text(self, random_key):
        if random_key == 1:
            self.text = [i for i in range(9)]
        elif random_key == 2:
            self.text = [i+1 for i in range(9)]
        elif random_key == 3:
            number_random = random.sample(list('0123456789'), 9)
            self.text = [number_random[i] for i in range(9)]
        elif random_key == 4:
            alphabet_random = random.sample(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 9)
            self.text = [alphabet_random[i] for i in range(9)]
        else:
            alphabet_random = random.sample(list('abcdefgjihklmnopqrstuvwxyz'), 9)
            self.text = [alphabet_random[i] for i in range(9)]    

    def island_text(self):
        islands_output = [[self.text[node] for node in island] for island in self.islands]
        for island in islands_output:
            random.shuffle(island)
        return islands_output

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

def check_intersect(obj1, obj2):
    shape1 = to_shapely(obj1)
    shape2 = to_shapely(obj2)
    
    if shape1 is None or shape2 is None:
        return False
    
    if shape1.contains(shape2):
        return True
    elif shape2.contains(shape1):
        return True
    elif shape1.intersects(shape2):
        return True
    else:
        return False

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
        x2, y2 = x1 + random.uniform(10, 50), y1
        x3, y3 = x1 + random.uniform(10, 50), y1 + random.uniform(10, 50)
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

# 두 점을 잇는 선이 connected인가? (color, True)
def connectedness1(diagram):
    connected = True
    point_label_available = False

    path1 = Path(connected = connected, point_label_available = point_label_available)
    diagram.components.append(path1)
    diagram.entities.append(("connectedness1", [path1.point_color]))

    return diagram

# 두 점을 잇는 선이 connected인가? (label, True)
def connectedness2(diagram):
    connected = True
    point_label_available = True

    path1 = Path(connected = connected, point_label_available = point_label_available)
    diagram.components.append(path1)

    if random.randint(1, 2) == 1:
        diagram.entities.append(("connectedness2", [path1.label_end, path1.label_start]))
    else:
        diagram.entities.append(("connectedness2", [path1.label_start, path1.label_end]))

    return diagram

# 두 점을 잇는 선이 connected인가? (color, False)
def connectedness3(diagram):
    connected = False
    point_label_available = False

    path1 = Path(connected = connected, point_label_available = point_label_available)
    diagram.components.append(path1)
    diagram.entities.append(("connectedness3", [path1.point_color]))

    return diagram

# 두 점을 잇는 선이 connected인가? (label, False)
def connectedness4(diagram):
    connected = False
    point_label_available = True

    path1 = Path(connected = connected, point_label_available = point_label_available)
    diagram.components.append(path1)

    if random.randint(1, 2) == 1:
        diagram.entities.append(("connectedness4", [path1.label_end, path1.label_start]))
    else:
        diagram.entities.append(("connectedness4", [path1.label_start, path1.label_end]))

    return diagram

# 주어진 그림에서 connected shape의 개수는?
def connectedness5(diagram):
    color = random.choice(color_list)

    shape_list = []
    lim_list = [(0, 100), (-50, 0), (0, 50), (50, 100), (100, 150), (-60, -30), (-30, 0), (0, 30), (30, 60), (60, 90), (90, 120), (120, 150)]
    if random.randint(1, 2) == 1:
        num_shapes = random.randint(3, 6)
    elif random.randint(1, 2) == 1:
        num_shapes = random.randint(7, 10)
    elif random.randint(1, 2) == 1:
        num_shapes = random.randint(11, 15)
    elif random.randint(1, 2) == 1:
        num_shapes = random.randint(16, 20)
    else:
        num_shapes = random.randint(21, 25)

    for i in range(num_shapes):
        xlim = random.choice(lim_list)
        ylim = random.choice(lim_list)
        new_shape = generate_random_shape(edgecolor = "none", facecolor = color, xlim = xlim, ylim = ylim)
        shape_list.append(new_shape)

    adj_list = { shape: [] for shape in shape_list }

    for i in range(len(shape_list)):
        for j in range(i+1, len(shape_list)):
            if check_intersect(shape_list[i].patch, shape_list[j].patch):
                adj_list[shape_list[i]].append(shape_list[j])
                adj_list[shape_list[j]].append(shape_list[i])

    visited = set()
    num_connected_area = 0

    def bfs(start):
        queue = [start]
        visited.add(start)
        while queue:
            current = queue.pop(0)
            for neighbor in adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    for shape in shape_list:
        if shape not in visited:
            bfs(shape)
            num_connected_area += 1

    diagram.components.extend(shape_list)
    diagram.entities.append(("connectedness5", [str(random.randint(1, 20)), str(num_connected_area)]))
    return diagram

# 그래프의 island의 개수
def connectedness6(diagram):
    i = Island()
    i.generate_matrix()
    i.find_islands()
    i.generate_text(random.randint(1, 5))
    diagram.components.append(i)
    island_output = i.island_text()
    diagram.entities.append(("connectedness6", [str(len(island_output))]))
    return diagram

# 연결된 노드 그룹
def connectedness7(diagram):
    i = Island()
    i.generate_matrix()
    i.find_islands()
    i.generate_text(random.randint(1, 5))
    diagram.components.append(i)
    island_output = i.island_text()

    i2 = Island()
    i2.generate_matrix()
    i2.find_islands()
    option = random.randint(1, 2)
    i2.generate_text(option)
    island_output2 = i2.island_text()
    if option == 1:
        node_start = 0
        node_end = 8
    else:
        node_start = 1
        node_end = 9
    example_matrix = str(i2.matrix)
    example_list = str(island_output2)

    diagram.entities.append(("connectedness7", [str(island_output), str(node_start), str(node_end), example_matrix, example_list]))
    return diagram

# N과 연결된 노드
def connectedness8(diagram):
    while True:
        i = Island()
        i.generate_matrix()
        i.find_islands()
        i.generate_text(random.randint(1, 5))
        island_output = i.island_text()
        if len(island_output) < 8:
            break
    for island in island_output:
        if len(island) > 1:
            connected_list = []
            criteria_node = random.choice(island)
            for one_node in island:
                if one_node != criteria_node:
                    connected_list.append(str(one_node))
    diagram.components.append(i)
    diagram.entities.append(("connectedness8", [str(criteria_node), ", ".join(connected_list)]))
    return diagram

rules = [
    connectedness1,
    connectedness2,
    connectedness3,
    connectedness4,
    connectedness5,
    connectedness5,
    connectedness5,
    connectedness5,
    connectedness6,
    connectedness7,
    connectedness8,
    connectedness6,
    connectedness7,
    connectedness8
]