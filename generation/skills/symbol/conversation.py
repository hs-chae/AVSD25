import random
import roman

conversation_long = {
    "symbol_1_a": [
        [
            "There is a triangle and a symbol represeting an angle in the image. Which angle is the symbol representing?",
            "The symbol is representing the angle <1>."
        ],
        [
            "What angle is represented by the angle symbol?",
            "Angle <1> is represented by the angle symbol."
        ],
        [
            "What is the meaning of the angle symbol in the image?",
            "The symbol in the image represents the angle <1>."
        ],
        [
            "Identify the angle represented by the angle symbol in the image.",
            "Angle <1> is the answer."
        ],
        [
            "Choose the angle that is represented by the angle symbol in the image. <1>",
            "<2>"
        ]
    ],
    "symbol_1_b": [
        [
            "In the image, you can find a single angle symbol. What two lines are forming this angle?",
            "The angle is formed by the lines <1> and <2>."
        ],
        [
            "Which two lines are forming the angle represented by the angle symbol in the image?",
            "Lines <1> and <2> are making the angle in the image."
        ],
        [
            "What are the two lines that are forming the (symboled) angle in the image?",
            "They are lines <1> and <2>."
        ],
        [
            "Identify the two lines that are forming the symboled angle in the image.",
            "The lines <1> and <2> are forming the angle."
        ]
    ],
    "symbol_1_c": [
        [
            "In the image, there are lines and angles formed by the lines. Choose the color of the angle symbol that represents perpendicular angle. <1>",
            "The answer is <2>."
        ],
        [
            "What is the color of the angle symbol representing the perpendicular angle in the image? <1>",
            "The correct option is <2>."
        ],
        [
            "Choose two lines that are forming the perpendicular angle in the image.",
            "The line <1> and the line <2> are forming the perpendicular angle."
        ],
        [
            "By which two lines is the perpendicular angle formed?",
            "The perpendicular angle is formed by the lines <1> and <2>."
        ]
    ],
    "symbol_2_a": [
        [
            "There are words in the image. Which word is symboled as correct?",
            "The correct word is <1>."
        ],
        [
            "Choose the word that is represented by the green symbol in the image.",
            "The word <1> is represented by the green symbol."
        ],
        [
            "What is the meaning of the red and green symbols in the image?",
            "The symbols in the image say that the word <1> is correct and elses are wrong."
        ],
        [
            "Identify the word that can be considered as correct.",
            "The word <1> is the correct answer."
        ]
    ],
    "symbol_2_b": [
        [
            "In the image, choose the word boxed with <1> box.",
            "The word boxed with <1> box is <2>."
        ],
        [
            "What is the word that is boxed with <1> box?",
            "The boxed word is <2>."
        ],
        [
            "Choose the word that is boxed in <1> color",
            "The word <2> is in the <1> box."
        ],
        [
            "Identify the word that is in the <1> box.",
            "The answer is <2>."
        ]
    ],
    "symbol3_a": [
        [
            "What is the <1> symbol in the image indicating?",
            "The <1> symbol in the image says that two lines are parallel."
        ],
        [
            "What is the meaning of the <1> symbol in the image?",
            "The meaning of the <1> symbol is that the lines are parallel."
        ],
        [
            "According to the symbol in the image, what is the relationship between two lines?",
            "They are parallel according to the <1> symbol."
        ],
        [
            "Let me know the relationship between the lines by interpreting the symbol in the image.",
            "The two lines are parallel."
        ],
        [
            "Choose the correct option that describes the image. The <1> symbol indicates that the lines (are parallel / have the same length).",
            "The lines are parallel."
        ],
        [
            "According to the symbol, two lines (are parallel / have the same length). What is the correct option?",
            "According to the symbol, two lines are parallel."
        ]
    ],
    "symbol3_b": [
        [
            "What is the <1> symbol in the image indicating?",
            "The <1> symbol in the image says that two lines have the same length."
        ],
        [
            "What is the meaning of the <1> symbol in the image?",
            "The meaning of the <1> symbol is that the lines have the same length."
        ],
        [
            "According to the symbol in the image, what is the relationship between two lines?",
            "They have the same length according to the <1> symbol."
        ],
        [
            "Let me know the relationship between the lines by interpreting the symbol in the image.",
            "The two lines have the same length."
        ],
        [
            "Choose the correct option that describes the image. The <1> symbol indicates that the lines (are parallel / have the same length).",
            "The lines have the same length."
        ],
        [
            "According to the symbol, two lines (are parallel / have the same length). What is the correct option?",
            "According to the symbol, two lines have the same length."
        ]
    ],
    "symbol4_a": [
        [
            "Find the two lines with same length. Hint: Look for the <1> symbol.",
            "The lines <2> and <3> have the same length."
        ],
        [
            "According to the <1> symbol, which two lines have the same length?",
            "The lines <2> and <3> have the same length."
        ],
        [
            "Identify a pair of lines that have the same length.",
            "The lines <2> and <3> are the answer by the <1> symbol."
        ],
        [
            "Choose the lines that have the same length. You should use the information of the symbol.",
            "The <1> symbol indicates that the lines <2> and <3> have the same length."
        ],
        [
            "What line has the same length with the line <2>? Hint: Look for the <1> symbol.",
            "The line <3> has the same length with the line <2>."
        ],
        [
            "There is a single pair of lines with the same length. What are the lines?",
            "The <1> symbol is saying that the lines <2> and <3> have the same length."
        ]
    ],
    "symbol4_b": [
        [
            "Find the two sides in the polygon with same length. Hint: Look for the <1> symbol.",
            "The sides <2> and <3> have the same length."
        ],
        [
            "According to the <1> symbol, which two sides in this shape have the same length?",
            "The sides <2> and <3> have the same length."
        ],
        [
            "Identify a pair of sides that have the same length.",
            "The sides <2> and <3> are the answer by the <1> symbol."
        ],
        [
            "Choose the sides that have the same length. You should use the information of the symbol.",
            "The <1> symbol indicates that the lines <2> and <3> have the same length."
        ],
        [
            "What side has the same length with the side <2>? Hint: Look for the <1> symbol.",
            "The line <3> has the same length with the line <2>."
        ],
        [
            "There is a single pair of lines with the same length. What are the lines?",
            "The <1> symbol is saying that the lines <2> and <3> have the same length."
        ]
    ],
    "symbol4_c": [
        [
            "According to the picture, What is correct? <1>",
            "<2> <3>"
        ],
        [
            "What is the correct option according to the image? <1>",
            "By the <4> symbol, <2> is the answer."
        ],
        [
            "Choose the correct option that describes the image. The lines (<1> / <2> / <3>) have the same length.",
            "The lines <4> have the same length."
        ],
        [
            "According to the symbol, two lines (<1> / <2> / <3>) have the same length. Complete the sentence.",
            "According to the symbol, two lines <4> have the same length."
        ],
        [
            "Choose the phrase that is correct according to the image. The length of lines (<1> / <2> / <3>) are equal.",
            "The length of lines <4> are equal."
        ]
    ],
    "symbol5": [
        [
            "What does the <1> symbol mean? Choose the correct option. \n<2>",
            "The correct option is <3>."
        ],
        [
            "What is the meaning of the <1> symbol in the image? Choose the correct option. \n<2>",
            "<3> is the correct option"
        ],
        [
            "Choose the correct option that describes the image. Hint: <1> symbol. \n<2>",
            "<3> is correct."
        ],
        [
            "Among the four options, what is true according to the <1> symbol? \n<2>",
            "<3> is true."
        ],
        [
            "According to the <1> symbol, what is correct? \n<2>",
            "<3> is the answer according to the symbol."
        ]
    ]
}

