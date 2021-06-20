import random as r

def main():
    list = input("Give me ten two-digit positive numbers:\n").split(" ")

    print(f"The highest number you've given is {max(list)}")

if __name__ == "__main__":
    main()
