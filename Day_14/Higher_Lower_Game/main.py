# importing libraries and other resources:
from random import randint
from art import logo
from art import vs
from game_data import data

def print_comparison(a_item_number, b_item_number):
    """[Insert Description]"""

    a_name = data[a_item_number]["name"]
    a_description = data[a_item_number]["description"]
    a_country = data[a_item_number]["country"]

    b_name = data[b_item_number]["name"]
    b_description = data[b_item_number]["description"]
    b_country = data[b_item_number]["country"]


    print( f"Compare A: {a_name}, a {a_description}, from {a_country}." )
    print( vs )
    print( f"Against B: {b_name}, a {b_description}, from {b_country}." )

def get_higher(a_item_number, b_item_number):
    a_followers = data[a_item_number]["follower_count"]
    b_followers = data[b_item_number]["follower_count"]

    if a_followers > b_followers:
        return {
            "choice":'A',
            "item": a_item_number
        }
    elif b_followers > a_followers:
        return {
            "choice":'B',
            "item": b_item_number
        }

def is_guess_right(guess, right_answer):
    if guess == right_answer:
        return True
    else:
        return False

def get_second_item(a_item_number):
    b_item_number = randint(0, len(data) -1)
    while b_item_number == a_item_number:
        b_item_number = randint(0, len(data) -1)
    return b_item_number

def game():

    score = 0
    a_item = randint(0, len(data) -1)
    b_item = get_second_item(a_item)

    is_game_ended = False

    while not is_game_ended:
        
        print_comparison(a_item, b_item)

        user_guess = input("Who has more follower? Type 'A' or 'B': ")

        higher = get_higher(a_item, b_item)

        if is_guess_right(user_guess, higher["choice"]):
            score += 1
            a_item = higher["item"]
            b_item = get_second_item(a_item)
        else:
            print( f"Sorry, that's wrong. Final score: {score}." )
            is_game_ended = True

game()
    