conversation_short = {
    "symbol_1_a": [
        [
            "There is a triangle and a symbol represeting an angle in the image. Which angle is the symbol representing?",
            "Angle <1>"
        ],
        [
            "What angle is represented by the angle symbol?",
            "Angle <1>"
        ],
        [
            "What is the meaning of the angle symbol in the image?",
            "Angle <1>"
        ],
        [
            "Identify the angle represented by the angle symbol in the image.",
            "Angle <1>"
        ],
        [
            "Choose the angle that is represented by the angle symbol in the image. <1>",
            "Angle <2>"
        ]
    ],
    "symbol_1_b": [
        [
            "In the image, you can find a single angle symbol. What two lines are forming this angle?",
            "Lines <1> and <2>."
        ],
        [
            "Which two lines are forming the angle represented by the angle symbol in the image?",
            "Lines <1> and <2>"
        ],
        [
            "What are the two lines that are forming the (symboled) angle in the image?",
            "Lines <1> and <2>."
        ],
        [
            "Identify the two lines that are forming the symboled angle in the image.",
            "Lines <1> and <2>."
        ]
    ],
    "symbol_1_c": [
        [
            "In the image, there are lines and angles formed by the lines. Choose the color of the angle symbol that represents perpendicular angle. <1>",
            "<2>"
        ],
        [
            "What is the color of the angle symbol representing the perpendicular angle in the image? <1>",
            "<2>"
        ],
        [
            "Choose two lines that are forming the perpendicular angle in the image.",
            "<1> and <2>"
        ],
        [
            "By which two lines is the perpendicular angle formed?",
            "<1> and <2>"
        ]
    ],
    "symbol_2_a": [
        [
            "There are words in the image. Which word is symboled as correct?",
            "<1>"
        ],
        [
            "Choose the word that is represented by the green symbol in the image.",
            "<1>"
        ],
        [
            "What is the meaning of the red and green symbols in the image?",
            "<1>"
        ],
        [
            "Identify the word that can be considered as correct.",
            "<1>"
        ]
    ],
    "symbol_2_b": [
        [
            "In the image, choose the word boxed with <1> box.",
            "<2>"
        ],
        [
            "What is the word that is boxed with <1> box?",
            "<2>"
        ],
        [
            "Choose the word that is boxed in <1> color",
            "<2>"
        ],
        [
            "Identify the word that is in the <1> box.",
            "<2>"
        ]
    ],
    "symbol3_a": [
        [
            "What is the <1> symbol in the image indicating?",
            "parallel"
        ],
        [
            "What is the meaning of the <1> symbol in the image?",
            "parallel"
        ],
        [
            "According to the symbol in the image, what is the relationship between two lines?",
            "parallel"
        ],
        [
            "Let me know the relationship between the lines by interpreting the symbol in the image.",
            "parallel"
        ],
        [
            "Choose the correct option that describes the image. The <1> symbol indicates that the lines (are parallel / have the same length).",
            "are parallel"
        ],
        [
            "According to the symbol, two lines (are parallel / have the same length). What is the correct option?",
            "are parallel"
        ]
    ],
    "symbol3_b": [
        [
            "What is the <1> symbol in the image indicating?",
            "same length"
        ],
        [
            "What is the meaning of the <1> symbol in the image?",
            "same length"
        ],
        [
            "According to the symbol in the image, what is the relationship between two lines?",
            "same length"
        ],
        [
            "Let me know the relationship between the lines by interpreting the symbol in the image.",
            "same length"
        ],
        [
            "Choose the correct option that describes the image. The <1> symbol indicates that the lines (are parallel / have the same length).",
            "have the same length"
        ],
        [
            "According to the symbol, two lines (are parallel / have the same length). What is the correct option?",
            "have the same length"
        ]
    ],
    "symbol4_a": [
        [
            "Find the two lines with same length. Hint: Look for the <1> symbol.",
            "<2> and <3>"
        ],
        [
            "According to the <1> symbol, which two lines have the same length?",
            "<2>, <3>"
        ],
        [
            "Identify a pair of lines that have the same length.",
            "<2> and <3>"
        ],
        [
            "Choose the lines that have the same length. You should use the information of the symbol.",
            "<2>, <3>"
        ],
        [
            "What line has the same length with the line <2>? Hint: Look for the <1> symbol.",
            "<3>"
        ],
        [
            "There is a single pair of lines with the same length. What are the lines?",
            "<2> and <3>"
        ]
    ],
    "symbol4_b": [
        [
            "Find the two sides in the polygon with same length. Hint: Look for the <1> symbol.",
            "<2>, <3>"
        ],
        [
            "According to the <1> symbol, which two sides in this shape have the same length?",
            "<2> and <3>"
        ],
        [
            "Identify a pair of sides that have the same length.",
            "<2>, <3>"
        ],
        [
            "Choose the sides that have the same length. You should use the information of the symbol.",
            "<2> and <3>"
        ],
        [
            "What side has the same length with the side <2>? Hint: Look for the <1> symbol.",
            "<3>"
        ],
        [
            "There is a single pair of lines with the same length. What are the lines?",
            "<2>, <3>"
        ]
    ],
    "symbol4_c": [
        [
            "According to the picture, What is correct? <1>",
            "<2>"
        ],
        [
            "What is the correct option according to the image? <1>",
            "<2>"
        ],
        [
            "Choose the correct option that describes the image. The lines (<1> / <2> / <3>) have the same length.",
            "<4>"
        ],
        [
            "According to the symbol, two lines (<1> / <2> / <3>) have the same length. Complete the sentence.",
            "<4>"
        ],
        [
            "Choose the phrase that is correct according to the image. The length of lines (<1> / <2> / <3>) are equal.",
            "<4>"
        ]
    ],
    "symbol5": [
        [
            "What does the <1> symbol mean? Choose the correct option. \n<2>",
            "<3>"
        ],
        [
            "What is the meaning of the <1> symbol in the image? Choose the correct option. \n<2>",
            "<3>"
        ],
        [
            "Choose the correct option that describes the image. Hint: <1> symbol. \n<2>",
            "<3>"
        ],
        [
            "Among the four options, what is true according to the <1> symbol? \n<2>",
            "<3>"
        ],
        [
            "According to the <1> symbol, what is correct? \n<2>",
            "<3>"
        ]
    ]
}

