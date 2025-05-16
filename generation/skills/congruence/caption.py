from .rules import *

captions = {
    "sentence1": [
        "In the given figure, the <1> on the left face and the <2> on the right face are congruent to each other.",
        "Within this diagram, the <1> located on the left side and the <2> on the right side are congruent.",
        "The <1> on the left side of the illustration and the <2> on the right side are congruent.",
        "According to the provided image, the <1> on the left and the <2> on the right are congruent shapes.",
        "In this figure, the <1> on the left and the <2> on the right are congruent to each other."
    ],
    "sentence2": [
        "In the given figure, the <1> on the left face and the <2> on the right face are not congruent to each other.",
        "Within this diagram, the <1> on the left side and the <2> on the right side are not congruent.",
        "The <1> on the left side of the illustration and the <2> on the right side are not congruent.",
        "According to the provided image, the <1> on the left and the <2> on the right are not congruent shapes.",
        "In this figure, the <1> on the left and the <2> on the right are not congruent to each other."
    ],
    "sentence0": [
        "In the given figure, there are <1> that are congruent to each other.",
        "Within this diagram, <1> are drawn such that they are all congruent.",
        "The provided image shows <1> that are mutually congruent.",
        "In this illustration, the <1> depicted are congruent to one another.",
        "This figure features <1> which are congruent to each other."
    ],
    "sentence3": [
        "The side that corresponds to side <1> is side <2>.",
        "Side <2> is the corresponding side to side <1>.",
        "Side <1> corresponds to side <2>.",
        "The matching side for side <1> is side <2>.",
        "The side parallel in position to side <1> is side <2>."
    ],
    "sentence4": [
        "The angle that corresponds to angle <1> is angle <2>.",
        "Angle <2> is the corresponding angle to angle <1>.",
        "Angle <1> corresponds to angle <2>.",
        "The matching angle for angle <1> is angle <2>.",
        "The angle parallel in position to angle <1> is angle <2>."
    ]
}


def congruence1_caption(component, entity_info, additional_info):
    captions_list = []
    one_text = random.choice(captions['sentence1'])
    one_text = one_text.replace("<1>", component[0][1].shape_type)
    one_text = one_text.replace("<2>", component[1][1].shape_type)
    captions_list.append(one_text)
    return captions_list

def congruence2_caption(component, entity_info, additional_info):
    captions_list = []
    one_text = random.choice(captions['sentence2'])
    one_text = one_text.replace("<1>", component[0][1].shape_type)
    one_text = one_text.replace("<2>", component[1][1].shape_type)
    captions_list.append(one_text)
    return captions_list

def congruence3_caption(component, entity_info, additional_info):
    captions_list = []

    shape_type = entity_info[0]
    first_list = additional_info[0]
    second_list = additional_info[1]

    one_text = random.choice(captions['sentence0'])
    one_text = one_text.replace("<1>", shape_type)
    captions_list.append(one_text)

    for idx in range(len(first_list)):
        one_text = random.choice(captions['sentence3'])
        one_text = one_text.replace("<1>", first_list[idx])
        one_text = one_text.replace("<2>", second_list[idx])
        captions_list.append(one_text)
    
    return captions_list

def congruence4_caption(component, entity_info, additional_info):
    captions_list = []

    shape_type = entity_info[0]
    first_list = additional_info[0]
    second_list = additional_info[1]

    one_text = random.choice(captions['sentence0'])
    one_text = one_text.replace("<1>", shape_type)
    captions_list.append(one_text)

    for idx in range(len(first_list)):
        one_text = random.choice(captions['sentence4'])
        one_text = one_text.replace("<1>", first_list[idx])
        one_text = one_text.replace("<2>", second_list[idx])
        captions_list.append(one_text)
    
    return captions_list

def generate_caption(diagram):
    captions_list = []

    component = diagram.components
    question_type = diagram.entities[0][0]
    entity_info = diagram.entities[0][1]
    additional_info = diagram.additional_info

    ftn_str = {'congruence1':congruence1_caption, 'congruence2':congruence2_caption, 'congruence3':congruence3_caption, 'congruence4':congruence4_caption}
    captions_list = ftn_str[question_type](component, entity_info, additional_info)

    return " ".join(captions_list)