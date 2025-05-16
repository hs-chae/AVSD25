import random
import math
import nltk
import nltk.corpus as corpus
from faker import Faker
import re
nltk.download('words', quiet=True)

fake = Faker()

class highlight:
    def __init__(self, color):
        self.color = color

class underline:
    def __init__(self, color):
        self.color = color

class Letter:
    def __init__(self, coordinate, letter, size, color, bold, italic, font, rotate, highlight=None, underline=None):
        self.coordinate = coordinate
        self.letter = letter
        self.size = size
        self.color = color
        self.bold = bold
        self.italic = italic
        self.font = font
        self.rotate = rotate              # 90도보다 작으면 기울어짐, 크면 뒤집힘
        self.highlight = highlight
        self.underline = underline
    
class Word:
    def __init__(self, coordinate, word, size, color, bold, italic, font, rotate, highlight=None, underline=None):
        self.coordinate = coordinate
        self.word = word
        self.size = size
        self.color = color
        self.bold = bold
        self.italic = italic
        self.font = font
        self.rotate = rotate              # 90도보다 작으면 기울어짐, 크면 뒤집힘
        self.highlight = highlight
        self.underline = underline
    
class Text:
    def __init__(self, text, font, rotate, align='left'):
        self.text = text
        self.highlights = []
        self.underlines = []
        self.font = font
        self.rotate = rotate
        self.align = align

class Table:
    def __init__(self, row, col, words):
        self.row = row
        self.col = col
        self.words = words

class Circle:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color


class Diagram:
    def __init__(self, letter=None, word=None, text=None, table=None, circle=None, entities=None, background_color='white'):
        self.letter = letter if letter is not None else []
        self.word = word if word is not None else []
        self.text = text if text is not None else []
        self.table = table if table is not None else []
        self.circle = circle if circle is not None else []
        self.background_color = background_color
        self.entities = entities if entities is not None else []


def random_alphabet():
    return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


def random_number():
    return random.choice('0123456789')


def random_letter():
    return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+-=[]{}|;:,.<>?/')

def random_all():
    return random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+-=[]{}|;:,.<>?/')

def random_color():
    if random.randint(1, 2) == 1:
        return random.choice(['red', 'blue', 'green', 'yellow', 'black', 'black', 'black', 'black'])
    else:
        trial = 0
        while trial < 10000:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            if (r+g+b)>100:
                break
        return("#{:02x}{:02x}{:02x}".format(r, g, b))


def random_tilt():
    if random.randint(1, 2) == 1:
        return 0
    else:
        return random.randint(-90, 90)


def random_flip():
    if random.randint(1, 2) == 1:
        return 180
    else:
        return random.randint(90, 270)

def random_meaningless_word():
    word = ''.join([random_alphabet() for _ in range(random.randint(5, 10))])
    return word

def random_word_with_letters():
    word = ''.join([random_letter() for _ in range(random.randint(5, 10))])
    return word

def random_word_all():
    word = ''.join([random_all() for _ in range(random.randint(5, 10))])
    return word

def random_meaningful_word():
    word_list = corpus.words.words()  # 영어 단어 리스트
    return random.choice(word_list)

def random_pos():
    return random.random(), random.random()

def random_font():
    return random.choice(['Arial', 'Times New Roman', 'Courier New', 'Comic Sans MS', 'Impact'])

already_bold_font = ['Impact']

def add_letter(diagram: Diagram):
    position = random_pos()
    letter = random_letter()
    size = random.randint(8, 30)
    color = random_color()
    font = random_font()

    l = Letter(position, letter, size, color, False, False, font, 0, None, None)
    diagram.letter.append(l)

    return l


def add_alphabet(diagram: Diagram):
    position = random_pos()
    letter = random_alphabet()
    size = random.randint(8, 30)
    color = random_color()
    font = random_font()

    l = Letter(position, letter, size, color, False, False, font, 0, None, None)
    diagram.letter.append(l)
    
    return l