def option_generation(labels, answer_index, sep=None):
    # 1. 2. 3.
    # (1) (2) (3)
    # A. B. C.
    # (A) (B) (C)
    # a. b. c.
    # (a) (b) (c)
    # i. ii. iii.
    # (i) (ii) (iii)
    # I. II. III.
    # (I) (II) (III)

    type = random.randint(0, 9)

    if type == 0:
        options = [f'{chr(ord("A") + i)}. {labels[i]}' for i in range(len(labels))]
        answer_option = chr(ord("A") + answer_index)
    elif type == 1:
        options = [f'({chr(ord("A") + i)}) {labels[i]}' for i in range(len(labels))]
        answer_option = f'({chr(ord("A") + answer_index)})'
    elif type == 2:
        options = [f'{chr(ord("1") + i)}. {labels[i]}' for i in range(len(labels))]
        answer_option = chr(ord("1") + answer_index)
    elif type == 3:
        options = [f'({chr(ord("1") + i)}) {labels[i]}' for i in range(len(labels))]
        answer_option = f'({chr(ord("1") + answer_index)})'
    elif type == 4:
        options = [f'{chr(ord("a") + i)}. {labels[i]}' for i in range(len(labels))]
        answer_option = chr(ord("a") + answer_index)
    elif type == 5:
        options = [f'({chr(ord("a") + i)}) {labels[i]}' for i in range(len(labels))]
        answer_option = f'({chr(ord("a") + answer_index)})'
    elif type == 6:
        options = [f'{roman.toRoman(i+1).lower()}. {labels[i]}' for i in range(len(labels))]
        answer_option = (roman.toRoman(answer_index+1).lower())
    elif type == 7:
        options = [f'({roman.toRoman(i+1).lower()}) {labels[i]}' for i in range(len(labels))]
        answer_option = f'({roman.toRoman(answer_index+1).lower()})'
    elif type == 8:
        options = [f'{roman.toRoman(i+1).upper()}. {labels[i]}' for i in range(len(labels))]
        answer_option = (roman.toRoman(answer_index+1).upper())
    elif type == 9:
        options = [f'({roman.toRoman(i+1).upper()}) {labels[i]}' for i in range(len(labels))]
        answer_option = f'({roman.toRoman(answer_index+1).upper()})'
    
    sep = sep or random.choice([" ", ", "])
    options = sep.join(options)

    return options, answer_option

