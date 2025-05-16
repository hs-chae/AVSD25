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
        "area_1_1": [
            [
                "In the image, there is a pie graph with four categories. Which category has the largest ratio? Choose from <1>, <2>, <3>, and <4>.",
                "Category <5> has the largest ratio."
            ],
            [
                "Refer to the image's pie chart that contains four segments. Which segment represents the highest proportion? Select from <1>, <2>, <3>, or <4>.",
                "Category <5> represents the highest proportion."
            ],
            [
                "Looking at the pie diagram with four divisions, which category occupies the greatest percentage? Choose between <1>, <2>, <3>, and <4>.",
                "Category <5> occupies the greatest percentage."
            ],
            [
                "Examine the pie chart in the image with four sections. Which section has the largest share? Pick from <1>, <2>, <3>, or <4>.",
                "Section <5> has the largest share."
            ],
            [
                "Based on the pie graph featuring four categories in the image, which category holds the highest ratio? Select from <1>, <2>, <3>, and <4>.",
                "Category <5> holds the highest ratio."
            ]
        ],
        "area_1_2": [
            [
                "In the image, there is a pie graph with five categories. Which category has the largest ratio? Choose from <1>, <2>, <3>, <4>, and <5>.",
                "Category <6> has the largest ratio."
            ],
            [
                "Refer to the pie chart in the image that includes five segments. Which segment represents the highest proportion? Select from <1>, <2>, <3>, <4>, or <5>.",
                "Category <6> represents the highest proportion."
            ],
            [
                "Looking at the pie diagram with five divisions, which category occupies the greatest percentage? Choose between <1>, <2>, <3>, <4>, and <5>.",
                "Category <6> occupies the greatest percentage."
            ],
            [
                "Examine the pie chart in the image with five sections. Which section has the largest share? Pick from <1>, <2>, <3>, <4>, or <5>.",
                "Section <6> has the largest share."
            ],
            [
                "Based on the pie graph featuring five categories in the image, which category holds the highest ratio? Select from <1>, <2>, <3>, <4>, and <5>.",
                "Category <6> holds the highest ratio."
            ]
        ],
        "area_1_3": [
            [
                "In the image, there is a pie graph with three categories. Which category has the largest ratio? Choose from <1>, <2>, and <3>.",
                "Category <4> has the largest ratio."
            ],
            [
                "Refer to the pie chart in the image that includes three segments. Which segment represents the highest proportion? Select from <1>, <2>, or <3>.",
                "Category <4> represents the highest proportion."
            ],
            [
                "Looking at the pie diagram with three divisions, which category occupies the greatest percentage? Choose between <1>, <2>, and <3>.",
                "Category <4> occupies the greatest percentage."
            ],
            [
                "Examine the pie chart in the image with three sections. Which section has the largest share? Pick from <1>, <2>, or <3>.",
                "Section <4> has the largest share."
            ],
            [
                "Based on the pie graph featuring three categories in the image, which category holds the highest ratio? Select from <1>, <2>, and <3>.",
                "Category <4> holds the highest ratio."
            ]
        ],
        "area_1_4": [
            [
                "In the image, there is a pie graph with six categories. Which category has the largest ratio? Choose from <1>, <2>, <3>, <4>, <5>, and <6>.",
                "Category <7> has the largest ratio."
            ],
            [
                "Refer to the pie chart in the image that includes six segments. Which segment represents the highest proportion? Select from <1>, <2>, <3>, <4>, <5>, or <6>.",
                "Category <7> represents the highest proportion."
            ],
            [
                "Looking at the pie diagram with six divisions, which category occupies the greatest percentage? Choose between <1>, <2>, <3>, <4>, <5>, and <6>.",
                "Category <7> occupies the greatest percentage."
            ],
            [
                "Examine the pie chart in the image with six sections. Which section has the largest share? Pick from <1>, <2>, <3>, <4>, <5>, or <6>.",
                "Section <7> has the largest share."
            ],
            [
                "Based on the pie graph featuring six categories in the image, which category holds the highest ratio? Select from <1>, <2>, <3>, <4>, <5>, and <6>.",
                "Category <7> holds the highest ratio."
            ]
        ],
        "area_1_5": [
            [
                "In the image, there is a pie graph with two categories. Which category has the largest ratio? Choose from <1> and <2>.",
                "Category <3> has the largest ratio."
            ],
            [
                "Refer to the pie chart in the image that includes two segments. Which segment represents the highest proportion? Select from <1> or <2>.",
                "Category <3> represents the highest proportion."
            ],
            [
                "Looking at the pie diagram with two divisions, which category occupies the greater percentage? Choose between <1> and <2>.",
                "Category <3> occupies the greater percentage."
            ],
            [
                "Examine the pie chart in the image with two sections. Which section has the largest share? Pick from <1> or <2>.",
                "Section <3> has the largest share."
            ],
            [
                "Based on the pie graph featuring two categories in the image, which category holds the highest ratio? Select from <1> and <2>.",
                "Category <3> holds the highest ratio."
            ]
        ],
        "area_2_1": [
            [
                "Choose the word in parentheses that correctly describes the image: In the given image, area <1> occupies a (larger/smaller) region than area <2>.",
                "Area <1> occupies a <3> region than area <2>."
            ],
            [
                "Select the appropriate word from the parentheses to describe the image: In the image, area <1> covers a (larger/smaller) area compared to area <2>.",
                "Area <1> covers a <3> area compared to area <2>."
            ],
            [
                "Pick the correct term from the options in parentheses to accurately describe the image: Area <1> takes up a (larger/smaller) portion than area <2>.",
                "Area <1> takes up a <3> portion than area <2>."
            ],
            [
                "Choose the suitable word from the parentheses to describe the image: In the illustration, area <1> has a (larger/smaller) size than area <2>.",
                "Area <1> has a <3> size than area <2>."
            ],
            [
                "Select the correct word in parentheses to accurately describe the image: Area <1> occupies a (larger/smaller) space relative to area <2>.",
                "Area <1> occupies a <3> space relative to area <2>."
            ]
        ],
        "area_2_2": [
            [
                "Choose the word in parentheses that correctly describes the image: In the given image, area <1> occupies a (larger/smaller) region than area <2>, and area <2> occupies a (larger/smaller) region than area <3>.",
                "Area <1> occupies a <4> region than area <2>, and area <2> occupies a <5> region than area <3>."
            ],
            [
                "Select the appropriate words from the parentheses to describe the image: In the image, area <1> covers a (larger/smaller) area compared to area <2>, and area <2> covers a (larger/smaller) area compared to area <3>.",
                "Area <1> covers a <4> area compared to area <2>, and area <2> covers a <5> area compared to area <3>."
            ],
            [
                "Pick the correct terms from the options in parentheses to accurately describe the image: Area <1> takes up a (larger/smaller) portion than area <2>, and area <2> takes up a (larger/smaller) portion than area <3>.",
                "Area <1> takes up a <4> portion than area <2>, and area <2> takes up a <5> portion than area <3>."
            ],
            [
                "Choose the suitable words from the parentheses to describe the image: In the illustration, area <1> has a (larger/smaller) size than area <2>, and area <2> has a (larger/smaller) size than area <3>.",
                "Area <1> has a <4> size than area <2>, and area <2> has a <5> size than area <3>."
            ],
            [
                "Select the correct words in parentheses to accurately describe the image: Area <1> occupies a (larger/smaller) space relative to area <2>, and area <2> occupies a (larger/smaller) space relative to area <3>.",
                "Area <1> occupies a <4> space relative to area <2>, and area <2> occupies a <5> space relative to area <3>."
            ]
        ]
}

