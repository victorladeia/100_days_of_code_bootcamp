import random
from stages import stages

end_of_game = False
word_list = [ "ardvark", "baboon", "camel" ]

chosen_word = random.choice( word_list )
word_lenght = len( chosen_word )

lives = 6

display = []
for position in chosen_word:
    display += "_"

while lives == 0 or "_" in display:
    guess = input( "Guess a letter: " ).lower()

    if guess in chosen_word:
        for position in range( word_lenght ):
            if chosen_word[ position ] == guess:
                display[ position ] = guess
        print( display )
        print( stages[ lives ])
    else:
        lives -= 1
        print( display )
        print( stages[ lives ] )