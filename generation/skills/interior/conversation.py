from .rules import *
import random

conversation = {
  "conversation_long": {
    "interior1": {
      "QA": [
        [
          "Find all the points that lie inside shape <1>.",
          "The points inside shape <1> are <4>."
        ],
        [
          "Which points are located within shape <1>?",
          "Those points within shape <1> are <4>."
        ],
        [
          "Identify every point that resides in shape <1>.",
          "Shape <1> contains the following points: <4>."
        ],
        [
          "Please list all points that are contained by shape <1>.",
          "All points contained by shape <1> are <4>."
        ],
        [
          "Determine the set of points found inside shape <1>.",
          "The set of points inside shape <1> is <4>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the points <3>, those inside shape <1> are <2>.",
            "Among the points <3>, those inside shape <1> are <4>."
          ],
          [
            "Choose the correct term from the parentheses. Of the points <3>, the ones inside shape <1> are <2>.",
            "Of the points <3>, the ones inside shape <1> are <4>."
          ],
          [
            "Pick a word in parentheses to finish the sentence. The points <3> that lie within shape <1> are <2>.",
            "The points <3> that lie within shape <1> are <4>."
          ],
          [
            "From the options in parentheses, select the correct one. Points <3> inside shape <1> correspond to <2>.",
            "Points <3> inside shape <1> correspond to <4>."
          ],
          [
            "Complete the sentence by choosing a term in parentheses. Among <3>, the points located in shape <1> are <2>.",
            "Among <3>, the points located in shape <1> are <4>."
          ]
        ],
        "type3": [
          "For example, if points X, Y, and Z are inside shape <1>, you should answer \"X, Y, Z\".",
          "As an illustration, if X, Y, Z lie within shape <1>, your answer should be \"X, Y, Z\".",
          "For instance, if the points inside shape <1> are X, Y, and Z, then the answer must be \"X, Y, Z\".",
          "If shape <1> contains points X, Y, Z, then you should respond with \"X, Y, Z\".",
          "An example: if X, Y, Z are the points inside shape <1>, answer with \"X, Y, Z\"."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "You should select your answer from <3>.",
          "Choose the correct points from <3>.",
          "Make your selection from <3>."
        ]
      }
    },
    "interior2": {
      "QA": [
        [
          "Find all the points that lie outside shape <1>.",
          "The points outside shape <1> are <4>."
        ],
        [
          "Which points are located outside shape <1>?",
          "Those points outside shape <1> are <4>."
        ],
        [
          "Identify every point that resides outside shape <1>.",
          "Shape <1> has the following points outside of it: <4>."
        ],
        [
          "Please list all points that are not contained by shape <1>.",
          "All points outside shape <1> are <4>."
        ],
        [
          "Determine the set of points found outside shape <1>.",
          "The set of points outside shape <1> is <4>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the points <3>, those outside shape <1> are <2>.",
            "Among the points <3>, those outside shape <1> are <4>."
          ],
          [
            "Choose the correct term from the parentheses. Of the points <3>, the ones outside shape <1> are <2>.",
            "Of the points <3>, the ones outside shape <1> are <4>."
          ],
          [
            "Pick a word in parentheses to finish the sentence. The points <3> that lie outside shape <1> are <2>.",
            "The points <3> that lie outside shape <1> are <4>."
          ],
          [
            "From the options in parentheses, select the correct one. Points <3> outside shape <1> correspond to <2>.",
            "Points <3> outside shape <1> correspond to <4>."
          ],
          [
            "Complete the sentence by choosing a term in parentheses. Among <3>, the points located outside shape <1> are <2>.",
            "Among <3>, the points located outside shape <1> are <4>."
          ]
        ],
        "type3": [
          "For example, if points X, Y, and Z are outside shape <1>, you should answer \"X, Y, Z\".",
          "As an illustration, if X, Y, Z lie outside shape <1>, your answer should be \"X, Y, Z\".",
          "For instance, if the points outside shape <1> are X, Y, and Z, then the answer must be \"X, Y, Z\".",
          "If shape <1> has points X, Y, Z outside it, then you should respond with \"X, Y, Z\".",
          "An example: if X, Y, Z are the points outside shape <1>, answer with \"X, Y, Z\"."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "You should select your answer from <3>.",
          "Choose the correct points from <3>.",
          "Make your selection from <3>."
        ]
      }
    },
    "interior3": {
      "QA": [
        [
          "Find all points inside shape <1>, and use their colors as your answer.",
          "The colors of the points inside shape <1> are <4>."
        ],
        [
          "Which points lie within shape <1>? Provide your response in terms of their colors.",
          "The point colors inside shape <1> are <4>."
        ],
        [
          "Identify every point inside shape <1>, describing them by color.",
          "Inside shape <1>, the point colors are <4>."
        ],
        [
          "List the points in shape <1> by their color.",
          "The set of colors for points within shape <1> is <4>."
        ],
        [
          "Determine the colors of all points located in shape <1>.",
          "All points in shape <1> have colors <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the points with color <3>, the ones inside shape <1> have the color <2>.",
            "Among the points with color <3>, those inside shape <1> have the color <4>."
          ],
          [
            "Choose the correct term from the parentheses. The points colored <3> that lie in shape <1> have the color <2>.",
            "The points colored <3> in shape <1> have the color <4>."
          ],
          [
            "Pick a word in parentheses to finish the sentence. If a point has color <3> and is inside shape <1>, its color is <2>.",
            "If a point has color <3> and is inside shape <1>, its color is <4>."
          ],
          [
            "From the options in parentheses, select the correct one. Points of color <3> inside shape <1> correspond to <2>.",
            "Points of color <3> inside shape <1> correspond to <4>."
          ],
          [
            "Complete the sentence by choosing a term in parentheses. The color of points <3> that are within shape <1> is <2>.",
            "The color of points <3> within shape <1> is <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct color from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior4": {
      "QA": [
        [
          "Find all points outside shape <1>, and use their colors as your answer.",
          "The colors of the points outside shape <1> are <4>."
        ],
        [
          "Which points lie outside shape <1>? Provide your response in terms of their colors.",
          "The point colors outside shape <1> are <4>."
        ],
        [
          "Identify every point outside shape <1>, describing them by color.",
          "Outside shape <1>, the point colors are <4>."
        ],
        [
          "List the points outside shape <1> by their color.",
          "The set of colors for points beyond shape <1> is <4>."
        ],
        [
          "Determine the colors of all points that are located outside shape <1>.",
          "All points outside shape <1> have colors <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the points with color <3>, the ones outside shape <1> have the color <2>.",
            "Among the points with color <3>, those outside shape <1> have the color <4>."
          ],
          [
            "Choose the correct term from the parentheses. The points colored <3> that lie outside shape <1> have the color <2>.",
            "The points colored <3> outside shape <1> have the color <4>."
          ],
          [
            "Pick a word in parentheses to finish the sentence. If a point has color <3> and is outside shape <1>, its color is <2>.",
            "If a point has color <3> and is outside shape <1>, its color is <4>."
          ],
          [
            "From the options in parentheses, select the correct one. Points of color <3> outside shape <1> correspond to <2>.",
            "Points of color <3> outside shape <1> correspond to <4>."
          ],
          [
            "Complete the sentence by choosing a term in parentheses. The color of points <3> that are outside shape <1> is <2>.",
            "The color of points <3> outside shape <1> is <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct color from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior5": {
      "QA": [
        [
          "Find all shapes that lie inside shape <1>.",
          "The shapes inside shape <1> are <4>."
        ],
        [
          "Which shapes are located within shape <1>?",
          "Those shapes within shape <1> are <4>."
        ],
        [
          "Identify every shape that resides in shape <1>.",
          "Shape <1> contains the following shapes: <4>."
        ],
        [
          "Please list all shapes that are contained by shape <1>.",
          "All shapes contained by shape <1> are <4>."
        ],
        [
          "Determine the set of shapes found inside shape <1>.",
          "The set of shapes inside shape <1> is <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the shapes <3>, those inside shape <1> are <2>.",
            "Among the shapes <3>, those inside shape <1> are <4>."
          ],
          [
            "Choose the correct term from the parentheses. Of the shapes <3>, the ones inside shape <1> are <2>.",
            "Of the shapes <3>, the ones inside shape <1> are <4>."
          ],
          [
            "Pick a word in parentheses to finish the sentence. The shapes <3> that lie within shape <1> are <2>.",
            "The shapes <3> that lie within shape <1> are <4>."
          ],
          [
            "From the options in parentheses, select the correct one. Shapes <3> inside shape <1> correspond to <2>.",
            "Shapes <3> inside shape <1> correspond to <4>."
          ],
          [
            "Complete the sentence by choosing a term in parentheses. Among <3>, the shapes located in shape <1> are <2>.",
            "Among <3>, the shapes located in shape <1> are <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct shapes from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior6": {
      "QA": [
        [
          "Find all shapes that lie outside shape <1>.",
          "The shapes outside shape <1> are <4>."
        ],
        [
          "Which shapes are located beyond shape <1>?",
          "Those shapes outside shape <1> are <4>."
        ],
        [
          "Identify every shape that resides outside shape <1>.",
          "Shape <1> has the following shapes outside of it: <4>."
        ],
        [
          "Please list all shapes not contained by shape <1>.",
          "All shapes outside shape <1> are <4>."
        ],
        [
          "Determine the set of shapes found outside shape <1>.",
          "The set of shapes outside shape <1> is <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the shapes <3>, those outside shape <1> are <2>.",
            "Among the shapes <3>, those outside shape <1> are <4>."
          ],
          [
            "Choose the correct term from the parentheses. Of the shapes <3>, the ones outside shape <1> are <2>.",
            "Of the shapes <3>, the ones outside shape <1> are <4>."
          ],
          [
            "Pick a word in parentheses to finish the sentence. The shapes <3> that lie outside shape <1> are <2>.",
            "The shapes <3> that lie outside shape <1> are <4>."
          ],
          [
            "From the options in parentheses, select the correct one. Shapes <3> outside shape <1> correspond to <2>.",
            "Shapes <3> outside shape <1> correspond to <4>."
          ],
          [
            "Complete the sentence by choosing a term in parentheses. Among <3>, the shapes located outside shape <1> are <2>.",
            "Among <3>, the shapes located outside shape <1> are <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct shapes from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior7": {
      "QA": [
        [
          "Find all shapes inside shape <1>, and use their colors as your answer.",
          "The colors of the shapes inside shape <1> are <4>."
        ],
        [
          "Which shapes lie within shape <1>? Provide your response in terms of their colors.",
          "The shape colors inside shape <1> are <4>."
        ],
        [
          "Identify every shape inside shape <1>, describing them by color.",
          "Inside shape <1>, the shapes have colors <4>."
        ],
        [
          "List the shapes in shape <1> by their color.",
          "The set of colors for shapes within shape <1> is <4>."
        ],
        [
          "Determine the colors of all shapes that are located in shape <1>.",
          "All shapes in shape <1> have colors <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the shapes <3>, the ones inside shape <1> have the color <2>.",
            "Among the shapes <3>, those inside shape <1> have the color <4>."
          ],
          [
            "Choose the correct term from the parentheses. The shapes <3> lying within shape <1> have the color <2>.",
            "The shapes <3> lying within shape <1> have the color <4>."
          ],
          [
            "Pick a word in parentheses to finish the sentence. If a shape is in <1> and is among <3>, its color is <2>.",
            "If a shape is in <1> and is among <3>, its color is <4>."
          ],
          [
            "From the options in parentheses, select the correct one. Shapes <3> inside <1> correspond to the color <2>.",
            "Shapes <3> inside <1> correspond to the color <4>."
          ],
          [
            "Complete the sentence by choosing a term in parentheses. The color of shapes <3> within shape <1> is <2>.",
            "The color of shapes <3> within shape <1> is <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct colors from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior8": {
      "QA": [
        [
          "Find all shapes outside shape <1>, and use their colors as your answer.",
          "The colors of the shapes outside shape <1> are <4>."
        ],
        [
          "Which shapes lie outside shape <1>? Provide your response in terms of their colors.",
          "The shape colors outside shape <1> are <4>."
        ],
        [
          "Identify every shape outside shape <1>, describing them by color.",
          "Outside shape <1>, the shapes have colors <4>."
        ],
        [
          "List the shapes outside shape <1> by their color.",
          "The set of colors for shapes beyond shape <1> is <4>."
        ],
        [
          "Determine the colors of all shapes that are located outside shape <1>.",
          "All shapes outside shape <1> have colors <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the shapes <3>, the ones outside shape <1> have the color <2>.",
            "Among the shapes <3>, those outside shape <1> have the color <4>."
          ],
          [
            "Choose the correct term from the parentheses. The shapes <3> lying outside shape <1> have the color <2>.",
            "The shapes <3> lying outside shape <1> have the color <4>."
          ],
          [
            "Pick a word in parentheses to finish the sentence. If a shape is outside <1> and is among <3>, its color is <2>.",
            "If a shape is outside <1> and is among <3>, its color is <4>."
          ],
          [
            "From the options in parentheses, select the correct one. Shapes <3> outside <1> correspond to the color <2>.",
            "Shapes <3> outside <1> correspond to the color <4>."
          ],
          [
            "Complete the sentence by choosing a term in parentheses. The color of shapes <3> beyond shape <1> is <2>.",
            "The color of shapes <3> beyond shape <1> is <4>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct colors from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior9": {
      "QA": [
        [
          "Among the points in the figure, which ones lie within <1>?",
          "Points <4> are inside <1>."
        ],
        [
          "Find all points that are inside <1> from the given figure.",
          "The points that lie within <1> are <4>."
        ],
        [
          "Identify the points that reside in <1> based on the figure.",
          "Inside <1> you can find points <4>."
        ],
        [
          "Which points does the figure show as being contained in <1>?",
          "Those points inside <1> are <4>."
        ],
        [
          "Determine the set of points located within <1> according to the figure.",
          "The set of points inside <1> is <4>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The points <2> are inside <1>.",
            "Points <4> are inside <1>."
          ],
          [
            "Pick the correct term in parentheses. It states that <2> lie within <1>.",
            "We find that <4> lie within <1>."
          ],
          [
            "Choose from the parentheses to finalize the sentence. According to the figure, <2> reside in <1>.",
            "According to the figure, <4> reside in <1>."
          ],
          [
            "From the parentheses provided, select the best word. We see that <2> exist inside <1>.",
            "We observe <4> existing inside <1>."
          ],
          [
            "Complete the sentence with the proper choice in parentheses. The figure shows <2> in <1>.",
            "The figure shows <4> in <1>."
          ]
        ],
        "type3": [
          "For instance, if points A and B are inside <1>, the answer is \"A, B\".",
          "As an example, if <1> contains points A, B, answer with \"A, B\".",
          "For example, if the points within <1> are A and B, write \"A, B\".",
          "If points A, B are found in <1>, your answer should be \"A, B\".",
          "E.g., if A, B lie inside <1>, you must respond with \"A, B\"."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Pick the correct points from <3>.",
          "Select your answer from <3>.",
          "Please choose from <3> for the answer.",
          "You must choose from <3>."
        ]
      }
    },
    "interior10": {
      "QA": [
        [
          "Among the points in the figure, which ones lie within <1>? Report all their colors.",
          "Points with color <4> are inside <1>."
        ],
        [
          "Find all points that are inside <1> from the figure, and give their colors.",
          "The colors of the points that lie within <1> are <4>."
        ],
        [
          "Identify the points in <1> by their color, based on the figure.",
          "Within <1>, the point colors are <4>."
        ],
        [
          "Which points does the figure show as being contained in <1>? Provide the colors.",
          "The points inside <1> have colors <4>."
        ],
        [
          "Determine the colors of the points located within <1> according to the figure.",
          "The set of point colors inside <1> is <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The points with color <2> are inside <1>.",
            "The points with color <4> are inside <1>."
          ],
          [
            "Choose from the parentheses to finish the sentence. Points of color <2> lie within <1>.",
            "Points of color <4> lie within <1>."
          ],
          [
            "Pick the correct term in parentheses. According to the figure, color <2> is found inside <1>.",
            "According to the figure, color <4> is found inside <1>."
          ],
          [
            "From the parentheses provided, select the correct color. We see color <2> inside <1>.",
            "We see color <4> inside <1>."
          ],
          [
            "Complete the sentence by selecting the right word in parentheses. The figure shows that color <2> is in <1>.",
            "The figure shows that color <4> is in <1>."
          ]
        ],
        "type3": [
          "For instance, if red and blue points are inside <1>, the answer should be \"red, blue\". The answer must be chosen from <3>.",
          "If <1> contains points of colors red and blue, reply with \"red, blue\". Remember to choose from <3>.",
          "For example, if the colors of points within <1> are red and blue, you should write \"red, blue\". Select from <3>.",
          "If inside <1> there are points colored red and blue, answer \"red, blue\". Your choices come from <3>.",
          "As an example, if red and blue lie in <1>, the correct response is \"red, blue\". Pick from <3>."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Pick the correct colors from <3>.",
          "Select your answer from <3>.",
          "Please choose from <3> for the answer.",
          "You must choose from <3>."
        ]
      }
    },
    "interior11": {
      "QA": [
        [
          "Which shapes in the figure lie within <1>?",
          "Shapes <4> are inside <1>."
        ],
        [
          "Find all shapes that are inside <1> according to the figure.",
          "The shapes that lie within <1> are <4>."
        ],
        [
          "Identify the shapes residing in <1> based on the diagram.",
          "Within <1>, the shapes are <4>."
        ],
        [
          "Which shapes does the figure show as being contained in <1>?",
          "Those shapes inside <1> are <4>."
        ],
        [
          "Determine the set of shapes located within <1> according to the figure.",
          "The set of shapes in <1> is <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The shapes <2> are in <1>.",
            "Shapes <4> are in <1>."
          ],
          [
            "Choose from the parentheses to finish the sentence. We see shapes <2> within <1>.",
            "We see shapes <4> within <1>."
          ],
          [
            "Pick the correct term in parentheses. According to the figure, shapes <2> lie in <1>.",
            "According to the figure, shapes <4> lie in <1>."
          ],
          [
            "From the parentheses provided, select the proper word. The diagram shows <2> in <1>.",
            "The diagram shows <4> in <1>."
          ],
          [
            "Complete the sentence by selecting the right word in parentheses. The shapes <2> appear in <1>.",
            "The shapes <4> appear in <1>."
          ]
        ],
        "type3": [
          "For instance, if shapes A and B are inside <1>, the answer is \"A, B\". The answer must be chosen from <3>.",
          "If <1> contains shapes A, B, answer with \"A, B\". Choose from <3>.",
          "For example, if the shapes within <1> are A and B, write \"A, B\". Remember to select from <3>.",
          "If shapes A, B are found in <1>, your answer should be \"A, B\". Pick from <3>.",
          "E.g., if A, B lie inside <1>, respond with \"A, B\". Choose from <3>."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Pick the correct shapes from <3>.",
          "Select your answer from <3>.",
          "Please choose from <3> for the answer.",
          "You must choose from <3>."
        ]
      }
    },
    "interior12": {
      "QA": [
        [
          "Which shapes in the figure lie within <1>? Provide all their colors.",
          "Shapes with color <4> are inside <1>."
        ],
        [
          "Find all shapes that are inside <1> according to the figure, and give their colors.",
          "The colors of the shapes that lie within <1> are <4>."
        ],
        [
          "Identify the shapes residing in <1>, describing them by color.",
          "Within <1>, the shapes have colors <4>."
        ],
        [
          "Which shapes does the figure show as being in <1>? Provide the colors.",
          "Those shapes in <1> have colors <4>."
        ],
        [
          "Determine the colors of all shapes located within <1> according to the figure.",
          "The set of shape colors in <1> is <4>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The shapes with color <2> are in <1>.",
            "The shapes with color <4> are in <1>."
          ],
          [
            "Choose from the parentheses to finish the sentence. Shapes of color <2> lie in <1>.",
            "Shapes of color <4> lie in <1>."
          ],
          [
            "Pick the correct term in parentheses. According to the figure, color <2> is found in <1>.",
            "According to the figure, color <4> is found in <1>."
          ],
          [
            "From the parentheses provided, select the proper color. We see color <2> in <1>.",
            "We see color <4> in <1>."
          ],
          [
            "Complete the sentence by selecting the right word in parentheses. The diagram shows shapes of color <2> in <1>.",
            "The diagram shows shapes of color <4> in <1>."
          ]
        ],
        "type3": [
          "For instance, if red and blue shapes are inside <1>, answer \"red, blue\". The answer must be chosen from <3>.",
          "If <1> contains shapes of colors red and blue, you should reply \"red, blue\". Choose from <3>.",
          "For example, if shapes within <1> are colored red and blue, then your answer is \"red, blue\". Select from <3>.",
          "If shapes in <1> have colors red and blue, provide the answer \"red, blue\". Remember to pick from <3>.",
          "As an example, if shapes in <1> are red and blue, respond with \"red, blue\". Choose from <3>."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Pick the correct colors from <3>.",
          "Select your answer from <3>.",
          "Please choose from <3> for the answer.",
          "You must choose from <3>."
        ]
      }
    }
  },
  "conversation_short": {
    "interior1": {
      "QA": [
        [
          "Which points lie inside shape <1>?",
          "<4>"
        ],
        [
          "Find the points contained by shape <1>.",
          "<4>"
        ],
        [
          "Identify all points in shape <1>.",
          "<4>"
        ],
        [
          "List the points within shape <1>.",
          "<4>"
        ],
        [
          "Which points are located in shape <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. Among the points <3>, those inside shape <1> are <2>.",
          "Choose the correct term from the parentheses. Of the points <3>, the ones inside shape <1> are <2>.",
          "Pick a word in parentheses to finish the sentence. The points <3> that lie within shape <1> are <2>.",
          "From the options in parentheses, select the correct one. Points <3> inside shape <1> correspond to <2>.",
          "Complete the sentence by choosing a term in parentheses. Among <3>, the points located in shape <1> are <2>."
        ],
        "type3": [
          "For example, if points X, Y, Z are inside shape <1>, you should answer \"X, Y, Z\".",
          "As an illustration, if X, Y, Z lie within shape <1>, your answer should be \"X, Y, Z\".",
          "For instance, if the points inside shape <1> are X, Y, and Z, then the answer must be \"X, Y, Z\".",
          "If shape <1> contains points X, Y, Z, then you should respond with \"X, Y, Z\".",
          "An example: if X, Y, Z are the points inside shape <1>, answer with \"X, Y, Z\"."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "You should select your answer from <3>.",
          "Choose the correct points from <3>.",
          "Make your selection from <3>."
        ]
      }
    },
    "interior2": {
      "QA": [
        [
          "Which points lie outside shape <1>?",
          "<4>"
        ],
        [
          "Find the points not contained by shape <1>.",
          "<4>"
        ],
        [
          "Identify all points beyond shape <1>.",
          "<4>"
        ],
        [
          "List the points that reside outside shape <1>.",
          "<4>"
        ],
        [
          "Which points can be found outside shape <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. Among the points <3>, those outside shape <1> are <2>.",
          "Choose the correct term from the parentheses. Of the points <3>, the ones outside shape <1> are <2>.",
          "Pick a word in parentheses to finish the sentence. The points <3> that lie outside shape <1> are <2>.",
          "From the options in parentheses, select the correct one. Points <3> outside shape <1> correspond to <2>.",
          "Complete the sentence by choosing a term in parentheses. Among <3>, the points located outside shape <1> are <2>."
        ],
        "type3": [
          "For example, if points X, Y, and Z are outside shape <1>, you should answer \"X, Y, Z\".",
          "As an illustration, if X, Y, Z lie outside shape <1>, your answer should be \"X, Y, Z\".",
          "For instance, if the points outside shape <1> are X, Y, and Z, then the answer must be \"X, Y, Z\".",
          "If shape <1> has points X, Y, Z outside it, then you should respond with \"X, Y, Z\".",
          "An example: if X, Y, Z are the points outside shape <1>, answer with \"X, Y, Z\"."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "You should select your answer from <3>.",
          "Choose the correct points from <3>.",
          "Make your selection from <3>."
        ]
      }
    },
    "interior3": {
      "QA": [
        [
          "Which points lie inside shape <1>? Answer with their colors.",
          "<4>"
        ],
        [
          "Find the points inside shape <1> by color.",
          "<4>"
        ],
        [
          "List the colors of all points within shape <1>.",
          "<4>"
        ],
        [
          "Identify the colors of the points in shape <1>.",
          "<4>"
        ],
        [
          "What are the colors of points contained by shape <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. Among the points with color <3>, those inside shape <1> have the color <2>.",
          "Choose the correct term from the parentheses. The points colored <3> that lie in shape <1> have the color <2>.",
          "Pick a word in parentheses. If a point has color <3> and is inside shape <1>, its color is <2>.",
          "From the options in parentheses, select the correct one. Points of color <3> inside shape <1> correspond to <2>.",
          "Complete the sentence by choosing a term in parentheses. The color of points <3> within shape <1> is <2>."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct color from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior4": {
      "QA": [
        [
          "Which points lie outside shape <1>? Answer with their colors.",
          "<4>"
        ],
        [
          "Find the points outside shape <1> by color.",
          "<4>"
        ],
        [
          "List the colors of all points beyond shape <1>.",
          "<4>"
        ],
        [
          "Identify the colors of the points not contained by shape <1>.",
          "<4>"
        ],
        [
          "What are the colors of points located outside shape <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. Among the points with color <3>, those outside shape <1> have the color <2>.",
          "Choose the correct term from the parentheses. The points colored <3> outside shape <1> have the color <2>.",
          "Pick a word in parentheses. If a point has color <3> and is outside shape <1>, its color is <2>.",
          "From the options in parentheses, select the correct one. Points of color <3> outside shape <1> correspond to <2>.",
          "Complete the sentence by choosing a term in parentheses. The color of points <3> outside shape <1> is <2>."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct color from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior5": {
      "QA": [
        [
          "Which shapes are inside shape <1>?",
          "<4>"
        ],
        [
          "Find the shapes contained by shape <1>.",
          "<4>"
        ],
        [
          "List all shapes within shape <1>.",
          "<4>"
        ],
        [
          "Identify the shapes that reside in shape <1>.",
          "<4>"
        ],
        [
          "What shapes can be found inside shape <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. Among the shapes <3>, those inside shape <1> are <2>.",
          "Choose the correct term from the parentheses. Of the shapes <3>, the ones inside shape <1> are <2>.",
          "Pick a word in parentheses to finish the sentence. The shapes <3> that lie within shape <1> are <2>.",
          "From the options in parentheses, select the correct one. Shapes <3> inside shape <1> correspond to <2>.",
          "Complete the sentence by choosing a term in parentheses. Among <3>, the shapes located in shape <1> are <2>."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct shapes from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior6": {
      "QA": [
        [
          "Which shapes are outside shape <1>?",
          "<4>"
        ],
        [
          "Find the shapes not contained by shape <1>.",
          "<4>"
        ],
        [
          "List all shapes beyond shape <1>.",
          "<4>"
        ],
        [
          "Identify the shapes that reside outside shape <1>.",
          "<4>"
        ],
        [
          "What shapes can be found outside shape <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. Among the shapes <3>, those outside shape <1> are <2>.",
          "Choose the correct term from the parentheses. Of the shapes <3>, the ones outside shape <1> are <2>.",
          "Pick a word in parentheses to finish the sentence. The shapes <3> that lie outside shape <1> are <2>.",
          "From the options in parentheses, select the correct one. Shapes <3> outside shape <1> correspond to <2>.",
          "Complete the sentence by choosing a term in parentheses. Among <3>, the shapes located outside shape <1> are <2>."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct shapes from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior7": {
      "QA": [
        [
          "Which shapes are inside shape <1>? Answer with their colors.",
          "<4>"
        ],
        [
          "Find the shapes in shape <1> by color.",
          "<4>"
        ],
        [
          "List the colors of all shapes within shape <1>.",
          "<4>"
        ],
        [
          "Identify the colors of the shapes that lie in shape <1>.",
          "<4>"
        ],
        [
          "What are the colors of shapes contained by shape <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. Among the shapes <3>, the ones inside shape <1> have the color <2>.",
          "Choose the correct term from the parentheses. The shapes <3> lying within shape <1> have the color <2>.",
          "Pick a word in parentheses. If a shape is in <1> and is among <3>, its color is <2>.",
          "From the options in parentheses, select the correct one. Shapes <3> inside <1> correspond to the color <2>.",
          "Complete the sentence by choosing a term in parentheses. The color of shapes <3> within shape <1> is <2>."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct colors from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior8": {
      "QA": [
        [
          "Which shapes are outside shape <1>? Answer with their colors.",
          "<4>"
        ],
        [
          "Find the shapes outside shape <1> by color.",
          "<4>"
        ],
        [
          "List the colors of all shapes beyond shape <1>.",
          "<4>"
        ],
        [
          "Identify the colors of the shapes not contained by shape <1>.",
          "<4>"
        ],
        [
          "What are the colors of shapes located outside shape <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. Among the shapes <3>, the ones outside shape <1> have the color <2>.",
          "Choose the correct term from the parentheses. The shapes <3> lying outside shape <1> have the color <2>.",
          "Pick a word in parentheses. If a shape is outside <1> and is among <3>, its color is <2>.",
          "From the options in parentheses, select the correct one. Shapes <3> outside <1> correspond to the color <2>.",
          "Complete the sentence by choosing a term in parentheses. The color of shapes <3> beyond shape <1> is <2>."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Please pick from <3> for the answer.",
          "Select your answer from <3>.",
          "Choose the correct colors from <3>.",
          "You must select from <3>."
        ]
      }
    },
    "interior9": {
      "QA": [
        [
          "Which points lie inside <1>?",
          "<4>"
        ],
        [
          "Find all points that are in <1>.",
          "<4>"
        ],
        [
          "Identify the points located within <1>.",
          "<4>"
        ],
        [
          "List the points shown inside <1> in the figure.",
          "<4>"
        ],
        [
          "Which points does the figure place in <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. The points <2> are inside <1>.",
          "Pick the correct term in parentheses. It states that <2> lie within <1>.",
          "Choose from the parentheses to finalize the sentence. According to the figure, <2> reside in <1>.",
          "From the parentheses provided, select the best word. We see that <2> exist inside <1>.",
          "Complete the sentence with the proper choice in parentheses. The figure shows <2> in <1>."
        ],
        "type3": [
          "For instance, if points A and B are inside <1>, the answer is \"A, B\".",
          "As an example, if <1> contains points A, B, answer with \"A, B\".",
          "For example, if the points within <1> are A and B, write \"A, B\".",
          "If points A, B are found in <1>, your answer should be \"A, B\".",
          "E.g., if A, B lie inside <1>, you must respond with \"A, B\"."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Pick the correct points from <3>.",
          "Select your answer from <3>.",
          "Please choose from <3> for the answer.",
          "You must choose from <3>."
        ]
      }
    },
    "interior10": {
      "QA": [
        [
          "Which points lie inside <1>? Report their colors.",
          "<4>"
        ],
        [
          "Find the points in <1> and provide their colors.",
          "<4>"
        ],
        [
          "List the colors of the points that reside within <1>.",
          "<4>"
        ],
        [
          "Identify the colors of the points in <1> according to the figure.",
          "<4>"
        ],
        [
          "What colors do the points inside <1> have?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. The points with color <2> are inside <1>.",
          "Choose from the parentheses to finish the sentence. Points of color <2> lie within <1>.",
          "Pick the correct term in parentheses. According to the figure, color <2> is found inside <1>.",
          "From the parentheses provided, select the correct color. We see color <2> inside <1>.",
          "Complete the sentence by selecting the right word in parentheses. The figure shows that color <2> is in <1>."
        ],
        "type3": [
          "For instance, if red and blue points are inside <1>, the answer should be \"red, blue\". The answer must be chosen from <3>.",
          "If <1> contains points of colors red and blue, reply with \"red, blue\". Remember to choose from <3>.",
          "For example, if the colors of points within <1> are red and blue, you should write \"red, blue\". Select from <3>.",
          "If inside <1> there are points colored red and blue, answer \"red, blue\". Your choices come from <3>.",
          "As an example, if red and blue lie in <1>, the correct response is \"red, blue\". Pick from <3>."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Pick the correct colors from <3>.",
          "Select your answer from <3>.",
          "Please choose from <3> for the answer.",
          "You must choose from <3>."
        ]
      }
    },
    "interior11": {
      "QA": [
        [
          "Which shapes lie within <1>?",
          "<4>"
        ],
        [
          "Find all shapes that are in <1>.",
          "<4>"
        ],
        [
          "Identify the shapes residing in <1>.",
          "<4>"
        ],
        [
          "List the shapes shown inside <1> in the figure.",
          "<4>"
        ],
        [
          "Which shapes does the figure place in <1>?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. The shapes <2> are in <1>.",
          "Choose from the parentheses to finish the sentence. We see shapes <2> within <1>.",
          "Pick the correct term in parentheses. According to the figure, shapes <2> lie in <1>.",
          "From the parentheses provided, select the proper word. The diagram shows <2> in <1>.",
          "Complete the sentence by selecting the right word in parentheses. The shapes <2> appear in <1>."
        ],
        "type3": [
          "For instance, if shapes A and B are inside <1>, the answer is \"A, B\". The answer must be chosen from <3>.",
          "If <1> contains shapes A, B, answer with \"A, B\". Choose from <3>.",
          "For example, if the shapes within <1> are A and B, write \"A, B\". Remember to select from <3>.",
          "If shapes A, B are found in <1>, your answer should be \"A, B\". Pick from <3>.",
          "E.g., if A, B lie inside <1>, respond with \"A, B\". Choose from <3>."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Pick the correct shapes from <3>.",
          "Select your answer from <3>.",
          "Please choose from <3> for the answer.",
          "You must choose from <3>."
        ]
      }
    },
    "interior12": {
      "QA": [
        [
          "Which shapes lie within <1>? Provide their colors.",
          "<4>"
        ],
        [
          "Find all shapes in <1> and give their colors.",
          "<4>"
        ],
        [
          "List the colors of the shapes that reside within <1>.",
          "<4>"
        ],
        [
          "Identify the shapes in <1>, describing them by color.",
          "<4>"
        ],
        [
          "What colors do the shapes inside <1> have?",
          "<4>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. The shapes with color <2> are in <1>.",
          "Choose from the parentheses to finish the sentence. Shapes of color <2> lie in <1>.",
          "Pick the correct term in parentheses. According to the figure, color <2> is found in <1>.",
          "From the parentheses provided, select the proper color. We see color <2> in <1>.",
          "Complete the sentence by selecting the right word in parentheses. The diagram shows shapes of color <2> in <1>."
        ],
        "type3": [
          "For instance, if red and blue shapes are inside <1>, answer \"red, blue\". The answer must be chosen from <3>.",
          "If <1> contains shapes of colors red and blue, you should reply \"red, blue\". Choose from <3>.",
          "For example, if shapes within <1> are colored red and blue, then your answer is \"red, blue\". Select from <3>.",
          "If shapes in <1> have colors red and blue, provide the answer \"red, blue\". Remember to pick from <3>.",
          "As an example, if shapes in <1> are red and blue, respond with \"red, blue\". Choose from <3>."
        ],
        "type4": [
          "The answer must be chosen from <3>.",
          "Pick the correct colors from <3>.",
          "Select your answer from <3>.",
          "Please choose from <3> for the answer.",
          "You must choose from <3>."
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
            if entity[1][i] == "Nothing":
                a = "Nothing is inside that area."
            else:
                a = a.replace(f"<{i+1}>", entity[1][i])
        conversation_list.append((q, a))
    return conversation_list