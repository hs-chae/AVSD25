from .rules import *

import random

# Correct the indentation of this dictionary. 
# This json has List of Rephrased [Question, Answer] per each of the conversation problem types. 
# For conversation problem types that has less than 5 rephrases, generate rephrases. 
# When rephrasing the pquestion, answer] You need to make not only a rephrased question, but also rephrased answer. 


# Given the conversation_long generate conversation_caption, where a caption instance have blank question and full decdiption as answer. 
# For example, for the following conversation in conversation_long, 
# [
#                 "In the image, there is a pie graph with four categories. Which category has the largest ratio? Choose from <1>, <2>, <3>, and <4>.",
#                 "Category <5> has the largest ratio."
# ],
# example caption instance would be 
# [
#               "",
#               "In the image, there is a pie graph with four categories. From categories <1>, <2>, <3>, and <4>, category <5> has the largest ratio"
# ]
# Note that you must include full details in the original answer in the caption. 
# Now, generate conversation_caption corresponding to the following conversation_long : 
conversation_long = {
        "orientation_1": [
            [
                "In the given image, there are letters arranged on a circle. If we read those letters clockwise or counterclockwise, we can form a word (a sequence of letters), <1>. Which direction should we read? Answer clockwise or counterclockwise.",
                "You should read it in the <2> direction."
            ],
            [
                "The image shows letters placed on a circle. Reading them either clockwise or counterclockwise forms the word <1>. Which reading direction is correct? Choose clockwise or counterclockwise.",
                "The correct direction to read is <2>."
            ],
            [
                "In the image, letters are positioned on a circle, and reading them clockwise or counterclockwise forms the word <1>. Which way should the letters be read? Answer clockwise or counterclockwise.",
                "Reading in the <2> direction is appropriate."
            ],
            [
                "There are letters on a circle in the given image. These letters form the word <1> when read clockwise or counterclockwise. Which direction is correct? Clockwise or counterclockwise?",
                "The word <1> can be formed by reading in the <2> direction."
            ],
            [
                "The letters on a circle in the image spell the word <1> when read clockwise or counterclockwise. Which direction is correct? Clockwise or counterclockwise?",
                "To form <1>, you need to read in the <2> direction."
            ],
            [
                "In the provided image, letters are arranged on a circular path. Reading clockwise or counterclockwise forms the word <1>. Which direction should you follow? Clockwise or counterclockwise?",
                "You should follow the <2> direction to form the word."
            ],
            [
                "The circular arrangement of letters in the image spells <1> when read clockwise or counterclockwise. Which is the correct direction? Clockwise or counterclockwise?",
                "The correct reading direction is <2>."
            ],
            [
                "Letters placed on a circle in the image form the word <1> when read clockwise or counterclockwise. Which direction should you use? Clockwise or counterclockwise?",
                "Use the <2> direction to read the sequence of letters <1>."
            ],
            [
                "In the image, letters arranged in a circular pattern spell <1> when read either clockwise or counterclockwise. Which direction is the correct one? Clockwise or counterclockwise?",
                "The correct direction for reading is <2>."
            ],
            [
                "The image displays letters on a circle that spell the word <1> when read clockwise or counterclockwise. Which direction should be used? Clockwise or counterclockwise?",
                "Reading in the <2> direction will spell <1>."
            ]
        ],
        "orientation_2": [
            [
                "There is a circle with letters on the image. Read the letters in <1> order starting from <2> (including <2>). For example, if you can read A, B, C, and D, your answer should be “ABCD”.",
                "My answer is <3>."
            ],
            [
                "In the image, letters are arranged in a circular pattern. Starting at <2>, read the letters in <1> order. For instance, if the letters are A, B, C, and D, the sequence should be “ABCD”.",
                "The sequence I read is <3>."
            ],
            [
                "The image shows letters placed around a circle. Begin reading from <2> and proceed in <1> order. For example, with letters A, B, C, and D, your answer would be “ABCD”.",
                "I read the letters as <3>."
            ],
            [
                "Letters are positioned on a circular path in the image. Starting from <2>, read them in <1> order. If the letters are A, B, C, and D, your response should be “ABCD”.",
                "The sequence is <3>."
            ],
            [
                "In the provided circular arrangement of letters, begin at <2> and read the letters in <1> order. For example, A, B, C, and D should be read as “ABCD”.",
                "The letters read in order are <3>."
            ]
        ],
        "orientation_2_1": [
            [
                "In the given image, there is a rhombus with numbers 1 to 4 written at each vertex. Starting from the top vertex with the number <1> and reading clockwise, what number sequence is formed? If the sequence is a, b, c, d, answer in the format 'abcd'.",
                "My answer is <2>."
            ],
            [
                "The image displays a rhombus with numbers 1 through 4 at each corner. Begin at the top vertex labeled <1> and read the numbers in a clockwise direction. What is the resulting sequence? Provide your answer as 'abcd'.",
                "The resulting sequence is <2>."
            ],
            [
                "There is a rhombus in the image with numbers 1 to 4 at its vertices. Starting at the top vertex marked <1> and moving clockwise, what is the sequence of numbers? Answer in the format 'abcd'.",
                "The number sequence is <2>."
            ],
            [
                "In the provided rhombus, numbers 1 to 4 are placed at each vertex. Starting from the top vertex with number <1> and reading clockwise, what sequence do you obtain? Respond with 'abcd'.",
                "The sequence obtained is <2>."
            ],
            [
                "The rhombus in the image has numbers 1 to 4 at its vertices. Starting at the top vertex labeled <1> and proceeding clockwise, what is the number sequence formed? Please answer in the 'abcd' format.",
                "The formed sequence is <2>."
            ]
        ],
        "orientation_3": [
            [
                "In the image, there is a cycle. What is the direction of the cycle, clockwise or counterclockwise? You may use arrows in the image as hints. Choose your answer from ”clockwise” or ”counterclockwise”.",
                "The direction of the cycle is <1>."
            ],
            [
                "The image depicts a cycle with directional arrows. Is the cycle moving clockwise or counterclockwise? Select either 'clockwise' or 'counterclockwise'.",
                "The cycle is moving <1>."
            ],
            [
                "Looking at the cycle in the image, determine its direction. Is it clockwise or counterclockwise? Use the arrows as a guide and choose 'clockwise' or 'counterclockwise'.",
                "The direction of movement is <1>."
            ],
            [
                "Examine the cycle shown in the image. Based on the arrows, is the cycle's direction clockwise or counterclockwise? Answer with 'clockwise' or 'counterclockwise'.",
                "The cycle is oriented in a <1> direction."
            ],
            [
                "The image features a cycle with arrows indicating its path. Is the cycle traveling in a clockwise or counterclockwise direction? Choose between 'clockwise' and 'counterclockwise'.",
                "The cycle travels in a <1> direction."
            ]
        ],
        "orientation_4": [
            [
                "In the image, <2> arrows are on a circle. Are they pointing clockwise or counterclockwise? Choose one from ‘clockwise’ and ‘counterclockwise’.",
                "Arrows are pointing <1>."
            ],
            [
                "The image shows <2> arrows arranged around a circle. Are these arrows directed clockwise or counterclockwise? Select 'clockwise' or 'counterclockwise'.",
                "The arrows are directed <1>."
            ],
            [
                "There are <2> arrows placed on a circular path in the image. Are the arrows pointing in a clockwise or counterclockwise direction? Choose 'clockwise' or 'counterclockwise'.",
                "The direction of the arrows is <1>."
            ],
            [
                "Examine the circle in the image with <2> arrows. Do these arrows point clockwise or counterclockwise? Answer with 'clockwise' or 'counterclockwise'.",
                "The arrows on the circle point <1>."
            ],
            [
                "In the provided image, <2> arrows are arranged on a circle. Determine if they are pointing clockwise or counterclockwise. Choose 'clockwise' or 'counterclockwise'.",
                "Arrows are pointing in the <1> direction."
            ]
        ],
        "orientation_5": [
            [
                "In the image, there are four arrows <2>, <3>, <4>, and <5> on a circle. Among <2>, <3>, <4>, and <5>, all except one are pointing <1>. Answer the one arrow that is not rotating the circle <1>, with a letter denoting the arrow.",
                "Arrow <6>."
            ],
            [
                "The image displays four arrows labeled <2>, <3>, <4>, and <5> arranged on a circle. All arrows except one are pointing <1>. Identify the arrow that is not rotating the circle <1> by providing its letter.",
                "The arrows except <6> are pointing the same directions"
            ],
            [
                "On the circular arrangement in the image, there are arrows <2>, <3>, <4>, and <5>. All but one arrow are directed <1>. Which arrow is not contributing to the circle's <1> rotation? Provide the arrow's letter.",
                "The arrows except <6> are directed <1>."
            ],
            [
                "There are four arrows labeled <2>, <3>, <4>, and <5> on a circle in the image. Except for one, all arrows point <1>. Which arrow does not rotate the circle <1>? Answer with the corresponding letter.",
                "The arrows except <6> point <1> direction."
            ],
            [
                "In the provided image, four arrows <2>, <3>, <4>, and <5> are positioned on a circle. All arrows except one are pointing <1>. Identify the arrow that isn't rotating the circle <1> by its letter.",
                "The arrow that isn't pointing <1> is <6>."
            ]
        ]
    }

