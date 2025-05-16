from .rules import *

captions = {
  "direction1": [
    "The image displays <1> arrows arranged randomly, with one arrow, labeled <2>, noticeably oriented in a direction that differs from the others.",
    "In the diagram featuring <1> arrows, the arrow labeled <2> stands out by pointing in a uniquely distinctive direction.",
    "The picture features multiple arrows, among which arrow <2> is distinguished by its unique orientation compared to the rest.",
    "The image contains several arrows, and careful observation reveals that arrow <2> deviates from the common orientation."
  ],
  "direction2": [
    "The image shows a single arrow that is clearly directed towards the <2>.",
    "In the diagram, a lone arrow is oriented towards the <2>, emphasizing its specific direction.",
    "This illustration presents one arrow, which is pointed in the direction of the <2>.",
    "A solitary arrow is featured in the image with its tip directed towards the <2>.",
    "The diagram highlights an arrow that unmistakably points to the <2>.",
    "The image clearly shows the arrow is directed towards the <2>."
  ],
  "direction3": [
    "In this diagram with <1> arrows, arrow <3> is prominently directed towards the <2>, setting it apart.",
    "The picture features multiple arrows, and arrow <3> can be identified by its orientation towards the <2>.",
    "Among the <1> arrows present, the one labeled <3> is clearly oriented towards the <2>.",
    "This image shows <1> arrows with arrow <3> standing out as it points directly towards the <2>."
  ],
  "direction4": [
    "At the center of the image, an arrow is prominently displayed, directing its attention towards the <1> <2>.",
    "The diagram features a central arrow that points directly to the <1> <2>, clearly indicating its focus.",
    "In the image, a centrally positioned arrow directs towards the <1> <2>, highlighting that specific element.",
    "A central arrow in the picture is seen pointing towards the <1> <2>.",
    "Although one might misinterpret its path as <1> <3>, the central arrow in the image actually points towards the <1> <2>."
  ],
  "direction5": [
    "The image features a two-headed arrow connecting two distinct elements: the <1> <2> and the <1> <3>.",
    "In the diagram, a double-headed arrow is seen linking the <1> <2> and the <1> <3>.",
    "This illustration displays a two-headed arrow that clearly points towards both the <1> <2> and the <1> <3>.",
    "The picture includes a two-headed arrow directing attention to the two items: the <1> <2> and the <1> <3>.",
    "A two-headed arrow in the image indicates both the <1> <2> and the <1> <3>."
  ],
  "direction6": [
    "The image presents an arrow that is clearly aimed towards the <1> <2>.",
    "In the diagram, an arrow directs towards the <1> <2>",
    "This illustration shows an arrow pointing specifically at the <1> <2>.",
    "A prominently featured arrow in the image is oriented towards the <1> <2>,",
    "The arrow is pointing to the <1> <2>."
  ],
  "direction7": [
    "The image contains several <1>s arranged in a sequence, with an arrow guiding the order to be read as: <2>.",
    "In the picture, multiple <1>s are presented with an arrow indicating the reading sequence: <2>.",
    "This illustration displays <1>s that are organized along a path defined by an arrow, resulting in the order: <2>.",
    "The diagram shows a collection of <1>s that should be read following the direction of the arrow, producing the sequence: <2>."
  ],
  "direction8": [
    "The image illustrates a scenario with a <1> arrow and a <2> arrow; from the viewpoint of the <1> arrow, the <2> arrow is positioned to the <3>.",
    "In this diagram, a <1> arrow and a <2> arrow are depicted, with the <2> arrow appearing to be oriented towards the <3> relative to the <1> arrow.",
    "This illustration shows both a <1> arrow and a <2> arrow, where the <2> arrow's orientation is perceived as <3> from the perspective of the <1> arrow.",
    "The diagram presents two arrows, with the relative position of the <2> arrow being <3> when observed from the direction of the <1> arrow."
  ],
  "direction9": [
    "The image features an arrow clearly oriented towards the <1> direction.",
    "The diagram shows an arrow that is distinctly directed towards the <2>.",
    "In this illustration, the arrow is seen pointing towards the <1>.",
    "The image clearly depicts an arrow oriented in the <2> direction.",
    "Observing the image confirms that the arrow is indeed pointing towards the <1>.",
    "The image reveals it is oriented towards the <1>.",
    "The diagram verifies that the arrow's direction is depicted as <2>.",
    "The image clearly shows the arrow's direction as <2>."
  ],
  "direction10": {
    "in": [
      "The image features multiple arrows, and among them, arrow <1> is uniquely directed towards the center.",
      "In the diagram, one arrow, labeled <1>, stands out as it points directly towards the center.",
      "This illustration displays an arrow that is clearly directing inwards, with arrow <1> leading to the center.",
      "In the image, a unique arrow, identified as <1>, is the sole arrow pointing towards the center."
    ],
    "out": [
      "The image displays several arrows, with arrow <1> distinctly oriented outwards from the center.",
      "In the diagram, arrow <1> is prominently seen pointing away from the center.",
      "This illustration shows an arrow, labeled <1>, that is clearly directing outwards from the center.",
      "The image uniquely highlights arrow <1> as the sole arrow that points outwards from the center."
    ]
  }
}

