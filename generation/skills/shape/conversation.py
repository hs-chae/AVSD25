from .rules import *
import roman

conversation_long = {
    "shape1": [
        [
            "What is the shape in the image?",
            "The shape in the image is a <1>."
        ],
        [
            "In the given picture, there is a single diagram. Tell me its shape.",
            "<1> is the shape of the diagram."
        ],
        [
            "What shape is in the image?",
            "There is a <1> in the image."
        ],
        [
            "What is the shape of the diagram?",
            "The shape of the diagram is a <1>."
        ],
        [
            "What shape can you see in the image?",
            "The shape I can see in the image is a <1>."
        ],
        [
            "Choose the shape that is in the image. <2>",
            "<3> <1> is the shape in the image."
        ],
        [
            "What shape is in the image? <2>",
            "There is <3> <1> in the image."
        ],
        [
            "<2>. What is in the image? Choose the correct option.",
            "The answer is <3> <1>."
        ]
    ],
    "shape2": [
        [
            "There are three shapes in the image. Tell the shapes from left to right.",
            "In the image, there are <1>, <2>, <3>"
        ],
        [
            "List the shapes in the image from left to right.",
            "<1>, <2>, <3>"
        ],
        [
            "From left to right, what are the shapes in the image?",
            "<1>, <2>, <3> are the shapes in the image."
        ]
    ],
    "shape3": [
        [
            "There are multiple shapes in the image. How many <1> are there?",
            "There are <2> <1> in the image."
        ],
        [
            "Count the number of <1> in the image.",
            "The answer is <2>."
        ],
        [
            "How many <1> are there in the picture?",
            "<2> <1> are there in the picture."
        ],
        [
            "Are there total <2> <1> in the image?",
            "Yes, there are total <2> <1> in the image."
        ],
        [
            "Are there total <2> <1> in the picture?",
            "No, there are total <3> <1> in the picture."
        ]
    ],
    "shape4": [
        [
            "What is the <1> shape in the image?",
            "<2> is the <1> shape."
        ],
        [
            "In the picture, there are shapes with different colors. What is the <1> shape?",
            "<2> is the <1> shape."
        ],
        [
            "There are various shapes in the image. Only one of them has a different color. What is that shape?",
            "<2> is the one with a different color."
        ],
        [
            "Tell the name of the shape that has a <1> color.",
            "<2> has a <1> color."
        ],
        [
            "The shape of the color <1> is ( ).",
            "<2>"
        ]
    ],
    "shape5": [
        [
            "What is shape <1>?",
            "Shape <1> is <2>."
        ],
        [
            "Which shape is labeled as <1>?",
            "<2> is labeled as <1>."
        ],
        [
            "Tell me the name of the shape labeled as <1>.",
            "<2> is the shape labeled as <1>."
        ],
        [
            "What type of shape is labeled as <1>?",
            "It is <2>."
        ]
    ],
    "shape6": [
        [
            "What is the shape that an arrow is pointing to?",
            "The arrow is pointing to a <1>."
        ],
        [
            "In the image, there is an arrow pointing to some shape. What is that shape?",
            "<1> is the shape that the arrow is pointing to."
        ],
        [
            "Which shape is indicated by the arrow?",
            "The arrow indicates a <1>."
        ],
        [
            "Can you tell me the shape that the arrow is pointing to?",
            "Yes, the arrow is pointing to a <1>."
        ],
        [
            "Is the arrow pointing to a <1>?",
            "Yes, the arrow is pointing to a <1>."
        ],
        [
            "Is the arrow pointing to a <2>?",
            "No, the arrow is pointing to a <1>."
        ]
    ],
    "shape7": [
        [
            "Tell me how many sides this polygon has. What is the name of this polygon?",
            "This polygon has <1> sides. So, it is a <2>."
        ],
        [
            "Count the number of sides of this polygon. Then, tell me the name of this polygon.",
            "It has <1> sides. Therefore, it is a <2>."
        ],
        [
            "Explain about the image.",
            "The image shows a polygon with <1> sides. It is a <2>."
        ],
        [
            "What shape is this?",
            "This is a <2>."
        ],
        [
            "Identify the shape in the image.",
            "The shape in the image is a <2>."
        ]
    ],
    "shape8": [
        [
            "The image is divided into two parts. What shape is in the both parts?",
            "The shape in both parts is a <1>."
        ],
        [
            "Let me know the shape that is in the both parts of the divided image.",
            "A <1> is in the both parts of the divided image."
        ],
        [
            "The line divides the image into two sections. What is the shape in both sections?",
            "The shape in both sections is a <1>."
        ],
        [
            "Tell me the shape that is both in the left and right parts of the image.",
            "The shape that is in both the left and right parts of the image is a <1>."
        ]
    ],
    "shape9": [
        [
            "There are shapes scattered in the <1> plane. What is the shape that is not filled?",
            "The shape that is not filled is a <2>."
        ],
        [
            "In the image, there are shapes with different colors. What is the shape that is not filled?",
            "The <2> is not filled."
        ],
        [
            "There are various shapes in the image. Only one of them is not filled with color. What is that shape?",
            "The answer is <2>."
        ],
        [
            "Tell me the name of the shape that is not filled with color.",
            "The shape that is not filled with color is a <2>."
        ],
        [
            "The shape that is not filled with color is ( ).",
            "The shape that is not filled with color is a <2>."
        ]
    ]
}

