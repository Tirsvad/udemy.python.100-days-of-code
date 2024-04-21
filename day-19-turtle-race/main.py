from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "orange", "purple", "yellow"]
distance_between_turtle = 50
tim = {}
screen = Screen()

# windows size depends on how many is going to race. 6 turtle => high of 400
screen.setup(width=500, height=(len(colors) + 2) * distance_between_turtle)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
# setting the first turtle start position depending on how many is going to race
x = -(screen.window_width() - (screen.window_width() / 2)) + 10
y = -(screen.window_height() - (screen.window_height() / 2)) + screen.window_height() / (len(colors) - 1)

# Start position
for color in colors:
    tim[color] = Turtle(shape="turtle")
    tim[color].color(color)
    tim[color].penup()
    tim[color].goto(x, y)

    y += distance_between_turtle

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")

# Race
finish = False
while not finish:
    # print(tim)
    color = random.choice(colors)
    tim[color].forward(1)
    if tim[color].xcor() == screen.window_width() / 2 - 25:
        finish = True
        print(f"The {color} turtle wins")
        if user_bet.lower() == color:
            print("You win")
        else:
            print("You loose. Better luck next time!")


screen.exitonclick()
