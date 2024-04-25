from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(to_angle=90)
        self.reset_pos()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.sety(new_y)

    def reset_pos(self):
        self.goto(STARTING_POSITION)
