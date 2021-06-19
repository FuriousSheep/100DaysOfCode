def main():
    height = float(input("What's your height in meters? "))
    weight = int(input("What's you weight in kilograms? "))
    bmi = weight / height**2
    print(f'Your BMI is: {bmi}')

if __name__ == "__main__":
    main()