import colorgram
import turtle as turtle
import random

# using colorgram package to extract colors from an image
# colors = colorgram.extract('images (9).jpeg', 40)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = turtle.Turtle()
turtle.colormode(255)

color_list = [(227, 234, 229), (205, 161, 86), (57, 88, 129), (144, 91, 42), (137, 27, 49), (220, 207, 110), (134, 175, 200), (155, 49, 83), (45, 55, 103), (170, 158, 42), (81, 18, 41), (129, 187, 143), (35, 42, 68), (189, 139, 163), (185, 93, 106), (86, 120, 178), (57, 40, 30), (88, 155, 93), (79, 152, 163), (193, 80, 73), (57, 127, 119), (161, 201, 218), (79, 72, 44), (45, 74, 77), (220, 175, 186), (221, 182, 168), (169, 206, 166), (181, 188, 212), (48, 74, 73), (125, 41, 38), (40, 57, 57), (230, 198, 25)]

tim.penup()
tim.hideturtle()
tim.setheading(222)
tim.forward(300)
tim.setheading(0)

dots_number = 100

for dot_count in range(1, dots_number + 1):
    tim.dot(13, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
