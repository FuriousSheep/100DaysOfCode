import random as r
r.seed()

def main():
    number = r.randint(1,2)
    if number == 1:
        print("heads")
    else:
        print("tails")

if __name__ == "__main__":
    main()
