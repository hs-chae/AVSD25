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
  "rotational_symmetry_1" : [
    [
        "Two triangles <1> and <2> in the image are in a point-symmetric relation (that is, 2-fold rotational symmetry in 2D). Among points <3>, <4>, <5>, <6>, and <7>, which point is most likely to be the center of symmetry?",
        "Point <8> is most likely to be the center of symmetry."
    ],
    [
        "In the image, triangles <1> and <2> exhibit a point-symmetric relationship (2-fold rotational symmetry in 2D). Which point among <3>, <4>, <5>, <6>, and <7> is most likely the symmetry center?",
        "Point <8> is most likely the symmetry center."
    ],
    [
        "Which point, out of <3>, <4>, <5>, <6>, and <7>, is most likely the center of 2-fold rotational symmetry between triangles <1> and <2> in the image?",
        "Point <8> is most likely the center of 2-fold rotational symmetry."
    ],
    [
        "Among the points <3>, <4>, <5>, <6>, and <7>, which one is most likely the center of the point-symmetric relation (2-fold rotational symmetry) between triangles <1> and <2> in the image?",
        "Point <8> is most likely the center of the symmetry."
    ],
    [
        "In the image, triangles <1> and <2> share a point-symmetric relationship. Which point among <3>, <4>, <5>, <6>, and <7> is most likely to be the point of symmetry?",
        "Point <8> is most likely to be the point of symmetry."
    ],
    [
        "From the points <3>, <4>, <5>, <6>, and <7>, which one is most likely the center of 2-fold rotational symmetry connecting triangles <1> and <2> in the image?",
        "Point <8> is most likely the center of the rotational symmetry."
    ],
    [
        "Which of the points <3>, <4>, <5>, <6>, and <7> is most likely the symmetry center for the point-symmetric (2-fold rotational) relationship between triangles <1> and <2>?",
        "Point <8> is most likely the symmetry center."
    ],
    [
        "Identify the point among <3>, <4>, <5>, <6>, and <7> that is most likely the center of symmetry for triangles <1> and <2>, which are in a point-symmetric relationship.",
        "Point <8> is most likely the center of symmetry."
    ],
    [
        "Which point, from <3>, <4>, <5>, <6>, and <7>, is most likely the point of symmetry for the 2-fold rotational symmetry between triangles <1> and <2>?",
        "Point <8> is most likely the point of symmetry."
    ],
    [
        "Among <3>, <4>, <5>, <6>, and <7>, which point is most likely the center of the point-symmetric relationship (2-fold rotational symmetry) of triangles <1> and <2>?",
        "Point <8> is most likely the center of the point-symmetric relationship."
    ]
],
  "rotational_symmetry_2": [
    [
      "The image contains a <1> that has rotational symmetry about a certain point. Identify the point that can serve as the center of this symmetry and state its label (<2>, <3>, <4>, or <5>). For example, if point X is the center, respond with \"X\".",
      "The rotational symmetry is centered at <6>."
    ],
    [
      "Within the image, a <1> exhibits symmetry around a specific point. Specify the label (<2>, <3>, <4>, or <5>) for the center of this symmetry. For instance, if the point is X, your response should be \"X\".",
      "Point <6> acts as the rotational center of symmetry."
    ],
    [
      "You can observe a <1> in the image, which is symmetric around some point. Indicate the point's label (<2>, <3>, <4>, or <5>). If the center is labeled as X, answer \"X\".",
      "The center of the rotational symmetry is labeled <6>."
    ],
    [
      "The image shows a <1> that is symmetric with respect to rotation about a certain point. Select the correct label (<2>, <3>, <4>, or <5>) for this center. Example: If it is point X, answer \"X\".",
      "Rotational symmetry is centered at point <6>."
    ],
    [
      "A <1> in the image demonstrates rotational symmetry around a point. Identify the center of this symmetry by its label (<2>, <3>, <4>, or <5>). For instance, if X is the center, respond with \"X\".",
      "Point <6> is the rotational symmetry center."
    ]
  ],
  "rotational_symmetry_3": [
    [
      "In the image, a <1> is symmetric around a point. Identify the color of the point (<2>, <3>, <4>, or <5>) that serves as the symmetry center. For example, if the center is black, your answer should be \"black\".",
      "The symmetry center is marked by the color <6>."
    ],
    [
      "A <1> in the image exhibits rotational symmetry around a central point. Name the color (<2>, <3>, <4>, or <5>) of the point serving as the symmetry center. Example: If the center is black, respond \"black\".",
      "The point with color <6> represents the center of symmetry."
    ],
    [
      "The image shows a <1> symmetric around some point. Specify the color (<2>, <3>, <4>, or <5>) of this point. For instance, if the center is black, answer \"black\".",
      "The color <6> identifies the rotational symmetry center."
    ],
    [
      "There is a <1> in the image that is symmetric with respect to some point. Choose the color (<2>, <3>, <4>, or <5>) of the center point. For example, if the center is black, answer \"black\".",
      "The center of symmetry corresponds to the color <6>."
    ],
    [
      "Within the image, a <1> is symmetric around a specific point. Indicate the color (<2>, <3>, <4>, or <5>) of the center of this symmetry. For instance, if black is the center, respond \"black\".",
      "The rotational symmetry center is colored <6>."
    ]
  ],
  "rotational_symmetry_4": [
    [
      "Between shapes <2> and <3>, which one most likely possesses <1>-fold rotational symmetry? That is, which shape retains its appearance after a 90-degree rotation about a point? The answer should be a single number.",
      "The shape labeled <4> most likely exhibits <1>-fold rotational symmetry."
    ],
    [
      "Consider shapes labeled <2> and <3>. Which shape is most likely to exhibit <1>-fold rotational symmetry? In other words, which one looks identical when rotated 90 degrees? Provide a single number as your answer.",
      "The shape with the label <4> has <1>-fold rotational symmetry."
    ],
    [
      "Out of the shapes labeled as <2> and <3>, which one is most likely to possess <1>-fold rotational symmetry? Answer with a single number.",
      "Shape <4> is the one most likely to display <1>-fold symmetry."
    ],
    [
      "Among shapes <2> and <3>, which is the best candidate for <1>-fold rotational symmetry? In other words, which shape would appear identical after a 90-degree rotation? Respond with one number.",
      "The shape labeled <4> likely has <1>-fold rotational symmetry."
    ],
    [
      "Choose between shapes labeled <2> and <3>: which one most likely has <1>-fold rotational symmetry? The answer must be a single number.",
      "Label <4> is associated with <1>-fold rotational symmetry."
    ]
  ],
  "rotational_symmetry_4_1": [
    [
      "In this figure, numbered shapes are shown, including <1> and 'Rotated <1>.' Identify which shape among these numbers is most likely to exhibit 4-fold rotational symmetry. Recall that 'Rotated <1>' represents a 90-degree rotation of shape <1>. Your answer should be a single number.",
      "The shape labeled <2> likely possesses 4-fold rotational symmetry."
    ],
    [
      "The figure displays shapes labeled with numbers, including <1> and 'Rotated <1>.' Among these, which shape has 4-fold rotational symmetry? Recall that 'Rotated <1>' shows the 90-degree rotation of <1>. Your answer should be one number.",
      "Shape <2> most likely has 4-fold rotational symmetry."
    ],
    [
      "Examine the labeled shapes in the figure, including <1> and 'Rotated <1>.' Determine which numbered shape exhibits 4-fold rotational symmetry. Note: 'Rotated <1>' illustrates a 90-degree rotation of shape <1>. Provide a single number as your answer.",
      "The 4-fold rotational symmetry is most likely found in shape <2>."
    ],
    [
      "Within the image, numbered shapes such as <1> and 'Rotated <1>' are presented. Identify the shape with 4-fold rotational symmetry. Remember, 'Rotated <1>' depicts a 90-degree rotation of shape <1>. Provide a single-number response.",
      "Shape labeled <2> demonstrates 4-fold rotational symmetry."
    ],
    [
      "Among the shapes numbered <1> and their rotations, determine which one exhibits 4-fold rotational symmetry. 'Rotated <1>' corresponds to a 90-degree rotation of shape <1>. Provide your answer as a single number.",
      "The rotational symmetry is most evident in shape <2>."
    ]
  ],
  "rotational_symmetry_5": [
    [
      "In the image, consider the shapes <2>, <3>, and <4>. Which of these shapes is symmetric to the <1> shape with respect to a point rather than a line? Select one and write: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to a point not shown in the image.",
      "The shape <5> is symmetric to <1> about a point."
    ],
    [
      "Among shapes <2>, <3>, and <4> in the figure, identify which one is symmetric with the <1> shape concerning a point, not a line. Write your final answer as: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to a point not visible in the image.",
      "The <5> shape is symmetric to the <1> shape with repect to a point not visible in the image."
    ],
    [
      "From the shapes labeled <2>, <3>, and <4>, choose the one symmetric to <1> concerning a point (not a line). Respond as: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to an unseen point.",
      "Symmetry to a point exists between <1> and <5>."
    ],
    [
      "Examine the shapes labeled <2>, <3>, and <4>. Which is symmetric to the <1> shape with respect to a point rather than a line? Your answer should be in the form: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to an unseen point.",
      "The <5> shape is point-symmetric to the <1> shape."
    ],
    [
      "Among the shapes <2>, <3>, and <4>, identify which is symmetric to the <1> shape with respect to a point (not a line). Write your answer as: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to a point not visible in the image.",
      "Shape <5> exhibits point symmetry with <1>."
    ]
  ]
}
conversation_caption = {
  "rotational_symmetry_1": [
    [
      "",
      "In the image, triangles <1> and <2> exhibit a point-symmetric relationship (2-fold rotational symmetry in 2D). Among points <3>, <4>, <5>, <6>, and <7>, point <8> is most likely the center of symmetry."
    ]
  ],
  "rotational_symmetry_2": [
    [
      "",
      "In the image, a <1> has rotational symmetry about a certain point. Among the points labeled <2>, <3>, <4>, and <5>, point <6> is the center of this symmetry."
    ]
  ],
  "rotational_symmetry_3": [
    [
      "",
      "In the image, a <1> is symmetric around a point. Among the colors <2>, <3>, <4>, and <5>, the symmetry center is marked by the color <6>."
    ]
  ],
  "rotational_symmetry_4": [
    [
      "",
      "Between shapes <2> and <3>, the shape labeled <4> most likely exhibits <1>-fold rotational symmetry, meaning it retains its appearance after a 90-degree rotation about a point."
    ]
  ],
  "rotational_symmetry_4_1": [
    [
      "",
      "In the image, numbered shapes are shown, including <1> and 'Rotated <1>.' Among these, the shape labeled <2> likely possesses 4-fold rotational symmetry. 'Rotated <1>' represents a 90-degree rotation of shape <1>."
    ]
  ],
  "rotational_symmetry_5": [
    [
      "",
      "In the image, among the shapes <2>, <3>, and <4>, the shape labeled <5> is symmetric to the <1> shape with respect to a point rather than a line."
    ]
  ]
}
conversation_short = {
  "rotational_symmetry_1" : [
    [
        "Two triangles <1> and <2> in the image are in a point-symmetric relation (that is, 2-fold rotational symmetry in 2D). Among points <3>, <4>, <5>, <6>, and <7>, which point is most likely to be the center of symmetry?",
        "<8>"
    ],
    [
        "In the image, triangles <1> and <2> exhibit a point-symmetric relationship (2-fold rotational symmetry in 2D). Which point among <3>, <4>, <5>, <6>, and <7> is most likely the symmetry center?",
        "<8>"
    ],
    [
        "Which point, out of <3>, <4>, <5>, <6>, and <7>, is most likely the center of 2-fold rotational symmetry between triangles <1> and <2> in the image?",
        "<8>"
    ],
    [
        "Among the points <3>, <4>, <5>, <6>, and <7>, which one is most likely the center of the point-symmetric relation (2-fold rotational symmetry) between triangles <1> and <2> in the image?",
        "<8>"
    ],
    [
        "In the image, triangles <1> and <2> share a point-symmetric relationship. Which point among <3>, <4>, <5>, <6>, and <7> is most likely to be the point of symmetry?",
        "<8>"
    ],
    [
        "From the points <3>, <4>, <5>, <6>, and <7>, which one is most likely the center of 2-fold rotational symmetry connecting triangles <1> and <2> in the image?",
        "<8>"
    ],
    [
        "Which of the points <3>, <4>, <5>, <6>, and <7> is most likely the symmetry center for the point-symmetric (2-fold rotational) relationship between triangles <1> and <2>?",
        "<8>"
    ],
    [
        "Identify the point among <3>, <4>, <5>, <6>, and <7> that is most likely the center of symmetry for triangles <1> and <2>, which are in a point-symmetric relationship.",
        "<8>"
    ],
    [
        "Which point, from <3>, <4>, <5>, <6>, and <7>, is most likely the point of symmetry for the 2-fold rotational symmetry between triangles <1> and <2>?",
        "<8>"
    ],
    [
        "Among <3>, <4>, <5>, <6>, and <7>, which point is most likely the center of the point-symmetric relationship (2-fold rotational symmetry) of triangles <1> and <2>?",
        "<8>"
    ]
],
  "rotational_symmetry_2": [
    [
      "The image contains a <1> that has rotational symmetry about a certain point. Identify the point that can serve as the center of this symmetry and state its label (<2>, <3>, <4>, or <5>). For example, if point X is the center, respond with \"X\".",
      "<6>"
    ],
    [
      "Within the image, a <1> exhibits symmetry around a specific point. Specify the label (<2>, <3>, <4>, or <5>) for the center of this symmetry. For instance, if the point is X, your response should be \"X\".",
      "<6>"
    ],
    [
      "You can observe a <1> in the image, which is symmetric around some point. Indicate the point's label (<2>, <3>, <4>, or <5>). If the center is labeled as X, answer \"X\".",
      "<6>"
    ],
    [
      "The image shows a <1> that is symmetric with respect to rotation about a certain point. Select the correct label (<2>, <3>, <4>, or <5>) for this center. Example: If it is point X, answer \"X\".",
      "<6>"
    ],
    [
      "A <1> in the image demonstrates rotational symmetry around a point. Identify the center of this symmetry by its label (<2>, <3>, <4>, or <5>). For instance, if X is the center, respond with \"X\".",
      "<6>"
    ]
  ],
  "rotational_symmetry_3": [
    [
      "In the image, a <1> is symmetric around a point. Identify the color of the point (<2>, <3>, <4>, or <5>) that serves as the symmetry center. For example, if the center is black, your answer should be \"black\".",
      "<6>"
    ],
    [
      "A <1> in the image exhibits rotational symmetry around a central point. Name the color (<2>, <3>, <4>, or <5>) of the point serving as the symmetry center. Example: If the center is black, respond \"black\".",
      "<6>"
    ],
    [
      "The image shows a <1> symmetric around some point. Specify the color (<2>, <3>, <4>, or <5>) of this point. For instance, if the center is black, answer \"black\".",
      "<6>"
    ],
    [
      "There is a <1> in the image that is symmetric with respect to some point. Choose the color (<2>, <3>, <4>, or <5>) of the center point. For example, if the center is black, answer \"black\".",
      "<6>"
    ],
    [
      "Within the image, a <1> is symmetric around a specific point. Indicate the color (<2>, <3>, <4>, or <5>) of the center of this symmetry. For instance, if black is the center, respond \"black\".",
      "<6>"
    ]
  ],
  "rotational_symmetry_4": [
    [
      "Between shapes <2> and <3>, which one most likely possesses <1>-fold rotational symmetry? That is, which shape retains its appearance after a 90-degree rotation about a point? The answer should be a single number.",
      "<4>"
    ],
    [
      "Consider shapes labeled <2> and <3>. Which shape is most likely to exhibit <1>-fold rotational symmetry? In other words, which one looks identical when rotated 90 degrees? Provide a single number as your answer.",
      "<4>"
    ],
    [
      "Out of the shapes labeled as <2> and <3>, which one is most likely to possess <1>-fold rotational symmetry? Answer with a single number.",
      "<4>"
    ],
    [
      "Among shapes <2> and <3>, which is the best candidate for <1>-fold rotational symmetry? In other words, which shape would appear identical after a 90-degree rotation? Respond with one number.",
      "<4>"
    ],
    [
      "Choose between shapes labeled <2> and <3>: which one most likely has <1>-fold rotational symmetry? The answer must be a single number.",
      "<4>"
    ]
  ],
  "rotational_symmetry_4_1": [
    [
      "In this figure, numbered shapes are shown, including <1> and 'Rotated <1>.' Identify which shape among these numbers is most likely to exhibit 4-fold rotational symmetry. Recall that 'Rotated <1>' represents a 90-degree rotation of shape <1>. Your answer should be a single number.",
      "<2>"
    ],
    [
      "The figure displays shapes labeled with numbers, including <1> and 'Rotated <1>.' Among these, which shape has 4-fold rotational symmetry? Recall that 'Rotated <1>' shows the 90-degree rotation of <1>. Your answer should be one number.",
      "<2>"
    ],
    [
      "Examine the labeled shapes in the figure, including <1> and 'Rotated <1>.' Determine which numbered shape exhibits 4-fold rotational symmetry. Note: 'Rotated <1>' illustrates a 90-degree rotation of shape <1>. Provide a single number as your answer.",
      "<2>"
    ],
    [
      "Within the image, numbered shapes such as <1> and 'Rotated <1>' are presented. Identify the shape with 4-fold rotational symmetry. Remember, 'Rotated <1>' depicts a 90-degree rotation of shape <1>. Provide a single-number response.",
      "<2>"
    ],
    [
      "Among the shapes numbered <1> and their rotations, determine which one exhibits 4-fold rotational symmetry. 'Rotated <1>' corresponds to a 90-degree rotation of shape <1>. Provide your answer as a single number.",
      "<2>"
    ]
  ],
  "rotational_symmetry_5": [
    [
      "In the image, consider the shapes <2>, <3>, and <4>. Which of these shapes is symmetric to the <1> shape with respect to a point rather than a line? Select one and write: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to a point not shown in the image.",
      "<5>"
    ],
    [
      "Among shapes <2>, <3>, and <4> in the figure, identify which one is symmetric with the <1> shape concerning a point, not a line. Write your final answer as: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to a point not visible in the image.",
      "<5>"
    ],
    [
      "From the shapes labeled <2>, <3>, and <4>, choose the one symmetric to <1> concerning a point (not a line). Respond as: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to an unseen point.",
      "<5>"
    ],
    [
      "Examine the shapes labeled <2>, <3>, and <4>. Which is symmetric to the <1> shape with respect to a point rather than a line? Your answer should be in the form: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to an unseen point.",
      "<5>"
    ],
    [
      "Among the shapes <2>, <3>, and <4>, identify which is symmetric to the <1> shape with respect to a point (not a line). Write your answer as: The [<2>/<3>/<4>] shape is symmetric to the <1> shape with respect to a point not visible in the image.",
      "<5>"
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