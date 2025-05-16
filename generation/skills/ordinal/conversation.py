from .rules import *

import random

# Correct the indentation of this dictionary. 
# This json has List of Rephrased [Question, Answer] per each of the conversation problem types. 
# For conversation problem types that has less than 5 rephrases, generate rephrases. 
# When rephrasing the pquestion, answer] You need to make not only a rephrased question, but also rephrased answer. 

conversation_long =  {
        "ordinal_1": [
            [
                "There are a circle, a triangle, a rectangle, a hexagon, and a pentagon in the image. What is the name of the <1> shape from the bottom?",
                "The <1> shape from the bottom is a <2>."
            ],
            [
                "In the image, there are a circle, a triangle, a rectangle, a hexagon, and a pentagon. What is the name of the <1> shape from the bottom?",
                "It is a <2> that corresponds to the <1> shape from the bottom."
            ],
            [
                "What is the <1> shape from the bottom in the image that contains a circle, a triangle, a rectangle, a hexagon, and a pentagon?",
                "From the bottom, the <1> shape is identified as a <2>."
            ],
            [
                "Given a circle, a triangle, a rectangle, a hexagon, and a pentagon in the image, what is the <1> shape from the bottom?",
                "A <2> is the <1> shape when counted from the bottom."
            ],
            [
                "Among the shapes in the image (a circle, a triangle, a rectangle, a hexagon, and a pentagon), what is the <1> shape from the bottom?",
                "The shape in the <1> position from the bottom is a <2>."
            ],
            [
                "In the image containing a circle, a triangle, a rectangle, a hexagon, and a pentagon, what is the <1> shape counted from the bottom?",
                "When counted from the bottom, the <1> shape is a <2>."
            ],
            [
                "What is the name of the <1> shape from the bottom in the image featuring a circle, a triangle, a rectangle, a hexagon, and a pentagon?",
                "The <1> shape is none other than a <2>."
            ],
            [
                "From the image containing a circle, a triangle, a rectangle, a hexagon, and a pentagon, what is the <1> shape starting from the bottom?",
                "Starting from the bottom, the <1> shape is a <2>."
            ],
            [
                "In the image where there are a circle, a triangle, a rectangle, a hexagon, and a pentagon, what is the <1> shape from the bottom?",
                "The <1> shape in the sequence is a <2>."
            ],
            [
                "What is the <1> shape counted from the bottom in the image that contains a circle, a triangle, a rectangle, a hexagon, and a pentagon?",
                "From the bottom of the image, the <1> shape happens to be a <2>."
            ]
        ],
        "ordinal_2": [
            [
                "There are several letters in the image. What is the letter that is <1> from the above? You should also consider its case (upper or lower).",
                "The letter that is <1> from the above is the letter <2>."
            ],
            [
                "In the image, multiple letters are present. Which letter is positioned <1> from the top? Remember to note its case (uppercase or lowercase).",
                "The letter positioned <1> from the top is <2>."
            ],
            [
                "Looking at the image with various letters, identify the letter that is <1> below the top. Consider whether it's uppercase or lowercase.",
                "The letter <2> is located <1> below the top."
            ],
            [
                "Examine the image containing several letters. Which letter stands <1> below the highest one? Take into account its case.",
                "The letter that stands <1> below the highest one is <2>."
            ],
            [
                "In the provided image with multiple letters, which letter is <1> away from the top? Ensure to consider its case (upper or lower).",
                "The letter <2> is <1> away from the top."
            ]
        ],
        "ordinal_3": [
            [
                "There are three labeled points on this 2-d graph. Choose the point that is in the <1>-highest position. The answer should be one of <2>, <3>, or <4>.",
                "The point <5> is in the <1>-highest position."
            ],
            [
                "In the 2D graph, three points are marked. Which point holds the <1>-highest position? Select from <2>, <3>, or <4>.",
                "Point <5> holds the <1>-highest position."
            ],
            [
                "Looking at the 2-dimensional graph with three labeled points, identify the point that is the <1>-highest. Your choices are <2>, <3>, or <4>.",
                "The <1>-highest point is <5>."
            ],
            [
                "On the 2D graph, three points are labeled. Which one is in the <1>-highest position? Choose between <2>, <3>, and <4>.",
                "Point <5> is the one in the <1>-highest position."
            ],
            [
                "Examine the 2D graph featuring three labeled points. Which point occupies the <1>-highest position? The options are <2>, <3>, or <4>.",
                "The point occupying the <1>-highest position is <5>."
            ]
        ],
        "ordinal_4": [
            [
                "In the image, there are three labeled shapes with different sizes. Which is the label of the <1> smallest shape? The answer should be one of <2>, <3>, or <4>.",
                "The label <5> corresponds to the <1> smallest shape."
            ],
            [
                "Looking at the image with three distinct labeled shapes, identify the label of the <1> smallest one. Choose from <2>, <3>, or <4>.",
                "The <1> smallest shape is labeled as <5>."
            ],
            [
                "Examine the image that displays three labeled shapes of varying sizes. Which label represents the <1> smallest shape? Options are <2>, <3>, or <4>.",
                "Label <5> represents the <1> smallest shape."
            ],
            [
                "In the provided image with three differently sized labeled shapes, which label corresponds to the <1> smallest shape? Select from <2>, <3>, or <4>.",
                "The <1> smallest shape is associated with label <5>."
            ],
            [
                "Identify the label of the <1> smallest shape among the three labeled shapes in the image. Your choices are <2>, <3>, or <4>.",
                "Label <5> is assigned to the <1> smallest shape."
            ]
        ],
        "ordinal_5": [
            [
                "There are several letters in the image. What is the letter that is <1> from the above? You should also consider its case.",
                "The letter that is <1> from the above is the letter <2>."
            ],
            [
                "In the image, multiple letters are present. Which letter is positioned <1> from the top? Remember to note its case (uppercase or lowercase).",
                "The letter positioned <1> from the top is <2>."
            ],
            [
                "Looking at the image with various letters, identify the letter that is <1> below the top. Consider whether it's uppercase or lowercase.",
                "The letter <2> is located <1> below the top."
            ],
            [
                "Examine the image containing several letters. Which letter stands <1> below the highest one? Take into account its case.",
                "The letter that stands <1> below the highest one is <2>."
            ],
            [
                "In the provided image with multiple letters, which letter is <1> away from the top? Ensure to consider its case (upper or lower).",
                "The letter <2> is <1> away from the top."
            ]
        ],
        "ordinal_6": [
            [
                "There is a table with distinct letters in the image. Find the location of letter <6>. Answer in ”(row, column)” format. For example, <3> is at <2> and <5> is at <4>.",
                "The letter <6> is at <1>."
            ],
            [
                "In the image, a table displays unique letters. Determine the position of letter <6>. Provide your answer as (row, column). For instance, <3> is located at <2> and <5> is at <4>.",
                "Letter <6> is located at <1>."
            ],
            [
                "Looking at the table with different letters in the image, identify where letter <6> is placed. Use the format (row, column). For example, <3> is in <2> and <5> is in <4>.",
                "Letter <6> can be found at <1>."
            ],
            [
                "Examine the image of a table containing distinct letters. Where is letter <6> positioned? Answer using (row, column) format, such as <3> is at <2> and <5> is at <4>.",
                "The position of letter <6> is <1>."
            ],
            [
                "In the provided table with unique letters shown in the image, locate letter <6>. Respond in the format (row, column). For example, <3> is at <2> and <5> is at <4>.",
                "Letter <6> is positioned at <1>."
            ]
        ]
}

