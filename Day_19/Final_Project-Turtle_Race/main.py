from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = {}
y_coord = -100
for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(x=-230, y=y_coord)
    y_coord += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtles[turtle].xcor() > 230:
            is_race_on = False
            winning_color = turtles[turtle].pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtles[turtle].forward(rand_distance)

screen.exitonclick()
