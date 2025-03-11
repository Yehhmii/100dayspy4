from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# coffee_menu = MenuItem()
feedback = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        feedback.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if feedback.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                feedback.make_coffee(drink)


