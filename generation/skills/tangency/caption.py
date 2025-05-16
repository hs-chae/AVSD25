from .rules import *

# captions = {
#     "sentence11": [
#         "In the given image, there is a curve colored <1>, a line segment colored <2>, and <3> points. The curve colored <1> and the line segment colored <2> are tangent to each other.",
#         "Within this figure, one <1>-colored curve, one <2>-colored line segment, and <3> points are shown. The <1>-colored curve and the <2>-colored line segment make contact (are tangent).",
#         "The image presents a <1>-colored curve, a <2>-colored line segment, and <3> points. Here, the <1>-colored curve and the <2>-colored line segment touch each other.",
#         "This illustration depicts a curve in color <1>, a line segment in color <2>, and <3> points. The <1>-colored curve and the <2>-colored line segment intersect tangentially.",
#         "In this diagram, you can see a curve of color <1>, a line segment of color <2>, and <3> points. The curve colored <1> and the line segment colored <2> are tangent."
#     ],
#     "sentence12": [
#         "In the given image, there is a line segment colored <2>, a curve colored <1>, and <3> points. The curve colored <1> and the line segment colored <2> are tangent to each other.",
#         "Within this figure, a <2>-colored line segment, a <1>-colored curve, and <3> points are shown. The <1>-colored curve and the <2>-colored line segment make contact (are tangent).",
#         "The image presents a <2>-colored line segment, a <1>-colored curve, and <3> points. Here, the <1>-colored curve and the <2>-colored line segment touch.",
#         "This illustration depicts a line segment in color <2>, a curve in color <1>, and <3> points. The <1>-colored curve and the <2>-colored line segment intersect tangentially.",
#         "In this diagram, you can see a line segment of color <2>, a curve of color <1>, and <3> points. They are tangent to each other."
#     ],
#     "sentence21": [
#         "In the given image, there is a curve colored <1>, a line segment colored <2>, and <3> points. The <1>-colored curve and the <2>-colored line segment do not touch each other.",
#         "Within this figure, a <1>-colored curve, a <2>-colored line segment, and <3> points appear. The curve of color <1> and the line segment of color <2> are not tangent.",
#         "The image shows a <1>-colored curve, a <2>-colored line segment, and <3> points. Here, the <1>-colored curve and the <2>-colored line segment fail to make contact.",
#         "This illustration includes one curve of color <1>, one line segment of color <2>, and <3> points. The <1>-colored curve and the <2>-colored line segment do not intersect tangentially.",
#         "In this diagram, a curve with color <1>, a line segment with color <2>, and <3> points are given, but they are not tangent to each other."
#     ],
#     "sentence22": [
#         "In the given image, there is a line segment colored <2>, a curve colored <1>, and <3> points. The <1>-colored curve and the <2>-colored line segment do not touch each other.",
#         "Within this figure, a <2>-colored line segment, a <1>-colored curve, and <3> points appear. The curve of color <1> and the line segment of color <2> are not tangent.",
#         "The image shows a line segment colored <2>, a curve colored <1>, and <3> points. Here, the <1>-colored curve and the <2>-colored line segment do not meet tangentially.",
#         "This illustration displays a line segment of color <2>, a curve of color <1>, and <3> points. The <1>-colored curve and <2>-colored line segment are not in contact.",
#         "In this diagram, you can see a <2>-colored line segment, a <1>-colored curve, and <3> points, but they do not touch each other."
#     ],
#     "sentence3": [
#         "In the given image, there is a curve colored <1>, a curve colored <2>, and <3> points. The curve colored <1> and the line segment colored <2> are tangent.",
#         "Within this figure, a <1>-colored curve, a <2>-colored curve, and <3> points are shown. However, the <1>-colored curve and the <2>-colored line segment make contact.",
#         "The image presents two curves: one <1>-colored and the other <2>-colored, along with <3> points. The first curve (<1>) and the line segment (<2>) are tangent.",
#         "This illustration depicts two curves (in colors <1> and <2>) plus <3> points. The <1>-colored curve and the <2>-colored line segment touch each other.",
#         "Here, a <1>-colored curve, a <2>-colored curve, and <3> points appear. Notably, the <1>-colored curve and the <2>-colored line segment are tangent."
#     ],
#     "sentence4": [
#         "In the given image, there is a curve colored <1>, a curve colored <2>, and <3> points. The curve colored <1> and the line segment colored <2> do not touch each other.",
#         "Within this figure, a <1>-colored curve, a <2>-colored curve, and <3> points are shown. The <1>-colored curve and the <2>-colored line segment do not make contact.",
#         "The image presents two curves: one <1>-colored and the other <2>-colored, along with <3> points. The first curve (<1>) and the line segment (<2>) are not tangent.",
#         "This illustration displays two curves (in colors <1> and <2>) plus <3> points. The <1>-colored curve and the <2>-colored line segment do not intersect tangentially.",
#         "Here, a <1>-colored curve, a <2>-colored curve, and <3> points appear. The <1>-colored curve and the <2>-colored line segment fail to meet."
#     ],
#     "sentence51": [
#         "In the given image, there is a circle colored <1> and a line segment colored <2>. The <1>-colored curve and the <2>-colored line segment are tangent.",
#         "Within this figure, a <1>-colored circle and a <2>-colored line segment are present. They make contact (are tangent).",
#         "The image shows a circle in color <1> and a line segment in color <2>. The <1>-colored curve and the <2>-colored line segment touch each other.",
#         "This illustration includes a <1>-colored circle and a <2>-colored line segment. The curve of color <1> and the line segment of color <2> intersect tangentially.",
#         "Here, a circle in color <1> and a line segment in color <2> are displayed, and they are tangent to each other."
#     ],
#     "sentence52": [
#         "In the given image, there is a line segment colored <2> and a circle colored <1>. The <1>-colored curve and the <2>-colored line segment are tangent.",
#         "Within this figure, a <2>-colored line segment and a <1>-colored circle can be seen. They make contact (are tangent).",
#         "The image shows a line segment in color <2> and a circle in color <1>. The curve colored <1> and the line segment colored <2> touch each other.",
#         "This illustration presents a <2>-colored line segment and a <1>-colored circle. They meet tangentially.",
#         "Here, a line segment in color <2> and a circle in color <1> are depicted, and they are tangent to each other."
#     ],
#     "sentence61": [
#         "In the given image, there is a circle colored <1> and a line segment colored <2>. The <1>-colored curve and the <2>-colored line segment do not touch.",
#         "Within this figure, a <1>-colored circle and a <2>-colored line segment are present, but they are not tangent.",
#         "The image shows a circle in color <1> and a line segment in color <2>. The <1>-colored curve and the <2>-colored line segment fail to meet tangentially.",
#         "This illustration includes a <1>-colored circle and a <2>-colored line segment, which do not intersect tangentially.",
#         "Here, a circle in color <1> and a line segment in color <2> are depicted, and they do not touch each other."
#     ],
#     "sentence62": [
#         "In the given image, there is a line segment colored <2> and a circle colored <1>. The <1>-colored curve and the <2>-colored line segment do not touch.",
#         "Within this figure, a <2>-colored line segment and a <1>-colored circle are present, but they are not tangent.",
#         "The image shows a line segment in color <2> and a circle in color <1>. They fail to meet tangentially.",
#         "This illustration depicts a <2>-colored line segment and a <1>-colored circle, which do not intersect tangentially.",
#         "Here, a line segment in color <2> and a circle in color <1> are drawn, and they do not touch each other."
#     ],
#     "sentence7": [
#         "In the given image, line segments and curves are drawn. Among the intersections of the two lines, the tangent point of the line segment and the curve is <1>.",
#         "Within this figure, there are line segments and curves. Out of the intersections of these two lines, the tangent point between the segment and the curve is <1>.",
#         "The image presents both a line segment and a curve. Among their intersection points, the one where they touch tangentially is <1>.",
#         "In this illustration, we see a segment and a curve. The intersection that serves as their tangent point is <1>.",
#         "Here, several segments and curves appear. Among the intersections, the point of tangency between the segment and the curve is <1>."
#     ],
#     "sentence8": [
#         "In the given image, two curves are drawn. Among their intersection points, the tangent point of the two curves is <1>.",
#         "Within this figure, there are two curves. Out of the intersections they share, the tangential contact point is <1>.",
#         "The image depicts two separate curves. Of the points where they intersect, the one that is their tangent point is <1>.",
#         "In this illustration, two curves are shown. The intersection that corresponds to their point of tangency is <1>.",
#         "Here, we see two distinct curves. Their intersection points include a tangential point, identified as <1>."
#     ],
#     "sentence9": [
#         "In the given image, there is 1 line segment colored <1>, and multiple curves each colored <2>. Among these, the curve colored <3> is tangent to the line segment colored <1>.",
#         "Within this figure, a line segment of color <1> and several curves of color <2> are drawn. Notably, the <3>-colored curve touches the <1>-colored segment.",
#         "The image shows one <1>-colored segment and multiple <2>-colored curves. The curve in color <3> is tangent to the segment in color <1>.",
#         "This illustration includes a single line segment colored <1> and curves colored <2>. Among them, the <3>-colored curve intersects the <1>-colored segment tangentially.",
#         "Here, there's one line segment in color <1> and various curves each colored <2>. In particular, the curve with color <3> is tangent to the <1>-colored segment."
#     ]
# }


