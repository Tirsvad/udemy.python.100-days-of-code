# # ##This code will not work in repl.it as there is no access to the colorgram package here.###
# # Download an image from internet search for hirst. Save as image.jpg in root off this project
# # #We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, b, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
#
# print(len(rgb_colors))
import turtle
import random

rgb_colors = [(140, 207, 207), (25, 48, 48), (26, 159, 159), (237, 235, 235), (209, 111, 111), (144, 63, 63),
              (230, 93, 93), (4, 197, 197), (218, 84, 84), (229, 43, 43), (195, 169, 169), (54, 114, 114),
              (28, 116, 116), (172, 95, 95), (108, 90, 90), (110, 87, 87), (193, 46, 46), (240, 2, 2), (1, 119, 119),
              (19, 21, 21), (50, 109, 109), (172, 172, 172), (118, 34, 34), (221, 188, 188), (227, 166, 166),
              (153, 220, 220), (184, 210, 210)]

circle_size = 20
space = 50
number_circle_x = 10
number_circle_y = 10


def draw_dot(color: tuple[float, float, float], size: int):
    timmy.pendown()
    timmy.color(color)
    timmy.dot(size)
    timmy.penup()


def hirst_graphic():

    y = space
    timmy.penup()

    for _ in range(number_circle_y):
        timmy.sety(y)
        x = space
        y += circle_size + space
        for _ in range(number_circle_x):
            timmy.setx(x)
            color_random = random.choice(rgb_colors)
            draw_dot(color_random, circle_size)
            x += circle_size + space



# Setup screen size and turtle
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(10)
timmy.hideturtle()
screen = turtle.Screen()
screen_width = (circle_size + space) * number_circle_x + space
screen_height = (circle_size + space) * number_circle_y + space
screen.screensize(screen_width, screen_height)
screen.setworldcoordinates(0,0, screen_width, screen_height)
timmy.pencolor()
timmy.color(rgb_colors[0])

hirst_graphic()

screen.exitonclick()
