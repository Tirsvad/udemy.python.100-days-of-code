# challenge 3 triangle, square, pentagon, hexagon, heptagon, octagon, nonagon,decagon
import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_sides_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shapes(shape_sides_n)


tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