def generate_symbol_1_a(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.randint(0, len(conversation["symbol_1_a"]) - 1)

    if index == 0 or index == 1 or index == 2 or index == 3:
        q = conversation["symbol_1_a"][index][0]
        a = conversation["symbol_1_a"][index][1]
        a = a.replace("<1>", entity[3].label)

    elif index == 4:
        q = conversation["symbol_1_a"][index][0]
        a = conversation["symbol_1_a"][index][1]

        angles = [entity[1].label, entity[2].label, entity[3].label]
        random.shuffle(angles)
        answer = angles.index(entity[3].label)
        options, answer_option = option_generation(angles, answer)

        q = q.replace("<1>", options)
        a = a.replace("<2>", answer_option)

    return q, a

def generate_symbol_1_b(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.randint(0, len(conversation["symbol_1_b"]) - 1)

    if index == 0 or index == 1 or index == 2 or index == 3:
        q = conversation["symbol_1_b"][index][0]
        a = conversation["symbol_1_b"][index][1]
        a = a.replace("<1>", entity[1].label)
        a = a.replace("<2>", entity[2].label)

    return q, a

def generate_symbol_1_c(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    type = entity[1]

    if type == 'color':
        colors = entity[2]
        answer = colors[-1]
        random.shuffle(colors)
        answer_index = colors.index(answer)
        options, answer_option = option_generation(colors, answer_index)

        index = random.choice([0, 1])
        q = conversation["symbol_1_c"][index][0].replace("<1>", options)
        a = conversation["symbol_1_c"][index][1].replace("<2>", answer_option)

    else:
        l1, l2 = entity[3], entity[4]
        label1, label2 = l1.label, l2.label

        index = random.choice([2, 3])
        q = conversation["symbol_1_c"][index][0]
        a = conversation["symbol_1_c"][index][1].replace("<1>", label1).replace("<2>", label2)
    
    return q, a

def generate_symbol_2_a(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    words = entity[1]
    correct = entity[2]

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0]
    a = conversation[entity[0]][index][1].replace("<1>", words[correct])

    return q, a

def generate_symbol_2_b(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    color = entity[1]
    answer = entity[2]

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", color)
    a = conversation[entity[0]][index][1].replace("<1>", color).replace("<2>", answer)

    return q, a

def generate_symbol3_a(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", entity[1])
    a = conversation[entity[0]][index][1].replace("<1>", entity[1])

    return q, a

def generate_symbol3_b(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", entity[1])
    a = conversation[entity[0]][index][1].replace("<1>", entity[1])

    return q, a

def generate_symbol4_a(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", entity[1]).replace("<2>", entity[2]).replace("<3>", entity[3])
    a = conversation[entity[0]][index][1].replace("<1>", entity[1]).replace("<2>", entity[2]).replace("<3>", entity[3])

    return q, a

def generate_symbol4_b(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    q = conversation[entity[0]][index][0].replace("<1>", entity[1]).replace("<2>", entity[2]).replace("<3>", entity[3])
    a = conversation[entity[0]][index][1].replace("<1>", entity[1]).replace("<2>", entity[2]).replace("<3>", entity[3])

    return q, a

def generate_symbol4_c(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.randint(0, len(conversation[entity[0]]) - 1)

    color = entity[1]
    center_label = entity[2]
    p1_label = entity[3]
    p2_label = entity[4]

    if index in [0, 1]:
        l1 = p1_label + center_label if random.choice([True, False]) else center_label + p1_label
        l2 = p2_label + center_label if random.choice([True, False]) else center_label + p2_label
        l3 = p1_label + p2_label if random.choice([True, False]) else p2_label + p1_label

        options = [
            f'{l1} and {l2}' if random.choice([True, False]) else f'{l2} and {l1}',
            f'{l1} and {l3}' if random.choice([True, False]) else f'{l3} and {l1}',
            f'{l2} and {l3}' if random.choice([True, False]) else f'{l3} and {l2}'
        ]

        answer = options[0]
        random.shuffle(options)
        answer_index = options.index(answer)

        options, answer_option = option_generation(options, answer_index)

        q = conversation[entity[0]][index][0].replace("<1>", options)
        a = conversation[entity[0]][index][1].replace("<2>", answer_option).replace("<3>", f'{l1} and {l2}').replace("<4>", color)

    elif index in [2, 3, 4]:
        l1 = p1_label + center_label if random.choice([True, False]) else center_label + p1_label
        l2 = p2_label + center_label if random.choice([True, False]) else center_label + p2_label
        l3 = p1_label + p2_label if random.choice([True, False]) else p2_label + p1_label

        options = [
            f'{l1} and {l2}' if random.choice([True, False]) else f'{l2} and {l1}',
            f'{l1} and {l3}' if random.choice([True, False]) else f'{l3} and {l1}',
            f'{l2} and {l3}' if random.choice([True, False]) else f'{l3} and {l2}'
        ]

        answer = options[0]

        random.shuffle(options)

        q = conversation[entity[0]][index][0].replace("<1>", options[0]).replace("<2>", options[1]).replace("<3>", options[2])
        a = conversation[entity[0]][index][1].replace("<4>", answer)

    return q, a

def generate_symbol5(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    color = entity[1]
    center_point = entity[2]
    p1 = entity[3]
    p2 = entity[4]
    p = entity[5]

    l1 = p1 + center_point if random.choice([True, False]) else center_point + p1
    l2 = p2 + center_point if random.choice([True, False]) else center_point + p2

    angle1 = p1 + center_point + p if random.choice([True, False]) else p + center_point + p1
    angle2 = p2 + center_point + p if random.choice([True, False]) else p + center_point + p2
    big_angle = p1 + center_point + p2 if random.choice([True, False]) else p2 + center_point + p1

    phrase = random.choice([
        ' have the same size.',
        ' are equal.',
    ])

    answer = random.choice([
        f'Angle {angle1} and {angle2}',
        f'Angle {angle2} and {angle1}'
    ]) + phrase

    neg1 = random.choice([
        f'Angle {angle1} and {big_angle}',
        f'Angle {big_angle} and {angle1}'
    ]) + phrase

    neg2 = random.choice([
        f'Angle {angle2} and {big_angle}',
        f'Angle {big_angle} and {angle2}'
    ]) + phrase

    neg3 = random.choice([
        f'Line {l1} and {l2}',
        f'Line {l2} and {l1}'
    ]) + ' have the same length.'

    neg4 = random.choice([
        f'Line {l1} and {l2}',
        f'Line {l2} and {l1}'
    ]) + ' are parallel.'

    neg5 = random.choice([
        f'Angle {angle1} and {angle2}',
        f'Angle {angle2} and {angle1}'
    ]) + ' forms a right angle.'

    negatives = random.sample([neg1, neg2, neg3, neg4, neg5], 3)

    options = [answer] + negatives
    random.shuffle(options)
    answer_index = options.index(answer)

    options, answer_option = option_generation(options, answer_index, sep="\n")

    index = random.randint(0, len(conversation_short["symbol5"]) - 1)

    q = conversation["symbol5"][index][0].replace("<1>", color).replace("<2>", options)
    a = conversation["symbol5"][index][1].replace("<3>", answer_option)

    return q, a


def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        if entity[0] == 'symbol_1_a':
            q, a = generate_symbol_1_a(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol_1_b':
            q, a = generate_symbol_1_b(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol_1_c':
            q, a = generate_symbol_1_c(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol_2_a':
            q, a = generate_symbol_2_a(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol_2_b':
            q, a = generate_symbol_2_b(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol3_a':
            q, a = generate_symbol3_a(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol3_b':
            q, a = generate_symbol3_b(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol4_a':
            q, a = generate_symbol4_a(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol4_b':
            q, a = generate_symbol4_a(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol4_c':
            q, a = generate_symbol4_c(entity, long)
            conversation_list.append((q, a))
        elif entity[0] == 'symbol5':
            q, a = generate_symbol5(entity, long)
            conversation_list.append((q, a))
    return conversation_list