conversation_caption = {
    "area_1_1": [
        ["", "In the image, there is a pie graph with four categories. From categories <1>, <2>, <3>, and <4>, category <5> has the largest ratio."],
        ["", "Refer to the image's pie chart that contains four segments. From segments <1>, <2>, <3>, and <4>, category <5> represents the highest proportion."],
        ["", "Looking at the pie diagram with four divisions, from categories <1>, <2>, <3>, and <4>, category <5> occupies the greatest percentage."],
        ["", "Examine the pie chart in the image with four sections. Among sections <1>, <2>, <3>, and <4>, section <5> has the largest share."],
        ["", "Based on the pie graph featuring four categories in the image, from categories <1>, <2>, <3>, and <4>, category <5> holds the highest ratio."]
    ],
    "area_1_2": [
        ["", "In the image, there is a pie graph with five categories. From categories <1>, <2>, <3>, <4>, and <5>, category <6> has the largest ratio."],
        ["", "Refer to the pie chart in the image that includes five segments. From segments <1>, <2>, <3>, <4>, and <5>, category <6> represents the highest proportion."],
        ["", "Looking at the pie diagram with five divisions, from categories <1>, <2>, <3>, <4>, and <5>, category <6> occupies the greatest percentage."],
        ["", "Examine the pie chart in the image with five sections. Among sections <1>, <2>, <3>, <4>, and <5>, section <6> has the largest share."],
        ["", "Based on the pie graph featuring five categories in the image, from categories <1>, <2>, <3>, <4>, and <5>, category <6> holds the highest ratio."]
    ],
    "area_1_3": [
        ["", "In the image, there is a pie graph with three categories. From categories <1>, <2>, and <3>, category <4> has the largest ratio."],
        ["", "Refer to the pie chart in the image that includes three segments. From segments <1>, <2>, and <3>, category <4> represents the highest proportion."],
        ["", "Looking at the pie diagram with three divisions, from categories <1>, <2>, and <3>, category <4> occupies the greatest percentage."],
        ["", "Examine the pie chart in the image with three sections. Among sections <1>, <2>, and <3>, section <4> has the largest share."],
        ["", "Based on the pie graph featuring three categories in the image, from categories <1>, <2>, and <3>, category <4> holds the highest ratio."]
    ],
    "area_1_4": [
        ["", "In the image, there is a pie graph with six categories. From categories <1>, <2>, <3>, <4>, <5>, and <6>, category <7> has the largest ratio."],
        ["", "Refer to the pie chart in the image that includes six segments. From segments <1>, <2>, <3>, <4>, <5>, and <6>, category <7> represents the highest proportion."],
        ["", "Looking at the pie diagram with six divisions, from categories <1>, <2>, <3>, <4>, <5>, and <6>, category <7> occupies the greatest percentage."],
        ["", "Examine the pie chart in the image with six sections. Among sections <1>, <2>, <3>, <4>, <5>, and <6>, section <7> has the largest share."],
        ["", "Based on the pie graph featuring six categories in the image, from categories <1>, <2>, <3>, <4>, <5>, and <6>, category <7> holds the highest ratio."]
    ],
    "area_1_5": [
        ["", "In the image, there is a pie graph with two categories. From categories <1> and <2>, category <3> has the largest ratio."],
        ["", "Refer to the pie chart in the image that includes two segments. From segments <1> and <2>, category <3> represents the highest proportion."],
        ["", "Looking at the pie diagram with two divisions, from categories <1> and <2>, category <3> occupies the greater percentage."],
        ["", "Examine the pie chart in the image with two sections. Among sections <1> and <2>, section <3> has the largest share."],
        ["", "Based on the pie graph featuring two categories in the image, from categories <1> and <2>, category <3> holds the highest ratio."]
    ],
    "area_2_1": [
        ["", "In the given image, area <1> occupies a <3> region than area <2>."],
        ["", "In the image, area <1> covers a <3> area compared to area <2>."],
        ["", "Area <1> takes up a <3> portion than area <2>."],
        ["", "In the illustration, area <1> has a <3> size than area <2>."],
        ["", "Area <1> occupies a <3> space relative to area <2>."]
    ],
    "area_2_2": [
        ["", "In the given image, area <1> occupies a <4> region than area <2>, and area <2> occupies a <5> region than area <3>."],
        ["", "In the image, area <1> covers a <4> area compared to area <2>, and area <2> covers a <5> area compared to area <3>."],
        ["", "Area <1> takes up a <4> portion than area <2>, and area <2> takes up a <5> portion than area <3>."],
        ["", "In the illustration, area <1> has a <4> size than area <2>, and area <2> has a <5> size than area <3>."],
        ["", "Area <1> occupies a <4> space relative to area <2>, and area <2> occupies a <5> space relative to area <3>."]
    ]
}


