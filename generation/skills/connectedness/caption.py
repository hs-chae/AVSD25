from .rules import *

captions = {
    "sentence1": [
        "In the figure, the line connecting the two <1>-colored points is continuous from start to end.",
        "Within this diagram, the line joining the two points colored <1> stays connected all the way through.",
        "The line linking the two points with color <1> runs without interruption throughout the figure.",
        "In this image, the line between the two <1>-colored points remains unbroken from beginning to end.",
        "According to the illustration, the line connecting the pair of points colored <1> is completely uninterrupted."
    ],
    "sentence2": [
        "In the figure, the line connecting point <1> and point <2> is continuous from start to finish.",
        "Within this diagram, the line joining point <1> and point <2> remains unbroken throughout.",
        "The line between point <1> and point <2> is uninterrupted from beginning to end in this figure.",
        "In this image, the line that connects point <1> and point <2> runs continuously from its start to its end.",
        "According to the illustration, the line linking point <1> and point <2> extends without interruption."
    ],
    "sentence3": [
        "In the figure, the line connecting the two <1>-colored points is broken at intervals.",
        "Within this diagram, the line linking the two points colored <1> is intermittently disconnected.",
        "The line between the two points with color <1> is partially broken in this figure.",
        "In this image, the line connecting the two <1>-colored points has segments that are not continuous.",
        "According to the illustration, the line joining the pair of points colored <1> is broken in several places."
    ],
    "sentence4": [
        "In the figure, the line connecting point <1> and point <2> is broken in parts.",
        "Within this diagram, the line linking point <1> and point <2> is intermittently interrupted.",
        "The line between point <1> and point <2> is not continuous throughout the figure.",
        "In this image, the line that joins point <1> and point <2> has gaps along the way.",
        "According to the illustration, the line connecting point <1> and point <2> is discontinuous at several intervals."
    ],
    "sentence5": [
        "In the given figure, there are various shapes, and if we count the connected shapes, there are a total of <1>.",
        "Within this diagram, multiple shapes are present, and upon counting the connected shapes, we find <1> in total.",
        "According to the provided image, several distinct shapes exist. Counting the connected shapes yields <1> in total.",
        "This figure contains a variety of shapes; when we sum the connected shapes, the total is <1>.",
        "In this illustration, there are diverse figures, and the number of connected shapes amounts to <1> overall."
    ],
    "sentence678": [
        "The list of connected components in the given figure is <1>.",
        "The figure's connected components can be represented as <1>.",
        "Those connected components are given by <1>.",
        "The connected components are listed as <1>.",
        "They should be listed as <1>."
    ]
}


def connectedness1_caption(component, entity_info):
    captions_list = []

    one_text = random.choice(captions["sentence1"])
    one_text = one_text.replace("<1>", str(entity_info[0]))
    captions_list.append(one_text)

    return captions_list

def connectedness2_caption(component, entity_info):
    captions_list = []

    one_text = random.choice(captions["sentence2"])
    one_text = one_text.replace("<1>", str(entity_info[0]))
    one_text = one_text.replace("<2>", str(entity_info[1]))
    captions_list.append(one_text)
    
    return captions_list

def connectedness3_caption(component, entity_info):
    captions_list = []

    one_text = random.choice(captions["sentence3"])
    one_text = one_text.replace("<1>", str(entity_info[0]))
    captions_list.append(one_text)
    
    return captions_list

def connectedness4_caption(component, entity_info):
    captions_list = []

    one_text = random.choice(captions["sentence4"])
    one_text = one_text.replace("<1>", str(entity_info[0]))
    one_text = one_text.replace("<2>", str(entity_info[1]))
    captions_list.append(one_text)
    
    return captions_list

def connectedness5_caption(component, entity_info):
    captions_list = []

    one_text = random.choice(captions["sentence5"])
    one_text = one_text.replace("<1>", str(entity_info[1]))
    captions_list.append(one_text)
    
    return captions_list

def connectedness678_caption(component, entity_info):
    captions_list = []

    one_text = random.choice(captions["sentence678"])
    one_text = one_text.replace("<1>", str(entity_info[1]))
    captions_list.append(one_text)
    
    return captions_list

def generate_caption(diagram):
    captions_list = []

    component = diagram.components
    question_type = diagram.entities[0][0]
    entity_info = diagram.entities[0][1]

    ftn_str = {'connectedness1':connectedness1_caption, 'connectedness2':connectedness2_caption, 'connectedness3':connectedness3_caption, 'connectedness4':connectedness4_caption, 'connectedness5':connectedness5_caption}
    if question_type[-1] in ['1', '2', '3', '4', '5']:
        captions_list = ftn_str[question_type](component, entity_info)
    else:
        captions_list = connectedness678_caption(component, entity_info)

    return " ".join(captions_list)
