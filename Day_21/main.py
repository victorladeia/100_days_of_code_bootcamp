from turtle import Turtle, Screen
from snake import Snake
from time import sleep
from food import Food



screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

is_game_on = True

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while is_game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detecting Collision with the food:

    if snake.head.distance(food) < 15:
        food.refresh()
        # TODO: snake.extend()

# TODO: Create a Scoreboard

# TODO: Detect Collision with Wall

# TODO: Detect Collision with Tail

screen.exitonclick()