conversation_short = {
    "shape1": [
        [
            "What is the shape in the image?",
            "<1>"
        ],
        [
            "In the given picture, there is a single diagram. Tell me its shape.",
            "<1>"
        ],
        [
            "What shape is in the image?",
            "<1>"
        ],
        [
            "What is the shape of the diagram?",
            "<1>"
        ],
        [
            "What shape can you see in the image?",
            "<1>"
        ],
        [
            "Choose the shape that is in the image. <2>",
            "<3>"
        ],
        [
            "What shape is in the image? <2>",
            "<3>"
        ],
        [
            "<2>. What is in the image? Choose the correct option.",
            "<3>"
        ]
    ],
    "shape2": [
        [
            "There are three shapes in the image. Tell the shapes from left to right.",
            "<1>, <2>, <3>"
        ],
        [
            "List the shapes in the image from left to right.",
            "<1>, <2>, <3>"
        ],
        [
            "From left to right, what are the shapes in the image?",
            "<1>, <2>, <3>"
        ]
    ],
    "shape3": [
        [
            "There are multiple shapes in the image. How many <1> are there?",
            "<2>"
        ],
        [
            "Count the number of <1> in the image.",
            "<2>"
        ],
        [
            "How many <1> are there in the picture?",
            "<2>"
        ],
        [
            "Are there total <2> <1> in the image?",
            "Yes"
        ],
        [
            "Are there total <2> <1> in the picture?",
            "No"
        ]
    ],
    "shape4": [
        [
            "What is the <1> shape in the image?",
            "<2>"
        ],
        [
            "In the picture, there are shapes with different colors. What is the <1> shape?",
            "<2>"
        ],
        [
            "There are various shapes in the image. Only one of them has a different color. What is that shape?",
            "<2>"
        ],
        [
            "Tell the name of the shape that has a <1> color.",
            "<2>"
        ],
        [
            "The shape of the color <1> is ( ).",
            "<2>"
        ]
    ],
    "shape5": [
        [
            "What is shape <1>?",
            "<2>"
        ],
        [
            "Which shape is labeled as <1>?",
            "<2>"
        ],
        [
            "Tell me the name of the shape labeled as <1>.",
            "<2>"
        ],
        [
            "What type of shape is labeled as <1>?",
            "<2>"
        ]
    ],
    "shape6": [
        [
            "What is the shape that an arrow is pointing to?",
            "<1>"
        ],
        [
            "In the image, there is an arrow pointing to some shape. What is that shape?",
            "<1>"
        ],
        [
            "Which shape is indicated by the arrow?",
            "<1>"
        ],
        [
            "Can you tell me the shape that the arrow is pointing to?",
            "<1>"
        ],
        [
            "Is the arrow pointing to a <1>?",
            "Yes"
        ],
        [
            "Is the arrow pointing to a <2>?",
            "No"
        ]
    ],
    "shape7": [
        [
            "Tell me how many sides this polygon has.",
            "<1>"
        ],
        [
            "Count the number of sides of this polygon.",
            "<1>"
        ],
        [
            "What shape is this?",
            "<2>"
        ],
        [
            "Identify the shape in the image.",
            "<2>"
        ]
    ],
    "shape8": [
        [
            "The image is divided into two parts. What shape is in the both parts?",
            "<1>"
        ],
        [
            "Let me know the shape that is in the both parts of the divided image.",
            "<1>"
        ],
        [
            "The line divides the image into two sections. What is the shape in both sections?",
            "<1>"
        ],
        [
            "Tell me the shape that is both in the left and right parts of the image.",
            "<1>"
        ]
    ],
    "shape9": [
        [
            "There are shapes scattered in the <1> plane. What is the shape that is not filled?",
            "<2>"
        ],
        [
            "In the image, there are shapes with different colors. What is the shape that is not filled?",
            "<2>"
        ],
        [
            "There are various shapes in the image. Only one of them is not filled with color. What is that shape?",
            "<2>"
        ],
        [
            "Tell me the name of the shape that is not filled with color.",
            "<2>"
        ],
        [
            "The shape that is not filled with color is ( ).",
            "<2>"
        ]
    ]
}

