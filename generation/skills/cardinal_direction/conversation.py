from .rules import *

conversation_long = {
    "cardinal_direction_dir_horizontal": [
        [
            "Which side of the <2> <4> is the <1> <3> located, left or right?",
            "The <1> <3> is located on the <5> side of the <2> <4>."
        ],
        [
            "Is the <1> <3> located on the <5> side of the <2> <4>?",
            "Yes, the <1> <3> is located on the <5> side of the <2> <4>."
        ],
        [
            "Is the <1> <3> located on the <-5> side of the <2> <4>?",
            "No, the <1> <3> is located on the <5> side of the <2> <4>."
        ],
        [
            "The <1> <3> is located on the (left/right) side of the <2> <4>.",
            "The <1> <3> is located on the <5> side of the <2> <4>."
        ]
    ],
    "cardinal_direction_dir_horizontal_colored": [
        [
            "Which side of the <2> <4> is the <1> <3> located, left or right?",
            "The <1> <3> is located on the <5> side of the <2> <4>."
        ],
        [
            "Is the <1> <3> located on the <5> side of the <2> <4>?",
            "Yes, the <1> <3> is located on the <5> side of the <2> <4>."
        ],
        [
            "Is the <1> <3> located on the <-5> side of the <2> <4>?",
            "No, the <1> <3> is located on the <5> side of the <2> <4>."
        ],
        [
            "The <1> <3> is located on the (left/right) side of the <2> <4>.",
            "The <1> <3> is located on the <5> side of the <2> <4>."
        ],
        [
            "Which side of the <8> <2> is the <7> <1> located, left or right?",
            "The <7> <1> is located on the <5> side of the <8> <2>."
        ],
        [
            "Is the <7> <1> located on the <5> side of the <8> <2>?",
            "Yes, the <7> <1> is located on the <5> side of the <8> <2>."
        ],
        [
            "Is the <7> <1> located on the <-5> side of the <8> <2>?",
            "No, the <7> <1> is located on the <5> side of the <8> <2>."
        ],
        [
            "The <7> <1> is located on the (left/right) side of the <8> <2>.",
            "The <7> <1> is located on the <5> side of the <8> <2>."
        ]
    ],
    "cardinal_direction_dir_vertical": [
        [
            "Which side of the <2> <4> is the <1> <3> located, top or bottom?",
            "The <1> <3> is located on the <6> side of the <2> <4>."
        ],
        [
            "Is the <1> <3> located on the <6> side of the <2> <4>?",
            "Yes, the <1> <3> is located on the <6> side of the <2> <4>."
        ],
        [
            "Is the <1> <3> located on the <-6> side of the <2> <4>?",
            "No, the <1> <3> is located on the <6> side of the <2> <4>."
        ],
        [
            "The <1> <3> is located on the (top/bottom) side of the <2> <4>.",
            "The <1> <3> is located on the <6> side of the <2> <4>."
        ]
    ],
    "cardinal_direction_dir_vertical_colored": [
        [
            "Which side of the <2> <4> is the <1> <3> located, top or bottom?",
            "The <1> <3> is located on the <6> side of the <2> <4>."
        ],
        [
            "Is the <1> <3> located on the <6> side of the <2> <4>?",
            "Yes, the <1> <3> is located on the <6> side of the <2> <4>."
        ],
        [
            "Is the <1> <3> located on the <-6> side of the <2> <4>?",
            "No, the <1> <3> is located on the <6> side of the <2> <4>."
        ],
        [
            "The <1> <3> is located on the (top/bottom) side of the <2> <4>.",
            "The <1> <3> is located on the <6> side of the <2> <4>."
        ],
        [
            "Which side of the <8> <2> is the <7> <1> located, top or bottom?",
            "The <7> <1> is located on the <6> side of the <8> <2>."
        ],
        [
            "Is the <7> <1> located on the <6> side of the <8> <2>?",
            "Yes, the <7> <1> is located on the <6> side of the <8> <2>."
        ],
        [
            "Is the <7> <1> located on the <-6> side of the <8> <2>?",
            "No, the <7> <1> is located on the <6> side of the <8> <2>."
        ],
        [
            "The <7> <1> is located on the (top/bottom) side of the <8> <2>.",
            "The <7> <1> is located on the <6> side of the <8> <2>."
        ]
    ],
    "cardinal_direction_dir_both": [
        [
            "Which side of the <2> <4> is the <1> <3> located, top right, top left, bottom right, or bottom left?",
            "The <1> <3> is located on the <6> <5> side of the <2> <4>."
        ],
        [
            "The <1> <3> is located on the (top right/top left/bottom right/bottom left) side of the <2> <4>.",
            "The <1> <3> is located on the <6> <5> side of the <2> <4>."
        ]
    ],
    "cardinal_direction_dir_both_colored": [
        [
            "Which side of the <2> <4> is the <1> <3> located, top right, top left, bottom right, or bottom left?",
            "The <1> <3> is located on the <6> <5> side of the <2> <4>."
        ],
        [
            "The <1> <3> is located on the (top right/top left/bottom right/bottom left) side of the <2> <4>.",
            "The <1> <3> is located on the <6> <5> side of the <2> <4>."
        ],
        [
            "Which side of the <8> <2> is the <7> <1> located, top right, top left, bottom right, or bottom left?",
            "The <7> <1> is located on the <6> <5> side of the <8> <2>."
        ],
        [
            "The <7> <1> is located on the (top right/top left/bottom right/bottom left) side of the <8> <2>.",
            "The <7> <1> is located on the <6> <5> side of the <8> <2>."
        ]
    ],
    "cardinal_direction_obj_horizontal": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <5> side of the other?",
            "<1> <3> is located on the <5> side of <2> <4>."
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <5> side of the other.",
            "Between <1> <3> and <2> <4>, <1> <3> is located on the <5> side of the other."
        ]
    ],
    "cardinal_direction_obj_horizontal_colored": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <5> side of the other?",
            "<1> <3> is located on the <5> side of <2> <4>."
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <5> side of the other.",
            "Between <1> <3> and <2> <4>, <1> <3> is located on the <5> side of the other."
        ],
        [
            "Between <7> <1> and <8> <2>, which one is located on the <5> side of the other?",
            "<7> <1> is located on the <5> side of <8> <2>."
        ],
        [
            "Between <7> <1> and <8> <2>, (<7> <1>/<8> <2>) is located on the <5> side of the other.",
            "Between <7> <1> and <8> <2>, <7> <1> is located on the <5> side of the other."
        ]
    ],
    "cardinal_direction_obj_vertical": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <6> side of the other?",
            "<1> <3> is located on the <6> side of <2> <4>."
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <6> side of the other.",
            "Between <1> <3> and <2> <4>, <1> <3> is located on the <6> side of the other."
        ]
    ],
    "cardinal_direction_obj_vertical_colored": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <6> side of the other?",
            "<1> <3> is located on the <6> side of <2> <4>."
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <6> side of the other.",
            "Between <1> <3> and <2> <4>, <1> <3> is located on the <6> side of the other."
        ],
        [
            "Between <7> <1> and <8> <2>, which one is located on the <6> side of the other?",
            "<7> <1> is located on the <6> side of <8> <2>."
        ],
        [
            "Between <7> <1> and <8> <2>, (<7> <1>/<8> <2>) is located on the <6> side of the other.",
            "Between <7> <1> and <8> <2>, <7> <1> is located on the <6> side of the other."
        ]
    ],
    "cardinal_direction_obj_both": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <6> <5> side of the other?",
            "<1> <3> is located on the <6> <5> side of <2> <4>."
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <6> <5> side of the other.",
            "Between <1> <3> and <2> <4>, <1> <3> is located on the <6> <5> side of the other."
        ]
    ],
    "cardinal_direction_obj_both_colored": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <6> <5> side of the other?",
            "<1> <3> is located on the <6> <5> side of <2> <4>."
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <6> <5> side of the other.",
            "Between <1> <3> and <2> <4>, <1> <3> is located on the <6> <5> side of the other."
        ],
        [
            "Between <7> <1> and <8> <2>, which one is located on the <6> <5> side of the other?",
            "<7> <1> is located on the <6> <5> side of <8> <2>."
        ],
        [
            "Between <7> <1> and <8> <2>, (<7> <1>/<8> <2>) is located on the <6> <5> side of the other.",
            "Between <7> <1> and <8> <2>, <7> <1> is located on the <6> <5> side of the other."
        ]
    ]
}

