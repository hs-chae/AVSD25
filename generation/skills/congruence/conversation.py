from .rules import *
import random

from .rules import *
import random

conversation = {
    "conversation_long": {
        "congruence1": {
            "QA": [
                [
                    "The figure shows two <1>. Are these figures congruent or not?",
                    "Yes, the two <1> are congruent."
                ],
                [
                    "Two <1> are depicted in the figure. Are they congruent, or not?",
                    "It appears that the two <1> are congruent."
                ],
                [
                    "In the figure, we have two <1>. Do you think they are congruent or not?",
                    "In fact, the two <1> are congruent."
                ],
                [
                    "We have two <1> provided in the figure. Are those shapes congruent or not?",
                    "We confirm that the two <1> are congruent."
                ],
                [
                    "There are two <1> in the diagram. Are they congruent or not?",
                    "Undoubtedly, the two <1> are congruent."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    [
                        "Select one word from the parentheses to complete the sentence. The given two <1> are (congruent/not congruent).",
                        "The given two <1> are congruent."
                    ],
                    [
                        "Please choose the correct option from the parentheses to finalize the sentence: The given two <1> are (congruent/not congruent).",
                        "It turns out the two <1> are congruent."
                    ],
                    [
                        "Pick the appropriate phrase from the parentheses to finish the sentence. The two <1> are (congruent/not congruent).",
                        "We conclude that the two <1> are congruent."
                    ],
                    [
                        "Complete the sentence by selecting one choice from the parentheses: The given two <1> are (congruent/not congruent).",
                        "Yes, indeed, the two <1> are congruent."
                    ],
                    [
                        "From the parentheses, choose the correct term to complete the sentence: The two <1> are (congruent/not congruent).",
                        "Hence, the two <1> are congruent."
                    ]
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    ""
                ]
            }
        },
        "congruence2": {
            "QA": [
                [
                    "The figure shows two <1>. Are these figures congruent or not?",
                    "No, the two <1> are not congruent."
                ],
                [
                    "Two <1> are depicted in the diagram. Do they appear to be congruent or not?",
                    "It appears that the two <1> are not congruent."
                ],
                [
                    "In the figure, we have two <1>. Are they congruent or not?",
                    "These two <1> are not congruent."
                ],
                [
                    "We have two <1> in the illustration. Do you think they are congruent or not?",
                    "We see that the two <1> are not congruent."
                ],
                [
                    "There are two <1> in the figure. Are they congruent, or not?",
                    "Indeed, the two <1> are not congruent."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    [
                        "Select one word from the parentheses to complete the sentence. The given two <1> are (congruent/not congruent).",
                        "The given two <1> are not congruent."
                    ],
                    [
                        "Please choose the correct option from the parentheses to finish the sentence: The two <1> are (congruent/not congruent).",
                        "It turns out the two <1> are not congruent."
                    ],
                    [
                        "Pick the phrase from the parentheses to conclude the sentence. The given two <1> are (congruent/not congruent).",
                        "We conclude that the two <1> are not congruent."
                    ],
                    [
                        "Complete the sentence by selecting one of the options in parentheses: The two <1> are (congruent/not congruent).",
                        "Yes, indeed, the two <1> are not congruent."
                    ],
                    [
                        "From the parentheses, choose the correct term to finalize the sentence: The two <1> are (congruent/not congruent).",
                        "Hence, the two <1> are not congruent."
                    ]
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    ""
                ]
            }
        },
        "congruence3": {
            "QA": [
                [
                    "There are two congruent <1> in the figure. Which side corresponds to side <2>?",
                    "The side corresponding to <2> is <5>."
                ],
                [
                    "In this figure, we have two congruent <1>. Identify the side that matches <2>.",
                    "Side <2> matches <5>."
                ],
                [
                    "The figure depicts a pair of congruent <1>. Which side is paired with <2>?",
                    "The corresponding side for <2> is <5>."
                ],
                [
                    "We can see two congruent <1> in the diagram. Determine the side corresponding to <2>.",
                    "The side for <2> is <5>."
                ],
                [
                    "Given two congruent <1> in the illustration, what is the matching side for <2>?",
                    "The matching side to <2> is <5>."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    [
                        "Select one word from the parentheses to complete the sentence. The side <2> corresponds to (<3>).",
                        "The side <2> corresponds to <5>."
                    ],
                    [
                        "Choose the correct phrase from the parentheses. The corresponding side for <2> is (<3>).",
                        "The corresponding side for <2> is <5>."
                    ],
                    [
                        "Pick one option from the parentheses to finish the sentence. Side <2> matches (<3>).",
                        "Side <2> matches <5>."
                    ],
                    [
                        "Complete the statement by selecting from the parentheses: The side that corresponds to <2> is (<3>).",
                        "The side that corresponds to <2> is <5>."
                    ],
                    [
                        "From the parentheses, choose the side that pairs with <2>. That side is (<3>).",
                        "That side pairing with <2> is <5>."
                    ]
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "The answer must be selected from <4>.",
                    "You need to pick the correct choice from <4>.",
                    "The correct side should be chosen from <4>.",
                    "Please select the correct option from <4>.",
                    "Determine the correct side from <4>."
                ]
            }
        },
        "congruence4": {
            "QA": [
                [
                    "There are two congruent <1> in the figure. Which vertex corresponds to vertex <2>?",
                    "The vertex corresponding to <2> is <5>."
                ],
                [
                    "In this diagram, we have two congruent <1>. Identify the vertex that matches <2>.",
                    "The matching vertex for <2> is <5>."
                ],
                [
                    "Observe the two congruent <1> in the figure. Which vertex pairs with <2>?",
                    "The vertex paired with <2> is <5>."
                ],
                [
                    "We see two congruent <1> in the illustration. Determine the vertex corresponding to <2>.",
                    "The vertex that corresponds to <2> is <5>."
                ],
                [
                    "Given two congruent <1> in the figure, find the vertex that matches <2>.",
                    "The vertex matching <2> is <5>."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    [
                        "Select one word from the parentheses to complete the sentence. The vertex <2> corresponds to (<3>).",
                        "The vertex <2> corresponds to <5>."
                    ],
                    [
                        "Choose the correct option in parentheses. The vertex matching <2> is (<3>).",
                        "The vertex matching <2> is <5>."
                    ],
                    [
                        "Pick the phrase from the parentheses to finish the sentence: Vertex <2> pairs with (<3>).",
                        "Vertex <2> pairs with <5>."
                    ],
                    [
                        "Complete the statement by selecting from the parentheses: Vertex <2> corresponds to (<3>).",
                        "Vertex <2> corresponds to <5>."
                    ],
                    [
                        "From the parentheses, choose the vertex that aligns with <2>. That vertex is (<3>).",
                        "That vertex aligning with <2> is <5>."
                    ]
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "You must choose the correct vertex from <4>.",
                    "Please select the correct vertex from <4>.",
                    "The answer must be picked out of <4>.",
                    "Determine the right vertex from <4>.",
                    "Choose the vertex from <4>."
                ]
            }
        }
    
    },
    "conversation_short": {
        "congruence1": {
            "QA": [
                [
                    "Are the two <1> shown in the figure congruent or not?",
                    "congruent"
                ],
                [
                    "Two <1> are provided. Are they congruent or not?",
                    "congruent"
                ],
                [
                    "In the figure, we see two <1>. Are these <1> congruent?",
                    "congruent"
                ],
                [
                    "Check whether the two <1> in the diagram are congruent or not.",
                    "congruent"
                ],
                [
                    "Determine if the two <1> are congruent or not.",
                    "congruent"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    "Select one word from the parentheses to complete the sentence. The given two <1> are (congruent/not congruent).",
                    "Please choose from the parentheses: The two <1> are (congruent/not congruent).",
                    "Pick the correct phrase: The given two <1> are (congruent/not congruent).",
                    "Complete the sentence by selecting an option: The two <1> are (congruent/not congruent).",
                    "Choose the right term for the sentence: The two <1> are (congruent/not congruent)."
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    ""
                ]
            }
        },
        "congruence2": {
            "QA": [
                [
                    "Are the two <1> in the figure congruent or not?",
                    "not congruent"
                ],
                [
                    "Two <1> are depicted. Are they congruent or not?",
                    "not congruent"
                ],
                [
                    "In this figure, do the two <1> appear congruent?",
                    "not congruent"
                ],
                [
                    "Check if the two <1> illustrated here are congruent or not.",
                    "not congruent"
                ],
                [
                    "Determine whether these two <1> are congruent or not.",
                    "not congruent"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    "Select one word from the parentheses to complete the sentence. The given two <1> are (congruent/not congruent).",
                    "Please choose from the parentheses: The two <1> are (congruent/not congruent).",
                    "Pick the correct phrase: The given two <1> are (congruent/not congruent).",
                    "Complete the sentence by selecting an option: The two <1> are (congruent/not congruent).",
                    "Choose the right term for the sentence: The two <1> are (congruent/not congruent)."
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    ""
                ]
            }
        },
        "congruence3": {
            "QA": [
                [
                    "Two congruent <1> are shown. Which side corresponds to <2>?",
                    "<5>"
                ],
                [
                    "In the figure, we have congruent <1>. Identify the corresponding side of <2>.",
                    "<5>"
                ],
                [
                    "Here are two congruent <1>. Which side matches <2>?",
                    "<5>"
                ],
                [
                    "Observe the two congruent <1>. Find the side that corresponds to <2>.",
                    "<5>"
                ],
                [
                    "There are two congruent <1> in the diagram. Which side is paired with <2>?",
                    "<5>"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    "Select one word from the parentheses to complete the sentence. The side <2> corresponds to (<3>).",
                    "Choose the correct phrase: Side <2> is (<3>).",
                    "Pick one option from the parentheses to complete: <2> matches (<3>).",
                    "Complete the statement: The side for <2> is (<3>).",
                    "From the parentheses, decide which side pairs with <2>: (<3>)."
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "The answer must be selected from <4>.",
                    "You need to pick the correct choice from <4>.",
                    "The correct side should be chosen from <4>.",
                    "Please select the correct option from <4>.",
                    "Determine the correct side from <4>."
                ]
            }
        },
        "congruence4": {
            "QA": [
                [
                    "Two congruent <1> are shown. Which vertex corresponds to <2>?",
                    "<5>"
                ],
                [
                    "In this figure, which vertex of the congruent <1> matches <2>?",
                    "<5>"
                ],
                [
                    "Observe the two congruent <1>. Identify the vertex corresponding to <2>.",
                    "<5>"
                ],
                [
                    "We see two congruent <1>. Which vertex pairs with <2>?",
                    "<5>"
                ],
                [
                    "There are two congruent <1>. Find the vertex that matches <2>.",
                    "<5>"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    "Select one word from the parentheses to complete the sentence. The vertex <2> corresponds to (<3>).",
                    "Choose the correct option: Vertex <2> is (<3>).",
                    "Pick the right term from parentheses for vertex <2>: (<3>).",
                    "Complete this sentence: Vertex <2> pairs with (<3>).",
                    "From the parentheses, decide which vertex matches <2>: (<3>)."
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "You must choose the correct vertex from <4>.",
                    "Please select the correct vertex from <4>.",
                    "The answer must be picked out of <4>.",
                    "Determine the right vertex from <4>.",
                    "Choose the vertex from <4>."
                ]
            }
        }
    }
}