def add_number(diagram: Diagram):
    position = random_pos()
    letter = random_number()
    size = random.randint(8, 30)
    color = random_color()
    font = random_font()

    l = Letter(position, letter, size, color, False, False, font, 0, None, None)
    diagram.letter.append(l)

    return l


def add_random_word(diagram: Diagram, tilting=False):
    length = random.randint(3, 10)

    x, y = random_pos()
    
    letter = ''.join([random_alphabet() for _ in range(length)])
    size = random.randint(8, 30)
    color = random_color()
    font = random_font()
    rotate = random_tilt() if tilting else 0

    word = Word((x, y), letter, size, color, False, False, font, rotate, None, None)
    diagram.word.append(word)
    return word

def add_random_all(diagram: Diagram, tilting=False):
    length = random.randint(3, 10)

    x, y = random_pos()
    
    letter = ''.join([random_all() for _ in range(length)])
    size = random.randint(8, 30)
    color = random_color()
    font = random_font()
    rotate = random_tilt() if tilting else 0

    word = Word((x, y), letter, size, color, False, False, font, rotate, None, None)
    diagram.word.append(word)
    return word


def add_meaningful_word(diagram: Diagram, tilting=False):
    word = random_meaningful_word()

    x, y = random_pos()

    size = random.randint(8, 30)
    color = random_color()
    font = random_font()
    rotate = random_tilt() if tilting else 0

    word = Word((x, y), word, size, color, False, False, font, rotate, None, None)
    diagram.word.append(word)
    return word


def add_alphabet_number_pair(diagram: Diagram):
    alphabet = random_alphabet()
    number = random_number()
    size = random.randint(8, 30)
    color = random_color()
    font = random_font()
    
    alphabet_pos = random_pos()
    number_pos = (alphabet_pos[0] + 10, alphabet_pos[1])

    l1 = Letter(alphabet_pos, alphabet, size, color, False, False, font, 0, None, None)
    l2 = Letter(number_pos, number, size, color, False, False, font, 0, None, None)

    diagram.letter.append(l1)
    diagram.letter.append(l2)

    return l1, l2


def add_circle_on_letter(diagram: Diagram, letter: Letter):
    x = letter.coordinate[0]
    y = letter.coordinate[1]
    color = random_color()
    radius = random.randint(10, 30)
    c = Circle((x, y), radius, color)
    diagram.circle.append(c)
    return c


def highlight_word(word: Word):
    h = highlight(random_color())
    word.highlight = h
    return h


def underline_word(word: Word):
    u = underline(random_color())
    word.underline = u
    return u

def ocr1(diagram):
    rand1 = random.randint(0, 1)            # 0: number, 1, 2: alphabet => 1 : alphabet
    rand2 = random.randint(0, 1)            # 0: different color, 1: same color
    rand3 = random.randint(0, 1)            # 0: different size, 1: same size
    rand4 = random.randint(0, 1)            # 0: different font, 1: same font
    num_of_letters = random.randint(3, 7)

    letters = []

    for _ in range(num_of_letters):
        if rand1 == 0:
            letters.append(add_number(diagram))
        else:
            letters.append(add_alphabet(diagram))

    if rand2:
        color = random_color()
        for letter in letters:
            letter.color = color

    if rand3:
        size = random.randint(8, 30)
        for letter in letters:
            letter.size = size

    if rand4:
        font = random_font()
        for letter in letters:
            letter.font = font

    diagram.entities.append(('ocr1', str(letters), rand1 == 0))

def ocr2(diagram):
    rand1 = random.randint(0, 2)            # 0: meaningless word, 1: meaningless word with number, 2: meaningful word
    rand2 = random.randint(0, 2)            # 0: not tilted, 1, 2: tilted
    
    tilt = 1 if rand2 != 0 else 0

    if rand1 == 0:
        word = add_random_word(diagram, tilt)
    elif rand1 == 1:
        word = add_random_all(diagram, tilt)
    else:
        word = add_meaningful_word(diagram, tilt)

    diagram.entities.append(('ocr2', str(word), rand1))

