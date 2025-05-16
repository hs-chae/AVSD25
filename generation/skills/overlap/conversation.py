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
"overlap_1" : [
  [
      "In the image, you can see two circles. Do the interiors of these circles overlap?",
      "<1>"
  ],
  [
      "Are the interiors of the two circles in the image overlapping?",
      "<1>"
  ],
  [
      "Does the area inside the two circles shown in the image overlap?",
      "<1>"
  ],
  [
      "In the given image, do the two circles have overlapping interiors?",
      "<1>"
  ],
  [
      "Do the two circles in the image share any overlapping interior regions?",
      "<1>"
  ],
  [
      "Are the interiors of the two circles in the picture overlapping?",
      "<1>"
  ],
  [
      "In the image provided, do the interiors of the two circles overlap?",
      "<1>"
  ],
  [
      "Does the interior region of one circle overlap with the other in the image?",
      "<1>"
  ],
  [
      "In the image, do the two circles have any overlapping interior spaces?",
      "<1>"
  ],
  [
      "Do the interiors of the two circles depicted in the image overlap?",
      "<1>"
  ]
],
  "overlap_2": [
    [
      "In the image, you can see two triangles. Do the interiors of these triangles overlap?",
      "<1>"
    ],
    [
      "In the image, there are two triangles. Are their interiors overlapping?",
      "<1>"
    ],
    [
      "The image contains two triangles. Do their interiors overlap?",
      "<1>"
    ],
    [
      "Look at the two triangles in the image. Do their interiors overlap?",
      "<1>"
    ],
    [
      "Do the interiors of the two triangles in the image overlap?",
      "<1>"
    ]
  ],
  "overlap_2_1": [
    [
      "In the image, you can see two squares. Do the interiors of these two squares overlap?",
      "<1>"
    ],
    [
      "The image shows two squares. Do their interiors overlap?",
      "<1>"
    ],
    [
      "Look at the two squares in the image. Are their interiors overlapping?",
      "<1>"
    ],
    [
      "In the given image, do the interiors of the two squares overlap?",
      "<1>"
    ],
    [
      "Are the interiors of the two squares in the image overlapping?",
      "<1>"
    ]
  ],
  "overlap_5": [
    [
      "Choose the word in parentheses that correctly describes the image. Rewrite the sentence with the chosen word. In the image, the purple region and the orange region overlap each other, and the shape of the intersection is a (triangle/square/pentagon/circle).",
      "The shape of the intersection is <1>."
    ],
    [
      "Select the correct word in parentheses to describe the image. Rewrite the sentence with the selected word. The purple region and the orange region overlap, forming a (triangle/square/pentagon/circle).",
      "The region of overlap forms a <1>."
    ],
    [
      "Pick the appropriate word in parentheses to describe the shape of the intersection. Rewrite the sentence using the chosen word. The purple region and the orange region overlap, and the intersection forms a (triangle/square/pentagon/circle).",
      "The intersection forms a <1>."
    ],
    [
      "Identify the correct word in parentheses that describes the intersection shape. Rewrite the sentence using that word. The purple region and the orange region overlap, creating a (triangle/square/pentagon/circle).",
      "The purple region and the orange region overlap, creating a <1>."
    ],
    [
      "Select the shape in parentheses that correctly describes the overlap. Rewrite the sentence using the chosen shape. The purple and orange regions overlap, and the resulting intersection is a (triangle/square/pentagon/circle).",
      "The purple and orange regions overlap, and the resulting intersection is a <1>."
    ]
  ]
}
conversation_caption = conversation_caption = {
    "overlap_1": [
        ["", "In the image, you can see two circles. The interiors of these circles overlap: <1>."],
        ["", "Are the interiors of the two circles in the image overlapping? The answer is: <1>."],
        ["", "Does the area inside the two circles shown in the image overlap? The answer is: <1>."],
        ["", "In the given image, the two circles have overlapping interiors: <1>."],
        ["", "The two circles in the image share overlapping interior regions: <1>."],
        ["", "The interiors of the two circles in the picture are overlapping: <1>."],
        ["", "In the image provided, the interiors of the two circles overlap: <1>."],
        ["", "The interior region of one circle overlaps with the other in the image: <1>."],
        ["", "In the image, the two circles have overlapping interior spaces: <1>."],
        ["", "The interiors of the two circles depicted in the image overlap: <1>."]
    ],
    "overlap_2": [
        ["", "In the image, you can see two triangles. Their interiors overlap: <1>."],
        ["", "In the image, there are two triangles. Their interiors are overlapping: <1>."],
        ["", "The image contains two triangles. Their interiors overlap: <1>."],
        ["", "Looking at the two triangles in the image, their interiors overlap: <1>."],
        ["", "The interiors of the two triangles in the image overlap: <1>."]
    ],
    "overlap_2_1": [
        ["", "In the image, you can see two squares. Their interiors overlap: <1>."],
        ["", "The image shows two squares. Their interiors overlap: <1>."],
        ["", "Looking at the two squares in the image, their interiors are overlapping: <1>."],
        ["", "In the given image, the interiors of the two squares overlap: <1>."],
        ["", "The interiors of the two squares in the image are overlapping: <1>."]
    ],
    "overlap_5": [
        ["", "In the image, the purple region and the orange region overlap, and the shape of the intersection is a <1>."],
        ["", "The purple region and the orange region overlap, forming a <1>."],
        ["", "The purple region and the orange region overlap, and the intersection forms a <1>."],
        ["", "The purple region and the orange region overlap, creating a <1>."],
        ["", "The purple and orange regions overlap, and the resulting intersection is a <1>."]
    ]
}

