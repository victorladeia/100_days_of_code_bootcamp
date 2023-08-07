# from turtle import (
#     Turtle,
#     Screen
# )
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable(["Pokemon Name", "Type"])
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
print(table.align)
table.align = "l"
print(table.align)

print(table)
