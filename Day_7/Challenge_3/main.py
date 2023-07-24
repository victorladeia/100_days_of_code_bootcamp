
import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice( word_list )

word_lenght = len( chosen_word )

empty_word = []

for letter in chosen_word:
    empty_word.append( "_" )

while ( "_" in empty_word ):
    guess = input("Guess a letter: ").lower()

    for position in range( word_lenght ):
        if chosen_word[ position ] == guess:
            empty_word[ position ] = guess
    print( empty_word )

print( "You won!" )

