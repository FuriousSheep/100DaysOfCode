def main():
    print("HELLO THIS IS BETTER BMI CALC FOR BETTER PEOPLE")
    height = float(input("What's your height in meters? "))
    weight = int(input("What's you weight in kilograms? "))
    bmi = round(weight / height**2)
    if bmi > 35:
        state = "clinically obese"
    elif bmi > 30:
        state = "obese"
    elif bmi > 25:
        state = "overweight"
    elif bmi > 18:
        state = "normal weight"
    else:
        state = "underweight"

    print(f'Your BMI is: {bmi}, which means you are {state} and thus not worthy of love')
    print("This improvement brought to you by Depresso3000")

if __name__ == "__main__":
    main()