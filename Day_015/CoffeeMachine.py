import Menu as M



def main():

    while True:
        #Greet the user, ask their choice
        choice = input("Welcome! What kind of coffee would you like?\nespresso / latte / cappuccino\n")
        #Check their choice. If invalid, abort.
        if choice == "off":
            return
        elif not choice in M.MENU:
            print("Wrong selection, try again later")
        #If their choice is valid, check if available resources are sufficient in stores
        else:
            coffee = M.MENU[choice]
            for ingredient in coffee["ingredients"]:
        #If they are not, abort.
                if coffee["ingredients"][ingredient] > M.resources[ingredient]:
                    print(f"Sorry, not enough {ingredient}, try again later.")
                    continue
        #If they are, ask for the adequate amount.        
            print(f"One {choice}, coming up!\nThat will be {coffee[('cost')]}$")
        #Remember, the user can only pay in instances of:
        ## Quarters 0.25, dimes 0.10, nickels 0.05 and pennies 0.01
            quarters = int(input("How many quarters will you insert?"))
            dimes = int(input("How many dimes will you insert?"))
            nickels = int(input("How many nickels will you insert?"))
            pennies = int(input("How many pennies will you insert?"))
            total = 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies

            if total < coffee['cost']:
                print("Not enough money, change refunded. Try again later!")
                continue
            else:
                for ingredient in coffee['ingredients']:
                    M.resources[ingredient] -= coffee['ingredients'][ingredient]
                print(f"Here's your change: {total - coffee['cost']}$ and your {choice}.\nSee you soon!")
        
    #If it's enough:
    # 1 deduct the resources from the stores
    # 2 give the user coffee
    # 3 give the user change 
    # 4 thank the user



if __name__ == "__main__":
    main()
