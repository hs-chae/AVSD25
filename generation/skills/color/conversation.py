from .rules import *

import random
import roman

conversation_long = {
    "color1": [
        [
            "What is the color of the <1>?",
            "The color of the <1> is <2>."
        ],
        [
            "There is a <1> in the image. What is its color?",
            "<2> is the color of the <1>."
        ],
        [
            "What color is the <1> in the given picture?",
            "The <1> is <2>."
        ],
        [
            "Tell me the color of the border of the <1>.",
            "The border of the <1> is <2>."
        ],
        [
            "By what color is the <1> filled?",
            "The <1> is filled with <2>."
        ]
    ],
    "color2_a": [
        [
            "There are several <1>s in the image. List all the colors of the <1>s.",
            "The colors of the <1>s are <2>."
        ],
        [
            "In the given picture, is there any <1> with <2> color?",
            "Yes, there is a <2> <1>."
        ],
        [
            "In the given picture, is there any <1> with <2> color?",
            "No, there is no <2> <1>. I could only find <3> <1>s."
        ],
        [
            "There are shapes scattered in the image. Find all the colors that you can see in the shapes.",
            "I could find <1> in the shapes."
        ],
        [
            "Can you find a <1> shape in the image?",
            "Yes, I found a <1> shape."
        ],
        [
            "Can you find a <1> shape in the image?",
            "No, I could only find <2> shapes."
        ]
    ],
    "color2_b": [
        [
            "There is a polygon in the image. List all the colors that the polygon consists of.",
            "The polygon consists of <1>."
        ],
        [
            "List all the colors of the sides of the <1>.",
            "The sides of the <1> are <2>."
        ],
        [
            "Is there a <1> in the side of the <2>?",
            "Yes, there is <1> in the side of the <2>."
        ],
        [
            "There is a <1> side in the <2>. Is it true?",
            "True"
        ],
        [
            "Is there a <1> in the side of the <2>?",
            "No, there is no <1> in the side of the <2>."
        ],
        [
            "There is a <1> side in the <2>. Is it true?",
            "False"
        ]
    ],
    "color3": [
        [
            "You can see a gradual change in colors. Guess the color that should be in the ? cell. Choose your answer from th options that are given in the image.",
            "The color that should be in the ? cell is <1>."
        ],
        [
            "In the image, there is a gradation of colors. What color best fits the ? cell? Choose your answer from the options that are given in the image.",
            "<1> is the color that best fits the ? cell."
        ],
        [
            "Among the four color options in the image, which color should be in the ? cell in the image by extrapolating the gradual change?",
            "The best color for the ? cell is <1>."
        ],
        [
            "What color should be in the ? cell in the image by following the gradation of colors?",
            "The color that should be in the ? cell is <1>."
        ],
        [
            "Extrapolate the gradual change of colors in the image and choose the color that should be in the ? cell. You should choose from the options given in the image.",
            "The answer is <1>."
        ]
    ],
    "color5": [
        [
            "Among four <1>s in the image, choose the brightest one.",
            "The brightest <1> is <2>."
        ],
        [
            "You can see four <1>s in the image. What is the brightest?",
            "<2> is the brightest <1>."
        ],
        [
            "List four <1>s from the darkest to the brightest.",
            "<2>, <3>, <4>, <5>"
        ],
        [
            "What is the darkest <1> in the image?",
            "The darkest <1> is <2>."
        ],
        [
            "You can see four <1>s in the image. What is the darkest?",
            "<2> is the darkest <1>."
        ],
        [
            "List four <1>s from the brightest to the darkest.",
            "<2>, <3>, <4>, <5>"
        ]
    ],
    "color6": [
        [
            "Among four <1>s in the image, choose the one with highest saturation.",
            "The <1> with the highest saturation is <2>."
        ],
        [
            "You can see four <1>s in the image. What has the highest saturation?",
            "<2> is the <1> with the highest saturation."
        ],
        [
            "List four <1>s in the order of saturation (from low to high).",
            "<2>, <3>, <4>, <5>"
        ],
        [
            "What is <1> that has the lowest saturation in the image?",
            "The <1> with the lowest saturation is <2>."
        ],
        [
            "You can see four <1>s in the image. What has the lowest saturation?",
            "<2> is the <1> with the lowest saturation."
        ],
        [
            "List four <1>s in the order of saturation (from high to low).",
            "<2>, <3>, <4>, <5>"
        ]
    ],
    "color7": [
        [
            "There are objects scattered in the plane. What is the background color of the image?",
            "The background color of the image is <1>."
        ],
        [
            "In this image of diverse colors, what is the background color?",
            "<1> is the background color."
        ],
        [
            "Choose the background color of the image. <2>",
            "The answer is <3>"
        ],
        [
            "Which option best describes the background color of the image? <2>",
            "<3> describes the background color."
        ],
        [
            "What is the background color of the image? <2>",
            "The background color is <3> <1>."
        ]
    ],
    "color8": [
        [
            "What is the color of the <2> that an arrow is pointing to?",
            "The arrow is pointing to a <1> <2>."
        ],
        [
            "In the image, there is an arrow pointing to some shape. What is the color of that shape?",
            "<1> is the color of the shape that the arrow is pointing to."
        ],
        [
            "Which color of <2> is indicated by the arrow?",
            "The arrow indicates a <1>."
        ],
        [
            "Can you tell me the color of the shape that the arrow is pointing to?",
            "Yes, the arrow is pointing to a <1> <2>."
        ],
        [
            "Is the arrow pointing to a <1> <2>?",
            "Yes, the arrow is pointing to a <1> <2>."
        ],
        [
            "Is the arrow pointing to a <3> <2>?",
            "No, the arrow is pointing to a <1> <2>."
        ],
        [
            "Choose the color of the <3> that the arrow is pointing to. <4>",
            "The answer is <5>."
        ],
        [
            "Which option best describes the color of the shape that the arrow is pointing to? <4>",
            "<5> describes the color of the shape."
        ],
        [
            "What is the color of the shape that the arrow is pointing to? <4>",
            "The color of the shape is <5> <1>."
        ]
    ],
    "color9": [
        [
            "Among the four colors, which one is <1> to the <2> color?",
            "Color <3> is the <1> color."
        ],
        [
            "Which color is <1> to the <2> color?",
            "The <1> color is <3>."
        ],
        [
            "Choose the color that is <1> to the <2> color.",
            "The answer is <3>."
        ],
        [
            "Which option best describes the color that is <1> to the <2> color?",
            "<3>"
        ]
    ],
    "color10": [
        [
            "Choose the color that is significantly different from the others.",
            "Color <1> is significantly different from the others."
        ],
        [
            "Which color is significantly different from the rest?",
            "The color that is significantly different is <1>."
        ],
        [
            "Select the color that is most distinct from the others.",
            "The most distinct color is <1>."
        ],
        [
            "Which color stands out from the rest?",
            "The color <1> stands out from the rest."
        ],
        [
            "Choose the color that is most unique.",
            "The most unique color is <1>."
        ]
    ],
    "color11": [
        [
            "What is the color of line <1>?",
            "The color of line <1> is <2>."
        ],
        [
            "Tell me the color of the line <1> in the image.",
            "The color of the line <1> is <2>."
        ],
        [
            "What color is the line <1> in the given picture?",
            "The line <1> is <2>."
        ],
        [
            "Find the <2> line in the image.",
            "The <2> line is <1>."
        ],
        [
            "Which line is colored <2>?",
            "<1> is colored <2>."
        ],
        [
            "In the given diagram, what line is <2>?",
            "The <2> line is <1>."
        ]
    ],
    "color12": [
        [
            "There is a gradation of colors in the image. How many lines are interrupting the gradation?",
            "There are <1> lines interrupting the gradation."
        ],
        [
            "In the image, there is a gradation of colors. How many lines are splitting the gradation?",
            "The gradation is split by <1> lines."
        ],
        [
            "How many lines are interrupting the gradation of colors in the image?",
            "The gradation is interrupted by <1> lines."
        ],
        [
            "There is a gradation of colors in the image. How many lines are dividing the gradation?",
            "The gradation is divided by <1> lines."
        ]
    ],
    "color13": [
        [
            "There are multiple colors in the image. All the colors are same except one. Which color is different from the others?",
            "The color <2> is different from the others."
        ],
        [
            "In the options, only one color has a different <1>. Which color is it?",
            "The color <2> has a different <1>."
        ],
        [
            "Among the colors in the image, which one has a different <1> from the rest?",
            "The color <2> has a different <1>."
        ],
        [
            "Choose the color that is most distinctive in terms of <1>.",
            "The most distinctive color in terms of <1> is <2>."
        ]
    ]
}

