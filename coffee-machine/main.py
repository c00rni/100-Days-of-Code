class CoffeeMachine:
    
    def __init__(self):
        self.bank = 0
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        COIN_TYPES = {"quarters":0.25, "dimes":0.1, "nickles":0.05, "pennies":0.01}
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
        
        def insertCoins():
            """Process coins."""
            user_deposit = 0
            for coin_type, coin_value in COIN_TYPES.items():
                coin_quantity = input("Insert {}: ".format(coin_type))
                user_deposit += float(coin_quantity)*coin_value
            return user_deposit
        
        def checkSucceffulTransaction(drink, user_deposit):
            """Check transaction successful"""

            if user_deposit >= self.MENU[drink]["cost"]:
                change = user_deposit - self.MENU[drink]["cost"]
                self.bank += self.MENU[drink]["cost"]
                print("Here is ${change} dollars in change.".format(change=change))

            for key in self.MENU[drink]["ingredients"].keys():
                self.resources[key] -= self.MENU[drink]["ingredients"][key]
            print("Here is your latte. Enjoy!")


        def main():
            while True:
                can_serve = True 
                drink = prompt()
                for (key, value) in self.MENU[drink]["ingredients"].items():
                    if not checkResources(key, value):
                        print("Sorry there is not enough {}".format(key))
                        can_serve = False
                        break
                if can_serve:
                    checkSucceffulTransaction(drink, insertCoins())


        if __name__ == '__main__':
            main()


CoffeeMachine()