import random as R

def main():
    number = R.randint(1,100)
    print("I'm thinking of a number between 1 and 100!")
    print(f"Psshhh, the answer is {number}")
    mode = input("First, select (easy) or (hard): ")
    modes = {
        "easy": 10,
        "hard": 5
    }
    if mode in modes.keys():
        tries = modes[mode]
    else:
        print("This mode is not yet supported!")
        return

    for i in range(0,tries):
        print(f"You have {tries - i} tries left")
        guess = int(input("Your guess:"))
        if number == guess:
            print(f"{number} was the number! You win!")
            return
        else:
            if number > guess:
                print("Too low")
            else: 
                print("Too high")
    print("You have no tries left! You lose :(")

if __name__ == "__main__":
    main()
