import time

def main():
    print("Welcome to Treasure Island! Your mission is to find the treasure")
    time.sleep(1)
    print("No, the treasure isn't the friends we made along the way")
    time.sleep(1)
    print("The treasure is BOOTAY")
    time.sleep(1)
    choice = input("You find yourself at a crossroad. Will you turn (left) or (right)? ")

    if not choice == "left" :
        print("YOU CHOSE WRONG")
        print("Depresso3000 pushes you into a hole and you spend the rest of your short life in physical and existential pain")
        return
    else:
        print("The path was unpleasant but safe, and ultimately you find yourself on a beautiful beach.")
    
    time.sleep(2)
    print("After a few seconds you see a pannel. This isn't treasure island! You've been misled!")
    print("Luckily, you can see treasure island in the horizon. There is a ferry that can carry you there.")
    choice = input("Do you wait for the ferry or do you swim? (wait) (swim) ")

    if not choice == "wait":
        print("YOU CHOSE WRONG")
        print("Violent trouts attack you and you drown in your tears from failing to defend against such weak fish")
        print("Not far from here, Depresso3000 laughs at your demise")
        return
    else:
        print("You wait for the ferry")

    time.sleep(3)
    print("The ferry appears on the horizon")
    time.sleep(3)
    print("It gets closer")
    time.sleep(3)
    print("And closer")
    time.sleep(3)
    print("And closer")
    time.sleep(3)
    print("Almost there")
    time.sleep(3)
    print("As soon as you step onto the ferry you get teleported to a set of doors inside of treasure island.")
    print("Yeah, I was bored too")
    print("There is a (blue) door, a (green) door and a (red) door.")
    choice = input("Which door do you open? (blue) (green) (red)")

    if choice == "blue":
        print("YOU CHOSE... DEATH")
        print("You get eaten by savage beasts hiding behind the door")
        print("Depresso3000 is amused but ultimately sighs. That's not a funny death. You failed in yet another way")
        return    
    elif choice == "red":
        print("Behind the door, there is light like you have never seen!")
        print("It's so bright you lose yourself in the light")
        print("Incidentally, your whole body erupts from the heat made by the light, and you die burnt to death")
        print("If he could see you, Depresso3000 would rejoice at your end")
        return
    elif choice == "green":
        print("Despite the treachery of the paths and the risk of death looming after every step, you managed to survive the challenge")
        print("You escape from Treasure Island with the grandest of treasures: your life!")
        print("Depresso3000 is pleased that you will have more chances to experience agony")
        print("YOU WIN! maybe...")
    else :
        print("Wait a minute, that's not part of the plan")
        print("In that case... YOU GET NOTHING ! YOU LOSE !")
        print("GOOD DAY SIR!")


if __name__ == "__main__":
    main()
