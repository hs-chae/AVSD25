import random
import roman

captions = {
  "symbol_1_a": [
    "The image shows a triangle with a distinct angle symbol that highlights one of its angles, identified as <1>.",
    "A triangle is presented where an angle is marked by a special symbol, indicating that the highlighted angle is <1>.",
    "In the image, a triangle features an angle symbol that emphasizes one of its angles as <1>, drawing attention to its significance.",
    "The picture displays a triangle with an angle marker that clearly points out angle <1> as the featured angle.",
    "A triangle is depicted with an angle symbol, and the visual cue suggests that the emphasized angle is represented as <1>."
  ],
  "symbol_1_b": [
    "The image presents an angle symbol formed by the intersection of two lines, which are labeled <1> and <2>.",
    "Two lines in the image meet at a point marked by an angle symbol, indicating that the angle is created by lines <1> and <2>.",
    "A clear angle symbol in the image points to the intersection of two lines, namely <1> and <2>, forming the indicated angle.",
    "In the picture, the angle is defined by the meeting point of lines <1> and <2>, as highlighted by the single angle symbol."
  ],
  "symbol_1_c": [
    "The image features several lines with an angle symbol whose color, shown as <2>, indicates that the angle formed is perpendicular.",
    "A set of intersecting lines is shown with an angle symbol; its color, <2>, signifies that the marked angle is a right angle.",
    "Within the image, two lines form a perpendicular intersection, clearly indicated by the angle symbol linking line <1> and line <2>.",
    "The picture illustrates a perpendicular angle created by the intersection of lines <1> and <2>, as denoted by a distinct angle symbol."
  ],
  "symbol_2_a": [
    "Multiple words appear in the image, with a visual marker identifying the correct word as \"<1>\".",
    "The image displays a group of words where a green symbol highlights \"<1>\" as the correct choice.",
    "Among several words shown, the red and green symbols in the image indicate that only \"<1>\" is correct while the others are not.",
    "In the picture, the correct word is clearly marked by a symbol, singling out \"<1>\" from the rest."
  ],
  "symbol_2_b": [
    "A word in the image is enclosed within a <1> colored box, drawing attention to the word \"<2>\".",
    "The image features a word boxed in <1> color, which distinguishes it as \"<2>\".",
    "Within the picture, one word stands out by being framed in a <1> box, revealing it to be \"<2>\".",
    "A distinct <1> box in the image encloses a word that is identified as \"<2>\"."
  ],
  "symbol3_a": [
    "The image shows two lines accompanied by a <1> symbol that clearly indicates they are parallel.",
    "A <1> symbol in the image marks the relationship between two lines, showing that they run parallel to each other.",
    "In the picture, the presence of a <1> symbol signifies that the two lines it relates to are parallel.",
    "By interpreting the <1> symbol, the image reveals that the two depicted lines are parallel.",
    "A <1> symbol in the image confirms that the lines shown are parallel.",
    "According to the <1> symbol featured in the image, the two lines are parallel."
  ],
  "symbol3_b": [
    "The image includes a <1> symbol that denotes the two lines shown are of equal length.",
    "A <1> symbol in the picture indicates that the lines it accompanies have the same length.",
    "In the image, the <1> symbol serves as a cue that the two lines are equally long.",
    "By interpreting the <1> symbol, one can see that the two lines in the image share the same length.",
    "The visual cue of the <1> symbol in the image highlights that the lines are identical in length.",
    "According to the <1> symbol, the two lines depicted in the image have the same length."
  ],
  "symbol4_a": [
    "The image displays several lines, and a <1> symbol highlights that lines <2> and <3> are of equal length.",
    "In the picture, the <1> symbol directs attention to the fact that lines <2> and <3> match in length.",
    "A <1> symbol in the image marks a pair of lines—<2> and <3>—that are equal in length.",
    "The visual cue provided by the <1> symbol in the image shows that lines <2> and <3> are identical in length.",
    "By following the <1> symbol in the image, it is evident that line <3> is the one that matches line <2> in length.",
    "The image clearly uses a <1> symbol to indicate that the pair of lines <2> and <3> have the same length."
  ],
  "symbol4_b": [
    "A polygon is featured in the image with a <1> symbol indicating that sides <2> and <3> are equal in length.",
    "The image of the polygon uses a <1> symbol to mark sides <2> and <3> as having the same length.",
    "Within the polygon shown, a <1> symbol highlights that sides <2> and <3> are of equal length.",
    "The picture emphasizes a pair of equal-length sides—<2> and <3>—by using a <1> symbol.",
    "Following the cue of the <1> symbol, the image reveals that side <3> matches side <2> in length.",
    "The polygon in the image is annotated with a <1> symbol, indicating that the sides <2> and <3> are equally long."
  ],
  "symbol4_c": [
    "The image presents <2> visual cues suggesting that the grouping lines <1> as a same-length pair is the correct interpretation.",
    "The <2> symbol makes it clear that lines <1> have the same length.",
    "The highlighted selection indicates that lines <1> are of equal length.",
    "The <2> visual cues in the image point out that the proper interpretation is that the two lines designated as <1> share the same length.",
    "The picture demonstrates that the length of lines marked as <1> is equal."
  ],
  "symbol5": [
    "The image features a prominent <1> symbol along with several options, and it clearly points to \"<2>\" as the correct interpretation.",
    "A <1> symbol in the image indicates that <2>",
    "The visual cue confirms that <2>",
    "The picture uses a <1> symbol to highlight that <2>",
    "Observing the <1> symbol in the image makes it evident that <2>"
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

def generate_symbol_1_a(entity):
    
    index = random.randint(0, len(captions["symbol_1_a"]) - 1)

    caption = captions["symbol_1_a"][index].replace("<1>", entity[3].label)

    return caption

def generate_symbol_1_b(entity):
    
    index = random.randint(0, len(captions["symbol_1_b"]) - 1)

    if index == 0 or index == 1 or index == 2 or index == 3:
        caption = captions["symbol_1_b"][index].replace("<1>", entity[1].label).replace("<2>", entity[2].label)

    return caption

def generate_symbol_1_c(entity):
    
    type = entity[1]

    if type == 'color':
        colors = entity[2]
        answer = colors[-1]
        random.shuffle(colors)
        answer_index = colors.index(answer)
        options, answer_option = option_generation(colors, answer_index)

        index = random.choice([0, 1])
        caption = captions["symbol_1_c"][index].replace("<2>", answer)

    else:
        l1, l2 = entity[3], entity[4]
        label1, label2 = l1.label, l2.label

        index = random.choice([2, 3])
        caption = captions["symbol_1_c"][index].replace("<1>", label1).replace("<2>", label2)
    
    return caption

def generate_symbol_2_a(entity):
    
    words = entity[1]
    correct = entity[2]

    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", words[correct])

    return caption

def generate_symbol_2_b(entity):
    
    color = entity[1]
    answer = entity[2]

    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", color).replace("<2>", answer)

    return caption

def generate_symbol3_a(entity):
    
    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", entity[1])

    return caption

def generate_symbol3_b(entity):
    
    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", entity[1])

    return caption

def generate_symbol4_a(entity):
    
    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", entity[1]).replace("<2>", entity[2]).replace("<3>", entity[3])

    return caption

def generate_symbol4_b(entity):
    
    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", entity[1]).replace("<2>", entity[2]).replace("<3>", entity[3])

    return caption

def generate_symbol4_c(entity):
    
    index = random.randint(0, len(captions[entity[0]]) - 1)

    color = entity[1]
    center_label = entity[2]
    p1_label = entity[3]
    p2_label = entity[4]
    
    l1 = p1_label + center_label if random.choice([True, False]) else center_label + p1_label
    l2 = p2_label + center_label if random.choice([True, False]) else center_label + p2_label
    # l3 = p1_label + p2_label if random.choice([True, False]) else p2_label + p1_label

    answer = f'{l1} and {l2}' if random.choice([True, False]) else f'{l2} and {l1}'

    caption = captions[entity[0]][index].replace("<1>", answer).replace("<2>", color)

    return caption

def generate_symbol5(entity):
    
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

    index = random.randint(0, len(captions["symbol5"]) - 1)

    caption = captions["symbol5"][index].replace("<1>", color).replace("<2>", answer)

    return caption


def generate_caption(diagram):
    captions_list = []
    for entity in diagram.entities:
        if entity[0] == 'symbol_1_a':
            caption = generate_symbol_1_a(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol_1_b':
            caption = generate_symbol_1_b(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol_1_c':
            caption = generate_symbol_1_c(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol_2_a':
            caption = generate_symbol_2_a(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol_2_b':
            caption = generate_symbol_2_b(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol3_a':
            caption = generate_symbol3_a(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol3_b':
            caption = generate_symbol3_b(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol4_a':
            caption = generate_symbol4_a(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol4_b':
            caption = generate_symbol4_a(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol4_c':
            caption = generate_symbol4_c(entity)
            captions_list.append((caption))
        elif entity[0] == 'symbol5':
            caption = generate_symbol5(entity)
            captions_list.append((caption))
    return random.choice(captions_list)
