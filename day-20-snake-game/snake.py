from turtle import Turtle
SNAKE_MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.starting_length = 3
        self.parts: list[Turtle] = []
        self.heading: int = 0

        self.create_body()
        self.head = self.parts[0]

    def create_body(self):
        y = 0
        x = 0
        for snake_part in range(self.starting_length):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(y=y, x=x)
            self.parts.append(new_turtle)
            x -= 20

    def move(self) -> bool:
        for snake_part in range(len(self.parts) - 1, 0, -1):
            new_pos_x = self.parts[snake_part -1].xcor()
            new_pos_y = self.parts[snake_part -1].ycor()
            self.parts[snake_part].goto(x=new_pos_x, y=new_pos_y)
        self.head.forward(SNAKE_MOVE_DISTANCE)

        # # alternative way where we only move back to new position
        # self.parts.insert(0, self.parts.pop(len(self.parts) - 1))
        # if self.heading == 0:
        #     previous_position_x += SNAKE_MOVE_DISTANCE
        # elif self.heading == 90:
        #     previous_position_y += SNAKE_MOVE_DISTANCE
        # elif self.heading == 180:
        #     previous_position_x -= SNAKE_MOVE_DISTANCE
        # elif self.heading == 270:
        #     previous_position_y -= SNAKE_MOVE_DISTANCE
        # self.parts[0].goto(x=previous_position_x, y=previous_position_y)

        return True

    def set_heading_up(self):
        if int(self.head.heading()) != DOWN:
            self.head.setheading(UP)

    def set_heading_down(self):
        if int(self.head.heading()) != UP:
            self.head.setheading(DOWN)

    def set_heading_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def set_heading_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
