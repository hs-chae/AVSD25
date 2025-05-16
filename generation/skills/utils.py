import yaml
import random
import math

import numpy as np
import cv2
from PIL import Image

from matplotlib.patheffects import withStroke

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

def fontsize():
    if isinstance(config['fontsize'], int):
        return config['fontsize']
    else:
        return random.randint(config['fontsize']['min'], config['fontsize']['max'])
    
def resolution():
    if isinstance(config['resolution'], int):
        return config['resolution']
    else:
        return random.randint(config['resolution']['min'], config['resolution']['max'])

class TextCollection:
    def __init__(self):
        self.texts = []

    def append(self, x, y, text, **kwargs):
        self.texts.append((x, y, text, kwargs))

    def draw(self, img, set_visible = True):
        size = fontsize()

        for text in self.texts:
            x, y, text, kwargs = text
            if 'fontsize' not in kwargs:
                kwargs['fontsize'] = size
            text = img.text(x, y, text, **kwargs)
            text.set_visible(set_visible)
            if set_visible:
                text.set_path_effects([withStroke(linewidth=2, foreground='white'), withStroke(linewidth=0, foreground='none')])

    def too_close(self, threshold):
        points = [(text[0], text[1]) for text in self.texts]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i][0], points[i][1],
                x2, y2 = points[j][0], points[i][1]
                distance = math.dist((x1, y1), (x2, y2))
                # Alternatively, you can calculate the distance manually:
                # distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if distance < threshold:
                    return True
        return False
        

def augment_isavailable(conversations):
    for converation in conversations:
        q = converation[0]
        a = converation[1]

        blacklist = [
            "color", "colour",
            'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black', 'gray', 
            'brown', 'pink', 'cyan', 'magenta', 'lime', 'olive', 'maroon', 'navy', 
            'teal', 'silver', 'gold', 'white', 'grey'
        ]

        if any(word in q for word in blacklist) or any(word in a for word in blacklist):
            return False
        
    return True

def apply_controlnet_pipeline(image, controlnet_pipeline):
    if controlnet_pipeline is None:
        return image

    numpy_image = np.array(image)
    gray_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGBA2GRAY)
    canny = cv2.Canny(gray_image, 50, 150)
    canny = cv2.cvtColor(canny, cv2.COLOR_GRAY2RGB)
    canny = Image.fromarray(canny)

    prompt = random.choice(config['controlnet_prompts'])

    return controlnet_pipeline(
        prompt=prompt,
        control_image=canny,
        **config['controlnet_hyperparameters']
    )[0][0]