def generate_direction1(entity):
        
    n = entity[1]
    answer = entity[2]

    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", str(n)).replace("<2>", answer)

    return caption

def generate_direction2(entity):
        
    direction = entity[1]

    if direction in ['up', 'down', 'left', 'right']:
        direction_pool = ['up', 'down', 'left', 'right']
    else:
        direction_pool = ['up-left', 'up-right', 'down-left', 'down-right']

    negative_direction = random.choice([x for x in direction_pool if x != direction])

    index = random.randint(0, len(captions[entity[0]]) - 1)
    caption = captions[entity[0]][index].replace("<1>", ", ".join(direction_pool)).replace("<2>", direction).replace("<3>", negative_direction)

    return caption

def generate_direction3(entity):
    
    n = entity[1]
    direction = entity[2]
    answer = entity[3]

    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", str(n)).replace("<2>", direction).replace("<3>", answer)

    return caption

def generate_direction4(entity):
    
    object_type = entity[1]

    if object_type == 'direction':
        object_type = 'word'

    answer = entity[2]
    negative_answer = entity[3]

    index = random.randint(0, len(captions[entity[0]]) - 1)
    caption = captions[entity[0]][index].replace("<1>", object_type).replace("<2>", answer).replace("<3>", negative_answer)

    return caption

def generate_direction5(entity):
    
    object_type = entity[1]
    answer1 = entity[2]
    answer2 = entity[3]

    if object_type == 'direction':
        object_type = 'word'

    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", object_type).replace("<2>", answer1).replace("<3>", answer2)

    return caption

def generate_direction6(entity):
    
    object_type = entity[1]
    answer = entity[2]
    negative_answer = entity[3]

    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", object_type).replace("<2>", answer).replace("<3>", negative_answer)

    return caption

def generate_direction7(entity):
    
    text_type = entity[1]
    answer = entity[2]

    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", text_type).replace("<2>", ''.join(answer))

    return caption

def generate_direction8(entity):
    
    color1 = entity[1]
    color2 = entity[2]
    direction = entity[3]

    index = random.randint(0, len(captions[entity[0]]) - 1)

    caption = captions[entity[0]][index].replace("<1>", color1).replace("<2>", color2).replace("<3>", direction)

    return caption

def generate_direction9(entity):
    
    direction = entity[1]
    
    lr = 'left' if 'left' in direction else 'right'
    ud = 'up' if 'up' in direction else 'down'

    lr_false = 'right' if lr == 'left' else 'left'
    ud_false = 'down' if ud == 'up' else 'up'

    index = random.randint(0, len(captions[entity[0]]) - 1)
    caption = captions[entity[0]][index].replace("<1>", lr).replace("<2>", ud).replace("<3>", lr_false).replace("<4>", ud_false)

    return caption

def generate_direction10(entity):
    
    q_type = entity[1]
    answer = entity[2]

    index = random.randint(0, len(captions[entity[0]][q_type]) - 1)

    caption = captions[entity[0]][q_type][index].replace("<1>", answer)

    return caption

def generate_caption(diagram):
    captions_list = []

    for entity in diagram.entities:
        if entity[0] == 'direction1':
            captions_list.append(generate_direction1(entity))
        elif entity[0] == 'direction2':
            captions_list.append(generate_direction2(entity))
        elif entity[0] == 'direction3':
            captions_list.append(generate_direction3(entity))
        elif entity[0] == 'direction4':
            captions_list.append(generate_direction4(entity))
        elif entity[0] == 'direction5':
            captions_list.append(generate_direction5(entity))
        elif entity[0] == 'direction6':
            captions_list.append(generate_direction6(entity))
        elif entity[0] == 'direction7':
            captions_list.append(generate_direction7(entity))
        elif entity[0] == 'direction8':
            captions_list.append(generate_direction8(entity))
        elif entity[0] == 'direction9':
            captions_list.append(generate_direction9(entity))
        elif entity[0] == 'direction10':
            captions_list.append(generate_direction10(entity))

    return random.choice(captions_list)