conversation_caption = {
  "orientation_1": [
    ["", "You should read it in the <2> direction."],
    ["", "The correct direction to read is <2>."],
    ["", "Reading in the <2> direction is appropriate."],
    ["", "The word <1> can be formed by reading in the <2> direction."],
    ["", "To form <1>, you need to read in the <2> direction."],
    ["", "You should follow the <2> direction to form the word."],
    ["", "The correct reading direction is <2>."],
    ["", "Use the <2> direction to read the sequence of letters <1>."],
    ["", "The correct direction for reading is <2>."],
    ["", "Reading in the <2> direction will spell <1>."]
  ],
  "orientation_2": [
    ["", "My answer is <3>."],
    ["", "The sequence I read is <3>."],
    ["", "I read the letters as <3>."],
    ["", "The sequence is <3>."],
    ["", "The letters read in order are <3>."]
  ],
  "orientation_2_1": [
    ["", "My answer is <2>."],
    ["", "The resulting sequence is <2>."],
    ["", "The number sequence is <2>."],
    ["", "The sequence obtained is <2>."],
    ["", "The formed sequence is <2>."]
  ],
  "orientation_3": [
    ["", "The direction of the cycle is <1>."],
    ["", "The cycle is moving <1>."],
    ["", "The direction of movement is <1>."],
    ["", "The cycle is oriented in a <1> direction."],
    ["", "The cycle travels in a <1> direction."]
  ],
  "orientation_4": [
    ["", "Arrows are pointing <1>."],
    ["", "The arrows are directed <1>."],
    ["", "The direction of the arrows is <1>."],
    ["", "The arrows on the circle point <1>."],
    ["", "Arrows are pointing in the <1> direction."]
  ],
  "orientation_5": [
    ["", "Arrow <6>."],
    ["", "The arrows except <6> are pointing the same directions."],
    ["", "The arrows except <6> are directed <1>."],
    ["", "The arrows except <6> point <1> direction."],
    ["", "The arrow that isn't pointing <1> is <6>."]
  ]
}


