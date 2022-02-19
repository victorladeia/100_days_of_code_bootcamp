from random import choice


word_list = ["aardvark", "baboon", "camel"]

word = choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in word:
    if ( letter == guess ):
        print( "Right" )
    else:
        print( "Wrong" )