def shape_to_string(shape):
    if isinstance(shape, Circle):
        answer = "circle"
    elif isinstance(shape, EquilateralTriangle):
        answer = random.choice(["triangle", "equilateral triangle"])
    elif isinstance(shape, Square):
        answer = "square"
    elif isinstance(shape, Rectangle):
        answer = "rectangle"
    elif isinstance(shape, Pentagon):
        answer = "pentagon"
    elif isinstance(shape, Hexagon):
        answer = "hexagon"
    elif isinstance(shape, Heptagon):
        answer = "heptagon"
    elif isinstance(shape, Octagon):
        answer = "octagon"
    elif isinstance(shape, Trapezoid):
        answer = "trapezoid"
    elif isinstance(shape, Parallelogram):
        answer = "parallelogram"
    elif isinstance(shape, Star):
        if shape.n == 5:
            answer = random.choice(["star", "pentagram"])
        elif shape.n == 6:
            answer = random.choice(["star", "hexagram"])
    elif isinstance(shape, Heart):
        answer = "heart"
    elif isinstance(shape, Diamond):
        answer = random.choice(["diamond", "rhombus"])
    elif isinstance(shape, Plus):
        answer = "plus"
    elif isinstance(shape, Arrow):
        answer = "arrow"
    elif isinstance(shape, IsoscelesTriangle):
        answer = random.choice(["triangle", "isosceles triangle"])
    elif isinstance(shape, RightTriangle):
        answer = random.choice(["triangle", "right triangle"])
    else:
        answer = ""
    return answer

def shape_to_string_deteministic(shape):
    if isinstance(shape, Circle):
        answer = "circles"
    elif isinstance(shape, EquilateralTriangle):
        answer = "equilateral triangles"
    elif isinstance(shape, Square):
        answer = "squares"
    elif isinstance(shape, Rectangle):
        answer = "rectangles (that are not squares)"
    elif isinstance(shape, Pentagon):
        answer = "pentagons"
    elif isinstance(shape, Hexagon):
        answer = "hexagons"
    elif isinstance(shape, Heptagon):
        answer = "heptagons"
    elif isinstance(shape, Octagon):
        answer = "octagons"
    elif isinstance(shape, Trapezoid):
        answer = "trapezoids (that are not parallelograms)"
    elif isinstance(shape, Parallelogram):
        answer = "parallelograms (that are not rectangles)"
    elif isinstance(shape, Star):
        answer = "stars"
    elif isinstance(shape, Heart):
        answer = "hearts"
    elif isinstance(shape, Diamond):
        answer = "diamonds"
    elif isinstance(shape, Plus):
        answer = "plus shapes"
    elif isinstance(shape, Arrow):
        answer = "arrows"
    elif isinstance(shape, IsoscelesTriangle):
        answer = "isosceles triangles (that are not equilateral triangles)"
    elif isinstance(shape, RightTriangle):
        answer = "right triangles"
    else:
        answer = ""
    return answer

