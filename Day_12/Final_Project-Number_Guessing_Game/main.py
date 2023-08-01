import random


def choose_a_random_number():
    random_number = int(round(random.random() * 100, 0))
    return random_number

# Greetings:
print( "Welcome to the Number Guessing Game!" )
print( "I'm thinking of a number between 1 and 100." ) 
dificulty = input( "Choose a dificult. Type 'easy' or 'hard': ")

if dificulty == 'easy':
    attempts = 10
else:
    attempts = 5

answer = choose_a_random_number()

has_guessed = False

while attempts > 0 and not has_guessed:
    print( f"You have {attempts} attempts remaining to guess the number." )
    guess = int( input( "Make a guess: " ) )
    if guess == answer:
        has_guessed = True
        print( f"You got it! The answer was {answer}." )
    elif guess < answer:
        attempts -= 1
        print( "Too low." )
    elif guess > answer:
        attempts -= 1
        print( "Too high." )
    
    if attempts > 0 and not has_guessed:
        print( "Guess again." )
    elif not has_guessed:
        print( f"You lost. The answer was {answer}" )
