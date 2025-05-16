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
        "reflection_1": [
            [
                "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, which one is most likely the line of reflection such that point <1> is the reflection of point <2> with respect to it?",
                "Point <1> is most likely the reflection of point <2> with respect to line <3><4>."
            ],
            [
                "Among lines <3><5>, <3><6>, <3><7>,and <3><8>, which is the most likely line of reflection such that point <1> corresponds to the reflection of point <2> across it?",
                "Point <1> is most likely the reflection of point <2> over line <3><4>."
            ],
            [
                "Which line, among <3><5>, <3><6>, <3><7>, and <3><8>, is most likely the reflection axis where point <1> reflects to point <2>?",
                "Point <1> is most likely reflected from point <2> with line <3><4> as the axis."
            ],
            [
                "Out of lines <3><5>, <3><6>, <3><7>, and <3><8>, which one is most probably the reflection line such that point <1> is reflected from point <2>?",
                "Point <1> is most likely reflected from point <2> across line <3><4>."
            ],
            [
                "Which of the lines <3><5>, <3><6>, <3><7>, or <3><8> most likely serves as the line of reflection for point <1> and point <2>?",
                "Point <1> is most likely reflected from point <2> with respect to line <3><4>."
            ],
            [
                "From lines <3><5>, <3><6>, <3><7>, and <3><8>, which is most likely the reflection axis such that point <1> mirrors point <2>?",
                "Point <1> is most likely the mirror image of point <2> with line <3><4> as the axis."
            ],
            [
                "Considering lines <3><5>, <3><6>, <3><7>, and <3><8>, which one is most likely the axis of reflection such that point <1> reflects to point <2>?",
                "Point <1> is most likely the reflection of point <2> with respect to line <3><4>."
            ],
            [
                "Which line, among <3><5>, <3><6>, <3><7>, and <3><8>, is most likely the reflection axis where point <1> is reflected from point <2>?",
                "Point <1> is most likely reflected from point <2> across line <3><4>."
            ],
            [
                "Among the lines <3><5>, <3><6>, <3><7>, and <3><8>, which is most likely the line where point <1> is reflected with respect to point <2>?",
                "Point <1> is most likely reflected with respect to point <2> over line <3><4>."
            ],
            [
                "From lines <3><5>, <3><6>, <3><7>, and <3><8> which one serves as the most likely line of reflection where point <1> mirrors point <2>?",
                "Point <1> is most likely the mirror image of point <2> along line <3><4>."
            ],
            [
                "Considering lines <3><5>, <3><6>, <3><7>, and <3><8>, which is the most probable reflection line for point <1> relative to point <2>?",
                "Point <1> is most likely the reflection of point <2> with respect to line <3><4>."
            ]
        ],
        "reflection_2": [
            [
                "There are four sub-images labeled as <1>, <2>, <3>, and <4> in the given image. Three of them are line symmetric, but one is not. Choose the one that is not line symmetric. You should choose your answer from <1>, <2>, <3>, or <4>.",
                "The shape marked as <5> does not possess line symmetry."
            ],
            [
                "In the image provided, four sub-images are labeled as <1>, <2>, <3>, and <4>. While most of them are line symmetric, one is not. Identify the shape that lacks line symmetry by choosing from <1>, <2>, <3>, or <4>.",
                "Sub-image <5> is the one without line symmetry."
            ],
            [
                "Four sub-images labeled <1>, <2>, <3>, and <4> are shown in the given image. Only one of them is not line symmetric. Select the asymmetric sub-image from <1>, <2>, <3>, or <4>.",
                "Sub-image labeled as <5> breaks the line symmetry."
            ],
            [
                "The given image contains four sub-images labeled as <1>, <2>, <3>, and <4>. Three of them are line symmetric, but one is not. Choose the shape without line symmetry from <1>, <2>, <3>, or <4>.",
                "The shape identified as <5> is not line symmetric."
            ],
            [
                "In the diagram, there are four sub-images labeled as <1>, <2>, <3>, and <4>. Among them, one is not line symmetric. Identify the shape without line symmetry by choosing from <1>, <2>, <3>, or <4>.",
                "Shape <5> is asymmetric and lacks line symmetry."
            ],
            [
                "Four sub-images are labeled as <1>, <2>, <3>, and <4> in the provided image. Three of these shapes are line symmetric, but one is not. Select the shape that lacks line symmetry from <1>, <2>, <3>, or <4>.",
                "The asymmetric shape is the one labeled <5>."
            ],
            [
                "The provided image contains four sub-images labeled as <1>, <2>, <3>, and <4>. Three of them exhibit line symmetry, but one does not. Pick the shape that is not line symmetric from <1>, <2>, <3>, or <4>.",
                "Sub-image <5> stands out as it does not show line symmetry."
            ],
            [
                "Four labeled sub-images <1>, <2>, <3>, and <4> are presented in the image. Three of these shapes are line symmetric, while one is not. Determine the asymmetric shape from <1>, <2>, <3>, or <4>.",
                "The shape marked <5> lacks line symmetry and is the answer."
            ],
            [
                "In the given image, there are four labeled sub-images: <1>, <2>, <3>, and <4>. One of these shapes does not exhibit line symmetry. Identify the odd one out by choosing from <1>, <2>, <3>, or <4>.",
                "Shape <5> is the one that fails to exhibit line symmetry."
            ],
            [
                "Four sub-images labeled <1>, <2>, <3>, and <4> are displayed in the image. All but one of these shapes are line symmetric. Select the shape that is not line symmetric from the provided options.",
                "Sub-image <5> is not line symmetric, unlike the others."
            ]
        ],
        "reflection_3": [
            [
                "There are four sub-images in the given image. One of them is line symmetric, but the others are not. Choose the one that is line symmetric. You should choose your answer from <1>, <2>, <3>, or <4>.",
                "The correct answer is <5>."
            ],
            [
                "Among the four sub-images shown in the image, only one is line symmetric, while the rest are not. Identify the line-symmetric sub-image by choosing from <1>, <2>, <3>, or <4>.",
                "Sub-image <5> is line symmetric."
            ],
            [
                "The image contains four sub-images. Three of them lack line symmetry, but one of them is line symmetric. Choose the line-symmetric sub-image from <1>, <2>, <3>, or <4>.",
                "<5> is the shape that is line symmetric."
            ],
            [
                "In the given image, there are four sub-images. Only one exhibits line symmetry, and the other three do not. Identify the line-symmetric sub-image from <1>, <2>, <3>, or <4>.",
                "The sub-image labeled <5> is the line-symmetric one."
            ],
            [
                "Four sub-images are shown in the image. One of them has line symmetry, while the others do not. Determine the line-symmetric sub-image by selecting from <1>, <2>, <3>, or <4>.",
                "Sub-image <5> possesses line symmetry."
            ],
            [
                "The provided image displays four sub-images. Only one of these sub-images is line symmetric. Select the line-symmetric sub-image from <1>, <2>, <3>, or <4>.",
                "<5> is the only shape with line symmetry."
            ],
            [
                "In the image, four sub-images are displayed. Among them, one exhibits line symmetry, while the rest do not. Choose the line-symmetric shape from <1>, <2>, <3>, or <4>.",
                "The correct choice is <5>, as it is line symmetric."
            ],
            [
                "Four sub-images are labeled in the image. Only one among them shows line symmetry, while the rest lack it. Identify the line-symmetric shape by choosing from <1>, <2>, <3>, or <4>.",
                "Shape <5> is the one that exhibits line symmetry."
            ],
            [
                "There are four sub-images in the given figure. One of these shapes is line symmetric, but the others are not. Determine the line-symmetric shape from the options <1>, <2>, <3>, or <4>.",
                "<5> is the shape with line symmetry."
            ],
            [
                "Among the four sub-images in the image, only one displays line symmetry. The other three are not line symmetric. Select the line-symmetric shape from <1>, <2>, <3>, or <4>.",
                "The line-symmetric shape is <5>."
            ]
        ],
        "reflection_4": [
            [
                "Two shapes depicted in the image are line-symmetric to each other. Among lines <1><2>, <1><3>, <1><4>, and <1><5> in the image, which one is most likely the line of reflection?",
                "Line <1><6>."
            ],
            [
                "In the image, two shapes are mirror images of each other. Considering lines <1><2>, <1><3>, <1><4>, and <1><5>, which line is most likely the axis of reflection?",
                "The axis of reflection is line <1><6>."
            ],
            [
                "The image shows two line-symmetric shapes. Among the lines <1><2>, <1><3>, <1><4>, and <1><5>, which one serves as the line of reflection?",
                "Line <1><6> serves as the line of reflection."
            ],
            [
                "There are two shapes in the image that are reflections of each other. Identify the most probable line of reflection from lines <1><2>, <1><3>, <1><4>, and <1><5>.",
                "The most probable line of reflection is <1><6>."
            ],
            [
                "In the given image, two shapes are symmetric with respect to a line. Which line among <1><2>, <1><3>, <1><4>, and <1><5> is likely the reflection line?",
                "The reflection line is <1><6>."
            ]
        ],
        "reflection_5": [
            [
                "The shape depicted in the image is line-symmetric. Among lines <1><2>, <1><3>, <1><4>, and <1><5> in the image, which one is most likely the line of reflection?",
                "Line <1><6>."
            ],
            [
                "In the image, a line-symmetric shape is present. Considering lines <1><2>, <1><3>, <1><4>, and <1><5>, which line serves as the axis of symmetry?",
                "The axis of symmetry is line <1><6>."
            ],
            [
                "The image features a line-symmetric shape. Among the lines <1><2>, <1><3>, <1><4>, and <1><5>, identify the most likely reflection line.",
                "Line <1><6> is the most likely reflection line."
            ],
            [
                "There is a line-symmetric shape in the image. Which line among <1><2>, <1><3>, <1><4>, and <1><5> is likely the line of reflection?",
                "The line of reflection is <1><6>."
            ],
            [
                "In the provided image, a shape exhibits line symmetry. Determine the reflection line from the options <1><2>, <1><3>, <1><4>, and <1><5>.",
                "The reflection line is <1><6>."
            ]
        ],
        
        "reflection_6": [
        [
            "Which figure among <1>, <2>, <3>, and <4> in the image most likely contains two shapes that are reflections of each other across the line separating them?",
            "Among the given figures, the shapes in figure <5> appear to exhibit line symmetry with respect to the provided line."
        ],
        [
            "Out of figures <1>, <2>, <3>, and <4> in the image, which one most likely shows two shapes that are mirror reflections across the separating line?",
            "The shapes in figure <5> seem to demonstrate line symmetry concerning the given line."
        ],
        [
            "Considering figures <1>, <2>, <3>, and <4> in the image, which one most likely features two shapes that are symmetrical reflections of each other with respect to the dividing line?",
            "Figure <5> contains shapes that are most likely line-symmetric relative to the given line."
        ],
        [
            "Among the figures <1>, <2>, <3>, and <4> shown in the image, which one most likely has two shapes that are reflections of each other across the line that separates them?",
            "The shapes in figure <5> are the ones that most likely demonstrate line symmetry with respect to the given line."
        ],
        [
            "From the given figures <1>, <2>, <3>, and <4> in the image, which figure best represents two shapes that are mirror images of each other along the dividing line?",
            "The shapes in figure <5> are most likely to display line symmetry in relation to the provided line."
        ]
    ]
    }