def ocr3(diagram):
    n_sentences = random.randint(3, 5)
    paragraph = fake.paragraph(nb_sentences=n_sentences)

    font = random_font()
    rotate = random.choice([0, random_tilt()])
    align = random.choice(['left', 'center', 'right'])

    text = Text(paragraph, font, rotate, align)

    diagram.text.append(text)

    diagram.entities.append(('ocr3', paragraph))

# def ocr4(diagram):
#     n_sentences = random.randint(3, 5)
#     paragraph = fake.paragraph(nb_sentences=n_sentences)

#     font = random_font()
#     rotate = random.choice([0, random_tilt()])
#     align = random.choice(['left', 'center', 'right'])

#     text = Text(paragraph, font, rotate, align)

#     start, end = random.choice([(m.start(), m.end()) for m in re.finditer(r'\b\w+\b', paragraph)])
#     color = random_color()

#     while color == 'black':
#         color = random_color()

#     text.highlights.append((start, end, color))

#     diagram.text.append(text)

def ocr7(diagram):
    w = add_meaningful_word(diagram, False)
    w.rotate = random.choice([180, random_flip()])
    diagram.entities.append(('ocr7', w.word))

def ocr9(diagram):
    num = random.randint(3, 7)
    capital = random.randint(0, 1)

    alphabets = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', num) if capital else random.sample('abcdefghijklmnopqrstuvwxyz', num)
    numbers = random.sample('0123456789', num)

    rand = random.randint(0, 1)
    pairs = [alphabet + number for alphabet, number in zip(alphabets, numbers)] if rand else [number + alphabet for number, alphabet in zip(numbers, alphabets)]

    same_size = random.randint(0, 1)
    same_color = random.randint(0, 1)
    same_font = random.randint(0, 1)

    global_size = random.randint(8, 30)
    gloabl_color = random.choice(['black', random_color()])
    global_font = random_font()

    for pair in pairs:
        position = random_pos()
        size = global_size if same_size else random.randint(8, 30)
        color = gloabl_color if same_color else random_color()
        font = global_font if same_font else random_font()

        w = Word(position, pair, size, color, False, False, font, 0, None, None)
        diagram.word.append(w)

    diagram.entities.append(('ocr9', pairs, rand))

def ocr14(diagram):
    word = random_meaningful_word()
    new_word = ""
    indicies = []

    for letter in word:
        n = random.randint(0, 2)
        for _ in range(n):
            new_word += random_alphabet()
        indicies.append(len(new_word))
        new_word += letter
    
    n = random.randint(0, 2)
    for _ in range(n):
        new_word += random_alphabet()

    position = random_pos()
    position = (position[0] - 0.1, position[1])

    variation = random.randint(0, 1)    # 0: color, 1: bold

    size = random.randint(8, 30)
    color = random.choice([random_color(), 'black'])
    font = random_font()
    rotate = random.choice([0, random_tilt()])

    answer_color = color
    answer_bold = False

    if variation == 0:
        while answer_color == color:
            answer_color = random_color()
    elif variation == 1:
        answer_bold = True
        new_word = new_word.lower()
        while font in already_bold_font:
            font = random_font()

    for i, letter in enumerate(list(new_word)):
        local_position = (
            position[0] + i * size * 0.004 * math.cos(math.radians(rotate)), 
            position[1] + i * size * 0.004 * math.sin(math.radians(rotate))
        )
        if i in indicies:
            l = Letter(local_position, letter, size, answer_color, answer_bold, False, font, rotate, None, None)
        else:
            l = Letter(local_position, letter, size, color, False, False, font, rotate, None, None)
        diagram.letter.append(l)

    diagram.entities.append(('ocr14', new_word, indicies, variation, answer_color))

