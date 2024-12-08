# Name: Haseeb Ali Khan
 # Student Number: 764066
 #Revision Date: December 7th 2024
 # Teacher: Mr. King
 # Class: ICS3U
# Imports turtle
import turtle
# Sets turtle background color
turtle.bgcolor("gray40")
# Turns off updates to speed up plotting
turtle.tracer(0, 0)
# Sets turtle to t variable
t = turtle.Turtle()
# Hides the plotter sprite
t.hideturtle()

"""
Modifies a string to remove unwanted characters (" and ,)
line (str): The input string to modify
Returns: Modified string
"""
def modify(line):
    # Initialize modified string
    modified_str = ""
    # Characters to remove
    bad_chars = ['"', ',']
    # Strip spaces and iterate through characters
    line = line.strip()
    for char in line:
        if char not in bad_chars:
            modified_str += char
    return modified_str

"""
Plots a point on the canvas at the specified coordinates with a given color
T (turtle): The turtle object
x (int): X coordinate
y (int): Y coordinate
d (int): Dot size
color (str): Color of the dot
"""
def plot_point(T, x, y, d, color):
    T.penup()
    T.goto(x, y)
    T.pendown()
    T.dot(d, color)
    T.penup()

"""
Draws the image on the canvas based on image data
img (list): Image data with color values
px_size (int): Size of each dot
rows (int): Number of rows
cols (int): Number of columns
x_flip (int): Flip factor for X-axis
y_flip (int): Flip factor for Y-axis
"""
def draw_image(img, px_size, rows, cols, x_flip, y_flip):
    x_start = -cols // 2
    y_start = -rows // 2
    r_idx = 0  # Row index
    for row in img:
        y_pos = (y_start + r_idx) * px_size * y_flip
        c_idx = 0  # Column index
        for color in row:
            x_pos = (x_start + c_idx) * px_size * x_flip
            plot_point(t, x_pos, y_pos, px_size, color)
            c_idx += 1
        r_idx += 1

"""
Reads image data from the file and maps colors
fh (file): Opened file object
rows (int): Number of rows
color_defs (list): Mapped symbols to colors
Returns: List of image data
"""
def get_image_data(fh, rows, color_defs):
    image_data = []
    for _ in range(rows):
        row = fh.readline()
        row = modify(row)
        row_colors = []
        for symbol in row:
            for color_map in color_defs:
                if symbol == color_map[0]:
                    row_colors.append(color_map[1])
                    break
        image_data.append(row_colors)
    return image_data

"""
Reads color definitions from the file
fh (file): Opened file object
num_colors (int): Number of colors to read
Returns: List of symbol-to-color mappings
"""
def get_color_data(fh, num_colors):
    color_defs = []
    for _ in range(num_colors):
        color_line = fh.readline()
        color_line = modify(color_line)
        symbol, _, color = color_line.split()
        if symbol == '~':
            symbol = ' '
        color_defs.append([symbol, color])
    return color_defs

# Initialize filename and rotate variables
filename = ""
rotate = False

# Prompt user for file selection
valid = False
while not valid:
    user_input = input("Choose an option to draw: \n A: rocky_bullwinkle_mod.xpm \n B: smiley_emoji_mod.xpm \n C: Enter a file name \n")
    if user_input.lower() == 'a':
        filename = "rocky_bullwinkle_mod.xpm"
        valid = True
    elif user_input.lower() == 'b':
        filename = "smiley_emoji_mod.xpm"
        valid = True
    elif user_input.lower() == 'c':
        filename = input("Enter the file name: ")
        valid = True

# Attempt to open the file
fh = None
try:
    fh = open(filename, "r")
except FileNotFoundError:
    print("File not found.")
    exit()

# Prompt user for rotation preference
valid = False
while not valid:
    user_input = input("Would you like to rotate the image (Y/N): ")
    if user_input.lower() == 'y':
        rotate = True
        valid = True
    elif user_input.lower() == 'n':
        valid = True

# Read color and image data
color_data = fh.readline()
color_data = modify(color_data)
if len(color_data.split()) == 4:
    cols, rows, num_colors, _ = color_data.split()
else:
    cols, rows, num_colors = color_data.split()

cols, rows, num_colors = int(cols), int(rows), int(num_colors)

color_defs = get_color_data(fh, num_colors)
image_data = get_image_data(fh, rows, color_defs)

fh.close()

# Display image properties
print("\nDimensions: %d x %d" % (rows, cols))
print("Number of colors:", num_colors)
print("Colors:", color_defs)

# Draw the image
if rotate:
    draw_image(image_data, 3, rows, cols, -1, -1)
else:
    draw_image(image_data, 3, rows, cols, 1, 1)

turtle.update()

