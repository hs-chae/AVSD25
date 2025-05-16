from .rules import *

import random

conversation_long = {
"point_1": [
    [
        "Out of labels <1>, <2>, <3>, <4>, and <5>, which one does not correspond to a point?",
        "Label <6> does not correspond to any point."
    ],
    [
        "Which of the labels <1>, <2>, <3>, <4>, and <5> is not associated with a point?",
        "Label <6> is not associated with any point."
    ],
    [
        "Among the labels <1>, <2>, <3>, <4>, and <5>, which one fails to represent a point?",
        "Label <6> fails to represent any point."
    ],
    [
        "From the labels <1>, <2>, <3>, <4>, and <5>, identify the one that does not signify a point.",
        "Label <6> does not signify any point."
    ],
    [
        "Which label, out of <1>, <2>, <3>, <4>, and <5>, is not a representation of a point?",
        "Label <6> is not a representation of any point."
    ],
    [
        "Identify the label among <1>, <2>, <3>, <4>, and <5> that does not depict a point.",
        "Label <6> does not depict any point."
    ],
    [
        "Among <1>, <2>, <3>, <4>, and <5>, which label does not correspond to a point?",
        "Label <6> does not correspond to any point."
    ],
    [
        "Which label from <1>, <2>, <3>, <4>, and <5> does not stand for a point?",
        "Label <6> does not stand for any point."
    ],
    [
        "Out of <1>, <2>, <3>, <4>, and <5>, determine the label that does not refer to a point.",
        "Label <6> does not refer to any point."
    ],
    [
        "From the labels <1>, <2>, <3>, <4>, and <5>, which one does not indicate a point?",
        "Label <6> does not indicate any point."
    ]
],

"point_2" : [
    [
        "The only point in the picture is labeled with the label right nest to it. Which label among <1>, <2>, <3>, <4>, and <5> denotes the label of the only point in the picture?",
        "Label <6> denotes the label of the only point in the picture."
    ],
    [
        "In the picture, the label of the only point is the one located right next to it. Which label among <1>, <2>, <3>, <4>, and <5> represents this point?",
        "Label <6> represents the only point in the picture."
    ],
    [
        "Out of <1>, <2>, <3>, <4>, and <5>, determine the label that refer to the only point in the given picture.",
        "Label <6> refer to the only point."
    ],
    [
        "From the labels <1>, <2>, <3>, <4>, and <5>, which one indicates a point?",
        "Label <6> indicates the point."
    ],
    [
        "Among the labels <1>, <2>, <3>, <4>, and <5>, which one represent the only point?",
        "Label <6> represent the point."
    ],
]
}
conversation_caption = {
    "point_1": [
        ["", "Out of labels <1>, <2>, <3>, <4>, and <5>, label <6> does not correspond to any point."],
        ["", "Among the labels <1>, <2>, <3>, <4>, and <5>, label <6> is not associated with any point."],
        ["", "From the labels <1>, <2>, <3>, <4>, and <5>, label <6> fails to represent any point."],
        ["", "Among the labels <1>, <2>, <3>, <4>, and <5>, label <6> does not signify any point."],
        ["", "From the labels <1>, <2>, <3>, <4>, and <5>, label <6> is not a representation of any point."],
        ["", "Among the labels <1>, <2>, <3>, <4>, and <5>, label <6> does not depict any point."],
        ["", "From the labels <1>, <2>, <3>, <4>, and <5>, label <6> does not correspond to any point."],
        ["", "Among the labels <1>, <2>, <3>, <4>, and <5>, label <6> does not stand for any point."],
        ["", "Out of labels <1>, <2>, <3>, <4>, and <5>, label <6> does not refer to any point."],
        ["", "Among the labels <1>, <2>, <3>, <4>, and <5>, label <6> does not indicate any point."]
    ],
    "point_2": [
        ["", "In the picture, the only point is labeled with the label right next to it. Among <1>, <2>, <3>, <4>, and <5>, label <6> denotes the only point in the picture."],
        ["", "In the picture, the only point is labeled with the label next to it. Among <1>, <2>, <3>, <4>, and <5>, label <6> represents the only point in the picture."],
        ["", "Out of labels <1>, <2>, <3>, <4>, and <5>, label <6> refers to the only point in the given picture."],
        ["", "Among the labels <1>, <2>, <3>, <4>, and <5>, label <6> indicates the only point."],
        ["", "Among the labels <1>, <2>, <3>, <4>, and <5>, label <6> represents the only point in the picture."]
    ]
}

conversation_short = {
"point_1": [
    [
        "Out of labels <1>, <2>, <3>, <4>, and <5>, which one does not correspond to a point?", 
        "<6>"
    ],
    [
        "Which of the labels <1>, <2>, <3>, <4>, and <5> is not associated with a point?", 
        "<6>"
    ],
    [
        "Among the labels <1>, <2>, <3>, <4>, and <5>, which one fails to represent a point?", 
        "<6>"
    ],
    [
        "From the labels <1>, <2>, <3>, <4>, and <5>, identify the one that does not signify a point.", 
        "<6>"
    ],
    [
        "Which label, out of <1>, <2>, <3>, <4>, and <5>, is not a representation of a point?", 
        "<6>"
    ],
    [
        "Identify the label among <1>, <2>, <3>, <4>, and <5> that does not depict a point.", 
        "<6>"
    ],
    [
        "Among <1>, <2>, <3>, <4>, and <5>, which label does not correspond to a point?", 
        "<6>"
    ],
    [
        "Which label from <1>, <2>, <3>, <4>, and <5> does not stand for a point?", 
        "<6>"
    ],
    [
        "Out of <1>, <2>, <3>, <4>, and <5>, determine the label that does not refer to a point.", 
        "<6>"
    ],
    [
        "From the labels <1>, <2>, <3>, <4>, and <5>, which one does not indicate a point?", 
        "<6>"
    ]
],

"point_2": [
    [
        "The only point in the picture is labeled with the label right nest to it. Which label among <1>, <2>, <3>, <4>, and <5> denotes the label of the only point in the picture?",
        "<6>"
    ],
    [
        "In the picture, the label of the only point is the one located right next to it. Which label among <1>, <2>, <3>, <4>, and <5> represents this point?",
        "<6>"
    ],
    [
        "Out of <1>, <2>, <3>, <4>, and <5>, determine the label that refer to the only point in the given picture.",
        "<6>"
    ],
    [
        "From the labels <1>, <2>, <3>, <4>, and <5>, which one indicates a point?",
        "<6>"
    ],
    [
        "Among the labels <1>, <2>, <3>, <4>, and <5>, which one represent the only point?",
        "<6>"
    ]
]

}

alphabets = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
numbers = set(list('0123456789'))

def generate_qa (entity, long=False, caption=False):

    rule            = entity[0] 
    inputs          = entity[1]
    if caption : 
        conversation = conversation_caption[rule]
    else : 
        conversation = conversation_long[rule] if long else conversation_short[rule]
    question, answer = random.choice ( conversation )
    for i in range(len(inputs)) : 
        question = question.replace(f'<{i+1}>', inputs[i])
        answer   = answer.replace(f'<{i+1}>', inputs[i])
    return question, answer

def generate_conversation(diagram, long=False, caption=False):
    conversation_list = []
    for entity in diagram.entities:
        conversation_list.append(generate_qa(entity, long, caption))
            
    return conversation_list