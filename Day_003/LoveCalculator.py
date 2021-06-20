def main():
    print("Have you ever wondered if you're gonna spend eternity alone?")
    print("Well, Depresso3000 can answer that for you! It just needs your name and that of your crush")
    name = input("Enter your name: ").lower()
    crush = input("Enter your crush's name: ").lower()
    score1 = name.count("t") + name.count("r") + name.count("u") + name.count("e") + crush.count("t") + crush.count("r") + crush.count("u") + crush.count("e")
    score2 = name.count("l") + name.count("o") + name.count("v") + name.count("e") + crush.count("l") + crush.count("o") + crush.count("v") + crush.count("e")
    score = score1*10 + score2

    print(f"Your final compatibility score is {score}%, but in the end you will die alone no matter what")

if __name__ == "__main__":
    main()
