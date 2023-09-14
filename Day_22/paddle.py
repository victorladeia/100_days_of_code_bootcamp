from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.resizemode("user")
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto((x_cor, y_cor))

    def up_player1(self):
        self.forward(20)

    def down_player1(self):
        self.forward(-20)

    def up_player2(self):
        self.forward(20)

    def down_player2(self):
        self.forward(-20)