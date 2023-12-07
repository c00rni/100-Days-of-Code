from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os 

menu = Menu()
maker = CoffeeMaker()
bank = MoneyMachine()
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    user_input = input("What would you like? ({}):".format(menu.get_items()))
    if user_input == "report":
        maker.report()
    if user_input == "off":
        print("System Shutdown...")
        exit()

    item = menu.find_drink(user_input)
    if not item:
        continue
    else:
        if maker.is_resource_sufficient(item) and bank.make_payment(item.cost):
            maker.make_coffee(item)
            


        
    

