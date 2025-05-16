from .rules import *
import re

conversation_long = {
    "abs_position_right": [
        [
            "Which side of the figure is the point <1> located, left or right?",
            "The point <1> is located on the right side of the figure.",
        ],
        [
            "Is the point <1> on the right side of the figure?",
            "Yes, the point <1> is on the right side of the figure.",
        ],
        [
            "Is the point <1> on the left side of the figure?",
            "No, the point <1> is on the right side of the figure.",
        ],
    ],
    "abs_position_left": [
        [
            "Which side of the figure is the point <1> located, left or right?",
            "The point <1> is located on the left side of the figure.",
        ],
        [
            "Is the point <1> on the left side of the figure?",
            "Yes, the point <1> is on the left side of the figure.",
        ],
        [
            "Is the point <1> on the right side of the figure?",
            "No, the point <1> is on the left side of the figure.",
        ],
    ],
    "abs_position_top": [
        [
            "Which side of the figure is the point <1> located, top or bottom?",
            "The point <1> is located on the top side of the figure.",
        ],
        [
            "Is the point <1> on the top side of the figure?",
            "Yes, the point <1> is on the top side of the figure.",
        ],
        [
            "Is the point <1> on the bottom side of the figure?",
            "No, the point <1> is on the top side of the figure.",
        ],
    ],
    "abs_position_bottom": [
        [
            "Which side of the figure is the point <1> located, top or bottom?",
            "The point <1> is located on the bottom side of the figure.",
        ],
        [
            "Is the point <1> on the bottom side of the figure?",
            "Yes, the point <1> is on the bottom side of the figure.",
        ],
        [
            "Is the point <1> on the top side of the figure?",
            "No, the point <1> is on the bottom side of the figure.",
        ],
    ],
    "abs_position_topright": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "The point <1> is located on the top right side of the figure.",
        ],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "Yes, the point <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No, the point <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No, the point <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No, the point <1> is on the top right side of the figure.",
        #],
    ],
    "abs_position_topleft": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "The point <1> is located on the top left side of the figure.",
        ],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "Yes, the point <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No, the point <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No, the point <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No, the point <1> is on the top left side of the figure.",
        #],
    ],
    "abs_position_bottomright": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "The point <1> is located on the bottom right side of the figure.",
        ],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "Yes, the point <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No, the point <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No, the point <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No, the point <1> is on the bottom right side of the figure.",
        #],
    ],
    "abs_position_bottomleft": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "The point <1> is located on the bottom left side of the figure.",
        ],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "Yes, the point <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No, the point <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No, the point <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No, the point <1> is on the bottom left side of the figure.",
        #],
    ],
    "C_abs_position_right": [
        [
            "Which side of the figure is the point <1> located, left or right?",
            "The point <1> is located on the right side of the figure.",
        ],
        [
            "Is the point <1> on the right side of the figure?",
            "Yes, the point <1> is on the right side of the figure.",
        ],
        [
            "Is the point <1> on the left side of the figure?",
            "No, the point <1> is on the right side of the figure.",
        ],
        [
            "Which side of the figure is the <2> point located, left or right?",
            "The <2> point is located on the right side of the figure.",
        ],
        [
            "Is the <2> point on the right side of the figure?",
            "Yes, the <2> point is on the right side of the figure.",
        ],
        [
            "Is the <2> point on the left side of the figure?",
            "No, the <2> point is on the right side of the figure.",
        ],
    ],
    "C_abs_position_left": [
        [
            "Which side of the figure is the point <1> located, left or right?",
            "The point <1> is located on the left side of the figure.",
        ],
        [
            "Is the point <1> on the left side of the figure?",
            "Yes, the point <1> is on the left side of the figure.",
        ],
        [
            "Is the point <1> on the right side of the figure?",
            "No, the point <1> is on the left side of the figure.",
        ],
        [
            "Which side of the figure is the <2> point located, left or right?",
            "The <2> point is located on the left side of the figure.",
        ],
        [
            "Is the <2> point on the left side of the figure?",
            "Yes, the <2> point is on the left side of the figure.",
        ],
        [
            "Is the <2> point on the right side of the figure?",
            "No, the <2> point is on the left side of the figure.",
        ],
    ],
    "C_abs_position_top": [
        [
            "Which side of the figure is the point <1> located, top or bottom?",
            "The point <1> is located on the top side of the figure.",
        ],
        [
            "Is the point <1> on the top side of the figure?",
            "Yes, the point <1> is on the top side of the figure.",
        ],
        [
            "Is the point <1> on the bottom side of the figure?",
            "No, the point <1> is on the top side of the figure.",
        ],
        [
            "Which side of the figure is the <2> point located, top or bottom?",
            "The <2> point is located on the top side of the figure.",
        ],
        [
            "Is the <2> point on the top side of the figure?",
            "Yes, the <2> point is on the top side of the figure.",
        ],
        [
            "Is the <2> point on the bottom side of the figure?",
            "No, the <2> point is on the top side of the figure.",
        ],
    ],
    "C_abs_position_bottom": [
        [
            "Which side of the figure is the point <1> located, top or bottom?",
            "The point <1> is located on the bottom side of the figure.",
        ],
        [
            "Is the point <1> on the bottom side of the figure?",
            "Yes, the point <1> is on the bottom side of the figure.",
        ],
        [
            "Is the point <1> on the top side of the figure?",
            "No, the point <1> is on the bottom side of the figure.",
        ],
        [
            "Which side of the figure is the <2> point located, top or bottom?",
            "The <2> point is located on the bottom side of the figure.",
        ],
        [
            "Is the <2> point on the bottom side of the figure?",
            "Yes, the <2> point is on the bottom side of the figure.",
        ],
        [
            "Is the <2> point on the top side of the figure?",
            "No, the <2> point is on the bottom side of the figure.",
        ],
    ],
    "C_abs_position_topright": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "The point <1> is located on the top right side of the figure.",
        ],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "Yes, the point <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No, the point <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No, the point <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No, the point <1> is on the top right side of the figure.",
        #],
        [
            "Which side of the figure is the <2> point located, top right, top left, bottom right, or bottom left?",
            "The <2> point is located on the top right side of the figure.",
        ],
        #[
        #    "Is the <2> point on the top right side of the figure?",
        #    "Yes, the <2> point is on the top right side of the figure.",
        #],
        #[
        #    "Is the <2> point on the top left side of the figure?",
        #    "No, the <2> point is on the top right side of the figure.",
        #],
        #[
        #    "Is the <2> point on the bottom right side of the figure?",
        #    "No, the <2> point is on the top right side of the figure.",
        #],
        #[
        #    "Is the <2> point on the bottom left side of the figure?",
        #    "No, the <2> point is on the top right side of the figure.",
        #],
    ],
    "C_abs_position_topleft": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "The point <1> is located on the top left side of the figure.",
        ],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "Yes, the point <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No, the point <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No, the point <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No, the point <1> is on the top left side of the figure.",
        #],
        [
            "Which side of the figure is the <2> point located, top right, top left, bottom right, or bottom left?",
            "The <2> point is located on the top left side of the figure.",
        ],
        #[
        #    "Is the <2> point on the top left side of the figure?",
        #    "Yes, the <2> point is on the top left side of the figure.",
        #],
        #[
        #    "Is the <2> point on the top right side of the figure?",
        #    "No, the <2> point is on the top left side of the figure.",
        #],
        #[
        #    "Is the <2> point on the bottom right side of the figure?",
        #    "No, the <2> point is on the top left side of the figure.",
        #],
        #[
        #    "Is the <2> point on the bottom left side of the figure?",
        #    "No, the <2> point is on the top left side of the figure.",
        #],
    ],
    "C_abs_position_bottomright": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "The point <1> is located on the bottom right side of the figure.",
        ],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "Yes, the point <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No, the point <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No, the point <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No, the point <1> is on the bottom right side of the figure.",
        #],
        [
            "Which side of the figure is the <2> point located, top right, top left, bottom right, or bottom left?",
            "The <2> point is located on the bottom right side of the figure.",
        ],
        #[
        #    "Is the <2> point on the bottom right side of the figure?",
        #    "Yes, the <2> point is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the <2> point on the top right side of the figure?",
        #    "No, the <2> point is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the <2> point on the top left side of the figure?",
        #    "No, the <2> point is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the <2> point on the bottom left side of the figure?",
        #    "No, the <2> point is on the bottom right side of the figure.",
        #],
    ],
    "C_abs_position_bottomleft": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "The point <1> is located on the bottom left side of the figure.",
        ],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "Yes, the point <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No, the point <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No, the point <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "No, the point <1> is on the bottom left side of the figure.",
        #],
        [
            "Which side of the figure is the <2> point located, top right, top left, bottom right, or bottom left?",
            "The <2> point is located on the bottom left side of the figure.",
        ],
        #[
        #    "Is the <2> point on the bottom left side of the figure?",
        #    "Yes, the <2> point is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the <2> point on the top right side of the figure?",
        #    "No, the <2> point is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the <2> point on the top left side of the figure?",
        #    "No, the <2> point is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the <2> point on the bottom right side of the figure?",
        #    "No, the <2> point is on the bottom left side of the figure.",
        #],
    ],
    "abs_position_line_right": [
        [
            "Which side of the figure is the line <1><2> located, left or right?",
            "The line <1><2> is located on the right side of the figure.",
        ],
        [
            "Is the line <1><2> on the right side of the figure?",
            "Yes, the line <1><2> is on the right side of the figure.",
        ],
        [
            "Is the line <1><2> on the left side of the figure?",
            "No, the line <1><2> is on the right side of the figure.",
        ],
    ],
    "abs_position_line_left": [
        [
            "Which side of the figure is the line <1><2> located, left or right?",
            "The line <1><2> is located on the left side of the figure.",
        ],
        [
            "Is the line <1><2> on the left side of the figure?",
            "Yes, the line <1><2> is on the left side of the figure.",
        ],
        [
            "Is the line <1><2> on the right side of the figure?",
            "No, the line <1><2> is on the left side of the figure.",
        ],
    ],
    "abs_position_line_top": [
        [
            "Which side of the figure is the line <1><2> located, top or bottom?",
            "The line <1><2> is located on the top side of the figure.",
        ],
        [
            "Is the line <1><2> on the top side of the figure?",
            "Yes, the line <1><2> is on the top side of the figure.",
        ],
        [
            "Is the line <1><2> on the bottom side of the figure?",
            "No, the line <1><2> is on the top side of the figure.",
        ],
    ],
    "abs_position_line_bottom": [
        [
            "Which side of the figure is the line <1><2> located, top or bottom?",
            "The line <1><2> is located on the bottom side of the figure.",
        ],
        [
            "Is the line <1><2> on the bottom side of the figure?",
            "Yes, the line <1><2> is on the bottom side of the figure.",
        ],
        [
            "Is the line <1><2> on the top side of the figure?",
            "No, the line <1><2> is on the bottom side of the figure.",
        ],
    ],
    "abs_position_line_topright": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "The line <1><2> is located on the top right side of the figure.",
        ],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "Yes, the line <1><2> is on the top right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No, the line <1><2> is on the top right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No, the line <1><2> is on the top right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No, the line <1><2> is on the top right side of the figure.",
        #],
    ],
    "abs_position_line_topleft": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "The line <1><2> is located on the top left side of the figure.",
        ],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "Yes, the line <1><2> is on the top left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No, the line <1><2> is on the top left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No, the line <1><2> is on the top left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No, the line <1><2> is on the top left side of the figure.",
        #],
    ],
    "abs_position_line_bottomright": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "The line <1><2> is located on the bottom right side of the figure.",
        ],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "Yes, the line <1><2> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No, the line <1><2> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No, the line <1><2> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No, the line <1><2> is on the bottom right side of the figure.",
        #],
    ],
    "abs_position_line_bottomleft": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "The line <1><2> is located on the bottom left side of the figure.",
        ],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "Yes, the line <1><2> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No, the line <1><2> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No, the line <1><2> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No, the line <1><2> is on the bottom left side of the figure.",
        #],
    ],
    "C_abs_position_line_right": [
        [
            "Which side of the figure is the line <1><2> located, left or right?",
            "The line <1><2> is located on the right side of the figure.",
        ],
        [
            "Is the line <1><2> on the right side of the figure?",
            "Yes, the line <1><2> is on the right side of the figure.",
        ],
        [
            "Is the line <1><2> on the left side of the figure?",
            "No, the line <1><2> is on the right side of the figure.",
        ],
        [
            "Which side of the figure is the <3> line located, left or right?",
            "The <3> line is located on the right side of the figure.",
        ],
        [
            "Is the <3> line on the right side of the figure?",
            "Yes, the <3> line is on the right side of the figure.",
        ],
        [
            "Is the <3> line on the left side of the figure?",
            "No, the <3> line is on the right side of the figure.",
        ],
    ],
    "C_abs_position_line_left": [
        [
            "Which side of the figure is the line <1><2> located, left or right?",
            "The line <1><2> is located on the left side of the figure.",
        ],
        [
            "Is the line <1><2> on the left side of the figure?",
            "Yes, the line <1><2> is on the left side of the figure.",
        ],
        [
            "Is the line <1><2> on the right side of the figure?",
            "No, the line <1><2> is on the left side of the figure.",
        ],
        [
            "Which side of the figure is the <3> line located, left or right?",
            "The <3> line is located on the left side of the figure.",
        ],
        [
            "Is the <3> line on the left side of the figure?",
            "Yes, the <3> line is on the left side of the figure.",
        ],
        [
            "Is the <3> line on the right side of the figure?",
            "No, the <3> line is on the left side of the figure.",
        ],
    ],
    "C_abs_position_line_top": [
        [
            "Which side of the figure is the line <1><2> located, top or bottom?",
            "The line <1><2> is located on the top side of the figure.",
        ],
        [
            "Is the line <1><2> on the top side of the figure?",
            "Yes, the line <1><2> is on the top side of the figure.",
        ],
        [
            "Is the line <1><2> on the bottom side of the figure?",
            "No, the line <1><2> is on the top side of the figure.",
        ],
        [
            "Which side of the figure is the <3> line located, top or bottom?",
            "The <3> line is located on the top side of the figure.",
        ],
        [
            "Is the <3> line on the top side of the figure?",
            "Yes, the <3> line is on the top side of the figure.",
        ],
        [
            "Is the <3> line on the bottom side of the figure?",
            "No, the <3> line is on the top side of the figure.",
        ],
    ],
    "C_abs_position_line_bottom": [
        [
            "Which side of the figure is the line <1><2> located, top or bottom?",
            "The line <1><2> is located on the bottom side of the figure.",
        ],
        [
            "Is the line <1><2> on the bottom side of the figure?",
            "Yes, the line <1><2> is on the bottom side of the figure.",
        ],
        [
            "Is the line <1><2> on the top side of the figure?",
            "No, the line <1><2> is on the bottom side of the figure.",
        ],
        [
            "Which side of the figure is the <3> line located, top or bottom?",
            "The <3> line is located on the bottom side of the figure.",
        ],
        [
            "Is the <3> line on the bottom side of the figure?",
            "Yes, the <3> line is on the bottom side of the figure.",
        ],
        [
            "Is the <3> line on the top side of the figure?",
            "No, the <3> line is on the bottom side of the figure.",
        ],
    ],
    "C_abs_position_line_topright": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "The line <1><2> is located on the top right side of the figure.",
        ],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "Yes, the line <1><2> is on the top right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No, the line <1><2> is on the top right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No, the line <1><2> is on the top right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No, the line <1><2> is on the top right side of the figure.",
        #],
        [
            "Which side of the figure is the <3> line located, top right, top left, bottom right, or bottom left?",
            "The <3> line is located on the top right side of the figure.",
        ],
        #[
        #    "Is the <3> line on the top right side of the figure?",
        #    "Yes, the <3> line is on the top right side of the figure.",
        #],
        #[
        #    "Is the <3> line on the top left side of the figure?",
        #    "No, the <3> line is on the top right side of the figure.",
        #],
        #[
        #    "Is the <3> line on the bottom right side of the figure?",
        #    "No, the <3> line is on the top right side of the figure.",
        #],
        #[
        #    "Is the <3> line on the bottom left side of the figure?",
        #    "No, the <3> line is on the top right side of the figure.",
        #],
    ],
    "C_abs_position_line_topleft": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "The line <1><2> is located on the top left side of the figure.",
        ],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "Yes, the line <1><2> is on the top left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No, the line <1><2> is on the top left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No, the line <1><2> is on the top left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No, the line <1><2> is on the top left side of the figure.",
        #],
        [
            "Which side of the figure is the <3> line located, top right, top left, bottom right, or bottom left?",
            "The <3> line is located on the top left side of the figure.",
        ],
        #[
        #    "Is the <3> line on the top left side of the figure?",
        #    "Yes, the <3> line is on the top left side of the figure.",
        #],
        #[
        #    "Is the <3> line on the top right side of the figure?",
        #    "No, the <3> line is on the top left side of the figure.",
        #],
        #[
        #    "Is the <3> line on the bottom right side of the figure?",
        #    "No, the <3> line is on the top left side of the figure.",
        #],
        #[
        #    "Is the <3> line on the bottom left side of the figure?",
        #    "No, the <3> line is on the top left side of the figure.",
        #],
    ],
    "C_abs_position_line_bottomright": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "The line <1><2> is located on the bottom right side of the figure.",
        ],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "Yes, the line <1><2> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No, the line <1><2> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No, the line <1><2> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No, the line <1><2> is on the bottom right side of the figure.",
        #],
        [
            "Which side of the figure is the <3> line located, top right, top left, bottom right, or bottom left?",
            "The <3> line is located on the bottom right side of the figure.",
        ],
        #[
        #    "Is the <3> line on the bottom right side of the figure?",
        #    "Yes, the <3> line is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the <3> line on the top right side of the figure?",
        #    "No, the <3> line is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the <3> line on the top left side of the figure?",
        #    "No, the <3> line is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the <3> line on the bottom left side of the figure?",
        #    "No, the <3> line is on the bottom right side of the figure.",
        #],
    ],
    "C_abs_position_line_bottomleft": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "The line <1><2> is located on the bottom left side of the figure.",
        ],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "Yes, the line <1><2> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No, the line <1><2> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No, the line <1><2> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No, the line <1><2> is on the bottom left side of the figure.",
        #],
        [
            "Which side of the figure is the <3> line located, top right, top left, bottom right, or bottom left?",
            "The <3> line is located on the bottom left side of the figure.",
        ],
        #[
        #    "Is the <3> line on the bottom left side of the figure?",
        #    "Yes, the <3> line is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the <3> line on the top right side of the figure?",
        #    "No, the <3> line is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the <3> line on the top left side of the figure?",
        #    "No, the <3> line is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the <3> line on the bottom right side of the figure?",
        #    "No, the <3> line is on the bottom left side of the figure.",
        #],
    ],
    "abs_position_circle_right": [
        [
            "Which side of the figure is the circle <1> located, left or right?",
            "The circle <1> is located on the right side of the figure.",
        ],
        [
            "Is the circle <1> on the right side of the figure?",
            "Yes, the circle <1> is on the right side of the figure.",
        ],
        [
            "Is the circle <1> on the left side of the figure?",
            "No, the circle <1> is on the right side of the figure.",
        ],
    ],
    "abs_position_circle_left": [
        [
            "Which side of the figure is the circle <1> located, left or right?",
            "The circle <1> is located on the left side of the figure.",
        ],
        [
            "Is the circle <1> on the left side of the figure?",
            "Yes, the circle <1> is on the left side of the figure.",
        ],
        [
            "Is the circle <1> on the right side of the figure?",
            "No, the circle <1> is on the left side of the figure.",
        ],
    ],
    "abs_position_circle_top": [
        [
            "Which side of the figure is the circle <1> located, top or bottom?",
            "The circle <1> is located on the top side of the figure.",
        ],
        [
            "Is the circle <1> on the top side of the figure?",
            "Yes, the circle <1> is on the top side of the figure.",
        ],
        [
            "Is the circle <1> on the bottom side of the figure?",
            "No, the circle <1> is on the top side of the figure.",
        ],
    ],
    "abs_position_circle_bottom": [
        [
            "Which side of the figure is the circle <1> located, top or bottom?",
            "The circle <1> is located on the bottom side of the figure.",
        ],
        [
            "Is the circle <1> on the bottom side of the figure?",
            "Yes, the circle <1> is on the bottom side of the figure.",
        ],
        [
            "Is the circle <1> on the top side of the figure?",
            "No, the circle <1> is on the bottom side of the figure.",
        ],
    ],
    "abs_position_circle_topright": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "The circle <1> is located on the top right side of the figure.",
        ],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "Yes, the circle <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No, the circle <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No, the circle <1> is on the top right side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No, the circle <1> is on the top right side of the figure.",
        #],
    ],
    "abs_position_circle_topleft": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "The circle <1> is located on the top left side of the figure.",
        ],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "Yes, the circle <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No, the circle <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No, the circle <1> is on the top left side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No, the circle <1> is on the top left side of the figure.",
        #],
    ],
    "abs_position_circle_bottomright": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "The circle <1> is located on the bottom right side of the figure.",
        ],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "Yes, the circle <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No, the circle <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No, the circle <1> is on the bottom right side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No, the circle <1> is on the bottom right side of the figure.",
        #],
    ],
    "abs_position_circle_bottomleft": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "The circle <1> is located on the bottom left side of the figure.",
        ],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "Yes, the circle <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No, the circle <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No, the circle <1> is on the bottom left side of the figure.",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No, the circle <1> is on the bottom left side of the figure.",
        #],
    ],
    "abs_position_object": [
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "(<i>) <TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Choose from : [<TYPE> <LABEL>, ].",
            "<TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects: [<TYPE> <LABEL>, ]. Which object is in the <DIR> of the image?",
            "<TYPE> <LABEL>"
        ]
    ],
    "abs_position_object_colored": [
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "(<i>) <TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Choose from : [<TYPE> <LABEL>, ].",
            "<TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects: [<TYPE> <LABEL>, ]. Which object is in the <DIR> of the image?",
            "<TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects. Which is the color of the object in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <COLOR> ]",
            "(<i>) <COLOR>"
        ],
        [
            "In the image, there are several different objects. Which is the color of the object in the <DIR> of the image? Choose from : [<COLOR>, ].",
            "<COLOR>"
        ],
        [
            "In the image, there are several different objects drawn in different colors: [<COLOR>, ]. Which is the color of the object in the <DIR> of the image?",
            "<COLOR>"
        ]
    ],
    "abs_position_object_quadrant": [
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "(<i>) <TYPE> <LABEL>"
        ],
        [
            "There are several different objects in the image. When the image is divided into four quadrants, which object is in the <DIR> quadrant? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "(<i>) <TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects. If we divide the image into four equal parts (top left, top right, bottom left, bottom right), which object is in the <DIR> part? Choose from : [<TYPE> <LABEL>, ]",
            "<TYPE> <LABEL>"
        ]
    ],
    "abs_position_object_colored_quadrant": [
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "(<i>) <TYPE> <LABEL>"
        ],
        [
            "There are several different objects in the image. When the image is divided into four quadrants, which object is in the <DIR> quadrant? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "(<i>) <TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects. If we divide the image into four equal parts (top left, top right, bottom left, bottom right), which object is in the <DIR> part? Choose from : [<TYPE> <LABEL>, ]",
            "<TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects. Which is the color of the object in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <COLOR> ]",
            "(<i>) <COLOR>"
        ],
        [
            "In the image, there are several different objects. If we divide the image into four equal parts (top left, top right, bottom left, bottom right), which is the color of the object in the <DIR> part? Choose from : [<COLOR>, ]",
            "<COLOR>"
        ],
        [
            "In the image, there are several different objects. When the image is divided into four quadrants, which is the color of the object in the <DIR> quadrant? ",
            "<COLOR>"
        ]
    ],
}