conversation_caption = {
  "ordinal_1": [
    ["", "The <1> shape from the bottom is a <2>."],
    ["", "It is a <2> that corresponds to the <1> shape from the bottom."],
    ["", "From the bottom, the <1> shape is identified as a <2>."],
    ["", "A <2> is the <1> shape when counted from the bottom."],
    ["", "The shape in the <1> position from the bottom is a <2>."],
    ["", "When counted from the bottom, the <1> shape is a <2>."],
    ["", "The <1> shape is none other than a <2>."],
    ["", "Starting from the bottom, the <1> shape is a <2>."],
    ["", "The <1> shape in the sequence is a <2>."],
    ["", "From the bottom of the image, the <1> shape happens to be a <2>."]
  ],
  "ordinal_2": [
    ["", "The letter that is <1> from the above is the letter <2>."],
    ["", "The letter positioned <1> from the top is <2>."],
    ["", "The letter <2> is located <1> below the top."],
    ["", "The letter that stands <1> below the highest one is <2>."],
    ["", "The letter <2> is <1> away from the top."]
  ],
  "ordinal_3": [
    ["", "The point <5> is in the <1>-highest position among <2>, <3>, and <4>."],
    ["", "Point <5> holds the <1>-highest position among <2>, <3>, and <4>."],
    ["", "The <1>-highest point is <5> among <2>, <3>, and <4>."],
    ["", "Point <5> is the one in the <1>-highest position among <2>, <3>, and <4>."],
    ["", "The point occupying the <1>-highest position is <5> among <2>, <3>, and <4>."]
  ],
  "ordinal_4": [
    ["", "The label <5> corresponds to the <1> smallest shape among <2>, <3>, and <4>."],
    ["", "The <1> smallest shape is labeled as <5> among <2>, <3>, and <4>."],
    ["", "Label <5> represents the <1> smallest shape among <2>, <3>, and <4>."],
    ["", "The <1> smallest shape is associated with label <5> among <2>, <3>, and <4>."],
    ["", "Label <5> is assigned to the <1> smallest shape among <2>, <3>, and <4>."]
  ],
  "ordinal_5": [
    ["", "The letter that is <1> from the above is the letter <2>."],
    ["", "The letter positioned <1> from the top is <2>."],
    ["", "The letter <2> is located <1> below the top."],
    ["", "The letter that stands <1> below the highest one is <2>."],
    ["", "The letter <2> is <1> away from the top."]
  ],
  "ordinal_6": [
    ["", "The letter <6> is at <1> in the table, where <3> is at <2> and <5> is at <4>."],
    ["", "Letter <6> is located at <1> in the table, with <3> at <2> and <5> at <4>."],
    ["", "Letter <6> can be found at <1> in the table, where <3> is at <2> and <5> is at <4>."],
    ["", "The position of letter <6> is <1> in the table, with <3> at <2> and <5> at <4>."],
    ["", "Letter <6> is positioned at <1> in the table, where <3> is at <2> and <5> is at <4>." ]
  ]
}


