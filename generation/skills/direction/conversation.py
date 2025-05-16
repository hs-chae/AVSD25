from .rules import *

conversation_long = {
    "direction1": [
        [
            "There are <1> arrows scattered on the given image. Find the arrow that has most different direction from the others.",
            "The arrow <2> has most different direction from the others."
        ],
        [
            "Among <1> arrows in the diagram, which one is directing to the most distinctive direction?",
            "The arrow <2> is directing to the most distinctive direction."
        ],
        [
            "Choose the arrow in the picture with distinct direction from the others.",
            "My choice is the arrow <2>. It has the most different direction from the others."
        ],
        [
            "Which arrow is point to the different direction? Choose the arrow from the image and tell me the label of the arrow.",
            "The arrow <2> is pointing to the different direction."
        ]
    ],
    "direction2": [
        [
            "There is an arrow in the image. What is the direction of the arrow?",
            "It is directed to the <2>."
        ],
        [
            "What is the direction of the arrow in the diagram?",
            "The arrow is directed to the <2>."
        ],
        [
            "Where is the arrow in the image pointing to? Choose your answer from the following options: <1>.",
            "The arrow is pointing to the <2>."
        ],
        [
            "See the arrow in the diagram. What is the direction of the arrow?",
            "The arrow is directed to the <2>."
        ],
        [
            "The arrow in the image is pointing to the <2>. Is it correct?",
            "Yes, the arrow is pointing to the <2>."
        ],
        [
            "The arrow in the diagram is pointing to the <3>. Is it correct?",
            "No, the arrow is pointing to the <2>."
        ]
    ],
    "direction3": [
        [
            "Among <1> arrows in the diagram, which one is directing to the <2>?",
            "The arrow <3> is directing to the <2>."
        ],
        [
            "Choose the arrow in the picture that is pointing to the <2>.",
            "The answer is the arrow <3>. It is pointing to the <2>."
        ],
        [
            "Which arrow is pointing to the <2>? Choose the arrow from <1> options in the image and tell me the label of the arrow.",
            "The arrow that is pointing to the <2> is the arrow <3>."
        ],
        [
            "<1> arrows are drawn on the given image. Find the arrow that is pointing to the <2>.",
            "The arrow <3> is pointing to the <2>."
        ]
    ],
    "direction4": [
        [
            "You can see an arrow at the center of the image. What is that arrow pointing to?",
            "The arrow is pointing to the <1> <2>."
        ],
        [
            "Tell me the <1> that an arrow is pointing to in the diagram.",
            "The arrow is pointing to the <1> <2>."
        ],
        [
            "What <1> is pointed by the arrow in the image?",
            "The <1> <2> is pointed by the arrow."
        ],
        [
            "The arrow at the center is directing to the <1> <2>. Tell me whether the statement is correct or not.",
            "It is correct. The arrow is pointing to the <1> <2>."
        ],
        [
            "The arrow at the center is pointing to the <1> <3>. Tell me whether the statement is correct or not.",
            "It is wrong. The arrow is pointing to the <1> <2>."
        ]
    ],
    "direction5": [
        [
            "In the image, there is a two-headed arrow. What are the two <1>s that the arrow is pointing to?",
            "The arrow is pointing to the <1> <2> and the <1> <3>."
        ],
        [
            "Tell me the <1>s that the two-headed arrow is pointing to in the diagram.",
            "The arrow is pointing to the <1> <2> and the <1> <3>."
        ],
        [
            "What <1>s are pointed by the two-headed arrow in the image?",
            "The <1> <2> and the <1> <3> are pointed by the arrow."
        ],
        [
            "Choose the correct <1>s that the two-headed arrow is pointing to in the image.",
            "The <1> <2> and the <1> <3>."
        ],
        [
            "By looking at the end points of the two-headed arrow, tell me the <1>s that the arrow is pointing to.",
            "The arrow is pointing to the <1> <2> and the <1> <3>."
        ]
    ],
    "direction6": [
        [
            "You can see an arrow in the image. What is that arrow pointing to?",
            "The arrow is pointing to the <1> <2>."
        ],
        [
            "Tell me the <1> that an arrow is pointing to in the diagram.",
            "The arrow is pointing to the <1> <2>."
        ],
        [
            "What <1> is pointed by the arrow in the image?",
            "The <1> <2> is pointed by the arrow."
        ],
        [
            "The arrow in the image is directing to the <1> <2>. Tell me whether the statement is correct or not.",
            "It is correct. The arrow is directing to the <1> <2>."
        ],
        [
            "The arrow in the image is directing to the <1> <3>. Tell me whether the statement is correct or not.",
            "It is wrong. The arrow is directing to the <1> <2>."
        ]
    ],
    "direction7": [
        [
            "There are <1>s and an arrow in the image. Read the <1>s by following the direction of the arrow.",
            "<2>"
        ],
        [
            "Arrange the <1>s by the order of the direction of the arrow in the image.",
            "<2>"
        ],
        [
            "Following the direction of the arrow, read the <1>s.",
            "<2>"
        ],
        [
            "The <1>s can be found in the image. Read the <1>s by following the arrow.",
            "<2>"
        ]
    ],
    "direction8": [
        [
            "In the perspective of the <1> arrow, what is the direction of the <2> arrow? Choose your answer from left, right, same direction, or opposite direction.",
            "The direction of the <2> arrow is <3> in the perspective of the <1> arrow."
        ],
        [
            "What is the direction of the <2> arrow in the perspective of the <1> arrow? Choose your answer from left, right, same direction, or opposite direction.",
            "The direction of the <2> arrow is <3> in the perspective of the <1> arrow."
        ],
        [
            "What is the direction of the <2> arrow relative to the <1> arrow? The answer options are left, right, same direction, or opposite direction.",
            "The relative direction of the <2> arrow to the <1> arrow is <3>."
        ],
        [
            "We are looking at the <2> arrow from the perspective of the <1> arrow. What is the direction of the <2> arrow? The answer should be one of left, right, same direction, or opposite direction.",
            "<3>"
        ]
    ],
    "direction9": [
        [
            "Where is the arrow pointing, left or right?",
            "The arrow is pointing to the <1>."
        ],
        [
            "Where is the arrow pointing, up or down?",
            "The arrow is pointing to the <2>."
        ],
        [
            "What is the direction of the arrow, left or right?",
            "The direction of the arrow is <1>."
        ],
        [
            "What is the direction of the arrow, up or down?",
            "The direction of the arrow is <2>."
        ],
        [
            "The arrow is pointing to the <1>. Is it correct?",
            "Yes, the arrow is pointing to the <1>."
        ],
        [
            "The arrow is pointing to the <3>. Is it correct?",
            "No, the arrow is pointing to the <1>."
        ],
        [
            "The direction of the arrow is <2>. Is it correct?",
            "Yes, the direction of the arrow is <2>."
        ],
        [
            "The direction of the arrow is <4>. Is it correct?",
            "No, the direction of the arrow is <2>."
        ]
    ],
    "direction10": {
        "in": [
            [
                "Choose the arrow that is pointing to the center of the image.",
                "The arrow <1> is pointing to the center of the image."
            ],
            [
                "Which arrow is pointing to the center of the image?",
                "The arrow <1> is pointing to the center of the image."
            ],
            [
                "Find the arrow that is directing inwards. What is the label of the arrow?",
                "The arrow <1> is directing inwards."
            ],
            [
                "Among the arrows in the diagram, only one arrow is pointing to the center. What is the label of that arrow?",
                "The arrow <1> is the only arrow pointing to the center."
            ]
        ],
        "out": [
            [
                "Choose the arrow that is pointing outwards from the center of the image.",
                "The arrow <1> is pointing outwards from the center of the image."
            ],
            [
                "Which arrow is pointing outwards from the center of the image?",
                "The arrow <1> is pointing outwards from the center of the image."
            ],
            [
                "Find the arrow that is directing outwards. What is the label of the arrow?",
                "The arrow <1> is directing outwards."
            ],
            [
                "Among the arrows in the diagram, only one arrow is pointing outwards from the center. What is the label of that arrow?",
                "The arrow <1> is the only arrow pointing outwards from the center."
            ]
        ]
    }
}

