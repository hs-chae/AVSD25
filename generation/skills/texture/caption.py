from .rules import *
import roman

captions = {
  "texture1": [
    "This image features <1> lines, with one line uniquely styled as <2> that clearly stands out from the rest.",
    "Among the <1> lines shown, the line identified as <2> displays a distinct style that sets it apart.",
    "The picture displays <1> lines, where one particular line, with <2> color, is distinguished by a unique style.",
    "Out of the <1> lines present, the line with the unique <2> color is highlighted by its different style.",
    "In an arrangement of <1> lines, one line is notably distinct in its styling, indicated by <2>.",
    "From the <1> options provided, the line marked as <2> is distinguished by its different style."
  ],
  "texture2": [
    "This image features several lines where <1> shares its style with <2>, both exhibiting a <3> pattern.",
    "Among the lines present, the one labeled <2> mirrors the style of <1>, characterized by a <3> appearance.",
    "The picture reveals that lines <1> and <2> share an identical style, defined by their <3> characteristics.",
    "Within the provided options, the line indicated as <3> exhibits the same style as <1>, as suggested by <2>.",
    "Out of <1> depicted lines, the line labeled <4> matches the style of <2>, as hinted by <3>.",
    "The image shows that line <2> possesses the same <3> style as <1> among the available options.",
    "Among the depicted lines, <2> exhibits the same distinct <3> style as <1>.",
    "Reviewing the numbered lines, it is clear that <2> mirrors the style of <1>, defined by a <3> pattern."
  ],
  "texture3_a": [
    "The image shows four shapes, with shape <1> standing out due to its distinct texture compared to the others.",
    "Out of the four shapes presented, shape <1> is uniquely textured and clearly different from the rest.",
    "Among four displayed shapes, shape <1> is notably different in texture from the remaining ones.",
    "In this collection of four shapes, shape <1> is confirmed to have a uniquely different texture.",
    "In an image featuring four shapes, one shape with a distinct texture is highlighted by its color, identified as <1>.",
    "Among the four shapes, the one marked as <1> stands out by its unique texture and corresponding color.",
    "The image displays four shapes, where the uniquely textured shape is identified by its color, <1>."
  ],
  "texture4": [
    "In an image with four options, one <1> is observed to share the same texture as the <2> <1>, specifically option <3>.",
    "The image features a <1> that matches the texture of the <2> <1>, identified as <3>.",
    "Among the options, the <1> labeled <3> mirrors the texture of the <2> <1> perfectly.",
    "Out of four available options, one <1> (option <3>) is distinct in texture from the <2> <1>.",
    "The image clearly shows that option <3> is the <1> with a texture different from the <2> <1>.",
    "Within the given options, the <1> labeled <3> stands out with a contrasting texture compared to the <2> <1>."
  ],
  "texture6": [
    "The image clearly displays line <1> with a line style characterized as <2>.",
    "Line <1> in the image is presented with a distinct <2> style.",
    "Within the polygon shown, line <1> exhibits a <2> line style.",
    "The depicted line <1> is associated with the <2> style.",
    "It is confirmed by the image that line <1> has a <2> style.",
    "The image indicates that line <1> features a <2> style."
  ],
  "texture7": [
    "The image shows a line segment divided by its style into <1> distinct parts.",
    "A line segment in the image is segmented by its style into <1> parts.",
    "Observing the line’s varying style, it is clearly divided into <1> segments.",
    "The image presents a line segmented by style into <1> distinct parts.",
    "The line is divided by changes in style, forming a total of <1> intervals.",
    "Segmented by its style, the line in the image is divided into <1> intervals.",
    "The image reveals that the line is distinctly segmented into <1> parts by its style.",
    "A clear segmentation by style divides the line in the image into <1> parts."
  ],
  "texture8": [
    "Among the <1> lines, each with a unique style, the line <2> is noted for its most dense pattern.",
    "Of the <1> lines present, line <2> exhibits the most densely patterned style.",
    "The image shows a line (<2>) that has the highest number of breaks per unit length.",
    "Among the uniquely styled <1> lines, line <2> is distinguished by its most sparse pattern.",
    "Out of the <1> lines, line <2> is characterized by a notably sparse style.",
    "In the image, line <2> stands out for having the fewest breaks per unit length.",
    "The lines in the image are arranged from most dense to most sparse style, with the order given as <2>.",
    "By counting breaks per unit length, the lines are ordered from dense to sparse, resulting in the order <2>.",
    "The image displays an ordering of lines from sparse to dense style, specified as <2>.",
    "Counting the breaks per unit length, the lines are arranged from sparse to dense style, with the order being <2>."
  ],
  "texture9": [
    "The image, featuring <1> lines, exhibits <2> distinct types of line styles, including a <3> pattern.",
    "Focusing solely on the styles, the image shows <2> types of line style, notably including a <3> pattern.",
    "In the image, a total of <2> different line styles are present, one of which is the <3> style.",
    "The image reveals <2> distinct line styles, among which is the characteristic <3> style."
  ],
  "texture10": [
    "The image contains <2> lines of <1> style.",
    "Upon inspection, there are <2> lines identified as <1> in the image.",
    "The picture shows a total of <2> <1> lines.",
    "A detailed look at the diagram reveals <2> lines categorized as <1> line."
  ],
  "texture11": {
    "one_different": [
      "Among the <1> shapes present, one shape, <2>, is distinguished by a different line style.",
      "Out of <1> shapes, <2> stands out with a unique line style.",
      "The image confirms that <2> is drawn with a line style that differs from the rest.",
    ],
    "all_different": [
      "In the image, among various shapes, the one marked as <2> is drawn with a <1> line style.",
      "The picture features several shapes, with <2> being notable for its <1> line style.",
      "The depiction shows that <2> is rendered with a <1> line style.",
      "It is clear from the image that <2> is illustrated using a <1> line style."
    ]
  },
  "texture12": [
    "The arrangement of <1> lines in the image forms the shape of a <2>.",
    "The <1> lines in the image come together to create a <2> shape.",
    "By examining only the <1> lines, one can discern that they form a <2> shape.",
    "The image illustrates that the <1> lines combine to form a <2>.",
    "In the image, the <1> lines form a geometric shape that has <3> sides."
  ],
  "texture13": [
    "The image shows that the <1> is rendered in a <2> line style.",
    "In the image, the <1> is depicted with a <2> line style.",
    "Observing the <1>, it is clear that it features a <2> line style.",
    "It is confirmed that the <1> in the image is drawn with a <2> line style.",
    "The image clarifies that the <1> have a <2> style."
  ],
  "texture14": [
    "In an image with <1> scattered lines, the line with <3> <4> has the <2> line style.",
    "Among the <1> lines present, the <4> line is characterized by a <2> style.",
    "The image includes a <2> line characterized by a <3>, identified as <4>.",
    "Observing the image, there is a <2> line which  has <3> <4>."
  ],
  "texture15": [
    "The image features several lines, one of which exhibits a distinct style; this uniquely styled line is clearly marked with the <1> <2>.",
    "Among the various lines depicted, the one that stands out with a different style is easily identifiable by its <1> <2>.",
    "In a composition of <3> lines, the line with a contrasting style is highlighted by its <1>, <2>, which sets it apart from the others.",
    "This scene displays multiple lines, and the one with an unusual style is distinctly marked with the <1> <2>, drawing attention to its difference.",
    "Out of the lines presented in the image, the line that deviates from the common style is clearly annotated with the <1> <2>, making it the standout element."
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

def generate_texture1(entity):
    
    line_count = len(entity[1])
    lines = entity[1].copy()
    answer_line = lines[0]
    type = entity[2]
    
    if type == 0:
        random.shuffle(lines)
        answer_label = answer_line.label
        labels = list(map(lambda x: x.label, lines))
        index = random.choice([0, 1, 4, 5])

        caption = captions["texture1"][index].replace("<1>", str(line_count)).replace("<2>", 'line ' + answer_label)
    
    elif type == 1:
        random.shuffle(lines)
        answer_label = answer_line.start.label + answer_line.end.label
        labels = list(map(lambda x: x.start.label + x.end.label, lines))

        index = random.choice([0, 1, 4, 5])

        caption = captions["texture1"][index].replace("<1>", str(line_count)).replace("<2>", 'line ' + answer_label)

    elif type == 2:
        random.shuffle(lines)
        answer_color = answer_line.color

        index = random.choice([2, 3, 4, 5])

        caption = captions["texture1"][index].replace("<1>", str(line_count)).replace("<2>", answer_color)
    
    return caption

def generate_texture2(entity):
    
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

        if index in [0, 1, 2, 3]:
            caption = captions["texture2"][index].replace("<1>", "line " + question_label).replace("<2>", "line " + answer_label).replace("<3>", answer_line.style)
        else:
            caption = captions["texture2"][index].replace("<1>", str(len(lines)+1)).replace("<2>", "line " + question_label).replace("<4>", answer_label).replace("<3>", answer_line.style)

    elif type == 2:
        question_label = question_line.color
        answer_label = answer_line.color

        index = random.choice([0, 1, 2, 3])

        caption = captions["texture2"][index].replace("<1>", question_label + " colored line").replace("<2>", answer_label + " line").replace("<3>", answer_line.style)

    elif type == 3:
        index = random.choice([5, 6, 7])
        caption = captions["texture2"][index].replace("<1>", question_line.color + " line").replace("<2>", answer_line.label).replace("<3>", answer_line.style)

    return caption

def generate_texture3_a(entity):
    
    answer = entity[1]
    labeling = entity[2]

    if labeling in [0, 1]:
        index = random.choice([0, 1, 2, 3])
        caption = captions["texture3_a"][index].replace("<1>", answer)
    elif labeling == 2:
        index = random.choice([4, 5, 6])
        caption = captions["texture3_a"][index].replace("<1>", answer)

    return caption

def generate_texture4(entity):
    
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

    caption = captions["texture4"][index].replace("<1>", shape_name).replace("<2>", indicator).replace("<3>", answer)

    return caption

def generate_texture6(entity):
    lines = entity[1]
    label_type = entity[2]  # 0: label of line, 1: label of points
    
    question_index = random.choice(range(len(lines)))
    question_line = lines[question_index]
    question_label = question_line.label if label_type == 0 else [question_line.start.label + question_line.end.label, question_line.end.label + question_line.start.label][random.choice([0, 1])]
    answer = question_line.style

    index = random.choice([0, 1, 2, 3, 4, 5])

    caption = captions["texture6"][index].replace("<1>", question_label).replace("<2>", answer)

    return caption

def generate_texture7(entity):
    n_intervals = entity[1]
    index = random.choice(range(0, len(captions["texture7"])))

    caption = captions["texture7"][index].replace("<1>", str(n_intervals))

    return caption

def generate_texture8(entity):
    labels = entity[1]
    density = entity[2]
    index = random.choice(range(0, len(captions["texture8"])))

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
    
    
    caption = captions["texture8"][index].replace("<1>", str(len(labels))).replace("<2>", answer)

    return caption

def generate_texture9(entity):
    styles = list(set(entity[1]))
    n = len(entity[1])
    m = entity[2]

    random.shuffle(styles)
    index = random.choice(range(0, len(captions["texture9"])))

    caption = captions["texture9"][index].replace("<1>", str(n)).replace("<2>", str(m)).replace("<3>", ', '.join(styles))

    return caption

def generate_texture10(entity):
    
    style = entity[3]
    answer = entity[2]

    index = random.choice(range(0, len(captions["texture10"])))

    caption = captions["texture10"][index].replace("<1>", style).replace("<2>", str(answer))

    return caption

def generate_texture11(entity):
    
    shapes = entity[1]
    one_different = entity[2]
    styles = entity[3]

    if one_different:
        index = random.choice(range(0, len(captions["texture11"]["one_different"])))
        caption = captions["texture11"]["one_different"][index].replace("<1>", str(len(shapes))).replace("<2>", shapes[0])
    else:
        index = random.choice(range(0, len(captions["texture11"]["all_different"])))
        caption = captions["texture11"]["all_different"][index].replace("<1>", styles[0]).replace("<2>", shapes[0])

    return caption

def generate_texture12(entity):
    
    n = entity[1]
    style = entity[2]

    if n == 3:
        shape = "triangle"
    elif n == 4:
        shape = "quadranlge"
    elif n == 5:
        shape = "pentagon"

    index = random.choice(range(0, len(captions["texture12"])))

    caption = captions["texture12"][index].replace("<1>", style).replace("<2>", shape).replace("<3>", str(n))

    return caption

def generate_texture13(entity):
    
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

    index = random.choice(range(0, len(captions["texture13"])))

    caption = captions["texture13"][index].replace("<1>", line_name).replace("<2>", style).replace("<3>", negative_style)

    return caption

def generate_texture14(entity):
    
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

    index = random.choice(range(0, len(captions["texture14"])))

    caption = captions["texture14"][index].replace("<1>", str(n)).replace("<2>", style).replace("<3>", naming).replace("<4>", answer)

    return caption

def generate_texture15(entity):
    
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

    index = random.choice(range(0, len(captions["texture15"])))

    caption = captions["texture15"][index].replace("<1>", naming).replace("<2>", answer).replace("<3>", str(n))

    return caption

def generate_caption(diagram):
    captions_list = []
    for entity in diagram.entities:
        if entity[0] == 'texture1':
            captions_list.append(generate_texture1(entity))
        elif entity[0] == 'texture2':
            captions_list.append(generate_texture2(entity))
        elif entity[0] == 'texture3_a':
            captions_list.append(generate_texture3_a(entity))
        elif entity[0] == 'texture4':
            captions_list.append(generate_texture4(entity))
        elif entity[0] == 'texture6':
            captions_list.append(generate_texture6(entity))
        elif entity[0] == 'texture7':
            captions_list.append(generate_texture7(entity))
        elif entity[0] == 'texture8':
            captions_list.append(generate_texture8(entity))
        elif entity[0] == 'texture9':
            captions_list.append(generate_texture9(entity))
        elif entity[0] == 'texture10':
            captions_list.append(generate_texture10(entity))
        elif entity[0] == 'texture11':
            captions_list.append(generate_texture11(entity))
        elif entity[0] == 'texture12':
            captions_list.append(generate_texture12(entity))
        elif entity[0] == 'texture13':
            captions_list.append(generate_texture13(entity))
        elif entity[0] == 'texture14':
            captions_list.append(generate_texture14(entity))
        elif entity[0] == 'texture15':
            captions_list.append(generate_texture15(entity))
    return random.choice(captions_list)