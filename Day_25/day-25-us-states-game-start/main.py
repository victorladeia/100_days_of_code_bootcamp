import turtle

import pandas as pd

import states


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

already_guessed_states = []
missing_states = states.states_df.state.to_list()

game_is_on = True

tittle = "Guess the State"

while game_is_on:

    # Get State name from user:
    answer_state = screen.textinput(title=tittle, prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state not in already_guessed_states and states.is_state_on_list(answer_state):
        already_guessed_states.append(answer_state)
        missing_states.remove(answer_state)
        states.print_state_name_on_screen(answer_state)
        tittle = f"{len(already_guessed_states)}/50 States Correct"
    else:
        continue

missing_states = pd.DataFrame(missing_states, columns=["state"])
missing_states.to_csv("states_to_learn.csv")
