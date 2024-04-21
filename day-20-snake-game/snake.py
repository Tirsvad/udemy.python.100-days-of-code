from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("green")

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self) -> bool:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

        for segment in self.segments[1:]:
            if self.head.position() == segment.position():
                print("Snake hit it's own tail")
                return False
        if not -280 < self.head.xcor() < 280 or not -280 < self.head.ycor() < 280:
            print("Snake hit the wall")
            return False
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
