from .rules import *

color_list = ["black", "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan"]

captions = {
    "sentence11": [
        "In the given figure, there is a table with <1> rows and <2> columns, and each cell is filled with one of the <3> colors.",
        "The provided image shows a grid with <1> rows and <2> columns, and each cell is painted in one of the <3> colors.",
        "Within this figure, a table of <1> rows by <2> columns is drawn, and every cell contains one of the <3> colors.",
        "The image depicts a table consisting of <1> rows and <2> columns, where each cell is colored with one of the <3> colors.",
        "In this given diagram, there's a grid made up of <1> rows and <2> columns, and each cell is painted with one of the <3> colors."
    ],
    "sentence12": [
        "The color in the cell that is <1> from the left and <2> from the top is <3>.",
        "The cell that is <1> from the left and <2> from the top has the color <3>.",
        "The color of the cell located <1> from the left and <2> from the top is <3>.",
        "In the cell located <1> from the left and <2> from the top, the color is <3>.",
        "At the cell <1> from the left and <2> from the top, the color is <3>."
    ],
    "sentence13": [
        "The color in the cell that is <1> from the left and <2> from the bottom is <3>.",
        "The cell located <1> from the left and <2> from the bottom has the color <3>.",
        "The color of the cell <1> from the left and <2> from the bottom is <3>.",
        "In the cell positioned <1> from the left and <2> from the bottom, the color is <3>.",
        "At the cell that is <1> from the left and <2> from the bottom, the color is <3>."
    ],
    "sentence14": [
        "The color in the cell that is <1> from the right and <2> from the top is <3>.",
        "The cell located <1> from the right and <2> from the top has the color <3>.",
        "The color of the cell <1> from the right and <2> from the top is <3>.",
        "In the cell positioned <1> from the right and <2> from the top, the color is <3>.",
        "At the cell that is <1> from the right and <2> from the top, the color is <3>."
    ],
    "sentence15": [
        "The color in the cell that is <1> from the right and <2> from the bottom is <3>.",
        "The cell located <1> from the right and <2> from the bottom has the color <3>.",
        "The color of the cell <1> from the right and <2> from the bottom is <3>.",
        "In the cell positioned <1> from the right and <2> from the bottom, the color is <3>.",
        "At the cell that is <1> from the right and <2> from the bottom, the color is <3>."
    ],
    "sentence16": [
        "In this figure, the color of the cell adjacent to a cell colored <1> is <2>.",
        "Within this picture, a cell next to one colored <1> is painted <2>.",
        "Any cell neighboring a <1>-colored cell in this diagram has the color <2>.",
        "In this image, the cell adjacent to a <1>-colored cell is colored <2>.",
        "The cells that are next to those with the color <1> in this figure are painted <2>."
    ],
    "sentence21": [
        "In the given figure, a total of <1> letters are written in a table with <2> rows and <3> columns.",
        "The provided image contains <1> letters arranged in a grid of <2> rows and <3> columns.",
        "Within the picture, there are <1> letters placed in a table that has <2> rows and <3> columns.",
        "The image shows <1> letters in a chart form with <2> rows and <3> columns.",
        "In this figure, <1> letters are depicted in a table structure consisting of <2> rows and <3> columns."
    ],
    "sentence22": [
        "The letter in the cell that is <1> from the left and <2> from the top is <3>.",
        "The cell located <1> from the left and <2> from the top contains the letter <3>.",
        "The letter of the cell <1> from the left and <2> from the top is <3>.",
        "In the cell positioned <1> from the left and <2> from the top, the letter is <3>.",
        "At the cell that is <1> from the left and <2> from the top, the letter is <3>."
    ],
    "sentence23": [
        "The letter in the cell that is <1> from the left and <2> from the bottom is <3>.",
        "The cell located <1> from the left and <2> from the bottom contains the letter <3>.",
        "The letter of the cell <1> from the left and <2> from the bottom is <3>.",
        "In the cell positioned <1> from the left and <2> from the bottom, the letter is <3>.",
        "At the cell that is <1> from the left and <2> from the bottom, the letter is <3>."
    ],
    "sentence24": [
        "The letter in the cell that is <1> from the right and <2> from the top is <3>.",
        "The cell located <1> from the right and <2> from the top contains the letter <3>.",
        "The letter of the cell <1> from the right and <2> from the top is <3>.",
        "In the cell positioned <1> from the right and <2> from the top, the letter is <3>.",
        "At the cell that is <1> from the right and <2> from the top, the letter is <3>."
    ],
    "sentence25": [
        "The letter in the cell that is <1> from the right and <2> from the bottom is <3>.",
        "The cell located <1> from the right and <2> from the bottom contains the letter <3>.",
        "The letter of the cell <1> from the right and <2> from the bottom is <3>.",
        "In the cell positioned <1> from the right and <2> from the bottom, the letter is <3>.",
        "At the cell that is <1> from the right and <2> from the bottom, the letter is <3>."
    ],
    "sentence26": [
        "In this figure, the letter in the cell adjacent to the one with <1> is <2>.",
        "Within this diagram, any cell next to the one that has <1> written in it contains the letter <2>.",
        "In this image, a cell neighboring the one marked with <1> has the letter <2>.",
        "Cells adjacent to the one containing <1> in this figure are written with <2>.",
        "In this picture, the letter of the cell next to the one with <1> is <2>."
    ]
}


