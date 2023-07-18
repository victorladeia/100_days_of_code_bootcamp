import game_hands
import random


hand = [game_hands.rock, game_hands.paper, game_hands.scissors]

result = [["tied","lose","win"],["win","tied","lose"],["lose","win","tied"]]

player_choice = int(input( "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n" ))

computer_choice = random.randint(0, 2)

print(hand[player_choice])
print(hand[computer_choice])

if result[player_choice][computer_choice] == "win":
    print( "You win! 😃" )
elif result[player_choice][computer_choice] == "lose":
    print( "You lose! 😕" )
else:
    print( "It's a tied!" )