# def tangency1_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list

# def tangency2_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list

# def tangency3_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list

# def tangency4_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list

# def tangency5_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list

# def tangency6_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list

# def tangency7_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list

# def tangency8_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list

# def tangency9_caption(component, entity_info):
#     captions_list = []
    
#     return captions_list



# def generate_caption(diagram):
#     captions_list = []

#     # component = diagram.components
#     # question_type = diagram.entities[0][0]
#     # entity_info = diagram.entities[0][1]

#     # ftn_str = {'tangency1':tangency1_caption, 'tangency2':tangency2_caption, 'tangency3':tangency3_caption, 'tangency4':tangency4_caption, 'tangency5':tangency5_caption, 'tangency6':tangency6_caption, 'tangency7':tangency7_caption, 'tangency8':tangency8_caption, 'tangency9':tangency9_caption}
#     # captions_list = ftn_str[question_type](component, entity_info)

#     return " ".join(captions_list)

captions = {
  "tangency1": [
    "In this figure, the line and curve are tangent.",
    "The straight line and the curve touch tangentially.",
    "They meet at exactly one point of tangency.",
    "There is a tangential contact between the line and the curve.",
    "The line and the curve shown here form a tangent."
  ],
  "tangency2": [
    "In this figure, the line and curve do not form a tangent.",
    "They do not touch at a tangential point.",
    "No tangent contact exists between the line and the curve.",
    "This diagram does not show a tangential intersection.",
    "The line and curve are not tangent in this figure."
  ],
  "tangency3": [
    "The two differently colored curves are tangent here.",
    "They meet at a point of tangential contact.",
    "These curves of distinct colors form a tangent intersection.",
    "There is a single point of tangency between the two curves.",
    "The figure demonstrates a tangential contact between the two colored curves."
  ],
  "tangency4": [
    "In this figure, the two colored curves do not form a tangent.",
    "They don't meet at a tangential point.",
    "No tangential intersection exists between these differently colored curves.",
    "There is no tangent contact in the given diagram.",
    "These two distinct-colored curves are not tangent."
  ],
  "tangency5": [
    "In this figure, <1> and the line segment are tangent.",
    "The <1> meets the line segment at a tangential point.",
    "<1> and the line segment form a tangent here.",
    "There's a single point of tangency between the <1> and the line segment.",
    "The diagram shows <1> and the line segment in a tangential relationship."
  ],
  "tangency6": [
    "In this figure, <1> and the line segment are not tangent.",
    "They do not meet at a tangential point.",
    "No tangential contact exists between <1> and the line segment.",
    "The <1> is not tangent to the line segment in this diagram.",
    "This illustration shows no tangent relationship between <1> and the line segment."
  ],
  "tangency7": [
    "The tangent points between the line and the curve are <1>.",
    "Those intersection points of tangency are <1>.",
    "Here, the tangential contacts are labeled as <1>.",
    "In this figure, the line-curve tangent points appear at <1>.",
    "Identified tangent points: <1>."
  ],
  "tangency8": [
    "The tangent points between these two curves are <1>.",
    "Two curves meet tangentially at <1>.",
    "Here, the two curves have tangential intersections at <1>.",
    "In this figure, the points of tangency for the two curves are <1>.",
    "The tangential contacts between the curves are <1>."
  ],
  "tangency9": [
    "At point <2>, the line of color <3> is tangent to curves in color(s) <4>.",
    "The curves that meet the <3>-colored line tangentially at <2> are <4>.",
    "In this diagram, the <3> line is tangent to the <4>-colored curves at <2>.",
    "<4> is the color of the curves tangent to the line at <2>.",
    "Those curves tangent to the <3>-colored line at point <2> appear in <4>."
  ]
}


def generate_caption(diagram):
    for entity in diagram.entities:
        version_key = entity[0]
        a = random.choice(captions[version_key])
        for i in range(0, len(entity[1])):
            a = a.replace(f"<{i+1}>", entity[1][i])
    return a