def non_existing_shapes(shapes):
    shape_pool = {"circle", "triangle", "square", "rectangle", "pentagon", "hexagon", "heptagon", "octagon", "trapezoid", "parallelogram", "star", "heart", "diamond", "plus", "isosceles triangle", "right triangle", "arrow"}
    for shape in shapes:
        if isinstance(shape, Circle):
            shape_pool = shape_pool - {"circle"}
        elif isinstance(shape, EquilateralTriangle):
            shape_pool = shape_pool - {"triangle", "equilateral triangle", "isosceles triangle"}
        elif isinstance(shape, Square):
            shape_pool = shape_pool - {"square", "rectangle", "diamond", "rhombus", "parallelogram", "trapezoid"}
        elif isinstance(shape, Rectangle):
            shape_pool = shape_pool - {"rectangle", "diamond", "rhombus", "parallelogram", "trapezoid"}
        elif isinstance(shape, Pentagon):
            shape_pool = shape_pool - {"pentagon"}
        elif isinstance(shape, Hexagon):
            shape_pool = shape_pool - {"hexagon"}
        elif isinstance(shape, Heptagon):
            shape_pool = shape_pool - {"heptagon"}
        elif isinstance(shape, Octagon):
            shape_pool = shape_pool - {"octagon"}
        elif isinstance(shape, Trapezoid):
            shape_pool = shape_pool - {"trapezoid"}
        elif isinstance(shape, Parallelogram):
            shape_pool = shape_pool - {"parallelogram", "trapezoid"}
        elif isinstance(shape, Star):
            if shape.n == 5:
                shape_pool = shape_pool - {"star", "pentagram"}
            elif shape.n == 6:
                shape_pool = shape_pool - {"star", "hexagram"}
        elif isinstance(shape, Heart):
            shape_pool = shape_pool - {"heart"}
        elif isinstance(shape, Diamond):
            shape_pool = shape_pool - {"diamond", "rhombus"}
        elif isinstance(shape, Plus):
            shape_pool = shape_pool - {"plus"}
        elif isinstance(shape, Arrow):
            shape_pool = shape_pool - {"arrow"}
        elif isinstance(shape, IsoscelesTriangle):
            shape_pool = shape_pool - {"triangle", "isosceles triangle"}
        elif isinstance(shape, RightTriangle):
            shape_pool = shape_pool - {"triangle", "right triangle"}

    return list(shape_pool)

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