conversation_short = {
    "direction1": [
        [
            "There are <1> arrows scattered on the given image. Find the arrow that has most different direction from the others.",
            "<2>"
        ],
        [
            "Among <1> arrows in the diagram, which one is directing to the most distinctive direction?",
            "<2>"
        ],
        [
            "Choose the arrow in the picture with distinct direction from the others.",
            "<2>"
        ],
        [
            "Which arrow is point to the different direction? Choose the arrow from the image and tell me the label of the arrow.",
            "<2>"
        ]
    ],
    "direction2": [
        [
            "There is an arrow in the image. What is the direction of the arrow?",
            "<2>"
        ],
        [
            "What is the direction of the arrow in the diagram?",
            "<2>"
        ],
        [
            "Where is the arrow in the image pointing to? Choose your answer from the following options: <1>.",
            "<2>"
        ],
        [
            "See the arrow in the diagram. What is the direction of the arrow?",
            "<2>"
        ],
        [
            "The arrow in the image is pointing to the <2>. Is it correct?",
            "Yes"
        ],
        [
            "The arrow in the diagram is pointing to the <3>. Is it correct?",
            "No"
        ]
    ],
    "direction3": [
        [
            "Among <1> arrows in the diagram, which one is directing to the <2>?",
            "<3>"
        ],
        [
            "Choose the arrow in the picture that is pointing to the <2>.",
            "<3>"
        ],
        [
            "Which arrow is pointing to the <2>? Choose the arrow from <1> options in the image and tell me the label of the arrow.",
            "<3>"
        ],
        [
            "<1> arrows are drawn on the given image. Find the arrow that is pointing to the <2>.",
            "<3>"
        ]
    ],
    "direction4": [
        [
            "You can see an arrow at the center of the image. What is that arrow pointing to?",
            "<2>"
        ],
        [
            "Tell me the <1> that an arrow is pointing to in the diagram.",
            "<2>"
        ],
        [
            "What <1> is pointed by the arrow in the image?",
            "<2>"
        ],
        [
            "The arrow at the center is directing to the <1> <2>. Tell me whether the statement is correct or not.",
            "It is correct."
        ],
        [
            "The arrow at the center is directing to the <1> <3>. Tell me whether the statement is correct or not.",
            "It is wrong."
        ]
    ],
    "direction5": [
        [
            "In the image, there is a two-headed arrow. What are the two <1>s that the arrow is pointing to?",
            "<2> and <3>"
        ],
        [
            "Tell me the <1>s that the two-headed arrow is pointing to in the diagram.",
            "<2> and <3>"
        ],
        [
            "What <1>s are pointed by the two-headed arrow in the image?",
            "<2> and <3>"
        ],
        [
            "Choose the correct <1>s that the two-headed arrow is pointing to in the image.",
            "<2> and <3>"
        ],
        [
            "By looking at the end points of the two-headed arrow, tell me the <1>s that the arrow is pointing to.",
            "<2> and <3>"
        ]
    ],
    "direction6": [
        [
            "You can see an arrow in the image. What is that arrow pointing to?",
            "<2>"
        ],
        [
            "Tell me the <1> that an arrow is pointing to in the diagram.",
            "<2>"
        ],
        [
            "What <1> is pointed by the arrow in the image?",
            "<2>"
        ],
        [
            "The arrow in the image is directing to the <1> <2>. Tell me whether the statement is correct or not.",
            "correct"
        ],
        [
            "The arrow in the image is directing to the <1> <3>. Tell me whether the statement is correct or not.",
            "wrong"
        ]
    ],
    "direction7": [
        [
            "There are <1>s and an arrow in the image. Read the <1>s by following the direction of the arrow.",
            "<2>"
        ],
        [
            "Arrange the <1>s by the order of the direction of the arrow in the image.",
            "<2>"
        ],
        [
            "Following the direction of the arrow, read the <1>s.",
            "<2>"
        ],
        [
            "The <1>s can be found in the image. Read the <1>s by following the arrow.",
            "<2>"
        ]
    ],
    "direction8": [
        [
            "In the perspective of the <1> arrow, what is the direction of the <2> arrow? Choose your answer from left, right, same direction, or opposite direction.",
            "<3>"
        ],
        [
            "What is the direction of the <2> arrow in the perspective of the <1> arrow? Choose your answer from left, right, same direction, or opposite direction.",
            "<3>"
        ],
        [
            "What is the direction of the <2> arrow relative to the <1> arrow? The answer options are left, right, same direction, or opposite direction.",
            "<3>"
        ],
        [
            "We are looking at the <2> arrow from the perspective of the <1> arrow. What is the direction of the <2> arrow? The answer should be one of left, right, same direction, or opposite direction.",
            "<3>"
        ]
    ],
    "direction9": [
        [
            "Where is the arrow pointing, left or right?",
            "<1>"
        ],
        [
            "Where is the arrow pointing, up or down?",
            "<2>"
        ],
        [
            "What is the direction of the arrow, left or right?",
            "<1>"
        ],
        [
            "What is the direction of the arrow, up or down?",
            "<2>"
        ],
        [
            "The arrow is pointing to the <1>. Is it correct?",
            "Yes"
        ],
        [
            "The arrow is pointing to the <3>. Is it correct?",
            "No"
        ],
        [
            "The direction of the arrow is <2>. Is it correct?",
            "Yes"
        ],
        [
            "The direction of the arrow is <4>. Is it correct?",
            "No"
        ]
    ],
    "direction10": {
        "in": [
            [
                "Choose the arrow that is pointing to the center of the image.",
                "<1>"
            ],
            [
                "Which arrow is pointing to the center of the image?",
                "<1>"
            ],
            [
                "Find the arrow that is directing inwards. What is the label of the arrow?",
                "<1>"
            ],
            [
                "Among the arrows in the diagram, only one arrow is pointing to the center. What is the label of that arrow?",
                "<1>"
            ]
        ],
        "out": [
            [
                "Choose the arrow that is pointing outwards from the center of the image.",
                "<1>"
            ],
            [
                "Which arrow is pointing outwards from the center of the image?",
                "<1>"
            ],
            [
                "Find the arrow that is directing outwards. What is the label of the arrow?",
                "<1>"
            ],
            [
                "Among the arrows in the diagram, only one arrow is pointing outwards from the center. What is the label of that arrow?",
                "<1>"
            ]
        ]
    }
}

