from turtle import Turtle, Screen
from time import sleep
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

body_parts = []
y = 0
x = 0

snake = Snake()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    sleep(0.1)

screen.exitonclick()