def generate_shape1(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shape = entity[1]
    answer = shape_to_string(shape)
    shapes = non_existing_shapes([shape])
    negative_options = random.sample(shapes, random.randint(2, 4))
    options = [answer] + negative_options
    random.shuffle(options)
    answer_index = options.index(answer)

    options, answer_option = option_generation(options, answer_index)
    
    index = random.randint(0, len(conversation["shape1"])-1)
    q, a = conversation["shape1"][index]
    q = q.replace("<2>", options)
    a = a.replace("<1>", answer).replace("<3>", answer_option)

    return q, a

def generate_shape2(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shape1 = entity[1][0]
    shape2 = entity[1][1]
    shape3 = entity[1][2]

    answer1 = shape_to_string(shape1)
    answer2 = shape_to_string(shape2)
    answer3 = shape_to_string(shape3)

    index = random.randint(0, len(conversation["shape2"])-1)
    q, a = conversation["shape2"][index]
    a = a.replace("<1>", answer1).replace("<2>", answer2).replace("<3>", answer3)

    return q, a

def generate_shape3(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shapes = entity[1]
    shapes = [shape_to_string_deteministic(shape) for shape in shapes]

    answer = shapes.count(shapes[0])

    index = random.randint(0, len(conversation["shape3"])-1)
    
    if index == 0 or index == 1 or index == 2:
        q, a = conversation["shape3"][index]
        q = q.replace("<1>", shapes[0])
        a = a.replace("<2>", str(answer)).replace("<1>", shapes[0])
    elif index == 3:
        q, a = conversation["shape3"][index]
        q = q.replace("<1>", shapes[0]).replace("<2>", str(answer))
        a = a.replace("<1>", shapes[0]).replace("<2>", str(answer))
    elif index == 4:
        negative_answer = random.randint(1, 4)

        while negative_answer == answer:
            negative_answer = random.randint(1, 4)

        q, a = conversation["shape3"][index]
        q = q.replace("<1>", shapes[0]).replace("<2>", str(negative_answer))
        a = a.replace("<1>", shapes[0]).replace("<3>", str(answer))
    
    return q, a

def generate_shape4(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shapes = entity[1]
    rand = entity[2]     # 0: all different, 1: one different

    if rand == 0:
        index = random.choice([0, 1, 3, 4])
    else:
        index = random.choice([0, 2, 3, 4])

    color = shapes[0].fill_color if shapes[0].fill_color not in ["white", "none"] else shapes[0].border_color
    shape = shape_to_string(shapes[0])
    q, a = conversation["shape4"][index]
    q = q.replace("<1>", color)
    a = a.replace("<2>", shape).replace("<1>", color)

    return q, a

def generate_shape5(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.randint(0, len(conversation["shape5"])-1)
    q, a = conversation["shape5"][index]

    shapes = entity[1]
    shape = random.choice(shapes)

    label = shape.label
    answer = shape_to_string(shape)

    q = q.replace("<1>", label)
    a = a.replace("<2>", answer).replace("<1>", label)

    return q, a

def generate_shape6(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shapes = entity[1]

    answer = shape_to_string(shapes[0])
    negative_answer = ""

    for i in range(1, len(shapes)):
        if shape_to_string(shapes[i]) != answer:
            negative_answer = shape_to_string(shapes[i])
            break

    index = random.randint(0, len(conversation["shape6"])-1)
    q, a = conversation["shape6"][index]
    q = q.replace("<1>", answer).replace("<2>", negative_answer)
    a = a.replace("<1>", answer)

    return q, a

def generate_shape7(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shape = entity[1]

    answer = shape_to_string(shape)
    sides = {
        "pentagon": 5,
        "hexagon": 6,
        "heptagon": 7,
        "octagon": 8
    }[answer]

    index = random.randint(0, len(conversation["shape7"])-1)
    q, a = conversation["shape7"][index]
    q = q.replace("<1>", str(sides)).replace("<2>", answer)
    a = a.replace("<1>", str(sides)).replace("<2>", answer)

    return q, a

def generate_shape8(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shapes = entity[1]
    answer_shape = shape_to_string(shapes[0])

    index = random.randint(0, len(conversation["shape8"])-1)
    q = conversation["shape8"][index][0]
    a = conversation["shape8"][index][1].replace("<1>", answer_shape)

    return q, a

def generate_shape9(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shapes = entity[1]
    answer_shape = shape_to_string(shapes[0])

    background = entity[2]

    index = random.randint(0, len(conversation["shape9"])-1)
    q = conversation["shape9"][index][0].replace("<1>", background.fill_color)
    a = conversation["shape9"][index][1].replace("<2>", answer_shape)

    return q, a

def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        if entity[0] == "shape1":
            conversation_list.append(generate_shape1(entity, long))
        elif entity[0] == "shape2":
            conversation_list.append(generate_shape2(entity, long))
        elif entity[0] == "shape3":
            conversation_list.append(generate_shape3(entity, long))
        elif entity[0] == "shape4":
            conversation_list.append(generate_shape4(entity, long))
        elif entity[0] == "shape5":
            conversation_list.append(generate_shape5(entity, long))
        elif entity[0] == "shape6":
            conversation_list.append(generate_shape6(entity, long))
        elif entity[0] == "shape7":
            conversation_list.append(generate_shape7(entity, long))
        elif entity[0] == "shape8":
            conversation_list.append(generate_shape8(entity, long))
        elif entity[0] == "shape9":
            conversation_list.append(generate_shape9(entity, long))
    return conversation_list