conversation_short = {
        "area_1_1": [
            [
                "In the image, there is a pie graph with four categories. Which category has the largest ratio? Choose from <1>, <2>, <3>, and <4>.",
                "<5>"
            ],
            [
                "Refer to the image's pie chart that contains four segments. Which segment represents the highest proportion? Select from <1>, <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "Looking at the pie diagram with four divisions, which category occupies the greatest percentage? Choose between <1>, <2>, <3>, and <4>.",
                "<5>"
            ],
            [
                "Examine the pie chart in the image with four sections. Which section has the largest share? Pick from <1>, <2>, <3>, or <4>.",
                "<5>"
            ],
            [
                "Based on the pie graph featuring four categories in the image, which category holds the highest ratio? Select from <1>, <2>, <3>, and <4>.",
                "<5>"
            ]
        ],
        "area_1_2": [
            [
                "In the image, there is a pie graph with five categories. Which category has the largest ratio? Choose from <1>, <2>, <3>, <4>, and <5>.",
                "<6>"
            ],
            [
                "Refer to the pie chart in the image that includes five segments. Which segment represents the highest proportion? Select from <1>, <2>, <3>, <4>, or <5>.",
                "<6>"
            ],
            [
                "Looking at the pie diagram with five divisions, which category occupies the greatest percentage? Choose between <1>, <2>, <3>, <4>, and <5>.",
                "<6>"
            ],
            [
                "Examine the pie chart in the image with five sections. Which section has the largest share? Pick from <1>, <2>, <3>, <4>, or <5>.",
               "<6>"
            ],
            [
                "Based on the pie graph featuring five categories in the image, which category holds the highest ratio? Select from <1>, <2>, <3>, <4>, and <5>.",
                "<6>"
            ]
        ],
        "area_1_3": [
            [
                "In the image, there is a pie graph with three categories. Which category has the largest ratio? Choose from <1>, <2>, and <3>.",
                "<4>"
            ],
            [
                "Refer to the pie chart in the image that includes three segments. Which segment represents the highest proportion? Select from <1>, <2>, or <3>.",
                "<4>"
            ],
            [
                "Looking at the pie diagram with three divisions, which category occupies the greatest percentage? Choose between <1>, <2>, and <3>.",
                "<4>"
            ],
            [
                "Examine the pie chart in the image with three sections. Which section has the largest share? Pick from <1>, <2>, or <3>.",
                "<4>"
            ],
            [
                "Based on the pie graph featuring three categories in the image, which category holds the highest ratio? Select from <1>, <2>, and <3>.",
                "<4>"
            ]
        ],
        "area_1_4": [
            [
                "In the image, there is a pie graph with six categories. Which category has the largest ratio? Choose from <1>, <2>, <3>, <4>, <5>, and <6>.",
                "<7>"
            ],
            [
                "Refer to the pie chart in the image that includes six segments. Which segment represents the highest proportion? Select from <1>, <2>, <3>, <4>, <5>, or <6>.",
                "<7>"
            ],
            [
                "Looking at the pie diagram with six divisions, which category occupies the greatest percentage? Choose between <1>, <2>, <3>, <4>, <5>, and <6>.",
                "<7>"
            ],
            [
                "Examine the pie chart in the image with six sections. Which section has the largest share? Pick from <1>, <2>, <3>, <4>, <5>, or <6>.",
                "<7>"
            ],
            [
                "Based on the pie graph featuring six categories in the image, which category holds the highest ratio? Select from <1>, <2>, <3>, <4>, <5>, and <6>.",
                "<7>"
            ]
        ],
        "area_1_5": [
            [
                "In the image, there is a pie graph with two categories. Which category has the largest ratio? Choose from <1> and <2>.",
                "<3>"
            ],
            [
                "Refer to the pie chart in the image that includes two segments. Which segment represents the highest proportion? Select from <1> or <2>.",
                "<3>"
            ],
            [
                "Looking at the pie diagram with two divisions, which category occupies the greater percentage? Choose between <1> and <2>.",
                "<3>"
            ],
            [
                "Examine the pie chart in the image with two sections. Which section has the largest share? Pick from <1> or <2>.",
                "<3>"
            ],
            [
                "Based on the pie graph featuring two categories in the image, which category holds the highest ratio? Select from <1> and <2>.",
                "<3>"
            ]
        ],
        "area_2_1": [
            [
                "Choose the word in parentheses that correctly describes the image: In the given image, area <1> occupies a (larger/smaller) region than area <2>.",
                "<3>"
            ],
            [
                "Select the appropriate word from the parentheses to describe the image: In the image, area <1> covers a (larger/smaller) area compared to area <2>.",
                "<3>"
            ],
            [
                "Pick the correct term from the options in parentheses to accurately describe the image: Area <1> takes up a (larger/smaller) portion than area <2>.",
                "<3>"
            ],
            [
                "Choose the suitable word from the parentheses to describe the image: In the illustration, area <1> has a (larger/smaller) size than area <2>.",
                "<3>"
            ],
            [
                "Select the correct word in parentheses to accurately describe the image: Area <1> occupies a (larger/smaller) space relative to area <2>.",
                "<3>"
            ]
        ],
        "area_2_2": [
            [
                "Choose the word in parentheses that correctly describes the image: In the given image, area <1> occupies a (larger/smaller) region than area <2>, and area <2> occupies a (larger/smaller) region than area <3>.",
                "<4>, <5>"
            ],
            [
                "Select the appropriate words from the parentheses to describe the image: In the image, area <1> covers a (larger/smaller) area compared to area <2>, and area <2> covers a (larger/smaller) area compared to area <3>.",
                "<4>, <5>"
            ],
            [
                "Pick the correct terms from the options in parentheses to accurately describe the image: Area <1> takes up a (larger/smaller) portion than area <2>, and area <2> takes up a (larger/smaller) portion than area <3>.",
                "<4>, <5>"
            ],
            [
                "Choose the suitable words from the parentheses to describe the image: In the illustration, area <1> has a (larger/smaller) size than area <2>, and area <2> has a (larger/smaller) size than area <3>.",
                "<4>, <5>"
            ],
            [
                "Select the correct words in parentheses to accurately describe the image: Area <1> occupies a (larger/smaller) space relative to area <2>, and area <2> occupies a (larger/smaller) space relative to area <3>.",
                "<4>, <5>"
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