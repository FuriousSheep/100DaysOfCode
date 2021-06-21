import time as t
import random as r
import os 

def initHangman():
    # 9 stages
    return [
        """
                
                
                
                
                
        
        """,
        """
                
                
                
                
                
        __________
        """,
        """
                |
                |
                |
                |
                |
        ________|_
        """,
        """
            ----|
                |
                |
                |
                |
        ________|_
        """,
        """
            ----|
            |   |
    -_-? -  O   |
            |   |
                |
        ________|_
        """,
        """
            ----|
            |   |
    O_o  -  O   |
            |\  |
                |
        ________|_
        """,
        """
            ----|
            |   |
     T_T -  O   |
           /|\  |
                |
        ________|_
        """,
        """
            ----|
            |   |
    help -  O   |
           /|\  |
           /    |
        ________|_
        """,
        """
            ----|
            |   |
     X_X -  O   |
           /|\  |
           / \  |
        ________|_
        """
    ]


def init():
    for i in range(0,5):
        clear()
        print("WELCOME TO HANGMAN!")
        print("The game where every time you make a mistake you bring someone else closer to their death!")
        print("Depresso3000 is thrilled by this peculiar activity!")
        print("It will now pick a random word from its vast computer brains for you to divine!")
        print(f"""                                     
        /            |   |   /\   |\  |  /¨¨  |\  /|   /\   |\  |             \\
        |----------- |---|  /--\  | \ | |  -- | \/ |  /--\  | \ |   -----------|
        \            |   | /    \ |  \|  \../ |    | /    \ |  \|             /
        
        Begins in {5-i}...
        """)
        t.sleep(1)

def chooseWord():
    words = ["meatbag", "rattlesack", "bloodsack", "despair", "finitude"]
    return r.choice(words)

def clear():
    os.system("clear")

def isGameWon(shadowWord):
    if not "_" in shadowWord:
        return True
    else:
        return False

def fillOut(fillable, word, guess):
    i = 0
    for letter in word:
        if letter == guess:
            temp = list(fillable)
            temp[2*i] = guess
            fillable = "".join(temp)
        i += 1
    return fillable

def playGame():
    hangScore = 0
    word = chooseWord()
    hangman = initHangman()
    shadowWord = ""
    for letter in word:
        shadowWord += "_ "
    while not isGameWon(shadowWord) and hangScore < 8:
        clear()
        print(shadowWord)
        print(hangman[hangScore])
        guess = input("""
        What is your letter choice?
        """).lower()
        if guess in word:
            shadowWord = fillOut(shadowWord, word, guess)
        else:
            hangScore += 1
    if isGameWon(shadowWord):
        clear()
        print(shadowWord)
        print(hangman[hangScore])
        print("YOU WON! Now go do something else")
    elif hangScore == 8:
        clear()
        print(shadowWord)
        print(hangman[hangScore])
        print("HA! You lost, and killed an innocent torturer! Loser!")
    else:
        print("""
        What... how... this isn't supposed to happen.
        Well you crashed the game somehow. Good job!
        """)

def main():
    init()
    playGame()
    
if __name__ == "__main__":
    main()