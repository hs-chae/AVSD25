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

point_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num_labels = list("1234567890")
func_labels = list("abcdefghijklmnopqrstuvwxyz")
color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
facecolor_list = ["None", "None", "None", "None", "None", "black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
edgecolor_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

class Diagram:
    def __init__(self, components=None, entities=None, background_color='white', labels=None, colors=None):
        self.components = components if components is not None else []
        self.entities = entities if entities is not None else []
        self.background_color = background_color
        self.labels = labels if labels is not None else []
        self.colors = colors if colors is not None else []

class Rectangle:
    def __init__(self, xy, width, height, edgecolor, facecolor, label=None, alpha=1):
        self.xy = xy  
        self.width = width
        self.height = height
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.label = label
        self.alpha = alpha
        self.update_patch()

        self.left = None
        self.right = None
        self.upper = None
        self.lower = None
    
    def update_patch(self):
        self.patch = patches.Rectangle(
            self.xy,
            self.width,
            self.height,
            edgecolor=self.edgecolor,
            facecolor=self.facecolor, 
            alpha=self.alpha,
            label=self.label
        )
    
    def plot(self, ax, tc, set_visible=True):
        self.update_patch()
        patch = ax.add_patch(self.patch)
        patch.set_visible(set_visible)
        if self.label is not None:
            x_center = self.xy[0] + self.width/2
            y_center = self.xy[1] + self.height/2
            tc.append(x_center, y_center, self.label)

class TextCollector:
    def __init__(self):
        self.texts = []

    def append(self, x, y, text):
        self.texts.append((x, y, text))

    def draw_all(self, ax):
        for (x, y, text) in self.texts:
            ax.text(x, y, text, ha='center', va='center')

class Grid:
    def __init__(self, row=None, col=None, width=1, height=1, alpha=1):
        self.row = random.randint(2, 10) if row is None else row
        self.col = random.randint(2, 10) if col is None else col
        self.width = width
        self.height = height
        self.edgecolor = random.choice(['black', 'none'])
        self.grid_type = "color"
        self.update_grid_info()
    
    def update_grid_info(self):
        self.grid_info = dict()
        for row_idx in range(self.row):
            for col_idx in range(self.col):
                new_rect = Rectangle(
                    (col_idx*self.width, row_idx*self.height),
                    self.width,
                    self.height,
                    self.edgecolor,
                    random.choice(color_list)
                )
                self.grid_info[(row_idx, col_idx)] = new_rect

        for row_idx in range(self.row):
            for col_idx in range(self.col):
                rect = self.grid_info[(row_idx, col_idx)]
                if col_idx > 0:
                    rect.left = self.grid_info[(row_idx, col_idx-1)]
                if col_idx < self.col - 1:
                    rect.right = self.grid_info[(row_idx, col_idx+1)]
                if row_idx > 0:
                    rect.lower = self.grid_info[(row_idx-1, col_idx)]
                if row_idx < self.row - 1:
                    rect.upper = self.grid_info[(row_idx+1, col_idx)]
    
    def adjust_color(self, answer_color=None):
        self.answer_color = answer_color
        self.new_color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]
        if self.answer_color not in self.new_color_list:
            self.answer_color = random.choice(self.new_color_list)
        self.option_color_list = copy.deepcopy(self.new_color_list)
        self.option_color_list.remove(self.answer_color)
        
        count = random.randint(1, (self.row*self.col)//4)
        self.idx_set = set()
        self.idx_set.add(random.choice(list(self.grid_info.keys())))

        trial = 0
        while len(self.idx_set) < count:
            move_idx = random.choice(list(self.idx_set))
            trial = 0
            while True:
                new_idx = random.choice([
                    (move_idx[0], move_idx[1]-1),  # 왼쪽
                    (move_idx[0], move_idx[1]+1),  # 오른쪽
                    (move_idx[0]-1, move_idx[1]),  # 아래
                    (move_idx[0]+1, move_idx[1])   # 위
                ])
                if new_idx in self.grid_info:
                    break
                trial += 1
                if trial > 1000:
                    break
            if new_idx in self.grid_info:
                self.idx_set.add(new_idx)

            trial += 1
            if trial > 1000:
                break

        for r in range(self.row):
            for c in range(self.col):
                if (r, c) in self.idx_set:
                    self.grid_info[(r, c)].facecolor = self.answer_color
                else:
                    self.grid_info[(r, c)].facecolor = random.choice(self.option_color_list)
        
        self.get_adjacent_colors()
    
    def get_adjacent_colors(self):
        self.adjacent_colors = set()
        for idx in self.idx_set:
            my_rect = self.grid_info[idx]
            for neighbor in [my_rect.left, my_rect.right, my_rect.upper, my_rect.lower]:
                if neighbor is not None and neighbor.facecolor != self.answer_color:
                    self.adjacent_colors.add(neighbor.facecolor)
    
    def plot(self, ax, tc, set_visible=True):
        for one_key in self.grid_info:
            self.grid_info[one_key].plot(ax, tc, set_visible=set_visible)
        ax.axis('equal')
        ax.axis('off')
        ax.set_xlim((-0.5, self.col*self.width + 0.5))
        ax.set_ylim((-0.5, self.row*self.height + 0.5))

class TextGrid:
    """
    글자가 들어간 그리드
    row: 세로(행) 개수
    col: 가로(열) 개수
    """
    def __init__(self, row=None, col=None, width=1, height=1, alpha=1):
        self.row = random.randint(2, 10) if row is None else row
        self.col = random.randint(2, 10) if col is None else col
        self.width = width
        self.height = height
        self.edgecolor = random.choice(['black', 'none'])
        self.option = random.randint(1, 3)  # 1: 투명, 2: 단색 통일, 3: 랜덤색
        self.alpha = random.random() / 2
        self.facecolor = "none"
        if self.option == 2:
            self.facecolor = random.choice(color_list)
        self.grid_type = "text"
        self.update_grid_info()
    
    def update_grid_info(self):
        self.grid_info = dict()
        for row_idx in range(self.row):
            for col_idx in range(self.col):
                if self.option == 3:
                    fc = random.choice(color_list)
                else:
                    fc = self.facecolor

                new_rect = Rectangle(
                    (col_idx*self.width, row_idx*self.height),
                    self.width,
                    self.height,
                    self.edgecolor,
                    fc,
                    alpha=self.alpha
                )
                self.grid_info[(row_idx, col_idx)] = new_rect

        for row_idx in range(self.row):
            for col_idx in range(self.col):
                rect = self.grid_info[(row_idx, col_idx)]
                if col_idx > 0:
                    rect.left = self.grid_info[(row_idx, col_idx-1)]
                if col_idx < self.col - 1:
                    rect.right = self.grid_info[(row_idx, col_idx+1)]
                if row_idx > 0:
                    rect.lower = self.grid_info[(row_idx-1, col_idx)]
                if row_idx < self.row - 1:
                    rect.upper = self.grid_info[(row_idx+1, col_idx)]
    
    def adjust_text(self, answer_text=None):
        self.answer_text = answer_text
        
        self.new_text_list = []
        rand_num = random.randint(1, 4)
        if rand_num in [1, 4]:
            self.new_text_list += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if rand_num in [2, 4]:
            self.new_text_list += list("1234567890")
        if rand_num in [3, 4]:
            self.new_text_list += list("abcdefghijklmnopqrstuvwxyz")

        if self.answer_text not in self.new_text_list:
            self.answer_text = random.choice(self.new_text_list)
        self.option_text_list = copy.deepcopy(self.new_text_list)
        self.option_text_list.remove(self.answer_text)

        self.answer_idx = random.choice(list(self.grid_info.keys()))

        for r in range(self.row):
            for c in range(self.col):
                if (r, c) == self.answer_idx:
                    self.grid_info[(r, c)].label = self.answer_text
                else:
                    self.grid_info[(r, c)].label = random.choice(self.option_text_list)
        
        self.get_adjacent_text()
    
    def get_adjacent_text(self):
        self.adjacent_text = set()
        my_rect = self.grid_info[self.answer_idx]
        for neighbor in [my_rect.left, my_rect.right, my_rect.upper, my_rect.lower]:
            if neighbor is not None and neighbor.label != self.answer_text:
                self.adjacent_text.add(neighbor.label)
        
    def plot(self, ax, tc, set_visible=True):
        for one_key in self.grid_info:
            self.grid_info[one_key].plot(ax, tc, set_visible=set_visible)
        ax.axis('equal')
        ax.axis('off')
        ax.set_xlim((-0.5, self.col*self.width + 0.5))
        ax.set_ylim((-0.5, self.row*self.height + 0.5))

def adjacency1(diagram):
    g = Grid()
    g.adjust_color()

    diagram.components.append(g)
    diagram.entities.append((
        "adjacency1",
        [
            str(g.row),
            str(g.col),
            g.answer_color,
            ", ".join(g.new_color_list),
            "/".join(g.option_color_list),
            ", ".join(g.option_color_list),
            ", ".join(g.adjacent_colors),
        ]
    ))
    return diagram

def adjacency2(diagram):
    g = TextGrid()
    g.adjust_text()
    diagram.components.append(g)
    diagram.entities.append((
        "adjacency2",
        [
            str(g.row),
            str(g.col),
            g.answer_text,
            ", ".join(g.new_text_list),
            "/".join(g.option_text_list),
            ", ".join(g.option_text_list),
            ", ".join(g.adjacent_text),
        ]
    ))
    return diagram

rules = [
    adjacency1,
    adjacency2
]
