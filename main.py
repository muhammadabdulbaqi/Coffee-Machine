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


def print_resources(list):
    print(f"Water: {list['water']}ml\nMilk: {list['milk']}ml\nCoffee: {list['coffee']}g\nMoney: ${list['money']}")

def resource_sufficient(resources, menu, item):
    requirements = menu[item]['ingredients']
    for ingredient, required_amount in requirements.items():
        if resources.get(ingredient, 0) < required_amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    # print("All ingredients are sufficient.")
    return True


def getcoins():
    print("Please enter coins.")
    num_quarters = int(input(f"How many quarters: "))
    num_dimes = int(input("How many quarters: "))
    num_nickels = int(input("How many quarters: "))
    num_pennies = int(input("How many quarters: "))
    total = (0.25*num_quarters) + (0.1*num_dimes) + (0.05*num_nickels) + (0.01*num_pennies)
    return total


def resource_update(resources, menu, item):
    requirements = menu[item]['ingredients']
    for ingredient, required_amount in requirements.items():
        resources[ingredient] -= required_amount
    return resources


money = 0
machine_on = True
while machine_on is True:
    userwant = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if userwant == 'off':
        machine_on = False
    elif userwant == 'report':
        resources["money"] = money
        print_resources(resources)
    elif 'espresso' or 'latte' or 'cappuccino':
        checkresource = resource_sufficient(resources, MENU, userwant)
        if checkresource is True:
            total_spent = getcoins()
            cost_of_item = MENU[userwant]["cost"]
            # print(cost_of_item)
            if total_spent < cost_of_item:
                print("Get your money up, not your funny up. Refunded")
            else:
                refund = round((total_spent - cost_of_item),2)
                print(f"Here is you ${refund} in change! ")
                print(f"Here is your {userwant}. Enjoy prick!")
                resources = resource_update(resources, MENU, userwant)
                money += cost_of_item
    else:
        print("Ever heard of a dictionary? Learn how to spell bozo")