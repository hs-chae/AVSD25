from .rules import *
import roman

conversation_long = {
    "texture1": [
        [
            "There are <1> lines in the image. Name the line with different line style from the rest.",
            "The line with different line style is <2>."
        ],
        [
            "Among <1> lines in the image, which line has different line style?",
            "Line style of <2> is different from the rest."
        ],
        [
            "In the given picture, there are <1> lines. What is the color of the line with different line style?",
            "<2> line has different line style."
        ],
        [
            "Among <1> lines in the image, tell me the color of the line that has different line style.",
            "The line with <2> color has different line style."
        ],
        [
            "Choose the line that can be distinguished by the line style from the rest among <1> lines in the image. <2>",
            "<3>"
        ],
        [
            "In the <1> options, select the line that has different line style. <2>",
            "<3>"
        ]
    ],
    "texture2": [
        [
            "Which line has the same line style as <1>?",
            "<2> has the same line style as <1>, which is <3>."
        ],
        [
            "Choose the line that has the same line style as <1>.",
            "The line with the same line style as <1> is <2>, which is <3>."
        ],
        [
            "I gave you a picture with lines. I want to find the line with the same line style as <1>.",
            "<1> and <2> have the same line style, and it is <3>."
        ],
        [
            "Select the option that represents the line with the same line style as <1>. <2>",
            "<3>"
        ],
        [
            "Among the <1> lines in the image, which line has the same line style as <2>? <3>",
            "<4>"
        ],
        [
            "Select the option that represents the line with the same line style as <1>.",
            "<2> has the same line style as <1>, which is <3>."
        ],
        [
            "Choose the line that has the same line style as <1>.",
            "The line with the same line style as <1> is <2>, which is <3>."
        ],
        [
            "Among the numbered lines, which line has the same line style as <1>?",
            "<2> has the same line style as <1> and it is <3>."
        ]
    ],
    "texture3_a": [
        [
            "There are four shapes in the image. Choose the shape that has different texture from the others.",
            "Shape <1> has different texture from the others."
        ],
        [
            "Among the four shapes in the image, which shape has different texture?",
            "The texture of shape <1> is different."
        ],
        [
            "In the image, there are four shapes. Find the shape with different texture from the rest.",
            "My answer is <1>."
        ],
        [
            "The shape <1> has different texture from the others. Is it correct?",
            "Yes, shape <1> has different texture."
        ],
        [
            "The shape <1> has different texture from the others. Is it correct?",
            "No, shape <1> cannot be distinguished from some other shape."
        ],
        [
            "There are four shapes in the image. Choose the shape that has different texture from the others and answer with its color.",
            "The answer is <1>."
        ],
        [
            "Among the four shapes in the image, which shape has different texture? What is the color of that shape?",
            "<1> shape has different texture."
        ],
        [
            "In the image, there are four shapes. Find the color of the shape with different texture from the rest.",
            "The color of the shape with different texture is <1>."
        ]
    ],
    "texture4": [
        [
            "Among the four options, choose the <1> that has the same texture as the <2> <1>.",
            "The <1> with the same texture as the <2> <1> is <3>."
        ],
        [
            "What is the <1> with the same texture as the <2> <1>?",
            "<3> is the <1> with the same texture as the <2> <1>."
        ],
        [
            "Select the option that has the same texture as the <2> <1>.",
            "The <1> <3> has the same texture as the <2> <1>."
        ],
        [
            "Among the four options, choose the <1> that has the different texture from the <2> <1>.",
            "The <1> with the different texture from the <2> <1> is <3>."
        ],
        [
            "What is the <1> with the different texture from the <2> <1>?",
            "<3> is the <1> with the different texture from the <2> <1>."
        ],
        [
            "Select the option that has the different texture from the <2> <1>.",
            "The <1> <3> has the different texture from the <2> <1>."
        ]
    ],
    "texture6": [
        [
            "What is the line style of line <1>?",
            "Its line style is <2>"
        ],
        [
            "What line style does line <1> have?",
            "Line <1> is <2>"
        ],
        [
            "In the image, there is a polygon. Name the line style of line <1>.",
            "<2> style is the line style of line <1>."
        ],
        [
            "Choose the correct line style of line <1>. <2>",
            "<3>"
        ],
        [
            "Is the line style of line <1> <2>?",
            "Yes, the lines style of line <1> is <2>."
        ],
        [
            "Is the line style of line <1> <2>?",
            "No, the line style of line <1> is not <2>."
        ]
    ],
    "texture7": [
        [
            "There is a line segment in the image. The line segment is divided by the line style. How many parts are there in total?",
            "<1> parts"
        ],
        [
            "There is a line segment in the image. The line segment is divided by the line style. How many parts are there in total?",
            "<1>"
        ],
        [
            "The line is segmented by its line style. Count the number of segments.",
            "The line is divided into <1> segments."
        ],
        [
            "The line is segmented by its line style. Count the number of segments.",
            "<1>"
        ],
        [
            "You can see that the line can be divided by the line style. What is the total number of such intervals?",
            "There are <1> intervals in total."
        ],
        [
            "You can see that the line can be divided by the line style. What is the total number of such intervals?",
            "<1>"
        ],
        [
            "The line is divided by the line style. How many parts are found in the image?",
            "I can find <1> parts."
        ],
        [
            "The line is divided by the line style. How many parts are found in the image?",
            "<1>"
        ]
    ],
    "texture8": [
        [
            "There are <1> lines in the image. All of them have different line style. Choose the one with the most dense line style.",
            "The line with the most dense line style is <2>."
        ],
        [
            "Among <1> lines in the image, which line has the most dense line style?",
            "Line <2> is the most dense line."
        ],
        [
            "Choose the line that has the most breaks per unit length.",
            "The line with the most breaks per unit length is <2>."
        ],
        [
            "There are <1> lines in the image. All of them have different line style. Choose the one with the most sparse line style.",
            "The line with the most sparse line style is <2>."
        ],
        [
            "Among <1> lines in the image, which line has the most sparse line style?",
            "Line <2> is the most sparse line."
        ],
        [
            "Choose the line that has the fewest breaks per unit length.",
            "The line with the fewest breaks per unit length is <2>."
        ],
        [
            "List the lines in the image from the most dense line style to the most sparse line style.",
            "The order of the lines from the most dense to the most sparse is <2>."
        ],
        [
            "Count the breaks per unit length of the lines to order them from the most dense to the most sparse.",
            "The answer is <2>."
        ],
        [
            "List the lines in the image from the most sparse line style to the most dense line style.",
            "The order of the lines from the most sparse to the most dense is <2>."
        ],
        [
            "Count the breaks per unit length of the lines to order them from the most sparse to the most dense.",
            "The answer is <2>."
        ]
    ],
    "texture9": [
        [
            "Among the <1> lines in the image, count the types of line style.",
            "There are <2> types of line style in total. The line styles are <3> line."
        ],
        [
            "Considering only the line style, how many types of line style are in the image?",
            "There are <2> line style. They are <3> line."
        ],
        [
            "Count the number of different line styles in the image.",
            "There are <2> different line styles: <3> line."
        ],
        [
            "How many different line styles are there in the image?",
            "<2> different line styles are found, which are <3> line."
        ]
    ],
    "texture10": [
        [
            "How many <1> lines are in the image?",
            "There are <2> <1> lines."
        ],
        [
            "Count the number of <1> lines in the image.",
            "The answer is <2>."
        ],
        [
            "In the given picture, what is the total number of <1> lines?",
            "There are <2> <1> lines in total."
        ],
        [
            "Find all the <1> lines in the diagram. How many are there?",
            "I found <2> <1> lines."
        ]
    ],
    "texture11": {
        "one_different": [
            [
                "There are <1> shapes in the image. Choose the shape that is drawn with different line style from the others.",
                "The shape <2> is drawn with different line style."
            ],
            [
                "Among the <1> shapes in the image, which shape has different line style?",
                "The shape <2> has different line style."
            ],
            [
                "Does the shape <2> have different line style from the others?",
                "Yes, the shape <2> has different line style."
            ],
            [
                "Does the shape <3> have different line style from the others?",
                "No, the shape <3> cannot be distinguished from some other shape."
            ]
        ],
        "all_different": [
            [
                "Choose the shape that is drawn with <1> line style.",
                "The shape with <1> line style is <2>."
            ],
            [
                "Among the shapes, which shape is drawn with <1> line style?",
                "The shape with <1> line style is <2>."
            ],
            [
                "What is the line style of the <2>?",
                "The <2> is drawn with <1> line style."
            ],
            [
                "Tell me the line style of the <2>.",
                "The <2> is drawn with <1> line style."
            ]
        ]
    },
    "texture12": [
        [
            "Only by looking at the <1> lines, what shape can you see?",
            "I can see a <2>."
        ],
        [
            "What is the shape that is formed by the <1> lines?",
            "The shape formed by the <1> lines is a <2>."
        ],
        [
            "Focus on the <1> lines. What is the shape that is formed by these lines?",
            "The shape is a <2>."
        ],
        [
            "The <1> lines are forming a shape. What is the name of the shape?",
            "The shape is a <2>."
        ],
        [
            "There is a shape that is formed by the <1> lines. How many sides does the shape have?",
            "The shape has <3> sides."
        ]
    ],
    "texture13": [
        [
            "What is the line style of the <1>?",
            "The line style of the <1> is <2>."
        ],
        [
            "Fine the <1> in the image. What is the line style of it?",
            "The <1> is a <2> line."
        ],
        [
            "State the line style of the <1>.",
            "The <1> has a <2> line style."
        ],
        [
            "Is the line style of the <1> <2>?",
            "Yes, the line style of the <1> is <2>."
        ],
        [
            "Is the line style of the <1> <3>?",
            "No, the line style of the <1> is <2>."
        ]
    ],
    "texture14": [
        [
            "There are <1> lines scattered in the image. Among them, find the <2> line. What is the <3> of that line?",
            "The <3> of the <2> line is <4>."
        ],
        [
            "In the image, there are <1> lines. Find the <2> line. What is the <3> of that line?",
            "The <3> of the <2> line is <4>."
        ],
        [
            "Can you find a <2> line? What is the <3> of that line?",
            "Yes, it is <4>."
        ],
        [
            "Look at the image and tell me the <3> of the <2> line.",
            "The <3> of the <2> line is <4>."
        ]
    ],
    "texture15": [
        [
            "From the lines in the image, choose the line that has the different line style from the others. What is the <1> of that line?",
            "The <1> of the line with different line style is <2>."
        ],
        [
            "Among the lines in the image, which line has different line style? What is the <1> of that line?",
            "The <1> of the line with different line style is <2>."
        ],
        [
            "There are <3> lines in the image. Find the line with different line style and tell me the <1> of that line.",
            "The <1> of the line with different line style is <2>."
        ],
        [
            "Choose the line that has different line style from the rest. What is the <1> of that line?",
            "The answer is <2>."
        ],
        [
            "Select the line that has different line style from the others. What is the <1> of that line?",
            "It is <2> that has different line style."
        ]
    ]
}

