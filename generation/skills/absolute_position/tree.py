from .rules import *

import random

def create_tree(diagram):
    rule = random.choice(rules)
    rule(diagram)
    return diagram, rule.__name__