from .rules import *
import json
import random

def file_open(file_path):
    with open(file_path, "r") as read_content: 
        return json.load(read_content)

conversation_long = {
    "coordinate1": [
      [
        "Is this figure related to the Cartesian coordinate system or the Polar coordinate system?",
        "The given figure is related to the <2> coordinate system."
      ],
      [
        "Does the figure illustrate a Cartesian or a Polar coordinate system?",
        "The figure shown here is associated with the <2> coordinate system."
      ],
      [
        "Which coordinate system does the presented figure use: Cartesian or Polar?",
        "It is the <2> coordinate system shown in the figure."
      ],
      [
        "Identify whether this figure corresponds to a Cartesian coordinate system or a Polar coordinate system.",
        "This figure corresponds to the <2> coordinate system."
      ],
      [
        "Determine if the figure is based on a Cartesian coordinate system or a Polar coordinate system.",
        "The figure depicted is based on the <2> coordinate system."
      ]
    ],
    "coordinate2": [
      [
        "What are the coordinates of point <2> in the given figure? Provide your answer in the form <2>(x, y).",
        "The coordinates of point <2> are <2>(<3>, <4>)."
      ],
      [
        "Please specify the coordinates of point <2> from the figure, using the format <2>(x, y).",
        "Point <2> is located at <2>(<3>, <4>)."
      ],
      [
        "In the figure, can you identify the coordinates of point <2>? Express them as <2>(x, y).",
        "You can write the coordinates of point <2> as <2>(<3>, <4>)."
      ],
      [
        "According to the given figure, what are the (x, y) coordinates of point <2>?",
        "According to the figure, point <2> sits at <2>(<3>, <4>)."
      ],
      [
        "Determine the coordinates of point <2> from the figure. Present your answer in the form <2>(x, y).",
        "Point <2> has the coordinates <2>(<3>, <4>)."
      ]
    ],
    "coordinate3": [
      [
        "What are the coordinates of the point that has the color <2>? Please give the answer in (x, y) form.",
        "The coordinates of the point colored <2> are (<3>, <4>)."
      ],
      [
        "From the figure, identify the (x, y) coordinates of the point whose color is <2>.",
        "The point with color <2> is positioned at (<3>, <4>)."
      ],
      [
        "Which point in the figure is colored <2>, and what are its coordinates in the format (x, y)?",
        "The point with the color <2> can be found at (<3>, <4>)."
      ],
      [
        "Could you determine the (x, y) location of the point that has color <2> in this figure?",
        "Its coordinates, for the point with color <2>, are (<3>, <4>)."
      ],
      [
        "Please specify the coordinates (x, y) of the point whose color is <2> in the given figure.",
        "The point whose color is <2> has coordinates (<3>, <4>)."
      ]
    ],
    "coordinate4": [
      [
        "In the provided figure, what is the label of the point that has the same <3> coordinate as point <2>?",
        "The point that shares the same <3> coordinate with point <2> is point <4>."
      ],
      [
        "Find the point label which has the same <3> coordinate as point <2> in the diagram.",
        "Point <4> has the same <3> coordinate as point <2>."
      ],
      [
        "Which point in the figure matches point <2> in the <3> coordinate, and what is its label?",
        "The label of the point sharing <3> with point <2> is <4>."
      ],
      [
        "Identify the point whose <3> coordinate is identical to that of point <2>. What is its label?",
        "That point is labeled <4>, as it has the same <3> coordinate as <2>."
      ],
      [
        "Please name the point with the same <3> coordinate as point <2> in the figure.",
        "The point with the same <3> coordinate as <2> is point <4>."
      ]
    ],
    "coordinate5": [
      [
        "Which point in the figure has the same <3> coordinate as the point that is colored <2>, and what is its color?",
        "The point that shares the <3> coordinate with the point colored <2> is the point with color <4>."
      ],
      [
        "Identify the color of the point that has the same <3> coordinate as the point of color <2>.",
        "It has color <4>, matching the <3> coordinate of the <2>-colored point."
      ],
      [
        "From the diagram, find the point whose <3> coordinate is the same as that of the <2>-colored point. Which color is it?",
        "The point with the same <3> coordinate is the one with color <4>."
      ],
      [
        "Determine the color of the point that shares the <3> coordinate with the point of color <2>.",
        "That point’s color is <4>, matching the <3> coordinate of the <2>-colored point."
      ],
      [
        "What is the color of the point that has the same <3> coordinate as the <2>-colored point?",
        "The color of that point is <4>, given it shares the <3> coordinate with the <2>-colored point."
      ]
    ],
    "coordinate6": [
      [
        "Which two points in the figure have the same <2> coordinate? Please select them.",
        "Points <3> and <4> share the same <2> coordinate."
      ],
      [
        "Identify the pair of points that have identical <2> coordinates in the given figure.",
        "Point <3> and point <4> have matching <2> coordinates."
      ],
      [
        "Find two points with the same <2> coordinate in the diagram.",
        "The two points with the same <2> coordinate are <3> and <4>."
      ],
      [
        "From the figure, choose the points whose <2> coordinates coincide.",
        "It is <3> and <4> that have the same <2> coordinate."
      ],
      [
        "Determine the pair of points that share the <2> coordinate in this diagram.",
        "Points <3> and <4> share that <2> coordinate."
      ]
    ],
    "coordinate7": [
      [
        "Which two points have the same <2> coordinate? Please provide their colors.",
        "The points with colors <3> and <4> share the same <2> coordinate."
      ],
      [
        "Identify the colors of the points that have the same <2> coordinate in the figure.",
        "Color <3> and color <4> correspond to points whose <2> coordinate is identical."
      ],
      [
        "Find the two points that share the <2> coordinate, and state their colors.",
        "They are the points colored <3> and <4>, both having the same <2> coordinate."
      ],
      [
        "In this diagram, which point colors match in terms of <2> coordinates?",
        "Points with colors <3> and <4> have identical <2> coordinates."
      ],
      [
        "Tell me the colors of the two points that have identical <2> coordinates.",
        "Those two points are colored <3> and <4>, sharing the same <2> coordinate."
      ]
    ],
  
    "coordinate8": [
      [
        "Which point has the <3> <2> coordinate?",
        "Point <4> has the <3> <2> coordinate."
      ],
      [
        "Identify the point that shows the <3> <2> coordinate in the figure.",
        "The point with the <3> <2> coordinate is <4>."
      ],
      [
        "In this diagram, which point is recognized for having the <3> <2> coordinate?",
        "That point is <4>, as it has the <3> <2> coordinate."
      ],
      [
        "Can you tell me which point exhibits the <3> <2> coordinate?",
        "Point <4> is the one with the <3> <2> coordinate."
      ],
      [
        "From the figure, which point is noted to possess the <3> <2> coordinate?",
        "We observe that point <4> holds the <3> <2> coordinate."
      ]
    ],
    "coordinate9": [
      [
        "Which point has the <3> <2> coordinate, and what is its color?",
        "The point with color <4> has the <3> <2> coordinate."
      ],
      [
        "Identify the point that shows the <3> <2> coordinate and specify its color.",
        "Its color is <4>, matching the <3> <2> coordinate."
      ],
      [
        "Which point in the figure is noted for having the <3> <2> coordinate? State its color.",
        "It is the <4>-colored point that has the <3> <2> coordinate."
      ],
      [
        "Please tell me the color of the point that holds the <3> <2> coordinate.",
        "That point is colored <4>, with the <3> <2> coordinate."
      ],
      [
        "Which point in the diagram is recognized by the <3> <2> coordinate? Indicate its color.",
        "We can see the point colored <4> has the <3> <2> coordinate."
      ]
    ],
  
    "coordinate10": [
      [
        "Which quadrant does point <2> lie in?",
        "Point <2> is located in the <3> quadrant."
      ],
      [
        "Identify the quadrant where point <2> is situated.",
        "Point <2> can be found in quadrant <3>."
      ],
      [
        "Determine the quadrant number for point <2> in the figure.",
        "It turns out that point <2> lies in the <3> quadrant."
      ],
      [
        "In which quadrant of the coordinate plane is point <2> placed?",
        "Point <2> occupies the <3> quadrant."
      ],
      [
        "Find the quadrant of point <2> in this diagram.",
        "The quadrant for point <2> is <3>."
      ]
    ],
    "coordinate11": [
      [
        "Which quadrant is occupied by the point whose color is <2>?",
        "The point with color <2> is located in the <3> quadrant."
      ],
      [
        "Identify the quadrant for the point that has color <2>.",
        "That <2>-colored point lies in quadrant <3>."
      ],
      [
        "Determine the quadrant number in which the <2>-colored point is found.",
        "You can find the <2>-colored point in the <3> quadrant."
      ],
      [
        "In which quadrant is the point of color <2> placed?",
        "The <2>-colored point is positioned in the <3> quadrant."
      ],
      [
        "Find the quadrant of the point colored <2> in this diagram.",
        "That point belongs to the <3> quadrant."
      ]
    ],
    "coordinate12": [
      [
        "The function <2> matches the given graph. What is its <3>-intercept?",
        "The <3>-intercept of the provided graph is <4>."
      ],
      [
        "Identify the <3>-intercept of the graph for the function <2> as shown.",
        "For the displayed function <2>, the <3>-intercept is <4>."
      ],
      [
        "Given that the graph represents <2>, find its <3>-intercept.",
        "The graph’s <3>-intercept is <4>."
      ],
      [
        "What is the <3>-intercept for the function <2> based on the figure?",
        "It turns out that the <3>-intercept is <4>."
      ],
      [
        "Determine the <3>-intercept of <2> from the provided graph.",
        "From the given graph, the <3>-intercept is <4>."
      ]
    ],
    "coordinate13": [
      [
        "Which quadrant does the shape <2> lie in?",
        "Shape <2> is located in the <3> quadrant."
      ],
      [
        "Identify the quadrant in which the shape <2> can be found.",
        "The shape <2> occupies quadrant <3>."
      ],
      [
        "Where is the shape <2> placed in terms of quadrants?",
        "It is in the <3> quadrant for shape <2>."
      ],
      [
        "Determine the quadrant number that contains the shape <2>.",
        "Shape <2> resides in the <3> quadrant."
      ],
      [
        "In which quadrant does shape <2> appear in the diagram?",
        "You will find shape <2> in quadrant <3>."
      ]
    ],
    "coordinate14": [
      [
        "Which quadrant(s) does shape <2> pass through? List all relevant quadrants.",
        "Shape <2> passes through the <3> quadrant(s)."
      ],
      [
        "Identify all quadrants that shape <2> spans, if it crosses more than one quadrant.",
        "Shape <2> goes through quadrant(s) <3>."
      ],
      [
        "Determine every quadrant that shape <2> intersects. Provide all that apply.",
        "Shape <2> intersects the <3> quadrant(s)."
      ],
      [
        "In which quadrant or quadrants can we find shape <2>?",
        "Shape <2> can be found traversing the <3> quadrant(s)."
      ],
      [
        "Which quadrant(s) does shape <2> cover according to the figure?",
        "According to the figure, shape <2> covers the <3> quadrant(s)."
      ]
    ],
    "coordinate15": [
      [
        "Out of the points <2>, which ones lie inside the shape <3>?",
        "<4> are located inside shape <3>."
      ],
      [
        "From the list of points <2>, identify all points contained within shape <3>.",
        "The points <4> lie inside shape <3>."
      ],
      [
        "Which of the points <2> can be found inside the boundaries of shape <3>?",
        "<4> can be found within shape <3>."
      ],
      [
        "Select all points among <2> that are positioned inside shape <3>.",
        "Inside shape <3>, you will find <4>."
      ],
      [
        "Determine which points from <2> are contained in shape <3>.",
        "<4> remain inside the shape <3>."
      ]
    ],
    "coordinate16": [
      [
        "Which of the points <2> lie outside the shape <3>?",
        "<5> are the points outside shape <3>."
      ],
      [
        "Identify all points among <2> that are not inside shape <3>.",
        "Those outside shape <3> are <5>."
      ],
      [
        "From the list <2>, which points are located beyond the boundaries of shape <3>?",
        "The points outside shape <3> include <5>."
      ],
      [
        "Please select the points from <2> that do not lie within shape <3>.",
        "Outside of shape <3>, we have <5>."
      ],
      [
        "Determine the points among <2> that lie outside the region of shape <3>.",
        "<5> remain outside the shape <3>."
      ]
    ],
    "coordinate17": [
      [
        "What are the coordinates of point <2> in the given figure, expressed in <2>(r, theta) form?",
        "Point <2> has the coordinates <2>(<3>, <4>)."
      ],
      [
        "Identify the polar coordinates of point <2> as <2>(r, theta).",
        "The coordinates of point <2> in polar form are <2>(<3>, <4>)."
      ],
      [
        "In the figure, which polar coordinates does point <2> have? Provide them as <2>(r, theta).",
        "You can express point <2> as <2>(<3>, <4>)."
      ],
      [
        "Please specify the (r, theta) coordinates of point <2> from the diagram.",
        "According to the diagram, point <2> is at <2>(<3>, <4>)."
      ],
      [
        "Determine the location of point <2> in polar coordinates, using the format <2>(r, theta).",
        "Point <2> is positioned at <2>(<3>, <4>) in polar form."
      ]
    ],
    "coordinate18": [
      [
        "In the given figure, what are the polar coordinates (r, theta) of the point colored <2>?",
        "The point with color <2> has the coordinates (<3>, <4>) in polar form."
      ],
      [
        "Please find the polar coordinates for the <2>-colored point. Provide your answer as (r, theta).",
        "That <2>-colored point is located at (<3>, <4>) in polar coordinates."
      ],
      [
        "Identify the (r, theta) coordinates of the point whose color is <2>. Use polar notation.",
        "Its polar coordinates are (<3>, <4>) for the point with color <2>."
      ],
      [
        "Which coordinates describe the <2>-colored point in polar form (r, theta)?",
        "The <2>-colored point can be described as (<3>, <4>) in polar form."
      ],
      [
        "From the figure, specify the polar coordinates of the point colored <2> as (r, theta).",
        "In the figure, the point colored <2> is situated at (<3>, <4>) in polar coordinates."
      ]
    ],
    "coordinate19": [
      [
        "Which point has the same <3> coordinate as point <2> in the polar system, and what is its label?",
        "The point sharing the same <3> coordinate with point <2> is labeled <4>."
      ],
      [
        "Find the label of the point that matches point <2> in its <3> coordinate (polar).",
        "Point <4> has the same <3> coordinate as point <2>."
      ],
      [
        "Identify the point label whose <3> coordinate is identical to that of point <2> in polar coordinates.",
        "That would be point <4>, sharing the <3> coordinate with <2>."
      ],
      [
        "Which point in this polar coordinate setup shares the same <3> coordinate as point <2>?",
        "Point <4> is the one that aligns with <2> in terms of the <3> coordinate."
      ],
      [
        "Determine the label of the point that has the same <3> coordinate as point <2> in the figure.",
        "The point labeled <4> matches point <2> in the <3> coordinate."
      ]
    ],
    "coordinate20": [
      [
        "Which point has the same <3> coordinate as the point of color <2> in the polar system, and what is its color?",
        "The point with color <4> shares the same <3> coordinate as the <2>-colored point."
      ],
      [
        "Identify the color of the point that matches the <2>-colored point in the <3> coordinate (polar).",
        "It is the point with color <4> that shares the <3> coordinate."
      ],
      [
        "Which point in the polar diagram has the same <3> coordinate as the point colored <2>, and what is its color?",
        "That point’s color is <4>, since it shares <3> with the <2>-colored point."
      ],
      [
        "Find the point that has an identical <3> coordinate to the <2>-colored point in polar form. Which color is it?",
        "Its color is <4>, matching the <3> coordinate of the <2>-colored point."
      ],
      [
        "Determine which point color aligns with the <2>-colored point’s <3> coordinate in the figure.",
        "The color of that point is <4> because it shares the <3> coordinate with <2>."
      ]
    ],
    "coordinate21": [
      [
        "Which two points in the polar coordinate system share the same <2> coordinate? Select them.",
        "Points <3> and <4> have identical <2> coordinates."
      ],
      [
        "Identify the pair of points in polar form whose <2> coordinates coincide.",
        "Those two points are <3> and <4>, sharing the same <2> coordinate."
      ],
      [
        "Find two points in the figure that match each other in terms of <2> (polar).",
        "You can see points <3> and <4> have the same <2> coordinate."
      ],
      [
        "Among the points shown, which pair has the same <2> coordinate in polar form?",
        "Point <3> and point <4> share that <2> coordinate."
      ],
      [
        "Select the points that have the same <2> coordinate in this polar diagram.",
        "The points <3> and <4> are aligned in <2> coordinate."
      ]
    ],
    "coordinate22": [
      [
        "Which two points have the same <2> coordinate in polar form? Please state their colors.",
        "Points with colors <3> and <4> share the same <2> coordinate."
      ],
      [
        "Identify the colors of the points whose <2> coordinates match in this polar diagram.",
        "Colors <3> and <4> indicate points that align in <2>."
      ],
      [
        "Find the two point colors that coincide in the <2> coordinate (polar).",
        "They are <3> and <4>, having the same <2> coordinate."
      ],
      [
        "In the figure, which point colors correspond to identical <2> coordinates?",
        "The point colors <3> and <4> share that <2> coordinate."
      ],
      [
        "State the colors of the points that match each other’s <2> coordinate in the polar system.",
        "Those two points are colored <3> and <4> with the same <2> coordinate."
      ]
    ],
  
    "coordinate23": [
      [
        "Which point has the <3> <2> coordinate in this polar diagram?",
        "Point <4> has the <3> <2> coordinate."
      ],
      [
        "Identify the point that shows the <3> <2> coordinate (polar).",
        "The <3> <2> coordinate belongs to point <4>."
      ],
      [
        "Which point in the polar coordinate system is recognized for having the <3> <2> coordinate?",
        "That distinction goes to point <4>, with the <3> <2> coordinate."
      ],
      [
        "Can you tell me which point exhibits the <3> <2> coordinate in polar form?",
        "Point <4> is the one that features the <3> <2> coordinate."
      ],
      [
        "From the polar diagram, which point is noted to possess the <3> <2> coordinate?",
        "We see that point <4> holds the <3> <2> coordinate."
      ]
    ],
    "coordinate24": [
      [
        "Which point has the <3> <2> coordinate in polar form, and what is its color?",
        "The point with color <4> has the <3> <2> coordinate."
      ],
      [
        "Identify the point with the <3> <2> coordinate (polar) and provide its color.",
        "It is colored <4>, showing the <3> <2> coordinate."
      ],
      [
        "Which point in this polar coordinate system is recognized by the <3> <2> coordinate? Please specify its color.",
        "That point has the color <4>, along with the <3> <2> coordinate."
      ],
      [
        "Please tell me the color of the point that has the <3> <2> coordinate in the polar diagram.",
        "The point's color is <4>, matching the <3> <2> coordinate."
      ],
      [
        "Which point is noted for having the <3> <2> coordinate? Mention its color.",
        "We can see the point is colored <4>, holding the <3> <2> coordinate."
      ]
    ]
  }

