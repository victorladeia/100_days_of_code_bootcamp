from turtle import Turtle
import random
from time import sleep

BALL_HEADINGS = [45, 135, 225, 315]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        random_heading = random.choice(BALL_HEADINGS)
        self.setheading(random_heading)
        #random_y = random.randint(-)
        self.setposition(x=0, y=0)

    def move(self):
        self.forward(20)

    def bounce_on_wall(self):
        bouncing_angle = 360 - self.heading()
        self.setheading(bouncing_angle)

    def bounce_on_paddle(self):
        bouncing_angle = 180 - self.heading()
        self.setheading(bouncing_angle)
