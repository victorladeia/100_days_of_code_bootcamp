#Greetings:
print( "Welcome to the Love Calculator!" )

# Getting name 1:
name1 = input( "What is your name? " )

# Getting name 2:
name2 = input( "What is their name? " )

name = ( name1 + name2 ).lower()

# Calculating True Digit:
true_digit = name.count( "t" ) + name.count( "r" ) + name.count( "u" ) + name.count( "e" )

# Calculating Love Digit:
love_digit = name.count( "l" ) + name.count( "o" ) + name.count( "v" ) + name.count( "e" )

# Calculating Love Score:
love_score = int( str( true_digit ) + str( love_digit ) )

if ( love_score  > 40 ) and ( love_score< 50 ):
    print( f"Your score is {love_score}, you are alright together." )
elif ( love_score < 10 ) or ( love_score > 90 ):
    print( f"Your score is {love_score}, you go together like coke and mentos." )
else:
    print( f"Your score is {love_score}" )