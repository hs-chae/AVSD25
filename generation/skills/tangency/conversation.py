from .rules import *
import random

conversation = {
    "conversation_long": {
        "tangency1": {
            "QA": [
                [
                    "In the figure, there is one straight line and one curve. Do they touch tangentially?",
                    "Yes, the line and the curve in the figure are tangent."
                ],
                [
                    "Observe the figure containing a single line and a single curve. Are they tangent to each other?",
                    "They are indeed tangent in the provided figure."
                ],
                [
                    "Look at the figure with one line and one curve. Do they meet at exactly one point of tangency?",
                    "Yes, the line and curve meet at a tangent point."
                ],
                [
                    "Does the figure, consisting of a single line and a single curve, show a tangential contact?",
                    "Yes, the line and the curve do have a point of tangential contact."
                ],
                [
                    "Check the figure that has one line and one curve. Are they tangent in this illustration?",
                    "Yes, in this illustration, the line and curve are tangent."
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
                    ""
                ]
            }
        },
        "tangency2": {
            "QA": [
                [
                    "In the figure, there is one straight line and one curve. Are they tangent to each other?",
                    "No, the line and curve in the figure are not tangent."
                ],
                [
                    "Look at the figure that shows a line and a curve. Do they meet tangentially?",
                    "No, they do not touch at a tangent point."
                ],
                [
                    "Does the provided diagram, consisting of a line and a curve, illustrate a tangential contact?",
                    "No, there is no tangential contact between them."
                ],
                [
                    "Are the single line and the single curve in this figure tangent to each other?",
                    "No, they are not tangent in the given diagram."
                ],
                [
                    "Check the figure with one line and one curve. Do they form a tangent?",
                    "No, they do not form a tangent in this figure."
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
                    ""
                ]
            }
        },
        "tangency3": {
            "QA": [
                [
                    "In the figure, there are two curves of different colors. Are these curves tangent to each other?",
                    "Yes, the two distinct-colored curves are tangent in this figure."
                ],
                [
                    "Look at the diagram showing two differently colored curves. Do they meet tangentially?",
                    "Yes, they do meet at a point of tangency."
                ],
                [
                    "Are the two colored curves in the provided illustration tangent?",
                    "Yes, these two curves do indeed touch tangentially."
                ],
                [
                    "Does the figure with a pair of curves in different colors demonstrate a tangential intersection?",
                    "Yes, the curves shown intersect at a tangent point."
                ],
                [
                    "Observe the two curves of varying colors. Are they tangent in the given diagram?",
                    "Yes, they are tangent in this diagram."
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
                    ""
                ]
            }
        },
        "tangency4": {
            "QA": [
                [
                    "In the figure, there are two curves of different colors. Are these curves tangent to each other?",
                    "No, the two differently colored curves do not form a tangent."
                ],
                [
                    "Look at the diagram showing two colored curves. Do they meet tangentially?",
                    "No, they do not meet at a tangent point."
                ],
                [
                    "Does the figure with two curves in distinct colors indicate a tangential intersection?",
                    "No, there is no tangential contact between them."
                ],
                [
                    "Are the pair of differently colored curves in the given illustration tangent?",
                    "No, they are not tangent in this figure."
                ],
                [
                    "In the diagram, do the two colored curves come into tangential contact?",
                    "No, these curves do not touch tangentially."
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
                    ""
                ]
            }
        },
        "tangency5": {
            "QA": [
                [
                    "The figure has one <1> and one line segment. In the given figure, do <1> and the line segment touch tangentially?",
                    "Yes, in this figure, <1> and the line segment are tangent."
                ],
                [
                    "Observe the diagram containing a single <1> and a single line segment. Are they tangent?",
                    "Yes, the <1> and the line segment shown are tangent."
                ],
                [
                    "Look at the figure with one <1> and one line segment. Are these two elements tangent to each other?",
                    "Yes, the <1> and the line segment do indeed form a tangent."
                ],
                [
                    "Is the single <1> and the single line segment in the diagram tangent?",
                    "Yes, in the provided diagram, <1> and the line segment meet at a tangent."
                ],
                [
                    "In the given illustration of one <1> and one line segment, are they tangent?",
                    "Yes, the <1> and the line segment are tangent in this illustration."
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
                    ""
                ]
            }
        },
        "tangency6": {
            "QA": [
                [
                    "The figure has one <1> and one line segment. In the given figure, do <1> and the line segment touch tangentially?",
                    "No, in this figure, <1> and the line segment are not tangent."
                ],
                [
                    "Observe the diagram containing a single <1> and a single line segment. Are they tangent?",
                    "No, the <1> and line segment shown do not meet tangentially."
                ],
                [
                    "Look at the figure with one <1> and one line segment. Do these two elements form a tangent?",
                    "No, the <1> and the line segment do not form a tangent."
                ],
                [
                    "Is the single <1> and the single line segment in the diagram tangent?",
                    "No, there is no tangential contact between them in this diagram."
                ],
                [
                    "In the given illustration of one <1> and one line segment, are they tangent?",
                    "No, the <1> and the line segment are not tangent."
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
                    ""
                ]
            }
        },
        "tangency7": {
            "QA": [
                [
                    "In the given figure, there is one straight line and one curve. Among their intersection points, select all the tangent points.",
                    "In the figure, the tangent points between the line and the curve are <1>."
                ],
                [
                    "Look at the diagram with a single line and a single curve. Which of their intersection points are tangent points?",
                    "The tangent points of the line and the curve in the figure are <1>."
                ],
                [
                    "Identify the tangent points among the intersection points of the line and curve shown in the figure.",
                    "Those tangent points of the line and curve are <1>."
                ],
                [
                    "In this illustration with one line and one curve, find all intersection points that serve as points of tangency.",
                    "The points of tangency between the line and the curve in the illustration are <1>."
                ],
                [
                    "From the figure presented, which intersection points between the line and curve are tangent intersections?",
                    "The tangent intersections of the line and curve are <1> in the figure."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    [
                        "Choose one word from the parentheses to complete the sentence: In the figure, the tangent points between the line and the curve are (<2>).",
                        "In the figure, the tangent points between the line and the curve are <1>."
                    ],
                    [
                        "Select the correct term from the parentheses to finish the sentence: The line and curve in the figure have tangent points (<2>).",
                        "The line and curve in the figure have tangent points <1>."
                    ],
                    [
                        "Pick one option in the parentheses to complete: The tangent intersections of the line and curve are (<2>).",
                        "The tangent intersections of the line and curve are <1>."
                    ],
                    [
                        "From the parentheses, choose the appropriate word to finalize this statement: The tangent points of the line and curve in the figure are (<2>).",
                        "The tangent points of the line and curve in the figure are <1>."
                    ],
                    [
                        "Decide which word in the parentheses correctly completes this: The line and curve's points of tangency are (<2>).",
                        "The line and curve's points of tangency are <1>."
                    ]
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "The correct answer should be selected from <3>.",
                    "You must pick your answer from among <3>.",
                    "Please choose the correct option from <3>.",
                    "Select the appropriate response from <3>.",
                    "Your answer must be one of the choices in <3>."
                ]
            }
        },
        "tangency8": {
            "QA": [
                [
                    "In the figure, there are two curves with different colors. Among their intersection points, which ones are points of tangency?",
                    "In the figure, the tangent points between the two curves are <1>."
                ],
                [
                    "Look at the diagram featuring two distinctly colored curves. Identify all tangent points among their intersections.",
                    "The tangent points between these two curves in the figure are <1>."
                ],
                [
                    "From the intersection points of the two differently colored curves, find all points where they are tangent.",
                    "Those points of tangency between the two curves are <1>."
                ],
                [
                    "In this illustration with two colored curves, which intersection points serve as tangential contacts?",
                    "The tangential intersections of the two curves are <1>."
                ],
                [
                    "Which intersection points are tangent points among the two curves drawn with distinct colors?",
                    "The tangent points of the two curves in the figure are <1>."
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    [
                        "Select one word from the parentheses to complete the sentence: In the figure, the tangent points between the two curves are (<2>).",
                        "In the figure, the tangent points between the two curves are <1>."
                    ],
                    [
                        "Choose the correct term from the parentheses to finish the sentence: The two curves in the figure have tangent points (<2>).",
                        "The two curves in the figure have tangent points <1>."
                    ],
                    [
                        "Pick one option in the parentheses to complete: The tangent intersections of the two curves are (<2>).",
                        "The tangent intersections of the two curves are <1>."
                    ],
                    [
                        "From the parentheses, choose the appropriate word to finalize this statement: The tangent points of the two curves in the figure are (<2>).",
                        "The tangent points of the two curves in the figure are <1>."
                    ],
                    [
                        "Decide which word in the parentheses correctly completes this: The two curves' points of tangency are (<2>).",
                        "The two curves' points of tangency are <1>."
                    ]
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "The correct answer should be selected from <3>.",
                    "You must pick your answer from among <3>.",
                    "Please choose the correct option from <3>.",
                    "Select the appropriate response from <3>.",
                    "Your answer must be one of the choices in <3>."
                ]
            }
        },
        "tangency9": {
            "QA": [
                [
                    "The figure shows <1> curves (none of which are straight) and one straight line colored <3>. Among these curves, which ones are tangent to the line at point <2>? State their colors.",
                    "The curves that are tangent to the line at point <2> have colors <4>."
                ],
                [
                    "Observe the diagram with <1> non-linear curves and a line of color <3>. Please identify all curves tangent to that line at point <2>, and give their colors.",
                    "The color(s) of the curves tangent to the line at point <2> is(are) <4>."
                ],
                [
                    "We have <1> curves and a <3>-colored line. Which of these curves meet the line tangentially at point <2>? Provide the colors.",
                    "The curves tangent to the line at point <2> appear in color(s) <4>."
                ],
                [
                    "In this figure of <1> non-straight curves and a line with color <3>, find which curves are tangent at point <2> on the line, and name their colors.",
                    "Those tangent curves at point <2> are colored <4>."
                ],
                [
                    "Look at the <1> curves and the <3>-colored line in the diagram. Among the curves, which ones are tangent to the line at point <2>? Indicate their color(s).",
                    "The curves tangent to the line at <2> are <4> in color."
                ]
            ],
            "additional": {
                "type1": [
                    "False"
                ],
                "type2": [
                    [
                        "Select one word from the parentheses to complete the sentence: The color of the curves tangent to the line at point <2> is (<5>).",
                        "The color of the curves tangent to the line at point <2> is <4>."
                    ],
                    [
                        "Choose the correct term in the parentheses to finish the sentence: The curves tangent to the line at <2> have color (<5>).",
                        "The curves tangent to the line at <2> have color <4>."
                    ],
                    [
                        "Pick one option in the parentheses to complete this: The line at point <2> is tangent to curves with color (<5>).",
                        "The line at point <2> is tangent to curves with color <4>."
                    ],
                    [
                        "From the parentheses, choose the appropriate word to finalize this statement: The curves that are tangent at point <2> are colored (<5>).",
                        "The curves that are tangent at point <2> are colored <4>."
                    ],
                    [
                        "Decide which word in the parentheses correctly completes this sentence: The curve(s) tangent to the <3> line at point <2> is(are) (<5>) in color.",
                        "The curve(s) tangent to the <3> line at point <2> is(are) <4> in color."
                    ]
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "You must choose your answer from <6>.",
                    "Pick the correct answer from among <6>.",
                    "Your response should come from the options in <6>.",
                    "Select your answer from <6>.",
                    "The correct choice must be taken from <6>."
                ]
            }
        }
    },
    "conversation_short": {
        "tangency1": {
            "QA": [
                [
                    "Is there a line and a curve in the figure that are tangent?",
                    "Yes"
                ],
                [
                    "Do the line and the curve in the figure touch at a single tangent point?",
                    "Yes"
                ],
                [
                    "Are the single line and curve shown in the figure tangent to each other?",
                    "Yes"
                ],
                [
                    "In the diagram with one line and one curve, do they form a tangent?",
                    "Yes"
                ],
                [
                    "Does the figure depict a tangent relationship between the line and curve?",
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
                    ""
                ]
            }
        },
        "tangency2": {
            "QA": [
                [
                    "Is the line and the curve in the figure tangent?",
                    "No"
                ],
                [
                    "Do the single line and curve depicted meet at a tangent point?",
                    "No"
                ],
                [
                    "Are they tangent in the provided figure?",
                    "No"
                ],
                [
                    "Does the figure show a tangential contact between the line and curve?",
                    "No"
                ],
                [
                    "Is there a tangent relationship in the diagram between the line and the curve?",
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
                    ""
                ]
            }
        },
        "tangency3": {
            "QA": [
                [
                    "Do the two differently colored curves in the figure form a tangent?",
                    "Yes"
                ],
                [
                    "Are the pair of curves in distinct colors tangent to each other?",
                    "Yes"
                ],
                [
                    "Does the diagram with two colored curves show them meeting tangentially?",
                    "Yes"
                ],
                [
                    "In the provided illustration, do the two curves of different colors touch at a tangent?",
                    "Yes"
                ],
                [
                    "Are these two colored curves tangent in the figure?",
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
                    ""
                ]
            }
        },
        "tangency4": {
            "QA": [
                [
                    "Are the two differently colored curves in the figure tangent to each other?",
                    "No"
                ],
                [
                    "Do the colored curves in the diagram meet at a tangent point?",
                    "No"
                ],
                [
                    "Is there a tangential intersection between these two curves of different colors?",
                    "No"
                ],
                [
                    "Does the figure show a tangent relationship between the distinct-colored curves?",
                    "No"
                ],
                [
                    "Are the two curves in separate colors tangent in the illustration?",
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
                    ""
                ]
            }
        },
        "tangency5": {
            "QA": [
                [
                    "Does the figure with one <1> and one line segment show them touching tangentially?",
                    "Yes"
                ],
                [
                    "Are the <1> and the line segment in the diagram tangent?",
                    "Yes"
                ],
                [
                    "Is the single <1> in the figure tangent to the line segment?",
                    "Yes"
                ],
                [
                    "Do the <1> and the line segment in the illustration form a tangent?",
                    "Yes"
                ],
                [
                    "Are the <1> and line segment shown in the figure tangent to each other?",
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
                    ""
                ]
            }
        },
        "tangency6": {
            "QA": [
                [
                    "Does the figure with one <1> and one line segment show them tangent?",
                    "No"
                ],
                [
                    "Are the <1> and the line segment in the diagram forming a tangent?",
                    "No"
                ],
                [
                    "Is the single <1> in the figure tangent to the line segment?",
                    "No"
                ],
                [
                    "Do the <1> and the line segment in the illustration meet tangentially?",
                    "No"
                ],
                [
                    "Are the <1> and line segment shown in the figure tangent to each other?",
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
                    ""
                ]
            }
        },
        "tangency7": {
            "QA": [
                [
                    "Which intersection points of the line and curve in the figure are tangent points?",
                    "<1>"
                ],
                [
                    "Identify all tangent intersections from the line-curve intersection points in the diagram.",
                    "<1>"
                ],
                [
                    "Find the line and curve's tangent points among their intersections.",
                    "<1>"
                ],
                [
                    "Which intersection points are tangential contacts between the line and the curve?",
                    "<1>"
                ],
                [
                    "Select all tangent points from the line-curve intersections shown.",
                    "<1>"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    "Choose one word from the parentheses to complete the sentence: In the figure, the tangent points between the line and the curve are (<2>).",
                    "Select the correct term from the parentheses to finish the sentence: The line and curve in the figure have tangent points (<2>).",
                    "Pick one option in the parentheses to complete: The tangent intersections of the line and curve are (<2>).",
                    "From the parentheses, choose the appropriate word to finalize this statement: The tangent points of the line and curve in the figure are (<2>).",
                    "Decide which word in the parentheses correctly completes this: The line and curve's points of tangency are (<2>)."
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "The correct answer should be selected from <3>.",
                    "You must pick your answer from among <3>.",
                    "Please choose the correct option from <3>.",
                    "Select the appropriate response from <3>.",
                    "Your answer must be one of the choices in <3>."
                ]
            }
        },
        "tangency8": {
            "QA": [
                [
                    "Which intersection points of the two differently colored curves are tangent points?",
                    "<1>"
                ],
                [
                    "Identify all tangent contacts among the intersections of the two colored curves.",
                    "<1>"
                ],
                [
                    "Find where the two curves with distinct colors are tangent among their intersection points.",
                    "<1>"
                ],
                [
                    "In the figure with two colored curves, which intersections are tangential points?",
                    "<1>"
                ],
                [
                    "Select the tangent points from the intersection points of the two differently colored curves.",
                    "<1>"
                ]
            ],
            "additional": {
                "type1": [
                    "True"
                ],
                "type2": [
                    "Select one word from the parentheses to complete the sentence: In the figure, the tangent points between the two curves are (<2>).",
                    "Choose the correct term from the parentheses to finish the sentence: The two curves in the figure have tangent points (<2>).",
                    "Pick one option in the parentheses to complete: The tangent intersections of the two curves are (<2>).",
                    "From the parentheses, choose the appropriate word to finalize this statement: The tangent points of the two curves in the figure are (<2>).",
                    "Decide which word in the parentheses correctly completes this: The two curves' points of tangency are (<2>)."
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "The correct answer should be selected from <3>.",
                    "You must pick your answer from among <3>.",
                    "Please choose the correct option from <3>.",
                    "Select the appropriate response from <3>.",
                    "Your answer must be one of the choices in <3>."
                ]
            }
        },
        "tangency9": {
            "QA": [
                [
                    "Among the <1> curves and the <3>-colored line in the figure, which curves are tangent at point <2>? Indicate their color.",
                    "<4>"
                ],
                [
                    "Find all curves that touch the <3>-colored line tangentially at point <2>. What color are they?",
                    "<4>"
                ],
                [
                    "In the diagram with <1> curves and a <3> line, which curves meet the line tangentially at <2>? State their color.",
                    "<4>"
                ],
                [
                    "Which curves among the <1> shown are tangent to the line of color <3> at point <2>? Provide the color(s).",
                    "<4>"
                ],
                [
                    "Identify the color of the curves that are tangent to the <3> line at point <2>.",
                    "<4>"
                ]
            ],
            "additional": {
                "type1": [
                    "False"
                ],
                "type2": [
                    "Select one word from the parentheses to complete the sentence: The color of the curves tangent to the line at point <2> is (<5>).",
                    "Choose the correct term in the parentheses to finish the sentence: The curves tangent to the line at <2> have color (<5>).",
                    "Pick one option in the parentheses to complete this: The line at point <2> is tangent to curves with color (<5>).",
                    "From the parentheses, choose the appropriate word to finalize this statement: The curves that are tangent at point <2> are colored (<5>).",
                    "Decide which word in the parentheses correctly completes this sentence: The curve(s) tangent to the <3> line at point <2> is(are) (<5>) in color."
                ],
                "type3": [
                    ""
                ],
                "type4": [
                    "You must choose your answer from <6>.",
                    "Pick the correct answer from among <6>.",
                    "Your response should come from the options in <6>.",
                    "Select your answer from <6>.",
                    "The correct choice must be taken from <6>."
                ]
            }
        }
    }
}



def generate_conversation(diagram, long=False):
    conversation_list = []
    question_type = None
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
    question_type = version_key
    return question_type, conversation_list