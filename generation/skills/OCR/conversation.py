from .rules import *

import random

conversation_long = {
    "ocr1": [
        [
            "Is there <1> in the image?",
            "Yes, there is <1>."
        ],
        [
            "Is there <1> in the image?",
            "No, there is no <1>."
        ],
        [
            "There are numbers in the image. List all the numbers you see.",
            "I can see <1>."
        ],
        [
            "What numbers are in the image?",
            "There are <1>."
        ],
        [
            "There are alphabets in the image. List all the alphabets you see.",
            "I can see <1>."
        ],
        [
            "What alphabets are in the image?",
            "There are <1>."
        ]
    ],
    "ocr2": [
        [
            "Read the word in the image.",
            "<1>"
        ],
        [
            "What is the word in the image?",
            "The word in the image is <1>."
        ],
        [
            "Word in the image is <1>. Is it correct?",
            "Yes, the word in the image is <1>."
        ],
        [
            "Word in the image is <1>. Is it correct?",
            "No, the word in the image is not <1>."
        ],
        [
            "What can you read in the image?",
            "I can read a word <1>."
        ]
    ],
    "ocr3": [
        [
            "Read the text in the image.",
            "<1>"
        ],
        [
            "There is a text in the image. Please read it.",
            "<1>"
        ],
        [
            "What is written in the image?",
            "<1>"
        ],
        [
            "Do OCR on the image and read the text.",
            "<1>"
        ]
    ],
    "ocr7": [
        [
            "There is a flipped word in the image. What is the word?",
            "The flipped word is <1>."
        ],
        [
            "In the picture, you can see a word upside down. Reat it.",
            "The word is <1>."
        ],
        [
            "What is the word that is flipped in the image?",
            "The flipped word is <1>."
        ],
        [
            "It is difficult for me to read the flipped word. Can you help me?",
            "Sure, the word is <1>."
        ],
        [
            "The upside down word in the image is <1>. Is it correct?",
            "Yes, the word is <1>."
        ],
        [
            "The upside down word in the image is <2>. Is it correct?",
            "No, the word is <1>."
        ]
    ],
    "ocr9": [
        [
            "There are pairs of alphabets and numbers in the image. List all the pairs you see.",
            "I can find <1>."
        ],
        [
            "Pairs of alphabets and numbers in the image. Which number is paired with alphabet <1>?",
            "Number <2> is paired with alphabet <1>."
        ],
        [
            "Pairs of alphabets and numbers in the image. Which alphabet is paired with number <1>?",
            "Alphabet <2> is paired with number <1>."
        ],
        [
            "In the given pairs of alphabets and numbers, is alphabet <1> paired with number <2>?",
            "Yes, alphabet <1> is paired with number <2>."
        ],
        [
            "In the given pairs of alphabets and numbers, is alphabet <1> paired with number <2>?",
            "No, alphabet <1> is not paired with number <2>."
        ]
    ],
    "ocr14": [
        [
            "Read the word written in <1> color.",
            "The word written in <1> color is <2>."
        ],
        [
            "Extract the word with <1> color from the long text.",
            "The result is <2>."
        ],
        [
            "Make the word by reading only the <1> color letters.",
            "<2> is made."
        ],
        [
            "Read the word by reading only the bold letters.",
            "The word is <1>."
        ],
        [
            "What can you read if you read only the bold letters?",
            "I can read <1>."
        ],
        [
            "Make the word by reading only the bold letters.",
            "The word in bold letter is <1>."
        ]
    ],
    "ocr15": [
        [
            "In the image, you can see a word <1>. On which letter is the circle drawn?",
            "The circle is drawn on letter <2>."
        ],
        [
            "I circled on some letter in the word <1>. Which letter is circled?",
            "The circled letter is <2>."
        ],
        [
            "Find the circled letter in the word <1>.",
            "The letter <2> is circled."
        ],
        [
            "You can see a letter is circled. Is the circled letter <1>?",
            "Yes, the circled letter is <1>."
        ],
        [
            "You can see a letter is circled. Is the circled letter <1>?",
            "No, the circled letter is <2>."
        ]
    ],
    "ocr16": [
        [
            "In the image, you can see the words <1>. Which letters are circled?",
            "The letters circled are <2>."
        ],
        [
            "I circled some letters in the word <1>. Which letters are circled?",
            "The circled letters are <2>."
        ],
        [
            "Find the circled letters in the word <1>.",
            "The letters <2> are circled."
        ],
        [
            "You can see some letters are circled. Are the circled letters <1>?",
            "Yes, the circled letters are <1>."
        ],
        [
            "You can see some letters are circled. Are the circled letters <1>?",
            "No, the circled letters are <2>."
        ]
    ],

    "ocr21": [
        [
            "Among the given options, which doesn't exist in the image? Options: <1>",
            "<2> doesn't exist in the image."
        ],
        [
            "Choose the letter that is not in the image. Choose from <1>.",
            "The letter <2> is not in the image."
        ],
        [
            "Which letter is not in the image? Your answer should be one of <1>.",
            "<2> is the answer."
        ],
        [
            "Complete the sentence. In the image, (<3>) doesn't exist.",
            "In the image, <2> doesn't exist."
        ],
        [
            "(<3>) is not in the image. What is the correct choice?",
            "<2> is not in the image."
        ]
    ],
    "ocr22": [
        [
            "Read the text that is written in <1> color.",
            "The text in <1> color is <2>."
        ],
        [
            "What is written in <1> color?",
            "The text <2> is written in <1> color."
        ],
        [
            "Read the <1> colored text.",
            "The text in <1> color is <2>."
        ],
        [
            "The text in <1> color is <2>. Is it correct?",
            "Yes, the text in <1> color is <2>."
        ],
        [
            "The text in <1> color is <3>. Is it correct?",
            "No, the text in <1> color is <2>."
        ]
    ],
    "ocr23": [
        [
            "Is there <1> in the image?",
            "Yes, there is <1>."
        ],
        [
            "Is there <1> in the image?",
            "No, there is no <1>."
        ],
        [
            "There are letters in the image. List all the letters you see.",
            "I can see <1>."
        ],
        [
            "What letters are in the image?",
            "There are <1>."
        ]
    ]
}

