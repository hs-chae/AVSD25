from .rules import *

import random

def create_tree():
    diagram = Diagram()
    rule = random.choice(rules)
    rule(diagram)
    return diagram
