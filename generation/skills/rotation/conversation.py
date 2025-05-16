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
  "rotation_1" : [
    [
        "In the image, which triangle among <3>, <4>, <5>, <6>, <7> is least likely to be a rotation of <2> about the point <8>?",
        "<1> is least likely to be a rotation of <2> with respect to the point <8>."
    ],
    [
        "Which triangle, out of <3>, <4>, <5>, <6>, and <7>, in the image is least likely to represent a rotation of <2> around point <8>?",
        "<1> is least likely to represent a rotation of <2> around point <8>."
    ],
    [
        "From the triangles <3>, <4>, <5>, <6>, and <7> in the image, which is least likely to be a rotated version of <2> about point <8>?",
        "<1> is least likely to be a rotated version of <2> about point <8>."
    ],
    [
        "Among the triangles <3>, <4>, <5>, <6>, and <7> in the image, which one is the least probable rotation of <2> around <8>?",
        "<1> is the least probable rotation of <2> around <8>."
    ],
    [
        "In the given image, which triangle among <3>, <4>, <5>, <6>, and <7> is least likely to correspond to a rotation of <2> about point <8>?",
        "<1> is least likely to correspond to a rotation of <2> about point <8>."
    ],
    [
        "Which triangle from <3>, <4>, <5>, <6>, and <7> in the image appears least likely to be a rotation of <2> around the point <8>?",
        "<1> appears least likely to be a rotation of <2> around the point <8>."
    ],
    [
        "Out of <3>, <4>, <5>, <6>, and <7>, which triangle in the image is least likely to have been rotated from <2> about point <8>?",
        "<1> is least likely to have been rotated from <2> about point <8>."
    ],
    [
        "From the image, identify the triangle among <3>, <4>, <5>, <6>, and <7> that is least likely to be a rotated version of <2> around point <8>.",
        "<1> is least likely to be a rotated version of <2> around point <8>."
    ],
    [
        "In the image, which triangle out of <3>, <4>, <5>, <6>, and <7> is the least plausible rotation of <2> with respect to the point <8>?",
        "<1> is the least plausible rotation of <2> with respect to the point <8>."
    ],
    [
        "Among the triangles <3>, <4>, <5>, <6>, and <7> in the image, which is least likely to match a rotation of <2> around <8>?",
        "<1> is least likely to match a rotation of <2> around <8>."
    ]
],
  "rotation_2" : [
    [
        "Among shapes <2>, <3>, and <4> in the image, which one can be made solely by rotating shape <1> on the 2D plane?",
        "Shape <5> can be made solely by rotating shape <1> on the white 2D plane."
    ],
    [
      "Which shape among <2>, <3>, and <4> in the image can be generated solely by rotating shape <1> on the 2D plane?",
      "Shape <5> can be generated solely by rotating shape <1> on the 2D plane."
    ],
    [
      "Out of the shapes <2>, <3>, and <4>, which one is formed purely by rotating shape <1> on the 2D plane?",
      "Shape <5> is formed purely by rotating shape <1> on the 2D plane."
    ],
    [
      "From the shapes <2>, <3>, and <4> shown in the image, which one results solely from rotating shape <1> on the 2D plane?",
      "Shape <5> results solely from rotating shape <1> on the 2D plane."
    ],
    [
      "Among shapes <2>, <3>, and <4>, which one can be derived solely by rotating shape <1> in the 2D plane?",
      "Shape <5> can be derived solely by rotating shape <1> in the 2D plane."
    ],
    [
      "Of the shapes <2>, <3>, and <4> in the image, which is obtained only by rotating shape <1> on the 2D plane?",
      "Shape <5> is obtained only by rotating shape <1> on the 2D plane."
    ]
],
  "rotation_3" : [
    [
        "Among shapes <2>, <3>, and <4> in the image, which one cannot be made solely by rotating shape <1> on the 2D plane?",
        "Shape <5> cannot be made solely by rotating shape <1> on the 2D plane."
    ],
    [
      "Which shape among <2>, <3>, and <4> in the image cannot be created solely by rotating shape <1> on the 2D plane?",
      "Shape <5> cannot be created solely by rotating shape <1> on the 2D plane."
    ],
    [
      "Out of the shapes <2>, <3>, and <4>, which one cannot result solely from rotating shape <1> on the 2D plane?",
      "Shape <5> cannot result solely from rotating shape <1> on the 2D plane."
    ],
    [
      "Among shapes <2>, <3>, and <4> in the image, which one cannot be obtained solely by rotating shape <1> on the 2D plane?",
      "Shape <5> cannot be obtained solely by rotating shape <1> on the 2D plane."
    ],
    [
      "From the shapes <2>, <3>, and <4> in the image, which one cannot be achieved by only rotating shape <1> on the 2D plane?",
      "Shape <5> cannot be achieved by only rotating shape <1> on the 2D plane."
    ],
    [
      "Among the shapes <2>, <3>, and <4>, which one is not possible to make solely by rotating shape <1> on the 2D plane?",
      "Shape <5> is not possible to make solely by rotating shape <1> on the 2D plane."
    ]
],
  "rotation_4" : [
    [
        "There are four triangles in the picture. Among triangle <2>, <3>, and <4>, choose the triangle that can be made by 90 degrees rotation of <1>.",
        "The triangle made by 90 degrees rotation of <1> is <5>."
    ],
    [
      "In the picture, there are four triangles. Among triangles <2>, <3>, and <4>, which one can be created by rotating <1> by 90 degrees?",
      "The triangle created by rotating <1> by 90 degrees is <5>."
    ],
    [
      "There are four triangles visible. From triangles <2>, <3>, and <4>, select the one that results from a 90-degree rotation of <1>.",
      "The triangle resulting from a 90-degree rotation of <1> is <5>."
    ],
    [
      "Among the four triangles in the image, which one among <2>, <3>, and <4> can be obtained by rotating triangle <1> by 90 degrees?",
      "The triangle obtained by rotating <1> by 90 degrees is <5>."
    ],
    [
      "In the image, out of triangles <2>, <3>, and <4>, which one is formed by rotating <1> by 90 degrees?",
      "The triangle formed by rotating <1> by 90 degrees is <5>."
    ],
    [
      "Among the four triangles in the picture, which triangle from <2>, <3>, and <4> corresponds to a 90-degree rotation of <1>?",
      "The triangle corresponding to a 90-degree rotation of <1> is <5>."
    ]
],
  "rotation_5" : [
    [
        "There are heart shapes in the picture. Among heart <2>, <3>, and <4>, choose the shape that can be made by 45 degrees rotation of <1>.",
        "The one that can be made by 45 degrees rotation of <1> is <5>."
    ],
    [
      "In the picture, there are heart shapes. Among hearts <2>, <3>, and <4>, which one is created by rotating <1> by 45 degrees?",
      "The heart created by rotating <1> by 45 degrees is <5>."
    ],
    [
      "Among the heart shapes in the image, which one among <2>, <3>, and <4> results from a 45-degree rotation of <1>?",
      "The heart resulting from a 45-degree rotation of <1> is <5>."
    ],
    [
      "In the picture, out of hearts <2>, <3>, and <4>, which one can be formed by a 45-degree rotation of <1>?",
      "The heart formed by a 45-degree rotation of <1> is <5>."
    ],
    [
      "Among the heart shapes shown, which one from <2>, <3>, and <4> corresponds to a 45-degree rotation of <1>?",
      "The heart corresponding to a 45-degree rotation of <1> is <5>."
    ],
    [
      "In the image, which heart shape among <2>, <3>, and <4> can be made by rotating <1> by 45 degrees?",
      "The heart that can be made by rotating <1> by 45 degrees is <5>."
    ]
]
}
conversation_caption = {
  "rotation_1": [
    [
      "",
      "In the image, among the triangles <3>, <4>, <5>, <6>, and <7>, the triangle least likely to be a rotation of <2> about the point <8> is <1>."
    ]
  ],
  "rotation_2": [
    [
      "",
      "In the image, among the shapes <2>, <3>, and <4>, the shape that can be made solely by rotating shape <1> on the 2D plane is <5>."
    ]
  ],
  "rotation_3": [
    [
      "",
      "In the image, among the shapes <2>, <3>, and <4>, the shape that cannot be made solely by rotating shape <1> on the 2D plane is <5>."
    ]
  ],
  "rotation_4": [
    [
      "",
      "In the image, among the four triangles, the triangle among <2>, <3>, and <4> that can be made by a 90-degree rotation of <1> is <5>."
    ]
  ],
  "rotation_5": [
    [
      "",
      "In the image, among the heart shapes <2>, <3>, and <4>, the heart that can be made by a 45-degree rotation of <1> is <5>."
    ]
  ]
}