conversation_short = {
    "texture1": [
        [
            "There are <1> lines in the image. Name the line with different line style from the rest.",
            "<2>"
        ],
        [
            "Among <1> lines in the image, which line has different line style?",
            "<2>"
        ],
        [
            "In the given picture, there are <1> lines. What is the color of the line with different line style?",
            "<2>"
        ],
        [
            "Among <1> lines in the image, tell me the color of the line that has different line style.",
            "<2>"
        ],
        [
            "Choose the line that can be distinguished by the line style from the rest among <1> lines in the image. <2>",
            "<3>"
        ],
        [
            "In the <1> options, select the line that has different line style. <2>",
            "<3>"
        ]
    ],
    "texture2": [
        [
            "Which line has the same line style as <1>?",
            "<2>"
        ],
        [
            "Choose the line that has the same line style as <1>.",
            "<2>"
        ],
        [
            "I gave you a picture with lines. I want to find the line with the same line style as <1>.",
            "<2>"
        ],
        [
            "Select the option that represents the line with the same line style as <1>. <2>",
            "<3>"
        ],
        [
            "Among the <1> lines in the image, which line has the same line style as <2>? <3>",
            "<4>"
        ],
        [
            "Select the option that represents the line with the same line style as <1>.",
            "<2>"
        ],
        [
            "Choose the line that has the same line style as <1>.",
            "<2>"
        ],
        [
            "Among the numbered lines, which line has the same line style as <1>?",
            "<2>"
        ]
    ],
    "texture3_a": [
        [
            "There are four shapes in the image. Choose the shape that has different texture from the others.",
            "<1>"
        ],
        [
            "Among the four shapes in the image, which shape has different texture?",
            "<1>"
        ],
        [
            "In the image, there are four shapes. Find the shape with different texture from the rest.",
            "<1>"
        ],
        [
            "The shape <1> has different texture from the others. Is it correct?",
            "Yes"
        ],
        [
            "The shape <1> has different texture from the others. Is it correct?",
            "No"
        ],
        [
            "There are four shapes in the image. Choose the shape that has different texture from the others and answer with its color.",
            "<1>"
        ],
        [
            "Among the four shapes in the image, which shape has different texture? What is the color of that shape?",
            "<1>"
        ],
        [
            "In the image, there are four shapes. Find the color of the shape with different texture from the rest.",
            "<1>"
        ]
    ],
    "texture4": [
        [
            "Among the four options, choose the <1> that has the same texture as the <2> <1>.",
            "<3>"
        ],
        [
            "What is the <1> with the same texture as the <2> <1>?",
            "<3>"
        ],
        [
            "Select the option that has the same texture as the <2> <1>.",
            "<3>"
        ],
        [
            "Among the four options, choose the <1> that has the different texture from the <2> <1>.",
            "<3>"
        ],
        [
            "What is the <1> with the different texture from the <2> <1>?",
            "<3>"
        ],
        [
            "Select the option that has the different texture from the <2> <1>.",
            "<3>"
        ]
    ],
    "texture6": [
        [
            "What is the line style of line <1>?",
            "<2>"
        ],
        [
            "What line style does line <1> have?",
            "<2>"
        ],
        [
            "In the image, there is a polygon. Name the line style of line <1>.",
            "<2>"
        ],
        [
            "Choose the correct line style of line <1>. <2>",
            "<3>"
        ],
        [
            "Is the line style of line <1> <2>?",
            "Yes"
        ],
        [
            "Is the line style of line <1> <2>?",
            "No"
        ]
    ],
    "texture7": [
        [
            "There is a line segment in the image. The line segment is divided by the line style. How many parts are there in total?",
            "<1>"
        ],
        [
            "There is a line segment in the image. The line segment is divided by the line style. How many parts are there in total?",
            "<1>"
        ],
        [
            "The line is segmented by its line style. Count the number of segments.",
            "<1>"
        ],
        [
            "The line is segmented by its line style. Count the number of segments.",
            "<1>"
        ],
        [
            "You can see that the line can be divided by the line style. What is the total number of such intervals?",
            "<1>"
        ],
        [
            "You can see that the line can be divided by the line style. What is the total number of such intervals?",
            "<1>"
        ],
        [
            "The line is divided by the line style. How many parts are found in the image?",
            "<1>"
        ],
        [
            "The line is divided by the line style. How many parts are found in the image?",
            "<1>"
        ]
    ],
    "texture8": [
        [
            "There are <1> lines in the image. All of them have different line style. Choose the one with the most dense line style.",
            "<2>"
        ],
        [
            "Among <1> lines in the image, which line has the most dense line style?",
            "<2>"
        ],
        [
            "Choose the line that has the most breaks per unit length.",
            "<2>"
        ],
        [
            "There are <1> lines in the image. All of them have different line style. Choose the one with the most sparse line style.",
            "<2>"
        ],
        [
            "Among <1> lines in the image, which line has the most sparse line style?",
            "<2>"
        ],
        [
            "Choose the line that has the fewest breaks per unit length.",
            "<2>"
        ],
        [
            "List the lines in the image from the most dense line style to the most sparse line style.",
            "<2>"
        ],
        [
            "Count the breaks per unit length of the lines to order them from the most dense to the most sparse.",
            "<2>"
        ],
        [
            "List the lines in the image from the most sparse line style to the most dense line style.",
            "<2>"
        ],
        [
            "Count the breaks per unit length of the lines to order them from the most sparse to the most dense.",
            "<2>"
        ]
    ],
    "texture9": [
        [
            "Among the <1> lines in the image, count the types of line style.",
            "<2>"
        ],
        [
            "Considering only the line style, how many types of line style are in the image?",
            "<2>"
        ],
        [
            "Count the number of different line styles in the image.",
            "<2>"
        ],
        [
            "How many different line styles are there in the image?",
            "<2>"
        ]
    ],
    "texture10": [
        [
            "How many <1> lines are in the image?",
            "<2>"
        ],
        [
            "Count the number of <1> lines in the image.",
            "<2>"
        ],
        [
            "In the given picture, what is the total number of <1> lines?",
            "<2>"
        ],
        [
            "Find all the <1> lines in the diagram. How many are there?",
            "<2>"
        ]
    ],
    "texture11": {
        "one_different": [
            [
                "There are <1> shapes in the image. Choose the shape that is drawn with different line style from the others.",
                "<2>"
            ],
            [
                "Among the <1> shapes in the image, which shape has different line style?",
                "<2>"
            ],
            [
                "Does the shape <2> have different line style from the others?",
                "Yes"
            ],
            [
                "Does the shape <3> have different line style from the others?",
                "No"
            ]
        ],
        "all_different": [
            [
                "Choose the shape that is drawn with <1> line style.",
                "<2>"
            ],
            [
                "Among the shapes, which shape is drawn with <1> line style?",
                "<2>"
            ],
            [
                "What is the line style of the <2>?",
                "<1>"
            ],
            [
                "Tell me the line style of the <2>.",
                "<1>"
            ]
        ]
    },
    "texture12": [
        [
            "Only by looking at the <1> lines, what shape can you see?",
            "<2>"
        ],
        [
            "What is the shape that is formed by the <1> lines?",
            "<2>"
        ],
        [
            "Focus on the <1> lines. What is the shape that is formed by these lines?",
            "<2>"
        ],
        [
            "The <1> lines are forming a shape. What is the name of the shape?",
            "<2>"
        ],
        [
            "There is a shape that is formed by the <1> lines. How many sides does the shape have?",
            "<3>"
        ]
    ],
    "texture13": [
        [
            "What is the line style of the <1>?",
            "<2>"
        ],
        [
            "Fine the <1> in the image. What is the line style of it?",
            "<2>"
        ],
        [
            "State the line style of the <1>.",
            "<2>"
        ],
        [
            "Is the line style of the <1> <2>?",
            "Yes"
        ],
        [
            "Is the line style of the <1> <3>?",
            "No"
        ]
    ],
    "texture14": [
        [
            "There are <1> lines scattered in the image. Among them, find the <2> line. What is the <3> of that line?",
            "<4>"
        ],
        [
            "In the image, there are <1> lines. Find the <2> line. What is the <3> of that line?",
            "<4>"
        ],
        [
            "Can you find a <2> line? What is the <3> of that line?",
            "<4>"
        ],
        [
            "Look at the image and tell me the <3> of the <2> line.",
            "<4>"
        ]
    ]
}

