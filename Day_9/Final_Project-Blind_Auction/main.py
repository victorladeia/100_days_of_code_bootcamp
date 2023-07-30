import os

bid_people = {}

name = input( "What's your name? " )
bid = int (input( "What's your bid? $" ))

bid_people[name] = bid

continue_action = input ( "Are there any other bidders? Type 'yes' or 'no'. " )

while ( continue_action == 'yes' ):
    os.system( "clear" )
    name = input( "What's your name? " )
    bid = int( input( "What's your bid? $" ) )

    bid_people[name] = bid

    continue_action = input ( "Are there any other bidders? Type 'yes' or 'no'. " )

winner = ''
winner_bid = 0

for key in bid_people:
    if bid_people[ key ] > winner_bid:
        winner_bid = bid_people[ key ]
        winner = key
os.system( "clear" )
print( f"The winner is {winner} with the bid of {winner_bid}." )