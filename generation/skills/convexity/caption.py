from .rules import *

captions = {
    "sentence1": [
        "In the given image, there is a <1> shape and <2> points drawn.",
        "Within this figure, a <1> shape and <2> points are depicted.",
        "The image shows a <1> shape along with <2> points.",
        "This illustration includes a <1> shape and <2> points.",
        "Here, one can see a <1> shape and <2> points in the diagram."
    ],
    "sentence2345": [
        "In the given image, there are <1> shapes drawn.",
        "Within this figure, <1> shapes appear.",
        "The image depicts <1> shapes.",
        "This illustration includes <1> shapes.",
        "Here, one can see <1> shapes in the figure."
    ],
    "sentence24": [
        "Shape <1> is a <2> shape.",
        "The figure labeled <1> is a <2> shape.",
        "Shape <1> happens to be <2>.",
        "We can see that shape <1> is <2>.",
        "In this image, shape <1> is identified as <2>."
    ],
    "sentence35": [
        "The shape colored <1> is a <2> shape.",
        "A shape of color <1> is <2>.",
        "The <1>-colored shape can be described as <2>.",
        "Any shape with the color <1> is considered <2>.",
        "In this figure, the <1>-colored shape is <2>."
    ],
    "sentence6": [
        "In the given image, there is a <1> function and <2> points drawn.",
        "Within this figure, a <1> function and <2> points are depicted.",
        "The image shows a <1> function along with <2> points.",
        "This illustration includes a <1> function and <2> points.",
        "Here, one can see a <1> function and <2> points in the diagram."
    ],
    "sentence71": [
        "In the given figure, a single function is drawn, and it is divided into multiple regions based on a rectangle.",
        "Within this image, one function is shown, split into various regions using a rectangle.",
        "The illustration depicts a single function that is partitioned into multiple sections by a rectangle.",
        "This figure presents one function, which is divided into multiple regions by a rectangle.",
        "Here, a function is drawn, and it is subdivided into several areas using a rectangle as a reference."
    ],
    "sentence72": [
        "In region <1>, the function is <2>.",
        "Within region <1>, the function behaves as <2>.",
        "The function in region <1> is <2>.",
        "Regarding region <1>, the function is <2>.",
        "In area <1>, the function can be classified as <2>."
    ],
    "sentence81": [
        "In the given figure, a single function is drawn, and it is divided into multiple regions based on points on the function.",
        "Within this image, one function is displayed, partitioned into various areas according to its points.",
        "The illustration shows one function, which is split into several regions using points on the function as references.",
        "This figure presents a function that is segmented into multiple areas based on the points lying on it.",
        "Here, the function is drawn and divided into different regions determined by its points."
    ],
    "sentence82": [
        "In the region <1>, the function is <2>.",
        "Within the area <1>, the function is <2>.",
        "In the region <1>, the function behaves as <2>.",
        "Regarding the region <1>, the function is <2>.",
        "The function is <2> in the region <1>."
    ],
    "sentence9": [
        "In the given image, there is a <1> lens and <2> points drawn.",
        "Within this figure, a <1> lens and <2> points are depicted.",
        "The image shows a <1> lens along with <2> points.",
        "This illustration includes a <1> lens and <2> points.",
        "Here, one can see a <1> lens and <2> points in the diagram."
    ],
    "sentence10111213": [
        "In the given image, there are <1> lenses drawn.",
        "Within this figure, <1> lenses are depicted.",
        "The image contains <1> lenses.",
        "This illustration presents <1> lenses.",
        "Here, <1> lenses appear in the image."
    ],
    "sentence1012": [
        "Lens <1> is a <2> lens.",
        "The lens labeled <1> is a <2> lens.",
        "Lens <1> happens to be <2>.",
        "In this figure, lens <1> is classified as <2>.",
        "We can observe that lens <1> is <2>."
    ],
    "sentence1113": [
        "The lens colored <1> is a <2> lens.",
        "A lens of color <1> is <2>.",
        "Any lens that is <1> in color can be described as <2>.",
        "This lens, which is <1> in color, is <2>.",
        "A <1>-colored lens is considered <2>."
    ]
}

def convexity1_caption(component, entity_info):
    caption_list = []
    new_text = random.choice(captions['sentence1'])
    new_text = new_text.replace("<1>", component[0].convex_concave)
    new_text = new_text.replace("<2>", str(len(component)-1))
    caption_list.append(new_text)
    return caption_list

