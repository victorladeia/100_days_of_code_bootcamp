from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.body = []
        self.create_snake()
        self.head = self.body[0]


    def create_snake(self):
        for position in INITIAL_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.color("white")
        segment.goto(position)
        segment.shape("square")
        self.body.append(segment)

    # TODO: snake.extend()

    def move(self):
        for body_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_num - 1].xcor()
            new_y = self.body[body_num - 1].ycor()
            self.body[body_num].goto(new_x, new_y)
        self.body[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)