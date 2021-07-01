import Menu as M

def formatMoney(amount):
    return int(amount*100)/100

def main():
    money = 0
    while True:
        choice = input("Welcome! What kind of coffee would you like?\nespresso / latte / cappuccino\n")
        if choice == "off":
            return
        elif choice == "report":
            for ingredient in M.resources:
                print(f"{ingredient}: {M.resources[ingredient]} {M.units[ingredient]}")
            print(f"Money made: {money} $")
        elif not choice in M.MENU:
            print("Wrong selection, try again later")
        else:
            coffee = M.MENU[choice]
            missing = 0
            for ingredient in coffee["ingredients"]:
                if coffee["ingredients"][ingredient] > M.resources[ingredient]:
                    missing = ingredient        
            if not missing == 0:
                print(f"Sorry, not enough {missing}, try again later.")
                continue
            else:
                print(f"One {choice}, coming up!\nThat will be {coffee[('cost')]}$")
                total = int(input("How many quarters will you insert?"))*0.25
                total += int(input("How many dimes will you insert?"))*0.1
                total += int(input("How many nickels will you insert?"))*0.05
                total += int(input("How many pennies will you insert?"))*0.01

                if total < coffee['cost']:
                    print("Not enough money, change refunded. Try again later!")
                    continue
                else:
                    for ingredient in coffee['ingredients']:
                        M.resources[ingredient] -= coffee['ingredients'][ingredient]
                    money += coffee['cost']
                    print(f"Here's your change: {formatMoney(total - coffee['cost'])}$ and your {choice}.\nSee you soon!")


if __name__ == "__main__":
    main()
