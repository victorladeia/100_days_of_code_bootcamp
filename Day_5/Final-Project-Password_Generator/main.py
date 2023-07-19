import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_length = nr_letters + nr_numbers + nr_symbols
password_idex = list( range( 0, password_length ) )
password = list(password_idex)

for symbol_unit in range( 1, nr_symbols + 1 ):
    symbol_index = random.choice( password_idex )
    password[ symbol_index ] = random.choice( symbols )
    password_idex.remove( symbol_index )

for letter_unit in range( 1, nr_letters + 1 ):
    letter_index = random.choice( password_idex )
    password[ letter_index ] = random.choice( letters )
    password_idex.remove( letter_index )

for number_unit in range( 1, nr_numbers + 1 ):
    number_index = random.choice( password_idex )
    password[ number_index ] = random.choice( numbers )
    password_idex.remove( number_index )

print(''.join( password))