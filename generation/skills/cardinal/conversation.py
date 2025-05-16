from .rules import *

import random

# Correct the indentation of this json. 
# This json has List of Rephrased [Question, Answer] per each of the conversation problem types. 
# For conversation problem types that has less than 5 rephrases, generate rephrases. 
# When rephrasing the pquestion, answer] You need to make not only a rephrased question, but also rephrased answer. 

conversation_long = {
  "cardinal_1": [
    [
      "How many points are present in the given image?", 
      "The image contains <1> points."
    ],
    [
      "What is the total number of points in the image?", 
      "A total of <1> points are in the image."
    ],
    [
      "Can you count the points in the given image?", 
      "There are exactly <1> points visible in the image."
    ],
    [
      "How many points can be identified in the image?", 
      "You can identify <1> points in this image."
    ],
    [
      "What is the count of points in the image?", 
      "The count of points in the image is <1>."
    ]
  ],
  "cardinal_2": [
    [
      "How many line segments are in the image? Answer in a number.", 
      "The image contains <1> line segments."
    ],
    [
      "What is the total number of line segments present?", 
      "A total of <1> line segments are present in the image."
    ],
    [
      "Can you count the line segments in this image?", 
      "You can count <1> line segments in this image."
    ],
    [
      "How many distinct line segments are visible in the image?", 
      "There are <1> distinct line segments visible."
    ],
    [
      "What is the number of line segments shown in the image?", 
      "The number of line segments shown here is <1>."
    ]
  ],
  "cardinal_3": [
    [
      "How many <1>s are there in the image? Answer in number.", 
      "<2> <1>s are in the image."
    ],
    [
      "What is the total count of <1>s visible in the image?", 
      "A total of <2> <1>s can be seen in the image."
    ],
    [
      "Can you find and count all the <1>s in the image?", 
      "There are <2> <1>s present in the image."
    ],
    [
      "What is the number of <1>s displayed in the image?", 
      "The image displays <2> <1>s."
    ],
    [
      "How many <1>s can you identify in the image?", 
      "You can identify <2> <1>s in this image."
    ]
  ],
  "cardinal_4": [
    [
      "How many different shapes are there? If there are multiple shapes that look exactly alike, count them as one. The answer should be a number.", 
      "The image contains <1> unique shapes."
    ],
    [
      "What is the total count of unique shapes in the image?", 
      "There are <1> unique shapes present in the image."
    ],
    [
      "Can you tell how many unique shapes are present in the image?", 
      "You can see <1> different shapes in the image."
    ],
    [
      "How many distinct shapes can be seen in the image?", 
      "<1> distinct shapes can be observed in the image."
    ],
    [
      "What is the number of unique shapes depicted in the image?", 
      "The number of unique shapes in the image is <1>."
    ]
  ],
  "cardinal_5": [
    [
      "In the image, there are several colored shapes. How many different colors are in the image? Ignore the background color.", 
      "The image features <1> distinct colors, excluding the background."
    ],
    [
      "What is the total number of colors in the image excluding the background?", 
      "<1> different colors are present, excluding the background."
    ],
    [
      "Can you identify the number of distinct colors in the image?", 
      "You can identify <1> distinct colors in the image."
    ],
    [
      "How many unique colors can you see in the image?", 
      "The image contains <1> unique colors."
    ],
    [
      "What is the count of different colors in the image, ignoring the background?", 
      "There are <1> different colors visible in this image, not counting the background."
    ]
  ],
  "cardinal_6": [
    [
      "In the image, there are several points and letters '<1>'. Count all the '<1>'s. The answer should be one of 3, 4, 5, or 6.", 
      "The correct count is <2>."
    ],
    [
      "How many instances of '<1>' can you find in the image? Choose from 3, 4, 5, or 6.", 
      "You can find <2> instances of '<1>' in the image."
    ],
    [
      "Can you count the number of '<1>'s in the image and select from 3, 4, 5, or 6?", 
      "There are <2> '<1>'s in the image."
    ],
    [
      "What is the total count of '<1>'s in the image? The result is either 3, 4, 5, or 6.", 
      "The total is <2> '<1>'s."
    ],
    [
      "How many '<1>'s are there in the image? Pick from 3, 4, 5, or 6.", 
      "The number of '<1>'s is <2>."
    ]
  ]
}

