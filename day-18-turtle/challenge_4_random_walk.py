# challenge 4 random walk
import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()
tim.shape("turtle")

angle_turn = [0, 90, 180, 270]
tim.pensize(5)
tim.speed(10)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


for _ in range(200):
    tim.pencolor(random_color())
    tim.setheading(random.choice(angle_turn))
    tim.forward(20)


tim.hideturtle()


screen = turtle.Screen()
screen.exitonclick()
