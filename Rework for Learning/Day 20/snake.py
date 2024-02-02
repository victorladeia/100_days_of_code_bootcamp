from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]


class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        snake_block = Turtle()
        snake_block.shape("square")
        snake_block.color("white")
        snake_block.penup()
        snake_block.setposition(position)
        self.snake_blocks.append(snake_block)

    def extend(self):
        """"

        """
        self.add_block(self.snake_blocks[-1].position())

    def move(self):
        """
        @return:
        Makes the snake goes forward by 20 px in heading direction

        """
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