from turtle import Turtle, Screen


def move_forward():
    """Moves the turtle 10 units forward"""

    tim.forward(10)


def move_backward():
    """Moves the turtle 10 units backward."""

    tim.backward(10)


def spin_left():
    """Turn the turtle left - Counter-Clockwise"""

    tim.left(15)


def spin_right():
    """Turns the turtle right - Clockwise."""

    tim.right(15)


def reset():
    """Resets the screen and put the turtle on Home."""
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


tim = Turtle()

screen = Screen()
screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=spin_left)
screen.onkey(key="d", fun=spin_right)
screen.onkey(key="c", fun=reset)

screen.exitonclick()
