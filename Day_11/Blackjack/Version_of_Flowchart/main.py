import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


def deal_card(user):
    user.append(random.choice(cards))

deal_card(user_cards)
deal_card(user_cards)

deal_card(computer_cards)
deal_card(computer_cards)

flag1 = 'y'
while ( flag1 = 'y' )
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)
    
    if ( user_sum == 21 or computer_sum == 21 ):
        if ( user_sum == 21 ):
            print("Congratulations! You won!")
        elif ( computer_sum == 21 ):
            print("The computer won...")

