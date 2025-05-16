from .rules import *

import random

captions = {
    "ocr1": [
        "The image contains the text: <1>.",
        "There is no occurrence of <1> in the image.",
        "The image displays the numbers: <1>.",
        "The visible numbers in the image are <1>.",
        "The text in the image includes the alphabets: <1>.",
        "The alphabets appearing in the image are <1>."
    ],
    "ocr2": [
        "The image contains the word: <1>.",
        "A prominently displayed word in the image is <1>.",
        "The word <1> is clearly written in the image.",
        "The word in the image is not <1>.",
        "A legible word in the image reads <1>."
    ],
    "ocr3": [
        "The image features the text: <1>.",
        "A portion of the image contains the written text: <1>.",
        "The text inscribed in the image is: <1>.",
        "The extracted text from the image is: <1>."
    ],
    "ocr7": [
        "The image includes a flipped word, which reads <1>.",
        "An upside-down word in the image is <1>.",
        "Despite being inverted, the word in the image is <1>.",
        "The word <1> appears flipped in the image.",
        "The upside-down word is <1>.",
        "The actual flipped word in the image is <1>."
    ],
    "ocr9": [
        "The image displays pairs of alphabets and numbers, including <1>.",
        "In the given dataset, the alphabet <1> is paired with the number <2>.",
        "The number <1> corresponds to the alphabet <2> in the image.",
        "The pair <1> - <2> exists in the image.",
        "Alphabet <1> is not associated with number <2>."
    ],
    "ocr14": [
        "In the image, the word written in <1> color is <2>.",
        "Extracting only the <1>-colored letters, the result forms the word <2>.",
        "Reading only the letters in <1> color spells out <2>.",
        "The bold letters in the image form the word <1>.",
        "When considering only bold text, the readable content is <1>.",
        "The word highlighted in bold is <1>."
    ],
    "ocr15": [
        "The letter <2> is circled in the word <1>.",
        "In the word <1>, a circle highlights the letter <2>.",
        "The image emphasizes the letter <2> by circling it in the word <1>.",
        "The letter circled in the image is <1>.",
        "The circled letter is <2>."
    ],
    "ocr16": [
        "The letters <2> are circled in the word <1>.",
        "In the word <1>, a circle highlights the letters <2>.",
        "The image emphasizes the letters <2> by circling them in the word <1>.",
        "The letters circled in the image are <2>.",
        "The circled letters are <2>."
    ],
    "ocr21": [
        "The full list of the alphabets in the image is <1>.",
        "The image contains all the letters from the set <1>.",
        "The alphabets present in the image are <1>.",
        "The complete list of letters in the image is <1>."
    ],
    "ocr22": [
        "The text written in <1> color is <2>.",
        "Within the image, the content highlighted in <1> color is <2>.",
        "The readable text in <1> color is <2>.",
        "The text appearing in <1> color is indeed <2>.",
        "The actual text in <1> color is <2>."
    ],
    "ocr23": [
        "The image contains the text: <1>.",
        "No instance of <1> is present in the image.",
        "The visible letters in the image include <1>.",
        "The image comprises the letters: <1>."
    ]
}

alphabets = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
capital_alphabets = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
lowercase_alphabets = set(list('abcdefghijklmnopqrstuvwxyz'))
numbers = set(list('0123456789'))
letters_list = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+-=[]{}|;:,.<>?'))

def generate_ocr1(entity):
    
    is_number = entity[2]
    if is_number:
        index = random.choice([0, 1, 2, 3])
        if index == 0:
            letter = random.choice(entity[1]).letter
            caption = captions['ocr1'][index].replace('<1>', letter)
        elif index == 1:
            letters = [letter.letter for letter in entity[1]]
            letter = random.choice(list(numbers - set(letters)))
            caption = captions['ocr1'][index].replace('<1>', letter)
        elif index == 2 or index == 3:
            letters = [letter.letter for letter in entity[1]]
            caption = captions['ocr1'][index].replace('<1>', ', '.join(list(set(letters))))
    else:
        index = random.choice([0, 1, 4, 5])
        if index == 0:
            letter = random.choice(entity[1]).letter
            caption = captions['ocr1'][index].replace('<1>', letter)
        elif index == 1:
            letters = [letter.letter for letter in entity[1]]
            letter = random.choice(list(alphabets - set(letters)))
            caption = captions['ocr1'][index].replace('<1>', letter)
        elif index == 4 or index == 5:
            letters = [letter.letter for letter in entity[1]]
            caption = captions['ocr1'][index].replace('<1>', ', '.join(list(set(letters))))
    
    return caption
    
def generate_ocr2(entity):
    
    index = random.choice([0, 1, 2, 3, 4])
    if index == 0 or index == 1 or index == 2 or index == 4:
        caption = captions['ocr2'][index].replace('<1>', entity[1].word)
    elif index == 3:
        word = entity[1].word
        while word == entity[1].word:
            word = random_meaningful_word()
        caption = captions['ocr2'][index].replace('<1>', word)
    
    return caption

def generate_ocr3(entity):
    index = random.choice([0, 1, 2, 3])
    if index == 0 or index == 1 or index == 2 or index == 3:
        caption = captions['ocr3'][index].replace('<1>', entity[1])
    
    return caption

