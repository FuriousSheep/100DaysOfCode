import random as r

def main():

    list = input("Please enter the names of the people willing to pay for your common debauchery:\n(format: \"Name, Name, Name, etc\")\n").split(', ')
    sacrifice = r.choice(list)
    print(f'The sacrifice should be {sacrifice}. Burn them at the stakes, or have them pay for your meal')
    
if __name__ == "__main__":
    main()