conversation_short = {
    "abs_position_right": [
        [
            "Which side of the figure is the point <1> located, left or right?",
            "Right",
        ],
        [
            "Is the point <1> on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the point <1> on the left side of the figure?",
            "No",
        ],
    ],
    "abs_position_left": [
        [
            "Which side of the figure is the point <1> located, left or right?",
            "Left",
        ],
        [
            "Is the point <1> on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the point <1> on the right side of the figure?",
            "No",
        ],
    ],
    "abs_position_top": [
        [
            "Which side of the figure is the point <1> located, top or bottom?",
            "Top",
        ],
        [
            "Is the point <1> on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the point <1> on the bottom side of the figure?",
            "No",
        ],
    ],
    "abs_position_bottom": [
        [
            "Which side of the figure is the point <1> located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the point <1> on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the point <1> on the top side of the figure?",
            "No",
        ],
    ],
    "abs_position_topright": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "Top right",        
        ],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_topleft": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_bottomright": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_bottomleft": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_right": [
        [
            "Which side of the figure is the point <1> located, left or right?",
            "Right",
        ],
        [
            "Is the point <1> on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the point <1> on the left side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <2> point located, left or right?",
            "Right",
        ],
        [
            "Is the <2> point on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the <2> point on the left side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_left": [
        [
            "Which side of the figure is the point <1> located, left or right?",
            "Left",
        ],
        [
            "Is the point <1> on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the point <1> on the right side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <2> point located, left or right?",
            "Left",
        ],
        [
            "Is the <2> point on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the <2> point on the right side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_top": [
        [
            "Which side of the figure is the point <1> located, top or bottom?",
            "Top",
        ],
        [
            "Is the point <1> on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the point <1> on the bottom side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <2> point located, top or bottom?",
            "Top",
        ],
        [
            "Is the <2> point on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the <2> point on the bottom side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_bottom": [
        [
            "Which side of the figure is the point <1> located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the point <1> on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the point <1> on the top side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <2> point located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the <2> point on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the <2> point on the top side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_topright": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "Top right",
        ],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <2> point located, top right, top left, bottom right, or bottom left?",
            "Top right",
        ],
        #[
        #    "Is the <2> point on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <2> point on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> point on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> point on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_topleft": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <2> point located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the <2> point on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <2> point on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> point on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> point on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_bottomright": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <2> point located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the <2> point on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <2> point on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> point on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> point on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_bottomleft": [
        [
            "Which side of the figure is the point <1> located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the point <1> on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the point <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the point <1> on the bottom right side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <2> point located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the <2> point on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <2> point on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> point on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> point on the bottom right side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_line_right": [
        [
            "Which side of the figure is the line <1> located, left or right?",
            "Right",
        ],
        [
            "Is the line <1> on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the line <1> on the left side of the figure?",
            "No",
        ],
    ],
    "abs_position_line_left": [
        [
            "Which side of the figure is the line <1> located, left or right?",
            "Left",
        ],
        [
            "Is the line <1> on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the line <1> on the right side of the figure?",
            "No",
        ],
    ],
    "abs_position_line_top": [
        [
            "Which side of the figure is the line <1> located, top or bottom?",
            "Top",
        ],
        [
            "Is the line <1> on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the line <1> on the bottom side of the figure?",
            "No",
        ],
    ],
    "abs_position_line_bottom": [
        [
            "Which side of the figure is the line <1> located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the line <1> on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the line <1> on the top side of the figure?",
            "No",
        ],
    ],
    "abs_position_line_topright": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "Top right",
        ],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_line_topleft": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_line_bottomright": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_line_bottomleft": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_line_right": [
        [
            "Which side of the figure is the line <1><2> located, left or right?",
            "Right",
        ],
        [
            "Is the line <1><2> on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the line <1><2> on the left side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <3> line located, left or right?",
            "Right",
        ],
        [
            "Is the <3> line on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the <3> line on the left side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_line_left": [
        [
            "Which side of the figure is the line <1><2> located, left or right?",
            "Left",
        ],
        [
            "Is the line <1><2> on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the line <1><2> on the right side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <3> line located, left or right?",
            "Left",
        ],
        [
            "Is the <3> line on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the <3> line on the right side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_line_top": [
        [
            "Which side of the figure is the line <1><2> located, top or bottom?",
            "Top",
        ],
        [
            "Is the line <1><2> on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the line <1><2> on the bottom side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <3> line located, top or bottom?",
            "Top",
        ],
        [
            "Is the <3> line on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the <3> line on the bottom side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_line_bottom": [
        [
            "Which side of the figure is the line <1><2> located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the line <1><2> on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the line <1><2> on the top side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <3> line located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the <3> line on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the <3> line on the top side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_line_topright": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "Top right",
        ],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <3> line located, top right, top left, bottom right, or bottom left?",
            "Top right",
        ],
        #[
        #    "Is the <3> line on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <3> line on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <3> line on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <3> line on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_line_topleft": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <3> line located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the <3> line on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <3> line on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <3> line on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <3> line on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_line_bottomright": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <3> line located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the <3> line on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <3> line on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <3> line on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <3> line on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_line_bottomleft": [
        [
            "Which side of the figure is the line <1><2> located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the line <1><2> on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the line <1><2> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the line <1><2> on the bottom right side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <3> line located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the <3> line on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <3> line on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <3> line on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <3> line on the bottom right side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_circle_right": [
        [
            "Which side of the figure is the circle <1> located, left or right?",
            "Right",
        ],
        [
            "Is the circle <1> on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the circle <1> on the left side of the figure?",
            "No",
        ],
    ],
    "abs_position_circle_left": [
        [
            "Which side of the figure is the circle <1> located, left or right?",
            "Left",
        ],
        [
            "Is the circle <1> on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the circle <1> on the right side of the figure?",
            "No",
        ],
    ],
    "abs_position_circle_top": [
        [
            "Which side of the figure is the circle <1> located, top or bottom?",
            "Top",
        ],
        [
            "Is the circle <1> on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the circle <1> on the bottom side of the figure?",
            "No",
        ],
    ],
    "abs_position_circle_bottom": [
        [
            "Which side of the figure is the circle <1> located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the circle <1> on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the circle <1> on the top side of the figure?",
            "No",
        ],
    ],
    "abs_position_circle_topright": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "Top right",
        ],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_circle_topleft": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_circle_bottomright": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_circle_bottomleft": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_circle_right": [
        [
            "Which side of the figure is the circle <1> located, left or right?",
            "Right",
        ],
        [
            "Is the circle <1> on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the circle <1> on the left side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <2> circle located, left or right?",
            "Right",
        ],
        [
            "Is the <2> circle on the right side of the figure?",
            "Yes",
        ],
        [
            "Is the <2> circle on the left side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_circle_left": [
        [
            "Which side of the figure is the circle <1> located, left or right?",
            "Left",
        ],
        [
            "Is the circle <1> on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the circle <1> on the right side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <2> circle located, left or right?",
            "Left",
        ],
        [
            "Is the <2> circle on the left side of the figure?",
            "Yes",
        ],
        [
            "Is the <2> circle on the right side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_circle_top": [
        [
            "Which side of the figure is the circle <1> located, top or bottom?",
            "Top",
        ],
        [
            "Is the circle <1> on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the circle <1> on the bottom side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <2> circle located, top or bottom?",
            "Top",
        ],
        [
            "Is the <2> circle on the top side of the figure?",
            "Yes",
        ],
        [
            "Is the <2> circle on the bottom side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_circle_bottom": [
        [
            "Which side of the figure is the circle <1> located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the circle <1> on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the circle <1> on the top side of the figure?",
            "No",
        ],
        [
            "Which side of the figure is the <2> circle located, top or bottom?",
            "Bottom",
        ],
        [
            "Is the <2> circle on the bottom side of the figure?",
            "Yes",
        ],
        [
            "Is the <2> circle on the top side of the figure?",
            "No",
        ],
    ],
    "C_abs_position_circle_topright": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "Top right",
        ],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <2> circle located, top right, top left, bottom right, or bottom left?",
            "Top right",
        ],
        #[
        #    "Is the <2> circle on the top right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <2> circle on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> circle on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> circle on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_circle_topleft": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <2> circle located, top right, top left, bottom right, or bottom left?",
            "Top left",
        ],
        #[
        #    "Is the <2> circle on the top left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <2> circle on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> circle on the bottom right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> circle on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_circle_bottomright": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <2> circle located, top right, top left, bottom right, or bottom left?",
            "Bottom right",
        ],
        #[
        #    "Is the <2> circle on the bottom right side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <2> circle on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> circle on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> circle on the bottom left side of the figure?",
        #    "No",
        #],
    ],
    "C_abs_position_circle_bottomleft": [
        [
            "Which side of the figure is the circle <1> located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the circle <1> on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the circle <1> on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the circle <1> on the bottom right side of the figure?",
        #    "No",
        #],
        [
            "Which side of the figure is the <2> circle located, top right, top left, bottom right, or bottom left?",
            "Bottom left",
        ],
        #[
        #    "Is the <2> circle on the bottom left side of the figure?",
        #    "Yes",
        #],
        #[
        #    "Is the <2> circle on the top right side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> circle on the top left side of the figure?",
        #    "No",
        #],
        #[
        #    "Is the <2> circle on the bottom right side of the figure?",
        #    "No",
        #],
    ],
    "abs_position_object": [
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "<i>"
        ],
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Choose from : [<TYPE> <LABEL>, ].",
            "<TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects: [<TYPE> <LABEL>, ]. Which object is in the <DIR> of the image?",
            "<TYPE> <LABEL>"
        ]
    ],
    "abs_position_object_colored": [
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "<i>"
        ],
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Choose from : [<TYPE> <LABEL>, ].",
            "<TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects: [<TYPE> <LABEL>, ]. Which object is in the <DIR> of the image?",
            "<TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects. Which is the color of the object in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <COLOR> ]",
            "<i>"
        ],
        [
            "In the image, there are several different objects. Which is the color of the object in the <DIR> of the image? Choose from : [<COLOR>, ].",
            "<COLOR>"
        ],
        [
            "In the image, there are several different objects drawn in different colors: [<COLOR>, ]. Which is the color of the object in the <DIR> of the image?",
            "<COLOR>"
        ]
    ],
    "abs_position_object_quadrant": [
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "<i>"
        ],
        [
            "There are several different objects in the image. When the image is divided into four quadrants, which object is in the <DIR> quadrant? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "<i>"
        ],
        [
            "In the image, there are several different objects. If we divide the image into four equal parts (top left, top right, bottom left, bottom right), which object is in the <DIR> part? Choose from : [<TYPE> <LABEL>, ]",
            "<TYPE> <LABEL>"
        ]
    ],
    "abs_position_object_colored_quadrant": [
        [
            "In the image, there are several different objects. Which object is in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "<i>"
        ],
        [
            "There are several different objects in the image. When the image is divided into four quadrants, which object is in the <DIR> quadrant? Answer with a single number between 1 and <N>.\n [(<i>) <TYPE> <LABEL> ]",
            "<i>"
        ],
        [
            "In the image, there are several different objects. If we divide the image into four equal parts (top left, top right, bottom left, bottom right), which object is in the <DIR> part? Choose from : [<TYPE> <LABEL>, ]",
            "<TYPE> <LABEL>"
        ],
        [
            "In the image, there are several different objects. Which is the color of the object in the <DIR> of the image? Answer with a single number between 1 and <N>.\n [(<i>) <COLOR> ]",
            "<i>"
        ],
        [
            "There are several different objects in the image. When the image is divided into four quadrants, which is the color of the object in the <DIR> quadrant? Answer with a single number between 1 and <N>.\n [(<i>) <COLOR> ]",
            "<i>"
        ],
        [
            "In the image, there are several different objects. If we divide the image into four equal parts (top left, top right, bottom left, bottom right), which is the color of the object in the <DIR> part? Choose from : [<COLOR>, ]",
            "<COLOR>"
        ],
    ],
}


def generate_absolute_position(entity, long=False):
    if long:
        conversation = conversation_long
    else:
        conversation = conversation_short

    # if entity[0] starts with "abs_position_object"
    if entity[0].startswith("abs_position_object"):
        keyword = entity[0]
        index = random.randint(0, len(conversation[keyword]) - 1)
        q, a = conversation[keyword][index]

        # find the part in '[]' (in question)
        parts_q = re.findall(r"\[.*?\]", q)
        # for each part in [], replace <i>, <TYPE>, <DIR>, <LABEL>, <COLOR> with the actual values
        for k, part in enumerate(parts_q):
            new_part = ""
            for i, value in enumerate(entity[1]):
                new_part_frag = (part + '.')[:-1]
                new_part_frag = new_part_frag.replace(f"<i>", str(i + 1))
                new_part_frag = new_part_frag.replace(f"<TYPE>", value[0])
                new_part_frag = new_part_frag.replace(f"<DIR>", value[1])
                new_part_frag = new_part_frag.replace(f"<LABEL>", value[2])
                new_part_frag = new_part_frag.replace(f"<COLOR>", value[3])
                new_part = f"{new_part}{new_part_frag[1:-1]}"
            q = q.replace(parts_q[k], new_part)
        
        q = q.replace("<N>", str(len(entity[1])))
        q = q.replace("<TYPE>", entity[2][0])
        q = q.replace("<DIR>", entity[2][1])
        q = q.replace("<LABEL>", entity[2][2])
        q = q.replace("<COLOR>", entity[2][3])
        q = q.replace("<i>", str(entity[2][4]+1))

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

        return q, a

    (
        xdir,
        ydir,
    ) = (
        entity[2],
        entity[3],
    )

    # find conversation with keyword "{entity[0]}_{ydir}{xdir}"
    keyword = f"{entity[0]}_{ydir if ydir else ''}{xdir if xdir else ''}"

    index = random.randint(0, len(conversation[keyword]) - 1)
    q, a = conversation[keyword][index]

    # replace <1>, <2>, ... with the actual values
    for i in range(len(entity[1])):
        q = q.replace(f"<{i+1}>", entity[1][i])
        a = a.replace(f"<{i+1}>", entity[1][i])

    return q, a


def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        if "abs_position" in entity[0]:
            conversation_list.append(generate_absolute_position(entity, long))
        break
    return conversation_list
