from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
import random

# TODO: Keep Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_player1 = Paddle(y_cor=0, x_cor=-350)
paddle_player2 = Paddle(y_cor=0, x_cor=350)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_player1.up_player1, "w")
screen.onkey(paddle_player1.down_player1, "s")
screen.onkey(paddle_player2.up_player2, "Up")
screen.onkey(paddle_player2.down_player2, "Down")

is_game_on = True

while is_game_on:
    screen.update()
    ball.move()
    sleep(0.1)

    # Detecting Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_on_wall()

    # Detecting Collision with paddles:
    if (ball.distance(paddle_player1) < 45 and ball.xcor() < -345) or (
            ball.distance(paddle_player2) < 45 and ball.xcor() > 345):
        ball.bounce_on_paddle()

    # Detect player 2 misses:
    if ball.xcor() > 380:
        ball.setposition(0, 0)
        ball.setheading(random.choice([225, 315]))
        scoreboard.player1_point()

    # Detect player 1 misses:
    if ball.xcor() < -380:
        ball.setposition(0, 0)
        ball.setheading(random.choice([45, 135]))
        scoreboard.player2_point()

screen.exitonclick()