def get_idx(row_count, col_count, i, criteria):
    """
    i는 인덱스(0부터 시작), criteria는 left/right/up/down
    row_count = 전체 행 개수
    col_count = 전체 열 개수
    
    - left : 왼쪽에서 i칸 떨어진 => (i+1)
    - right : 오른쪽에서 i칸 떨어진 => (col_count - i)
    - up : 위에서 i칸 떨어진 => (row_count - i)
    - down : 아래에서 i칸 떨어진 => (i+1)
    """
    if criteria == "left":
        return i + 1
    elif criteria == "right":
        return col_count - i
    elif criteria == "up":
        return row_count - i
    elif criteria == "down":
        return i + 1


def generate_adjacency1(grid, entity_list):
    """
    grid: Grid() 객체
    entity_list: ["row", "col", "answer_color", ... , "adjacent_colors"]
    """
    captions_list = []

    # 표 전반에 대한 설명 (row, col 순서 주의!)
    text1 = random.choice(captions["sentence11"])
    text1 = text1.replace("<1>", str(grid.row))  # rows
    text1 = text1.replace("<2>", str(grid.col))  # columns
    random.shuffle(color_list)
    text1 = text1.replace("<3>", ", ".join(color_list))
    captions_list.append(text1)

    # 표의 각 칸에 대한 설명: 
    # (lr : left/right) -> col 인덱스
    # (ud : up/down) -> row 인덱스
    lr = random.choice(["left", "right"])
    ud = random.choice(["up", "down"])

    if lr == "left":
        col_range_info = range(grid.col)  # 0 ~ col-1
    else:
        col_range_info = range(grid.col-1, -1, -1)

    if ud == "down":
        row_range_info = range(grid.row)
    else:
        row_range_info = range(grid.row-1, -1, -1)

    # 전체 셀 순회하면서 문장 생성
    if random.randint(1, 2) == 1:
        # row 우선 순회
        for r in row_range_info:
            for c in col_range_info:
                adjusted_row_idx = get_idx(grid.row, grid.col, r, ud)
                adjusted_col_idx = get_idx(grid.row, grid.col, c, lr)
                color_info = grid.grid_info[(r, c)].facecolor
                sentence_list = []
                if lr == "left" and ud == "up":
                    sentence_list = captions["sentence12"]
                elif lr == "left" and ud == "down":
                    sentence_list = captions["sentence13"]
                elif lr == "right" and ud == "up":
                    sentence_list = captions["sentence14"]
                elif lr == "right" and ud == "down":
                    sentence_list = captions["sentence15"]
                
                chosen_sent = random.choice(sentence_list)
                chosen_sent = chosen_sent.replace("<1>", str(adjusted_col_idx))
                chosen_sent = chosen_sent.replace("<2>", str(adjusted_row_idx))
                chosen_sent = chosen_sent.replace("<3>", color_info)
                captions_list.append(chosen_sent)
    else:
        # col 우선 순회
        for c in col_range_info:
            for r in row_range_info:
                adjusted_row_idx = get_idx(grid.row, grid.col, r, ud)
                adjusted_col_idx = get_idx(grid.row, grid.col, c, lr)
                color_info = grid.grid_info[(r, c)].facecolor
                sentence_list = []
                if lr == "left" and ud == "up":
                    sentence_list = captions["sentence12"]
                elif lr == "left" and ud == "down":
                    sentence_list = captions["sentence13"]
                elif lr == "right" and ud == "up":
                    sentence_list = captions["sentence14"]
                elif lr == "right" and ud == "down":
                    sentence_list = captions["sentence15"]
                
                chosen_sent = random.choice(sentence_list)
                chosen_sent = chosen_sent.replace("<1>", str(adjusted_col_idx))
                chosen_sent = chosen_sent.replace("<2>", str(adjusted_row_idx))
                chosen_sent = chosen_sent.replace("<3>", color_info)
                captions_list.append(chosen_sent)

    # 이웃한 칸(특정 color) 정보
    # entity_list[2] = answer_color, entity_list[6] = ", ".join(g.adjacent_colors)
    sentence = random.choice(captions["sentence16"])
    sentence = sentence.replace("<1>", entity_list[2])
    sentence = sentence.replace("<2>", entity_list[6])
    captions_list.append(sentence)

    return captions_list