conversation_short = {
    "coordinate1": [
      [
        "Is this figure related to the Cartesian coordinate system or the Polar coordinate system?",
        "<2>"
      ],
      [
        "Does the figure illustrate a Cartesian or a Polar coordinate system?",
        "<2>"
      ],
      [
        "Which coordinate system is depicted here: Cartesian or Polar?",
        "<2>"
      ],
      [
        "Determine whether the figure is based on a Cartesian or Polar coordinate system.",
        "<2>"
      ],
      [
        "Identify if this figure corresponds to Cartesian coordinates or Polar coordinates.",
        "<2>"
      ]
    ],
    "coordinate2": [
      [
        "What are the coordinates of point <2> in the figure? Express your answer as <2>(x, y).",
        "<2>(<3>, <4>)"
      ],
      [
        "Specify the coordinates of point <2> as <2>(x, y).",
        "<2>(<3>, <4>)"
      ],
      [
        "Identify the (x, y) coordinates of point <2>.",
        "<2>(<3>, <4>)"
      ],
      [
        "In the figure, what is the coordinate of point <2>? Use the format <2>(x, y).",
        "<2>(<3>, <4>)"
      ],
      [
        "Please give the coordinates of point <2> in the form <2>(x, y).",
        "<2>(<3>, <4>)"
      ]
    ],
    "coordinate3": [
      [
        "Which point in the figure is colored <2>, and what are its (x, y) coordinates?",
        "(<3>, <4>)"
      ],
      [
        "Identify the coordinates of the <2>-colored point in (x, y) form.",
        "(<3>, <4>)"
      ],
      [
        "What is the (x, y) location of the point with color <2>?",
        "(<3>, <4>)"
      ],
      [
        "From the diagram, what are the coordinates of the point having color <2>?",
        "(<3>, <4>)"
      ],
      [
        "Give the (x, y) position of the point whose color is <2>.",
        "(<3>, <4>)"
      ]
    ],
    "coordinate4": [
      [
        "Which point in the figure shares the same <3> coordinate as point <2>?",
        "<4>"
      ],
      [
        "Identify the label of the point that has the same <3> coordinate as <2>.",
        "<4>"
      ],
      [
        "Find the point label matching <2> in its <3> coordinate.",
        "<4>"
      ],
      [
        "What is the label of the point that aligns with <2> on the <3> axis?",
        "<4>"
      ],
      [
        "Name the point that has the same <3> coordinate as <2>.",
        "<4>"
      ]
    ],
    "coordinate5": [
      [
        "Which point has the same <3> coordinate as the point colored <2>, and what is its color?",
        "<4>"
      ],
      [
        "Identify the color of the point sharing the <3> coordinate with the <2>-colored point.",
        "<4>"
      ],
      [
        "What color belongs to the point that matches <2> in the <3> coordinate?",
        "<4>"
      ],
      [
        "Find the color of the point whose <3> coordinate equals that of the <2>-colored point.",
        "<4>"
      ],
      [
        "Which point's color corresponds to the same <3> coordinate as the point colored <2>?",
        "<4>"
      ]
    ],
    "coordinate6": [
      [
        "Which two points share the same <2> coordinate?",
        "<3>, <4>"
      ],
      [
        "Identify the pair of points with identical <2> coordinates.",
        "<3>, <4>"
      ],
      [
        "Choose the two points that match in <2> coordinate.",
        "<3>, <4>"
      ],
      [
        "Name the points that align in terms of <2> coordinate.",
        "<3>, <4>"
      ],
      [
        "Select the points whose <2> coordinates are the same.",
        "<3>, <4>"
      ]
    ],
    "coordinate7": [
      [
        "Which two points share the same <2> coordinate, and what are their colors?",
        "<3>, <4>"
      ],
      [
        "Identify the colors of the points with the same <2> coordinate.",
        "<3>, <4>"
      ],
      [
        "Name the two colors corresponding to points that match in <2> coordinate.",
        "<3>, <4>"
      ],
      [
        "Pick the point colors that have identical <2> coordinates.",
        "<3>, <4>"
      ],
      [
        "Which pair of colors indicates points sharing the same <2> coordinate?",
        "<3>, <4>"
      ]
    ],
  
    "coordinate8": [
      [
        "Which point has the <3> <2> coordinate?",
        "Point <4> has the <3> <2> coordinate."
      ],
      [
        "Identify the point that possesses the <3> <2> coordinate.",
        "Point <4>."
      ],
      [
        "In this figure, which point is recognized for having the <3> <2> coordinate?",
        "<4>"
      ],
      [
        "Where do we see the <3> <2> coordinate? Which point is it?",
        "<4>"
      ],
      [
        "Name the point with the <3> <2> coordinate.",
        "<4>"
      ]
    ],
    "coordinate9": [
      [
        "Which point has the <3> <2> coordinate, and what is its color?",
        "<4>"
      ],
      [
        "Identify the color of the point with the <3> <2> coordinate.",
        "<4>"
      ],
      [
        "Which point's color corresponds to the <3> <2> coordinate?",
        "<4>"
      ],
      [
        "State the color of the point that holds the <3> <2> coordinate.",
        "<4>"
      ],
      [
        "What is the color of the point showing the <3> <2> coordinate?",
        "<4>"
      ]
    ],
  
    "coordinate10": [
      [
        "Which quadrant does point <2> lie in?",
        "<3>"
      ],
      [
        "Identify the quadrant number for point <2>.",
        "<3>"
      ],
      [
        "What quadrant is point <2> in?",
        "<3>"
      ],
      [
        "Specify the quadrant containing point <2>.",
        "<3>"
      ],
      [
        "Where does point <2> appear on the quadrant grid?",
        "<3>"
      ]
    ],
    "coordinate11": [
      [
        "Which quadrant does the <2>-colored point occupy?",
        "<3>"
      ],
      [
        "Identify the quadrant of the point whose color is <2>.",
        "<3>"
      ],
      [
        "What quadrant is the <2>-colored point in?",
        "<3>"
      ],
      [
        "Specify the quadrant that contains the <2>-colored point.",
        "<3>"
      ],
      [
        "Determine the quadrant for the point colored <2>.",
        "<3>"
      ]
    ],
    "coordinate12": [
      [
        "What is the <3>-intercept of the function <2> based on the graph?",
        "<4>"
      ],
      [
        "Identify the <3>-intercept for <2> as shown in the figure.",
        "<4>"
      ],
      [
        "Which value is the <3>-intercept of the function <2> in the diagram?",
        "<4>"
      ],
      [
        "Give the <3>-intercept of the graphed function <2>.",
        "<4>"
      ],
      [
        "State the <3>-intercept of <2> from the provided graph.",
        "<4>"
      ]
    ],
    "coordinate13": [
      [
        "Which quadrant does shape <2> occupy?",
        "<3>"
      ],
      [
        "In what quadrant can shape <2> be found?",
        "<3>"
      ],
      [
        "What is the quadrant of shape <2>?",
        "<3>"
      ],
      [
        "Identify the quadrant containing shape <2>.",
        "<3>"
      ],
      [
        "Which quadrant does the diagram show for shape <2>?",
        "<3>"
      ]
    ],
    "coordinate14": [
      [
        "Which quadrant(s) does shape <2> pass through?",
        "<3>"
      ],
      [
        "Identify all quadrants that shape <2> intersects.",
        "<3>"
      ],
      [
        "Name any quadrant(s) that shape <2> covers.",
        "<3>"
      ],
      [
        "Which quadrant(s) does shape <2> traverse?",
        "<3>"
      ],
      [
        "List the quadrant(s) in which shape <2> is present.",
        "<3>"
      ]
    ],
    "coordinate15": [
      [
        "Out of the points <2>, which are inside shape <3>?",
        "<4>"
      ],
      [
        "Which points from <2> lie within shape <3>?",
        "<4>"
      ],
      [
        "Identify the points among <2> that are inside <3>.",
        "<4>"
      ],
      [
        "Name the points in <2> that fall within the boundary of shape <3>.",
        "<4>"
      ],
      [
        "Which points from <2> does shape <3> contain?",
        "<4>"
      ]
    ],
    "coordinate16": [
      [
        "Which points from <2> lie outside shape <3>?",
        "<5>"
      ],
      [
        "Identify the points among <2> that are not inside <3>.",
        "<5>"
      ],
      [
        "Which of the points <2> are beyond the boundary of shape <3>?",
        "<5>"
      ],
      [
        "Which points in <2> are located outside shape <3>?",
        "<5>"
      ],
      [
        "Name the points from <2> that exist outside the region of shape <3>.",
        "<5>"
      ]
    ],
    "coordinate17": [
      [
        "What are the polar coordinates of point <2>, expressed as <2>(r, theta)?",
        "<2>(<3>, <4>)"
      ],
      [
        "Which (r, theta) coordinates belong to point <2>?",
        "<2>(<3>, <4>)"
      ],
      [
        "Identify the polar position of point <2>, using the format <2>(r, theta).",
        "<2>(<3>, <4>)"
      ],
      [
        "Provide the polar coordinates of point <2> as <2>(<3>, <4>).",
        "<2>(<3>, <4>)"
      ],
      [
        "How can we express point <2> in polar form (r, theta)?",
        "<2>(<3>, <4>)"
      ]
    ],
    "coordinate18": [
      [
        "What are the polar coordinates (r, theta) of the point colored <2>?",
        "(<3>, <4>)"
      ],
      [
        "State the (r, theta) coordinates for the point with color <2>.",
        "(<3>, <4>)"
      ],
      [
        "In polar form, what is the position of the <2>-colored point?",
        "(<3>, <4>)"
      ],
      [
        "Which coordinates describe the <2>-colored point in polar notation?",
        "(<3>, <4>)"
      ],
      [
        "Identify the polar coordinates of the point whose color is <2>.",
        "(<3>, <4>)"
      ]
    ],
    "coordinate19": [
      [
        "Which point shares the same <3> coordinate as point <2> in polar form?",
        "<4>"
      ],
      [
        "Identify the label of the point matching <2> in the <3> coordinate (polar).",
        "<4>"
      ],
      [
        "What is the label of the point whose <3> coordinate matches that of point <2>?",
        "<4>"
      ],
      [
        "Find the point label that has an identical <3> coordinate to point <2>.",
        "<4>"
      ],
      [
        "Which point in polar coordinates lines up with <2> on the <3> axis?",
        "<4>"
      ]
    ],
    "coordinate20": [
      [
        "Which point has the same <3> coordinate as the <2>-colored point in polar form, and what is its color?",
        "<4>"
      ],
      [
        "Identify the color of the point that aligns with the <2>-colored point in <3> coordinate.",
        "<4>"
      ],
      [
        "What color is the point sharing the <3> coordinate with the <2>-colored point?",
        "<4>"
      ],
      [
        "Find the point's color that has the same <3> coordinate as the <2>-colored point.",
        "<4>"
      ],
      [
        "Name the color of the point matching <2> in <3> coordinate in the polar setup.",
        "<4>"
      ]
    ],
    "coordinate21": [
      [
        "Which two points in polar coordinates have the same <2> coordinate?",
        "<3>, <4>"
      ],
      [
        "Identify the pair of points that share <2> in the polar system.",
        "<3>, <4>"
      ],
      [
        "Name the two points whose <2> coordinate is identical in polar form.",
        "<3>, <4>"
      ],
      [
        "Find the pair of points that coincide in <2> coordinate (polar).",
        "<3>, <4>"
      ],
      [
        "Select the points that have the same <2> coordinate in the polar diagram.",
        "<3>, <4>"
      ]
    ],
    "coordinate22": [
      [
        "Which two points have the same <2> coordinate in polar form, and what are their colors?",
        "<3>, <4>"
      ],
      [
        "Identify the colors of the points that share <2> in polar coordinates.",
        "<3>, <4>"
      ],
      [
        "Which point colors line up in <2> coordinate in the polar system?",
        "<3>, <4>"
      ],
      [
        "Find the color pair that has an identical <2> coordinate in the diagram.",
        "<3>, <4>"
      ],
      [
        "Name the two colors that correspond to points sharing the same <2> coordinate (polar).",
        "<3>, <4>"
      ]
    ],
  
    "coordinate23": [
      [
        "Which point has the <3> <2> coordinate in polar form?",
        "Point <4> has the <3> <2> coordinate."
      ],
      [
        "Identify the point recognized by the <3> <2> coordinate (polar).",
        "<4>"
      ],
      [
        "Which point is associated with the <3> <2> coordinate in the polar system?",
        "<4>"
      ],
      [
        "Name the point that has the <3> <2> coordinate here.",
        "<4>"
      ],
      [
        "Which point in this polar diagram shows the <3> <2> coordinate?",
        "<4>"
      ]
    ],
    "coordinate24": [
      [
        "Which point has the <3> <2> coordinate in polar form, and what is its color?",
        "<4>"
      ],
      [
        "Identify the color of the point with the <3> <2> coordinate (polar).",
        "<4>"
      ],
      [
        "Which point is recognized by the <3> <2> coordinate? State its color.",
        "<4>"
      ],
      [
        "What is the color of the point that has the <3> <2> coordinate in the diagram?",
        "<4>"
      ],
      [
        "Name the color of the point showing the <3> <2> coordinate in polar form.",
        "<4>"
      ]
    ]
  }

def generate_conversation(diagram, long=False):
    conversation_list = []
    for entity in diagram.entities:
        version_key = entity[0]
        if long:
            conversation = conversation_long
        else:
            conversation = conversation_short
        one_conversation = random.choice(conversation[version_key])
        q = one_conversation[0]
        a = one_conversation[1]
        for i in range(1, len(entity[1])):
            q = q.replace(f"<{i+1}>", entity[1][i])
            a = a.replace(f"<{i+1}>", entity[1][i])
        conversation_list.append((q, a))
    return conversation_list