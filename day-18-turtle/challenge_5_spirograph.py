# Challenge 5 Spirograph
import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(numbers_of_circles):
    angle = 360 / numbers_of_circles
    for i in range(numbers_of_circles):
        current_heading = tim.heading()
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(current_heading + angle)


turtle.colormode(255)
tim = turtle.Turtle()
tim.shape("turtle")
tim.speed(10)

draw_spirograph(80)

tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
