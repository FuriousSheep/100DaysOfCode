def main():
    hometown = input("What is your hometown?\n")
    if hometown == "":
        print("Ok so you come from Nowhere, Alabama, got it.")
        hometown = "Nowhere"
    petName = input("What is your first pet name?\n")
    if petName == "":
        print("No pet, so no pet name. I'll go with \"Honey\", it's a common petname for all genders.")
        petName = "Honey"
    print(f'Your band name should be \"{hometown.capitalize()} {petName.capitalize()}\"')

if __name__ == "__main__":
    main()