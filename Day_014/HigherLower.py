import logo as L
import data as D
import random as R
from os import system

def main():
    score = 0
    gameOn = True
    while gameOn:
        system("clear")
        print(L.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        a = R.choice(D.data)
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        D.data.remove(a)

        print(len(D.data))
        b = R.choice(D.data)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        answer = input("Who has more followers? Type (A) or (B)")
        gameOn = False
        # b = R.choice()
        # # print(f"Compare A:")
        # print(a)
        # print(b)

if __name__ == "__main__":
    main()