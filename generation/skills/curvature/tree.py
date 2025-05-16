from .rules import *

import random

def create_tree(ax, tc):
    diagram = Diagram()
    rule = random.choice(rules)
    rule(diagram, ax, tc)
    return diagram