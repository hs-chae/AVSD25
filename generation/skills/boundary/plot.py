from .rules import *

def plot_diagram(ax, tc, diagram):
    for one_component in diagram.components:
        one_component.plot(ax, tc)