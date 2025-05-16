from .rules import *

captions = {
  "cardinal_direction_dir_horizontal": [
    "The <1> <3> is positioned on the <5> side of the <2> <4>.",
    "You can see the <1> <3> along the <5> side of the <2> <4>.",
    "In this image, the <1> <3> lies on the <5> side of the <2> <4>.",
    "Here, the <1> <3> appears on the <5> side of the <2> <4>.",
    "The diagram shows the <1> <3> situated on the <5> side of the <2> <4>."
  ],
  "cardinal_direction_dir_horizontal_colored": [
    "The <1> <3> is on the <5> side of the <2> <4>, and the <7> <1> is on the <5> side of the <8> <2>.",
    "In this figure, the <1> <3> is located on the <5> side of the <2> <4>, while the <7> <1> also appears on the <5> side of the <8> <2>.",
    "Observe that both the <1> <3> (relative to <2> <4>) and the <7> <1> (relative to <8> <2>) occupy the <5> side.",
    "You can see the <1> <3> placed on the <5> side of the <2> <4>, and similarly, the <7> <1> on the <5> side of the <8> <2>.",
    "The diagram shows the <1> <3> and the <7> <1> each situated on the <5> side of their respective <2> <4> and <8> <2>."
  ],
  "cardinal_direction_dir_vertical": [
    "The <1> <3> is positioned on the <6> side of the <2> <4>.",
    "You can see the <1> <3> along the <6> side of the <2> <4>.",
    "In this image, the <1> <3> lies on the <6> side of the <2> <4>.",
    "Here, the <1> <3> appears on the <6> side of the <2> <4>.",
    "The diagram shows the <1> <3> situated on the <6> side of the <2> <4>."
  ],
  "cardinal_direction_dir_vertical_colored": [
    "The <1> <3> is on the <6> side of the <2> <4>, and the <7> <1> is on the <6> side of the <8> <2>.",
    "In this figure, the <1> <3> is located on the <6> side of the <2> <4>, while the <7> <1> also appears on the <6> side of the <8> <2>.",
    "Observe that both the <1> <3> (relative to <2> <4>) and the <7> <1> (relative to <8> <2>) occupy the <6> side.",
    "You can see the <1> <3> placed on the <6> side of the <2> <4>, and similarly, the <7> <1> on the <6> side of the <8> <2>.",
    "The diagram shows the <1> <3> and the <7> <1> each situated on the <6> side of their respective <2> <4> and <8> <2>."
  ],
  "cardinal_direction_dir_both": [
    "The <1> <3> is located on the <6> <5> side of the <2> <4>.",
    "You can see the <1> <3> placed on the <6> <5> side of the <2> <4>.",
    "In this figure, the <1> <3> appears on the <6> <5> side of the <2> <4>.",
    "Here, the <1> <3> is found on the <6> <5> side of the <2> <4>.",
    "The diagram shows the <1> <3> situated on the <6> <5> side of the <2> <4>."
  ],
  "cardinal_direction_dir_both_colored": [
    "The <1> <3> is on the <6> <5> side of the <2> <4>, and the <7> <1> is on the <6> <5> side of the <8> <2>.",
    "In this figure, the <1> <3> is positioned on the <6> <5> side of the <2> <4>, while the <7> <1> also lies on the <6> <5> side of the <8> <2>.",
    "Observe that both the <1> <3> and the <7> <1> occupy the <6> <5> side relative to their respective <2> <4> and <8> <2>.",
    "You can see the <1> <3> and the <7> <1> each placed on the <6> <5> side of the <2> <4> and <8> <2>.",
    "The diagram shows that the <1> <3> and the <7> <1> are situated on the <6> <5> side of the <2> <4> and <8> <2>, respectively."
  ],
  "cardinal_direction_obj_horizontal": [
    "Between <1> <3> and <2> <4>, the <1> <3> is positioned on the <5> side.",
    "The <1> <3> lies on the <5> side relative to <2> <4>.",
    "Comparatively, <1> <3> is on the <5> side while <2> <4> is on the opposite.",
    "Here, <1> <3> appears on the <5> side of <2> <4>.",
    "In this layout, <1> <3> occupies the <5> side next to <2> <4>."
  ],
  "cardinal_direction_obj_horizontal_colored": [
    "Between <1> <3> and <2> <4>, the <1> <3> is on the <5> side, and similarly, <7> <1> is on the <5> side of <8> <2>.",
    "Comparatively, <1> <3> lies on the <5> side of <2> <4>, while <7> <1> lies on the <5> side of <8> <2>.",
    "You can see that <1> <3> takes the <5> position relative to <2> <4>, as does <7> <1> relative to <8> <2>.",
    "Here, <1> <3> is on the <5> side when compared with <2> <4>, and <7> <1> is also on the <5> side of <8> <2>.",
    "The diagram shows both <1> <3> and <7> <1> positioned on the <5> side with respect to <2> <4> and <8> <2>, respectively."
  ],
  "cardinal_direction_obj_vertical": [
    "Between <1> <3> and <2> <4>, the <1> <3> is positioned on the <6> side.",
    "The <1> <3> lies on the <6> side relative to <2> <4>.",
    "Comparatively, <1> <3> is on the <6> side while <2> <4> is on the opposite.",
    "Here, <1> <3> appears on the <6> side of <2> <4>.",
    "In this layout, <1> <3> occupies the <6> side next to <2> <4>."
  ],
  "cardinal_direction_obj_vertical_colored": [
    "Between <1> <3> and <2> <4>, the <1> <3> is on the <6> side, and likewise <7> <1> is on the <6> side of <8> <2>.",
    "Comparatively, <1> <3> lies on the <6> side of <2> <4>, while <7> <1> lies on the <6> side of <8> <2>.",
    "Observe that <1> <3> takes the <6> position relative to <2> <4>, as does <7> <1> relative to <8> <2>.",
    "Here, <1> <3> is on the <6> side when compared with <2> <4>, and <7> <1> is also on the <6> side of <8> <2>.",
    "The diagram shows both <1> <3> and <7> <1> positioned on the <6> side with respect to <2> <4> and <8> <2>, respectively."
  ],
  "cardinal_direction_obj_both": [
    "Between <1> <3> and <2> <4>, the <1> <3> is located on the <6> <5> side.",
    "The <1> <3> is on the <6> <5> side relative to <2> <4>.",
    "In this figure, <1> <3> sits on the <6> <5> side while <2> <4> is on the opposite side.",
    "Here, <1> <3> appears on the <6> <5> side compared to <2> <4>.",
    "The diagram positions <1> <3> on the <6> <5> side with respect to <2> <4>."
  ],
  "cardinal_direction_obj_both_colored": [
    "Between <1> <3> and <2> <4>, the <1> <3> is on the <6> <5> side, and likewise <7> <1> is on the <6> <5> side of <8> <2>.",
    "In this figure, <1> <3> sits on the <6> <5> side of <2> <4>, and <7> <1> sits on the <6> <5> side of <8> <2>.",
    "Observe that <1> <3> occupies the <6> <5> side in comparison to <2> <4>, and <7> <1> similarly for <8> <2>.",
    "Here, <1> <3> is placed on the <6> <5> side relative to <2> <4>, and <7> <1> is on the <6> <5> side of <8> <2>.",
    "The diagram shows both <1> <3> and <7> <1> positioned on the <6> <5> side with respect to <2> <4> and <8> <2>, respectively."
  ]
}


def generate_cardinal_direction(entity, long=False):
    conversation = captions

    # find conversation with keyword
    if entity[1][6] is None:
        keyword = entity[0]
    else:
        keyword = entity[0] + "_colored"

    index = random.randint(0, len(conversation[keyword]) - 1)
    a = conversation[keyword][index]

    # replace <1>, <2>, ... with the actual values
    for i in range(len(entity[1])):
        if entity[1][i] is None:
            continue
        a = a.replace(f"<{i+1}>", entity[1][i])
    
    opposite ={
        "left": "right",
        "right": "left",
        "top": "bottom",
        "bottom": "top"
    }

    # replace <-1>, <-2>, ... with the opposite values
    for i in range(len(entity[1])):
        if entity[1][i] is None:
            continue
        if entity[1][i] in opposite:
            a = a.replace(f"<-{i+1}>", opposite[entity[1][i]])
        else:
            a = a.replace(f"<-{i+1}>", entity[1][i])

    return a


def generate_caption(diagram, long=False):
    for entity in diagram.entities:
        if "cardinal_direction" in entity[0]:
            a = generate_cardinal_direction(entity, long)
        break

    return a