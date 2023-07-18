import random

names_string = input( "Give me everybody's names, separated by a comma. " )
names = names_string.split(", ")

who_pays = names[random.randint(0, len(names) - 1)]
print( f"{who_pays} is going to buy the meal today!" )


