

def main():
    row1 = [" "," "," "]
    row2 = [" "," "," "]
    row3 = [" "," "," "]
    map = [row1, row2, row3]
    print("Where do you want to bury the co... the treasure?")
    print(f"{row1}\n{row2}\n{row3}")
    coordinates = int(input("Format: xy, x the column, y the row, starting from top left.\n"))
    y = coordinates%10-1
    x = int((coordinates-y)/10 -1)
    if (x >= 0 and x <= 2) and (y >= 0 and y <= 2):
        map[y][x] = "X"
        print("Here is your treasure map!")
        print(f"{row1}\n{row2}\n{row3}")
    else: 
        print("The coordinates aren't on the map!")

if __name__ == "__main__":
    main()
