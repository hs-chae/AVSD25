from .rules import *
import random

conversation = {
  "conversation_long": {
    "connectedness1": {
      "QA": [
        [
          "Is the line connecting the two points of color <1> continuous and unbroken?",
          "Yes, the line connecting the two <1>-colored points is indeed connected."
        ],
        [
          "Does the line linking the two points of color <1> remain fully connected?",
          "Yes, the line linking the two points of color <1> is fully connected."
        ],
        [
          "Would the line between the two <1>-colored points be considered uninterrupted?",
          "Indeed, the line between the two points of color <1> is connected without any breaks."
        ],
        [
          "Are the two <1>-colored points joined by a continuous line that does not break?",
          "Yes, those two points of color <1> are connected by an unbroken line."
        ],
        [
          "Is there a single unbroken segment connecting the two points of color <1>?",
          "Yes, a continuous segment links the two <1>-colored points."
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
    "connectedness2": {
      "QA": [
        [
          "Is the line connecting point <1> and point <2> continuous and unbroken?",
          "Yes, the line connecting point <1> and point <2> remains fully connected."
        ],
        [
          "Does the line from point <1> to point <2> stay uninterrupted?",
          "Yes, there is a continuous connection between point <1> and point <2>."
        ],
        [
          "Are points <1> and <2> joined by a line with no breaks?",
          "Yes, the line between points <1> and <2> shows no interruptions."
        ],
        [
          "Would you say the line linking point <1> with point <2> is unbroken?",
          "Indeed, point <1> and point <2> are connected by a continuous line."
        ],
        [
          "Is there a single unbroken path that connects point <1> and point <2>?",
          "Yes, point <1> and point <2> are connected by a single unbroken path."
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
    "connectedness3": {
      "QA": [
        [
          "Is the line connecting the two points of color <1> continuous and unbroken?",
          "No, the line connecting the two <1>-colored points is not connected."
        ],
        [
          "Does the line linking the two points of color <1> remain uninterrupted?",
          "No, the line linking the two points of color <1> is broken."
        ],
        [
          "Would the line between the two <1>-colored points be considered uninterrupted?",
          "No, the line between the two points of color <1> is not continuous."
        ],
        [
          "Are the two <1>-colored points joined by a continuous line with no breaks?",
          "No, those two points of color <1> are not connected by a continuous line."
        ],
        [
          "Is there a single unbroken segment connecting the two points of color <1>?",
          "No, the segment connecting the two <1>-colored points is not unbroken."
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
    "connectedness4": {
      "QA": [
        [
          "Is the line connecting point <1> and point <2> continuous and unbroken?",
          "No, the line connecting point <1> and point <2> is not connected."
        ],
        [
          "Does the line from point <1> to point <2> stay uninterrupted?",
          "No, there is a break in the connection between point <1> and point <2>."
        ],
        [
          "Are points <1> and <2> joined by a line with no breaks?",
          "No, the line between points <1> and <2> does not remain unbroken."
        ],
        [
          "Would you say the line linking point <1> with point <2> is unbroken?",
          "No, point <1> and point <2> are not connected by a continuous line."
        ],
        [
          "Is there a single unbroken path that connects point <1> and point <2>?",
          "No, point <1> and point <2> do not share an unbroken path."
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
    "connectedness5": {
      "QA": [
        [
          "How many connected shapes are present in the given figure?",
          "There are <2> connected shapes in the given figure."
        ],
        [
          "What is the number of connected shapes in the provided illustration?",
          "The given illustration contains <2> connected shapes."
        ],
        [
          "In the figure shown, how many connected shapes can be observed?",
          "You can observe <2> connected shapes in the figure."
        ],
        [
          "Determine the total count of connected shapes in the given diagram.",
          "This diagram includes <2> connected shapes in total."
        ],
        [
          "Identify how many connected shapes exist in the presented figure.",
          "There are <2> connected shapes within the presented figure."
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
          "For example, if the figure had <1> connected shapes, then the answer should be \"<1>\".",
          "As an example, if there were <1> connected shapes in the figure, the correct response would be \"<1>\".",
          "If, for instance, the diagram contained <1> connected shapes, the answer must be \"<1>\".",
          "For instance, suppose the figure has <1> connected shapes; then you should answer \"<1>\".",
          "Example: if the figure contains <1> connected shapes, your answer must simply be \"<1>\"."
        ],
        "type4": [
          ""
        ]
      }
    },
    "connectedness6": {
      "QA": [
        [
          "In the given figure, which shows some or all of the 9 nodes connected by edges, how many connected components are there?",
          "The number of connected components in the given figure is <1>."
        ],
        [
          "How many connected components can be identified among the 9 nodes in the provided diagram?",
          "In this diagram, the total count of connected components is <1>."
        ],
        [
          "Determine the number of connected components in the illustration, where edges link some (or all) of the 9 nodes.",
          "The figure contains <1> connected components."
        ],
        [
          "Please find the count of connected components present in the figure showing up to 9 interconnected nodes.",
          "There are <1> connected components in the given figure."
        ],
        [
          "What is the number of distinct connected components in the provided graph with up to 9 nodes connected by edges?",
          "This graph has <1> connected components."
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
          "If two nodes share an edge, then they belong to the same connected component.",
          "Any pair of nodes that are directly connected by an edge is part of the same connected component.",
          "Whenever there is an edge between two nodes, those nodes are considered to be in one connected component.",
          "Two nodes with an edge between them are included within a single connected component.",
          "When an edge links two nodes, those nodes fall under the same connected component."
        ],
        "type4": [
          "In other words, figure out how many 'islands' appear in this diagram.",
          "Put simply, please find the count of 'islands' in the given figure.",
          "Alternatively stated, determine how many distinct 'islands' are present in the diagram.",
          "Restated, you need to calculate the number of 'islands' in this figure.",
          "To rephrase, identify the total number of 'islands' in the provided diagram."
        ]
      }
    },
    "connectedness7": {
      "QA": [
        [
          "In the provided diagram of up to 9 interconnected nodes, present the list of connected components in the appropriate format.",
          "The list of connected components in the given figure is <1>."
        ],
        [
          "Could you list out all the connected components shown in the figure of 9 nodes, following the required structure?",
          "The figure's connected components can be represented as <1>."
        ],
        [
          "Please provide the list of connected components in the correct format for the graph with up to 9 nodes.",
          "Those connected components are given by <1>."
        ],
        [
          "Identify each connected component found among the 9 nodes and present them as a list in the proper format.",
          "The connected components are listed as <1>."
        ],
        [
          "How should the connected components be listed, according to the specified format, for the diagram of 9 nodes?",
          "They should be listed as <1>."
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          ""
        ],
        "type3": [
          "For example, if you have a graph containing nodes from <2> to <3>, and <4> is the adjacency matrix (where 0 denotes not connected and 1 denotes connected), then you should provide the answer in a format similar to <5>.",
          "As an illustration, consider a graph with nodes ranging from <2> to <3>, and an adjacency matrix <4>, where 0 and 1 represent disconnection and connection respectively; the correct response must follow the structure shown by <5>.",
          "Suppose there's a graph with nodes labeled from <2> to <3>, and <4> represents the adjacency matrix indicating connections (1) or lack thereof (0). In this case, your answer should be formatted like <5>.",
          "Imagine a graph that includes nodes <2> through <3> and employs <4> as its adjacency matrix, with 0 meaning no connection and 1 meaning a connection. You need to provide the solution in the same style as <5>.",
          "For instance, if the graph has nodes from <2> to <3>, with <4> denoting the adjacency matrix (where 0=not connected, 1=connected), then you must give your answer according to the template shown by <5>."
        ],
        "type4": [
          ""
        ]
      }
    },
    "connectedness8": {
      "QA": [
        [
          "Which nodes in the figure are directly connected to node <1>? Provide all of them.",
          "In the given figure, the nodes connected to node <1> are <2>."
        ],
        [
          "Identify all the nodes that share an edge with node <1> in the diagram.",
          "All nodes linked to node <1> in this figure are <2>."
        ],
        [
          "From the graph of up to 9 nodes, which ones are connected to node <1>?",
          "Node <1> in the diagram is connected to <2>."
        ],
        [
          "Please list every node that has a direct connection to node <1> in the provided figure.",
          "The set of nodes connected to <1> is <2>."
        ],
        [
          "In this graph, can you determine which nodes are connected to node <1>?",
          "Those connected to node <1> are <2>."
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
          "For instance, if node <1> is connected to X, Y, and Z, your answer should read 'X, Y, Z'.",
          "As an example, if <1> links to nodes X, Y, and Z, then the correct response would be 'X, Y, Z'.",
          "Suppose node <1> is connected to nodes labeled X, Y, and Z; you would write the answer as 'X, Y, Z'.",
          "If, for example, node <1> has edges to X, Y, and Z, you should provide the answer 'X, Y, Z'.",
          "Imagine that <1> is connected to X, Y, and Z. In such a case, 'X, Y, Z' would be the proper answer."
        ],
        "type4": [
          ""
        ]
      }
    }
  },
  "conversation_short": {
    "connectedness1": {
      "QA": [
        [
          "Is the line connecting the two points of color <1> connected?",
          "Yes"
        ],
        [
          "Do the two <1>-colored points share an unbroken line?",
          "Yes"
        ],
        [
          "Are the two points of color <1> joined without interruption?",
          "Yes"
        ],
        [
          "Is there a continuous path connecting the two <1>-colored points?",
          "Yes"
        ],
        [
          "Are the two points of color <1> linked by a single, unbroken connection?",
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
    "connectedness2": {
      "QA": [
        [
          "Are point <1> and point <2> connected by a continuous line?",
          "Yes"
        ],
        [
          "Does the line between point <1> and point <2> have no breaks?",
          "Yes"
        ],
        [
          "Is the connection from point <1> to point <2> unbroken?",
          "Yes"
        ],
        [
          "Are points <1> and <2> joined without interruption?",
          "Yes"
        ],
        [
          "Would you describe the line from point <1> to point <2> as continuous?",
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
    "connectedness3": {
      "QA": [
        [
          "Is the line connecting the two points of color <1> unbroken?",
          "No"
        ],
        [
          "Are the two <1>-colored points connected by a continuous line?",
          "No"
        ],
        [
          "Is there a continuous path linking the points of color <1>?",
          "No"
        ],
        [
          "Do the two points of color <1> share an unbroken connection?",
          "No"
        ],
        [
          "Would you say the line for the <1>-colored points is uninterrupted?",
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
    "connectedness4": {
      "QA": [
        [
          "Are point <1> and point <2> connected by a continuous line?",
          "No"
        ],
        [
          "Does the line between point <1> and point <2> have no breaks?",
          "No"
        ],
        [
          "Is the connection from point <1> to point <2> unbroken?",
          "No"
        ],
        [
          "Are points <1> and <2> joined without interruption?",
          "No"
        ],
        [
          "Would you describe the line from point <1> to point <2> as continuous?",
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
    "connectedness5": {
      "QA": [
        [
          "How many connected shapes does the figure have?",
          "<2>"
        ],
        [
          "What is the total number of connected shapes in the figure?",
          "<2>"
        ],
        [
          "How many connected shapes can you find in the given diagram?",
          "<2>"
        ],
        [
          "Identify the count of connected shapes in this illustration.",
          "<2>"
        ],
        [
          "In the presented figure, how many connected shapes are there?",
          "<2>"
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
          "For example, if the figure had <1> connected shapes, then the answer should be \"<1>\".",
          "As an example, if there were <1> connected shapes in the figure, the correct response would be \"<1>\".",
          "If, for instance, the diagram contained <1> connected shapes, the answer must be \"<1>\".",
          "For instance, suppose the figure has <1> connected shapes; then you should answer \"<1>\".",
          "Example: if the figure contains <1> connected shapes, your answer must simply be \"<1>\"."
        ],
        "type4": [
          ""
        ]
      }
    },
    "connectedness6": {
      "QA": [
        [
          "How many connected components are shown in the figure with some or all of the 9 nodes connected?",
          "<1>"
        ],
        [
          "What is the total number of connected components in the given diagram of 9 nodes?",
          "<1>"
        ],
        [
          "Identify how many connected components exist among the 9 nodes in the figure.",
          "<1>"
        ],
        [
          "In the provided figure featuring up to 9 connected nodes, how many connected components are there?",
          "<1>"
        ],
        [
          "Determine the count of connected components in the graph where edges link some of the 9 nodes.",
          "<1>"
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
          "If two nodes share an edge, then they belong to the same connected component.",
          "Any pair of nodes that are directly connected by an edge is part of the same connected component.",
          "Whenever there is an edge between two nodes, those nodes are considered to be in one connected component.",
          "Two nodes with an edge between them are included within a single connected component.",
          "When an edge links two nodes, those nodes fall under the same connected component."
        ],
        "type4": [
          "In other words, figure out how many 'islands' appear in this diagram.",
          "Put simply, please find the count of 'islands' in the given figure.",
          "Alternatively stated, determine how many distinct 'islands' are present in the diagram.",
          "Restated, you need to calculate the number of 'islands' in this figure.",
          "To rephrase, identify the total number of 'islands' in the provided diagram."
        ]
      }
    },
    "connectedness7": {
      "QA": [
        [
          "Provide the list of connected components for the 9-node diagram in the correct format.",
          "<1>"
        ],
        [
          "What is the formatted list of connected components in the figure?",
          "<1>"
        ],
        [
          "List the connected components shown in this graph with up to 9 nodes.",
          "<1>"
        ],
        [
          "Identify the connected components in the figure and present them in the required list format.",
          "<1>"
        ],
        [
          "How are the connected components arranged in the given diagram?",
          "<1>"
        ]
      ],
      "additional": {
        "type1": [
          "False"
        ],
        "type2": [
          ""
        ],
        "type3": [
          "For example, if you have a graph containing nodes from <2> to <3>, and <4> is the adjacency matrix (where 0 denotes not connected and 1 denotes connected), then you should provide the answer in a format similar to <5>.",
          "As an illustration, consider a graph with nodes ranging from <2> to <3>, and an adjacency matrix <4>, where 0 and 1 represent disconnection and connection respectively; the correct response must follow the structure shown by <5>.",
          "Suppose there's a graph with nodes labeled from <2> to <3>, and <4> represents the adjacency matrix indicating connections (1) or lack thereof (0). In this case, your answer should be formatted like <5>.",
          "Imagine a graph that includes nodes <2> through <3> and employs <4> as its adjacency matrix, with 0 meaning no connection and 1 meaning a connection. You need to provide the solution in the same style as <5>.",
          "For instance, if the graph has nodes from <2> to <3>, with <4> denoting the adjacency matrix (where 0=not connected, 1=connected), then you must give your answer according to the template shown by <5>."
        ],
        "type4": [
          ""
        ]
      }
    },
    "connectedness8": {
      "QA": [
        [
          "Which nodes are connected to node <1> in the figure?",
          "<2>"
        ],
        [
          "List the nodes that share an edge with node <1>.",
          "<2>"
        ],
        [
          "Identify all nodes connected to <1>.",
          "<2>"
        ],
        [
          "From the diagram, which nodes link to node <1>?",
          "<2>"
        ],
        [
          "In the given figure, which nodes are connected to node <1>?",
          "<2>"
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
          "For instance, if node <1> is connected to X, Y, and Z, your answer should read 'X, Y, Z'.",
          "As an example, if <1> links to nodes X, Y, and Z, then the correct response would be 'X, Y, Z'.",
          "Suppose node <1> is connected to nodes labeled X, Y, and Z; you would write the answer as 'X, Y, Z'.",
          "If, for example, node <1> has edges to X, Y, and Z, you should provide the answer 'X, Y, Z'.",
          "Imagine that <1> is connected to X, Y, and Z. In such a case, 'X, Y, Z' would be the proper answer."
        ],
        "type4": [
          ""
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