conversation_short = {
        "ordinal_1": [
            [
                "There are a circle, a triangle, a rectangle, a hexagon, and a pentagon in the image. What is the name of the <1> shape from the bottom?",
                "<2>"
            ],
            [
                "In the image, there are a circle, a triangle, a rectangle, a hexagon, and a pentagon. What is the name of the <1> shape from the bottom?",
                "<2>"
            ],
            [
                "What is the <1> shape from the bottom in the image that contains a circle, a triangle, a rectangle, a hexagon, and a pentagon?",
                "<2>"
            ],
            [
                "Given a circle, a triangle, a rectangle, a hexagon, and a pentagon in the image, what is the <1> shape from the bottom?",
                "<2>"
            ],
            [
                "Among the shapes in the image (a circle, a triangle, a rectangle, a hexagon, and a pentagon), what is the <1> shape from the bottom?",
                "<2>"
            ],
            [
                "In the image containing a circle, a triangle, a rectangle, a hexagon, and a pentagon, what is the <1> shape counted from the bottom?",
                "<2>"
            ],
            [
                "What is the name of the <1> shape from the bottom in the image featuring a circle, a triangle, a rectangle, a hexagon, and a pentagon?",
                "<2>"
            ],
            [
                "From the image containing a circle, a triangle, a rectangle, a hexagon, and a pentagon, what is the <1> shape starting from the bottom?",
                "<2>"
            ],
            [
                "In the image where there are a circle, a triangle, a rectangle, a hexagon, and a pentagon, what is the <1> shape from the bottom?",
                "<2>"
            ],
            [
                "What is the <1> shape counted from the bottom in the image that contains a circle, a triangle, a rectangle, a hexagon, and a pentagon?",
                "<2>"
            ]
        ],
        "ordinal_2": [
            [
                "There are several letters in the image. What is the letter that is <1> from the above? You should also consider its case (upper or lower).",
                "<2>"
            ],
            [
                "In the image, multiple letters are present. Which letter is positioned <1> from the top? Remember to note its case (uppercase or lowercase).",
                "<2>"
            ],
            [
                "Looking at the image with various letters, identify the letter that is <1> below the top. Consider whether it's uppercase or lowercase.",
                "<2>"
            ],
            [
                "Examine the image containing several letters. Which letter stands <1> below the highest one? Take into account its case.",
                "<2>"
            ],
            [
                "In the provided image with multiple letters, which letter is <1> away from the top? Ensure to consider its case (upper or lower).",
                "<2>"
            ]
        ],
        "ordinal_3": [
            [
                "There are three labeled points on this 2-d graph. Choose the point that is in the <1>-highest position. The answer should be one of <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "In the 2D graph, three points are marked. Which point holds the <1>-highest position? Select from <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "Looking at the 2-dimensional graph with three labeled points, identify the point that is the <1>-highest. Your choices are <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "On the 2D graph, three points are labeled. Which one is in the <1>-highest position? Choose between <2>, <3>, and <4>.",
                "<5>"
            ],
            [
                "Examine the 2D graph featuring three labeled points. Which point occupies the <1>-highest position? The options are <2>, <3>, or <4>.",
                "<5>"
            ]
        ],
        "ordinal_4": [
            [
                "In the image, there are three labeled shapes with different sizes. Which is the label of the <1> smallest shape? The answer should be one of <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "Looking at the image with three distinct labeled shapes, identify the label of the <1> smallest one. Choose from <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "Examine the image that displays three labeled shapes of varying sizes. Which label represents the <1> smallest shape? Options are <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "In the provided image with three differently sized labeled shapes, which label corresponds to the <1> smallest shape? Select from <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "Identify the label of the <1> smallest shape among the three labeled shapes in the image. Your choices are <2>, <3>, or <4>.",
                "<5>"
            ]
        ],
        "ordinal_5": [
            [
                "There are several letters in the image. What is the letter that is <1> from the above? You should also consider its case.",
                "<2>"
            ],
            [
                "In the image, multiple letters are present. Which letter is positioned <1> from the top? Remember to note its case (uppercase or lowercase).",
                "<2>"
            ],
            [
                "Looking at the image with various letters, identify the letter that is <1> below the top. Consider whether it's uppercase or lowercase.",
                "<2>"
            ],
            [
                "Examine the image containing several letters. Which letter stands <1> below the highest one? Take into account its case.",
                "<2>"
            ],
            [
                "In the provided image with multiple letters, which letter is <1> away from the top? Ensure to consider its case (upper or lower).",
                "<2>"
            ]
        ],
        "ordinal_6": [
            [
                "There is a table with distinct letters in the image. Find the location of letter <6>. Answer in ”(row, column)” format. For example, <3> is at <2> and <5> is at <4>.",
                "<1>"
            ],
            [
                "In the image, a table displays unique letters. Determine the position of letter <6>. Provide your answer as (row, column). For instance, <3> is located at <2> and <5> is at <4>.",
                "<1>"
            ],
            [
                "Looking at the table with different letters in the image, identify where letter <6> is placed. Use the format (row, column). For example, <3> is in <2> and <5> is in <4>.",
                "<1>"
            ],
            [
                "Examine the image of a table containing distinct letters. Where is letter <6> positioned? Answer using (row, column) format, such as <3> is at <2> and <5> is at <4>.",
                "<1>"
            ],
            [
                "In the provided table with unique letters shown in the image, locate letter <6>. Respond in the format (row, column). For example, <3> is at <2> and <5> is at <4>.",
                "<1>"
            ]
        ]
}


alphabets = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
numbers = set(list('0123456789'))

def generate_qa (entity, long=False, caption=False):

    rule            = entity[0] 
    inputs          = entity[1]
    if caption : 
        conversation = conversation_caption[rule]
    else : 
        conversation = conversation_long[rule] if long else conversation_short[rule]
    question, answer = random.choice ( conversation )
    for i in range(len(inputs)) : 
        question = question.replace(f'<{i+1}>', inputs[i])
        answer   = answer.replace(f'<{i+1}>', inputs[i])
    return question, answer

def generate_conversation(diagram, long=False, caption=False):
    conversation_list = []
    for entity in diagram.entities:
        conversation_list.append(generate_qa(entity, long, caption))
            
    return conversation_list