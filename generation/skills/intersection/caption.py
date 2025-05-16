from .rules import *

captions = {
  "intersection1": [
    "Yes, the <1> <2><3> and the <4> <5><6> do intersect.",
    "Yes, there is an intersection between the <1> <2><3> and the <4> <5><6>.",
    "Yes, the <1> <2><3> intersects with the <4> <5><6>.",
    "Yes, the <1> <2><3> does meet the <4> <5><6>.",
    "Yes, they do intersect."
  ],
  "intersection2": [
    "No, the <1> <2><3> and the <4> <5><6> do not intersect.",
    "No, there is no intersection between the <1> <2><3> and the <4> <5><6>.",
    "No, those two do not meet.",
    "No, the <1> <2><3> and the <4> <5><6> remain separate.",
    "No, they do not intersect at all."
  ],
  "intersection3": [
    "Yes, the <1> with color <2> and the <3> with color <4> do intersect.",
    "Yes, they intersect.",
    "Yes, the <1> (color <2>) intersects with the <3> (color <4>).",
    "Yes, the <1> of color <2> does meet the <3> of color <4>.",
    "Yes, those two differently colored segments/curves intersect."
  ],
  "intersection4": [
    "No, the <1> with color <2> and the <3> with color <4> do not intersect.",
    "No, there's no intersection.",
    "No, they remain separate.",
    "No, those two do not meet.",
    "No, there's no intersection."
  ],
  "intersection5": [
    "The number of intersection points between the <1> <2><3> and the <4> <5><6> is <7>.",
    "There are <7> intersection points between the <1> <2><3> and the <4> <5><6>.",
    "The <1> <2><3> and the <4> <5><6> intersect in <7> points.",
    "Yes, the total intersection points amount to <7>.",
    "They intersect at <7> points."
  ],
  "intersection6": [
    "The number of intersection points between the <1> of color <2> and the <3> of color <4> is <5>.",
    "They have <5> intersection points in total.",
    "Those two intersect in <5> points.",
    "Yes, the total intersection points amount to <5>.",
    "They intersect at <5> points."
  ],
  "intersection7": [
    "The line segment(s) with the most intersection points with the curve colored <1> is the one (or ones) colored <4>.",
    "The segment that has the highest number of intersections with the <1>-colored curve is colored <4>.",
    "The line segment(s) with the greatest intersection count for the <1>-colored curve is <4>.",
    "The line segment with color <4> has the most intersections with the <1>-colored curve.",
    "That line segment is colored <4>."
  ],
  "intersection8": [
    "The number of line segments that meet the <1>-colored curve is <4>.",
    "They meet in <4> line segments.",
    "The total number is <4>.",
    "There are <4> such segments.",
    "<4> line segments intersect with it."
  ],
  "intersection9": [
    "Among the curves shown, the one(s) that have the most intersection points with the line colored <1> is <4>.",
    "The curve(s) with the greatest number of intersections with the <1>-colored line is <4>.",
    "The curve(s) that achieve the maximum intersections with the <1>-colored line is <4>.",
    "Yes, that curve is colored <4>.",
    "They are the curves colored <4>."
  ],
  "intersection10": [
    "The number of curves that meet the <1>-colored line segment is <4>.",
    "They meet in <4> curves.",
    "The total number is <4>.",
    "There are <4> such curves.",
    "<4> curves intersect with it."
  ],
  "intersection11": [
    "Yes, the boundaries of the two shapes in the figure do intersect.",
    "Yes, those boundaries meet.",
    "Yes, the two boundaries come into contact.",
    "Yes, they do intersect.",
    "Yes, they meet."
  ],
  "intersection12": [
    "No, the boundaries of the two shapes in the figure do not intersect.",
    "No, they remain separate.",
    "No, there is no contact between them.",
    "No, they do not meet.",
    "No, there is no intersection."
  ],
  "intersection13": [
    "The boundaries of the two shapes intersect in <1> points.",
    "They have <1> intersection points.",
    "There are <1> such points of intersection.",
    "They intersect <1> times.",
    "The number of boundary intersection points is <1>."
  ]
}


def generate_caption(diagram):
    for entity in diagram.entities:
        version_key = entity[0]
        a = random.choice(captions[version_key])
        for i in range(0, len(entity[1])):
            a = a.replace(f"<{i+1}>", entity[1][i])
    return a