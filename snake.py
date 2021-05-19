from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

STARTING_POSITION = [(0, 0), (-20, -20), (-40, -40)]
SPEED = 20


class Snake:

    # Body of the snake, creating the parts...
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # making the last part of the snake go to the next part and move it from there.
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.segments[0].forward(SPEED)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
