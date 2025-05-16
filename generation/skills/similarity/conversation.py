from .rules import *

import random


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
    "similarity_1": [
        [
            "Among <2>, <3>, <4>, and <5>, which triangle is not similar to the rest, while the others are similar to each other?",
            "<1> is not similar to the other triangles, while the rest are similar to each other."
        ],
        [
            "Which triangle, among <2>, <3>, <4>, and <5>, is not similar to the rest, where the others share similarity?",
            "<1> is not similar to the other triangles, while the others share similarity."
        ],
        [
            "From <2>, <3>, <4>, and <5>, identify the triangle that is not similar to the rest, while the others are mutually similar.",
            "<1> is not similar to the other triangles, while the others are mutually similar."
        ],
        [
            "Among the triangles <2>, <3>, <4>, and <5>, which one is not similar, while the others are similar to each other?",
            "<1> is not similar to the other triangles, while the others are similar to each other."
        ],
        [
            "Which triangle among <2>, <3>, <4>, and <5> lacks similarity with the rest, while the remaining triangles are similar?",
            "<1> is not similar to the other triangles, while the remaining ones are similar."
        ],
        [
            "Out of the triangles <2>, <3>, <4>, and <5>, which one stands out as not similar, with the others being similar to each other?",
            "<1> is not similar to the other triangles, while the others are similar to each other."
        ],
        [
            "Which of the triangles <2>, <3>, <4>, and <5> is not similar to the rest, while the others share mutual similarity?",
            "<1> is not similar to the other triangles, while the others share mutual similarity."
        ],
        [
            "From <2>, <3>, <4>, and <5>, which triangle is different in similarity, while the others are similar to each other?",
            "<1> is not similar to the other triangles, while the others are similar to each other."
        ],
        [
            "Identify the triangle among <2>, <3>, <4>, and <5> that is not similar to the rest, while the remaining triangles are similar.",
            "<1> is not similar to the other triangles, while the remaining triangles are similar."
        ],
        [
            "Among the triangles <2>, <3>, <4>, and <5>, which one differs in similarity, while the rest share similarity with each other?",
            "<1> is not similar to the other triangles, while the rest share similarity with each other."
        ]
    ],
    "similarity_2": [
        [
            "There are 4 shapes <1>, <2>, <3>, and <4> in the image. There is a similar shape pair in the image. What is that? Write the pair of labels in lexicographical order. For example, if X and Y shapes are similar, your answer should be “X, Y.”",
            "The similar pair of shapes are “<5>.”"
        ],
        [
            "In the image, four shapes labeled <1>, <2>, <3>, and <4> are present. Identify the pair of shapes that are similar. Provide your answer as a pair of labels in alphabetical order, such as “X, Y.”",
            "The similar pair of shapes are “<5>.”"
        ],
        [
            "Among the four shapes <1>, <2>, <3>, and <4> displayed in the image, there exists a pair that is similar. Which pair is it? Respond with the labels in alphabetical order, for instance, “X, Y.”",
            "The similar pair of shapes are “<5>.”"
        ],
        [
            "The image showcases four shapes labeled <1>, <2>, <3>, and <4>. There is one pair of shapes that are similar. Which pair is it? Enter your answer as two labels in order, such as “X, Y.”",
            "The similar pair of shapes are “<5>.”"
        ],
        [
            "Within the image, there are four shapes marked as <1>, <2>, <3>, and <4>. Identify the two shapes that form a similar pair. Provide your answer using their labels in alphabetical order, like “X, Y.”",
            "The similar pair of shapes are “<5>.”"
        ]
    ],
    "similarity_3": [
        [
            "In the image, there are 4 shapes with labels <1>, <2>, <3>, and <4>. Three of them are similar and one of them is not. Which is not similar to the other shapes? Tell me the label indicating that shape. You should choose your answer from <1>, <2>, <3>, and <4>.",
            "The shape labeled “<5>” is not similar to the others."
        ],
        [
            "There are four shapes in the image labeled <1>, <2>, <3>, and <4>. Three shapes share similarity, while one does not. Which shape is the outlier in terms of similarity? Provide the corresponding label from <1>, <2>, <3>, or <4>.",
            "The shape labeled “<5>” is the one that is not similar to the others."
        ],
        [
            "Within the image, four shapes are marked as <1>, <2>, <3>, and <4>. Identify the shape that does not share similarity with the rest. Choose the label of that shape from <1>, <2>, <3>, or <4>.",
            "The shape labeled “<5>” does not share similarity with the other shapes."
        ],
        [
            "In the provided image, there are four shapes labeled <1>, <2>, <3>, and <4>. Out of these, three are similar, and one is different. Which shape is the different one? Select the label from <1>, <2>, <3>, or <4>.",
            "The different shape is labeled “<5>”."
        ],
        [
            "The image contains four shapes labeled <1>, <2>, <3>, and <4>. Three shapes are similar, but one lacks similarity. Which shape lacks similarity? Indicate your answer by its label from <1>, <2>, <3>, or <4>.",
            "The shape labeled “<5>” lacks similarity with the others."
        ]
    ],
    "similarity_4": [
        [
            "There are five <1>s in the image. Choose the shape that is geometrically similar to the leftmost <1>. What is the number indicating that shape? Your answer should be “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The shape similar to the leftmost <1> is “<6>”."
        ],
        [
            "In the image, five instances of <1> are present. Identify which shape is geometrically similar to the first <1> on the left. Provide the number corresponding to that shape as “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The shape similar to the first <1> is “<6>”."
        ],
        [
            "The image displays five <1>s. Determine which shape matches geometrically with the leftmost <1>. What is the label number of that shape? Choose from “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The matching shape is “<6>”."
        ],
        [
            "Among the five <1>s shown in the image, select the one that is geometrically similar to the leftmost <1>. What number corresponds to that shape? Your options are “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The geometrically similar shape is “<6>”."
        ],
        [
            "In the provided image, there are five shapes labeled as <1>. Identify which shape is geometrically similar to the leftmost <1>. Provide the number of that shape from “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The geometrically similar shape is “<6>”."
        ]
    ],
    "similarity_5": [
        [
            "There are five <1>s in the image. Choose the shape that is not geometrically similar to the leftmost <1>. What is the number indicating that shape? Your answer should be “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The shape not similar to the leftmost <1> is “<6>”."
        ],
        [
            "In the image, five instances of <1> are present. Identify which shape is not geometrically similar to the first <1> on the left. Provide the number corresponding to that shape as “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The shape that is not similar to the first <1> is “<6>”."
        ],
        [
            "The image displays five <1>s. Determine which shape does not match geometrically with the leftmost <1>. What is the label number of that shape? Choose from “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The non-similar shape is “<6>”."
        ],
        [
            "Among the five <1>s shown in the image, select the one that is not geometrically similar to the leftmost <1>. What number corresponds to that shape? Your options are “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The non-geometrically similar shape is “<6>”."
        ],
        [
            "In the provided image, there are five shapes labeled as <1>. Identify which shape is not geometrically similar to the leftmost <1>. Provide the number of that shape from “<2>”, “<3>”, “<4>”, or “<5>”.",
            "The shape not geometrically similar to the leftmost <1> is “<6>”."
        ]
    ],
    "similarity_6": [
        [
            "In the image, there are three pairs of shapes: \"<1>\", \"<2>\", and \"<3>\". Among these pairs, choose the pair that is in the similarity relationship (in the sense of geometry). Choose your answer from “<1>”, “<2>”, and “<3>”.",
            "The answer is “<4>”."
        ],
        [
            "The image presents three pairs of shapes: \"<1>\", \"<2>\", and \"<3>\". Identify which pair exhibits a similarity relationship based on geometry. Select your answer from “<1>”, “<2>”, or “<3>”.",
            "The correct pair is “<4>”."
        ],
        [
            "There are three pairs of shapes in the image labeled \"<1>\", \"<2>\", and \"<3>\". Determine which pair has a similarity relationship geometrically. Your answer should be one of “<1>”, “<2>”, or “<3>”.",
            "The geometrically similar pair is “<4>”."
        ],
        [
            "Within the image, three shape pairs are shown: \"<1>\", \"<2>\", and \"<3>\". Which of these pairs shares a similarity relationship in terms of geometry? Choose from “<1>”, “<2>”, or “<3>”.",
            "The pair that shares similarity is “<4>”."
        ],
        [
            "The provided image contains three pairs of shapes: \"<1>\", \"<2>\", and \"<3>\". Select the pair that demonstrates a similarity relationship geometrically. Your options are “<1>”, “<2>”, or “<3>”.",
            "The similar pair is “<4>”."
        ]
    ]
}
conversation_caption = {
    "similarity_1": [
        [
            "",
            "Among <2>, <3>, <4>, and <5>, <1> is not similar to the other triangles, while the others are similar to each other."
        ],
        [
            "",
            "Which triangle, among <2>, <3>, <4>, and <5>, is not similar to the rest, where the others share similarity? <1> is not similar to the other triangles, while the others share similarity."
        ],
        [
            "",
            "From <2>, <3>, <4>, and <5>, identify the triangle that is not similar to the rest, while the others are mutually similar. <1> is not similar to the other triangles, while the others are mutually similar."
        ],
        [
            "",
            "Among the triangles <2>, <3>, <4>, and <5>, <1> is not similar to the other triangles, while the others are similar to each other."
        ],
        [
            "",
            "Which triangle among <2>, <3>, <4>, and <5> lacks similarity with the rest, while the remaining triangles are similar? <1> is not similar to the other triangles, while the remaining ones are similar."
        ],
        [
            "",
            "Out of the triangles <2>, <3>, <4>, and <5>, <1> is not similar to the other triangles, while the others are similar to each other."
        ],
        [
            "",
            "Which of the triangles <2>, <3>, <4>, and <5> is not similar to the rest, while the others share mutual similarity? <1> is not similar to the other triangles, while the others share mutual similarity."
        ],
        [
            "",
            "From <2>, <3>, <4>, and <5>, <1> is not similar to the other triangles, while the others are similar to each other."
        ],
        [
            "",
            "Identify the triangle among <2>, <3>, <4>, and <5> that is not similar to the rest, while the remaining triangles are similar. <1> is not similar to the other triangles, while the remaining triangles are similar."
        ],
        [
            "",
            "Among the triangles <2>, <3>, <4>, and <5>, <1> is not similar to the other triangles, while the rest share similarity with each other."
        ]
    ],
    "similarity_2": [
        [
            "",
            "There are 4 shapes <1>, <2>, <3>, and <4> in the image. Among these, the similar pair of shapes are \"<5>\"."
        ],
        [
            "",
            "In the image, four shapes labeled <1>, <2>, <3>, and <4> are present. The similar pair of shapes are \"<5>\"."
        ],
        [
            "",
            "Among the four shapes <1>, <2>, <3>, and <4> displayed in the image, the similar pair of shapes are \"<5>\"."
        ],
        [
            "",
            "The image showcases four shapes labeled <1>, <2>, <3>, and <4>. The similar pair of shapes are \"<5>\"."
        ],
        [
            "",
            "Within the image, there are four shapes marked as <1>, <2>, <3>, and <4>. The similar pair of shapes are \"<5>\"."
        ]
    ],
    "similarity_3": [
        [
            "",
            "In the image, there are 4 shapes with labels <1>, <2>, <3>, and <4>. The shape labeled \"<5>\" is not similar to the others."
        ],
        [
            "",
            "There are four shapes in the image labeled <1>, <2>, <3>, and <4>. The shape labeled \"<5>\" is the one that is not similar to the others."
        ],
        [
            "",
            "Within the image, four shapes are marked as <1>, <2>, <3>, and <4>. The shape labeled \"<5>\" does not share similarity with the other shapes."
        ],
        [
            "",
            "In the provided image, there are four shapes labeled <1>, <2>, <3>, and <4>. The different shape is labeled \"<5>\"."
        ],
        [
            "",
            "The image contains four shapes labeled <1>, <2>, <3>, and <4>. The shape labeled \"<5>\" lacks similarity with the others."
        ]
    ],
    "similarity_4": [
        [
            "",
            "In the image, five instances of <1> are present. The shape similar to the leftmost <1> is \"<6>\"."
        ]
    ],
    "similarity_5": [
        [
            "",
            "In the image, five instances of <1> are present. The shape not similar to the leftmost <1> is \"<6>\"."
        ]
    ],
    "similarity_6": [
        [
            "",
            "In the image, three pairs of shapes are shown: \"<1>\", \"<2>\", and \"<3>\". The pair that shares similarity is \"<4>\"."
        ]
    ]
}