conversation_short = {
 "orientation_1" : [
    [
        "In the given image, there are letters arranged on a circle. If we read those letters clockwise or counterclockwise, we can form a word (a sequence of letters), <1>. Which direction should we read? Answer clockwise or counterclockwise.",
        "<2>"
    ],
    [
        "The image shows letters placed on a circle. Reading them either clockwise or counterclockwise forms the word <1>. Which reading direction is correct? Choose clockwise or counterclockwise.",
        "<2>"
    ],
    [
        "In the image, letters are positioned on a circle, and reading them clockwise or counterclockwise forms the word <1>. Which way should the letters be read? Answer clockwise or counterclockwise.",
        "<2>"
    ],
    [
        "There are letters on a circle in the given image. These letters form the word <1> when read clockwise or counterclockwise. Which direction is correct? Clockwise or counterclockwise?",
        "<2>"
    ],
    [
        "The letters on a circle in the image spell the word <1> when read clockwise or counterclockwise. Which direction is correct? Clockwise or counterclockwise?",
        "<2>"
    ],
    [
        "In the provided image, letters are arranged on a circular path. Reading clockwise or counterclockwise forms the word <1>. Which direction should you follow? Clockwise or counterclockwise?",
        "<2>"
    ],
    [
        "The circular arrangement of letters in the image spells <1> when read clockwise or counterclockwise. Which is the correct direction? Clockwise or counterclockwise?",
        "<2>"
    ],
    [
        "Letters placed on a circle in the image form the word <1> when read clockwise or counterclockwise. Which direction should you use? Clockwise or counterclockwise?",
        "<2>"
    ],
    [
        "In the image, letters arranged in a circular pattern spell <1> when read either clockwise or counterclockwise. Which direction is the correct one? Clockwise or counterclockwise?",
        "<2>"
    ],
    [
        "The image displays letters on a circle that spell the word <1> when read clockwise or counterclockwise. Which direction should be used? Clockwise or counterclockwise?",
        "<2>"
    ]
],
        "orientation_2": [
            [
                "There is a circle with letters on the image. Read the letters in <1> order starting from <2> (including <2>). For example, if you can read A, B, C, and D, your answer should be “ABCD”.",
                "<3>"
            ],
            [
                "In the image, letters are arranged in a circular pattern. Starting at <2>, read the letters in <1> order. For instance, if the letters are A, B, C, and D, the sequence should be “ABCD”.",
                "<3>"
            ],
            [
                "The image shows letters placed around a circle. Begin reading from <2> and proceed in <1> order. For example, with letters A, B, C, and D, your answer would be “ABCD”.",
                "<3>"
            ],
            [
                "Letters are positioned on a circular path in the image. Starting from <2>, read them in <1> order. If the letters are A, B, C, and D, your response should be “ABCD”.",
                "<3>"
            ],
            [
                "In the provided circular arrangement of letters, begin at <2> and read the letters in <1> order. For example, A, B, C, and D should be read as “ABCD”.",
                "<3>"
            ]
        ],
        "orientation_2_1": [
            [
                "In the given image, there is a rhombus with numbers 1 to 4 written at each vertex. Starting from the top vertex with the number <1> and reading clockwise, what number sequence is formed? If the sequence is a, b, c, d, answer in the format 'abcd'.",
                "<2>"
            ],
            [
                "The image displays a rhombus with numbers 1 through 4 at each corner. Begin at the top vertex labeled <1> and read the numbers in a clockwise direction. What is the resulting sequence? Provide your answer as 'abcd'.",
                "<2>"
            ],
            [
                "There is a rhombus in the image with numbers 1 to 4 at its vertices. Starting at the top vertex marked <1> and moving clockwise, what is the sequence of numbers? Answer in the format 'abcd'.",
                "<2>"
            ],
            [
                "In the provided rhombus, numbers 1 to 4 are placed at each vertex. Starting from the top vertex with number <1> and reading clockwise, what sequence do you obtain? Respond with 'abcd'.",
                "<2>"
            ],
            [
                "The rhombus in the image has numbers 1 to 4 at its vertices. Starting at the top vertex labeled <1> and proceeding clockwise, what is the number sequence formed? Please answer in the 'abcd' format.",
                "<2>"
            ]
        ],
        "orientation_3": [
            [
                "In the image, there is a cycle. What is the direction of the cycle, clockwise or counterclockwise? You may use arrows in the image as hints. Choose your answer from ”clockwise” or ”counterclockwise”.",
                "<1>"
            ],
            [
                "The image depicts a cycle with directional arrows. Is the cycle moving clockwise or counterclockwise? Select either 'clockwise' or 'counterclockwise'.",
                "<1>"
            ],
            [
                "Looking at the cycle in the image, determine its direction. Is it clockwise or counterclockwise? Use the arrows as a guide and choose 'clockwise' or 'counterclockwise'.",
                "<1>"
            ],
            [
                "Examine the cycle shown in the image. Based on the arrows, is the cycle's direction clockwise or counterclockwise? Answer with 'clockwise' or 'counterclockwise'.",
                "<1>"
            ],
            [
                "The image features a cycle with arrows indicating its path. Is the cycle traveling in a clockwise or counterclockwise direction? Choose between 'clockwise' and 'counterclockwise'.",
                "<1>"
            ]
        ],
        "orientation_4": [
            [
                "In the image, <2> arrows are on a circle. Are they pointing clockwise or counterclockwise? Choose one from ‘clockwise’ and ‘counterclockwise’.",
                "<1>"
            ],
            [
                "The image shows <2> arrows arranged around a circle. Are these arrows directed clockwise or counterclockwise? Select 'clockwise' or 'counterclockwise'.",
                "<1>"
            ],
            [
                "There are <2> arrows placed on a circular path in the image. Are the arrows pointing in a clockwise or counterclockwise direction? Choose 'clockwise' or 'counterclockwise'.",
                "<1>"
            ],
            [
                "Examine the circle in the image with <2> arrows. Do these arrows point clockwise or counterclockwise? Answer with 'clockwise' or 'counterclockwise'.",
                "<1>"
            ],
            [
                "In the provided image, <2> arrows are arranged on a circle. Determine if they are pointing clockwise or counterclockwise. Choose 'clockwise' or 'counterclockwise'.",
                "<1>"
            ]
        ],
        "orientation_5": [
            [
                "In the image, there are four arrows <2>, <3>, <4>, and <5> on a circle. Among <2>, <3>, <4>, and <5>, all except one are pointing <1>. Answer the one arrow that is not rotating the circle <1>, with a letter denoting the arrow.",
                "<6>"
            ],
            [
                "The image displays four arrows labeled <2>, <3>, <4>, and <5> arranged on a circle. All arrows except one are pointing <1>. Identify the arrow that is not rotating the circle <1> by providing its letter.",
                "<6>"
            ],
            [
                "On the circular arrangement in the image, there are arrows <2>, <3>, <4>, and <5>. All but one arrow are directed <1>. Which arrow is not contributing to the circle's <1> rotation? Provide the arrow's letter.",
                "<6>"
            ],
            [
                "There are four arrows labeled <2>, <3>, <4>, and <5> on a circle in the image. Except for one, all arrows point <1>. Which arrow does not rotate the circle <1>? Answer with the corresponding letter.",
                "<6>"
            ],
            [
                "In the provided image, four arrows <2>, <3>, <4>, and <5> are positioned on a circle. All arrows except one are pointing <1>. Identify the arrow that isn't rotating the circle <1> by its letter.",
                "<6>"
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