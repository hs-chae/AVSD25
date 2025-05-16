from .rules import *

captions = {
    "sentence1": [
        "In the given figure, multiple line segments and multiple curves are mixed together.",
        "Within this diagram, several line segments and various curves are intermingled.",
        "This illustration shows a combination of numerous line segments and multiple curves.",
        "The figure contains a mixture of multiple segments and multiple curves.",
        "In this image, line segments and curves coexist in several forms."
    ],
    "sentence11": [
        "The line colored <1> is a straight line segment.",
        "A line that is <1> in color is a straight line segment.",
        "The <1>-colored line represents a straight line segment.",
        "Any line of color <1> corresponds to a straight line segment.",
        "Lines with color <1> are straight line segments."
    ],
    "sentence12": [
        "The line colored <1> is part of a curve, not a straight line.",
        "A line that is <1> in color belongs to a curve rather than a straight line.",
        "The <1>-colored line is a segment of a curve and not a straight line.",
        "Any line of color <1> is part of a curved path, not a straight line.",
        "Lines with color <1> are portions of a curve, instead of being straight lines."
    ],
    "sentence3": [
        "In the given figure, there are line segments, arcs of a circle, and curves that are neither line segments nor circle arcs, all mixed together.",
        "This diagram shows three types of curves mixed: line segments, circular arcs, and other curves that are neither.",
        "The figure contains line segments, circle arcs, and additional curves not classified as either, all intermingled.",
        "In this illustration, you'll find line segments, arcs of a circle, and curves that are neither type, coexisting together.",
        "The provided image includes a variety of curves: line segments, circular arcs, and other curves that are neither line segments nor arcs."
    ],
    "sentence31": [
        "The line colored <1> is a line segment.",
        "A line that is <1> in color is a line segment.",
        "The <1>-colored line happens to be a line segment.",
        "Any line with color <1> represents a line segment.",
        "Lines of color <1> are recognized as line segments."
    ],
    "sentence32": [
        "The line colored <1> is an arc of a circle.",
        "A line that is <1> in color forms a circular arc.",
        "The <1>-colored line constitutes a circle arc.",
        "Any line of color <1> is an arc of a circle.",
        "Lines with color <1> correspond to circular arcs."
    ],
    "sentence33": [
        "The line colored <1> is a curve that is neither a line segment nor a circle arc.",
        "A line that is <1> in color is a curve, not a segment or a circular arc.",
        "The <1>-colored line is neither a straight segment nor a circle arc, but rather another type of curve.",
        "Any line of color <1> belongs to a curve distinct from line segments and circle arcs.",
        "Lines with color <1> fall into the category of curves that are neither segments nor circle arcs."
    ],
    "sentence451": [
        "In the given figure, there are circles with different radii.",
        "Within this diagram, several circles of varying radii are presented.",
        "This image shows multiple circles, each with a distinct radius.",
        "The figure contains circles that differ in their radii.",
        "Different-sized circles with varying radii appear in the illustration."
    ],
    "sentence452": [
        "The relative radius length of the circle colored <1> is <2>.",
        "For the circle that is <1> in color, its radius measures <2> in relative terms.",
        "A circle colored <1> has a relative radius of <2>.",
        "The circle with color <1> possesses a radius of <2> (relative value).",
        "Regarding the <1>-colored circle, its relative radius is <2>."
    ],
    "sentence4": [
        "Therefore, the circle with the greatest curvature is <1>.",
        "Hence, <1> is the circle that has the highest curvature.",
        "As a result, the circle possessing the largest curvature is <1>.",
        "It follows that the circle with the maximum curvature is <1>.",
        "Thus, among the circles shown, the one with the highest curvature is <1>."
    ],
    "sentence5": [
        "Therefore, the circle with the smallest curvature is <1>.",
        "Hence, <1> is the circle that has the lowest curvature.",
        "As a result, the circle possessing the smallest curvature is <1>.",
        "It follows that the circle with the minimum curvature is <1>.",
        "Thus, among the circles shown, the one with the least curvature is <1>."
    ],
    "sentence671": [
        "In the given figure, there is a single curve with multiple points plotted on it.",
        "Within this diagram, one curve and numerous points on that curve are shown.",
        "This image depicts one curve along with several points lying on it.",
        "The figure displays one curve and multiple points positioned on that curve.",
        "A single curve is presented in the illustration, along with many points located on it."
    ],
    "sentence672": [
        "The curvature of the curve at point <1> is <2>.",
        "At point <1>, the curve has a curvature of <2>.",
        "The curve's curvature at point <1> equals <2>.",
        "Point <1> on the curve exhibits a curvature of <2>.",
        "In this diagram, the curvature of the curve at point <1> measures <2>."
    ],
    "sentence6": [
        "Therefore, the point with the greatest curvature on the given curve is <1>.",
        "Hence, the point <1> exhibits the highest curvature on this curve.",
        "As a result, <1> is the point of maximum curvature on the curve.",
        "It follows that the point on the curve with the largest curvature is <1>.",
        "Thus, among the points on this curve, the one with the greatest curvature is <1>."
    ],
    "sentence7": [
        "Therefore, the point with the smallest curvature on the given curve is <2>.",
        "Hence, the point <2> exhibits the lowest curvature on this curve.",
        "As a result, <2> is the point of minimum curvature on the curve.",
        "It follows that the point on the curve with the smallest curvature is <2>.",
        "Thus, among the points on this curve, the one with the least curvature is <2>."
    ]
}


