import random
from stages import stages
from words import word_list
from logo import logo
import os

LIVES = 6
ENDGAME = 0

chosen_word = random.choice( word_list )
chosen_word_lenght = len( chosen_word )

display = []
for position in range( chosen_word_lenght ):
    display += "_"

print( logo )

guessed_letter = []

while LIVES != ENDGAME and '_' in display:
    #print( chosen_word  )
    print( ''.join( display ) )
    print( stages[ LIVES ] )
    guess = input( "Guess a letter: ").lower()

    os.system( 'clear' )
    if guess not in guessed_letter:
        guessed_letter.append( guess )
        if guess in chosen_word:
            for position in range( chosen_word_lenght ):
                if chosen_word [ position ] == guess:
                    display[ position ] = guess
        else:
            LIVES -= 1
            print( ''.join( display ) )
            print( stages[ LIVES ] )
    else:
        print( "You have already guessed this letter. Guess another one." )

if LIVES == ENDGAME:
    print( "You lose." )
    print( f"The word was {chosen_word}.")
else:
    print( "You win!" )
