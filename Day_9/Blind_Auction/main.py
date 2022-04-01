import os

people = {}

key = "yes"
while(key != "no"):
    name = input( "Name: " )  
    bid = int(input( "Bid: " ))

    key = input( "Add more bid? (yes or no:" )
    people[name] = bid
    
    os.system("clear")

highiest_bid = 0
winner = ""

for pearson in people:
    if ( people[pearson] > highiest_bid ):
        highiest_bid = people[pearson]
        winner = pearson

print( f"The winner is {winner} with the bid of {highiest_bid}" )




