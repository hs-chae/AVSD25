from .rules import *
import random

conversation = {
  "conversation_long": {
    "convexity1": {
      "QA": [
        [
          "Is the given shape concave or convex?",
          "The given shape is <2>."
        ],
        [
          "Determine whether the provided shape is concave or convex.",
          "This shape is <2>."
        ],
        [
          "Which type does the shape belong to: concave or convex?",
          "The shape belongs to <2>."
        ],
        [
          "Identify whether the shape is concave or convex.",
          "The shape is <2>."
        ],
        [
          "Please specify whether the given shape is concave or convex.",
          "It is <2>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The given shape is (convex/concave).",
            "The given shape is <2>."
          ],
          [
            "Choose the correct word from the options in parentheses to finish the statement. The shape is (convex/concave).",
            "The shape is <2>."
          ],
          [
            "Pick one of the words inside the parentheses to finalize the sentence. The shape is (convex/concave).",
            "The shape is <2>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The correct answer must be chosen from \"convex\" or \"concave\".",
          "Select your answer from \"convex\" or \"concave\".",
          "You must choose either \"convex\" or \"concave\"."
        ]
      }
    },
    "convexity2": {
      "QA": [
        [
          "Among the given shapes, which one is <2>?",
          "Among these shapes, the <2> shape is <5>."
        ],
        [
          "Identify which shape is <2> from the set of given shapes.",
          "The shape that is <2> is <5>."
        ],
        [
          "Which shape qualifies as <2> among those provided?",
          "The <2> shape among them is <5>."
        ],
        [
          "Select the shape that can be classified as <2> from the given options.",
          "The chosen <2> shape is <5>."
        ],
        [
          "Determine the shape that fits the <2> property among the listed ones.",
          "The shape fitting <2> is <5>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the given shapes, the one that is <2> is (<3>).",
            "Among the given shapes, the one that is <2> is <5>."
          ],
          [
            "Pick the correct term from the options in parentheses. The shape that is <2> is (<3>).",
            "The shape that is <2> is <5>."
          ],
          [
            "Choose from the parentheses to finish the statement. The <2> shape among the given ones is (<3>).",
            "The <2> shape among the given ones is <5>."
          ]
        ],
        "type3": [
          "For example, if the only <2> shape is Z, then your answer should be \"Z\".",
          "For instance, if Z is the unique shape that is <2>, your response should be \"Z\".",
          "As an example, if Z happens to be the sole <2> shape, the correct answer is \"Z\"."
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Please select the correct shape from <4>.",
          "Pick your answer from <4>."
        ]
      }
    },
    "convexity3": {
      "QA": [
        [
          "Which color corresponds to the shape that is <2> among the given figures?",
          "The color of the shape that is <2> is <5>."
        ],
        [
          "Identify the color of the shape categorized as <2> from the provided shapes.",
          "The shape that is <2> has the color <5>."
        ],
        [
          "Among the listed shapes, which color belongs to the <2> shape?",
          "Its color is <5>."
        ],
        [
          "What is the color of the shape that qualifies as <2> among those shown?",
          "The color is <5> for the <2> shape."
        ],
        [
          "Determine the color of the shape that is <2> from the given options.",
          "The <2> shape has the color <5>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the given shapes, the shape that is <2> has the color (<3>).",
            "Among the given shapes, the shape that is <2> has the color <5>."
          ],
          [
            "Choose from the parentheses to finish the statement. The color of the <2> shape is (<3>).",
            "The color of the <2> shape is <5>."
          ],
          [
            "Pick the correct option in parentheses to complete the sentence. The shape classified as <2> has color (<3>).",
            "The shape classified as <2> has color <5>."
          ]
        ],
        "type3": [
          "For example, if the only <2> shape's color is red, your answer should be \"red\".",
          "If the single <2> shape has the color red, then the correct response is \"red\".",
          "As an instance, if red is the unique color for the <2> shape, you should answer \"red\"."
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Please select the color from <4>.",
          "You must pick the correct color from <4>."
        ]
      }
    },
    "convexity4": {
      "QA": [
        [
          "Among the given shapes, choose all the shapes that are <2>.",
          "All shapes that are <2> among them are <5>."
        ],
        [
          "Which shapes qualify as <2> from the list provided?",
          "The <2> shapes are <5>."
        ],
        [
          "Identify every shape that is <2> among those presented.",
          "The shapes that are <2> turn out to be <5>."
        ],
        [
          "Select all the shapes that meet the <2> property from the given options.",
          "The <2> shapes from the list are <5>."
        ],
        [
          "Determine which shapes are <2> among the ones shown.",
          "Those <2> shapes are <5>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one or more words from the parentheses to complete the sentence. The shapes that are <2> among the given shapes are (<3>).",
            "The shapes that are <2> among the given shapes are <5>."
          ],
          [
            "Choose all applicable terms in parentheses. Among these shapes, the <2> shapes are (<3>).",
            "Among these shapes, the <2> shapes are <5>."
          ],
          [
            "Pick the correct words inside the parentheses to finish the statement. The <2> shapes here are (<3>).",
            "The <2> shapes here are <5>."
          ]
        ],
        "type3": [
          "For instance, if the <2> shapes are A, B, and C, your answer should be \"A, B, C\".",
          "If the shapes labeled A, B, and C are <2>, then the correct response is \"A, B, C\".",
          "As an example, if A, B, and C fulfill the <2> property, you would answer \"A, B, C\"."
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Please pick your answers from <4>.",
          "Select all applicable options from <4>."
        ]
      }
    },
    "convexity5": {
      "QA": [
        [
          "Among the given shapes, which colors belong to the shapes that are <2>?",
          "The <2> shapes have the colors <5>."
        ],
        [
          "Identify all the colors of the shapes that are <2> in the list.",
          "Their colors are <5>."
        ],
        [
          "Which colors correspond to the <2> shapes from the provided options?",
          "The colors of the <2> shapes are <5>."
        ],
        [
          "Select the colors of every shape that meets the <2> property.",
          "These <2> shapes are colored <5>."
        ],
        [
          "Determine the colors of all shapes that are <2> among those shown.",
          "They are <5> in color."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one or more words from the parentheses to complete the sentence. The colors of the <2> shapes are (<3>).",
            "The colors of the <2> shapes are <5>."
          ],
          [
            "Choose the appropriate terms in parentheses. Among the given shapes, those that are <2> have colors (<3>).",
            "Among the given shapes, those that are <2> have colors <5>."
          ],
          [
            "Pick from the parentheses to finish the sentence. The <2> shapes possess the following colors: (<3>).",
            "The <2> shapes possess the following colors: <5>."
          ]
        ],
        "type3": [
          "For example, if the <2> shapes have colors red, blue, and green, answer \"red, blue, green\".",
          "If your <2> shapes are colored red, blue, and green, then your response should be \"red, blue, green\".",
          "As an instance, when the <2> shapes are red, blue, and green, you must write \"red, blue, green\"."
        ],
        "type4": [
          "The answer must be selected from <4>.",
          "Please pick the colors from <4>.",
          "Choose your answer from <4>."
        ]
      }
    },
    "convexity6": {
      "QA": [
        [
          "Is the given function concave or convex?",
          "The given function is <2>."
        ],
        [
          "Determine whether the provided function is concave or convex.",
          "This function is <2>."
        ],
        [
          "Which type does the function belong to: concave or convex?",
          "It is <2>."
        ],
        [
          "Identify if the function is concave or convex.",
          "The function is <2>."
        ],
        [
          "Please specify whether the function is concave or convex.",
          "The function is <2>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The given function is (convex/concave).",
            "The given function is <2>."
          ],
          [
            "Choose the correct term from the parentheses. This function is (convex/concave).",
            "This function is <2>."
          ],
          [
            "Pick one of the words in parentheses to finish the statement. The function is (convex/concave).",
            "The function is <2>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be either \"convex\" or \"concave\".",
          "Please choose between \"convex\" or \"concave\".",
          "Select \"convex\" or \"concave\" as your answer."
        ]
      }
    },
    "convexity7": {
      "QA": [
        [
          "From the given function, which regions are <2>?",
          "No specific long answer was provided."
        ],
        [
          "Identify all the regions that qualify as <2> in the function.",
          "No specific long answer was given."
        ],
        [
          "Select the portion(s) of the function that is/are <2>.",
          "There is no direct long answer provided."
        ],
        [
          "Determine which regions in the function are <2>.",
          "There is no long answer associated with this question."
        ],
        [
          "Among the highlighted areas of the function, which ones exhibit <2>?",
          "A long answer was not specified."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one or more words from the parentheses to complete the sentence. The regions in the given function that are <2> are (<3>).",
            ""
          ],
          [
            "Pick the correct items in parentheses. In the function, <2> regions include (<3>).",
            ""
          ],
          [
            "Choose from the parentheses to finalize the statement. The function's <2> regions can be described as (<3>).",
            ""
          ]
        ],
        "type3": [
          "For example, if the <2> regions in the function are 1, 3, and 4, you should write \"1, 3, 4\".",
          "If 1, 3, 4 happen to be the <2> areas, then your response should be \"1, 3, 4\".",
          "As an instance, if the function's <2> regions are 1, 3, 4, answer with \"1, 3, 4\"."
        ],
        "type4": [
          "The answer must be selected from <4>.",
          "Choose the appropriate options from <4>.",
          "Pick your response from <4>."
        ]
      }
    },
    "convexity8": {
      "QA": [
        [
          "When considering the function in segments based on the marked point, which segments are <2>?",
          "If divided by the point, the segments that are <2> are <5>."
        ],
        [
          "Identify all segments that qualify as <2> when the function is partitioned by the given point.",
          "Those <2> segments are <5>."
        ],
        [
          "Which intervals are <2> if the function is split at the marked point?",
          "The <2> intervals are <5>."
        ],
        [
          "Determine the <2> segments by dividing the function at the specified point.",
          "<5> represents the <2> segments."
        ],
        [
          "Among the segments created by splitting the function at the given point, which are <2>?",
          "They are <5>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one or more words from the parentheses to complete the sentence. If the function is divided at the marked point, the <2> segments are (<3>).",
            "If the function is divided at the marked point, the <2> segments are <5>."
          ],
          [
            "Pick all applicable terms in parentheses. The function's <2> intervals, based on the point, are (<3>).",
            "The function's <2> intervals are <5>."
          ],
          [
            "Choose from the parentheses to finalize the statement. After splitting by the point, the <2> segments become (<3>).",
            "After splitting by the point, the <2> segments become <5>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Select your answer from <4>.",
          "Pick the correct segments from <4>."
        ]
      }
    },
    "convexity9": {
      "QA": [
        [
          "Is the given lens concave or convex?",
          "The given lens is <2>."
        ],
        [
          "Determine whether the provided lens is concave or convex.",
          "This lens is <2>."
        ],
        [
          "Which type does the lens belong to: concave or convex?",
          "It is <2>."
        ],
        [
          "Identify if the lens is concave or convex.",
          "The lens is <2>."
        ],
        [
          "Please specify whether the lens is concave or convex.",
          "The lens is <2>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. The given lens is (convex/concave).",
            "The given lens is <2>."
          ],
          [
            "Choose the correct term in parentheses. This lens is (convex/concave).",
            "This lens is <2>."
          ],
          [
            "Pick one word from the parentheses to finish the statement. The lens is (convex/concave).",
            "The lens is <2>."
          ]
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be either \"convex\" or \"concave\".",
          "Please choose between \"convex\" and \"concave\".",
          "Select \"convex\" or \"concave\" as your response."
        ]
      }
    },
    "convexity10": {
      "QA": [
        [
          "Which lens is <2> among the given lenses?",
          "The <2> lens among them is <5>."
        ],
        [
          "Identify the <2> lens from the set of provided lenses.",
          "The lens that is <2> is <5>."
        ],
        [
          "Select the lens classified as <2> from the options given.",
          "The chosen <2> lens is <5>."
        ],
        [
          "Determine which lens meets the <2> property from the provided set.",
          "That <2> lens is <5>."
        ],
        [
          "Which lens qualifies as <2> in the list?",
          "The lens qualifying as <2> is <5>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the given lenses, the <2> lens is (<3>).",
            "Among the given lenses, the <2> lens is <5>."
          ],
          [
            "Choose the correct term from parentheses to finish the statement. The lens that is <2> is (<3>).",
            "The lens that is <2> is <5>."
          ],
          [
            "Pick one word in parentheses to conclude the sentence. The <2> lens among them is (<3>).",
            "The <2> lens among them is <5>."
          ]
        ],
        "type3": [
          "For example, if the only <2> lens is Z, then you should answer \"Z\".",
          "If Z is the unique lens that is <2>, then the correct response is \"Z\".",
          "As an instance, if there's only one <2> lens labeled Z, your answer is \"Z\"."
        ],
        "type4": [
          "The answer must be selected from <4>.",
          "Please pick your answer from <4>.",
          "Choose the correct lens from <4>."
        ]
      }
    },
    "convexity11": {
      "QA": [
        [
          "What is the color of the <2> lens among the given lenses?",
          "Its color is <5>."
        ],
        [
          "Identify the color of the lens that is <2> from the options provided.",
          "The <2> lens has the color <5>."
        ],
        [
          "Which lens, categorized as <2>, and what is its color?",
          "The lens that is <2> is colored <5>."
        ],
        [
          "From the given lenses, find the color of the lens that is <2>.",
          "The color of the <2> lens is <5>."
        ],
        [
          "Determine the color of the lens that meets the <2> property.",
          "The lens fulfilling <2> is <5> in color."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one word from the parentheses to complete the sentence. Among the given lenses, the <2> lens has the color (<3>).",
            "Among the given lenses, the <2> lens has the color <5>."
          ],
          [
            "Choose the correct term in parentheses to finish the statement. The color of the <2> lens is (<3>).",
            "The color of the <2> lens is <5>."
          ],
          [
            "Pick one word from the parentheses. The <2> lens among them is colored (<3>).",
            "The <2> lens among them is colored <5>."
          ]
        ],
        "type3": [
          "For example, if the only <2> lens is red, then you should answer \"red\".",
          "If red is the single color for the <2> lens, your response should be \"red\".",
          "As an instance, if the unique <2> lens has the color red, the correct answer is \"red\"."
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Select the color from <4>.",
          "Pick your answer from <4>."
        ]
      }
    },
    "convexity12": {
      "QA": [
        [
          "Which lenses are <2> among the provided options?",
          "All <2> lenses are <5>."
        ],
        [
          "Identify every lens that is <2> in the given list.",
          "The <2> lenses from the list are <5>."
        ],
        [
          "Select all lenses classified as <2> from the provided choices.",
          "Those <2> lenses are <5>."
        ],
        [
          "Determine the lenses that meet the <2> property among the ones shown.",
          "They are <5>."
        ],
        [
          "Which lenses qualify as <2> in the set provided?",
          "The qualifying lenses are <5>."
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          [
            "Select one or more words from the parentheses to complete the sentence. The <2> lenses among the given options are (<3>).",
            "The <2> lenses among the given options are <5>."
          ],
          [
            "Choose all correct items in parentheses to finish the statement. The lenses that are <2> happen to be (<3>).",
            "The lenses that are <2> happen to be <5>."
          ],
          [
            "Pick the applicable words in parentheses. The <2> lenses from the list are (<3>).",
            "The <2> lenses from the list are <5>."
          ]
        ],
        "type3": [
          "For instance, if the <2> lenses are A, B, and C, the answer should be \"A, B, C\".",
          "If lenses labeled A, B, and C are <2>, your response is \"A, B, C\".",
          "As an example, if A, B, and C are <2> lenses, answer with \"A, B, C\"."
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Please select your answers from <4>.",
          "Choose all appropriate options from <4>."
        ]
      }
    },
    "convexity13": {
      "QA": [
        [
          "Which colors belong to the <2> lenses among the given ones?",
          "Their colors are <5>."
        ],
        [
          "Identify all the colors of the lenses that are <2> in the provided set.",
          "The <2> lenses each have colors <5>."
        ],
        [
          "Which lenses, categorized as <2>, and what are their colors?",
          "They are <5> in color."
        ],
        [
          "From the given lenses, find all colors of those that are <2>.",
          "The <2> lenses have the following colors: <5>."
        ],
        [
          "Determine the colors of every lens that meets the <2> property.",
          "The colors of the <2> lenses are <5>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          [
            "Select one or more words from the parentheses to complete the sentence. The <2> lenses each have colors (<3>).",
            "The <2> lenses each have colors <5>."
          ],
          [
            "Choose all applicable options in parentheses to finish the statement. Among the given lenses, the <2> lenses have colors (<3>).",
            "Among the given lenses, the <2> lenses have colors <5>."
          ],
          [
            "Pick the correct words from the parentheses. The lenses that are <2> show colors (<3>).",
            "The lenses that are <2> show colors <5>."
          ]
        ],
        "type3": [
          "For example, if the <2> lenses have red, blue, and yellow colors, your answer should be \"red, blue, yellow\".",
          "If the colors are red, blue, and yellow for the <2> lenses, you should respond with \"red, blue, yellow\".",
          "As an instance, if each <2> lens is colored red, blue, or yellow, your answer should be \"red, blue, yellow\"."
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Select your color answers from <4>.",
          "Pick the correct colors from <4>."
        ]
      }
    }
  },
  "conversation_short": {
    "convexity1": {
      "QA": [
        [
          "Is the given shape concave or convex?",
          "<2>"
        ],
        [
          "Which type does this shape belong to: concave or convex?",
          "<2>"
        ],
        [
          "Identify whether the shape is concave or convex.",
          "<2>"
        ],
        [
          "Determine if the shape is concave or convex.",
          "<2>"
        ],
        [
          "Is this shape <2>?",
          "<2>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from the parentheses to complete the sentence. The given shape is (convex/concave).",
          "Choose the correct option in parentheses. The shape is (convex/concave).",
          "Pick the right word in parentheses. The shape is (convex/concave)."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "You must choose either \"convex\" or \"concave\".",
          "Please select \"convex\" or \"concave\" as the answer.",
          "The answer should be \"convex\" or \"concave\"."
        ]
      }
    },
    "convexity2": {
      "QA": [
        [
          "Which shape is <2> among the given ones?",
          "<5>"
        ],
        [
          "Identify the <2> shape in the list.",
          "<5>"
        ],
        [
          "Select the shape that qualifies as <2>.",
          "<5>"
        ],
        [
          "Which one is <2>?",
          "<5>"
        ],
        [
          "Determine the shape labeled as <2>.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from parentheses to finalize the sentence. The shape that is <2> is (<3>).",
          "Choose the correct term. The <2> shape is (<3>).",
          "Pick the option in parentheses. The <2> shape is (<3>)."
        ],
        "type3": [
          "For example, if the <2> shape is Z, answer \"Z\".",
          "If Z is the shape that is <2>, respond with \"Z\".",
          "As an instance, if Z is the only <2> shape, you write \"Z\"."
        ],
        "type4": [
          "The answer must be picked from <4>.",
          "Choose from <4>.",
          "Select the correct shape from <4>."
        ]
      }
    },
    "convexity3": {
      "QA": [
        [
          "Which color does the <2> shape have?",
          "<5>"
        ],
        [
          "Identify the color of the shape that is <2>.",
          "<5>"
        ],
        [
          "What color belongs to the <2> shape?",
          "<5>"
        ],
        [
          "State the color of the <2> shape.",
          "<5>"
        ],
        [
          "Name the color of the shape that is <2>.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word from parentheses to complete the sentence. The <2> shape has color (<3>).",
          "Choose the correct term. The color of the <2> shape is (<3>).",
          "Pick the option in parentheses. The shape that is <2> has color (<3>)."
        ],
        "type3": [
          "For instance, if it's red, answer \"red\".",
          "If the color is red, respond with \"red\".",
          "As an example, if the <2> shape is red, write \"red\"."
        ],
        "type4": [
          "The answer must be selected from <4>.",
          "Pick the correct color from <4>.",
          "Choose from <4>."
        ]
      }
    },
    "convexity4": {
      "QA": [
        [
          "Which shapes are <2>?",
          "<5>"
        ],
        [
          "Identify all shapes that are <2>.",
          "<5>"
        ],
        [
          "Select the <2> shapes.",
          "<5>"
        ],
        [
          "Which ones meet the <2> property?",
          "<5>"
        ],
        [
          "Name every shape that is <2>.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one or more terms from parentheses. The <2> shapes are (<3>).",
          "Choose all applicable words. The shapes that are <2> are (<3>).",
          "Pick from the parentheses. The <2> shapes among them are (<3>)."
        ],
        "type3": [
          "For instance, if they are A, B, C, you answer \"A, B, C\".",
          "If A, B, and C are <2>, respond \"A, B, C\".",
          "As an example, if the shapes are A, B, C, write \"A, B, C\"."
        ],
        "type4": [
          "The answer must come from <4>.",
          "Pick your answers from <4>.",
          "Select all fitting options from <4>."
        ]
      }
    },
    "convexity5": {
      "QA": [
        [
          "Which colors belong to the shapes that are <2>?",
          "<5>"
        ],
        [
          "Identify all colors of the <2> shapes.",
          "<5>"
        ],
        [
          "What are the colors of the <2> shapes?",
          "<5>"
        ],
        [
          "Select the colors of the shapes that are <2>.",
          "<5>"
        ],
        [
          "Name the colors for every <2> shape.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one or more from parentheses. The <2> shapes have colors (<3>).",
          "Choose the relevant words. The colors of the <2> shapes are (<3>).",
          "Pick the options in parentheses. The <2> shapes' colors are (<3>)."
        ],
        "type3": [
          "For example, if they are red, blue, green, answer \"red, blue, green\".",
          "If the colors are red, blue, green, respond \"red, blue, green\".",
          "As an instance, if red, blue, green are the colors, write \"red, blue, green\"."
        ],
        "type4": [
          "The answer must be selected from <4>.",
          "Pick from <4>.",
          "Choose the correct colors from <4>."
        ]
      }
    },
    "convexity6": {
      "QA": [
        [
          "Is the function concave or convex?",
          "<2>"
        ],
        [
          "Which type does the function belong to: concave or convex?",
          "<2>"
        ],
        [
          "Identify if the function is concave or convex.",
          "<2>"
        ],
        [
          "Determine whether the function is concave or convex.",
          "<2>"
        ],
        [
          "Specify if the function is concave or convex.",
          "<2>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from parentheses. The function is (convex/concave).",
          "Choose the correct term. This function is (convex/concave).",
          "Pick from parentheses to complete the sentence. The function is (convex/concave)."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be \"convex\" or \"concave\".",
          "Select \"convex\" or \"concave\".",
          "Choose either \"convex\" or \"concave\"."
        ]
      }
    },
    "convexity7": {
      "QA": [
        [
          "Which regions are <2> in the function?",
          ""
        ],
        [
          "Identify all the <2> regions in the function.",
          ""
        ],
        [
          "Select the portion(s) that are <2>.",
          ""
        ],
        [
          "Which parts of the function are <2>?",
          ""
        ],
        [
          "Determine the <2> areas from the highlighted function.",
          ""
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one or more words. The function's <2> regions are (<3>).",
          "Pick from parentheses. The <2> portions are (<3>).",
          "Choose the relevant terms. The <2> parts are (<3>)."
        ],
        "type3": [
          "For example, if the <2> regions are 1, 3, 4, write \"1, 3, 4\".",
          "If 1, 3, 4 are <2>, answer \"1, 3, 4\".",
          "As an instance, if the <2> segments are 1, 3, and 4, respond \"1, 3, 4\"."
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Pick your answers from <4>.",
          "Select the correct regions from <4>."
        ]
      }
    },
    "convexity8": {
      "QA": [
        [
          "Which segments are <2> when the function is divided by the marked point?",
          "<5>"
        ],
        [
          "Identify the segments that qualify as <2> in the partitioned function.",
          "<5>"
        ],
        [
          "Select all intervals that are <2> based on the point division.",
          "<5>"
        ],
        [
          "Which intervals are <2> after splitting the function at the given point?",
          "<5>"
        ],
        [
          "Name the <2> segments formed by partitioning the function at the point.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one or more words. The <2> segments are (<3>).",
          "Pick the correct terms in parentheses. The function's <2> intervals are (<3>).",
          "Choose from the parentheses. After splitting, the <2> regions are (<3>)."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be selected from <4>.",
          "Pick the correct segments from <4>.",
          "Choose your answer from <4>."
        ]
      }
    },
    "convexity9": {
      "QA": [
        [
          "Is the lens concave or convex?",
          "<2>"
        ],
        [
          "Which type does the lens belong to: concave or convex?",
          "<2>"
        ],
        [
          "Identify if the lens is concave or convex.",
          "<2>"
        ],
        [
          "Determine whether the lens is concave or convex.",
          "<2>"
        ],
        [
          "Specify if the lens is concave or convex.",
          "<2>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word. The lens is (convex/concave).",
          "Choose the correct term in parentheses. This lens is (convex/concave).",
          "Pick from parentheses to complete the statement. The lens is (convex/concave)."
        ],
        "type3": [
          ""
        ],
        "type4": [
          "The answer must be either \"convex\" or \"concave\".",
          "Choose from \"convex\" or \"concave\".",
          "Select your response as \"convex\" or \"concave\"."
        ]
      }
    },
    "convexity10": {
      "QA": [
        [
          "Which lens is <2> among the given ones?",
          "<5>"
        ],
        [
          "Identify the lens that is <2>.",
          "<5>"
        ],
        [
          "Select the <2> lens from the options provided.",
          "<5>"
        ],
        [
          "Which lens meets the <2> property?",
          "<5>"
        ],
        [
          "Determine the <2> lens in this list.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one word from parentheses. Among the given lenses, the <2> lens is (<3>).",
          "Choose the correct term. The lens that is <2> is (<3>).",
          "Pick the option in parentheses. The <2> lens among them is (<3>)."
        ],
        "type3": [
          "For example, if Z is the only <2> lens, answer \"Z\".",
          "If the <2> lens is Z, respond with \"Z\".",
          "As an instance, if Z is the sole <2> lens, write \"Z\"."
        ],
        "type4": [
          "The answer must come from <4>.",
          "Choose your answer from <4>.",
          "Pick the correct lens from <4>."
        ]
      }
    },
    "convexity11": {
      "QA": [
        [
          "What is the color of the <2> lens?",
          "<5>"
        ],
        [
          "Identify the color for the lens that is <2>.",
          "<5>"
        ],
        [
          "Which lens is <2>, and what's its color?",
          "<5>"
        ],
        [
          "Find the color of the lens classified as <2>.",
          "<5>"
        ],
        [
          "State the color of the <2> lens among the given ones.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one word. The <2> lens has color (<3>).",
          "Choose from parentheses. The color of the <2> lens is (<3>).",
          "Pick the correct term. The lens that is <2> is colored (<3>)."
        ],
        "type3": [
          "For instance, if it's red, answer \"red\".",
          "If red is the color, respond \"red\".",
          "As an example, if the color is red, write \"red\"."
        ],
        "type4": [
          "The answer must be selected from <4>.",
          "Pick your color from <4>.",
          "Choose the correct color from <4>."
        ]
      }
    },
    "convexity12": {
      "QA": [
        [
          "Which lenses are <2> among the list provided?",
          "<5>"
        ],
        [
          "Identify all lenses that are <2>.",
          "<5>"
        ],
        [
          "Select every lens that meets the <2> property.",
          "<5>"
        ],
        [
          "Which ones classify as <2> lenses?",
          "<5>"
        ],
        [
          "Name the lenses labeled as <2>.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "True"
        ],
        "type2": [
          "Select one or more from parentheses. The <2> lenses are (<3>).",
          "Choose the correct items. The lenses that are <2> include (<3>).",
          "Pick from parentheses. The <2> lenses in the list are (<3>)."
        ],
        "type3": [
          "For instance, if the <2> lenses are A, B, C, your answer is \"A, B, C\".",
          "If A, B, C are all <2> lenses, respond with \"A, B, C\".",
          "As an example, if A, B, and C are <2>, write \"A, B, C\"."
        ],
        "type4": [
          "The answer must be chosen from <4>.",
          "Pick your answers from <4>.",
          "Select all applicable lenses from <4>."
        ]
      }
    },
    "convexity13": {
      "QA": [
        [
          "Which colors belong to the <2> lenses?",
          "<5>"
        ],
        [
          "Identify the colors of the lenses that are <2>.",
          "<5>"
        ],
        [
          "What are the colors of the <2> lenses?",
          "<5>"
        ],
        [
          "List all colors for the lenses categorized as <2>.",
          "<5>"
        ],
        [
          "Select the colors associated with <2> lenses.",
          "<5>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          "Select one or more words in parentheses. The lenses that are <2> have colors (<3>).",
          "Choose the correct items. The <2> lenses each show colors (<3>).",
          "Pick from parentheses. The lenses <2> are described by colors (<3>)."
        ],
        "type3": [
          "For example, if they're red, blue, yellow, answer \"red, blue, yellow\".",
          "If the colors are red, blue, and yellow, respond with \"red, blue, yellow\".",
          "As an instance, if those <2> lenses are red, blue, and yellow, you should write \"red, blue, yellow\"."
        ],
        "type4": [
          "The answer must come from <4>.",
          "Choose the correct colors from <4>.",
          "Pick your answer from <4>."
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
        for i in range(1, len(entity[1])):
            q = q.replace(f"<{i+1}>", entity[1][i])
            a = a.replace(f"<{i+1}>", entity[1][i])
        conversation_list.append((q, a))
    return conversation_list