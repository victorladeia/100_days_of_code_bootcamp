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
    pepperoni = 2
elif size == 'M':
    bill += 20
    pepperoni = 3
else:
    bill += 25
    pepperoni = 3

if add_pepperoni == 'Y':
    bill += pepperoni

if extra_cheese == 'Y':
    bill += 1

print( f"Your final bill is: {bill}" )