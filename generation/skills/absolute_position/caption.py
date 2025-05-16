from .rules import *
import re

captions = {
  "abs_position_right": [
    "The point <1> is on the right side of the figure.",
    "In the figure, the point <1> can be found on the right.",
    "Point <1> appears on the right portion of the figure.",
    "You can see point <1> on the figure's right side.",
    "Point <1> is positioned to the right within the figure."
  ],
  "abs_position_left": [
    "The point <1> is on the left side of the figure.",
    "In the figure, the point <1> is located on the left.",
    "Point <1> appears on the left portion of the figure.",
    "You can see point <1> on the figure's left side.",
    "Point <1> is positioned to the left within the figure."
  ],
  "abs_position_top": [
    "The point <1> is on the top side of the figure.",
    "In the figure, the point <1> is located near the top.",
    "Point <1> appears on the upper portion of the figure.",
    "You can see point <1> at the top side of the diagram.",
    "Point <1> is placed in the top area of the figure."
  ],
  "abs_position_bottom": [
    "The point <1> is on the bottom side of the figure.",
    "In the figure, the point <1> is located at the bottom.",
    "Point <1> can be found on the lower portion of the figure.",
    "You can see point <1> on the figure's bottom side.",
    "Point <1> is placed in the bottom area of the figure."
  ],
  "abs_position_topright": [
    "The point <1> is on the top right side of the figure.",
    "In the figure, the point <1> sits in the top right region.",
    "Point <1> appears in the upper right portion of the figure.",
    "You can see point <1> on the figure's top right side.",
    "Point <1> is positioned in the top right corner of the diagram."
  ],
  "abs_position_topleft": [
    "The point <1> is on the top left side of the figure.",
    "In the figure, the point <1> sits in the top left region.",
    "Point <1> appears in the upper left portion of the figure.",
    "You can see point <1> on the figure's top left side.",
    "Point <1> is positioned in the top left corner of the diagram."
  ],
  "abs_position_bottomright": [
    "The point <1> is on the bottom right side of the figure.",
    "In the figure, the point <1> sits in the bottom right region.",
    "Point <1> appears in the lower right portion of the figure.",
    "You can see point <1> on the figure's bottom right side.",
    "Point <1> is positioned in the bottom right corner of the diagram."
  ],
  "abs_position_bottomleft": [
    "The point <1> is on the bottom left side of the figure.",
    "In the figure, the point <1> sits in the bottom left region.",
    "Point <1> appears in the lower left portion of the figure.",
    "You can see point <1> on the figure's bottom left side.",
    "Point <1> is positioned in the bottom left corner of the diagram."
  ],
  "C_abs_position_right": [
    "Points <1> and <2> are both on the right side of the figure.",
    "In this figure, the point <1> and the <2> point appear on the right.",
    "You can find point <1> and the <2> point along the right side of the figure.",
    "The figure shows that <1> and <2> lie on the right side.",
    "Both <1> and <2> are positioned to the right in the diagram."
  ],
  "C_abs_position_left": [
    "Points <1> and <2> are both on the left side of the figure.",
    "In this figure, the point <1> and the <2> point appear on the left.",
    "You can find point <1> and the <2> point along the left side of the figure.",
    "The figure shows that <1> and <2> lie on the left side.",
    "Both <1> and <2> are positioned to the left in the diagram."
  ],
  "C_abs_position_top": [
    "Points <1> and <2> are both on the top side of the figure.",
    "In this figure, point <1> and point <2> appear at the top.",
    "You can find <1> and <2> along the upper side of the figure.",
    "The figure shows that <1> and <2> lie on the top side.",
    "Both <1> and <2> are positioned at the top in the diagram."
  ],
  "C_abs_position_bottom": [
    "Points <1> and <2> are both on the bottom side of the figure.",
    "In this figure, point <1> and point <2> appear at the bottom.",
    "You can find <1> and <2> along the lower side of the figure.",
    "The figure shows that <1> and <2> lie on the bottom side.",
    "Both <1> and <2> are positioned at the bottom in the diagram."
  ],
  "C_abs_position_topright": [
    "Points <1> and <2> are both on the top right side of the figure.",
    "In this figure, point <1> and point <2> appear in the top right region.",
    "You can find <1> and <2> along the upper right side of the figure.",
    "The figure shows that <1> and <2> lie in the top right portion.",
    "Both <1> and <2> are positioned at the top right of the diagram."
  ],
  "C_abs_position_topleft": [
    "Points <1> and <2> are both on the top left side of the figure.",
    "In this figure, point <1> and point <2> appear in the top left region.",
    "You can find <1> and <2> along the upper left side of the figure.",
    "The figure shows that <1> and <2> lie in the top left portion.",
    "Both <1> and <2> are positioned at the top left of the diagram."
  ],
  "C_abs_position_bottomright": [
    "Points <1> and <2> are both on the bottom right side of the figure.",
    "In this figure, point <1> and point <2> appear in the bottom right region.",
    "You can find <1> and <2> along the lower right side of the figure.",
    "The figure shows that <1> and <2> lie in the bottom right portion.",
    "Both <1> and <2> are positioned at the bottom right of the diagram."
  ],
  "C_abs_position_bottomleft": [
    "Points <1> and <2> are both on the bottom left side of the figure.",
    "In this figure, point <1> and point <2> appear in the bottom left region.",
    "You can find <1> and <2> along the lower left side of the figure.",
    "The figure shows that <1> and <2> lie in the bottom left portion.",
    "Both <1> and <2> are positioned at the bottom left of the diagram."
  ],
  "abs_position_line_right": [
    "The line <1><2> is located on the right side of the figure.",
    "You can see the line <1><2> on the figure's right side.",
    "In the figure, the line <1><2> appears to the right.",
    "Line <1><2> is positioned along the right portion of the diagram.",
    "The diagram shows line <1><2> on the right side."
  ],
  "abs_position_line_left": [
    "The line <1><2> is located on the left side of the figure.",
    "You can see the line <1><2> on the figure's left side.",
    "In the figure, the line <1><2> appears to the left.",
    "Line <1><2> is positioned along the left portion of the diagram.",
    "The diagram shows line <1><2> on the left side."
  ],
  "abs_position_line_top": [
    "The line <1><2> is located on the top side of the figure.",
    "You can see the line <1><2> on the figure's upper side.",
    "In the figure, the line <1><2> appears at the top.",
    "Line <1><2> is positioned along the top portion of the diagram.",
    "The diagram shows line <1><2> near the top side."
  ],
  "abs_position_line_bottom": [
    "The line <1><2> is located on the bottom side of the figure.",
    "You can see the line <1><2> on the figure's lower side.",
    "In the figure, the line <1><2> appears at the bottom.",
    "Line <1><2> is positioned along the bottom portion of the diagram.",
    "The diagram shows line <1><2> near the bottom side."
  ],
  "abs_position_line_topright": [
    "The line <1><2> is located on the top right side of the figure.",
    "You can see the line <1><2> in the figure's upper right region.",
    "In the figure, line <1><2> appears at the top right.",
    "Line <1><2> is positioned along the top right portion of the diagram.",
    "The diagram shows line <1><2> near the top right side."
  ],
  "abs_position_line_topleft": [
    "The line <1><2> is located on the top left side of the figure.",
    "You can see the line <1><2> in the figure's upper left region.",
    "In the figure, line <1><2> appears at the top left.",
    "Line <1><2> is positioned along the top left portion of the diagram.",
    "The diagram shows line <1><2> near the top left side."
  ],
  "abs_position_line_bottomright": [
    "The line <1><2> is located on the bottom right side of the figure.",
    "You can see line <1><2> in the figure's lower right region.",
    "In the figure, line <1><2> appears at the bottom right.",
    "Line <1><2> is positioned along the bottom right portion of the diagram.",
    "The diagram shows line <1><2> near the bottom right side."
  ],
  "abs_position_line_bottomleft": [
    "The line <1><2> is located on the bottom left side of the figure.",
    "You can see line <1><2> in the figure's lower left region.",
    "In the figure, line <1><2> appears at the bottom left.",
    "Line <1><2> is positioned along the bottom left portion of the diagram.",
    "The diagram shows line <1><2> near the bottom left side."
  ],
  "C_abs_position_line_right": [
    "Both line <1><2> and the <3> line are located on the right side of the figure.",
    "In this figure, line <1><2> and the <3> line appear on the right.",
    "You can see line <1><2> and the <3> line along the right portion of the diagram.",
    "The diagram shows line <1><2> and the <3> line on the right side.",
    "Line <1><2> and the <3> line are positioned to the right in this figure."
  ],
  "C_abs_position_line_left": [
    "Both line <1><2> and the <3> line are located on the left side of the figure.",
    "In this figure, line <1><2> and the <3> line appear on the left.",
    "You can see line <1><2> and the <3> line along the left portion of the diagram.",
    "The diagram shows line <1><2> and the <3> line on the left side.",
    "Line <1><2> and the <3> line are positioned to the left in this figure."
  ],
  "C_abs_position_line_top": [
    "Both line <1><2> and the <3> line are located on the top side of the figure.",
    "In this figure, line <1><2> and the <3> line appear at the top.",
    "You can see line <1><2> and the <3> line along the upper portion of the diagram.",
    "The diagram shows line <1><2> and the <3> line on the top side.",
    "Line <1><2> and the <3> line are positioned at the top in this figure."
  ],
  "C_abs_position_line_bottom": [
    "Both line <1><2> and the <3> line are located on the bottom side of the figure.",
    "In this figure, line <1><2> and the <3> line appear at the bottom.",
    "You can see line <1><2> and the <3> line along the lower portion of the diagram.",
    "The diagram shows line <1><2> and the <3> line on the bottom side.",
    "Line <1><2> and the <3> line are positioned at the bottom in this figure."
  ],
  "C_abs_position_line_topright": [
    "Both line <1><2> and the <3> line are located on the top right side of the figure.",
    "In this figure, line <1><2> and the <3> line appear in the top right region.",
    "You can see line <1><2> and the <3> line in the upper right portion of the diagram.",
    "The diagram shows line <1><2> and the <3> line on the top right side.",
    "Line <1><2> and the <3> line are positioned at the top right in this figure."
  ],
  "C_abs_position_line_topleft": [
    "Both line <1><2> and the <3> line are located on the top left side of the figure.",
    "In this figure, line <1><2> and the <3> line appear in the top left region.",
    "You can see line <1><2> and the <3> line in the upper left portion of the diagram.",
    "The diagram shows line <1><2> and the <3> line on the top left side.",
    "Line <1><2> and the <3> line are positioned at the top left in this figure."
  ],
  "C_abs_position_line_bottomright": [
    "Both line <1><2> and the <3> line are located on the bottom right side of the figure.",
    "In this figure, line <1><2> and the <3> line appear in the bottom right region.",
    "You can see line <1><2> and the <3> line in the lower right portion of the diagram.",
    "The diagram shows line <1><2> and the <3> line on the bottom right side.",
    "Line <1><2> and the <3> line are positioned at the bottom right in this figure."
  ],
  "C_abs_position_line_bottomleft": [
    "Both line <1><2> and the <3> line are located on the bottom left side of the figure.",
    "In this figure, line <1><2> and the <3> line appear in the bottom left region.",
    "You can see line <1><2> and the <3> line in the lower left portion of the diagram.",
    "The diagram shows line <1><2> and the <3> line on the bottom left side.",
    "Line <1><2> and the <3> line are positioned at the bottom left in this figure."
  ],
  "abs_position_circle_right": [
    "The circle <1> is located on the right side of the figure.",
    "You can see the circle <1> on the figure's right side.",
    "In the figure, the circle <1> appears on the right.",
    "Circle <1> is positioned along the right portion of the diagram.",
    "The diagram shows circle <1> on the right side."
  ],
  "abs_position_circle_left": [
    "The circle <1> is located on the left side of the figure.",
    "You can see the circle <1> on the figure's left side.",
    "In the figure, the circle <1> appears on the left.",
    "Circle <1> is positioned along the left portion of the diagram.",
    "The diagram shows circle <1> on the left side."
  ],
  "abs_position_circle_top": [
    "The circle <1> is located on the top side of the figure.",
    "You can see the circle <1> on the figure's upper side.",
    "In the figure, the circle <1> appears at the top.",
    "Circle <1> is positioned along the top portion of the diagram.",
    "The diagram shows circle <1> near the top side."
  ],
  "abs_position_circle_bottom": [
    "The circle <1> is located on the bottom side of the figure.",
    "You can see the circle <1> on the figure's lower side.",
    "In the figure, the circle <1> appears at the bottom.",
    "Circle <1> is positioned along the bottom portion of the diagram.",
    "The diagram shows circle <1> near the bottom side."
  ],
  "abs_position_circle_topright": [
    "The circle <1> is located on the top right side of the figure.",
    "You can see the circle <1> in the figure's upper right region.",
    "In the figure, circle <1> appears at the top right.",
    "Circle <1> is positioned along the top right portion of the diagram.",
    "The diagram shows circle <1> near the top right side."
  ],
  "abs_position_circle_topleft": [
    "The circle <1> is located on the top left side of the figure.",
    "You can see the circle <1> in the figure's upper left region.",
    "In the figure, circle <1> appears at the top left.",
    "Circle <1> is positioned along the top left portion of the diagram.",
    "The diagram shows circle <1> near the top left side."
  ],
  "abs_position_circle_bottomright": [
    "The circle <1> is located on the bottom right side of the figure.",
    "You can see the circle <1> in the figure's lower right region.",
    "In the figure, circle <1> appears at the bottom right.",
    "Circle <1> is positioned along the bottom right portion of the diagram.",
    "The diagram shows circle <1> near the bottom right side."
  ],
  "abs_position_circle_bottomleft": [
    "The circle <1> is located on the bottom left side of the figure.",
    "You can see the circle <1> in the figure's lower left region.",
    "In the figure, circle <1> appears at the bottom left.",
    "Circle <1> is positioned along the bottom left portion of the diagram.",
    "The diagram shows circle <1> near the bottom left side."
  ],
  "C_abs_position_circle_right": [
    "Which side of the figure is the circle <1> located, left or right?",
    "Yes, the circle <1> is on the right side of the figure."
  ],
  "abs_position_object": [
    "Object (<i>) <TYPE> <LABEL> is located in the <DIR> area of the image.",
    "In the <DIR> part of this image, you'll find (<i>) <TYPE> <LABEL>.",
    "Positioned in the <DIR> section of the image is object (<i>) <TYPE> <LABEL>.",
    "Within the <DIR> of the image, the object is (<i>) <TYPE> <LABEL>.",
    "You can spot (<i>) <TYPE> <LABEL> in the <DIR> region of the image."
  ],
  "abs_position_object_colored": [
    "Object (<i>) <TYPE> <LABEL>, colored <COLOR>, is located in the <DIR> area of the image.",
    "In the <DIR> part of this image, you'll find the (<i>) <COLOR> <TYPE> <LABEL>.",
    "Positioned in the <DIR> section of the image is (<i>) <COLOR> <TYPE> <LABEL>.",
    "Within the <DIR> of the image lies (<i>) <COLOR> <TYPE> <LABEL>.",
    "You can spot (<i>) <COLOR> <TYPE> <LABEL> in the <DIR> region of the image."
  ],
  "abs_position_object_quadrant": [
    "In the <DIR> quadrant of the image, you can find object (<i>) <TYPE> <LABEL>.",
    "Object (<i>) <TYPE> <LABEL> is located in the <DIR> quadrant of the figure.",
    "Within the <DIR> portion of the image, there is (<i>) <TYPE> <LABEL>.",
    "If you look at the <DIR> quadrant, you'll see (<i>) <TYPE> <LABEL>.",
    "The <DIR> area of the image contains (<i>) <TYPE> <LABEL>."
  ],
  "abs_position_object_colored_quadrant": [
    "In the <DIR> quadrant of the image, you can find (<i>) <COLOR> <TYPE> <LABEL>.",
    "Object (<i>) <COLOR> <TYPE> <LABEL> is located in the <DIR> quadrant of the figure.",
    "Within the <DIR> portion of the image lies (<i>) <COLOR> <TYPE> <LABEL>.",
    "If you look at the <DIR> quadrant, you'll see (<i>) <COLOR> <TYPE> <LABEL>.",
    "The <DIR> area of the image contains (<i>) <COLOR> <TYPE> <LABEL>."
  ]
}


