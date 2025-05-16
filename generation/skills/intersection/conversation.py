from .rules import *
import random

conversation = {
  "conversation_long": {
    "intersection1": {
      "QA": [
        [
          "Does the <1> <2><3> intersect with the <4> <5><6>?",
          "Yes, the <1> <2><3> and the <4> <5><6> do intersect."
        ],
        [
          "Does the <1> <2><3> meet the <4> <5><6>?",
          "Yes, there is an intersection between the <1> <2><3> and the <4> <5><6>."
        ],
        [
          "Are we seeing an intersection between the <1> <2><3> and the <4> <5><6>?",
          "Yes, the <1> <2><3> intersects with the <4> <5><6>."
        ],
        [
          "Is there a point of intersection for the <1> <2><3> and the <4> <5><6>?",
          "Yes, the <1> <2><3> does meet the <4> <5><6>."
        ],
        [
          "Do the <1> <2><3> and the <4> <5><6> cross each other?",
          "Yes, they do intersect."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection2": {
      "QA": [
        [
          "Does the <1> <2><3> intersect with the <4> <5><6>?",
          "No, the <1> <2><3> and the <4> <5><6> do not intersect."
        ],
        [
          "Do the <1> <2><3> and the <4> <5><6> meet at any point?",
          "No, there is no intersection between the <1> <2><3> and the <4> <5><6>."
        ],
        [
          "Are the <1> <2><3> and the <4> <5><6> intersecting?",
          "No, those two do not meet."
        ],
        [
          "Is there a point of intersection for the <1> <2><3> and the <4> <5><6>?",
          "No, the <1> <2><3> and the <4> <5><6> remain separate."
        ],
        [
          "Could the <1> <2><3> and the <4> <5><6> cross each other?",
          "No, they do not intersect at all."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection3": {
      "QA": [
        [
          "Does the <1> with color <2> intersect with the <3> with color <4>?",
          "Yes, the <1> with color <2> and the <3> with color <4> do intersect."
        ],
        [
          "Are the <1> of color <2> and the <3> of color <4> meeting?",
          "Yes, they intersect."
        ],
        [
          "Is there an intersection between the <1> (color <2>) and the <3> (color <4>)?",
          "Yes, the <1> (color <2>) intersects with the <3> (color <4>)."
        ],
        [
          "Do we see the <1> of color <2> and the <3> of color <4> intersecting?",
          "Yes, the <1> of color <2> does meet the <3> of color <4>."
        ],
        [
          "Does the curve/line segment colored <2> intersect with the curve/line segment colored <4>?",
          "Yes, those two differently colored segments/curves intersect."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection4": {
      "QA": [
        [
          "Does the <1> with color <2> intersect with the <3> with color <4>?",
          "No, the <1> with color <2> and the <3> with color <4> do not intersect."
        ],
        [
          "Do the <1> colored <2> and the <3> colored <4> meet?",
          "No, there's no intersection."
        ],
        [
          "Is there a point of intersection between the <1> (color <2>) and the <3> (color <4>)?",
          "No, they remain separate."
        ],
        [
          "Are the <1> of color <2> and the <3> of color <4> crossing each other?",
          "No, those two do not meet."
        ],
        [
          "Could the <1> <2> and the <3> <4> come together at a point?",
          "No, there's no intersection."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection5": {
      "QA": [
        [
          "How many intersection points exist between the <1> <2><3> and the <4> <5><6>?",
          "The number of intersection points between the <1> <2><3> and the <4> <5><6> is <7>."
        ],
        [
          "What is the count of intersection points formed by the <1> <2><3> and the <4> <5><6>?",
          "There are <7> intersection points between the <1> <2><3> and the <4> <5><6>."
        ],
        [
          "Determine how many points of intersection appear where the <1> <2><3> meets the <4> <5><6>.",
          "The <1> <2><3> and the <4> <5><6> intersect in <7> points."
        ],
        [
          "Could you find the number of intersections between the <1> <2><3> and the <4> <5><6>?",
          "Yes, the total intersection points amount to <7>."
        ],
        [
          "Identify the total intersection points that occur when the <1> <2><3> meets the <4> <5><6>.",
          "They intersect at <7> points."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of intersection points between the <1> <2><3> and the <4> <5><6> is (<8>).",
            "Select one word from the parentheses to complete the sentence. The number of intersection points between the <1> <2><3> and the <4> <5><6> is <7>."
          ],
          [
            "Choose the correct term from the parentheses to finalize the statement. The total intersections of the <1> <2><3> and the <4> <5><6> is (<8>).",
            "Choose the correct term from the parentheses to finalize the statement. The total intersections of the <1> <2><3> and the <4> <5><6> is <7>."
          ],
          [
            "Pick the right option from the parentheses for the sentence. The <1> <2><3> and the <4> <5><6> intersect in (<8>) points.",
            "Pick the right option from the parentheses for the sentence. The <1> <2><3> and the <4> <5><6> intersect in <7> points."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "You must choose your answer from among <9>.",
          "Select the correct answer from <9>.",
          "Pick the right choice from <9>."
        ]
      }
    },
    "intersection6": {
      "QA": [
        [
          "How many intersection points exist between the <1> of color <2> and the <3> of color <4>?",
          "The number of intersection points between the <1> of color <2> and the <3> of color <4> is <5>."
        ],
        [
          "What is the count of intersections formed by the <1> in <2> and the <3> in <4>?",
          "They have <5> intersection points in total."
        ],
        [
          "Determine how many points of intersection appear where the <1> (color <2>) meets the <3> (color <4>).",
          "Those two intersect in <5> points."
        ],
        [
          "Could you find the number of intersections between the <1> colored <2> and the <3> colored <4>?",
          "Yes, the total intersection points amount to <5>."
        ],
        [
          "Identify the total intersection points that occur when the <1> <2> intersects with the <3> <4>.",
          "They intersect at <5> points."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of intersection points between the <1> of color <2> and the <3> of color <4> is (<6>).",
            "Select one word from the parentheses to complete the sentence. The number of intersection points between the <1> of color <2> and the <3> of color <4> is <5>."
          ],
          [
            "Choose the correct term from the parentheses to complete this statement. The total intersections of the <1> <2> and the <3> <4> is (<6>).",
            "Choose the correct term from the parentheses to complete this statement. The total intersections of the <1> <2> and the <3> <4> is <5>."
          ],
          [
            "Pick the right option from the parentheses to fill in the sentence. The <1> (color <2>) and the <3> (color <4>) intersect in (<6>) points.",
            "Pick the right option from the parentheses to fill in the sentence. The <1> (color <2>) and the <3> (color <4>) intersect in <5> points."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <7>.",
          "Please select the correct option from <7>.",
          "You should pick from <7>."
        ]
      }
    },
    "intersection7": {
      "QA": [
        [
          "Among the line segments in the figure, which one has the greatest number of intersection points with the curve colored <1>? Please state the color(s).",
          "The line segment(s) with the most intersection points with the curve colored <1> is the one (or ones) colored <4>."
        ],
        [
          "Which line segment in the diagram intersects with the <1>-colored curve the most times? Provide the color of that segment.",
          "The segment that has the highest number of intersections with the <1>-colored curve is colored <4>."
        ],
        [
          "Identify the line segment that yields the largest count of intersection points with the curve of color <1>. If multiple segments qualify, list them all.",
          "The line segment(s) with the greatest intersection count for the <1>-colored curve is <4>."
        ],
        [
          "Can you determine which line segment has the maximum intersections with the <1> curve? Please mention its color.",
          "The line segment with color <4> has the most intersections with the <1>-colored curve."
        ],
        [
          "Find the line segment that intersects most frequently with the curve of color <1>. If there is more than one, include all relevant colors.",
          "That line segment is colored <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the line segments in the figure, the one with the greatest number of intersections with the curve colored <1> is colored (<2>).",
            "Among the line segments in the figure, the one with the greatest number of intersections with the curve colored <1> is colored <4>."
          ],
          [
            "Choose from the parentheses to finish the statement. The line segment that most frequently intersects the <1>-colored curve is colored (<2>).",
            "The line segment that most frequently intersects the <1>-colored curve is colored <4>."
          ],
          [
            "Pick the correct term from the parentheses for the sentence. The segment whose intersections with the <1>-colored curve are the most is colored (<2>).",
            "The segment whose intersections with the <1>-colored curve are the most is colored <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please select from <3>.",
          "Choose the correct color from <3>."
        ]
      }
    },
    "intersection8": {
      "QA": [
        [
          "How many line segments in the figure intersect with the curve of color <1>?",
          "The number of line segments that meet the <1>-colored curve is <4>."
        ],
        [
          "Determine how many segments make contact with the <1>-colored curve in the diagram.",
          "They meet in <4> line segments."
        ],
        [
          "Can you find the total count of line segments that intersect with the curve colored <1>?",
          "The total number is <4>."
        ],
        [
          "Identify how many line segments intersect the curve of color <1> in the given figure.",
          "There are <4> such segments."
        ],
        [
          "What is the count of line segments that have intersection points with the <1>-colored curve?",
          "<4> line segments intersect with it."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of line segments intersecting the <1>-colored curve is (<2>).",
            "The number of line segments intersecting the <1>-colored curve is <4>."
          ],
          [
            "Choose the correct term from the parentheses. In this figure, the count of segments that meet the <1>-colored curve is (<2>).",
            "In this figure, the count of segments that meet the <1>-colored curve is <4>."
          ],
          [
            "Pick the right option in parentheses to finalize the sentence. The total of line segments intersecting the <1>-colored curve is (<2>).",
            "The total of line segments intersecting the <1>-colored curve is <4>."
          ]
        ],
        "type3": [
          "False"
        ],
        "type4": [
          "The answer must be selected from <3>.",
          "Please pick the correct number from <3>.",
          "Select your answer from the options in <3>."
        ]
      }
    },
    "intersection9": {
      "QA": [
        [
          "Which curve(s) in the figure have the greatest number of intersections with the line segment colored <1>? Please give the color(s).",
          "Among the curves shown, the one(s) that have the most intersection points with the line colored <1> is <4>."
        ],
        [
          "Identify the curve(s) that intersect with the line of color <1> the most. If multiple curves qualify, list them all.",
          "The curve(s) with the greatest number of intersections with the <1>-colored line is <4>."
        ],
        [
          "Determine which curve(s) yield the highest intersection count with the line segment colored <1>.",
          "The curve(s) that achieve the maximum intersections with the <1>-colored line is <4>."
        ],
        [
          "Can you find the curve that has the largest number of intersection points where it meets the line of color <1>?",
          "Yes, that curve is colored <4>."
        ],
        [
          "Which curve(s) in the diagram meet the <1>-colored line in the greatest number of points? Provide the color(s).",
          "They are the curves colored <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the curves, the one with the most intersections with the line colored <1> is colored (<2>).",
            "Among the curves, the one with the most intersections with the line colored <1> is colored <4>."
          ],
          [
            "Choose the correct option in parentheses. The curve(s) that intersect the <1>-colored line the most is (are) colored (<2>).",
            "The curve(s) that intersect the <1>-colored line the most is (are) colored <4>."
          ],
          [
            "Pick the correct term from the parentheses for the sentence. The curve that has the highest intersection count with the line of color <1> is (<2>).",
            "The curve that has the highest intersection count with the line of color <1> is <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be selected from <3>.",
          "Please choose from <3>.",
          "Pick from <3> for your answer."
        ]
      }
    },
    "intersection10": {
      "QA": [
        [
          "How many curves in the figure intersect with the line segment colored <1>?",
          "The number of curves that meet the <1>-colored line segment is <4>."
        ],
        [
          "Determine how many curves make contact with the line of color <1> in the diagram.",
          "They meet in <4> curves."
        ],
        [
          "Can you find the total count of curves that intersect with the line colored <1>?",
          "The total number is <4>."
        ],
        [
          "Identify how many curves intersect the line of color <1> in the given figure.",
          "There are <4> such curves."
        ],
        [
          "What is the count of curves that have intersection points with the <1>-colored line?",
          "<4> curves intersect with it."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of curves intersecting the line colored <1> is (<2>).",
            "The number of curves intersecting the line colored <1> is <4>."
          ],
          [
            "Choose the correct term from the parentheses for this statement. The count of curves meeting the <1>-colored line is (<2>).",
            "The count of curves meeting the <1>-colored line is <4>."
          ],
          [
            "Pick the right option in parentheses to finalize the sentence. The total of curves intersecting the <1>-colored line is (<2>).",
            "The total of curves intersecting the <1>-colored line is <4>."
          ]
        ],
        "type3": [
          "False"
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick the correct number from <3>.",
          "Select your answer from <3>."
        ]
      }
    },
    "intersection11": {
      "QA": [
        [
          "Do the boundaries of the two shapes in the figure meet?",
          "Yes, the boundaries of the two shapes in the figure do intersect."
        ],
        [
          "Are the boundaries of the two figures intersecting?",
          "Yes, those boundaries meet."
        ],
        [
          "Is there an intersection point along the boundaries of the two shapes?",
          "Yes, the two boundaries come into contact."
        ],
        [
          "Could the boundaries of both shapes possibly intersect?",
          "Yes, they do intersect."
        ],
        [
          "Do we see the boundaries of the two shapes in the diagram meet each other?",
          "Yes, they meet."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection12": {
      "QA": [
        [
          "Do the boundaries of the two shapes in the figure meet?",
          "No, the boundaries of the two shapes in the figure do not intersect."
        ],
        [
          "Are the boundaries of these two figures intersecting?",
          "No, they remain separate."
        ],
        [
          "Is there an intersection point along the boundaries of the two shapes?",
          "No, there is no contact between them."
        ],
        [
          "Could the boundaries of both shapes possibly intersect?",
          "No, they do not meet."
        ],
        [
          "Do we see the boundaries of the two shapes in the diagram meet each other?",
          "No, there is no intersection."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection13": {
      "QA": [
        [
          "How many intersection points occur where the boundaries of the two shapes meet?",
          "The boundaries of the two shapes intersect in <1> points."
        ],
        [
          "What is the number of intersections along the boundaries of the two figures?",
          "They have <1> intersection points."
        ],
        [
          "Determine the total count of intersection points formed by the boundaries of the two shapes.",
          "There are <1> such points of intersection."
        ],
        [
          "Identify how many times the boundaries of these two shapes intersect.",
          "They intersect <1> times."
        ],
        [
          "Can you tell me the number of intersection points along the boundaries of the two shapes in the figure?",
          "The number of boundary intersection points is <1>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of intersection points where the boundaries of the two shapes meet is (<2>)개.",
            "The number of intersection points where the boundaries of the two shapes meet is <1>개."
          ],
          [
            "Choose from the parentheses. The two shapes have (<2>) points of intersection along their boundaries.",
            "The two shapes have <1> points of intersection along their boundaries."
          ],
          [
            "Pick the correct option in parentheses. The boundary intersection count for the two shapes is (<2>)개.",
            "The boundary intersection count for the two shapes is <1>개."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be selected from <3>.",
          "Choose the correct option from <3>.",
          "Pick the right answer from <3>."
        ]
      }
    }
  },
  "conversation_short": {
    "intersection1": {
      "QA": [
        [
          "Do the <1> <2><3> and the <4> <5><6> intersect?",
          "Yes"
        ],
        [
          "Does the <1> <2><3> meet the <4> <5><6>?",
          "Yes"
        ],
        [
          "Are the <1> <2><3> and the <4> <5><6> intersecting?",
          "Yes"
        ],
        [
          "Is there an intersection between the <1> <2><3> and the <4> <5><6>?",
          "Yes"
        ],
        [
          "Do the <1> <2><3> and <4> <5><6> cross paths?",
          "Yes"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection2": {
      "QA": [
        [
          "Do the <1> <2><3> and the <4> <5><6> intersect?",
          "No"
        ],
        [
          "Does the <1> <2><3> meet the <4> <5><6>?",
          "No"
        ],
        [
          "Are <1> <2><3> and <4> <5><6> intersecting?",
          "No"
        ],
        [
          "Is there an intersection between <1> <2><3> and <4> <5><6>?",
          "No"
        ],
        [
          "Do the <1> <2><3> and <4> <5><6> cross paths?",
          "No"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection3": {
      "QA": [
        [
          "Do the <1> of color <2> and the <3> of color <4> intersect?",
          "Yes"
        ],
        [
          "Are the <1> colored <2> and the <3> colored <4> meeting?",
          "Yes"
        ],
        [
          "Is there an intersection between the <1> in <2> and the <3> in <4>?",
          "Yes"
        ],
        [
          "Does the <1> (color <2>) meet the <3> (color <4>)?",
          "Yes"
        ],
        [
          "Are the <1> with color <2> and the <3> with color <4> crossing paths?",
          "Yes"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection4": {
      "QA": [
        [
          "Do the <1> of color <2> and the <3> of color <4> intersect?",
          "No"
        ],
        [
          "Are the <1> colored <2> and the <3> colored <4> meeting?",
          "No"
        ],
        [
          "Is there an intersection between the <1> (color <2>) and the <3> (color <4>)?",
          "No"
        ],
        [
          "Does the <1> in <2> meet the <3> in <4>?",
          "No"
        ],
        [
          "Are the <1> of color <2> and the <3> of color <4> crossing each other?",
          "No"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection5": {
      "QA": [
        [
          "How many intersection points do the <1> <2><3> and the <4> <5><6> share?",
          "<7>"
        ],
        [
          "What is the number of intersections between the <1> <2><3> and the <4> <5><6>?",
          "<7>"
        ],
        [
          "State how many times the <1> <2><3> intersects with the <4> <5><6>.",
          "<7>"
        ],
        [
          "How many points of intersection are there for the <1> <2><3> and the <4> <5><6>?",
          "<7>"
        ],
        [
          "What's the intersection count between the <1> <2><3> and the <4> <5><6>?",
          "<7>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of intersection points between the <1> <2><3> and the <4> <5><6> is (<8>).",
            "The number of intersection points between the <1> <2><3> and the <4> <5><6> is <7>."
          ],
          [
            "Choose the correct term from the parentheses to finalize the statement. The total intersections of the <1> <2><3> and the <4> <5><6> is (<8>).",
            "The total intersections of the <1> <2><3> and the <4> <5><6> is <7>."
          ],
          [
            "Pick the right option from the parentheses for the sentence. The <1> <2><3> and the <4> <5><6> intersect in (<8>) points.",
            "The <1> <2><3> and the <4> <5><6> intersect in <7> points."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "You must choose your answer from among <9>.",
          "Select the correct answer from <9>.",
          "Pick the right choice from <9>."
        ]
      }
    },
    "intersection6": {
      "QA": [
        [
          "How many intersection points do the <1> of color <2> and the <3> of color <4> share?",
          "<5>"
        ],
        [
          "What is the number of intersections between the <1> <2> and the <3> <4>?",
          "<5>"
        ],
        [
          "State how many times the <1> (color <2>) intersects with the <3> (color <4>).",
          "<5>"
        ],
        [
          "How many points of intersection exist for the <1> in <2> and the <3> in <4>?",
          "<5>"
        ],
        [
          "What's the intersection count between the <1> with color <2> and the <3> with color <4>?",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of intersection points between the <1> of color <2> and the <3> of color <4> is (<6>).",
            "The number of intersection points between the <1> of color <2> and the <3> of color <4> is <5>."
          ],
          [
            "Choose the correct term from the parentheses to complete this statement. The total intersections of the <1> <2> and the <3> <4> is (<6>).",
            "The total intersections of the <1> <2> and the <3> <4> is <5>."
          ],
          [
            "Pick the right option from the parentheses to fill in the sentence. The <1> (color <2>) and the <3> (color <4>) intersect in (<6>) points.",
            "The <1> (color <2>) and the <3> (color <4>) intersect in <5> points."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <7>.",
          "Please select the correct option from <7>.",
          "You should pick from <7>."
        ]
      }
    },
    "intersection7": {
      "QA": [
        [
          "Which line segment in the figure has the greatest number of intersections with the curve of color <1>?",
          "<4>"
        ],
        [
          "Find the segment that intersects most frequently with the <1>-colored curve.",
          "<4>"
        ],
        [
          "Which segment shows the largest intersection count with the curve in <1>?",
          "<4>"
        ],
        [
          "Point out the line segment that meets the <1>-colored curve the most times.",
          "<4>"
        ],
        [
          "Which line segment color corresponds to the maximum intersections with the <1>-colored curve?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The line segment that has the most intersections with the <1>-colored curve is colored (<2>).",
            "The line segment that has the most intersections with the <1>-colored curve is colored <4>."
          ],
          [
            "Choose from the parentheses to finish the statement. The segment that most frequently intersects the curve of color <1> is colored (<2>).",
            "The segment that most frequently intersects the curve of color <1> is colored <4>."
          ],
          [
            "Pick the correct term from the parentheses for the sentence. The segment with the greatest intersection count for the <1>-colored curve is colored (<2>).",
            "The segment with the greatest intersection count for the <1>-colored curve is colored <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please select from <3>.",
          "Choose the correct color from <3>."
        ]
      }
    },
    "intersection8": {
      "QA": [
        [
          "How many line segments in the figure intersect the curve of color <1>?",
          "<4>"
        ],
        [
          "Identify how many segments meet the <1>-colored curve.",
          "<4>"
        ],
        [
          "What is the total number of segments that intersect with the curve <1>?",
          "<4>"
        ],
        [
          "State the count of line segments that have intersection points with the curve of color <1>.",
          "<4>"
        ],
        [
          "Determine how many segments cross paths with the curve in <1>.",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of line segments intersecting the <1>-colored curve is (<2>).",
            "The number of line segments intersecting the <1>-colored curve is <4>."
          ],
          [
            "Choose the correct term from the parentheses. The count of segments meeting the curve of color <1> is (<2>).",
            "The count of segments meeting the curve of color <1> is <4>."
          ],
          [
            "Pick the right option in parentheses. The total of line segments that intersect with the <1>-colored curve is (<2>).",
            "The total of line segments that intersect with the <1>-colored curve is <4>."
          ]
        ],
        "type3": [
          "False"
        ],
        "type4": [
          "The answer must be selected from <3>.",
          "Please pick the correct number from <3>.",
          "Select your answer from the options in <3>."
        ]
      }
    },
    "intersection9": {
      "QA": [
        [
          "Which curve in the figure has the greatest number of intersections with the line colored <1>?",
          "<4>"
        ],
        [
          "Identify the curve that meets the <1>-colored line most frequently.",
          "<4>"
        ],
        [
          "Which curve shows the highest intersection count with the line <1>?",
          "<4>"
        ],
        [
          "Point out the curve that has the most intersections with the line of color <1>.",
          "<4>"
        ],
        [
          "Which curve color corresponds to the maximum intersections with the <1>-colored line?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The curve with the most intersections with the line colored <1> is colored (<2>).",
            "The curve with the most intersections with the line colored <1> is colored <4>."
          ],
          [
            "Choose the correct option in parentheses. The curve that intersects the <1>-colored line the most is colored (<2>).",
            "The curve that intersects the <1>-colored line the most is colored <4>."
          ],
          [
            "Pick the right term from the parentheses for the sentence. The curve with the highest intersection count for the line of color <1> is (<2>).",
            "The curve with the highest intersection count for the line of color <1> is <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be selected from <3>.",
          "Please choose from <3>.",
          "Pick from <3> for your answer."
        ]
      }
    },
    "intersection10": {
      "QA": [
        [
          "How many curves in the figure intersect with the line colored <1>?",
          "<4>"
        ],
        [
          "Identify how many curves meet the <1>-colored line.",
          "<4>"
        ],
        [
          "What is the total number of curves that intersect with the line <1>?",
          "<4>"
        ],
        [
          "State the count of curves that have intersection points with the line of color <1>.",
          "<4>"
        ],
        [
          "Determine how many curves cross paths with the line in <1>.",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of curves intersecting the line colored <1> is (<2>).",
            "The number of curves intersecting the line colored <1> is <4>."
          ],
          [
            "Choose the correct term from the parentheses for this statement. The count of curves meeting the <1>-colored line is (<2>).",
            "The count of curves meeting the <1>-colored line is <4>."
          ],
          [
            "Pick the right option in parentheses to finalize the sentence. The total of curves intersecting the <1>-colored line is (<2>).",
            "The total of curves intersecting the <1>-colored line is <4>."
          ]
        ],
        "type3": [
          "False"
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick the correct number from <3>.",
          "Select your answer from <3>."
        ]
      }
    },
    "intersection11": {
      "QA": [
        [
          "Do the boundaries of the two shapes meet in the figure?",
          "Yes"
        ],
        [
          "Are the boundaries of these two shapes intersecting?",
          "Yes"
        ],
        [
          "Is there a boundary intersection between the two shapes?",
          "Yes"
        ],
        [
          "Could the boundaries of both shapes possibly meet?",
          "Yes"
        ],
        [
          "Do we see the boundaries of the two shapes touching?",
          "Yes"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection12": {
      "QA": [
        [
          "Do the boundaries of the two shapes meet in the figure?",
          "No"
        ],
        [
          "Are these two shapes' boundaries intersecting?",
          "No"
        ],
        [
          "Is there a boundary intersection between the two shapes?",
          "No"
        ],
        [
          "Could the boundaries of both shapes possibly meet?",
          "No"
        ],
        [
          "Do we see the boundaries of the two shapes touching?",
          "No"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          ""
        ],
        "type3": [
          ""
        ],
        "type4": [
          ""
        ]
      }
    },
    "intersection13": {
      "QA": [
        [
          "How many intersection points occur where the boundaries of the two shapes meet?",
          "<1>"
        ],
        [
          "What is the number of boundary intersections between the two figures?",
          "<1>"
        ],
        [
          "Determine the total count of intersection points formed by the boundaries of the two shapes.",
          "<1>"
        ],
        [
          "Identify how many times the two shapes intersect along their boundaries.",
          "<1>"
        ],
        [
          "Can you tell me the number of intersection points on the boundaries of these two shapes?",
          "<1>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The number of intersection points where the boundaries of the two shapes meet is (<2>)개.",
            "The number of intersection points where the boundaries of the two shapes meet is <1>개."
          ],
          [
            "Choose from the parentheses. The two shapes have (<2>) points of intersection along their boundaries.",
            "The two shapes have <1> points of intersection along their boundaries."
          ],
          [
            "Pick the correct option in parentheses. The boundary intersection count for the two shapes is (<2>)개.",
            "The boundary intersection count for the two shapes is <1>개."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be selected from <3>.",
          "Choose the correct option from <3>.",
          "Pick the right answer from <3>."
        ]
      }
    }
  }
}


def generate_conversation(diagram, long=False):
    conversation_list = []
    question_type = None
    for entity in diagram.entities:
        version_key = entity[0]
        if long:
            conversation_extracted = conversation['conversation_long']
        else:
            conversation_extracted = conversation['conversation_short']
        qa = random.choice(conversation_extracted[version_key]['QA'])
        additional = conversation_extracted[version_key]['additional']
        additional_type = []
        if additional['type1'] == ['True']:
            additional_type.append('type1')
        for candidate in ['type2', 'type3', 'type4']:
            if additional[candidate] != [""]:
                additional_type.append(candidate)
        additional_type = random.choice(additional_type)
        if additional_type != 'type1':
            if long:
                if additional_type == 'type2':
                    random_idx = random.randint(0, len(additional[additional_type])-1)
                    qa[0] = qa[0] + " "+ additional[additional_type][random_idx][0]
                    qa[1] = additional[additional_type][random_idx][1]
                else:
                    qa[0] = qa[0] + " "+ random.choice(additional[additional_type])
            else:
                if additional_type == 'type2':
                    random_idx = random.randint(0, len(additional[additional_type])-1)
                    qa[0] = qa[0] + " "+ additional[additional_type][random_idx][0]
                else:
                    qa[0] = qa[0] + " "+ random.choice(additional[additional_type])
        q = qa[0]
        a = qa[1]
        for i in range(0, len(entity[1])):
            q = q.replace(f"<{i+1}>", entity[1][i])
            a = a.replace(f"<{i+1}>", entity[1][i])
        conversation_list.append((q, a))
    question_type = version_key
    return question_type, conversation_list