conversation_short = {
    "color1": [
        [
            "What is the color of the <1>?",
            "<2>"
        ],
        [
            "There is a <1> in the image. What is its color?",
            "<2>"
        ],
        [
            "What color is the <1> in the given picture?",
            "<2>."
        ],
        [
            "Tell me the color of the border of the <1>.",
            "<2>"
        ],
        [
            "By what color is the <1> filled?",
            "<2>"
        ]
    ], 
    "color2_a": [
        [
            "There are several <1>s in the image. List all the colors of the <1>s.",
            "<2>."
        ],
        [
            "In the given picture, is there any <1> with <2> color?",
            "Yes"
        ],
        [
            "In the given picture, is there any <1> with <2> color?",
            "No"
        ],
        [
            "There are shapes scattered in the image. Find all the colors that you can see in the shapes.",
            "<1>"
        ],
        [
            "Can you find a <1> shape in the image?",
            "Yes"
        ],
        [
            "Can you find a <1> shape in the image?",
            "No"
        ]
    ],
    "color2_b": [
        [
            "There is a polygon in the image. List all the colors that the polygon consists of.",
            "<1>"
        ],
        [
            "List all the colors of the sides of the <1>.",
            "<2>"
        ],
        [
            "Is there a <1> in the side of the <2>?",
            "Yes"
        ],
        [
            "There is a <1> side in the <2>. Is it true?",
            "True"
        ],
        [
            "Is there a <1> in the side of the <2>?",
            "No"
        ],
        [
            "There is a <1> side in the <2>. Is it true?",
            "False"
        ]
    ],
    "color3": [
        [
            "You can see a gradual change in colors. Guess the color that should be in the ? cell. Choose your answer from th options that are given in the image.",
            "<1>"
        ],
        [
            "In the image, there is a gradation of colors. What color best fits the ? cell? Choose your answer from the options that are given in the image.",
            "<1>"
        ],
        [
            "Among the four color options in the image, which color should be in the ? cell in the image by extrapolating the gradual change?",
            "<1>"
        ],
        [
            "What color should be in the ? cell in the image by following the gradation of colors?",
            "<1>"
        ],
        [
            "Extrapolate the gradual change of colors in the image and choose the color that should be in the ? cell. You should choose from the options given in the image.",
            "<1>"
        ]
    ],
    "color5": [
        [
            "Among four <1>s in the image, choose the brightest one.",
            "<2>"
        ],
        [
            "You can see four <1>s in the image. What is the brightest?",
            "<2>"
        ],
        [
            "List four <1>s from the darkest to the brightest.",
            "<2>, <3>, <4>, <5>"
        ],
        [
            "What is the darkest <1> in the image?",
            "<2>"
        ],
        [
            "You can see four <1>s in the image. What is the darkest?",
            "<2>"
        ],
        [
            "List four <1>s from the brightest to the darkest.",
            "<2>, <3>, <4>, <5>"
        ]
    ],
    "color6": [
        [
            "Among four <1>s in the image, choose the one with highest saturation.",
            "<2>"
        ],
        [
            "You can see four <1>s in the image. What has the highest saturation?",
            "<2>"
        ],
        [
            "List four <1>s in the order of saturation (from low to high).",
            "<2>, <3>, <4>, <5>"
        ],
        [
            "What is <1> that has the lowest saturation in the image?",
            "<2>"
        ],
        [
            "You can see four <1>s in the image. What has the lowest saturation?",
            "<2>"
        ],
        [
            "List four <1>s in the order of saturation (from high to low).",
            "<2>, <3>, <4>, <5>"
        ]
    ],
    "color7": [
        [
            "There are objects scattered in the plane. What is the background color of the image?",
            "<1>"
        ],
        [
            "In this image of diverse colors, what is the background color?",
            "<1>"
        ],
        [
            "Choose the background color of the image. <2>",
            "<3>"
        ],
        [
            "Which option best describes the background color of the image? <2>",
            "<3>"
        ],
        [
            "What is the background color of the image? <2>",
            "<3>"
        ]
    ],
    "color8": [
        [
            "What is the color of the <2> that an arrow is pointing to?",
            "<1>"
        ],
        [
            "In the image, there is an arrow pointing to some shape. What is the color of that shape?",
            "<1>"
        ],
        [
            "Which color of <2> is indicated by the arrow?",
            "<1>"
        ],
        [
            "Can you tell me the color of the shape that the arrow is pointing to?",
            "<1>"
        ],
        [
            "Is the arrow pointing to a <1> <2>?",
            "Yes"
        ],
        [
            "Is the arrow pointing to a <3> <2>?",
            "No"
        ],
        [
            "Choose the color of the <3> that the arrow is pointing to. <4>",
            "<5>"
        ],
        [
            "Which option best describes the color of the shape that the arrow is pointing to? <4>",
            "<5>"
        ],
        [
            "What is the color of the shape that the arrow is pointing to? <4>",
            "<5>"
        ]
    ],
    "color9": [
        [
            "Among the four colors, which one is <1> to the <2> color?",
            "<3>"
        ],
        [
            "Which color is <1> to the <2> color?",
            "<3>"
        ],
        [
            "Choose the color that is <1> to the <2> color.",
            "<3>"
        ],
        [
            "Which option best describes the color that is <1> to the <2> color?",
            "<3>"
        ]
    ],
    "color10": [
        [
            "Choose the color that is significantly different from the others.",
            "<1>"
        ],
        [
            "Which color is significantly different from the rest?",
            "<1>"
        ],
        [
            "Select the color that is most distinct from the others.",
            "<1>"
        ],
        [
            "Which color stands out from the rest?",
            "<1>"
        ],
        [
            "Choose the color that is most unique.",
            "<1>"
        ]
    ],
    "color11": [
        [
            "What is the color of line <1>?",
            "<2>"
        ],
        [
            "Tell me the color of the line <1> in the image.",
            "<2>"
        ],
        [
            "What color is the line <1> in the given picture?",
            "<2>"
        ],
        [
            "Find the <2> line in the image.",
            "<1>"
        ],
        [
            "Which line is colored <2>?",
            "<1>"
        ],
        [
            "In the given diagram, what line is <2>?",
            "<1>"
        ]
    ],
    "color12": [
        [
            "There is a gradation of colors in the image. How many lines are interrupting the gradation?",
            "<1>"
        ],
        [
            "In the image, there is a gradation of colors. How many lines are splitting the gradation?",
            "<1>"
        ],
        [
            "How many lines are interrupting the gradation of colors in the image?",
            "<1>"
        ],
        [
            "There is a gradation of colors in the image. How many lines are dividing the gradation?",
            "<1>"
        ]
    ],
    "color13": [
        [
            "There are multiple colors in the image. All the colors are same except one. Which color is different from the others?",
            "<2>"
        ],
        [
            "In the options, only one color has a different <1>. Which color is it?",
            "<2>"
        ],
        [
            "Among the colors in the image, which one has a different <1> from the rest?",
            "<2>"
        ],
        [
            "Choose the color that is most distinctive in terms of <1>.",
            "<2>"
        ]
    ]
}

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

