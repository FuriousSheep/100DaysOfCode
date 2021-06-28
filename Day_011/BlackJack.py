import BlackJackData as B
import random as R
from os import system

def sum(list):
    sum = 0
    for e in list:
        sum += e
    return sum

def showHands(playerHand, dealerHand):
    print(f"Your cards: {playerHand}, current score {sum(playerHand)}")
    print(f"Dealer's first card: {dealerHand[0]}")

def updateDealerHand(hand):
    if sum(hand) < 17:
        hand += [R.choice(B.cards)]
    return hand

def updatePlayerHand(hand):
    hand += [R.choice(B.cards)]
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
    return hand

def isGameWon(playerHand, dealerHand):
    playerScore = sum(playerHand)
    dealerScore = sum(dealerHand)
    
    if playerScore == 21:
        print(B.blackjackWinMessage)
        return True
    elif dealerScore == 21:
        print(B.blackjackLossMessage)
        return True
    elif playerScore > 21:
        print(B.lossMessage)
        return True
    elif dealerScore > 21:
        print(B.winMessage)
        return True
    else:
        return False 

def playerWins(playerScore,dealerScore):
    if playerScore > dealerScore:
        return not playerScore > 21
    else:
        return dealerScore > 21

def play():
    print(B.logo)
    playerHand = [R.choice(B.cards), R.choice(B.cards)]
    dealerHand = [R.choice(B.cards), R.choice(B.cards)]
    showHands(playerHand, dealerHand)
    while (not isGameWon(playerHand, dealerHand)) and (input(B.getNewCard) == 'y'):
        playerHand = updatePlayerHand(playerHand)
        dealerHand = updateDealerHand(dealerHand)
        showHands(playerHand, dealerHand)
    playerScore = sum(playerHand)
    dealerScore = sum(dealerHand)
    print(f"\nYour final score is {playerScore} against the dealer's {dealerScore}\n")
    print("The winner is " + ('you! =D\nYou win!' if playerWins(playerScore,dealerScore) else "the dealer\nYou lost :'("))

def main():
    while input(B.beginMessage) == "y":
        system("clear")
        play()

if __name__ == "__main__":
    main()