def convexity24_caption(component, entity_info):
    caption_list = []

    new_text = random.choice(captions['sentence2345'])
    new_text = new_text.replace("<1>", str(len(component)))
    caption_list.append(new_text)

    for one_component in component:
        new_text = random.choice(captions['sentence24'])
        new_text = new_text.replace("<1>", str(one_component.label))
        new_text = new_text.replace("<2>", one_component.convex_concave)
        caption_list.append(new_text)

    return caption_list

def convexity35_caption(component, entity_info):
    caption_list = []

    new_text = random.choice(captions['sentence2345'])
    new_text = new_text.replace("<1>", str(len(component)))
    caption_list.append(new_text)

    for one_component in component:
        new_text = random.choice(captions['sentence35'])
        new_text = new_text.replace("<1>", str(one_component.facecolor))
        new_text = new_text.replace("<2>", one_component.convex_concave)
        caption_list.append(new_text)

    return caption_list

def convexity6_caption(component, entity_info):
    caption_list = []
    new_text = random.choice(captions['sentence6'])
    new_text = new_text.replace("<1>", component[0].convex_concave)
    new_text = new_text.replace("<2>", str(len(component)-1))
    caption_list.append(new_text)
    return caption_list

def convexity7_caption(component, entity_info):
    caption_list = []

    new_text = random.choice(captions['sentence71'])
    caption_list.append(new_text)

    for one_label in component[0].label_list:
        if one_label in component[0].info_dict["convex"]:
            convex_concave = "convex"
        else:
            convex_concave = "concave"
        
        new_text = random.choice(captions['sentence72'])
        new_text = new_text.replace("<1>", str(one_label))
        new_text = new_text.replace("<2>", convex_concave)
        caption_list.append(new_text)

    return caption_list

def convexity8_caption(component, entity_info):
    caption_list = []
    
    new_text = random.choice(captions['sentence81'])
    caption_list.append(new_text)

    for one_label in component[0].options:
        if one_label in component[0].info_dict["convex"]:
            convex_concave = "convex"
        else:
            convex_concave = "concave"
        
        new_text = random.choice(captions['sentence82'])
        new_text = new_text.replace("<1>", str(one_label))
        new_text = new_text.replace("<2>", convex_concave)
        caption_list.append(new_text)

    return caption_list

def convexity9_caption(component, entity_info):
    caption_list = []
    new_text = random.choice(captions['sentence9'])
    new_text = new_text.replace("<1>", component[0].convex_concave)
    new_text = new_text.replace("<2>", str(len(component)-1))
    caption_list.append(new_text)
    return caption_list

def convexity1012_caption(component, entity_info):
    caption_list = []

    new_text = random.choice(captions['sentence10111213'])
    new_text = new_text.replace("<1>", str(len(component)))
    caption_list.append(new_text)

    for one_component in component:
        new_text = random.choice(captions['sentence1012'])
        new_text = new_text.replace("<1>", str(one_component.label))
        new_text = new_text.replace("<2>", one_component.convex_concave)
        caption_list.append(new_text)

    return caption_list

def convexity1113_caption(component, entity_info):
    caption_list = []

    new_text = random.choice(captions['sentence10111213'])
    new_text = new_text.replace("<1>", str(len(component)))
    caption_list.append(new_text)

    for one_component in component:
        new_text = random.choice(captions['sentence1113'])
        new_text = new_text.replace("<1>", str(one_component.lens_color))
        new_text = new_text.replace("<2>", one_component.convex_concave)
        caption_list.append(new_text)

    return caption_list


def generate_caption(diagram):
    caption_list = []

    component = diagram.components
    question_type = diagram.entities[0][0]
    entity_info = diagram.entities[0][1]

    ftn_str = {
        'convexity1':convexity1_caption,
        'convexity2':convexity24_caption,
        'convexity4':convexity24_caption,
        'convexity3':convexity35_caption,
        'convexity5':convexity35_caption,
        'convexity6':convexity6_caption,
        'convexity7':convexity7_caption,
        'convexity8':convexity8_caption,
        'convexity9':convexity9_caption,
        'convexity10':convexity1012_caption,
        'convexity12':convexity1012_caption,
        'convexity11':convexity1113_caption,
        'convexity13':convexity1113_caption,
    }

    caption_list = ftn_str[question_type](component, entity_info)

    return " ".join(caption_list)