conversation_caption = {
  "cardinal_1": [
    ["", "The image contains <1> points."],
    ["", "A total of <1> points are in the image."],
    ["", "There are exactly <1> points visible in the image."],
    ["", "You can identify <1> points in this image."],
    ["", "The count of points in the image is <1>."]
  ],
  "cardinal_2": [
    ["", "The image contains <1> line segments."],
    ["", "A total of <1> line segments are present in the image."],
    ["", "You can count <1> line segments in this image."],
    ["", "There are <1> distinct line segments visible."],
    ["", "The number of line segments shown here is <1>."]
  ],
  "cardinal_3": [
    ["", "<2> <1>s are in the image."],
    ["", "A total of <2> <1>s can be seen in the image."],
    ["", "There are <2> <1>s present in the image."],
    ["", "The image displays <2> <1>s."],
    ["", "You can identify <2> <1>s in this image."]
  ],
  "cardinal_4": [
    ["", "The image contains <1> unique shapes."],
    ["", "There are <1> unique shapes present in the image."],
    ["", "You can see <1> different shapes in the image."],
    ["", "<1> distinct shapes can be observed in the image."],
    ["", "The number of unique shapes in the image is <1>."]
  ],
  "cardinal_5": [
    ["", "The image features <1> distinct colors, excluding the background."],
    ["", "<1> different colors are present, excluding the background."],
    ["", "You can identify <1> distinct colors in the image."],
    ["", "The image contains <1> unique colors."],
    ["", "There are <1> different colors visible in this image, not counting the background."]
  ],
  "cardinal_6": [
    ["", "The correct count is <2>."],
    ["", "You can find <2> instances of '<1>' in the image."],
    ["", "There are <2> '<1>'s in the image."],
    ["", "The total is <2> '<1>'s."],
    ["", "The number of '<1>'s is <2>."]
  ]
}


conversation_short = {
  "cardinal_1": [
    [
      "How many points are present in the given image?", 
      "<1>"
    ],
    [
      "What is the total number of points in the image?", 
      "<1>"
    ],
    [
      "Can you count the points in the given image?", 
      "<1>"
    ],
    [
      "How many points can be identified in the image?", 
      "<1>"
    ],
    [
      "What is the count of points in the image?", 
      "<1>"
    ]
  ],
  "cardinal_2": [
    [
      "How many line segments are in the image? Answer in a number.", 
      "<1>"
    ],
    [
      "What is the total number of line segments present?", 
      "<1>"
    ],
    [
      "Can you count the line segments in this image?", 
      "<1>"
    ],
    [
      "How many distinct line segments are visible in the image?", 
      "<1>"
    ],
    [
      "What is the number of line segments shown in the image?", 
      "<1>"
    ]
  ],
  "cardinal_3": [
    [
      "How many <1>s are there in the image? Answer in number.", 
      "<2>"
    ],
    [
      "What is the total count of <1>s visible in the image?", 
      "<2>"
    ],
    [
      "Can you find and count all the <1>s in the image?", 
      "<2>"
    ],
    [
      "What is the number of <1>s displayed in the image?", 
      "<2>"
    ],
    [
      "How many <1>s can you identify in the image?", 
      "<2>"
    ]
  ],
  "cardinal_4": [
    [
      "How many different shapes are there? If there are multiple shapes that look exactly alike, count them as one. The answer should be a number.", 
      "<1>"
    ],
    [
      "What is the total count of unique shapes in the image?", 
      "<1>"
    ],
    [
      "Can you tell how many unique shapes are present in the image?", 
      "<1>"
    ],
    [
      "How many distinct shapes can be seen in the image?", 
      "<1>"
    ],
    [
      "What is the number of unique shapes depicted in the image?", 
      "<1>"
    ]
  ],
  "cardinal_5": [
    [
      "In the image, there are several colored shapes. How many different colors are in the image? Ignore the background color.", 
      "<1>"
    ],
    [
      "What is the total number of colors in the image excluding the background?", 
      "<1>"
    ],
    [
      "Can you identify the number of distinct colors in the image?", 
      "<1>"
    ],
    [
      "How many unique colors can you see in the image?", 
      "<1>"
    ],
    [
      "What is the count of different colors in the image, ignoring the background?", 
      "<1>"
    ]
  ],
  "cardinal_6": [
    [
      "In the image, there are several points and letters '<1>'. Count all the '<1>'s. The answer should be one of 3, 4, 5, or 6.", 
      "<2>"
    ],
    [
      "How many instances of '<1>' can you find in the image? Choose from 3, 4, 5, or 6.", 
      "<2>"
    ],
    [
      "Can you count the number of '<1>'s in the image and select from 3, 4, 5, or 6?", 
      "<2>"
    ],
    [
      "What is the total count of '<1>'s in the image? The result is either 3, 4, 5, or 6.", 
      "<2>"
    ],
    [
      "How many '<1>'s are there in the image? Pick from 3, 4, 5, or 6.", 
      "<2>"
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