from .rules import *

import random
import roman

captions = {
  "color1": [
    "The image highlights a <1> prominently, showcasing its vibrant <2> hue.",
    "In the image, a <1> is clearly visible, featuring a beautiful shade of <2> that defines its appearance.",
    "This picture captures a <1> whose striking color of <2> draws the viewer's attention.",
    "The image focuses on a <1> with a distinct border colored in <2>, adding depth to its design.",
    "In the image, a <1> is filled uniformly with <2>, creating a balanced and eye-catching visual effect."
  ],
  "color2_a": [
    "The image presents multiple <1>s, each displaying a range of colors including <2> that collectively create a colorful ensemble.",
    "The image features several <1>s, and notably, one of them shines in a distinct <2> color.",
    "While the image includes a collection of <1>s, none exhibit the <2> hue; instead, only <3> variations of <1>s are present.",
    "The image is filled with an array of shapes, and a noticeable color palette is observed with shades including <1> throughout.",
    "Among the various elements, the image clearly depicts a <1> shape, adding to the overall composition.",
    "The image does not include a solitary <1> shape, but rather a set of <2> shapes that contribute to its dynamic layout."
  ],
  "color2_b": [
    "A polygon is central in the image, composed of a blend of colors, notably featuring <1>.",
    "The image showcases a <1> with sides that exhibit a harmonious combination of colors, specifically <2>.",
    "One can observe a detail in the image where the side of the <2> incorporates a subtle touch of <1>.",
    "The image confirms the presence of a <1> side within the <2>, emphasizing its distinct design element.",
    "The image clearly demonstrates that the side of the <2> does not contain any trace of <1>.",
    "Contrary to initial impressions, the image shows that the <2> does not feature a <1> side."
  ],
  "color3": [
    "The image presents a smooth gradation of colors, suggesting that the missing cell in the sequence would naturally be filled with <1>.",
    "Observing the seamless transition of colors in the image, it is evident that the ? cell is best complemented by the color <1>.",
    "By following the gradual color progression, the image indicates that the optimal color for the ? cell is <1>.",
    "The image exhibits a clear gradation, leading to the conclusion that the ? cell should naturally be <1> in color.",
    "Reflecting the smooth transition of colors, the image implies that the missing ? cell is ideally completed by the color <1>."
  ],
  "color5": [
    "The image features four distinct <1>s, among which the one with a radiant appearance is highlighted as <2>.",
    "Out of four visible <1>s, the image clearly accentuates the brilliance of the one in <2>.",
    "The image displays four <1>s with different brightness, ranging from the dark <2> to the brightest <5>, with the order <2>, <3>, <4>, <5>.",
    "Among the four <1>s in the image, one stands out for its deep hue, identified as <2> being the darkest.",
    "The image highlights four <1>s, and careful observation reveals that the darkest of them is <2>.",
    "In the image, the four <1>s are organized by brightness, beginning with the vivid <2> and descending in intensity to <5>, with the order <2>, <3>, <4>, <5>."
  ],
  "color6": [
    "The image presents four <1>s, with one exhibiting a notably intense saturation, identified as <2>.",
    "Among the four <1>s featured, the image draws attention to the one in <2> for its highest level of saturation.",
    "The image arranges four <1>s with diverse saturation, transitioning from the lowest (<2>) to the highest (<5>), with intermediate tones <3> and <4>.",
    "The image features a <1> that exhibits the most subdued saturation, clearly identified as <2>.",
    "Out of the four <1>s displayed, the image highlights the one with a muted, low saturation, denoted as <2>.",
    "In the image, the four <1>s have different saturation, starting with the most vivid <2> and tapering off to <5>, with intermediate tones <3> and <4>."
  ],
  "color7": [
    "The image, though filled with scattered objects, features a dominant background painted in <1>.",
    "Amidst a colorful array of objects, the image is set against a backdrop of <1>.",
    "The image’s overall tone is defined by its background, which is <1>.",
    "The image’s background is best characterized by the color <1>.",
    "The image is set against a layered background where the primary color is <1>."
  ],
  "color8": [
    "The image includes an arrow that clearly directs attention to a <1> <2>, highlighting its distinct color.",
    "An arrow in the image points towards a shape, which is predominantly colored <1>.",
    "The image features an arrow that emphasizes a <1> hue present on the <2>.",
    "In the image, the arrow directs the viewer’s eye to a shape that is colored <1> <2>, adding focus to the composition.",
    "The image clearly shows an arrow pointing to a <1> <2>, confirming its distinctive color and form.",
    "The image makes it evident that the arrow directs attention to a <1> <2>.",
    "In the image, the arrow points towards a <1> element.",
    "By observing the arrow's direction, the image reveals that the shape it highlights is characterized by the color <1>.",
    "The image features an arrow that emphasizes a shape, whose color is rendered as <1>, adding clarity to the scene."
  ],
  "color9": [
    "Within the image's palette of four colors, the one that is most <1> relative to <2> is distinguished as <3>.",
    "The image presents a selection of colors, where the <1> tone compared to <2> is clearly identified as <3>.",
    "Among the array of hues, the image suggests that the color most <1> to <2> is <3>.",
    "The image’s color composition reveals that the hue which is most <1> to <2> is best represented by <3>."
  ],
  "color10": [
    "The image displays a set of colors, with one standout hue, <1>, that markedly differs from the rest.",
    "Amidst a harmonious palette, the image features a distinct color, <1>, that contrasts sharply with the others.",
    "In the image, one color, <1>, stands out as particularly unique and noticeably different from the remaining hues.",
    "The image emphasizes a particular color, <1>, that distinctly stands apart from the other colors present.",
    "Among the various hues in the image, one color, <1>, is notably unique and draws attention with its individuality."
  ],
  "color11": [
    "The image features a line labeled <1>, which is rendered in a striking <2> color.",
    "A line, denoted as <1>, runs through the image, showcasing the <2> color.",
    "Within the image, the line identified as <1> is vividly colored in <2>.",
    "The image contains a line described as <1>, which is highlighted with the color <2>.",
    "Among the lines depicted, the one labeled <1> is distinguished by its <2> color.",
    "The diagram within the image reveals that the line described as <1> is represented by <2>, marked with its signature color."
  ],
  "color12": [
    "The image features a smooth color gradation that is intersected by <1> lines, creating an interesting visual disruption.",
    "A subtle gradation of colors in the image is divided by <1> lines, adding structure to the visual flow.",
    "The image displays a gentle gradient, carefully interrupted by <1> lines that segment the transition.",
    "The smooth gradation of colors in the image is artfully divided by <1> lines, contributing to its organized design."
  ],
  "color13": [
    "The image showcases a variety of colors that are uniform, except for a distinctive shade <2> that sets it apart.",
    "Among the options, the image reveals that only the color <2> displays a unique <1> that differentiates it from the rest.",
    "While most colors in the image share a common <1>, the color <2> stands out with a noticeably different attribute.",
    "The image’s color scheme is largely consistent, but the color <2> is particularly distinctive in its <1> feature."
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

def generate_color1(entity):
    object = entity[1]
    rand = entity[2]
    object_type = get_type(object)

    index = random.randint(0, len(captions["color1"])-1)

    while object_type == "text" and index == 3 or index == 4:
        index = random.randint(0, len(captions["color1"])-1)

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

        caption = captions["color1"][index].replace("<1>", object_name).replace("<2>", answer)
    
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

        caption = captions["color1"][index].replace("<1>", object_name).replace("<2>", answer)

    return caption

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

def generate_color2_a(entity):
    
    objects = entity[1]
    colors = entity[2]
    same_shape = entity[3]

    if same_shape:
        index = random.choice([0, 1, 2])
        if index == 0:
            shape = shape_to_string(objects[0])
            caption = captions["color2_a"][index].replace("<1>", shape).replace("<2>", ', '.join(colors))
        elif index == 1:
            shape = shape_to_string(objects[0])
            color = random.choice(colors)
            caption = captions["color2_a"][index].replace("<1>", shape).replace("<2>", color)
        elif index == 2:
            shape = shape_to_string(objects[0])
            negative_color = random.choice(list(set(color_list) - set(colors)))
            caption = captions["color2_a"][index].replace("<1>", shape).replace("<2>", negative_color).replace("<3>", ', '.join(colors))

    else:
        index = random.choice([3, 4, 5])
        if index == 3:
            caption = captions["color2_a"][index].replace("<1>", ', '.join(colors))
        elif index == 4:
            color = random.choice(colors)
            caption = captions["color2_a"][index].replace("<1>", color)
        elif index == 5:
            negative_color = random.choice(list(set(color_list) - set(colors)))
            caption = captions["color2_a"][index].replace("<1>", negative_color).replace("<2>", ', '.join(colors))
    
    return caption

def generate_color2_b(entity):
    
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
        caption = captions["color2_b"][index].replace("<1>", ', '.join(colors))
    elif index == 1:
        caption = captions["color2_b"][index].replace("<1>", shape).replace("<2>", ', '.join(colors))
    elif index == 2 or index == 3:
        color = random.choice(colors)
        caption = captions["color2_b"][index].replace("<1>", color).replace("<2>", shape)
    elif index == 4 or index == 5:
        negative_color = random.choice(list(set(color_list) - set(colors)))
        caption = captions["color2_b"][index].replace("<1>", negative_color).replace("<2>", shape)

    return caption

def generate_color3(entity):
    
    answer = entity[1]

    index = random.randint(0, len(captions["color3"])-1)

    caption = captions["color3"][index].replace("<1>", answer)

    return caption

def generate_color5(entity):
    
    shape = shape_to_string(entity[1][0])
    brightness = entity[2]
    brightness = [(i + 1, b) for i, b in enumerate(brightness)]
    brightness.sort(key=lambda x: x[1])
    rankings = [str(i[0]) for i in brightness]

    index = random.randint(0, len(captions["color5"])-1)

    if index == 0 or index == 1:
        caption = captions["color5"][index].replace("<1>", shape).replace("<2>", rankings[-1])
    elif index == 2:
        caption = captions["color5"][index].replace("<1>", shape).replace("<2>", rankings[0]).replace("<3>", rankings[1]).replace("<4>", rankings[2]).replace("<5>", rankings[3])
    elif index == 3 or index == 4:
        caption = captions["color5"][index].replace("<1>", shape).replace("<2>", rankings[0])
    elif index == 5:
        caption = captions["color5"][index].replace("<1>", shape).replace("<2>", rankings[-1]).replace("<3>", rankings[-2]).replace("<4>", rankings[-3]).replace("<5>", rankings[-4])

    return caption

def generate_color6(entity):
    shape = shape_to_string(entity[1][0])
    saturation = entity[2]
    saturation = [(i + 1, b) for i, b in enumerate(saturation)]
    saturation.sort(key=lambda x: x[1])
    rankings = [str(i[0]) for i in saturation]

    index = random.randint(0, len(captions["color6"])-1)

    if index == 0 or index == 1:
        caption = captions["color6"][index].replace("<1>", shape).replace("<2>", rankings[-1])
    elif index == 2:
        caption = captions["color6"][index].replace("<1>", shape).replace("<2>", rankings[0]).replace("<3>", rankings[1]).replace("<4>", rankings[2]).replace("<5>", rankings[3])
    elif index == 3 or index == 4:
        caption = captions["color6"][index].replace("<1>", shape).replace("<2>", rankings[0])
    elif index == 5:
        caption = captions["color6"][index].replace("<1>", shape).replace("<2>", rankings[-1]).replace("<3>", rankings[-2]).replace("<4>", rankings[-3]).replace("<5>", rankings[-4])

    return caption

def genrate_color7(entity):
    
    background_color = entity[1]

    index = random.randint(0, len(captions["color7"])-1)

    negative_colors = not_existing_colors([background_color])
    negative_colors = random.sample(negative_colors, random.randint(2, 4))

    colors = [background_color] + negative_colors
    random.shuffle(colors)
    right_index = colors.index(background_color)
    
    options, answer_option = option_generation(colors, right_index)

    caption = captions["color7"][index].replace("<1>", background_color).replace("<2>", options).replace("<3>", answer_option)

    return caption

def generate_color8(entity):
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
    
    index = random.randint(0, len(captions["color8"])-1)

    caption = captions["color8"][index].replace("<1>", answer_color).replace("<2>", shape).replace("<4>", options).replace("<3>", negative_answer).replace("<5>", answer_option)

    return caption

def generate_color9(entity):
    rand = entity[1]
    answer = entity[2]
    rand2 = entity[3]

    if rand == 0:
        q_type = 'same'
    else:
        q_type = random.choice(['the most similar', 'the closest'])

    p_type = 'topmost' if rand2 == 0 else 'leftmost'

    index = random.randint(0, len(captions["color9"])-1)

    caption = captions["color9"][index].replace("<1>", q_type).replace("<2>", p_type).replace("<3>", answer)

    return caption

def generate_color10(entity):
    label = entity[1]

    index = random.randint(0, len(captions["color10"])-1)

    caption = captions["color10"][index].replace("<1>", label)

    return caption

def generate_color11(entity):
    
    colors = entity[1]
    labels = entity[2]

    index = random.randint(0, len(captions["color11"])-1)
    color, label = random.choice(list(zip(colors, labels)))

    caption = captions["color11"][index].replace("<1>", label).replace("<2>", color)

    return caption

def generate_color12(entity):
        
    n = entity[1]

    index = random.randint(0, len(captions["color12"])-1)

    caption = captions["color12"][index].replace("<1>", str(n))

    return caption

def generate_color13(entity):
    
    variation = entity[1]
    answer = entity[2]

    variations = {
        0: "saturation",
        1: "brightness"
    }

    index = random.randint(0, len(captions["color13"])-1)

    caption = captions["color13"][index].replace("<1>", variations[variation]).replace("<2>", answer)

    return caption

def generate_caption(diagram):
    captions_list = []
    for entity in diagram.entities:
        if entity[0] == "color1":
            captions_list.append(generate_color1(entity))
        elif entity[0] == "color2_a":
            captions_list.append(generate_color2_a(entity))
        elif entity[0] == "color2_b":
            captions_list.append(generate_color2_b(entity))
        elif entity[0] == "color3":
            captions_list.append(generate_color3(entity))
        elif entity[0] == "color5":
            captions_list.append(generate_color5(entity))
        elif entity[0] == "color6":
            captions_list.append(generate_color6(entity))
        elif entity[0] == "color7":
            captions_list.append(genrate_color7(entity))
        elif entity[0] == "color8":
            captions_list.append(generate_color8(entity))
        elif entity[0] == "color9":
            captions_list.append(generate_color9(entity))
        elif entity[0] == "color10":
            captions_list.append(generate_color10(entity))
        elif entity[0] == "color11":
            captions_list.append(generate_color11(entity))
        elif entity[0] == "color12":
            captions_list.append(generate_color12(entity))
        elif entity[0] == "color13":
            captions_list.append(generate_color13(entity))
    return random.choice(captions_list)