conversation_short = {
"overlap_1" : [
  [
      "In the image, you can see two circles. Do the interiors of these circles overlap?",
      "<2>"
  ],
  [
      "Are the interiors of the two circles in the image overlapping?",
      "<2>"
  ],
  [
      "Does the area inside the two circles shown in the image overlap?",
      "<2>"
  ],
  [
      "In the given image, do the two circles have overlapping interiors?",
      "<2>"
  ],
  [
      "Do the two circles in the image share any overlapping interior regions?",
      "<2>"
  ],
  [
      "Are the interiors of the two circles in the picture overlapping?",
      "<2>"
  ],
  [
      "In the image provided, do the interiors of the two circles overlap?",
      "<2>"
  ],
  [
      "Does the interior region of one circle overlap with the other in the image?",
      "<2>"
  ],
  [
      "In the image, do the two circles have any overlapping interior spaces?",
      "<2>"
  ],
  [
      "Do the interiors of the two circles depicted in the image overlap?",
      "<2>"
  ]
],
  "overlap_2": [
    [
      "In the image, you can see two triangles. Do the interiors of these triangles overlap?",
      "<1>"
    ],
    [
      "In the image, there are two triangles. Are their interiors overlapping?",
      "<1>"
    ],
    [
      "The image contains two triangles. Do their interiors overlap?",
      "<1>"
    ],
    [
      "Look at the two triangles in the image. Do their interiors overlap?",
      "<1>"
    ],
    [
      "Do the interiors of the two triangles in the image overlap?",
      "<1>"
    ]
  ],
  "overlap_2_1": [
    [
      "In the image, you can see two squares. Do the interiors of these two squares overlap?",
      "<1>"
    ],
    [
      "The image shows two squares. Do their interiors overlap?",
      "<1>"
    ],
    [
      "Look at the two squares in the image. Are their interiors overlapping?",
      "<1>"
    ],
    [
      "In the given image, do the interiors of the two squares overlap?",
      "<1>"
    ],
    [
      "Are the interiors of the two squares in the image overlapping?",
      "<1>"
    ]
  ],
  "overlap_5": [
    [
      "Choose the word in parentheses that correctly describes the image. Rewrite the sentence with the chosen word. In the image, the purple region and the orange region overlap each other, and the shape of the intersection is a (triangle/square/pentagon/circle).",
      "<1>"
    ],
    [
      "Slect the correct word in parentheses to describe the image. Rewrite the sentence with the selected word. The purple region and the orange region overlap, forming a (triangle/square/pentagon/circle).",
      "<1>"
    ],
    [
      "Pick the appropriate word in parentheses to describe the shape of the intersection. Rewrite the sentence using the chosen word. The purple region and the orange region overlap, and the intersection forms a (triangle/square/pentagon/circle).",
      "<1>"
    ],
    [
      "Identify the correct word in parentheses that describes the intersection shape. Rewrite the sentence using that word. The purple region and the orange region overlap, creating a (triangle/square/pentagon/circle).",
      "<1>"
    ],
    [
      "Select the shape in parentheses that correctly describes the overlap. Rewrite the sentence using the chosen shape. The purple and orange regions overlap, and the resulting intersection is a (triangle/square/pentagon/circle).",
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