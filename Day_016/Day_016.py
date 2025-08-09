from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


def coffee_machine():
    options = Menu()
    coffee = CoffeeMaker()
    money = MoneyMachine()
    print(f"All the items available are : {options.get_items()}")
    drink = input("\nWhat would you like? ")

    if drink == "report":
        coffee.report()
        money.report()
        coffee_machine()
    elif drink == "off":
        exit()
    else:
        drink = options.find_drink(drink)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
    
coffee_machine()