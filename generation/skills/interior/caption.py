from .rules import *

captions = {
  "interior1": [
    "The points inside shape <1> are <4>.",
    "Those points within shape <1> are <4>.",
    "Shape <1> contains the following points: <4>.",
    "All points contained by shape <1> are <4>.",
    "The set of points inside shape <1> is <4>."
  ],
  "interior2": [
    "The points outside shape <1> are <4>.",
    "Those points outside shape <1> are <4>.",
    "Shape <1> has the following points outside of it: <4>.",
    "All points outside shape <1> are <4>.",
    "The set of points outside shape <1> is <4>."
  ],
  "interior3": [
    "The colors of the points inside shape <1> are <4>.",
    "The point colors inside shape <1> are <4>.",
    "Inside shape <1>, the point colors are <4>.",
    "The set of colors for points within shape <1> is <4>.",
    "All points in shape <1> have colors <4>."
  ],
  "interior4": [
    "The colors of the points outside shape <1> are <4>.",
    "The point colors outside shape <1> are <4>.",
    "Outside shape <1>, the point colors are <4>.",
    "The set of colors for points beyond shape <1> is <4>.",
    "All points outside shape <1> have colors <4>."
  ],
  "interior5": [
    "The shapes inside shape <1> are <4>.",
    "Those shapes within shape <1> are <4>.",
    "Shape <1> contains the following shapes: <4>.",
    "All shapes contained by shape <1> are <4>.",
    "The set of shapes inside shape <1> is <4>."
  ],
  "interior6": [
    "The shapes outside shape <1> are <4>.",
    "Those shapes outside shape <1> are <4>.",
    "Shape <1> has the following shapes outside of it: <4>.",
    "All shapes outside shape <1> are <4>.",
    "The set of shapes outside shape <1> is <4>."
  ],
  "interior7": [
    "The colors of the shapes inside shape <1> are <4>.",
    "The shape colors inside shape <1> are <4>.",
    "Inside shape <1>, the shapes have colors <4>.",
    "The set of colors for shapes within shape <1> is <4>.",
    "All shapes in shape <1> have colors <4>."
  ],
  "interior8": [
    "The colors of the shapes outside shape <1> are <4>.",
    "The shape colors outside shape <1> are <4>.",
    "Outside shape <1>, the shapes have colors <4>.",
    "The set of colors for shapes beyond shape <1> is <4>.",
    "All shapes outside shape <1> have colors <4>."
  ],
  "interior9": [
    "Points <4> are inside <1>.",
    "The points that lie within <1> are <4>.",
    "Inside <1> you can find points <4>.",
    "Those points inside <1> are <4>.",
    "The set of points inside <1> is <4>."
  ],
  "interior10": [
    "Points with color <4> are inside <1>.",
    "The colors of the points that lie within <1> are <4>.",
    "Within <1>, the point colors are <4>.",
    "The points inside <1> have colors <4>.",
    "The set of point colors inside <1> is <4>."
  ],
  "interior11": [
    "Shapes <4> are inside <1>.",
    "The shapes that lie within <1> are <4>.",
    "Within <1>, the shapes are <4>.",
    "Those shapes inside <1> are <4>.",
    "The set of shapes in <1> is <4>."
  ],
  "interior12": [
    "Shapes with color <4> are inside <1>.",
    "The colors of the shapes that lie within <1> are <4>.",
    "Within <1>, the shapes have colors <4>.",
    "Those shapes in <1> have colors <4>.",
    "The set of shape colors in <1> is <4>."
  ]
}


def generate_caption(diagram):
    for entity in diagram.entities:
        version_key = entity[0]
        a = random.choice(captions[version_key])
        for i in range(0, len(entity[1])):
            a = a.replace(f"<{i+1}>", entity[1][i])
    return a