def curvature12_caption(component, entity_info):
    captions_list = [random.choice(captions["sentence1"])]

    for one_component in component:
        if one_component[0] == "line":
            one_text = random.choice(captions["sentence11"])
        else:
            one_text = random.choice(captions["sentence12"])
        one_text = one_text.replace("<1>", one_component[1].line_color)
        captions_list.append(one_text)

    return captions_list

def curvature3_caption(component, entity_info):
    captions_list = [random.choice(captions["sentence3"])]
    for one_component in component:
        if one_component[0] == "line":
            one_text = random.choice(captions["sentence31"])
            one_text = one_text.replace("<1>", one_component[1].line_color)
        elif one_component[1] == "arc":
            one_text = random.choice(captions["sentence32"])
            one_text = one_text.replace("<1>", one_component[1].edge_color)
        else:
            one_text = random.choice(captions["sentence33"])
            one_text = one_text.replace("<1>", one_component[1].line_color)
        captions_list.append(one_text)

    return captions_list

def curvature4_caption(component, entity_info):
    captions_list = [random.choice(captions["sentence451"])]
    for one_component in component:
        one_text = random.choice(captions["sentence452"])
        one_text = one_text.replace("<1>", one_component.edgecolor)
        one_text = one_text.replace("<2>", str(one_component.radius))
        captions_list.append(one_text)
    one_text = random.choice(captions["sentence4"])
    one_text = one_text.replace("<1>", entity_info[2])
    captions_list.append(one_text)
    return captions_list

def curvature5_caption(component, entity_info):
    captions_list = [random.choice(captions["sentence451"])]
    for one_component in component:
        one_text = random.choice(captions["sentence452"])
        one_text = one_text.replace("<1>", one_component.edgecolor)
        one_text = one_text.replace("<2>", str(one_component.radius))
        captions_list.append(one_text)
    one_text = random.choice(captions["sentence5"])
    one_text = one_text.replace("<1>", entity_info[2])
    captions_list.append(one_text)
    return captions_list

def curvature6_caption(component, entity_info):
    captions_list = [random.choice(captions["sentence671"])]
    wanted_dict = component[0]
    for one_key in wanted_dict:
        one_text = random.choice(captions["sentence672"])
        one_text = one_text.replace("<1>", str(one_key))
        one_text = one_text.replace("<2>", str(wanted_dict[one_key]))
        captions_list.append(one_text)
    one_text = random.choice(captions["sentence6"])
    one_text = one_text.replace("<1>", entity_info[2])
    captions_list.append(one_text)
    return captions_list

def curvature7_caption(component, entity_info):
    captions_list = [random.choice(captions["sentence671"])]
    wanted_dict = component[0]
    for one_key in wanted_dict:
        one_text = random.choice(captions["sentence672"])
        one_text = one_text.replace("<1>", str(one_key))
        one_text = one_text.replace("<2>", str(wanted_dict[one_key]))
        captions_list.append(one_text)
    one_text = random.choice(captions["sentence7"])
    one_text = one_text.replace("<1>", entity_info[2])
    captions_list.append(one_text)
    return captions_list

def generate_caption(diagram):
    captions_list = []

    component = diagram.components
    question_type = diagram.entities[0][0]
    entity_info = diagram.entities[0][1]

    ftn_str = {'curvature1':curvature12_caption, 'curvature2':curvature12_caption, 'curvature3':curvature3_caption, 'curvature4':curvature4_caption, 'curvature5':curvature5_caption, 'curvature6':curvature6_caption, 'curvature7':curvature7_caption}
    captions_list = ftn_str[question_type](component, entity_info)

    return " ".join(captions_list)