conversation_short = {
    "ocr1": [
        [
            "Is there <1> in the image?",
            "Yes"
        ],
        [
            "Is there <1> in the image?",
            "No"
        ],
        [
            "There are numbers in the image. List all the numbers you see.",
            "<1>"
        ],
        [
            "What numbers are in the image?",
            "<1>"
        ],
        [
            "There are alphabets in the image. List all the alphabets you see.",
            "<1>"
        ],
        [
            "What alphabets are in the image?",
            "<1>"
        ]
    ],
    "ocr2": [
        [
            "Read the word in the image.",
            "<1>"
        ],
        [
            "What is the word in the image?",
            "<1>"
        ],
        [
            "Word in the image is <1>. Is it correct?",
            "Yes"
        ],
        [
            "Word in the image is <1>. Is it correct?",
            "No"
        ],
        [
            "What can you read in the image?",
            "<1>"
        ]
    ],
    "ocr3": [
        [
            "Read the text in the image.",
            "<1>"
        ],
        [
            "There is a text in the image. Please read it.",
            "<1>"
        ],
        [
            "What is written in the image?",
            "<1>"
        ],
        [
            "Do OCR on the image and read the text.",
            "<1>"
        ]
    ],
    "ocr7": [
        [
            "There is a flipped word in the image. What is the word?",
            "<1>"
        ],
        [
            "In the picture, you can see a word upside down. Reat it.",
            "<1>"
        ],
        [
            "What is the word that is flipped in the image?",
            "<1>"
        ],
        [
            "It is difficult for me to read the flipped word. Can you help me?",
            "<1>"
        ],
        [
            "The upside down word in the image is <1>. Is it correct?",
            "Yes"
        ],
        [
            "The upside down word in the image is <2>. Is it correct?",
            "No"
        ]
    ],
    "ocr9": [
        [
            "There are pairs of alphabets and numbers in the image. List all the pairs you see.",
            "<1>"
        ],
        [
            "Pairs of alphabets and numbers in the image. Which number is paired with alphabet <1>?",
            "<2>"
        ],
        [
            "Pairs of alphabets and numbers in the image. Which alphabet is paired with number <1>?",
            "<2>"
        ],
        [
            "In the given pairs of alphabets and numbers, is alphabet <1> paired with number <2>?",
            "Yes"
        ],
        [
            "In the given pairs of alphabets and numbers, is alphabet <1> paired with number <2>?",
            "No"
        ]
    ],
    "ocr14": [
        [
            "Read the word written in <1> color.",
            "<2>"
        ],
        [
            "Extract the word with <1> color from the long text.",
            "<2>"
        ],
        [
            "Make the word by reading only the <1> color letters.",
            "<2>"
        ],
        [
            "Read the word by reading only the bold letters.",
            "<1>"
        ],
        [
            "What can you read if you read only the bold letters?",
            "<1>"
        ],
        [
            "Make the word by reading only the bold letters.",
            "<1>"
        ]
    ],
    "ocr15": [
        [
            "In the image, you can see a word <1>. On which letter is the circle drawn?",
            "<2>"
        ],
        [
            "I circled on some letter in the word <1>. Which letter is circled?",
            "<2>"
        ],
        [
            "Find the circled letter in the word <1>.",
            "<2>"
        ],
        [
            "You can see a letter is circled. Is the circled letter <1>?",
            "Yes"
        ],
        [
            "You can see a letter is circled. Is the circled letter <1>?",
            "No"
        ]
    ],
    "ocr16": [
        [
            "In the image, you can see the word <1>. Which letters are circled?",
            "<2>"
        ],
        [
            "I circled some letters in the word <1>. Which letters are circled?",
            "<2>"
        ],
        [
            "Find the circled letters in the word <1>.",
            "<2>"
        ],
        [
            "You can see some letters are circled. Are the circled letters <1>?",
            "Yes"
        ],
        [
            "You can see some letters are circled. Are the circled letters <1>?",
            "No"
        ]
    ],
    "ocr21": [
        [
            "Among the given options, which doesn't exist in the image? Options: <1>",
            "<2>"
        ],
        [
            "Choose the letter that is not in the image. Choose from <1>.",
            "<2>"
        ],
        [
            "Which letter is not in the image? Your answer should be one of <1>.",
            "<2>"
        ],
        [
            "Complete the sentence. In the image, (<3>) doesn't exist.",
            "<2>"
        ],
        [
            "(<3>) is not in the image. What is the correct choice?",
            "<2>"
        ]
    ],
    "ocr22": [
        [
            "Read the text that is written in <1> color.",
            "<2>"
        ],
        [
            "What is written in <1> color?",
            "<2>"
        ],
        [
            "Read the <1> colored text.",
            "<2>"
        ],
        [
            "The text in <1> color is <2>. Is it correct?",
            "Yes"
        ],
        [
            "The text in <1> color is <3>. Is it correct?",
            "No"
        ]
    ],
    "ocr23": [
        [
            "Is there <1> in the image?",
            "Yes"
        ],
        [
            "Is there <1> in the image?",
            "No"
        ],
        [
            "There are letters in the image. List all the letters you see.",
            "<1>"
        ],
        [
            "What letters are in the image?",
            "<1>"
        ]
    ]
}