def generate_ocr7(entity):
    word = entity[1]
    negative_word = random_meaningful_word()

    while negative_word == word:
        negative_word = random_meaningful_word()

    index = random.choice([0, 1, 2, 3, 4, 5])

    caption = captions['ocr7'][index].replace('<1>', word).replace('<2>', negative_word)

    return caption

def generate_ocr9(entity):
    pairs = entity[1]
    index = random.choice(range(len(captions['ocr9'])))

    if index == 0:
        caption = captions['ocr9'][index].replace('<1>', ', '.join(pairs))
    elif index == 1:
        pair = random.choice(pairs)

        if entity[2]:
            alphabet = pair[0]
            number = pair[1]
        else:
            alphabet = pair[1]
            number = pair[0]

        caption = captions['ocr9'][index].replace('<1>', alphabet).replace('<2>', number)
    elif index == 2:
        pair = random.choice(pairs)

        if entity[2]:
            alphabet = pair[0]
            number = pair[1]
        else:
            alphabet = pair[1]
            number = pair[0]

        caption = captions['ocr9'][index].replace('<1>', number).replace('<2>', alphabet)
    elif index == 3:
        pair = random.choice(pairs)

        if entity[2]:
            alphabet = pair[0]
            number = pair[1]
        else:
            alphabet = pair[1]
            number = pair[0]

        caption = captions['ocr9'][index].replace('<1>', alphabet).replace('<2>', number)
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

        caption = captions['ocr9'][index].replace('<1>', alphabet).replace('<2>', number)

    return caption

def generate_ocr14(entity):
    
    word = entity[1]
    indicies = entity[2]
    answer = ''.join([word[i] for i in indicies])

    variation = entity[3]
    answer_color = entity[4]

    if variation == 0:
        index = random.choice([0, 1, 2])
        caption = captions['ocr14'][index].replace('<1>', answer_color).replace('<2>', answer)
    elif variation == 1:
        index = random.choice([3, 4, 5])
        caption = captions['ocr14'][index].replace('<1>', answer)
    
    return caption

def generate_ocr15(entity):
    word = entity[1]

    circled_letter = word[entity[2]]

    index = random.choice([0, 1, 2, 3, 4])

    if index == 0 or index == 1 or index == 2:
        caption = captions['ocr15'][index].replace('<1>', word).replace('<2>', circled_letter)
    elif index == 3:
        caption = captions['ocr15'][index].replace('<1>', circled_letter)
    elif index == 4:
        negative = random.choice(list(alphabets - set(circled_letter)))
        caption = captions['ocr15'][index].replace('<1>', negative).replace('<2>', circled_letter)

    return caption

def generate_ocr16(entity):
    word = entity[1]

    circled_letter = word[entity[2]]

    index = random.choice([0, 1, 2, 3, 4])

    if index == 0 or index == 1 or index == 2:
        caption = captions['ocr16'][index].replace('<1>', word).replace('<2>', circled_letter)
    elif index == 3:
        caption = captions['ocr16'][index].replace('<1>', circled_letter)
    elif index == 4:
        negative = random.choice(list(alphabets - set(circled_letter)))
        caption = captions['ocr16'][index].replace('<1>', negative).replace('<2>', circled_letter)

    return caption

def generate_ocr21(entity):
    exist = entity[1]
    words = ', '.join(exist)

    index = random.choice([0, 1, 2, 3])
    caption = captions['ocr21'][index].replace('<1>', words)

    return caption

def generate_ocr22(entity):
    color_word = entity[1]

    color = color_word[0][0]
    word = color_word[0][1]
    wrong_word = color_word[1][1]

    index = random.randint(0, len(captions['ocr22']) - 1)
    caption = captions['ocr22'][index].replace('<1>', color).replace('<2>', word).replace('<3>', wrong_word)

    return caption

def generate_ocr23(entity):
    letters = entity[1]

    index = random.choice([0, 1, 2, 3])
    if index == 0:
        letter = random.choice(entity[1]).letter
        caption = captions['ocr23'][index].replace('<1>', letter)
    elif index == 1:
        letters = [letter.letter for letter in entity[1]]
        letter = random.choice(list(letters_list - set(letters)))
        caption = captions['ocr23'][index].replace('<1>', letter)
    elif index == 2 or index == 3:
        letters = [letter.letter for letter in entity[1]]
        caption = captions['ocr23'][index].replace('<1>', ', '.join(list(set(letters))))

    return caption


def generate_caption(diagram):
    captions_list = []
    for entity in diagram.entities:
        if entity[0] == 'ocr1':
            captions_list.append(generate_ocr1(entity))
        elif entity[0] == 'ocr2':
            captions_list.append(generate_ocr2(entity))
        elif entity[0] == 'ocr3':
            captions_list.append(generate_ocr3(entity))
        elif entity[0] == 'ocr7':
            captions_list.append(generate_ocr7(entity))
        elif entity[0] == 'ocr9':
            captions_list.append(generate_ocr9(entity))
        elif entity[0] == 'ocr14':
            captions_list.append(generate_ocr14(entity))
        elif entity[0] == 'ocr15':
            captions_list.append(generate_ocr15(entity))
        elif entity[0] == 'ocr16':
            captions_list.append(generate_ocr16(entity))
        elif entity[0] == 'ocr21':
            captions_list.append(generate_ocr21(entity))
        elif entity[0] == 'ocr22':
            captions_list.append(generate_ocr22(entity))
        elif entity[0] == 'ocr23':
            captions_list.append(generate_ocr23(entity))
    return random.choice(captions_list)