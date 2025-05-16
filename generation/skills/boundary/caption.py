from .rules import *

captions = {
    "sentence1": [
        "In the figure, there is a line colored <1> and a rectangle colored <2>. In the given image, the line with color <1> exactly forms the boundary of the rectangle with color <2>.",
        "The illustration shows a line in color <1> along with a rectangle in color <2>. In this picture, the <1>-colored line precisely serves as the boundary of the <2>-colored rectangle.",
        "Within the diagram, a line of color <1> and a rectangle of color <2> are present. Here, the line colored <1> perfectly acts as the boundary of the rectangle colored <2>.",
        "The figure contains a <1>-colored line and a <2>-colored rectangle. In this particular image, the line with color <1> is exactly the boundary of the rectangle with color <2>.",
        "This illustration features a line in color <1> and a rectangle in color <2>. Specifically, the <1>-colored line precisely matches the boundary of the <2>-colored rectangle."
    ],
    "sentence2": [
        "In the figure, there is a line colored <1> and a rectangle colored <2>. In the given image, the line with color <1> does not become the boundary of the rectangle with color <2>.",
        "The illustration shows a line in color <1> and a rectangle in color <2>. In this picture, the <1>-colored line does not serve as the boundary of the <2>-colored rectangle.",
        "Within the diagram, a line of color <1> and a rectangle of color <2> are depicted. Here, the line colored <1> is not the boundary of the rectangle colored <2>.",
        "The figure contains a <1>-colored line and a <2>-colored rectangle. In this particular image, the <1>-colored line fails to coincide with the boundary of the <2>-colored rectangle.",
        "This illustration features a line in color <1> and a rectangle in color <2>. However, in this image, the <1>-colored line does not form the boundary of the <2>-colored rectangle."
    ],
    "sentence3": [
        "In the given figure, there is a shape <1> whose interior is colored <2>, while its outline is colored <3>. In other words, a boundary in a different color from the interior is explicitly drawn.",
        "Within this diagram, we see a shape <1> that has an inside colored <2> and an outline colored <3>. Thus, there is a clearly depicted boundary that contrasts with the interior.",
        "In this illustration, a shape <1> is present with an interior color of <2> and an outline color of <3>. Hence, a boundary differing in color from its interior is explicitly shown.",
        "The figure shows a shape <1>, where the inside is <2> and the perimeter is <3>. Therefore, a boundary in a contrasting color to its interior is explicitly depicted.",
        "Here, a shape <1> appears with an interior of <2> and an outline of <3>. This indicates that there is a distinct boundary in a different color from the shape’s interior."
    ],
    "sentence4": [
        "In the given figure, there is a shape <1> with an interior colored <2>, and no perimeter with a different color from its interior is observed. In other words, a boundary in a contrasting color is not explicitly drawn.",
        "Within this diagram, a shape <1> can be seen with an inside colored <2>, but there's no outline in a distinct color. Hence, there is no explicitly drawn boundary differing from the interior color.",
        "This illustration presents a shape <1> whose interior is <2>, yet a perimeter in a different color does not appear. Therefore, no boundary in a contrasting color is clearly shown.",
        "The figure features a shape <1> that has an interior of <2>, but we do not see an outline in a different color. Consequently, there is no clearly indicated boundary that differs from the interior.",
        "Here, a shape <1> is depicted with a color <2> filling its interior, but a perimeter in another color is not visible. Thus, a differently colored boundary is not explicitly drawn."
    ],
    "sentence5": [
        "In the given figure, a table with <1> rows and <2> columns is drawn.",
        "The illustration shows a grid consisting of <1> rows and <2> columns.",
        "The figure depicts a table that has <1> rows and <2> columns.",
        "Within the diagram, a table of <1> rows by <2> columns is represented.",
        "The provided image contains a table with <1> rows and <2> columns."
    ],
    "sentence6_inner": [
        "In the given figure, there are multiple layers of <1>. The color of the shape's perimeter, listed from the inside outward, is <3>. That is, the outermost boundary's color is <4>.",
        "Within this diagram, several stacked <1> appear. When noting the perimeter colors from the innermost layer outward, they are <3>. Hence, the outermost boundary color is <4>.",
        "This illustration shows multiple overlapping <1>. The shape's outline colors, starting from the inside and moving outward, are <3>. Therefore, the outermost boundary is <4>.",
        "A series of layered <1> is present in this figure. If we list the boundary colors from inside to outside, we get <3>. Thus, the outermost boundary color is <4>.",
        "The figure contains multiple levels of <1>. The colors of the outline, when recorded from the inside toward the outside, are <3>. Consequently, the color of the outermost boundary is <4>."
    ],
    "sentence6_outer": [
        "In the given figure, there are multiple layers of <1>. The color of the shape's perimeter, listed from the outside inward, is <3>. Thus, the outermost boundary's color is <4>.",
        "Within this diagram, several stacked <1> appear. If we note the perimeter colors from the outermost layer inward, they are <3>. Therefore, the color of the outer boundary is <4>.",
        "This illustration shows multiple overlapping <1>. The outline colors, when recorded from the outside moving inward, come to <3>. Hence, the outermost boundary color is <4>.",
        "A set of layered <1> is present in this figure. Listed from the outside to the inside, the perimeter colors are <3>. Consequently, the outermost boundary is <4>.",
        "The figure contains multiple layers of <1>. The shape’s edges, enumerated from outside toward the inside, are <3>. Accordingly, the color of the outermost boundary is <4>."
    ]
}

