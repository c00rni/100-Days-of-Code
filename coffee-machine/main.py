class CoffeeMachine:
    
    def __init__(self):
        self.bank = 0
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.MENU = {
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
    
        def prompt():
            """Prompte user by asking
                off - Turn off the Coffee Machine by entering “off” to the prompt.
                report - Print report.

            """
            while True:
                choise = input("What would you like? (espresso/latte/cappuccino):").casefold()
                match choise:
                    case "espresso":
                        return choise
                    case "latte":
                        return choise
                    case "cappuccino":
                        return choise
                    case "off":
                        exit()
                    case "report":
                        print("Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money}".format(water=self.resources["water"], milk=self.resources["milk"], coffee=self.resources["coffee"], money=self.bank))

        def checkResources(resource_name, quantity):
            """Check resources sufficient"""
            if self.resources[resource_name] >= quantity:
                return True
            else:
                return False

        def main():
            drink = prompt()
            for (key, value) in self.MENU[drink]["ingredients"].items():
                if not checkResources(key, value):
                    print("Sorry there is not enough {}".format(key))
                    break
            

        if __name__ == '__main__':
            main()


CoffeeMachine()

# TODO: Process coins.
# TODO: Check transaction successful?
# TODO: Make Coffee - If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.2

#prompt()