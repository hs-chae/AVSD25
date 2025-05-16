import inspect
from .rule_list import *
from .rules import *


def skill_tree(diagram : Diagram):
    rule_name = random.choice(skill_rules)
    # print("Rule : " + rule_name)
    diagram = eval(rule_name)(diagram)
    diagram.steps.append(rule_name)
        # except:
        #     print("step failed with rule: ", rule_name)
    return diagram
