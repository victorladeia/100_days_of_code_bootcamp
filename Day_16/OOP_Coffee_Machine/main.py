from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

accepted_entries = ["latte", "espresso", "cappuccino", "off", "report"]

coffee_machine_menu = Menu()
coffee_machine_money = MoneyMachine()
coffee_machine_coffee_maker = CoffeeMaker()

keep_on: bool = True

while keep_on:
    user_entry = input(f" What would you like? ({coffee_machine_menu.get_items()}): ")
    while user_entry not in accepted_entries:
        print("Entry not valid! Try again, please.")
        user_entry = input(f" What would you like? ({coffee_machine_menu.get_items()}): ")

    if user_entry == 'off':
        print("Turning Coffee Machine Off...")
        keep_on = False
    elif user_entry == 'report':
        coffee_machine_coffee_maker.report()
        coffee_machine_money.report()
    else:
        item = coffee_machine_menu.find_drink(user_entry)
        if coffee_machine_coffee_maker.is_resource_sufficient(item) and coffee_machine_money.make_payment(item.cost):
            coffee_machine_coffee_maker.make_coffee(item)
