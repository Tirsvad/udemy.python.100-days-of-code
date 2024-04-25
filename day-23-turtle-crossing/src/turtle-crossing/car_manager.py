from turtle import Turtle, Vec2D
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.start_position()

    def start_position(self):
        self.goto(300, randint(-250, 250))


class CarManager:

    cars: list[Car]
    car_speed: int

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Car()
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() == -300:
                car.hideturtle()
                self.cars.remove(car)
            else:
                car.backward(self.car_speed)

    def if_car_collide(self, player_position: Vec2D):
        for car in self.cars:
            ycor = car.ycor()
            if -20 < player_position[1] - ycor < 20:
                # print(f"p {player_position[1]} c {ycor}")
                if -30 < player_position[0] - car.xcor() < 30:
                    return True
        return False

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
