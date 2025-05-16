from .rules import *
import copy

def plot_diagram(ax, tc, diagram, set_visible = True):
    for one_component in diagram.components:
        one_component.plot(ax, tc, set_visible = set_visible)
    ax.axis('equal')

def copy_plot_diagram(ax, tc, diagram, set_visible = True):
    for one_component in diagram.components:
        new_component = copy.deepcopy(one_component)
        try:
            new_component.update_patch()
        except:
            pass
        finally:
            new_component.plot(ax, tc, set_visible = set_visible)
