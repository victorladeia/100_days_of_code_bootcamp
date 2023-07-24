import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice( word_list )

empty_word = []

for letter in chosen_word:
    empty_word.append( "_" )

print( empty_word )

guess = input( "Guess a letter: " ).lower()

for letter_index in range( len( chosen_word) ):
    if chosen_word[ letter_index ] == guess:
        empty_word[ letter_index ] = guess


print( empty_word )