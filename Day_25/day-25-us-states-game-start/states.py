import pandas as pd
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')


states_df = pd.read_csv("50_states.csv")
states_list = states_df.state.to_list()


def is_state_on_list(guessed_state):
    return guessed_state.title() in states_df.state.tolist()


def print_state_name_on_screen(guessed_state):
    state = Turtle()
    state.penup()
    state.hideturtle()
    state_index = states_df.state.tolist().index(guessed_state)
    x_position = states_df.x[state_index]
    y_position = states_df.y[state_index]
    state.setposition(x_position, y_position)
    state.write(arg=f"{guessed_state}", font=FONT, align=ALIGNMENT)
