import random as r

def main():
    letters = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
        "u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
        "Q","R","S","T","U","V","W","X","Y","Z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    symbols = ["+","=","-","*","/","&","@","(",")", "$", "#", "%"]

    print("Welcome to the password generator!")
    num_letters = int(input("How many letters would you want for your password? "))
    num_numbers = int(input("How many numbers? "))
    num_symbols = int(input("How many symbols? "))

    password = []
    for i in range (0, num_letters):
        password.append(r.choice(letters))
    for i in range (0, num_numbers):
        password.append(r.choice(numbers))
    for i in range (0, num_symbols):
        password.append(r.choice(symbols))
    r.shuffle(password)
    print(f"Your password is {''.join(password)}")

if __name__ == "__main__":
    main()
