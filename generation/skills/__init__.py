from . import absolute_position
from . import adjacency
from . import angle
from . import area
from . import boundary
from . import cardinal
from . import cardinal_direction
from . import color
from . import congruence
from . import connectedness
from . import convexity
from . import coordinate
from . import curvature
from . import direction
from . import interior
from . import intersection
from . import length
from . import line
from . import OCR
from . import ordinal
from . import orientation
from . import orthogonality
from . import overlap
from . import parallel
from . import point
from . import reflection
from . import rel_pos
from . import rotation
from . import rotational_symmetry
from . import shape
from . import sharpness
from . import similarity
from . import symbol
from . import tangency
from . import texture
from . import width 


import builtins

skill_list = [
    "absolute_position",
    "adjacency",
    "angle",
    "area",
    "boundary",
    "cardinal",
    "cardinal_direction",
    "color",
    "congruence",
    "connectedness",
    "convexity",
    "coordinate",
    "curvature",
    "direction",
    "interior",
    "intersection",
    "length",
    "line",
    "OCR",
    "ordinal",
    "orientation",
    "orthogonality",
    "overlap",
    "parallel",
    "point",
    "reflection",
    "rel_pos",
    "rotation",
    "rotational_symmetry",
    "shape",
    "sharpness",
    "similarity",
    "symbol",
    "tangency",
    "texture",
    "width",
]

def ban_print(func):
    def wrapper(*args, **kwargs):
        original_print = builtins.print
        builtins.print = lambda *args, **kwargs: None
        try:
            return func(*args, **kwargs)
        finally:
            builtins.print = original_print
    return wrapper

@ban_print
def generate(skill, *args, **kwargs):
    assert skill in skill_list
    return eval(skill).generate(*args, **kwargs)

@ban_print
def generate_with_augmentation(skill, *args, **kwargs):
    assert skill in skill_list
    return eval(skill).generate_with_augmentation(*args, **kwargs)

def generate_image_caption_pair(skill, *args, **kwargs):
    assert skill in skill_list
    return eval(skill).generate_image_caption_pair(*args, **kwargs)


__all__ = ["skill_list", "generate", "generate_with_augmentation"]