conversation_short = {
    "cardinal_direction_dir_horizontal": [
        [
            "Which side of the <2> <4> is the <1> <3> located, left or right?",
            "<5>"
        ],
        [
            "Is the <1> <3> located on the <5> side of the <2> <4>?",
            "Yes"
        ],
        [
            "Is the <1> <3> located on the <-5> side of the <2> <4>?",
            "No"
        ],
        [
            "The <1> <3> is located on the (left/right) side of the <2> <4>.",
            "<5>"
        ]
    ],
    "cardinal_direction_dir_horizontal_colored": [
        [
            "Which side of the <2> <4> is the <1> <3> located, left or right?",
            "<5>"
        ],
        [
            "Is the <1> <3> located on the <5> side of the <2> <4>?",
            "Yes"
        ],
        [
            "Is the <1> <3> located on the <-5> side of the <2> <4>?",
            "No"
        ],
        [
            "The <1> <3> is located on the (left/right) side of the <2> <4>.",
            "<5>"
        ],
        [
            "Which side of the <8> <2> is the <7> <1> located, left or right?",
            "<5>"
        ],
        [
            "Is the <7> <1> located on the <5> side of the <8> <2>?",
            "Yes"
        ],
        [
            "Is the <7> <1> located on the <-5> side of the <8> <2>?",
            "No"
        ],
        [
            "The <7> <1> is located on the (left/right) side of the <8> <2>.",
            "<5>"
        ]
    ],
    "cardinal_direction_dir_vertical": [
        [
            "Which side of the <2> <4> is the <1> <3> located, top or bottom?",
            "<6>"
        ],
        [
            "Is the <1> <3> located on the <6> side of the <2> <4>?",
            "Yes"
        ],
        [
            "Is the <1> <3> located on the <-6> side of the <2> <4>?",
            "No"
        ],
        [
            "The <1> <3> is located on the (top/bottom) side of the <2> <4>.",
            "<6>"
        ]
    ],
    "cardinal_direction_dir_vertical_colored": [
        [
            "Which side of the <2> <4> is the <1> <3> located, top or bottom?",
            "<6>"
        ],
        [
            "Is the <1> <3> located on the <6> side of the <2> <4>?",
            "Yes"
        ],
        [
            "Is the <1> <3> located on the <-6> side of the <2> <4>?",
            "No"
        ],
        [
            "The <1> <3> is located on the (top/bottom) side of the <2> <4>.",
            "<6>"
        ],
        [
            "Which side of the <8> <2> is the <7> <1> located, top or bottom?",
            "<6>"
        ],
        [
            "Is the <7> <1> located on the <6> side of the <8> <2>?",
            "Yes"
        ],
        [
            "Is the <7> <1> located on the <-6> side of the <8> <2>?",
            "No"
        ],
        [
            "The <7> <1> is located on the (top/bottom) side of the <8> <2>.",
            "<6>"
        ]
    ],
    "cardinal_direction_dir_both": [
        [
            "Which side of the <2> <4> is the <1> <3> located, top right, top left, bottom right, or bottom left?",
            "<6> <5>"
        ],
        [
            "The <1> <3> is located on the (top right/top left/bottom right/bottom left) side of the <2> <4>.",
            "<6> <5>"
        ]
    ],
    "cardinal_direction_dir_both_colored": [
        [
            "Which side of the <2> <4> is the <1> <3> located, top right, top left, bottom right, or bottom left?",
            "<6> <5>"
        ],
        [
            "The <1> <3> is located on the (top right/top left/bottom right/bottom left) side of the <2> <4>.",
            "<6> <5>"
        ],
        [
            "Which side of the <8> <2> is the <7> <1> located, top right, top left, bottom right, or bottom left?",
            "<6> <5>"
        ],
        [
            "The <7> <1> is located on the (top right/top left/bottom right/bottom left) side of the <8> <2>.",
            "<6> <5>"
        ]
    ],
    "cardinal_direction_obj_horizontal": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <5> side of the other?",
            "<1> <3>"
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <5> side of the other.",
            "<1> <3>"
        ]
    ],
    "cardinal_direction_obj_horizontal_colored": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <5> side of the other?",
            "<1> <3>"
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <5> side of the other.",
            "<1> <3>"
        ],
        [
            "Between <7> <1> and <8> <2>, which one is located on the <5> side of the other?",
            "<7> <1>"
        ],
        [
            "Between <7> <1> and <8> <2>, (<7> <1>/<8> <2>) is located on the <5> side of the other.",
            "<7> <1>"
        ]
    ],
    "cardinal_direction_obj_vertical": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <6> side of the other?",
            "<1> <3>"
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <6> side of the other.",
            "<1> <3>"
        ]
    ],
    "cardinal_direction_obj_vertical_colored": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <6> side of the other?",
            "<1> <3>"
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <6> side of the other.",
            "<1> <3>"
        ],
        [
            "Between <7> <1> and <8> <2>, which one is located on the <6> side of the other?",
            "<7> <1>"
        ],
        [
            "Between <7> <1> and <8> <2>, (<7> <1>/<8> <2>) is located on the <6> side of the other.",
            "<7> <1>"
        ]
    ],
    "cardinal_direction_obj_both": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <6> <5> side of the other?",
            "<1> <3>"
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <6> <5> side of the other.",
            "<1> <3>"
        ]
    ],
    "cardinal_direction_obj_both_colored": [
        [
            "Between <1> <3> and <2> <4>, which one is located on the <6> <5> side of the other?",
            "<1> <3>"
        ],
        [
            "Between <1> <3> and <2> <4>, (<1> <3>/<2> <4>) is located on the <6> <5> side of the other.",
            "<1> <3>"
        ],
        [
            "Between <7> <1> and <8> <2>, which one is located on the <6> <5> side of the other?",
            "<7> <1>"
        ],
        [
            "Between <7> <1> and <8> <2>, (<7> <1>/<8> <2>) is located on the <6> <5> side of the other.",
            "<7> <1>"
        ]
    ]
}

