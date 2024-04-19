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

COINS = {
    "quarters": .25,
    "dimes": .1,
    "nickles": .05,
    "pennies": .01,
}

money = 0


def rapport_status():
    print(f"water {resources['water']} ml")
    print(f"coffee {resources['coffee']} gr")
    print(f"milk {resources['milk']} ml")
    print(f"money $ {money}")


def resources_check(check_resource_use: dict) -> bool:
    status = True
    for ingredient in check_resource_use:
        if check_resource_use[ingredient] > resources[ingredient]:
            print(f"there is not enough {ingredient}")
            status = False
    return status


def coin_process(price: float) -> bool:
    inserted_coins = {}
    paid = 0
    global money
    print("Please insert coins")
    for coin in COINS:
        inserted_coins[coin] = int(input(f"How many {coin}? "))
        paid += inserted_coins[coin] * COINS[coin]
    print(inserted_coins)
    print(paid)
    if paid < price:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        money += price
        print(f"Here is ${round(paid - price, 2)} dollars in change.")
        return True


def make_coffee(flavour: str):
    global resources
    for ingredient in MENU[flavour]['ingredients']:
        resources[ingredient] = resources[ingredient] - MENU[flavour]['ingredients'][ingredient]
    print("Here is your coffee. Enjoy!")

machine_on = True
while machine_on:
    # clear screen
    print("\033[2J\033[H", end="", flush=True)
    choice = input("What would you like? (espresso / latte / cappuccino): ")
    # # My other solution. Auto change if MENU is changed
    # # Depend on screen lines available else make it as one line as above
    # print("menu:")
    # for key in MENU:
    #     print(f"    {key}")
    # order = input("What would you like? ")

    if choice in MENU:
        if resources_check(check_resource_use=MENU[choice]['ingredients']):
            if coin_process(price=MENU[choice]['cost']):
                make_coffee(choice)
    elif choice == "rapport":
        rapport_status()
    elif choice == "off":
        machine_on = False
    else:
        print("I don't understand your choice!")
