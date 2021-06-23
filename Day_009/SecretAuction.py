import math as M
import os
import SecretAuctionText as S


def getAuctionneers(auction):
    name = input("What is your name?")
    auctionAmount = int(input("How much do you want to auction? $"))
    auction[name] = auctionAmount
    while(input(S.ContinueAuctionMessage) == "yes"):
        os.system("clear")
        name = input("What is your name?")
        auctionAmount = int(input("How much do you want to auction? $"))
        auction[name] = auctionAmount
    return auction

def showWinner(auction):
    os.system("clear")
    maxAuction = 0
    winner = ""
    for key in auction.keys():
        if auction[key] > maxAuction:
            maxAuction = auction[key]
            winner = key
    print(f"The winner of the auction is {winner} who bid ${maxAuction}.")

def main():
    print(S.logo)
    auction = {}
    auction = getAuctionneers(auction)
    showWinner(auction)

if __name__ == "__main__":
    main()
