import inspect
from .rule_list import *
from .parallel_rules import *


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
    if len(diagram.points) > 7 :
        rule_name = random.choice(length_only_rules)
    rule_name = random.choice(color_length_rules)
    # print("Rule : " + rule_name)
    diagram = eval(rule_name)(diagram)
    diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram
