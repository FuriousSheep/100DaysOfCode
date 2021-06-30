import logo as L
import data as D
import random as R
from os import system

def main():
    score = 0
    gameOn = True
    a = 0
    while gameOn and score < 49:
        system("clear")
        print(L.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        if a == 0:
            a = R.choice(D.data)
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        D.data.remove(a)
        print(L.vs)
        b = R.choice(D.data)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        answer = input("Who has more followers? Type (A) or (B)")
        solution = "A" if a["follower_count"]>b["follower_count"] else "B"
        if answer == solution:
            score += 1
            a = b
            print("correct!")
        else:
            system("clear")
            print(L.logo)
            print(f"Wrong answer. Final score: {score}")
            gameOn = False
    if score == 49:
        system("clear")
        print(L.logo)    
        print("Wow! You got the max amount of points! You win!")

if __name__ == "__main__":
    main()