alphabets = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
capital_alphabets = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
lowercase_alphabets = set(list('abcdefghijklmnopqrstuvwxyz'))
numbers = set(list('0123456789'))
letters_list = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+-=[]{}|;:,.<>?'))

def generate_ocr1(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    is_number = entity[2]
    if is_number:
        index = random.choice([0, 1, 2, 3])
        if index == 0:
            letter = random.choice(entity[1]).letter
            q = conversation['ocr1'][index][0].replace('<1>', letter)
            r = conversation['ocr1'][index][1].replace('<1>', letter)
        elif index == 1:
            letters = [letter.letter for letter in entity[1]]
            letter = random.choice(list(numbers - set(letters)))
            q = conversation['ocr1'][index][0].replace('<1>', letter)
            r = conversation['ocr1'][index][1].replace('<1>', letter)
        elif index == 2 or index == 3:
            letters = [letter.letter for letter in entity[1]]
            q = conversation['ocr1'][index][0].replace('<1>', ', '.join(list(set(letters))))
            r = conversation['ocr1'][index][1].replace('<1>', ', '.join(list(set(letters))))
    else:
        index = random.choice([0, 1, 4, 5])
        if index == 0:
            letter = random.choice(entity[1]).letter
            q = conversation['ocr1'][index][0].replace('<1>', letter)
            r = conversation['ocr1'][index][1].replace('<1>', letter)
        elif index == 1:
            letters = [letter.letter for letter in entity[1]]
            letter = random.choice(list(alphabets - set(letters)))
            q = conversation['ocr1'][index][0].replace('<1>', letter)
            r = conversation['ocr1'][index][1].replace('<1>', letter)
        elif index == 4 or index == 5:
            letters = [letter.letter for letter in entity[1]]
            q = conversation['ocr1'][index][0].replace('<1>', ', '.join(list(set(letters))))
            r = conversation['ocr1'][index][1].replace('<1>', ', '.join(list(set(letters))))
    
    return q, r
    
def generate_ocr2(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.choice([0, 1, 2, 3, 4])
    if index == 0 or index == 1 or index == 2 or index == 4:
        q = conversation['ocr2'][index][0].replace('<1>', entity[1].word)
        r = conversation['ocr2'][index][1].replace('<1>', entity[1].word)
    elif index == 3:
        word = entity[1].word
        while word == entity[1].word:
            word = random_meaningful_word()
        q = conversation['ocr2'][index][0].replace('<1>', word)
        r = conversation['ocr2'][index][1].replace('<1>', word)
    
    return q, r

def generate_ocr3(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    index = random.choice([0, 1, 2, 3])
    if index == 0 or index == 1 or index == 2 or index == 3:
        q = conversation['ocr3'][index][0]
        r = conversation['ocr3'][index][1].replace('<1>', entity[1])
    
    return q, r

def generate_ocr7(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    word = entity[1]
    negative_word = random_meaningful_word()

    while negative_word == word:
        negative_word = random_meaningful_word()

    index = random.choice([0, 1, 2, 3, 4, 5])

    q = conversation['ocr7'][index][0].replace('<1>', word).replace('<2>', negative_word)
    r = conversation['ocr7'][index][1].replace('<1>', word).replace('<2>', negative_word)

    return q, r

def generate_ocr9(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    pairs = entity[1]
    index = random.choice(range(len(conversation['ocr9'])))

    if index == 0:
        q = conversation['ocr9'][index][0]
        r = conversation['ocr9'][index][1].replace('<1>', ', '.join(pairs))
    elif index == 1:
        pair = random.choice(pairs)

        if entity[2]:
            alphabet = pair[0]
            number = pair[1]
        else:
            alphabet = pair[1]
            number = pair[0]

        q = conversation['ocr9'][index][0].replace('<1>', alphabet)
        r = conversation['ocr9'][index][1].replace('<2>', number).replace('<1>', alphabet)
    elif index == 2:
        pair = random.choice(pairs)

        if entity[2]:
            alphabet = pair[0]
            number = pair[1]
        else:
            alphabet = pair[1]
            number = pair[0]

        q = conversation['ocr9'][index][0].replace('<1>', number)
        r = conversation['ocr9'][index][1].replace('<2>', alphabet).replace('<1>', number)
    elif index == 3:
        pair = random.choice(pairs)

        if entity[2]:
            alphabet = pair[0]
            number = pair[1]
        else:
            alphabet = pair[1]
            number = pair[0]

        q = conversation['ocr9'][index][0].replace('<1>', alphabet).replace('<2>', number)
        r = conversation['ocr9'][index][1].replace('<1>', alphabet).replace('<2>', number)
    elif index == 4:
        pair = random.choice(pairs)

        if entity[2]:
            alphabet = pair[0]
            number = pair[1]
        else:
            alphabet = pair[1]
            number = pair[0]

        rand = random.randint(0, 1)

        if rand:
            number = random.choice(list(numbers - set(number)))
        else:
            if alphabet in capital_alphabets:
                alphabet = random.choice(list(capital_alphabets - set(alphabet)))
            else:
                alphabet = random.choice(list(lowercase_alphabets - set(alphabet)))

        q = conversation['ocr9'][index][0].replace('<1>', alphabet).replace('<2>', number)
        r = conversation['ocr9'][index][1].replace('<1>', alphabet).replace('<2>', number)

    return q, r

def generate_ocr14(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    word = entity[1]
    indicies = entity[2]
    answer = ''.join([word[i] for i in indicies])

    variation = entity[3]
    answer_color = entity[4]

    if variation == 0:
        index = random.choice([0, 1, 2])
        q = conversation['ocr14'][index][0].replace('<1>', answer_color)
        a = conversation['ocr14'][index][1].replace('<2>', answer).replace('<1>', answer_color)
    elif variation == 1:
        index = random.choice([3, 4, 5])
        q = conversation['ocr14'][index][0]
        a = conversation['ocr14'][index][1].replace('<1>', answer)
    
    return q, a

def generate_ocr15(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    word = entity[1]

    circled_letter = word[entity[2]]

    index = random.choice([0, 1, 2, 3, 4])

    if index == 0 or index == 1 or index == 2:
        q = conversation['ocr15'][index][0].replace('<1>', word)
        a = conversation['ocr15'][index][1].replace('<2>', circled_letter)
    elif index == 3:
        q = conversation['ocr15'][index][0].replace('<1>', circled_letter)
        a = conversation['ocr15'][index][1].replace('<1>', circled_letter)
    elif index == 4:
        negative = random.choice(list(alphabets - set(circled_letter)))
        q = conversation['ocr15'][index][0].replace('<1>', negative)
        a = conversation['ocr15'][index][1].replace('<2>', circled_letter)

    return q, a

def generate_ocr16(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    word = entity[1]

    circled_letter_list = []
    for one_idx in entity[2]:
        circled_letter_list.append(word[one_idx])
    circled_letter = ", ".join(circled_letter_list)

    index = random.choice([0, 1, 2, 3, 4])

    if index == 0 or index == 1 or index == 2:
        q = conversation['ocr16'][index][0].replace('<1>', word)
        a = conversation['ocr16'][index][1].replace('<2>', circled_letter)
    elif index == 3:
        q = conversation['ocr16'][index][0].replace('<1>', circled_letter)
        a = conversation['ocr16'][index][1].replace('<1>', circled_letter)
    elif index == 4:
        negative = random.choice(list(alphabets - set(circled_letter)))
        q = conversation['ocr16'][index][0].replace('<1>', negative)
        a = conversation['ocr16'][index][1].replace('<2>', circled_letter)

    return q, a

def generate_ocr21(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    exist = entity[1]
    non_exist = entity[2]

    if random.randint(0, 3):
        pool = exist + [non_exist]
        random.shuffle(pool)

        comma_list = ', '.join(pool + ['none'])
        slash_list = ' / '.join(pool + ['none'])

        answer = non_exist
        index = random.choice([0, 1, 2, 3, 4])
    else:
        pool = exist
        random.shuffle(pool)

        comma_list = ', '.join(pool + ['none'])
        slash_list = ' / '.join(pool + ['none'])

        answer = 'none'
        index = random.choice([0, 2, 3, 4])

    q = conversation['ocr21'][index][0].replace('<1>', comma_list).replace('<3>', slash_list)
    a = conversation['ocr21'][index][1].replace('<2>', answer)

    return q, a

def generate_ocr22(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    color_word = entity[1]

    color = color_word[0][0]
    word = color_word[0][1]
    wrong_word = color_word[1][1]

    index = random.randint(0, len(conversation['ocr22']) - 1)
    
    q = conversation['ocr22'][index][0].replace('<1>', color).replace('<2>', word).replace('<3>', wrong_word)
    a = conversation['ocr22'][index][1].replace('<1>', color).replace('<2>', word).replace('<3>', wrong_word)

    return q, a

def generate_ocr23(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    letters = entity[1]


    index = random.choice([0, 1, 2, 3])
    if index == 0:
        letter = random.choice(entity[1]).letter
        q = conversation['ocr23'][index][0].replace('<1>', letter)
        r = conversation['ocr23'][index][1].replace('<1>', letter)
    elif index == 1:
        letters = [letter.letter for letter in entity[1]]
        letter = random.choice(list(letters_list - set(letters)))
        q = conversation['ocr23'][index][0].replace('<1>', letter)
        r = conversation['ocr23'][index][1].replace('<1>', letter)
    elif index == 2 or index == 3:
        letters = [letter.letter for letter in entity[1]]
        q = conversation['ocr23'][index][0].replace('<1>', ', '.join(list(set(letters))))
        r = conversation['ocr23'][index][1].replace('<1>', ', '.join(list(set(letters))))

    return q, r


def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        if entity[0] == 'ocr1':
            conversation_list.append(generate_ocr1(entity, long))
        elif entity[0] == 'ocr2':
            conversation_list.append(generate_ocr2(entity, long))
        elif entity[0] == 'ocr3':
            conversation_list.append(generate_ocr3(entity, long))
        elif entity[0] == 'ocr7':
            conversation_list.append(generate_ocr7(entity, long))
        elif entity[0] == 'ocr9':
            conversation_list.append(generate_ocr9(entity, long))
        elif entity[0] == 'ocr14':
            conversation_list.append(generate_ocr14(entity, long))
        elif entity[0] == 'ocr15':
            conversation_list.append(generate_ocr15(entity, long))
        elif entity[0] == 'ocr16':
            conversation_list.append(generate_ocr16(entity, long))
        elif entity[0] == 'ocr21':
            conversation_list.append(generate_ocr21(entity, long))
        elif entity[0] == 'ocr22':
            conversation_list.append(generate_ocr22(entity, long))
        elif entity[0] == 'ocr23':
            conversation_list.append(generate_ocr23(entity, long))
    return conversation_list