def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        version_key = entity[0]
        if long:
            conversation_extracted = conversation['conversation_long']
        else:
            conversation_extracted = conversation['conversation_short']
        qa = random.choice(conversation_extracted[version_key]['QA'])
        additional = conversation_extracted[version_key]['additional']
        additional_type = []
        if additional['type1'] == ['True']:
            additional_type.append('type1')
        for candidate in ['type2', 'type3', 'type4']:
            if additional[candidate] != [""]:
                additional_type.append(candidate)
        additional_type = random.choice(additional_type)
        if additional_type != 'type1':
            if long:
                if additional_type == 'type2':
                    random_idx = random.randint(0, len(additional[additional_type])-1)
                    qa[0] = qa[0] + " "+ additional[additional_type][random_idx][0]
                    qa[1] = additional[additional_type][random_idx][1]
                else:
                    qa[0] = qa[0] + " "+ random.choice(additional[additional_type])
            else:
                qa[0] = qa[0] + " "+ random.choice(additional[additional_type])
        q = qa[0]
        a = qa[1]
        for i in range(0, len(entity[1])):
            q = q.replace(f"<{i+1}>", entity[1][i])
            a = a.replace(f"<{i+1}>", entity[1][i])
        conversation_list.append((q, a))
    return conversation_list

def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        version_key = entity[0]
        if long:
            conversation_extracted = conversation['conversation_long']
        else:
            conversation_extracted = conversation['conversation_short']
        qa = random.choice(conversation_extracted[version_key]['QA'])
        additional = conversation_extracted[version_key]['additional']
        additional_type = []
        if additional['type1'] == ['True']:
            additional_type.append('type1')
        for candidate in ['type2', 'type3', 'type4']:
            if additional[candidate] != [""]:
                additional_type.append(candidate)
        additional_type = random.choice(additional_type)
        if additional_type != 'type1':
            if long:
                if additional_type == 'type2':
                    random_idx = random.randint(0, len(additional[additional_type])-1)
                    qa[0] = qa[0] + " "+ additional[additional_type][random_idx][0]
                    qa[1] = additional[additional_type][random_idx][1]
                else:
                    qa[0] = qa[0] + " "+ random.choice(additional[additional_type])
            else:
                if additional_type == 'type2':
                    random_idx = random.randint(0, len(additional[additional_type])-1)
                    qa[0] = qa[0] + " "+ additional[additional_type][random_idx][0]
                else:
                    qa[0] = qa[0] + " "+ random.choice(additional[additional_type])
        q = qa[0]
        a = qa[1]
        for i in range(0, len(entity[1])):
            q = q.replace(f"<{i+1}>", entity[1][i])
            a = a.replace(f"<{i+1}>", entity[1][i])
        conversation_list.append((q, a))
    return conversation_list