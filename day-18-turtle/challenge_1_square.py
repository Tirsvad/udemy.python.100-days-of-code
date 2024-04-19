# challenge 1 square
import turtle

tim = turtle.Turtle()
tim.shape("turtle")

# challenge 1 square
for _ in range(4):
    tim.forward(100)
    tim.right(90)

tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
