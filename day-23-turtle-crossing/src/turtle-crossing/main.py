import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

PLAYER_MOVE_UP_KEY = "Up"
game_speed = .1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(fun=player.move_up, key=PLAYER_MOVE_UP_KEY)

game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    if randint(1, 6) == 1:
        if len(car_manager.cars) < 30:
            car_manager.add_car()
    car_manager.move_cars()
    if player.ycor() >= 290:
        player.reset_pos()
        car_manager.level_up()
        scoreboard.increase_score()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
    scoreboard.update_scoreboard()

screen.exitonclick()
