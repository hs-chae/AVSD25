from .rules import *
import random

conversation = {
    "conversation_long": {
      "adjacency1": {
        "QA": [
          [
            "In the image, each of the <1> rows and <2> columns of cells is colored in <4>. Cells of the same color form a single-colored region. Identify all the colors of the regions that share at least one side with the <3> region.",
            "The regions with color <7> share at least one side with the <3> region."
          ],
          [
            "You have an arrangement of <1> rows and <2> columns, each cell colored according to <4>. Determine which region colors share a common edge with the <3> region.",
            "Color <7> regions are adjacent by at least one side to the <3> region."
          ],
          [
            "Observe the <1> rows by <2> columns grid, where cells are colored with <4>. Which colors belong to regions that have at least one shared side with the <3> region?",
            "Those regions that have color <7> share a common edge with the <3> region."
          ],
          [
            "Given a grid of <1> rows and <2> columns colored in <4>, find all region colors that are adjacent by at least one side to the <3> region.",
            "The region(s) in color <7> directly share a border with the <3> region."
          ],
          [
            "In this <1> by <2> grid, the cells are colored using <4>. Some adjacent cells of the same color form a region. Please list all the colors that share a border with the <3> region.",
            "All regions colored <7> are side-adjacent to the <3> region."
          ]
        ],
        "additional": {
          "type1": [
            "False"
          ],
          "type2": [
            [
              "Select one word from the parentheses to complete the sentence. The regions with color (<5>) share at least one side with the <3> region.",
              "The regions with color <7> share at least one side with the <3> region."
            ],
            [
              "Pick the correct term from the parentheses. The regions that have color (<5>) are adjacent by at least one side to the <3> region.",
              "The regions with color <7> share at least one side with the <3> region."
            ],
            [
              "Choose the word within parentheses to finish the statement: The <3> region is side-adjacent to the region(s) colored (<5>).",
              "The regions with color <7> share at least one side with the <3> region."
            ],
            [
              "Use the parentheses to complete the sentence: The regions with color (<5>) are adjacent by a shared edge to the <3> region.",
              "The regions with color <7> share at least one side with the <3> region."
            ],
            [
              "From the parentheses, select the color that completes the sentence. Regions with color (<5>) share at least one side with the <3> region.",
              "The regions with color <7> share at least one side with the <3> region."
            ]
          ],
          "type3": [
            "For example, if the adjacent region colors are Red and Blue, write 'Red, Blue'.",
            "If two regions that share a side have colors C1 and C2, the answer format is 'C1, C2'.",
            "Imagine the adjacent colors are 'Green' and 'Yellow'; then you should answer 'Green, Yellow'.",
            "As an instance, if 'Orange' and 'Purple' are adjacent to <3>, respond with 'Orange, Purple'.",
            "Should the adjoining colors be 'Pink' and 'Gray', you would write 'Pink, Gray' as your answer."
          ],
          "type4": [
            "You must choose your answer from among <6>.",
            "Select the correct colors from <6>.",
            "Pick the appropriate option from <6>.",
            "Your answer should be one of those listed in <6>.",
            "The valid choices for the answer are contained in <6>."
          ]
        }
      },
      "adjacency2": {
        "QA": [
          [
            "In the image, a matrix is displayed with an element labeled <3>. Adjacency is defined by sharing edges vertically or horizontally. Which elements are adjacent to the <3> element?",
            "The elements that are adjacent to <3> in the given table are <7>."
          ],
          [
            "Examine the provided matrix containing an element labeled <3>. List all elements that share a direct edge (up, down, left, right) with <3>.",
            "Those elements adjacent to <3> are <7>."
          ],
          [
            "Look at the matrix in the image. The element <3> is there. Which elements in the matrix are directly adjacent (above, below, left, or right) to <3>?",
            "In this table, the elements neighboring <3> are <7>."
          ],
          [
            "Given a matrix with an element labeled <3>, identify all elements that are considered adjacent to it by vertical or horizontal contact.",
            "All elements that are neighbors to <3> in the table are <7>."
          ],
          [
            "You have a matrix that includes an element named <3>. Which elements in the matrix are immediately adjacent to <3> (up, down, left, right)?",
            "The table shows that <3> is adjacent to <7>."
          ]
        ],
        "additional": {
          "type1": [
            "True"
          ],
          "type2": [
            [
              "Select the appropriate word from the parentheses. In the given table, the elements neighboring <3> are (<5>).",
              "In the given table, the elements neighboring <3> are <7>."
            ],
            [
              "Choose one option from the parentheses to complete the statement: The matrix elements adjacent to <3> are (<5>).",
              "The matrix elements adjacent to <3> are <7>."
            ],
            [
              "Pick from the parentheses to form a complete sentence: The items next to <3> are (<5>) in the given table.",
              "The items next to <3> are <7> in the given table."
            ],
            [
              "Use the parentheses to fill in the blank: In the table, (<5>) represents the elements adjacent to <3>.",
              "In the table, <7> represents the elements adjacent to <3>."
            ],
            [
              "From the parentheses, select the correct label for the elements adjacent to <3>. Those elements are (<5>).",
              "The elements adjacent to <3> are <7>."
            ]
          ],
          "type3": [
            "For instance, if 'a' and 'b' are adjacent to <3>, the answer should be 'a, b'.",
            "If the neighbors of <3> are 'x' and 'y', you should respond with 'x, y'.",
            "As an example, if <3>'s adjacent elements are A and B, your answer would be 'A, B'.",
            "Suppose 'L' and 'M' are next to <3>; then write 'L, M' as the answer.",
            "If 'P' and 'Q' are directly adjacent to <3>, then you must answer 'P, Q'."
          ],
          "type4": [
            "You must choose from among <6> for the correct answer.",
            "Select the correct elements from <6>.",
            "Pick the right labels from <6>.",
            "Your response should be one of the options listed in <6>.",
            "The possible answers are contained in <6>."
          ]
        }
      }
    }
    ,
    "conversation_short": {
      "adjacency1": {
        "QA": [
          [
            "Which colors share at least one side with the <3> region in the <1> by <2> colored grid?",
            "<7>"
          ],
          [
            "Name all region colors that are adjacent by one side to the <3> region.",
            "<7>"
          ],
          [
            "Identify the colors of the regions that share a side with the <3> region.",
            "<7>"
          ],
          [
            "Which colors belong to the regions that border the <3> region?",
            "<7>"
          ],
          [
            "In the grid, which region colors are side-adjacent to the <3> region?",
            "<7>"
          ]
        ],
        "additional": {
          "type1": [
            "False"
          ],
          "type2": [
            "Select one word from the parentheses to complete the sentence. The regions with color (<5>) share at least one side with the <3> region.",
            "Pick the correct term from the parentheses. The regions that have color (<5>) are adjacent by at least one side to the <3> region.",
            "Choose the word within parentheses to finish the statement: The <3> region is side-adjacent to the region(s) colored (<5>).",
            "Use the parentheses to complete the sentence: The regions with color (<5>) are adjacent by a shared edge to the <3> region.",
            "From the parentheses, select the color that completes the sentence. Regions with color (<5>) share at least one side with the <3> region."
          ],
          "type3": [
            "For example, if the adjacent region colors are Red and Blue, write 'Red, Blue'.",
            "If two regions that share a side have colors C1 and C2, the answer format is 'C1, C2'.",
            "Imagine the adjacent colors are 'Green' and 'Yellow'; then you should answer 'Green, Yellow'.",
            "As an instance, if 'Orange' and 'Purple' are adjacent to <3>, respond with 'Orange, Purple'.",
            "Should the adjoining colors be 'Pink' and 'Gray', you would write 'Pink, Gray' as your answer."
          ],
          "type4": [
            "You must choose your answer from among <6>.",
            "Select the correct colors from <6>.",
            "Pick the appropriate option from <6>.",
            "Your answer should be one of those listed in <6>.",
            "The valid choices for the answer are contained in <6>."
          ]
        }
      },
      "adjacency2": {
        "QA": [
          [
            "Which elements in the matrix are next to <3>?",
            "<7>"
          ],
          [
            "Name all adjacent elements to <3> in the table.",
            "<7>"
          ],
          [
            "List the elements directly neighboring <3>.",
            "<7>"
          ],
          [
            "Which items are adjacent (up, down, left, right) to <3>?",
            "<7>"
          ],
          [
            "Identify the neighbors of <3> in the given matrix.",
            "<7>"
          ]
        ],
        "additional": {
          "type1": [
            "True"
          ],
          "type2": [
            "Select the appropriate word from the parentheses. In the given table, the elements neighboring <3> are (<5>).",
            "Choose one option from the parentheses to complete the statement: The matrix elements adjacent to <3> are (<5>).",
            "Pick from the parentheses to form a complete sentence: The items next to <3> are (<5>) in the given table.",
            "Use the parentheses to fill in the blank: In the table, (<5>) represents the elements adjacent to <3>.",
            "From the parentheses, select the correct label for the elements adjacent to <3>. Those elements are (<5>)."
          ],
          "type3": [
            "For instance, if 'a' and 'b' are adjacent to <3>, the answer should be 'a, b'.",
            "If the neighbors of <3> are 'x' and 'y', you should respond with 'x, y'.",
            "As an example, if <3>'s adjacent elements are A and B, your answer would be 'A, B'.",
            "Suppose 'L' and 'M' are next to <3>; then write 'L, M' as the answer.",
            "If 'P' and 'Q' are directly adjacent to <3>, then you must answer 'P, Q'."
          ],
          "type4": [
            "You must choose from among <6> for the correct answer.",
            "Select the correct elements from <6>.",
            "Pick the right labels from <6>.",
            "Your response should be one of the options listed in <6>.",
            "The possible answers are contained in <6>."
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