def generate_cardinal_direction(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    # find conversation with keyword
    if entity[1][6] is None:
        keyword = entity[0]
    else:
        keyword = entity[0] + "_colored"

    index = random.randint(0, len(conversation[keyword]) - 1)
    q, a = conversation[keyword][index]

    # replace <1>, <2>, ... with the actual values
    for i in range(len(entity[1])):
        if entity[1][i] is None:
            continue
        q = q.replace(f"<{i+1}>", entity[1][i])
        a = a.replace(f"<{i+1}>", entity[1][i])
    
    opposite ={
        "left": "right",
        "right": "left",
        "top": "bottom",
        "bottom": "top"
    }

    # replace <-1>, <-2>, ... with the opposite values
    for i in range(len(entity[1])):
        if entity[1][i] is None:
            continue
        if entity[1][i] in opposite:
            q = q.replace(f"<-{i+1}>", opposite[entity[1][i]])
            a = a.replace(f"<-{i+1}>", opposite[entity[1][i]])
        else:
            q = q.replace(f"<-{i+1}>", entity[1][i])
            a = a.replace(f"<-{i+1}>", entity[1][i])

    return q, a


def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        if "cardinal_direction" in entity[0]:
            conversation_list.append(generate_cardinal_direction(entity, long))
        break
    return conversation_list
