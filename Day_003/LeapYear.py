def main():
    year = int(input("The great Nostradamus wants you to feed it a year!\n"))
    if year % 4 :
        leap = False
    else:
        if year % 100 :
            leap = True
        else: 
            if year % 400 :
                leap = False
            else: 
                leap = True
    if leap :
        print(f"{year} is a leap year! Rejoice!")
    else:
        print(f"{year} is not a leap year! So sayeth Nostradamus.")
        

if __name__ == "__main__":
    main()
