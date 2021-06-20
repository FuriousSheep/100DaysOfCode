import random as r

def main():
    moves = ["Rock", "Paper", "Scissors"]
    print("Let's play Rock Paper Scissors with Depresso3000!")
    playerMove = int(input("Choose rock (0), paper (1) or scissors (2)\n"))
    if playerMove not in [0, 1, 2]:
        print ("You're an idiot and you will die unloved")
        return
    compMove = r.randint(0, 2)
    print(f"You play {moves[playerMove]}, and Depresso3000 plays {moves[compMove]}")
    result = playerMove - compMove
    if result in [1, -2]:
        print("You may win today, but Depresso3000 will feast on your tears")
    elif result == 0:
        print("Noone wins, which is exactly what happens everyday in real life")
    else:
        print("You lose! Depresso3000 is thrilled to see you're as stupid as you look")

        

if __name__ == "__main__":
    main()
