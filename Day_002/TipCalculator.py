def main():
    print("Welcome to TipCalculator 3000, where the numbers are made up and the currency don't matter.")
    bill = float(input("What was the total bill? "))
    people = int(input("How many people to split the bill? "))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
    dirtyBillPerPerson = (bill * (100 + tip) / 100) / people
    billPerPerson = int(dirtyBillPerPerson * 100) / 100
    print(f'Each person should pay: {billPerPerson} ')

if __name__ == "__main__":
    main()