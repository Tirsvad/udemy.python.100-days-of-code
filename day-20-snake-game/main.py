from turtle import Screen
import time
from snake import Snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
snake = Snake()

screen.onkey(fun=snake.set_heading_up, key="Up")
screen.onkey(fun=snake.set_heading_down, key="Down")
screen.onkey(fun=snake.set_heading_left, key="Left")
screen.onkey(fun=snake.set_heading_right, key="Right")

game_is_on = True
while game_is_on:
    game_is_on = snake.move()
    screen.update()
    time.sleep(.1)
