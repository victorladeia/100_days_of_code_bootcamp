import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_result( player_hand, computer_hand ):
    user_score = 0
    computer_score = 0

    for card in player_hand:
        user_score += card
    
    for card in computer_hand:
        computer_score += card

    if user_score == 21 and computer_score < 21:
        return False
    elif computer_score == 21 and user_score < 21:
        return False
    elif user_score < 21 and computer_score < 21:
        return True
    elif user_score > 21:
        return False

    play_again()



def end_game( player_hand, computer_hand ):
    user_score = 0
    computer_score = 0

    for card in player_hand:
        user_score += card
    
    for card in computer_hand:
        computer_score += card

    print( f"Your final hand: {player_hand}\nComputer's final hand: {computer_hand}")

    if user_score <= 21 and user_score > computer_score:
        print("You win!")
    elif computer_score <=21 and computer_score > user_score:
        print( "You lost!" )
        return False
    elif computer_score ==  user_score:
        print( "It's a Draw!" )
        return False
    elif user_score > 21:
        print("You lost.")
        return False

def play_again():
    user_choice = input( "Do you want to play a game of Blackjack? 'y' or 'n': ")
    if user_choice == 'y':
        blackjack()
    else:
        return
    
def blackjack():
    os.system("clear")
    print(logo)

    player_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))

    computer_cards = []
    computer_cards.append( random.choice( cards ) )
    computer_cards.append( random.choice( cards ) )

    can_game_continue = True

    while can_game_continue:
        print ( f"Your cards: { player_cards }" )
        print ( f"Computer's first card: { computer_cards[ 0 ] }" )
    
        can_game_continue = check_result(player_cards, computer_cards)
    
        if can_game_continue:
            if input( "Type 'y' to get another card, type 'n' to pass: " ) == 'y':
                player_cards.append(random.choice(cards))
            else:
                end_game(player_cards, computer_cards)
                can_game_continue = False
        else:
            end_game(player_cards, computer_cards)
    play_again()
blackjack()