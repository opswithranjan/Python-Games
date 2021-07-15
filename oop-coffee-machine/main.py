from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? {options}:")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
    else:
        drink = menu.find_drink(choice)
        is_ingredients_enough = coffeemaker.is_resource_sufficient(drink)
        payment = moneymachine.make_payment(drink.cost)
        if is_ingredients_enough and payment:
            coffeemaker.make_coffee(drink)
