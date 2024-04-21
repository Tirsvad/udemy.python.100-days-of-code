from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(fun=snake.set_heading_up, key="Up")
screen.onkey(fun=snake.set_heading_down, key="Down")
screen.onkey(fun=snake.set_heading_left, key="Left")
screen.onkey(fun=snake.set_heading_right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    game_is_on = snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

scoreboard.game_over()
screen.exitonclick()
