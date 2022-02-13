import random
import game_hands

person_choice = int( input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n") )

computer_choice = random.randint(0, 2)

if (person_choice >= 3 or person_choice < 0):
    print("Invalid Number. You lost.")
else:
    if ( person_choice == 0 ):
        print( game_hands.rock )
    elif ( person_choice == 1 ):
        print( game_hands.paper )
    elif ( person_choice == 2 ):
        print( game_hands.scissors )

    print( "Computer chose: " )

    if ( computer_choice == 0 ):
        print( game_hands.rock )
    elif ( computer_choice == 1 ):
        print( game_hands.paper )
    elif ( computer_choice == 2 ):
        print( game_hands.scissors )

    if ( ( person_choice == 0 and computer_choice == 2 ) or (person_choice == 1 and computer_choice == 0) or (person_choice == 2 and computer_choice == 1)):
        print("You win!")
    elif ( ( computer_choice == 0 and person_choice == 2 ) or (computer_choice == 1 and person_choice == 0) or (computer_choice == 2 and person_choice == 1)):
        print("You lose!")
    else:
        print("It's a Tie!")