def generate_absolute_position(entity):
    if entity[0].startswith("abs_position_object"):
        keyword = entity[0]
        index = random.randint(0, len(captions[keyword]) - 1)
        a = captions[keyword][index]

        # find the part in '[]' (in answer)
        parts_a = re.findall(r"\[.*?\]", a)
        # for each part in [], replace <i>, <TYPE>, <DIR>, <LABEL>, <COLOR> with the actual values
        for k, part in enumerate(parts_a):
            new_part = ""
            for i, value in enumerate(entity[1]):
                new_part_frag = (a + '.')[:-1]
                new_part_frag = new_part_frag.replace(f"<i>", str(i + 1))
                new_part_frag = new_part_frag.replace(f"<TYPE>", value[0])
                new_part_frag = new_part_frag.replace(f"<DIR>", value[1])
                new_part_frag = new_part_frag.replace(f"<LABEL>", value[2])
                new_part_frag = new_part_frag.replace(f"<COLOR>", value[3])
                new_part = f"{new_part}{new_part_frag[1:-1]}"
            a = a.replace(parts_a[k], new_part)
        
        a = a.replace("<N>", str(len(entity[1])))
        a = a.replace("<TYPE>", entity[2][0])
        a = a.replace("<DIR>", entity[2][1])
        a = a.replace("<LABEL>", entity[2][2])
        a = a.replace("<COLOR>", entity[2][3])
        a = a.replace("<i>", str(entity[2][4]+1))

        return a

    (
        xdir,
        ydir,
    ) = (
        entity[2],
        entity[3],
    )

    # find conversation with keyword "{entity[0]}_{ydir}{xdir}"
    keyword = f"{entity[0]}_{ydir if ydir else ''}{xdir if xdir else ''}"

    index = random.randint(0, len(captions[keyword]) - 1)
    a = captions[keyword][index]

    # replace <1>, <2>, ... with the actual values
    for i in range(len(entity[1])):
        a = a.replace(f"<{i+1}>", entity[1][i])

    return a


def generate_caption(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        if "abs_position" in entity[0]:
            conversation_list.append(generate_absolute_position(entity))
        break
    return " ".join(conversation_list)