def shape_to_name(shape):
    if isinstance(shape, Polygon):
        if shape.n == 3:
            return "triangle"
        elif shape.n == 4:
            return "square"
        elif shape.n == 5:
            return "pentagon"
        elif shape.n == 6:
            return "hexagon"
    elif isinstance(shape, Circle):
        return "circle"
    return ""

def option_generation(labels, answer_index):
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
    
    sep = random.choice([" ", ", "])
    options = sep.join(options)

    return options, answer_option

def generate_texture1(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    line_count = len(entity[1])
    lines = entity[1].copy()
    answer_line = lines[0]
    type = entity[2]
    
    if type == 0:
        random.shuffle(lines)
        answer_label = answer_line.label
        labels = list(map(lambda x: x.label, lines))
        index = random.choice([0, 1, 4, 5])

        if index == 0 or index == 1:
            q = conversation["texture1"][index][0].replace("<1>", str(line_count))
            a = conversation["texture1"][index][1].replace("<2>", 'line ' + answer_label)
        elif index == 4 or index == 5:
            answer_index = labels.index(answer_label)
            options, answer_option = option_generation(labels, answer_index)
            q = conversation["texture1"][index][0].replace("<1>", str(line_count)).replace("<2>", options)
            a = conversation["texture1"][index][1].replace("<3>", answer_option)
    elif type == 1:
        random.shuffle(lines)
        answer_label = answer_line.start.label + answer_line.end.label
        labels = list(map(lambda x: x.start.label + x.end.label, lines))

        index = random.choice([0, 1, 4, 5])

        if index == 0 or index == 1:
            q = conversation["texture1"][index][0].replace("<1>", str(line_count))
            a = conversation["texture1"][index][1].replace("<2>", 'line ' + answer_label)
        elif index == 4 or index == 5:
            answer_index = labels.index(answer_label)
            options, answer_option = option_generation(labels, answer_index)
            q = conversation["texture1"][index][0].replace("<1>", str(line_count)).replace("<2>", options)
            a = conversation["texture1"][index][1].replace("<3>", answer_option)
    elif type == 2:
        random.shuffle(lines)
        answer_color = answer_line.color
        colors = list(map(lambda x: x.color, lines))

        index = random.choice([2, 3, 4, 5])

        if index == 2 or index == 3:
            q = conversation["texture1"][index][0].replace("<1>", str(line_count))
            if index == 2:
                a = conversation["texture1"][index][1].replace("<2>", answer_color)
            else:
                a = conversation["texture1"][index][1].replace("<2>", answer_color)
        elif index == 4 or index == 5:
            answer_index = colors.index(answer_color)
            options, answer_option = option_generation(colors, answer_index)
            q = conversation["texture1"][index][0].replace("<1>", str(line_count)).replace("<2>", options)
            a = conversation["texture1"][index][1].replace("<3>", answer_option)
    
    return q, a

def generate_texture2(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    type = entity[3]
    question_line = entity[1]
    lines = entity[2].copy()
    answer_line = lines[0]

    if type == 0 or type == 1:
        if type == 0:
            question_label = question_line.label
            answer_label = answer_line.label
        else:
            question_label = question_line.start.label + question_line.end.label
            answer_label = answer_line.start.label + answer_line.end.label

        index = random.choice([0, 1, 2, 3, 4])

        if index == 0 or index == 1 or index == 2:
            q = conversation["texture2"][index][0].replace("<1>", "line " + question_label)
            a = conversation["texture2"][index][1].replace("<1>", "line " + question_label).replace("<2>", "line " + answer_label).replace("<3>", answer_line.style)
        elif index == 3:
            random.shuffle(lines)
            answer_index = lines.index(answer_line)
            if type == 0:
                labels = list(map(lambda x: x.label, lines))
            else:
                labels = list(map(lambda x: x.start.label + x.end.label, lines))
            options, answer_option = option_generation(labels, answer_index)
            q = conversation["texture2"][index][0].replace("<1>", "line " + question_label).replace("<2>", options)
            a = conversation["texture2"][index][1].replace("<3>", answer_option)
        elif index == 4:
            random.shuffle(lines)
            answer_index = lines.index(answer_line)
            if type == 0:
                labels = list(map(lambda x: x.label, lines))
            else:
                labels = list(map(lambda x: x.start.label + x.end.label, lines))
            options, answer_option = option_generation(labels, answer_index)
            q = conversation["texture2"][index][0].replace("<1>", str(len(lines))).replace("<2>", "line " + question_label).replace("<3>", options)
            a = conversation["texture2"][index][1].replace("<4>", answer_option)
    elif type == 2:
        question_label = question_line.color
        answer_label = answer_line.color

        index = random.choice([0, 1, 2, 3, 4])

        if index == 0 or index == 1 or index == 2:
            q = conversation["texture2"][index][0].replace("<1>", question_label + " colored line")
            a = conversation["texture2"][index][1].replace("<1>", question_label + " colored line").replace("<2>", answer_label + " line").replace("<3>", answer_line.style)
        elif index == 3:
            random.shuffle(lines)
            answer_index = lines.index(answer_line)
            labels = list(map(lambda x: x.color, lines))
            options, answer_option = option_generation(labels, answer_index)
            q = conversation["texture2"][index][0].replace("<1>", question_label + " line").replace("<2>", options)
            a = conversation["texture2"][index][1].replace("<3>", answer_option)
        elif index == 4:
            random.shuffle(lines)
            answer_index = lines.index(answer_line)
            labels = list(map(lambda x: x.color, lines))
            options, answer_option = option_generation(labels, answer_index)
            q = conversation["texture2"][index][0].replace("<1>", str(len(lines))).replace("<2>", question_label + " line").replace("<3>", options)
            a = conversation["texture2"][index][1].replace("<4>", answer_option)
    elif type == 3:
        index = random.choice([5, 6, 7])
        q = conversation["texture2"][index][0].replace("<1>", question_line.color + " line")
        a = conversation["texture2"][index][1].replace("<1>", question_line.color + " line").replace("<2>", answer_line.label).replace("<3>", answer_line.style)

    return q, a

def generate_texture3_a(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    answer = entity[1]
    labeling = entity[2]

    if labeling in [0, 1]:
        index = random.choice([0, 1, 2, 3, 4])

        if index == 0 or index == 1 or index == 2:
            q = conversation["texture3_a"][index][0]
            a = conversation["texture3_a"][index][1].replace("<1>", answer)
        elif index == 3:
            q = conversation["texture3_a"][index][0].replace("<1>", answer)
            a = conversation["texture3_a"][index][1].replace("<1>", answer)
        elif index == 4:
            if labeling == 0:
                negative_answer = random.choice(list(set(['1', '2', '3', '4']) - set([answer])))
            else:
                negative_answer = random.choice(list(set(['A', 'B', 'C', 'D']) - set([answer])))
            q = conversation["texture3_a"][index][0].replace("<1>", negative_answer)
            a = conversation["texture3_a"][index][1].replace("<1>", negative_answer)
    elif labeling == 2:
        index = random.choice([5, 6, 7])

        q = conversation["texture3_a"][index][0]
        a = conversation["texture3_a"][index][1].replace("<1>", answer)

    return q, a

def generate_texture4(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    answer_index = entity[1]
    rand = entity[2]    # 0: choose same color, 1: choose different color
    shapes = entity[3]

    if rand == 0:
        index = random.choice([0, 1, 2])
    else:
        index = random.choice([3, 4, 5])
    
    shape_name = shape_to_name(shapes[0])
    answer = shapes[answer_index].label

    fill_color_distinguishable = True
    for shape in shapes[1:]:
        if shape.fill_color == shapes[0].fill_color or shape.fill_color != shapes[1].fill_color:
            fill_color_distinguishable = False
            break

    border_color_distinguishable = True
    for shape in shapes[1:]:
        if shape.border_color == shapes[0].border_color or shape.border_color != shapes[1].border_color:
            border_color_distinguishable = False
            break

    if fill_color_distinguishable:
        indicator = shapes[0].fill_color
    elif border_color_distinguishable:
        indicator = shapes[0].border_color
    else:
        if shapes[0].y > shapes[1].y:
            indicator = "topmost"
        else:
            indicator = "leftmost"

    q = conversation["texture4"][index][0].replace("<1>", shape_name).replace("<2>", indicator)
    a = conversation["texture4"][index][1].replace("<1>", shape_name).replace("<2>", indicator).replace("<3>", answer)

    return q, a

def generate_texture6(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    lines = entity[1]
    label_type = entity[2]  # 0: label of line, 1: label of points
    
    question_index = random.choice(range(len(lines)))
    question_line = lines[question_index]
    question_label = question_line.label if label_type == 0 else [question_line.start.label + question_line.end.label, question_line.end.label + question_line.start.label][random.choice([0, 1])]
    answer = question_line.style

    index = random.choice([0, 1, 2, 3, 4, 5])

    if index == 0 or index == 1 or index == 2:
        q = conversation["texture6"][index][0].replace("<1>", question_label)
        a = conversation["texture6"][index][1].replace("<1>", question_label).replace("<2>", answer)
    elif index == 3:
        options = ['solid', 'dotted', 'dashed', 'dashdot']
        random.shuffle(options)
        answer_index = options.index(answer)
        options, answer_option = option_generation(options, answer_index)
        q = conversation["texture6"][index][0].replace("<1>", question_label).replace("<2>", options)
        a = conversation["texture6"][index][1].replace("<3>", answer_option)
    elif index == 4:
        q = conversation["texture6"][index][0].replace("<1>", question_label).replace("<2>", answer)
        a = conversation["texture6"][index][1].replace("<1>", question_label).replace("<2>", answer)
    elif index == 5:
        negative_answer = random.choice(list(set(['solid', 'dotted', 'dashed', 'dashdot']) - set([answer])))
        q = conversation["texture6"][index][0].replace("<1>", question_label).replace("<2>", negative_answer)
        a = conversation["texture6"][index][1].replace("<1>", question_label).replace("<2>", negative_answer)

    return q, a

def generate_texture7(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    n_intervals = entity[1]
    index = random.choice(range(0, len(conversation["texture7"])))
    q = conversation["texture7"][index][0]
    a = conversation["texture7"][index][1].replace("<1>", str(n_intervals))
    return q, a

def generate_texture8(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    labels = entity[1]
    density = entity[2]
    index = random.choice(range(0, len(conversation["texture8"])))

    ld = zip(labels, density)
    ld = sorted(ld, key=lambda x: x[1])
    ordered_labels = [x[0] for x in ld]

    if index in [0, 1, 2]:
        answer = ordered_labels[-1]
    elif index in [3, 4, 5]:
        answer = ordered_labels[0]
    elif index in [6, 7]:
        answer = ', '.join(reversed(ordered_labels))
    else:
        answer = ', '.join(ordered_labels)
    
    q = conversation["texture8"][index][0].replace("<1>", str(len(labels)))
    a = conversation["texture8"][index][1].replace("<2>", answer)

    return q, a

def generate_texture9(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    styles = list(set(entity[1]))
    n = len(entity[1])
    m = entity[2]

    random.shuffle(styles)
    index = random.choice(range(0, len(conversation["texture9"])))

    q = conversation["texture9"][index][0].replace("<1>", str(n))
    a = conversation["texture9"][index][1].replace("<2>", str(m)).replace("<3>", ', '.join(styles))

    return q, a

def generate_texture10(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    style = entity[3]
    answer = entity[2]

    index = random.choice(range(0, len(conversation["texture10"])))

    q = conversation["texture10"][index][0].replace("<1>", style)
    a = conversation["texture10"][index][1].replace("<1>", style).replace("<2>", str(answer))

    return q, a

def generate_texture11(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shapes = entity[1]
    one_different = entity[2]
    styles = entity[3]

    if one_different:
        index = random.choice(range(0, len(conversation["texture11"]["one_different"])))
        q = conversation["texture11"]["one_different"][index][0].replace("<1>", str(len(shapes))).replace("<2>", shapes[0]).replace("<3>", shapes[1])
        a = conversation["texture11"]["one_different"][index][1].replace("<1>", str(len(shapes))).replace("<2>", shapes[0]).replace("<3>", shapes[1])
    else:
        index = random.choice(range(0, len(conversation["texture11"]["all_different"])))
        q = conversation["texture11"]["all_different"][index][0].replace("<1>", styles[0]).replace("<2>", shapes[0])
        a = conversation["texture11"]["all_different"][index][1].replace("<1>", styles[0]).replace("<2>", shapes[0])

    return q, a

def generate_texture12(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    n = entity[1]
    style = entity[2]

    if n == 3:
        shape = "triangle"
    elif n == 4:
        shape = "quadranlge"
    elif n == 5:
        shape = "pentagon"

    index = random.choice(range(0, len(conversation["texture12"])))

    q = conversation["texture12"][index][0].replace("<1>", style)
    a = conversation["texture12"][index][1].replace("<1>", style).replace("<2>", shape).replace("<3>", str(n))

    return q, a

def generate_texture13(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    labeling = entity[1]
    lines = entity[2]

    line = random.choice(lines)

    if labeling == 0:
        label = line.label
        line_name = 'line ' + label
    elif labeling == 1:
        label = line.start.label + line.end.label
        line_name = 'line ' + label
    else:
        label = line.color
        line_name = ([label + ' colored line', label + ' line'][random.choice([0, 1])])

    style = line.style
    negative_style = random.choice(list(set(['solid', 'dotted', 'dashed', 'dashdot']) - set([style])))

    index = random.choice(range(0, len(conversation["texture13"])))

    q = conversation["texture13"][index][0].replace("<1>", line_name).replace("<2>", style).replace("<3>", negative_style)
    a = conversation["texture13"][index][1].replace("<1>", line_name).replace("<2>", style).replace("<3>", negative_style)

    return q, a

def generate_texture14(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    answer = entity[1]
    labeling = entity[2]
    lines = entity[3]
    style = entity[4]

    n = len(lines)

    if labeling == 0:
        naming = random.choice(['name', 'label'])
    elif labeling == 1:
        naming = random.choice(['name', 'label'])
    else:
        naming = 'color'

    index = random.choice(range(0, len(conversation["texture14"])))

    q = conversation["texture14"][index][0].replace("<1>", str(n)).replace("<2>", style).replace("<3>", naming).replace("<4>", answer)
    a = conversation["texture14"][index][1].replace("<1>", str(n)).replace("<2>", style).replace("<3>", naming).replace("<4>", answer)

    return q, a

def generate_texture15(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    answer = entity[1]
    labeling = entity[2]
    lines = entity[3]
    n = len(lines)

    if labeling == 0:
        naming = random.choice(['name', 'label'])
    elif labeling == 1:
        naming = random.choice(['name', 'label'])
    else:
        naming = 'color'

    index = random.choice(range(0, len(conversation["texture15"])))

    q = conversation["texture15"][index][0].replace("<1>", naming).replace("<2>", answer).replace("<3>", str(n))
    a = conversation["texture15"][index][1].replace("<1>", naming).replace("<2>", answer).replace("<3>", str(n))

    return q, a

def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        if entity[0] == 'texture1':
            conversation_list.append(generate_texture1(entity, long))
        elif entity[0] == 'texture2':
            conversation_list.append(generate_texture2(entity, long))
        elif entity[0] == 'texture3_a':
            conversation_list.append(generate_texture3_a(entity, long))
        elif entity[0] == 'texture4':
            conversation_list.append(generate_texture4(entity, long))
        elif entity[0] == 'texture6':
            conversation_list.append(generate_texture6(entity, long))
        elif entity[0] == 'texture7':
            conversation_list.append(generate_texture7(entity, long))
        elif entity[0] == 'texture8':
            conversation_list.append(generate_texture8(entity, long))
        elif entity[0] == 'texture9':
            conversation_list.append(generate_texture9(entity, long))
        elif entity[0] == 'texture10':
            conversation_list.append(generate_texture10(entity, long))
        elif entity[0] == 'texture11':
            conversation_list.append(generate_texture11(entity, long))
        elif entity[0] == 'texture12':
            conversation_list.append(generate_texture12(entity, long))
        elif entity[0] == 'texture13':
            conversation_list.append(generate_texture13(entity, long))
        elif entity[0] == 'texture14':
            conversation_list.append(generate_texture14(entity, long))
        elif entity[0] == 'texture15':
            conversation_list.append(generate_texture15(entity, long))
    return conversation_list