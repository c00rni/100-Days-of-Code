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


def prompt():
    """Prompte user by asking"""
    while True:
        choise = input("What would you like? (espresso/latte/cappuccino):").casefold()
        if choise == "espresso" or choise ==  "latte" or choise == "cappuccino":
            return choise

# TODO: Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: Print report. when asked. List current resources values left.
# TODO: Check resources sufficient?
# TODO: Process coins.
# TODO: Check transaction successful?
# TODO: Make Coffee - If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.2

prompt()