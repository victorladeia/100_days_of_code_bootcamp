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
user_score = sum(user_cards)

flag1 = 'y'
while ( flag1 == 'y' ):
    deal_card(user_cards)
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    
    if ( user_score == 21 or computer_score == 21 ):
        if ( user_score == 21 ):
            print("Congratulations! You won!")
        elif ( computer_score == 21 ):
            print("The computer won...")
    else:
        if ( user_score > 21 ):
            if 11 in user_cards:
                if ( (user_score - 10) > 21 ):
                    print("The computer won...")
            else:
                print("The computer won...")
    flag1 = input("Do you want another card? 'y' [yes] 'n' [no]: ")
