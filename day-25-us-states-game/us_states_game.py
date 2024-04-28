from turtle import Turtle, Screen
import time
import pandas as pd


class UsStatesGame:

    screen: Screen
    text: Turtle
    correct_answers: int

    def __init__(self):
        self.data_us_states = pd.read_csv("50_states.csv")
        self.all_state_list = self.data_us_states["state"].to_list()
        self.screen = Screen()
        self.screen.title("U.S. states game")
        self.screen.setup(725,491)
        self.screen.tracer(0)
        self.screen.bgpic('blank_states_img.gif')
        self.text = Turtle()
        self.text.hideturtle()
        self.text.penup()
        # self.screen.exitonclick()
        self.start = time.time()
        self.correct_answers = 0

    def reset(self):
        self.start = time.time()

    def update(self):
        answer = self.screen.textinput(f"{self.correct_answers}/50 states correct","What's another state name?").title()
        # answer = answer.capitalize()
        if answer.capitalize() in self.all_state_list:
            self.all_state_list.remove(answer)
            state_data = self.data_us_states[self.data_us_states.state == answer]
            self.text.goto(
                int(state_data.x.item()),
                int(state_data.y.item())
            )
            self.text.write(answer)
            self.correct_answers += 1
            if self.correct_answers == 50:
                return False
        if answer.lower() == "exit":
            new_data = pd.DataFrame(self.all_state_list)
            new_data.to_csv("missed_state.csv")
            print(new_data)
            return False
        self.screen.update()
        return True
