from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
menu = Menu()

def report():
    cm.report()
    mm.report()

def main():
    print(f"Welcome to the OOP Coffee Machine!\nWhat would you want?")
    while True:
        command = input(f"{menu.get_items()}\n")
        if command == "off":
            return
        elif command == "report":
            report()
        else:
            order = menu.find_drink(command)
            print(f"That will cost ${order.cost} please.")
            if cm.is_resource_sufficient(order):
                if mm.make_payment(order.cost):
                    cm.make_coffee(order)

if __name__ == "__main__":
    main()