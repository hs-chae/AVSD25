from .rules import *
import random

conversation = {
  "conversation_long": {
    "curvature1": {
      "QA": [
        [
          "In the given figure, multiple lines are drawn. Which lines are segments rather than curves? Provide all their colors.",
          "The line segments in the figure that are not curves are colored <3>."
        ],
        [
          "In the figure, there are various lines. Identify the colors of any lines that are segments instead of curves.",
          "The colors of the line segments, not curves, in the figure are <3>."
        ],
        [
          "Looking at the diagram, which lines are straight segments (not curves)? Name their colors.",
          "In this diagram, the lines that aren't curves are colored <3>."
        ],
        [
          "Observe the figure with several lines drawn. Please indicate which are line segments (as opposed to curves) by their color.",
          "Those line segments are colored <3>."
        ],
        [
          "Among the lines shown, which ones are not curved but straight? State the colors of those segments.",
          "The non-curved line segments in the figure are colored <3>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. In the figure, the line segments that are not curves are colored (<1>).",
            "In the figure, the line segments that are not curves are colored <3>."
          ],
          [
            "Choose the correct word from the parentheses to finalize the statement. The figure features segments (not curves) colored (<1>).",
            "The figure features segments (not curves) colored <3>."
          ],
          [
            "Pick the suitable option in parentheses to complete the sentence: The lines that aren't curves are colored (<1>).",
            "The lines that aren't curves are colored <3>."
          ],
          [
            "Decide which word in parentheses applies. The segments that are not curves in the figure come in color (<1>).",
            "The segments that are not curves in the figure come in color <3>."
          ],
          [
            "From the given parentheses, select the term that completes the sentence. The non-curve segments are colored (<1>).",
            "The non-curve segments are colored <3>."
          ]
        ],
        "type3": [
          "For example, if only the red line is a straight segment and the rest are curves, you should answer 'red'. The answer must be chosen from <2>.",
          "Suppose the red line alone is straight, and all others are curves; in that case, you should answer 'red'. You must select from <2>.",
          "Imagine that the only straight line is red, and the other lines are curvy; your answer would be 'red'. The options are <2>.",
          "If the red line is the sole segment, and everything else is curved, you would respond with 'red'. The correct response must be one of <2>.",
          "Consider a scenario where the red line is the single segment, while the rest are curves. Then 'red' is the correct answer, which must be picked from <2>."
        ],
        "type4": [
          "You must choose your answer from among <2>.",
          "Select the correct color from <2>.",
          "Your response should be taken from the list <2>.",
          "Pick the correct answer from <2>.",
          "The valid answer is one of <2>."
        ]
      }
    },
    "curvature2": {
      "QA": [
        [
          "In the figure, several lines are drawn. Which ones are curves rather than a straight line? Provide their colors.",
          "In this figure, the lines that are not straight lines (but curves) are colored <3>."
        ],
        [
          "Looking at the diagram, identify any lines that are curves (not straight lines). Name the colors.",
          "The lines that aren't straight lines in this diagram have color <3>."
        ],
        [
          "Among the lines shown, which ones are curves as opposed to straight lines? Specify their colors.",
          "The curves in the figure, distinct from straight lines, are colored <3>."
        ],
        [
          "Observe the figure. Which lines are curved rather than straight? Indicate their colors.",
          "Those curved lines are colored <3>."
        ],
        [
          "Which lines in the diagram qualify as curves (not straight lines)? State all their colors.",
          "All non-straight lines in the figure are colored <3>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. In the figure, the lines that are not straight lines are colored (<1>).",
            "In the figure, the lines that are not straight lines are colored <3>."
          ],
          [
            "Choose the appropriate term from the parentheses. The figure shows curves (not a straight line) colored (<1>).",
            "The figure shows curves colored <3>."
          ],
          [
            "Pick the correct word in parentheses to finalize the statement: The non-straight lines are colored (<1>).",
            "The non-straight lines in the figure are colored <3>."
          ],
          [
            "Decide which word in parentheses applies. The lines that deviate from being straight are colored (<1>).",
            "The lines that deviate from being straight are colored <3>."
          ],
          [
            "From the parentheses, choose the term that completes the sentence. The curved lines in the figure come in color (<1>).",
            "The curved lines in the figure come in color <3>."
          ]
        ],
        "type3": [
          "For example, if only the red line is a curve and the others are straight lines, then the answer should be 'red'. The answer must be one of <2>.",
          "Suppose the red line alone is curved, and the others are straight lines; then you should respond 'red'. The valid options are in <2>.",
          "Imagine only the red line is a curve, with the rest being straight lines. The correct response is 'red', chosen from <2>.",
          "If the line in red is the sole curve, while every other line is straight, you must answer 'red' from the choices in <2>.",
          "Consider a situation in which the red line is the only curve, and the rest are straight. Hence, 'red' is correct, picked from <2>."
        ],
        "type4": [
          "Your answer must be selected from <2>.",
          "Please choose from <2> for your answer.",
          "Pick the correct color from among <2>.",
          "The valid choice should be made from <2>.",
          "Select your answer from the list <2>."
        ]
      }
    },
    "curvature3": {
      "QA": [
        [
          "Among the various colored curves in the figure, choose the curve that forms part of a circle.",
          "Among the differently colored curves, the curve colored <3> is the part of a circle."
        ],
        [
          "From the figure, which colored curve is actually part of a circle?",
          "The curve with color <3> is a portion of a circle."
        ],
        [
          "Identify which curve is part of a circle among the multiple colored curves in the diagram.",
          "The circular segment in the diagram is the one colored <3>."
        ],
        [
          "Looking at the multiple colors of curves, which one belongs to a circle?",
          "The circular portion is colored <3>."
        ],
        [
          "Observe the figure. Which of these colored curves is part of a circle?",
          "The curve that is part of a circle is colored <3>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the various colored curves, the one colored (<1>) is part of a circle.",
            "Among the various colored curves, the one colored <3> is part of a circle."
          ],
          [
            "Choose the correct word in parentheses. The curve with color (<1>) is part of a circle.",
            "The curve with color <3> is part of a circle."
          ],
          [
            "Pick from the parentheses to finalize the sentence. The curve that forms part of a circle has color (<1>).",
            "The curve that forms part of a circle has color <3>."
          ],
          [
            "Decide which term fits in the parentheses: The circle portion is colored (<1>).",
            "The circle portion is colored <3>."
          ],
          [
            "From the options in parentheses, identify the color of the curve that is part of a circle: (<1>).",
            "That curve is colored <3>, forming part of the circle."
          ]
        ],
        "type3": [
          "For example, if the yellow curve is part of a circle, you should answer 'yellow'. The answer must come from <2>.",
          "Suppose the only arc belonging to a circle is yellow; then your response is 'yellow', which must be chosen from <2>.",
          "If you find that the yellow curve is circular, answer 'yellow'. Choose from <2>.",
          "When the yellow curve is the circle segment, 'yellow' is your answer. It should be selected from <2>.",
          "Imagine the circle portion is the yellow curve. In that case, 'yellow' is correct, picked from <2>."
        ],
        "type4": [
          "You must select your answer from <2>.",
          "Choose the correct color from among <2>.",
          "The valid answer is within <2>.",
          "Pick the appropriate color from <2>.",
          "The correct response should be one of <2>."
        ]
      }
    },
    "curvature4": {
      "QA": [
        [
          "Several circles of different colors are given in the figure. Among these, find the circle with the largest absolute curvature and provide its color.",
          "Among the given circles, the circle with the largest absolute curvature is colored <3>."
        ],
        [
          "In the figure, multiple circles appear. Which circle has the greatest absolute curvature? State its color.",
          "The circle that exhibits the greatest absolute curvature has color <3>."
        ],
        [
          "Identify which of the colored circles possesses the highest absolute curvature. What is its color?",
          "The circle with the highest absolute curvature is colored <3>."
        ],
        [
          "Looking at the various colored circles, which one has the maximal absolute curvature? Provide the color.",
          "That circle with the largest absolute curvature has color <3>."
        ],
        [
          "Among the colored circles shown, which has the biggest absolute curvature? Please specify its color.",
          "The circle boasting the greatest absolute curvature is colored <3>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the given circles, the circle with the largest absolute curvature is colored (<1>).",
            ""
          ],
          [
            "Choose the correct term in parentheses. The circle possessing the highest absolute curvature is colored (<1>).",
            ""
          ],
          [
            "Pick a word from the parentheses to finalize the statement: The circle with the greatest absolute curvature is colored (<1>).",
            ""
          ],
          [
            "Decide which word in parentheses applies. The circle that has the maximum absolute curvature is colored (<1>).",
            ""
          ],
          [
            "From the options provided in parentheses, identify the circle with the highest absolute curvature: It's colored (<1>).",
            ""
          ]
        ],
        "type3": [
          "For example, if the circle with the largest absolute curvature is blue, the answer should be 'blue'. The answer must be one of <2>.",
          "Suppose the circle of maximum absolute curvature is colored blue. In that case, answer 'blue', chosen from <2>.",
          "If the circle that has the biggest absolute curvature is blue, then 'blue' is the correct answer from <2>.",
          "When the blue circle has the highest absolute curvature, you answer 'blue'. Please pick from <2>.",
          "Imagine the most curved circle is the blue one; your response is 'blue', selected from <2>."
        ],
        "type4": [
          "The answer must be selected from <2>.",
          "You need to choose from among <2>.",
          "Pick your answer from <2>.",
          "Please select the color from <2>.",
          "The valid choice is among <2>."
        ]
      }
    },
    "curvature5": {
      "QA": [
        [
          "Several circles of different colors appear in the figure. Find the circle with the smallest absolute curvature and give its color.",
          "Among the given circles, the circle with the smallest absolute curvature is colored <3>."
        ],
        [
          "Look at the multiple colored circles. Which has the least absolute curvature? Indicate its color.",
          "The circle with the least absolute curvature has color <3>."
        ],
        [
          "Identify the colored circle that exhibits the smallest absolute curvature. State the color.",
          "That circle with the smallest absolute curvature is colored <3>."
        ],
        [
          "Which circle, among those shown, has the minimal absolute curvature? Provide its color.",
          "This circle with the minimal absolute curvature is colored <3>."
        ],
        [
          "From the circles displayed, which one has the lowest absolute curvature? Please name its color.",
          "The circle possessing the lowest absolute curvature is colored <3>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the given circles, the circle with the smallest absolute curvature is colored (<1>).",
            ""
          ],
          [
            "Choose the appropriate word in parentheses. The circle with the minimal absolute curvature is colored (<1>).",
            ""
          ],
          [
            "Pick a term from the parentheses to complete the statement: The circle with the least absolute curvature is colored (<1>).",
            ""
          ],
          [
            "Decide which word applies. The circle that has the lowest absolute curvature is colored (<1>).",
            ""
          ],
          [
            "From the options provided, identify which circle is colored (<1>) for the smallest absolute curvature.",
            ""
          ]
        ],
        "type3": [
          "For example, if the circle with the smallest absolute curvature is blue, you should answer 'blue'. The answer must be one of <2>.",
          "Suppose the smallest absolute curvature belongs to the blue circle. Then the correct response is 'blue', taken from <2>.",
          "If the blue circle happens to have the least absolute curvature, the answer is 'blue' from <2>.",
          "When the blue circle exhibits the lowest absolute curvature, 'blue' is the correct answer. Please pick from <2>.",
          "Imagine the circle with minimal curvature is the blue one; you'd respond 'blue', selected from <2>."
        ],
        "type4": [
          "You must choose your answer from <2>.",
          "Select the correct color from among <2>.",
          "Pick the appropriate color from <2>.",
          "The valid answer is included in <2>.",
          "Select your response from <2>."
        ]
      }
    },
    "curvature6": {
      "QA": [
        [
          "On the given curve, there are multiple points placed. Which point has the greatest absolute curvature?",
          "Among the points on the given curve, the point with the largest absolute curvature is <3>."
        ],
        [
          "Several points are marked on the curve. Identify the point that exhibits the maximum absolute curvature.",
          "The point with the highest absolute curvature on this curve is <3>."
        ],
        [
          "Looking at the points on the curve, which point's curvature is greatest in absolute value?",
          "The point with the greatest absolute curvature is <3>."
        ],
        [
          "Observe the marked points on the curve. Which one has the largest absolute curvature?",
          "It turns out that <3> is the point with the largest absolute curvature."
        ],
        [
          "Among the points placed on the curve, find the one having the greatest absolute curvature.",
          "The point featuring the greatest absolute curvature is <3>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the points on the curve, the point with the largest absolute curvature is (<1>).",
            "Among the points on the curve, the point with the largest absolute curvature is <3>."
          ],
          [
            "Choose the correct term in parentheses. The point of maximum absolute curvature is (<1>).",
            "The point of maximum absolute curvature is <3>."
          ],
          [
            "Pick from the parentheses to finalize the statement: The point with the greatest absolute curvature is (<1>).",
            "The point with the greatest absolute curvature is <3>."
          ],
          [
            "Decide which word in parentheses applies. The point that holds the highest absolute curvature is (<1>).",
            "The point that holds the highest absolute curvature is <3>."
          ],
          [
            "From the options provided, identify which point is (<1>) for the largest absolute curvature.",
            "The point showing the largest absolute curvature is <3>."
          ]
        ],
        "type3": [
          "For example, if point A is the one with the greatest absolute curvature, you should answer: Answer : A.",
          "Suppose point A has the highest absolute curvature. Then your answer must be 'Answer : A'.",
          "If point A demonstrates the largest absolute curvature, the correct response is 'Answer : A'.",
          "In the scenario where A stands for the point with the greatest curvature, respond 'Answer : A'.",
          "Imagine that A is the point with the maximum absolute curvature. Then your answer is 'Answer : A'."
        ],
        "type4": [
          "Your answer must be selected from <2>.",
          "Please choose from <2>.",
          "Pick the correct point from among <2>.",
          "Select one point in <2> as your answer.",
          "The valid response is in <2>."
        ]
      }
    },
    "curvature7": {
      "QA": [
        [
          "On the given curve, there are multiple points. Which point shows the smallest absolute curvature?",
          "Among the points on the given curve, the point with the smallest absolute curvature is <3>."
        ],
        [
          "Several points lie on the curve. Identify the point with the least absolute curvature.",
          "The point with the lowest absolute curvature on this curve is <3>."
        ],
        [
          "Check the points on the curve. Which one has the minimal absolute curvature?",
          "The point that demonstrates the smallest absolute curvature is <3>."
        ],
        [
          "Observe the points marked on the curve. Which point has the least absolute curvature?",
          "<3> is the point with the least absolute curvature."
        ],
        [
          "Among all the points placed on the curve, which has the smallest absolute curvature?",
          "The point that exhibits the smallest absolute curvature is <3>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the points on the curve, the point with the smallest absolute curvature is (<1>).",
            "Among the points on the curve, the point with the smallest absolute curvature is <3>."
          ],
          [
            "Choose the correct term in parentheses. The point of minimum absolute curvature is (<1>).",
            "The point of minimum absolute curvature is <3>."
          ],
          [
            "Pick from the parentheses to complete the statement: The point with the least absolute curvature is (<1>).",
            "The point with the least absolute curvature is <3>."
          ],
          [
            "Decide which option applies. The point that has the lowest absolute curvature is (<1>).",
            "The point that has the lowest absolute curvature is <3>."
          ],
          [
            "From the parentheses, select the point that exhibits the smallest absolute curvature: (<1>).",
            "That point of smallest absolute curvature is <3>."
          ]
        ],
        "type3": [
          "For example, if point Z has the smallest absolute curvature, you should answer: Answer : Z.",
          "Suppose point Z shows the least absolute curvature. Then your response is 'Answer : Z'.",
          "If Z has the minimum absolute curvature, the correct answer is 'Answer : Z'.",
          "Where point Z is the one with the lowest curvature, respond 'Answer : Z'.",
          "Imagine that the point Z has the smallest absolute curvature. In that case, your answer is 'Answer : Z'."
        ],
        "type4": [
          "The answer must be picked from <2>.",
          "Choose your response from <2>.",
          "Select the correct point out of <2>.",
          "You must pick your answer from <2>.",
          "The valid choice is found in <2>."
        ]
      }
    },
    "curvature8": {
      "QA": [
        [
          "There are multiple curves passing through point <1>. Find which curve has the largest absolute curvature at point <1> and name its color.",
          "Among the given curves, the one with the greatest absolute curvature at point <1> is colored <4>."
        ],
        [
          "Looking at the curves passing through point <1>, which has the highest absolute curvature at that point? State the color.",
          "The curve with the highest absolute curvature at point <1> has the color <4>."
        ],
        [
          "In the diagram, several curves intersect point <1>. Identify the curve whose curvature is greatest in absolute value at <1>, and give its color.",
          "The curve that has the maximum absolute curvature at point <1> is colored <4>."
        ],
        [
          "Observe the curves going through <1>. Which one has the largest absolute curvature there? Provide the color.",
          "The curve showing the largest curvature at <1> is colored <4>."
        ],
        [
          "Among these curves passing through point <1>, which attains the greatest absolute curvature at that point? Indicate its color.",
          "That curve is colored <4>, having the greatest absolute curvature at <1>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the given curves, the one with the greatest absolute curvature at point <1> is colored (<2>).",
            "Among the given curves, the one with the greatest absolute curvature at point <1> is colored <4>."
          ],
          [
            "Choose the correct color in parentheses. The curve with the maximum absolute curvature at <1> is colored (<2>).",
            "The curve with the maximum absolute curvature at <1> is colored <4>."
          ],
          [
            "Pick from the parentheses to finalize the statement. The curve that shows the highest absolute curvature at <1> is colored (<2>).",
            "The curve that shows the highest absolute curvature at <1> is colored <4>."
          ],
          [
            "Decide which term in parentheses applies: The curve with the greatest absolute curvature at point <1> has color (<2>).",
            "The curve with the greatest absolute curvature at point <1> has color <4>."
          ],
          [
            "From the parentheses, select the color for the curve that has the largest curvature at <1>: (<2>).",
            "That curve is colored <4>, featuring the greatest curvature at <1>."
          ]
        ],
        "type3": [
          "For example, if the purple curve has the maximum absolute curvature at point <1>, then answer: Answer : purple.",
          "Suppose the purple curve exhibits the greatest absolute curvature at <1>. Then your answer is 'Answer : purple'.",
          "If the curve in purple is the one with the highest curvature at <1>, respond 'Answer : purple'.",
          "When purple is the color of the curve with the greatest curvature at <1>, you must answer 'Answer : purple'.",
          "Imagine that at point <1>, the purple curve has the maximum absolute curvature. Then 'Answer : purple' is correct."
        ],
        "type4": [
          "You must choose from <3>.",
          "Select the correct color out of <3>.",
          "The valid answer is found in <3>.",
          "Pick your response from <3>.",
          "Make sure to choose your answer from <3>."
        ]
      }
    },
    "curvature9": {
      "QA": [
        [
          "There are multiple curves passing through point <1>. Among these, which curve has the smallest absolute curvature at point <1>? Provide its color.",
          "Among the given curves, the one with the smallest absolute curvature at point <1> is colored <4>."
        ],
        [
          "From the curves that go through <1>, identify the curve whose absolute curvature is the least at that point. State the color.",
          "The curve with the smallest absolute curvature at <1> is colored <4>."
        ],
        [
          "In the diagram, several curves intersect point <1>. Which shows the lowest absolute curvature at <1>? Indicate its color.",
          "That curve, with the lowest absolute curvature at <1>, is colored <4>."
        ],
        [
          "Looking at the curves passing through <1>, which one has the minimal absolute curvature there? Provide the color.",
          "The curve that displays the smallest absolute curvature at <1> is colored <4>."
        ],
        [
          "Among these curves through <1>, pick the curve with the least absolute curvature at that point. What is its color?",
          "It is the curve colored <4>, having the smallest absolute curvature at <1>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the given curves, the one with the smallest absolute curvature at point <1> is colored (<2>).",
            "Among the given curves, the one with the smallest absolute curvature at point <1> is colored <4>."
          ],
          [
            "Choose the correct color from the parentheses. The curve of minimum absolute curvature at <1> has color (<2>).",
            "The curve of minimum absolute curvature at <1> has color <4>."
          ],
          [
            "Pick the suitable term from the parentheses to finalize the statement. The curve with the least absolute curvature at <1> is colored (<2>).",
            "The curve with the least absolute curvature at <1> is colored <4>."
          ],
          [
            "Decide which parentheses term applies: The curve with the lowest absolute curvature at <1> is colored (<2>).",
            "The curve with the lowest absolute curvature at <1> is colored <4>."
          ],
          [
            "From the parentheses, select the color of the curve that has the smallest curvature at <1>: (<2>).",
            "That curve is colored <4>, showcasing the smallest absolute curvature at <1>."
          ]
        ],
        "type3": [
          "For example, if the purple curve has the smallest absolute curvature at point <1>, then the answer is: Answer : purple.",
          "Suppose the purple curve exhibits the least absolute curvature at <1>. Answer : purple.",
          "If the curve in purple shows the lowest curvature at <1>, respond with 'Answer : purple'.",
          "When purple is the color of the curve that has the minimum curvature at <1>, you must write 'Answer : purple'.",
          "Imagine that the purple curve has the smallest absolute curvature at <1>. Then your answer is 'Answer : purple'."
        ],
        "type4": [
          "Choose your answer from <3>.",
          "Select the correct color out of <3>.",
          "The valid option is within <3>.",
          "Pick your answer from the list <3>.",
          "You must select from <3>."
        ]
      }
    }
  },
  "conversation_short": {
    "curvature1": {
      "QA": [
        [
          "Which lines are segments instead of curves in the figure?",
          "<3>"
        ],
        [
          "Identify the straight segments (not curves) by their colors.",
          "<3>"
        ],
        [
          "Which colored lines in the diagram are not curves?",
          "<3>"
        ],
        [
          "Point out the non-curved line segments. What are their colors?",
          "<3>"
        ],
        [
          "From the lines shown, which are segments rather than curves?",
          "<3>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. The line segments that are not curves in the figure are colored (<1>).",
          "Choose the correct term from parentheses. The non-curve segments appear in color (<1>).",
          "Pick the option in parentheses that describes the straight segments: (<1>).",
          "Decide which parentheses term applies to the line segments: (<1>).",
          "From the parentheses, specify the color of the non-curve segments: (<1>)."
        ],
        "type3": [
          "For example, if only the red line is a segment, answer 'red' from <2>.",
          "Suppose red is the only straight segment, so you'd answer 'red'. The choice must come from <2>.",
          "If the red line is the sole non-curve, the correct response is 'red' from <2>.",
          "When the red line is the only segment, choose 'red' from <2>.",
          "Imagine the single straight line is red. Then you must pick 'red' out of <2>."
        ],
        "type4": [
          "The answer should be chosen from <2>.",
          "Select from <2> as your answer.",
          "Pick the correct color from <2>.",
          "The valid response must be one of <2>.",
          "Your answer must come from <2>."
        ]
      }
    },
    "curvature2": {
      "QA": [
        [
          "Which lines are curves, not straight lines?",
          "<3>"
        ],
        [
          "Identify any curved lines in the figure and give their colors.",
          "<3>"
        ],
        [
          "Point out the lines that aren't straight in the diagram.",
          "<3>"
        ],
        [
          "Which colored lines are non-straight (curved) in the figure?",
          "<3>"
        ],
        [
          "Which lines qualify as curves rather than straight lines?",
          "<3>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from parentheses: The lines that aren't straight are colored (<1>).",
          "Choose the correct option from parentheses for the curve color (<1>).",
          "Pick the word in parentheses that fits the curved lines (<1>).",
          "Which parentheses term applies to the curved lines' color? (<1>)",
          "From the parentheses, select the color for the curve: (<1>)."
        ],
        "type3": [
          "For example, if red is the only curve, choose 'red' from <2>.",
          "Suppose red alone is a curve; then 'red' is your answer from <2>.",
          "If the red line is curved, respond with 'red', which is in <2>.",
          "In case only the red line is curved, your answer is 'red' from <2>.",
          "Imagine the red line is the sole curve. Then 'red' is correct out of <2>."
        ],
        "type4": [
          "Choose your answer from <2>.",
          "Select the correct color from among <2>.",
          "Pick your response out of <2>.",
          "You must pick your answer from <2>.",
          "The valid option is in <2>."
        ]
      }
    },
    "curvature3": {
      "QA": [
        [
          "Which colored curve in the figure is part of a circle?",
          "<3>"
        ],
        [
          "Identify the curve that forms part of a circle.",
          "<3>"
        ],
        [
          "Find the circle segment among these colored curves.",
          "<3>"
        ],
        [
          "Which curve belongs to a circle?",
          "<3>"
        ],
        [
          "Point out the circular arc from the colored curves.",
          "<3>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from parentheses. The circle portion is colored (<1>).",
          "Choose the correct color from (<1>) for the circle arc.",
          "Pick the parentheses term that indicates the circle segment's color (<1>).",
          "Which parentheses option matches the circle arc color? (<1>)",
          "Identify which color in parentheses belongs to the circle portion (<1>)."
        ],
        "type3": [
          "For instance, if the yellow curve is the circular part, answer 'yellow'. The answer is in <2>.",
          "Suppose the circular arc is yellow; then pick 'yellow' from <2>.",
          "If the yellow curve is the circle portion, respond 'yellow', choosing from <2>.",
          "When the circle arc is yellow, the correct response is 'yellow' out of <2>.",
          "Imagine the yellow curve is the circle segment; you must answer 'yellow' from <2>."
        ],
        "type4": [
          "Select your answer from <2>.",
          "Pick the correct color from <2>.",
          "You must choose from <2>.",
          "The valid response is among <2>.",
          "Please select from <2>."
        ]
      }
    },
    "curvature4": {
      "QA": [
        [
          "Which circle has the largest absolute curvature among those shown?",
          "<3>"
        ],
        [
          "Identify the color of the circle with the greatest absolute curvature.",
          "<3>"
        ],
        [
          "Point out the circle possessing the maximum absolute curvature.",
          "<3>"
        ],
        [
          "Among the colored circles, which has the highest curvature magnitude?",
          "<3>"
        ],
        [
          "Which circle stands out for having the largest absolute curvature?",
          "<3>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses: The circle with the greatest absolute curvature is colored (<1>).",
          "Choose the correct term in parentheses for the circle of maximal curvature (<1>).",
          "Pick the parentheses option that indicates the highest curvature circle (<1>).",
          "Which parentheses term applies to the circle with the largest curvature? (<1>)",
          "From the options, identify the color for the most curved circle (<1>)."
        ],
        "type3": [
          "For instance, if the blue circle has the maximum absolute curvature, choose 'blue' from <2>.",
          "Suppose the circle with the highest curvature is blue. Then your answer is 'blue' out of <2>.",
          "If the blue circle is the most curved, respond 'blue' from <2>.",
          "When blue has the greatest curvature, 'blue' is your choice from <2>.",
          "Imagine the blue circle is the steepest in curvature; thus, 'blue' is the correct answer from <2>."
        ],
        "type4": [
          "Your answer must come from <2>.",
          "Pick the color out of <2>.",
          "Select your response from <2>.",
          "You need to choose from <2>.",
          "The valid answer is within <2>."
        ]
      }
    },
    "curvature5": {
      "QA": [
        [
          "Which circle shows the smallest absolute curvature among the ones displayed?",
          "<3>"
        ],
        [
          "Identify the color of the circle with the least absolute curvature.",
          "<3>"
        ],
        [
          "Point out the circle possessing the minimum absolute curvature.",
          "<3>"
        ],
        [
          "Among the circles in the figure, which has the lowest curvature magnitude?",
          "<3>"
        ],
        [
          "Which circle is noted for having the smallest absolute curvature?",
          "<3>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses: The circle with the smallest absolute curvature is colored (<1>).",
          "Choose the correct term in parentheses for the circle of minimal curvature (<1>).",
          "Pick the parentheses option that corresponds to the least curvature circle (<1>).",
          "Which parentheses term applies to the circle with the smallest curvature? (<1>)",
          "Identify the color for the circle with the lowest absolute curvature (<1>)."
        ],
        "type3": [
          "For instance, if the blue circle has the smallest absolute curvature, respond 'blue' from <2>.",
          "Suppose the circle with the minimal curvature is blue; then choose 'blue' out of <2>.",
          "If the blue circle is the least curved, the answer is 'blue' from <2>.",
          "When blue has the lowest curvature, 'blue' is your response from <2>.",
          "Imagine that the blue circle is the least curved one. Then pick 'blue' from <2>."
        ],
        "type4": [
          "You must choose your answer from <2>.",
          "Select from <2> for your response.",
          "Pick your answer out of <2>.",
          "The valid color is one of <2>.",
          "Your choice must be within <2>."
        ]
      }
    },
    "curvature6": {
      "QA": [
        [
          "Which point on the given curve has the largest absolute curvature?",
          "<3>"
        ],
        [
          "Identify the point that shows the maximum curvature in absolute value.",
          "<3>"
        ],
        [
          "Which point stands out for having the greatest absolute curvature?",
          "<3>"
        ],
        [
          "Among the marked points, which has the highest curvature magnitude?",
          "<3>"
        ],
        [
          "Find the point with the greatest absolute curvature on this curve.",
          "<3>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from parentheses. The point of largest absolute curvature is (<1>).",
          "Choose the correct option: The maximum curvature belongs to (<1>).",
          "Pick the parentheses term indicating the point with greatest curvature (<1>).",
          "Which parentheses word represents the point of highest curvature? (<1>)",
          "Identify from the parentheses which point is highest in curvature (<1>)."
        ],
        "type3": [
          "For example, if it's A, you answer: Answer : A.",
          "Suppose A is the point with the largest curvature. Then 'Answer : A'.",
          "If A has the maximum curvature, respond 'Answer : A'.",
          "When A shows the highest curvature, your answer is 'Answer : A'.",
          "Imagine that A is the point with the biggest curvature. Then pick 'Answer : A'."
        ],
        "type4": [
          "Select your answer from <2>.",
          "Choose from <2> for the point.",
          "Pick the correct point in <2>.",
          "You must decide from <2>.",
          "The valid choice is within <2>."
        ]
      }
    },
    "curvature7": {
      "QA": [
        [
          "Which point on this curve has the smallest absolute curvature?",
          "<3>"
        ],
        [
          "Identify the point that shows the least absolute curvature.",
          "<3>"
        ],
        [
          "Which point presents the lowest absolute curvature among those on the curve?",
          "<3>"
        ],
        [
          "Among the points placed, which has the minimal curvature magnitude?",
          "<3>"
        ],
        [
          "Find the point with the smallest absolute curvature.",
          "<3>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from parentheses. The point of smallest absolute curvature is (<1>).",
          "Choose the correct term representing the point with the lowest curvature: (<1>).",
          "Pick the parentheses option for the minimal curvature point (<1>).",
          "Which parentheses word applies to the point with the smallest curvature? (<1>)",
          "Identify the point with the lowest curvature from parentheses: (<1>)."
        ],
        "type3": [
          "For example, if it's Z, answer: Answer : Z.",
          "Suppose Z is the point with the smallest curvature. Then 'Answer : Z'.",
          "If Z has the least curvature, respond with 'Answer : Z'.",
          "When Z is minimal in curvature, you must write 'Answer : Z'.",
          "Imagine Z is the point of the lowest curvature. Your answer is 'Answer : Z'."
        ],
        "type4": [
          "Select your answer from <2>.",
          "Pick the correct point out of <2>.",
          "You must choose from <2>.",
          "The valid answer is in <2>.",
          "Decide among <2> for your response."
        ]
      }
    },
    "curvature8": {
      "QA": [
        [
          "Among the curves passing through <1>, which has the largest absolute curvature there?",
          "<4>"
        ],
        [
          "Identify the curve that reaches the highest absolute curvature at point <1>.",
          "<4>"
        ],
        [
          "Which curve exhibits the greatest curvature at <1>?",
          "<4>"
        ],
        [
          "Find the curve with the largest absolute curvature at point <1>.",
          "<4>"
        ],
        [
          "Point out the color of the curve that shows the maximum curvature at <1>.",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from parentheses. The curve with the greatest curvature at <1> is colored (<2>).",
          "Choose the correct color for the curve that has the maximum curvature at <1> (<2>).",
          "Pick the parentheses term for the curve with the highest curvature at <1> (<2>).",
          "Which parentheses option indicates the color of the max curvature curve at <1>? (<2>)",
          "Identify from parentheses the color of the curve with the largest curvature at <1> (<2>)."
        ],
        "type3": [
          "For example, if it's purple, answer: Answer : purple.",
          "Suppose purple is the curve with the greatest curvature. Then 'Answer : purple'.",
          "If purple shows the max curvature at <1>, respond 'Answer : purple'.",
          "When purple has the highest curvature at <1>, your answer is 'Answer : purple'.",
          "Imagine the purple curve is the top curvature at <1>. Then pick 'Answer : purple'."
        ],
        "type4": [
          "Select from <3>.",
          "Pick the correct color in <3>.",
          "You must choose from <3>.",
          "The valid answer is inside <3>.",
          "Choose the color out of <3>."
        ]
      }
    },
    "curvature9": {
      "QA": [
        [
          "Among the curves passing through <1>, which one has the smallest absolute curvature there?",
          "<4>"
        ],
        [
          "Identify the curve with the least absolute curvature at <1>.",
          "<4>"
        ],
        [
          "Which curve exhibits the lowest curvature at point <1>?",
          "<4>"
        ],
        [
          "Find the curve possessing the minimal absolute curvature at <1>.",
          "<4>"
        ],
        [
          "Which of these curves shows the smallest absolute curvature at <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from parentheses. The curve with the smallest curvature at <1> is colored (<2>).",
          "Choose the correct color from parentheses for the minimum curvature at <1> (<2>).",
          "Pick the parentheses term indicating the curve of least curvature at <1> (<2>).",
          "Which parentheses word matches the minimal curvature curve at <1>? (<2>)",
          "Identify which color is for the curve with the smallest curvature at <1> (<2>)."
        ],
        "type3": [
          "For example, if it's purple, answer: Answer : purple.",
          "Suppose purple is the curve with the smallest curvature at <1>. Then 'Answer : purple'.",
          "If the purple curve shows minimal curvature at <1>, respond 'Answer : purple'.",
          "When purple has the least curvature at <1>, your answer is 'Answer : purple'.",
          "Imagine the purple curve is the one with the smallest curvature at <1>. Then pick 'Answer : purple'."
        ],
        "type4": [
          "You must pick your answer from <3>.",
          "Select the correct color in <3>.",
          "The valid choice is in <3>.",
          "Please choose from <3>.",
          "Your answer must come from <3>."
        ]
      }
    }
  }
}


def generate_conversation(diagram, long=False):
    conversation_list = []
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
    return conversation_list