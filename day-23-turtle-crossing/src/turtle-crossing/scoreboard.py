from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    ALIGNMENT = "left"
    score: int

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 260)

    def increase_score(self):
        self.score += 1

    def update_scoreboard(self):
        """
        Visualize the scoreboard

        :return:
        """
        self.clear()
        self.write(arg=f"Level {self.score}", align=self.ALIGNMENT, font=FONT)
