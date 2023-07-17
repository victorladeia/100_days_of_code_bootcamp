#Greetings:
print( "Welcome to Python Pizza Deliveries!" )

#Get pizza size:
size = input( "What size pizza do you want? S, M ou L? " )

# Get if one wants pepperoni:
add_pepperoni = input( "Do you want pepperoni? Y or N " )

# Get if one wants extra cheese:
extra_cheese = input( "Do you want extra cheese? " )

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print( f"Your final bill is: ${bill}." )
