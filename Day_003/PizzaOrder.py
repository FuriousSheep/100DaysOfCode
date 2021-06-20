def main():
    print("Welcome to Depresso Pizza, where you only have one choice: getter poorer and fatter")
    print("Prices are the following: 15 for small, 20 for medium and 25 for large")
    print("Extra pepperoni is 2 for a small pizza and 3 otherwise")
    print("Extra cheese is 1")
    size = input("Please choose the size of your pizza: small, medium or large (S, M, L)\n")
    
    if size == "S":
        price = 15
    elif size == "M":
        price = 20
    elif size == "L":
        price = 25
    else:
        print("Wow. Can't even answer a good size. Well, you better enjoy starving")
        return
    
    pepperoni = input("Would you like extra pepperoni? Y or N\n")

    if pepperoni == "Y":
        if size == "S":
            price += 2
        elif size == "M" or size == "L":
            price +=3
    elif not pepperoni == "N":
        print("Frankly I can't be bother by your blasphemous ways")
        return

    cheese = input("Would you like extra cheese with your fat? Y or N\n")
    if cheese == "Y":
        price +=1
    elif not cheese == "N":
        print("I've had enough. Your bank account has been emptied. Do not toy with Depresso3000 again.")
        return

    print(f"That will be a total of {price} remaining days of your life to be paid immediately")
    print("Depresso3000 thanks you for your purchase and wishes you the best of panic attack induced food binge")

if __name__ == "__main__":
    main()