conversation_caption = {
    "reflection_1": [
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely the reflection of point <2> with respect to line <3><4>."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely the reflection of point <2> over line <3><4>."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely reflected from point <2> with line <3><4> as the axis."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely reflected from point <2> across line <3><4>."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely reflected from point <2> with respect to line <3><4>."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely the mirror image of point <2> with line <3><4> as the axis."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely the reflection of point <2> with respect to line <3><4>."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely reflected from point <2> across line <3><4>."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely reflected with respect to point <2> over line <3><4>."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely the mirror image of point <2> along line <3><4>."],
        ["", "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, point <1> is most likely the reflection of point <2> with respect to line <3><4>."]
    ],
    "reflection_2": [
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, the shape marked as <5> does not possess line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, sub-image <5> is the one without line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, sub-image labeled as <5> breaks the line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, the shape identified as <5> is not line symmetric."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, shape <5> is asymmetric and lacks line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, the asymmetric shape is the one labeled <5>."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, sub-image <5> stands out as it does not show line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, the shape marked <5> lacks line symmetry and is the answer."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, shape <5> is the one that fails to exhibit line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, sub-image <5> is not line symmetric, unlike the others."]
    ],
    "reflection_3": [
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, the correct answer is <5> as it is line symmetric."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, sub-image <5> is line symmetric."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, <5> is the shape that is line symmetric."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, the sub-image labeled <5> is the line-symmetric one."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, sub-image <5> possesses line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, <5> is the only shape with line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, the correct choice is <5>, as it is line symmetric."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, shape <5> is the one that exhibits line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, <5> is the shape with line symmetry."],
        ["", "In the image, among four sub-images labeled as <1>, <2>, <3>, and <4>, the line-symmetric shape is <5>."]
    ],
    "reflection_4": [
        ["", "In the image, two shapes are line-symmetric to each other, and line <1><6> is most likely the line of reflection."],
        ["", "In the image, two shapes are mirror images of each other, and the axis of reflection is line <1><6>."],
        ["", "In the image, two line-symmetric shapes exist, and line <1><6> serves as the line of reflection."],
        ["", "In the image, two shapes are reflections of each other, and the most probable line of reflection is <1><6>."],
        ["", "In the image, two shapes are symmetric with respect to a line, and the reflection line is <1><6>."]
    ],
    "reflection_5": [
        ["", "In the image, a line-symmetric shape is present, and line <1><6> is most likely the line of reflection."],
        ["", "In the image, a line-symmetric shape exists, and the axis of symmetry is line <1><6>."],
        ["", "In the image, a line-symmetric shape is shown, and line <1><6> is the most likely reflection line."],
        ["", "In the image, a line-symmetric shape is depicted, and the line of reflection is <1><6>."],
        ["", "In the image, a shape exhibits line symmetry, and the reflection line is <1><6>."]
    ]
}

