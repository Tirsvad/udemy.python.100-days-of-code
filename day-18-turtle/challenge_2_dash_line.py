# challenge 2 dash line
import turtle

tim = turtle.Turtle()
tim.shape("turtle")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