def generate_direction1(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short
    
    n = entity[1]
    answer = entity[2]

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", str(n))
    a = conversation[entity[0]][index][1].replace("<2>", answer)

    return q, a

def generate_direction2(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short
    
    direction = entity[1]

    if direction in ['up', 'down', 'left', 'right']:
        direction_pool = ['up', 'down', 'left', 'right']
    else:
        direction_pool = ['up-left', 'up-right', 'down-left', 'down-right']

    negative_direction = random.choice([x for x in direction_pool if x != direction])

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", ", ".join(direction_pool)).replace("<2>", direction).replace("<3>", negative_direction)
    a = conversation[entity[0]][index][1].replace("<2>", direction).replace("<3>", negative_direction)

    return q, a

def generate_direction3(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    n = entity[1]
    direction = entity[2]
    answer = entity[3]

    index = random.randint(0, len(conversation[entity[0]]) - 1)
    
    q = conversation[entity[0]][index][0].replace("<1>", str(n)).replace("<2>", direction)
    a = conversation[entity[0]][index][1].replace("<2>", direction).replace("<3>", answer)

    return q, a

def generate_direction4(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    object_type = entity[1]

    if object_type == 'direction':
        object_type = 'word'

    answer = entity[2]
    negative_answer = entity[3]

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", object_type).replace("<2>", answer).replace("<3>", negative_answer)
    a = conversation[entity[0]][index][1].replace("<1>", object_type).replace("<2>", answer).replace("<3>", negative_answer)

    return q, a

def generate_direction5(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    object_type = entity[1]
    answer1 = entity[2]
    answer2 = entity[3]

    if object_type == 'direction':
        object_type = 'word'

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", object_type)
    a = conversation[entity[0]][index][1].replace("<1>", object_type).replace("<2>", answer1).replace("<3>", answer2)

    return q, a

def generate_direction6(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    object_type = entity[1]
    answer = entity[2]
    negative_answer = entity[3]

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", object_type).replace("<2>", answer).replace("<3>", negative_answer)
    a = conversation[entity[0]][index][1].replace("<1>", object_type).replace("<2>", answer).replace("<3>", negative_answer)

    return q, a

def generate_direction7(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    text_type = entity[1]
    answer = entity[2]

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", text_type)
    a = conversation[entity[0]][index][1].replace("<2>", ''.join(answer))

    return q, a

def generate_direction8(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    color1 = entity[1]
    color2 = entity[2]
    direction = entity[3]

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", color1).replace("<2>", color2).replace("<3>", direction)
    a = conversation[entity[0]][index][1].replace("<1>", color1).replace("<2>", color2).replace("<3>", direction)

    return q, a

def generate_direction9(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    direction = entity[1]
    
    lr = 'left' if 'left' in direction else 'right'
    ud = 'up' if 'up' in direction else 'down'

    lr_false = 'right' if lr == 'left' else 'left'
    ud_false = 'down' if ud == 'up' else 'up'

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", lr).replace("<2>", ud).replace("<3>", lr_false).replace("<4>", ud_false)
    a = conversation[entity[0]][index][1].replace("<1>", lr).replace("<2>", ud).replace("<3>", lr_false).replace("<4>", ud_false)

    return q, a

def generate_direction10(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    q_type = entity[1]
    answer = entity[2]

    index = random.randint(0, len(conversation[entity[0]][q_type]) - 1)

    q = conversation[entity[0]][q_type][index][0]
    a = conversation[entity[0]][q_type][index][1].replace("<1>", answer)

    return q, a

def generate_conversation(diagram, long=False):
    conversation_list = []

    for entity in diagram.entities:
        if entity[0] == 'direction1':
            conversation_list.append(generate_direction1(entity, long))
        elif entity[0] == 'direction2':
            conversation_list.append(generate_direction2(entity, long))
        elif entity[0] == 'direction3':
            conversation_list.append(generate_direction3(entity, long))
        elif entity[0] == 'direction4':
            conversation_list.append(generate_direction4(entity, long))
        elif entity[0] == 'direction5':
            conversation_list.append(generate_direction5(entity, long))
        elif entity[0] == 'direction6':
            conversation_list.append(generate_direction6(entity, long))
        elif entity[0] == 'direction7':
            conversation_list.append(generate_direction7(entity, long))
        elif entity[0] == 'direction8':
            conversation_list.append(generate_direction8(entity, long))
        elif entity[0] == 'direction9':
            conversation_list.append(generate_direction9(entity, long))
        elif entity[0] == 'direction10':
            conversation_list.append(generate_direction10(entity, long))

    return conversation_list