conversation_short = {
    "reflection_1": [
        [
            "Among lines <3><5>, <3><6>, <3><7>, and <3><8>, which one is most likely the line of reflection such that point <1> is the reflection of point <2> with respect to it?",
            "<3><4>"
        ],
        [
            "Among lines <3><5>, <3><6>, <3><7>,and  <3><8>, which is the most likely line of reflection such that point <1> corresponds to the reflection of point <2> across it?",
            "<3><4>"
        ],
        [
            "Which line, among <3><5>, <3><6>, <3><7>, and <3><8>, is most likely the reflection axis where point <1> reflects to point <2>?",
            "<3><4>"
        ],
        [
            "Out of lines <3><5>, <3><6>, <3><7>, and <3><8>, which one is most probably the reflection line such that point <1> is reflected from point <2>?",
            "<3><4>"
        ],
        [
            "Which of the lines <3><5>, <3><6>, <3><7>, or <3><8> most likely serves as the line of reflection for point <1> and point <2>?",
            "<3><4>"
        ],
        [
            "From lines <3><5>, <3><6>, <3><7>, and <3><8>, which is most likely the reflection axis such that point <1> mirrors point <2>?",
            "<3><4>"
        ],
        [
            "Considering lines <3><5>, <3><6>, <3><7>, and <3><8>, which one is most likely the axis of reflection such that point <1> reflects to point <2>?",
            "<3><4>"
        ],
        [
            "Which line, among <3><5>, <3><6>, <3><7>, and <3><8>, is most likely the reflection axis where point <1> is reflected from point <2>?",
            "<3><4>"
        ],
        [
            "Among the lines <3><5>, <3><6>, <3><7>, and <3><8>, which is most likely the line where point <1> is reflected with respect to point <2>?",
            "<3><4>"
        ],
        [
            "From lines <3><5>, <3><6>, <3><7>, and <3><8> which one serves as the most likely line of reflection where point <1> mirrors point <2>?",
            "<3><4>"
        ],
        [
            "Considering lines <3><5>, <3><6>, <3><7>, and <3><8>, which is the most probable reflection line for point <1> relative to point <2>?",
            "<3><4>"
        ]
    ],
    "reflection_2": [
        [
            "There are four sub-images labeled as <1>, <2>, <3>, and <4> in the given image. Three of them are line symmetric, but one is not. Choose the one that is not line symmetric. You should choose your answer from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "In the image provided, four sub-images are labeled as <1>, <2>, <3>, and <4>. While most of them are line symmetric, one is not. Identify the shape that lacks line symmetry by choosing from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Four sub-images labeled <1>, <2>, <3>, and <4> are shown in the given image. Only one of them is not line symmetric. Select the asymmetric sub-image from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "The given image contains four sub-images labeled as <1>, <2>, <3>, and <4>. Three of them are line symmetric, but one is not. Choose the shape without line symmetry from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "In the diagram, there are four sub-images labeled as <1>, <2>, <3>, and <4>. Among them, one is not line symmetric. Identify the shape without line symmetry by choosing from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Four sub-images are labeled as <1>, <2>, <3>, and <4> in the provided image. Three of these shapes are line symmetric, but one is not. Select the shape that lacks line symmetry from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "The provided image contains four sub-images labeled as <1>, <2>, <3>, and <4>. Three of them exhibit line symmetry, but one does not. Pick the shape that is not line symmetric from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Four labeled sub-images <1>, <2>, <3>, and <4> are presented in the image. Three of these shapes are line symmetric, while one is not. Determine the asymmetric shape from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "In the given image, there are four labeled sub-images: <1>, <2>, <3>, and <4>. One of these shapes does not exhibit line symmetry. Identify the odd one out by choosing from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Four sub-images labeled <1>, <2>, <3>, and <4> are displayed in the image. All but one of these shapes are line symmetric. Select the shape that is not line symmetric from the provided options.",
            "<5>"
        ]
    ],
    "reflection_3": [
        [
            "There are four sub-images in the given image. One of them is line symmetric, but the others are not. Choose the one that is line symmetric. You should choose your answer from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Among the four sub-images shown in the image, only one is line symmetric, while the rest are not. Identify the line-symmetric sub-image by choosing from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "The image contains four sub-images. Three of them lack line symmetry, but one of them is line symmetric. Choose the line-symmetric sub-image from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "In the given image, there are four sub-images. Only one exhibits line symmetry, and the other three do not. Identify the line-symmetric sub-image from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Four sub-images are shown in the image. One of them has line symmetry, while the others do not. Determine the line-symmetric sub-image by selecting from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "The provided image displays four sub-images. Only one of these sub-images is line symmetric. Select the line-symmetric sub-image from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "In the image, four sub-images are displayed. Among them, one exhibits line symmetry, while the rest do not. Choose the line-symmetric shape from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Four sub-images are labeled in the image. Only one among them shows line symmetry, while the rest lack it. Identify the line-symmetric shape by choosing from <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "There are four sub-images in the given figure. One of these shapes is line symmetric, but the others are not. Determine the line-symmetric shape from the options <1>, <2>, <3>, or <4>.",
            "<5>"
        ],
        [
            "Among the four sub-images in the image, only one displays line symmetry. The other three are not line symmetric. Select the line-symmetric shape from <1>, <2>, <3>, or <4>.",
            "<5>"
        ]
    ],
    "reflection_4": [
        [
            "Two shapes depicted in the image are line-symmetric to each other. Among lines <1><2>, <1><3>, <1><4>, and <1><5> in the image, which one is most likely the line of reflection?",
            "<1><6>"
        ],
        [
            "In the image, two shapes are mirror images of each other. Considering lines <1><2>, <1><3>, <1><4>, and <1><5>, which line is most likely the axis of reflection?",
            "<1><6>"
        ],
        [
            "The image shows two line-symmetric shapes. Among the lines <1><2>, <1><3>, <1><4>, and <1><5>, which one serves as the line of reflection?",
            "<1><6>"
        ],
        [
            "There are two shapes in the image that are reflections of each other. Identify the most probable line of reflection from lines <1><2>, <1><3>, <1><4>, and <1><5>.",
            "<1><6>"
        ],
        [
            "In the given image, two shapes are symmetric with respect to a line. Which line among <1><2>, <1><3>, <1><4>, and <1><5> is likely the reflection line?",
            "<1><6>"
        ]
    ],
    "reflection_5": [
        [
            "The shape depicted in the image is line-symmetric. Among lines <1><2>, <1><3>, <1><4>, and <1><5> in the image, which one is most likely the line of reflection?",
            "<1><6>"
        ],
        [
            "In the image, a line-symmetric shape is present. Considering lines <1><2>, <1><3>, <1><4>, and <1><5>, which line serves as the axis of symmetry?",
            "<1><6>"
        ],
        [
            "The image features a line-symmetric shape. Among the lines <1><2>, <1><3>, <1><4>, and <1><5>, identify the most likely reflection line.",
            "<1><6>"
        ],
        [
            "There is a line-symmetric shape in the image. Which line among <1><2>, <1><3>, <1><4>, and <1><5> is likely the line of reflection?",
            "<1><6>"
        ],
        [
            "In the provided image, a shape exhibits line symmetry. Determine the reflection line from the options <1><2>, <1><3>, <1><4>, and <1><5>.",
            "<1><6>"
        ]
    ],
        "reflection_6": [
        [
            "Which figure among <1>, <2>, <3>, and <4> in the image most likely contains two shapes that are reflections of each other across the line separating them?",
            "<5>"
        ],
        [
            "Out of figures <1>, <2>, <3>, and <4> in the image, which one most likely shows two shapes that are mirror reflections across the separating line?",
            "<5>"
        ],
        [
            "Considering figures <1>, <2>, <3>, and <4> in the image, which one most likely features two shapes that are symmetrical reflections of each other with respect to the dividing line?",
            "<5>"
        ],
        [
            "Among the figures <1>, <2>, <3>, and <4> shown in the image, which one most likely has two shapes that are reflections of each other across the line that separates them?",
            "<5>"
        ],
        [
            "From the given figures <1>, <2>, <3>, and <4> in the image, which figure best represents two shapes that are mirror images of each other along the dividing line?",
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