def boundary1_caption(component, entity_info):
    captions_list = []

    facecolor = entity_info[1]
    edgecolor = entity_info[2]

    one_text = random.choice(captions["sentence1"])
    one_text = one_text.replace("<1>", edgecolor)
    one_text = one_text.replace("<2>", facecolor)
    captions_list.append(one_text)

    return captions_list

def boundary2_caption(component, entity_info):
    captions_list = []

    facecolor = entity_info[1]
    edgecolor = entity_info[2]

    one_text = random.choice(captions["sentence2"])
    one_text = one_text.replace("<1>", edgecolor)
    one_text = one_text.replace("<2>", facecolor)
    captions_list.append(one_text)

    return captions_list

def boundary3_caption(component, entity_info):
    captions_list = []

    type_of_shape = component[0].shape_type
    facecolor = entity_info[1]
    edgecolor = entity_info[2]

    one_text = random.choice(captions["sentence3"])
    one_text = one_text.replace("<1>", type_of_shape)
    one_text = one_text.replace("<2>", facecolor)
    one_text = one_text.replace("<3>", edgecolor)
    captions_list.append(one_text)

    return captions_list

def boundary4_caption(component, entity_info):
    captions_list = []

    type_of_shape = component[0].shape_type
    facecolor = entity_info[1]

    one_text = random.choice(captions["sentence4"])
    one_text = one_text.replace("<1>", type_of_shape)
    one_text = one_text.replace("<2>", facecolor)
    captions_list.append(one_text)

    return captions_list

def boundary5_caption(component, entity_info):
    captions_list = []

    table = component[0]
    one_text = random.choice(captions["sentence5"])
    one_text = one_text.replace("<1>", str(table.height))
    one_text = one_text.replace("<2>", str(table.width))
    captions_list.append(one_text)

    num_sentences = random.randint(1, 10)
    record_list = []
    count_added = 0
    trial = 0
    while True:
        one_cell = random.choice(table.cell_dict)
        area1 = one_cell.idx
        neighbor_list = [one_element for one_element in one_cell.neighbor_cells if one_cell.neighbor_cells[one_element] is not None]
        place_key = random.choice(neighbor_list)
        neighbor = one_cell.neighbor_cells[place_key]
        answer = one_cell.lines[place_key].label
        area2 = neighbor.idx
        if ((area1, area2) not in record_list) and ((area2, area1) not in record_list):
            one_text = random.choice(captions["sentence6"])
            one_text = one_text.replace("<1>", str(area1))
            one_text = one_text.replace("<2>", str(area2))
            one_text = one_text.replace("<3>", str(answer))
            captions_list.append(one_text)
            record_list.append((area1, area2))
            count_added += 1
        if count_added > num_sentences:
            break
        trial += 1
        if trial > 10000:
            break

    return captions_list

def boundary6_caption(component, entity_info):
    captions_list = []

    # [new_shape.shape_type, "/".join(option_list), ", ".join(option_list), answer]
    shape_type = entity_info[0]
    option_list = entity_info[1].split("/")
    answer = entity_info[3]

    if random.randint(1, 2) == 1:
        one_text = random.choice(captions["sentence6_outer"])
        one_text = one_text.replace("<1>", str(shape_type))
        one_text = one_text.replace("<3>", ", ".join(option_list[::-1]))
        one_text = one_text.replace("<4>", str(answer))
    else:
        one_text = random.choice(captions["sentence6_inner"])
        one_text = one_text.replace("<1>", str(shape_type))
        one_text = one_text.replace("<3>", ", ".join(option_list))
        one_text = one_text.replace("<4>", str(answer))
    
    captions_list.append(one_text)

    return captions_list

def generate_caption(diagram):
    captions_list = []

    component = diagram.components
    question_type = diagram.entities[0][0]
    entity_info = diagram.entities[0][1]

    ftn_str = {'boundary1':boundary1_caption, 'boundary2':boundary2_caption, 'boundary3':boundary3_caption, 'boundary4':boundary4_caption, 'boundary5':boundary5_caption, 'boundary6':boundary6_caption}
    captions_list = ftn_str[question_type](component, entity_info)

    return " ".join(captions_list)