conversation_short = {
  "rotation_1" : [
    [
        "In the image, which triangle among <3>, <4>, <5>, <6>, <7> is least likely to be a rotation of <2> about the point <8>?",
        "<1>"
    ],
    [
        "Which triangle, out of <3>, <4>, <5>, <6>, and <7>, in the image is least likely to represent a rotation of <2> around point <8>?",
        "<1>"
    ],
    [
        "From the triangles <3>, <4>, <5>, <6>, and <7> in the image, which is least likely to be a rotated version of <2> about point <8>?",
        "<1>"
    ],
    [
        "Among the triangles <3>, <4>, <5>, <6>, and <7> in the image, which one is the least probable rotation of <2> around <8>?",
        "<1>"
    ],
    [
        "In the given image, which triangle among <3>, <4>, <5>, <6>, and <7> is least likely to correspond to a rotation of <2> about point <8>?",
        "<1>"
    ],
    [
        "Which triangle from <3>, <4>, <5>, <6>, and <7> in the image appears least likely to be a rotation of <2> around the point <8>?",
        "<1>"
    ],
    [
        "Out of <3>, <4>, <5>, <6>, and <7>, which triangle in the image is least likely to have been rotated from <2> about point <8>?",
        "<1>"
    ],
    [
        "From the image, identify the triangle among <3>, <4>, <5>, <6>, and <7> that is least likely to be a rotated version of <2> around point <8>.",
        "<1>"
    ],
    [
        "In the image, which triangle out of <3>, <4>, <5>, <6>, and <7> is the least plausible rotation of <2> with respect to the point <8>?",
        "<1>"
    ],
    [
        "Among the triangles <3>, <4>, <5>, <6>, and <7> in the image, which is least likely to match a rotation of <2> around <8>?",
        "<1>"
    ]
],
  "rotation_2" : [
    [
        "Among shapes <2>, <3>, and <4> in the image, which one can be made solely by rotating shape <1> on the 2D plane?",
        "<5>"
    ],
    [
      "Which shape among <2>, <3>, and <4> in the image can be generated solely by rotating shape <1> on the 2D plane?",
      "<5>"
    ],
    [
      "Out of the shapes <2>, <3>, and <4>, which one is formed purely by rotating shape <1> on the 2D plane?",
      "<5>"
    ],
    [
      "From the shapes <2>, <3>, and <4> shown in the image, which one results solely from rotating shape <1> on the 2D plane?",
      "<5>"
    ],
    [
      "Among shapes <2>, <3>, and <4>, which one can be derived solely by rotating shape <1> in the 2D plane?",
      "<5>"
    ],
    [
      "Of the shapes <2>, <3>, and <4> in the image, which is obtained only by rotating shape <1> on the 2D plane?",
      "<5>"
    ]
],
  "rotation_3" : [
    [
        "Among shapes <2>, <3>, and <4> in the image, which one cannot be made solely by rotating shape <1> on the 2D plane?",
        "<5>"
    ],
    [
      "Which shape among <2>, <3>, and <4> in the image cannot be created solely by rotating shape <1> on the 2D plane?",
      "<5>"
    ],
    [
      "Out of the shapes <2>, <3>, and <4>, which one cannot result solely from rotating shape <1> on the 2D plane?",
      "<5>"
    ],
    [
      "Among shapes <2>, <3>, and <4> in the image, which one cannot be obtained solely by rotating shape <1> on the 2D plane?",
      "<5>"
    ],
    [
      "From the shapes <2>, <3>, and <4> in the image, which one cannot be achieved by only rotating shape <1> on the 2D plane?",
      "<5>"
    ],
    [
      "Among the shapes <2>, <3>, and <4>, which one is not possible to make solely by rotating shape <1> on the 2D plane?",
      "<5>"
    ]
],
  "rotation_4" : [
    [
        "There are four triangles in the picture. Among triangle <2>, <3>, and <4>, choose the triangle that can be made by 90 degrees rotation of <1>.",
        "<5>"
    ],
    [
      "In the picture, there are four triangles. Among triangles <2>, <3>, and <4>, which one can be created by rotating <1> by 90 degrees?",
      "<5>"
    ],
    [
      "There are four triangles visible. From triangles <2>, <3>, and <4>, select the one that results from a 90-degree rotation of <1>.",
      "<5>"
    ],
    [
      "Among the four triangles in the image, which one among <2>, <3>, and <4> can be obtained by rotating triangle <1> by 90 degrees?",
      "<5>"
    ],
    [
      "In the image, out of triangles <2>, <3>, and <4>, which one is formed by rotating <1> by 90 degrees?",
      "<5>"
    ],
    [
      "Among the four triangles in the picture, which triangle from <2>, <3>, and <4> corresponds to a 90-degree rotation of <1>?",
      "<5>"
    ]
],
  "rotation_5" : [
    [
        "There are heart shapes in the picture. Among heart <2>, <3>, and <4>, choose the shape that can be made by 45 degrees rotation of <1>.",
        "<5>"
    ],
    [
      "In the picture, there are heart shapes. Among hearts <2>, <3>, and <4>, which one is created by rotating <1> by 45 degrees?",
      "<5>"
    ],
    [
      "Among the heart shapes in the image, which one among <2>, <3>, and <4> results from a 45-degree rotation of <1>?",
      "<5>"
    ],
    [
      "In the picture, out of hearts <2>, <3>, and <4>, which one can be formed by a 45-degree rotation of <1>?",
      "<5>"
    ],
    [
      "Among the heart shapes shown, which one from <2>, <3>, and <4> corresponds to a 45-degree rotation of <1>?",
      "<5>"
    ],
    [
      "In the image, which heart shape among <2>, <3>, and <4> can be made by rotating <1> by 45 degrees?",
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