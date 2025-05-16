from .rules import *
import random

conversation = {
    "conversation_long": {
        "boundary1": {
            "QA": [
                [
                    "A <1> is filled with <2>, and a <3>-colored line is drawn. Does this <3>-colored line accurately mark the boundary of the <1> with the <2> interior?",
                    "Yes, the <3>-colored line precisely forms the boundary of the <1> shape."
                ],
                [
                    "In the figure, you see a <1> with its interior colored <2>, alongside a <3>-colored line. Does the <3>-colored line exactly form the boundary of this <1>?",
                    "Indeed, the <3>-colored line exactly represents the boundary of <1>."
                ],
                [
                    "There is a <1> painted <2> inside and a <3>-colored outline. Does this <3>-colored outline perfectly match the boundary of the <1>?",
                    "Yes, the <3>-colored line perfectly matches the boundary of the <1>."
                ],
                [
                    "Observe the <1> filled with <2> and the line drawn in <3>. Is that <3>-colored line the precise boundary of the <1>?",
                    "Yes, the <3>-colored line serves precisely as the boundary of <1>."
                ],
                [
                    "You have a <1> whose interior is <2> and a <3>-colored line surrounding it. Does this <3>-colored line completely outline the boundary of the <1>?",
                    "Yes, the <3>-colored line completely outlines the <1> as its boundary."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    ""
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "Please choose Yes or No for your answer.",
                    "The response must be either Yes or No.",
                    "Select Yes or No as the correct answer.",
                    "The answer should be chosen from Yes/No.",
                    "Pick either Yes or No to respond."
                ]
            }
        },
        "boundary2": {
            "QA": [
                [
                    "A <1> is filled with <2>, and a <3>-colored line is drawn. Does the <3>-colored line accurately mark the boundary of the <1> with the <2> interior?",
                    "No, the <3>-colored line does not precisely form the boundary of the <1>."
                ],
                [
                    "In the figure, there is a <1> whose interior is <2> and a <3>-colored line. Is this <3>-colored line truly the exact boundary of the <1>?",
                    "No, the <3>-colored line does not exactly match the boundary of the <1>."
                ],
                [
                    "We have a <1> colored <2> inside and a <3>-colored line on the figure. Does that <3>-colored line serve as a perfect boundary for the <1>?",
                    "No, the <3>-colored line fails to align perfectly with the boundary of the <1>."
                ],
                [
                    "Observe the <1> with its interior in <2> and a line drawn in <3>. Does this <3>-colored line form the precise boundary of the <1>?",
                    "No, the <3>-colored line does not form the precise boundary of <1>."
                ],
                [
                    "Look at the <1> having an interior of <2> and a line in <3>. Is the <3>-colored line exactly outlining the <1> boundary?",
                    "No, the <3>-colored line is not the exact boundary of the <1>."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    ""
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "Please choose Yes or No for your answer.",
                    "The response must be either Yes or No.",
                    "Select Yes or No as the correct answer.",
                    "The answer should be chosen from Yes/No.",
                    "Pick either Yes or No to respond."
                ]
            }
        },
        "boundary3": {
            "QA": [
                [
                    "Does the given shape in the figure have a boundary that differs in color from its interior?",
                    "Yes, the shape in the figure has a boundary colored <3> while its interior is <2>, so they differ."
                ],
                [
                    "In this illustration, is there a shape whose boundary color is distinct from its <2>-colored interior?",
                    "Indeed, the outer boundary is <3>, whereas the interior is <2>."
                ],
                [
                    "Check if the figure’s shape features a differently colored outline compared to the <2> interior. Is that the case?",
                    "Yes, the boundary is <3>, making it different from the <2> interior."
                ],
                [
                    "Observe the shape with an interior of <2>. Does it have a perimeter colored <3>, signifying a different color than its interior?",
                    "Yes, it does. The shape’s perimeter is <3>, distinct from the <2> fill."
                ],
                [
                    "Is the boundary color in the given shape different from the <2>-colored fill?",
                    "Yes, the boundary color is <3>, indicating a different color from the interior <2>."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    ""
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "Please choose Yes or No for your answer.",
                    "The response must be either Yes or No.",
                    "Select Yes or No as the correct answer.",
                    "The answer should be chosen from Yes/No.",
                    "Pick either Yes or No to respond.",
                    "You must respond with Yes or No."
                ]
            }
        },
        "boundary4": {
            "QA": [
                [
                    "Does the shape in the provided figure have a boundary colored differently than its interior?",
                    "No, the shape does not show a distinct boundary color; the boundary color isn’t observed to differ from its <2> interior."
                ],
                [
                    "In the figure, can you see if the boundary color of the shape is different from the <2> interior color?",
                    "No, there is no differently colored boundary visible; it appears only <2>."
                ],
                [
                    "Is there a boundary with a color that stands out from the <2>-colored interior in the diagram?",
                    "No, the diagram doesn’t exhibit a boundary with a different color; it remains <2>."
                ],
                [
                    "Check if the shape’s perimeter has a color that differs from <2>. Is such a boundary visible?",
                    "No, we do not see a separate color <3>; it’s not observed in the figure."
                ],
                [
                    "Does the shape maintain a distinct <3>-colored edge separate from the <2> interior?",
                    "No, there’s no <3>-colored boundary contrasting the <2> interior here."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    ""
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "Please choose Yes or No for your answer.",
                    "The response must be either Yes or No.",
                    "Select Yes or No as the correct answer.",
                    "The answer should be chosen from Yes/No.",
                    "Pick either Yes or No to respond."
                ]
            }
        },
        "boundary5": {
            "QA": [
                [
                    "In the given figure, name the line that separates area <3> from area <4>.",
                    "The line segment <5> divides area <3> from area <4>."
                ],
                [
                    "Which line serves as the boundary between area <3> and area <4> in the drawing?",
                    "Line segment <5> is the dividing boundary between area <3> and area <4>."
                ],
                [
                    "Identify the line that marks the border separating area <3> and area <4> in the provided figure.",
                    "The segment <5> marks the boundary between area <3> and area <4>."
                ],
                [
                    "Point out the specific line that acts as the partition for area <3> from area <4> in this diagram.",
                    "It is the line segment <5> that separates area <3> from area <4>."
                ],
                [
                    "Which line in the illustration creates the boundary between area <3> and area <4>?",
                    "The boundary is drawn by line segment <5> between area <3> and area <4>."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    [
                        "Select one word from the parentheses to complete the sentence. The segment <1> divides area <3> and <4>.",
                        "The segment <5> divides area <3> and <4>."
                    ],
                    [
                        "Choose a word from the given parentheses. The line <1> is what splits area <3> and <4>.",
                        "The line <5> is what splits area <3> and <4>."
                    ],
                    [
                        "Pick the correct option to finish the sentence. The boundary <1> separates area <3> from area <4>.",
                        "The boundary <5> separates area <3> from area <4>."
                    ],
                    [
                        "Fill in the blank from the choices in parentheses. The line <1> forms the division between area <3> and <4>.",
                        "The line <5> forms the division between area <3> and <4>."
                    ],
                    [
                        "Complete the sentence using the parentheses. The segment <1> is the boundary for area <3> and <4>.",
                        "The segment <5> is the boundary for area <3> and <4>."
                    ]
                ],
                "type3": [
                    "For instance, if the line between points A and B separates area <3> and <4>, you should answer AB.",
                    "If a segment AB divides area <3> from <4>, then 'AB' is the correct response.",
                    "For example, when points A and B form the boundary between area <3> and <4>, provide the answer as AB.",
                    "In case the boundary is the line from A to B for areas <3> and <4>, the reply should be AB.",
                    "As an illustration, if segment AB delineates area <3> and area <4>, answer with AB."
                ],
                "type4": [
                    "You must choose from <6> for the answer.",
                    "Pick the correct line from the options in <6>.",
                    "Select your answer from among <6>.",
                    "Your choice should be one of <6>.",
                    "The answer should be found in <6>."
                ]
            }
        },
        "boundary6": {
            "QA": [
                [
                    "In the given figure, multiple layers of <1> are shown. What is the color of the outermost boundary?",
                    "The outermost boundary in the figure is colored <4>."
                ],
                [
                    "Observe the overlapping <1> in the image. Which color does the outer boundary have?",
                    "Its outer boundary is <4>."
                ],
                [
                    "Among the multiple stacked <1> in the diagram, identify the color of the outermost boundary.",
                    "The color of the outermost boundary is <4>."
                ],
                [
                    "Looking at the various <1> layered in the figure, can you specify the color of the boundary on the very outside?",
                    "The boundary on the very outside is <4> in color."
                ],
                [
                    "In the illustration with multiple <1>, name the color of the boundary that lies outermost.",
                    "The color <4> is found on the outermost boundary of the figure."
                ]
            ],
            "additional": {
                "type1": [
                    "False"
                ],
                "type2": [
                    [
                        "Select one word from the parentheses to complete the sentence. In the figure, the color of the outermost boundary is <2>.",
                        "In the figure, the color of the outermost boundary is <4>."
                    ],
                    [
                        "Choose the correct color from the parentheses to finish the sentence. The outer boundary in the figure is <2>.",
                        "The outer boundary in the figure is <4>."
                    ],
                    [
                        "Pick the color option in parentheses to complete the statement. The figure's outermost boundary color is <2>.",
                        "The figure's outermost boundary color is <4>."
                    ],
                    [
                        "Fill in the blank from the parentheses. The outer boundary is <2> in this diagram.",
                        "The outer boundary is <4> in this diagram."
                    ],
                    [
                        "Complete the sentence using the parentheses. The color <2> appears on the outermost boundary of the figure.",
                        "The color <4> appears on the outermost boundary of the figure."
                    ]
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "You must select from <3> for your answer.",
                    "Please pick the color from <3>.",
                    "Choose the correct color from <3>.",
                    "Select your answer among the options in <3>.",
                    "The color should be one from <3>."
                ]
            }
        }
    },
    "conversation_short": {
        "boundary1": {
            "QA": [
                [
                    "Is the <3>-colored line precisely the boundary of a <1> filled with <2>?",
                    "Yes"
                ],
                [
                    "Does the <3>-colored line perfectly outline the <1> that has a <2>-colored interior?",
                    "Yes"
                ],
                [
                    "Is the boundary of the <1>, which is <2> inside, formed exactly by the <3>-colored line?",
                    "Yes"
                ],
                [
                    "Check if the line in <3> color is exactly the boundary of the <1> with <2> fill.",
                    "Yes"
                ],
                [
                    "Determine whether the <3>-colored line is truly the boundary of the <2>-colored <1>.",
                    "Yes"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    ""
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "Please choose Yes or No for your answer.",
                    "The response must be either Yes or No.",
                    "Select Yes or No as the correct answer.",
                    "The answer should be chosen from Yes/No.",
                    "Pick either Yes or No to respond."
                ]
            }
        },
        "boundary2": {
            "QA": [
                [
                    "Is the <3>-colored line precisely the boundary of a <1> filled with <2>?",
                    "No"
                ],
                [
                    "Does the <3>-colored line perfectly outline the <1> that has a <2>-colored interior?",
                    "No"
                ],
                [
                    "Is the boundary of the <1>, which is <2> inside, formed exactly by the <3>-colored line?",
                    "No"
                ],
                [
                    "Check if the line in <3> color is exactly the boundary of the <1> with <2> fill.",
                    "No"
                ],
                [
                    "Determine whether the <3>-colored line is truly the boundary of the <2>-colored <1>.",
                    "No"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    ""
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "Please choose Yes or No for your answer.",
                    "The response must be either Yes or No.",
                    "Select Yes or No as the correct answer.",
                    "The answer should be chosen from Yes/No.",
                    "Pick either Yes or No to respond."
                ]
            }
        },
        "boundary3": {
            "QA": [
                [
                    "Does the shape have a boundary color different from the <2>-colored interior?",
                    "Yes"
                ],
                [
                    "Is there a differently colored boundary compared to the interior <2>?",
                    "Yes"
                ],
                [
                    "Check if the shape’s boundary, colored <3>, is distinct from its <2> interior.",
                    "Yes"
                ],
                [
                    "Is the outline color <3> different from the fill color <2>?",
                    "Yes"
                ],
                [
                    "Look at the shape’s perimeter. Does it differ in color from its <2> interior?",
                    "Yes"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    ""
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "Please choose Yes or No for your answer.",
                    "The response must be either Yes or No.",
                    "Select Yes or No as the correct answer.",
                    "The answer should be chosen from Yes/No.",
                    "Pick either Yes or No to respond."
                ]
            }
        },
        "boundary4": {
            "QA": [
                [
                    "Does the shape have a boundary color different from the <2>-colored interior?",
                    "No"
                ],
                [
                    "Is there a boundary in a color distinct from <2>?",
                    "No"
                ],
                [
                    "Check if the figure has a perimeter colored <3> rather than <2>.",
                    "No"
                ],
                [
                    "Is the <3>-colored boundary visible as different from the <2> interior?",
                    "No"
                ],
                [
                    "Observe if the shape's boundary is a color apart from <2>.",
                    "No"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    ""
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "Please choose Yes or No for your answer.",
                    "The response must be either Yes or No.",
                    "Select Yes or No as the correct answer.",
                    "The answer should be chosen from Yes/No.",
                    "Pick either Yes or No to respond."
                ]
            }
        },
        "boundary5": {
            "QA": [
                [
                    "Which line divides area <3> from area <4>?",
                    "<5>"
                ],
                [
                    "What is the name of the line segment separating area <3> and area <4>?",
                    "<5>"
                ],
                [
                    "Identify the line that forms the boundary between area <3> and area <4>.",
                    "<5>"
                ],
                [
                    "Which segment marks the border between area <3> and area <4>?",
                    "<5>"
                ],
                [
                    "Tell me the line that splits area <3> from area <4>.",
                    "<5>"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    "Select one word from the parentheses to complete the sentence. The segment <1> divides area <3> and <4>.",
                    "Choose a word from the given parentheses. The line <1> is what splits area <3> and <4>.",
                    "Pick the correct option to finish the sentence. The boundary <1> separates area <3> from area <4>.",
                    "Fill in the blank from the choices in parentheses. The line <1> forms the division between area <3> and <4>.",
                    "Complete the sentence using the parentheses. The segment <1> is the boundary for area <3> and <4>."
                ],
                "type3": [
                    "For instance, if the line between points A and B separates area <3> and <4>, you should answer AB.",
                    "If a segment AB divides area <3> from <4>, then 'AB' is the correct response.",
                    "For example, if AB is the dividing line for areas <3> and <4>, then 'AB' is correct.",
                    "Should the line from A to B be the boundary for areas <3> and <4>, answer AB.",
                    "In a case where A-B segment separates <3> from <4>, provide the answer as AB."
                ],
                "type4": [
                    "You must choose from <6> for the answer.",
                    "Pick the correct line from the options in <6>.",
                    "Select your answer from among <6>.",
                    "Your choice should be one of <6>.",
                    "The answer should be found in <6>."
                ]
            }
        },
        "boundary6": {
            "QA": [
                [
                    "What is the color of the outermost boundary among the multiple <1> in the figure?",
                    "<4>"
                ],
                [
                    "Name the color of the boundary on the very outside among the layered <1>.",
                    "<4>"
                ],
                [
                    "Which color appears on the outermost edge of the overlapping <1> in the figure?",
                    "<4>"
                ],
                [
                    "Identify the outermost boundary color in the diagram with several <1>.",
                    "<4>"
                ],
                [
                    "Among the stacked <1>, can you tell me the color of the outermost boundary?",
                    "<4>"
                ]
            ],
            "additional": {
                "type1": [
                    "False"
                ],
                "type2": [
                    "Select one word from the parentheses to complete the sentence. In the figure, the color of the outermost boundary is <2>.",
                    "Choose the correct color from the parentheses to finish the sentence. The outer boundary in the figure is <2>.",
                    "Pick the color option in parentheses to complete the statement. The figure's outermost boundary color is <2>.",
                    "Fill in the blank from the parentheses. The outer boundary is <2> in this diagram.",
                    "Complete the sentence using the parentheses. The color <2> appears on the outermost boundary of the figure."
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "You must select from <3> for your answer.",
                    "Please pick the color from <3>.",
                    "Choose the correct color from <3>.",
                    "Select your answer among the options in <3>.",
                    "The color should be one from <3>."
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
            a = a.replace(f"<{i+1}>", entity[1][i])
        conversation_list.append((q, a))
    return conversation_list