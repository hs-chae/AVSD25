from .rules import *

def plot_diagram(ax, tc, diagram, set_visible = True):
    for one_component in diagram.components:
        one_component.plot(ax, tc, set_visible = set_visible)
