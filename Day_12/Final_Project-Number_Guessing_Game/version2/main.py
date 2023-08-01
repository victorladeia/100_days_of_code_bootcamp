from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess( guess, answer, attempts ):
    """Prints differents statements based on comparison between guess and answer."""
    if guess > answer:
        print( "Too high." )
        return attempts - 1
    elif guess < answer:
        print( "Too low." )
        return attempts - 1
    else:
        print( f"You got it! The answer was {answer}." )

def set_difficulty():
    """Sets number of attemps based on user choice."""
    level = input( "Choose a difficulty. Type 'easy' or 'hard': " )
    while level not in ['easy', 'hard']:
        level = input( "Choose a difficulty. Type 'easy' or 'hard': " )
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    # Greetings:
    print( "Welcome to the Number Guessing Game!" )
    print( "I'm thinking of a number between 1 and 100." )
    
    attempts = set_difficulty()

    #Choosing a random number between 1 and 100:
    answer = randint(1, 100)
    #print( f"Pssst, the correct answer is {answer}." )

    #Repeating the guessing functionality if they get it wrong.

    guess = 0

    while guess != answer:
        
        print( f"You have {attempts} attempts remaining to guess the number.")
        # Let the user guess a number:
        guess = int( input( "Make a guess: " ) )

        attempts = check_guess( guess=guess, answer=answer, attempts=attempts )
        if attempts == 0:
            print( "You've run out of guesses, you lose." )
            return
        elif guess != answer:
            print( "Guess again." )

game()