conversation_short = {
    "similarity_1": [
        [
            "Among <2>, <3>, <4>, and <5>, which triangle is not similar to the rest, while the others are similar to each other?",
            "<1>"
        ],
        [
            "Which triangle, among <2>, <3>, <4>, and <5>, is not similar to the rest, where the others share similarity?",
            "<1>"
        ],
        [
            "From <2>, <3>, <4>, and <5>, identify the triangle that is not similar to the rest, while the others are mutually similar.",
            "<1>"
        ],
        [
            "Among the triangles <2>, <3>, <4>, and <5>, which one is not similar, while the others are similar to each other?",
            "<1>"
        ],
        [
            "Which triangle among <2>, <3>, <4>, and <5> lacks similarity with the rest, while the remaining triangles are similar?",
            "<1>"
        ],
        [
            "Out of the triangles <2>, <3>, <4>, and <5>, which one stands out as not similar, with the others being similar to each other?",
            "<1>"
        ],
        [
            "Which of the triangles <2>, <3>, <4>, and <5> is not similar to the rest, while the others share mutual similarity?",
            "<1>"
        ],
        [
            "From <2>, <3>, <4>, and <5>, which triangle is different in similarity, while the others are similar to each other?",
            "<1>"
        ],
        [
            "Identify the triangle among <2>, <3>, <4>, and <5> that is not similar to the rest, while the remaining triangles are similar.",
            "<1>"
        ],
        [
            "Among the triangles <2>, <3>, <4>, and <5>, which one differs in similarity, while the rest share similarity with each other?",
            "<1>"
        ]
    ],
    "similarity_2": [
        [
            "There are 4 shapes <1>, <2>, <3>, and <4> in the image. There is a similar shape pair in the image. What is that? Write the pair of labels in lexicographical order. For example, if X and Y shapes are similar, your answer should be “X, Y.”",
            "<5>"
        ],
        [
            "In the image, four shapes labeled <1>, <2>, <3>, and <4> are present. Identify the pair of shapes that are similar. Provide your answer as a pair of labels in alphabetical order, such as “X, Y.”",
            "<5>"
        ],
        [
            "Among the four shapes <1>, <2>, <3>, and <4> displayed in the image, there exists a pair that is similar. Which pair is it? Respond with the labels in alphabetical order, for instance, “X, Y.”",
            "<5>"
        ],
        [
            "The image showcases four shapes labeled <1>, <2>, <3>, and <4>. There is one pair of shapes that are similar. Which pair is it? Enter your answer as two labels in order, such as “X, Y.”",
            "<5>"
        ],
        [
            "Within the image, there are four shapes marked as <1>, <2>, <3>, and <4>. Identify the two shapes that form a similar pair. Provide your answer using their labels in alphabetical order, like “X, Y.”",
            "<5>"
        ]
    ],
    "similarity_3": [
        [
            "In the image, there are 4 shapes with labels <1>, <2>, <3>, and <4>. Three of them are similar and one of them is not. Which is not similar to the other shapes? Tell me the label indicating that shape. You should choose your answer from <1>, <2>, <3>, and <4>.",
            "<5>"
        ],
        [
            "There are four shapes in the image labeled <1>, <2>, <3>, and <4>. Three shapes share similarity, while one does not. Which shape is the outlier in terms of similarity? Provide the corresponding label from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Within the image, four shapes are marked as <1>, <2>, <3>, and <4>. Identify the shape that does not share similarity with the rest. Choose the label of that shape from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "In the provided image, there are four shapes labeled <1>, <2>, <3>, and <4>. Out of these, three are similar, and one is different. Which shape is the different one? Select the label from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "The image contains four shapes labeled <1>, <2>, <3>, and <4>. Three shapes are similar, but one lacks similarity. Which shape lacks similarity? Indicate your answer by its label from <1>, <2>, <3>, or <4>.",
            "<5>"
        ]
    ],
    "similarity_4": [
        [
            "There are five <1>s in the image. Choose the shape that is geometrically similar to the leftmost <1>. What is the number indicating that shape? Your answer should be “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ],
        [
            "In the image, five instances of <1> are present. Identify which shape is geometrically similar to the first <1> on the left. Provide the number corresponding to that shape as “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ],
        [
            "The image displays five <1>s. Determine which shape matches geometrically with the leftmost <1>. What is the label number of that shape? Choose from “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ],
        [
            "Among the five <1>s shown in the image, select the one that is geometrically similar to the leftmost <1>. What number corresponds to that shape? Your options are “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ],
        [
            "In the provided image, there are five shapes labeled as <1>. Identify which shape is geometrically similar to the leftmost <1>. Provide the number of that shape from “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ]
    ],
    "similarity_5": [
        [
            "There are five <1>s in the image. Choose the shape that is not geometrically similar to the leftmost <1>. What is the number indicating that shape? Your answer should be “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ],
        [
            "In the image, five instances of <1> are present. Identify which shape is not geometrically similar to the first <1> on the left. Provide the number corresponding to that shape as “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ],
        [
            "The image displays five <1>s. Determine which shape does not match geometrically with the leftmost <1>. What is the label number of that shape? Choose from “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ],
        [
            "Among the five <1>s shown in the image, select the one that is not geometrically similar to the leftmost <1>. What number corresponds to that shape? Your options are “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ],
        [
            "In the provided image, there are five shapes labeled as <1>. Identify which shape is not geometrically similar to the leftmost <1>. Provide the number of that shape from “<2>”, “<3>”, “<4>”, or “<5>”.",
            "<6>"
        ]
    ],
    "similarity_6": [
        [
            "In the image, there are three pairs of shapes: \"<1>\", \"<2>\", and \"<3>\". Among these pairs, choose the pair that is in the similarity relationship (in the sense of geometry). Choose your answer from “<1>”, “<2>”, and “<3>”.",
            "<4>"
        ],
        [
            "The image presents three pairs of shapes: \"<1>\", \"<2>\", and \"<3>\". Identify which pair exhibits a similarity relationship based on geometry. Select your answer from “<1>”, “<2>”, or “<3>”.",
            "<4>"
        ],
        [
            "There are three pairs of shapes in the image labeled \"<1>\", \"<2>\", and \"<3>\". Determine which pair has a similarity relationship geometrically. Your answer should be one of “<1>”, “<2>”, or “<3>”.",
            "<4>"
        ],
        [
            "Within the image, three shape pairs are shown: \"<1>\", \"<2>\", and \"<3>\". Which of these pairs shares a similarity relationship in terms of geometry? Choose from “<1>”, “<2>”, or “<3>”.",
            "<4>"
        ],
        [
            "The provided image contains three pairs of shapes: \"<1>\", \"<2>\", and \"<3>\". Select the pair that demonstrates a similarity relationship geometrically. Your options are “<1>”, “<2>”, or “<3>”.",
            "<4>"
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