def generate_adjacency2(grid, entity_list):
    """
    grid: TextGrid() 객체
    entity_list: ["row", "col", "answer_text", ... , "adjacent_text"]
    """
    captions_list = []

    # 표 전반에 대한 설명 (row, col)
    text1 = random.choice(captions["sentence21"])
    text1 = text1.replace("<2>", str(grid.row))  # 표기: rows
    text1 = text1.replace("<3>", str(grid.col))  # 표기: columns
    total_letters = grid.row * grid.col
    text1 = text1.replace("<1>", str(total_letters))
    captions_list.append(text1)

    # 표의 각 칸에 대한 설명
    lr = random.choice(["left", "right"])
    ud = random.choice(["up", "down"])

    if lr == "left":
        col_range_info = range(grid.col)
    else:
        col_range_info = range(grid.col-1, -1, -1)

    if ud == "down":
        row_range_info = range(grid.row)
    else:
        row_range_info = range(grid.row-1, -1, -1)

    if random.randint(1, 2) == 1:
        # row 우선
        for r in row_range_info:
            for c in col_range_info:
                adjusted_row_idx = get_idx(grid.row, grid.col, r, ud)
                adjusted_col_idx = get_idx(grid.row, grid.col, c, lr)
                text_info = grid.grid_info[(r, c)].label

                if lr == "left" and ud == "up":
                    sentence_list = captions["sentence22"]
                elif lr == "left" and ud == "down":
                    sentence_list = captions["sentence23"]
                elif lr == "right" and ud == "up":
                    sentence_list = captions["sentence24"]
                else:
                    sentence_list = captions["sentence25"]

                chosen_sent = random.choice(sentence_list)
                chosen_sent = chosen_sent.replace("<1>", str(adjusted_col_idx))
                chosen_sent = chosen_sent.replace("<2>", str(adjusted_row_idx))
                chosen_sent = chosen_sent.replace("<3>", text_info)
                captions_list.append(chosen_sent)
    else:
        # col 우선
        for c in col_range_info:
            for r in row_range_info:
                adjusted_row_idx = get_idx(grid.row, grid.col, r, ud)
                adjusted_col_idx = get_idx(grid.row, grid.col, c, lr)
                text_info = grid.grid_info[(r, c)].label

                if lr == "left" and ud == "up":
                    sentence_list = captions["sentence22"]
                elif lr == "left" and ud == "down":
                    sentence_list = captions["sentence23"]
                elif lr == "right" and ud == "up":
                    sentence_list = captions["sentence24"]
                else:
                    sentence_list = captions["sentence25"]

                chosen_sent = random.choice(sentence_list)
                chosen_sent = chosen_sent.replace("<1>", str(adjusted_col_idx))
                chosen_sent = chosen_sent.replace("<2>", str(adjusted_row_idx))
                chosen_sent = chosen_sent.replace("<3>", text_info)
                captions_list.append(chosen_sent)

    # 이웃한 칸(특정 글자) 정보
    sentence = random.choice(captions["sentence26"])
    sentence = sentence.replace("<1>", entity_list[2])
    sentence = sentence.replace("<2>", entity_list[6])
    captions_list.append(sentence)

    return captions_list


def generate_caption(diagram):
    """
    diagram.components[0]가 Grid 또는 TextGrid
    diagram.entities[0][1]이 [row, col, ...] 형태
    """
    grid = diagram.components[0]
    entity_list = diagram.entities[0][1]
    captions_list = []
    if grid.grid_type == "color":
        # adjacency1
        captions_list = generate_adjacency1(grid, entity_list)
    else:
        # adjacency2
        captions_list = generate_adjacency2(grid, entity_list)

    # 여러 문장을 하나의 문자열로 합쳐 반환
    return " ".join(captions_list)
