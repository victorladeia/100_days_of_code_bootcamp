from time import sleep
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

accepted_entries = ['espresso', 'latte', 'cappuccino', 'off', 'report']

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def check_resources(product):
    ingredients = MENU[product]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] >= ingredients[ingredient]:
            continue
        else:
            return [False, ingredient]
    return [True, '']


def print_machine_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def get_coins():
    total = 0
    for coin in coins:
        total += coins[coin] * int(input(f"How many {coin}?: "))
    return total


money = 0
keep_on = True

while keep_on:

    user_entry = input(" What would you like? (espresso/latte/cappuccino): ")
    while user_entry not in accepted_entries:
        print("Entry not valid! Try again, please.")
        user_entry = input(" What would you like? (espresso/latte/cappuccino): ")

    if user_entry == 'off':
        print("Turning Coffee Machine Off...")
        keep_on = False
    elif user_entry == 'report':
        print_machine_resources()
    else:
        results_from_check_resources = check_resources(user_entry)
        is_resources_enough = results_from_check_resources[0]
        missing_resource = results_from_check_resources[1]
        if is_resources_enough:
            print("Please insert coins.")
            inserted_value: float = get_coins()
            change = inserted_value - MENU[user_entry]["cost"]
            if change >= 0:
                print(f"Here is ${round(change, 2)} in change")
                print(f"Here is your {user_entry}. Enjoy!")
                money += MENU[user_entry]["cost"]
                for item in MENU[user_entry]["ingredients"]:
                    resources[item] -= MENU[user_entry]["ingredients"][item]
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough {missing_resource}")