def get_type(object):
    if isinstance(object, Polygon):
        if object.n == 3:
            return "triangle"
        elif object.n == 4:
            return "square"
        elif object.n == 5:
            return "pentagon"
        elif object.n == 6:
            return "hexagon"
    elif isinstance(object, Circle):
        return "circle"
    elif isinstance(object, Star):
        return "star"
    elif isinstance(object, Heart):
        return "heart"
    elif isinstance(object, Text):
        return "text"
    elif isinstance(object, TextBox):
        return "textbox"
    
    return ""

def not_existing_colors(colors):
    return list(set(color_list) - set(colors))

def generate_color1(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    object = entity[1]
    rand = entity[2]
    object_type = get_type(object)

    index = random.randint(0, len(conversation["color1"])-1)

    while object_type == "text" and index == 3 or index == 4:
        index = random.randint(0, len(conversation["color1"])-1)

    if index == 0 or index == 1 or index == 2:
        if object_type == "text":
            object_name = f"text \"{object.text}\""
        elif object_type == "textbox":
            object_name = f"box containing text \"{object.text}\""
        else:
            object_name = object_type
        
        if object_type == "text":
            answer = object.color
        elif rand == 0:
            answer = object.border_color
        else:
            answer = object.fill_color

        q = conversation["color1"][index][0].replace("<1>", object_name)
        a = conversation["color1"][index][1].replace("<1>", object_name).replace("<2>", answer)
    
    elif index == 3 or index == 4:
        object_type = get_type(object)
        if object_type == "text":
            object_name = f"text \"{object.text}\""
        elif object_type == "textbox":
            object_name = f"box containing text \"{object.text}\""
        else:
            object_name = object_type
        
        if index == 3:
            answer = object.border_color
        else:
            answer = object.fill_color

        q = conversation["color1"][index][0].replace("<1>", object_name)
        a = conversation["color1"][index][1].replace("<1>", object_name).replace("<2>", answer)

    return q, a

def shape_to_string(shape):
    if isinstance(shape, Circle):
        answer = "circle"
    elif isinstance(shape, Polygon):
        if shape.n == 3:
            answer = "triangle"
        elif shape.n == 4:
            answer = "square"
        elif shape.n == 5:
            answer = "pentagon"
        elif shape.n == 6:
            answer = "hexagon"
    elif isinstance(shape, Star):
        answer = "star"
    elif isinstance(shape, Heart):
        answer = "heart"
    elif isinstance(shape, Text):
        answer = f"text"
    elif isinstance(shape, TextBox):
        answer = f"box containing text"
    elif isinstance(shape, Line):
        answer = "line"
    elif isinstance(shape, Point):
        answer = "point"
    return answer

def generate_color2_a(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    objects = entity[1]
    colors = entity[2]
    same_shape = entity[3]

    if same_shape:
        index = random.choice([0, 1, 2])
        if index == 0:
            shape = shape_to_string(objects[0])
            q = conversation["color2_a"][index][0].replace("<1>", shape)
            a = conversation["color2_a"][index][1].replace("<1>", shape).replace("<2>", ', '.join(colors))
        elif index == 1:
            shape = shape_to_string(objects[0])
            color = random.choice(colors)
            q = conversation["color2_a"][index][0].replace("<1>", shape).replace("<2>", color)
            a = conversation["color2_a"][index][1].replace("<1>", shape).replace("<2>", color)
        elif index == 2:
            shape = shape_to_string(objects[0])
            negative_color = random.choice(list(set(color_list) - set(colors)))
            q = conversation["color2_a"][index][0].replace("<1>", shape).replace("<2>", negative_color)
            a = conversation["color2_a"][index][1].replace("<1>", shape).replace("<2>", negative_color).replace("<3>", ', '.join(colors))

    else:
        index = random.choice([3, 4, 5])
        if index == 3:
            q = conversation["color2_a"][index][0]
            a = conversation["color2_a"][index][1].replace("<1>", ', '.join(colors))
        elif index == 4:
            color = random.choice(colors)
            q = conversation["color2_a"][index][0].replace("<1>", color)
            a = conversation["color2_a"][index][1].replace("<1>", color)
        elif index == 5:
            negative_color = random.choice(list(set(color_list) - set(colors)))
            q = conversation["color2_a"][index][0].replace("<1>", negative_color)
            a = conversation["color2_a"][index][1].replace("<2>", ', '.join(colors))
    
    return q, a

def generate_color2_b(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    n_to_shape = {
        3: "triangle",
        4: "square",
        5: "pentagon",
        6: "hexagon"
    }

    n = entity[1]
    colors = entity[2]
    shape = n_to_shape[n]

    index = random.choice([0, 1, 2, 3, 4, 5])

    if index == 0:
        q = conversation["color2_b"][index][0]
        a = conversation["color2_b"][index][1].replace("<1>", ', '.join(colors))
    elif index == 1:
        q = conversation["color2_b"][index][0].replace("<1>", shape)
        a = conversation["color2_b"][index][1].replace("<1>", shape).replace("<2>", ', '.join(colors))
    elif index == 2 or index == 3:
        color = random.choice(colors)
        q = conversation["color2_b"][index][0].replace("<1>", color).replace("<2>", shape)
        a = conversation["color2_b"][index][1].replace("<1>", color).replace("<2>", shape)
    elif index == 4 or index == 5:
        negative_color = random.choice(list(set(color_list) - set(colors)))
        q = conversation["color2_b"][index][0].replace("<1>", negative_color).replace("<2>", shape)
        a = conversation["color2_b"][index][1].replace("<1>", negative_color).replace("<2>", shape)

    return q, a

def generate_color3(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    answer = entity[1]

    index = random.randint(0, len(conversation["color3"])-1)

    q = conversation["color3"][index][0]
    a = conversation["color3"][index][1].replace("<1>", answer)

    return q, a

def generate_color5(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shape = shape_to_string(entity[1][0])
    brightness = entity[2]
    brightness = [(i + 1, b) for i, b in enumerate(brightness)]
    brightness.sort(key=lambda x: x[1])
    rankings = [str(i[0]) for i in brightness]

    index = random.randint(0, len(conversation["color5"])-1)

    if index == 0 or index == 1:
        q = conversation["color5"][index][0].replace("<1>", shape)
        a = conversation["color5"][index][1].replace("<1>", shape).replace("<2>", rankings[-1])
    elif index == 2:
        q = conversation["color5"][index][0].replace("<1>", shape)
        a = conversation["color5"][index][1].replace("<2>", rankings[0]).replace("<3>", rankings[1]).replace("<4>", rankings[2]).replace("<5>", rankings[3])
    elif index == 3 or index == 4:
        q = conversation["color5"][index][0].replace("<1>", shape)
        a = conversation["color5"][index][1].replace("<1>", shape).replace("<2>", rankings[0])
    elif index == 5:
        q = conversation["color5"][index][0].replace("<1>", shape)
        a = conversation["color5"][index][1].replace("<2>", rankings[-1]).replace("<3>", rankings[-2]).replace("<4>", rankings[-3]).replace("<5>", rankings[-4])

    return q, a

def generate_color6(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shape = shape_to_string(entity[1][0])
    saturation = entity[2]
    saturation = [(i + 1, b) for i, b in enumerate(saturation)]
    saturation.sort(key=lambda x: x[1])
    rankings = [str(i[0]) for i in saturation]

    index = random.randint(0, len(conversation["color6"])-1)

    if index == 0 or index == 1:
        q = conversation["color6"][index][0].replace("<1>", shape)
        a = conversation["color6"][index][1].replace("<1>", shape).replace("<2>", rankings[-1])
    elif index == 2:
        q = conversation["color6"][index][0].replace("<1>", shape)
        a = conversation["color6"][index][1].replace("<2>", rankings[0]).replace("<3>", rankings[1]).replace("<4>", rankings[2]).replace("<5>", rankings[3])
    elif index == 3 or index == 4:
        q = conversation["color6"][index][0].replace("<1>", shape)
        a = conversation["color6"][index][1].replace("<1>", shape).replace("<2>", rankings[0])
    elif index == 5:
        q = conversation["color6"][index][0].replace("<1>", shape)
        a = conversation["color6"][index][1].replace("<2>", rankings[-1]).replace("<3>", rankings[-2]).replace("<4>", rankings[-3]).replace("<5>", rankings[-4])

    return q, a

def genrate_color7(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    background_color = entity[1]

    index = random.randint(0, len(conversation["color7"])-1)

    negative_colors = not_existing_colors([background_color])
    negative_colors = random.sample(negative_colors, random.randint(2, 4))

    colors = [background_color] + negative_colors
    random.shuffle(colors)
    right_index = colors.index(background_color)
    
    options, answer_option = option_generation(colors, right_index)

    q = conversation["color7"][index][0].replace("<2>", options)
    a = conversation["color7"][index][1].replace("<1>", background_color).replace("<3>", answer_option)

    return q, a

def generate_color8(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    shapes = entity[1]

    colors = []

    for shape in shapes:
        if shape.fill_color != "none":
            colors.append(shape.fill_color)
        else:
            colors.append(shape.border_color)

    answer_color = colors[0]
    shape = shape_to_string(shapes[0])

    negative_answer = random.choice(list(set(colors)))
    while negative_answer == answer_color:
        negative_answer = random.choice(list(set(colors)))

    if len(colors) >= 4:
        options = colors[:4]
        random.shuffle(options)
        right_index = options.index(answer_color)
        options, answer_option = option_generation(options, right_index)
    else:
        options = colors + not_existing_colors(colors)[:4-len(colors)]
        random.shuffle(options)
        right_index = options.index(answer_color)
        options, answer_option = option_generation(options, right_index)
    
    index = random.randint(0, len(conversation["color8"])-1)

    q = conversation["color8"][index][0].replace("<1>", answer_color).replace("<2>", shape).replace("<4>", options).replace("<3>", negative_answer)
    a = conversation["color8"][index][1].replace("<1>", answer_color).replace("<2>", shape).replace("<5>", answer_option)

    return q, a

def generate_color9(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    rand = entity[1]
    answer = entity[2]
    rand2 = entity[3]

    if rand == 0:
        q_type = 'same'
    else:
        q_type = random.choice(['the most similar', 'the closest'])

    p_type = 'topmost' if rand2 == 0 else 'leftmost'

    index = random.randint(0, len(conversation["color9"])-1)

    q = conversation["color9"][index][0].replace("<1>", q_type).replace("<2>", p_type)
    a = conversation["color9"][index][1].replace("<1>", q_type).replace("<2>", p_type).replace("<3>", answer)

    return q, a

def generate_color10(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    label = entity[1]

    index = random.randint(0, len(conversation["color10"])-1)

    q = conversation["color10"][index][0]
    a = conversation["color10"][index][1].replace("<1>", label)

    return q, a

def generate_color11(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    colors = entity[1]
    labels = entity[2]

    index = random.randint(0, len(conversation["color11"])-1)
    color, label = random.choice(list(zip(colors, labels)))

    q = conversation["color11"][index][0].replace("<1>", label).replace("<2>", color)
    a = conversation["color11"][index][1].replace("<1>", label).replace("<2>", color)

    return q, a

def generate_color12(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short
    
    n = entity[1]

    index = random.randint(0, len(conversation["color12"])-1)

    q = conversation["color12"][index][0]
    a = conversation["color12"][index][1].replace("<1>", str(n))

    return q, a

def generate_color13(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    variation = entity[1]
    answer = entity[2]

    variations = {
        0: "saturation",
        1: "brightness"
    }

    index = random.randint(0, len(conversation["color13"])-1)

    q = conversation["color13"][index][0].replace("<1>", variations[variation])
    a = conversation["color13"][index][1].replace("<1>", variations[variation]).replace("<2>", answer)

    return q, a

def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        if entity[0] == "color1":
            conversation_list.append(generate_color1(entity, long))
        elif entity[0] == "color2_a":
            conversation_list.append(generate_color2_a(entity, long))
        elif entity[0] == "color2_b":
            conversation_list.append(generate_color2_b(entity, long))
        elif entity[0] == "color3":
            conversation_list.append(generate_color3(entity, long))
        elif entity[0] == "color5":
            conversation_list.append(generate_color5(entity, long))
        elif entity[0] == "color6":
            conversation_list.append(generate_color6(entity, long))
        elif entity[0] == "color7":
            conversation_list.append(genrate_color7(entity, long))
        elif entity[0] == "color8":
            conversation_list.append(generate_color8(entity, long))
        elif entity[0] == "color9":
            conversation_list.append(generate_color9(entity, long))
        elif entity[0] == "color10":
            conversation_list.append(generate_color10(entity, long))
        elif entity[0] == "color11":
            conversation_list.append(generate_color11(entity, long))
        elif entity[0] == "color12":
            conversation_list.append(generate_color12(entity, long))
        elif entity[0] == "color13":
            conversation_list.append(generate_color13(entity, long))
    return conversation_list