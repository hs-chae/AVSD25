from .rules import *
import copy

def plot_diagram(ax, tc, diagram, set_visible = True):
    for one_element in diagram.components:
        idx, one_component = one_element
        one_component.plot(idx, ax, tc, set_visible = set_visible)

def copy_plot_diagram(ax, tc, diagram, set_visible = True):
    for one_element in diagram.components:
        idx, one_component = one_element
        new_component = copy.deepcopy(one_component)
        try:
            new_component.update_patch()
        except:
            pass
        finally:
            new_component.plot(idx, ax, tc, set_visible = set_visible)