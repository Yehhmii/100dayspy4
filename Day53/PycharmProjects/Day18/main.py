# from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
# tim.color("red")


# tim.forward(100)
# tim.right(90)

# 1. having our turtle draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# 2. drawing a dashes line with turtle
# for _ in range(15):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)

# 3. drawing  multiple shapes with the turtle with random colors

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(n)

# 4. drawing a random walk
# directions = [0, 90, 180, 270]
# we can create random colors also using the rgb format, but first we have to change the color mode in the class
# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# for _ in range(100):
#     tim.width(5)
#     tim.forward(30)
#     tim.speed("fastest")
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())

# 5. drawing a spirograph
t.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()