def ocr15(diagram):
    word = random.choice([random_meaningful_word(), random_meaningless_word(), random_word_with_letters(), random_word_all()])
    index = random.randint(0, len(word)-1)

    position = random_pos()
    position = (position[0] - 0.1, position[1])

    size = random.randint(8, 30)
    color = random.choice([random_color(), 'black'])
    font = random_font()
    rotate = random.choice([0, random_tilt()])

    circle_color = random_color()

    for i, letter in enumerate(list(word)):
        local_position = (
            position[0] + i * size * 0.004 * math.cos(math.radians(rotate)), 
            position[1] + i * size * 0.004 * math.sin(math.radians(rotate))
        )

        if i == index:
            c = Circle(local_position, size * 0.004, circle_color)
            diagram.circle.append(c)

        l = Letter(local_position, letter, size, color, False, False, font, rotate, None, None)
        diagram.letter.append(l)
        
    diagram.entities.append(('ocr15', str(word), index))

def ocr16(diagram):
    word = random.choice([random_meaningful_word(), random_meaningless_word(), random_word_with_letters(), random_word_all()])
    if len(word) < 2:
        index = [random.randint(0, len(word)-1)]
    else:
        if random.randint(1, 2) == 1:
            index = random.sample(range(len(word)),2)
        else:
            index = random.sample(range(len(word)), random.randint(2, len(word)-1))

    position = random_pos()
    position = (position[0] - 0.1, position[1])

    size = random.randint(8, 30)
    color = random.choice([random_color(), 'black'])
    font = random_font()
    rotate = random.choice([0, random_tilt()])

    circle_color = random_color()

    for i, letter in enumerate(list(word)):
        local_position = (
            position[0] + i * size * 0.004 * math.cos(math.radians(rotate)), 
            position[1] + i * size * 0.004 * math.sin(math.radians(rotate))
        )

        if i in index:
            c = Circle(local_position, size * 0.004, circle_color)
            diagram.circle.append(c)

        l = Letter(local_position, letter, size, color, False, False, font, rotate, None, None)
        diagram.letter.append(l)
        
    diagram.entities.append(('ocr16', word, index))

def ocr21(diagram):
    n = random.randint(3, 5)
    alphabets = [add_alphabet(diagram) for _ in range(n)]

    if random.randint(0, 1):
        for alphabet in alphabets:
            alphabet.letter = alphabet.letter.lower()
        non_exist = set('abcdefghijklmnopqrstuvwxyz') - set([alphabet.letter for alphabet in alphabets])
    else:
        for alphabet in alphabets:
            alphabet.letter = alphabet.letter.upper()
        non_exist = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - set([alphabet.letter for alphabet in alphabets])

    exist = list(set([alphabet.letter for alphabet in alphabets]))
    non_exist = random.choice(list(non_exist))

    diagram.entities.append(('ocr21', exist, non_exist))

def ocr22(diagram):
    n = random.randint(3, 5)

    colors = random.sample(['red', 'blue', 'green', 'yellow', 'black'], n)
    words = []

    for i in range(n):
        m = random.randint(3, 5)
        word = [random.choice([random_alphabet, random_number])() for _ in range(m)]
        word = ''.join(word)
        position = random_pos()
        size = random.randint(8, 30)
        color = colors[i]
        font = random_font()

        w = Word(position, word, size, color, False, False, font, 0, None, None)
        words.append(w)
    
    diagram.word.extend(words)

    color_word = [(word.color, word.word) for word in words]

    diagram.entities.append(('ocr22', color_word))

def ocr23(diagram):
    rand2 = random.randint(0, 1)            # 0: different color, 1: same color
    rand3 = random.randint(0, 1)            # 0: different size, 1: same size
    rand4 = random.randint(0, 1)            # 0: different font, 1: same font
    num_of_letters = random.randint(3, 7)

    letters = []

    for _ in range(num_of_letters):
        letters.append(add_letter(diagram))

    if rand2:
        color = random_color()
        for letter in letters:
            letter.color = color

    if rand3:
        size = random.randint(8, 30)
        for letter in letters:
            letter.size = size

    if rand4:
        font = random_font()
        for letter in letters:
            letter.font = font

    diagram.entities.append(('ocr23', letters))

rules = [ocr1, ocr2, ocr3, ocr7, ocr9, ocr14, ocr15, ocr16, ocr21, ocr22, ocr23]
