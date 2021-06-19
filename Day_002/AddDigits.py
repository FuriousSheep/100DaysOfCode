def main():
    number = int(input("GIMME A TWO DIGIT NUMBER: "))
    output = int(number%10 + (number-number%10)/10)
    print(f'Result is: {output}')

if __name__ == "__main__":
    main()