import inspect
from .rule_list import *
from .a2_rules import *


def length_tree(diagram : Diagram):
    rule_name = random.choice(length_rules)
    # print("Rule : " + rule_name)
    diagram = eval(rule_name)(diagram)
    diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram


def C_angle_tree(diagram : Diagram):
    if len(diagram.points) > 7 :
        rule_name = random.choice(angle_only_rules)
    else:
        rule_name = random.choice(color_angle_rules)
    # print("Rule : " + rule_name)
    diagram = eval(rule_name)(diagram)
    diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram

def C_parallel_tree(diagram : Diagram):
    rule_name = random.choice(color_parallel_rules)
    # print("Rule : " + rule_name)
    diagram = eval(rule_name)(diagram)
    diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram

def C_length_tree(diagram : Diagram):
    rule_name = random.choice(color_length_rules)
    # print("Rule : " + rule_name)
    diagram = eval(rule_name)(diagram)
    diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram

def a2_tree(diagram : Diagram):
    rule_name = random.choice(a2_rules)
    # if len(diagram.points) == 0 and  len(diagram.lines) == 0 and len(diagram.circles) == 0 and len(diagram.curves) == 0:
    #     diagram = random.choice([add_free_line,add_free_circle,add_free_point])(diagram)
    diagram = eval(rule_name)(diagram)
    diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram
