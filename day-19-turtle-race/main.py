from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "orange", "purple", "yellow"]
distance_between_turtle = 50
tim = {}
screen = Screen()

# windows size depends on how many is going to race. 6 turtle => high of 400
screen.setup(width=500, height=(len(colors) + 2) * distance_between_turtle)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")


def start_position():
    tim.clear()
    screen.clear()
    # setting the first turtle start position depending on how many is going to race
    x = -(screen.window_width() - (screen.window_width() / 2)) + 10
    y = -(screen.window_height() - (screen.window_height() / 2)) + screen.window_height() / (len(colors) - 1)
    for color in colors:
        tim[color] = Turtle(shape="turtle")
        tim[color].clear()
        tim[color].color(color)
        tim[color].penup()
        tim[color].goto(x, y)
        y += distance_between_turtle


def race():
    game_is_on = True
    while game_is_on:
        start_position()
        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")
        race_is_on = True
        while race_is_on:
            color = random.choice(colors)
            tim[color].forward(1)
            if tim[color].xcor() == screen.window_width() / 2 - 25:
                race_is_on = False
                print(f"The {color} turtle wins")
                if user_bet.lower() == color:
                    print("You win")
                else:
                    print("You loose. Better luck next time!")
        choice = screen.textinput(title="New game", prompt="Do you wish continue gaming: ")
        if choice != "y":
            game_is_on = False


race()
