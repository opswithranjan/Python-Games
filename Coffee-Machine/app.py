import os
from need import MENU, resources


penny = 0.01
dime = 0.1
nickle = 0.05
quarter = 0.25

profit = 0


def process_coin():
    print("\nPlease insert coin\n")
    quarters = int(input("How many quarters? : ")) * quarter
    dimes = int(input("How many dimes? : ")) * dime
    nickles = int(input("How many nickles? : ")) * nickle
    pennies = int(input("How many pennies? : ")) * penny
    money = quarters + dimes + nickles + pennies
    return money


def is_money_enough(money, cost):
    """return true when payment is accepted"""
    if money < cost:
        global profit
        print("Sorry that's not enough money. Money refunded")
        return False
    elif money == cost:
        profit += cost
        return True
    elif money > cost:
        refund = round(money - cost, 2)
        profit += cost
        print(f"Here is ${refund} in change")
        return True


def is_enough(order_ingridients):
    for item in order_ingridients:
        if order_ingridients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_a_drink(drink, order_ingridients):
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"Here is your ☕️ {drink}\n")


machine_on = True
while machine_on is True:
    choice = input("What would you like to drink?(Espresso,Latte,Cappucino):").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(
            f"Water: {resources['water']} \nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney:{profit}\n"
        )
    else:
        drink = MENU[choice]
        if is_enough(drink["ingredients"]):
            payment = process_coin()
            if is_money_enough(payment, drink["cost"]):
                make_a_drink(choice, drink["ingredients"])
