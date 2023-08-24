from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):
        x = 0
        y = 0
        for _ in range(0, 3):
            snake_block = Turtle()
            snake_block.shape("square")
            snake_block.color("white")
            snake_block.penup()
            snake_block.setposition(x, y)
            x -= 20
            self.snake_blocks.append(snake_block)

    def move(self):

        for part_num in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[part_num - 1].xcor()
            new_y = self.snake_blocks[part_num - 1].ycor()
            self.snake_blocks[part_num].goto(new_x, new_y)
        self.snake_blocks[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


