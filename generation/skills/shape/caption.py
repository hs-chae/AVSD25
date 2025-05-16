from .rules import *
import roman

captions = {
    "shape1": [
        "The image contains a single shape, which is a <1>.",
        "A <1> is prominently displayed in the image.",
        "The visual depicts a <1> as the main element.",
        "An isolated <1> is present in the image.",
        "A clear depiction of a <1> is visible in the image.",
        "The scene showcases a <1>.",
        "In the image, there is a <1>.",
        "A <1> is the focus of the visual."
    ],
    "shape2": [
        "The image features three distinct shapes arranged from left to right: <1>, <2>, and <3>.",
        "From left to right, the image presents <1>, <2>, and <3>.",
        "A sequence of shapes appears in the image, ordered as <1>, <2>, and <3>."
    ],
    "shape3": [
        "The image includes <2> <1>, scattered or positioned throughout.",
        "There are exactly <2> <1> present in the image.",
        "Within the visual, <2> <1> can be identified.",
        "The image confirms the presence of <2> <1>.",
        "Instead of <3>, the image contains <2> <1>."
    ],
    "shape4": [
        "The image contains multiple shapes, with one distinguished by its <1> color. This unique shape is a <2>.",
        "Among the various shapes in the image, the one with a <1> color is a <2>.",
        "A distinct <2> stands out due to its <1> color.",
        "The shape with a <1> hue is a <2>.",
        "In the visual, a <2> is the only shape that has a <1> color."
    ],
    "shape5": [
        "The shape labeled as <1> in the image is a <2>.",
        "The visual assigns the label <1> to a <2>.",
        "A <2> is identified with the label <1> in the image.",
        "The shape referred to as <1> is actually a <2>."
    ],
    "shape6": [
        "An arrow in the image is pointing to a <1>.",
        "The arrow directs attention to a <1> shape.",
        "A <1> is specifically indicated by the arrow in the image.",
        "The visual highlights a <1> as the object of interest.",
        "The arrow is not pointing to a <2>, but instead to a <1>."
    ],
    "shape7": [
        "The image illustrates a polygon with <1> sides, classifying it as a <2>.",
        "This geometric figure has <1> sides, making it a <2>.",
        "A <2> is depicted in the image, defined by its <1> sides.",
        "The shape shown in the image is a <2>.",
        "A polygon featuring <1> sides is present in the image, confirming it as a <2>."
    ],
    "shape8": [
        "The image is divided into two sections, both containing a <1>.",
        "A <1> appears in both the left and right halves of the divided image.",
        "Each section of the divided image contains the same shape, a <1>.",
        "Regardless of the division, a <1> remains consistent in both parts of the image."
    ],
    "shape9": [
        "The image displays multiple shapes scattered across the <1> plane, with one shape, a <2>, left unfilled.",
        "Among the various shapes in the image, the <2> is the only one not filled with color.",
        "A distinct <2> stands out as the sole unfilled shape in the image.",
        "The uncolored shape in the image is a <2>.",
        "Unlike the other filled shapes, the <2> remains without color."
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

def generate_shape1(entity):
    shape = entity[1]
    answer = shape_to_string(shape)
    shapes = non_existing_shapes([shape])
    negative_options = random.sample(shapes, random.randint(2, 4))
    options = [answer] + negative_options
    random.shuffle(options)
    answer_index = options.index(answer)

    options, answer_option = option_generation(options, answer_index)
    
    index = random.randint(0, len(captions["shape1"])-1)
    caption = captions["shape1"][index].replace("<1>", answer).replace("<2>", options).replace("<3>", answer_option)

    return caption

def generate_shape2(entity):
    shape1 = entity[1][0]
    shape2 = entity[1][1]
    shape3 = entity[1][2]

    answer1 = shape_to_string(shape1)
    answer2 = shape_to_string(shape2)
    answer3 = shape_to_string(shape3)

    index = random.randint(0, len(captions["shape2"])-1)
    caption = captions["shape2"][index].replace("<1>", answer1).replace("<2>", answer2).replace("<3>", answer3)

    return caption

def generate_shape3(entity):
    shapes = entity[1]
    shapes = [shape_to_string_deteministic(shape) for shape in shapes]

    answer = shapes.count(shapes[0])

    index = random.randint(0, len(captions["shape3"])-1)
    
    if index == 0 or index == 1 or index == 2:
        caption = captions["shape3"][index].replace("<1>", shapes[0]).replace("<2>", str(answer)).replace("<1>", shapes[0])
    elif index == 3:
        caption = captions["shape3"][index].replace("<1>", shapes[0]).replace("<2>", str(answer))
    elif index == 4:
        negative_answer = random.randint(1, 4)

        while negative_answer == answer:
            negative_answer = random.randint(1, 4)

        caption = captions["shape3"][index].replace("<1>", shapes[0]).replace("<2>", str(answer)).replace("<3>", str(negative_answer))
    
    return caption

def generate_shape4(entity):
    shapes = entity[1]
    rand = entity[2]     # 0: all different, 1: one different

    if rand == 0:
        index = random.choice([0, 1, 3, 4])
    else:
        index = random.choice([0, 2, 3, 4])

    color = shapes[0].fill_color if shapes[0].fill_color not in ["white", "none"] else shapes[0].border_color
    shape = shape_to_string(shapes[0])
    caption = captions["shape4"][index].replace("<2>", shape).replace("<1>", color)

    return caption

def generate_shape5(entity):
    shapes = entity[1]
    shape = random.choice(shapes)

    label = shape.label
    answer = shape_to_string(shape)


    index = random.randint(0, len(captions["shape5"])-1)
    caption = captions["shape5"][index].replace("<1>", label).replace("<2>", answer)

    return caption

def generate_shape6(entity):
    shapes = entity[1]

    answer = shape_to_string(shapes[0])
    negative_answer = ""

    for i in range(1, len(shapes)):
        if shape_to_string(shapes[i]) != answer:
            negative_answer = shape_to_string(shapes[i])
            break

    index = random.randint(0, len(captions["shape6"])-1)
    caption = captions["shape6"][index].replace("<1>", answer).replace("<2>", negative_answer)

    return caption

def generate_shape7(entity):
    

    shape = entity[1]

    answer = shape_to_string(shape)
    sides = {
        "pentagon": 5,
        "hexagon": 6,
        "heptagon": 7,
        "octagon": 8
    }[answer]

    index = random.randint(0, len(captions["shape7"])-1)
    caption = captions["shape7"][index].replace("<1>", str(sides)).replace("<2>", answer)

    return caption

def generate_shape8(entity):
    shapes = entity[1]
    answer_shape = shape_to_string(shapes[0])

    index = random.randint(0, len(captions["shape8"])-1)
    caption = captions["shape8"][index].replace("<1>", answer_shape)

    return caption

def generate_shape9(entity):
    shapes = entity[1]
    answer_shape = shape_to_string(shapes[0])

    background = entity[2]

    index = random.randint(0, len(captions["shape9"])-1)
    caption = captions["shape9"][index].replace("<1>", background.fill_color).replace("<2>", answer_shape)

    return caption

def generate_caption(diagram):
    captions_list = []
    for entity in diagram.entities:
        if entity[0] == "shape1":
            captions_list.append(generate_shape1(entity))
        elif entity[0] == "shape2":
            captions_list.append(generate_shape2(entity))
        elif entity[0] == "shape3":
            captions_list.append(generate_shape3(entity))
        elif entity[0] == "shape4":
            captions_list.append(generate_shape4(entity))
        elif entity[0] == "shape5":
            captions_list.append(generate_shape5(entity))
        elif entity[0] == "shape6":
            captions_list.append(generate_shape6(entity))
        elif entity[0] == "shape7":
            captions_list.append(generate_shape7(entity))
        elif entity[0] == "shape8":
            captions_list.append(generate_shape8(entity))
        elif entity[0] == "shape9":
            captions_list.append(generate_shape9(entity))
    return random.choice(captions_list)
