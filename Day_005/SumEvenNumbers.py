def main():
    sum = 0
    for i in range(1,50):
        sum += 2*i

    print(f"THE SUM OF ALL EVEN NUMBERS BETWEEN 1 AND 100 IS {sum}")

    print("BUT THAT WAS TOO EASY. LETS DO IT DYNAMICALLY")
    gimme = input("Write me two numbers and I'll give you the sum of the even numbers between them!\n").split(" ")
    for i in range(0,2):
        gimme[i] = int(gimme[i])

    sum = 0
    sum_start = round(min(gimme)/2)
    sum_end = int(max(gimme)/2 + 1)
    for i in range(sum_start, sum_end):
        sum += 2*i

    print(f"AND THE SUM IS {sum}")
    print(f"GET REKT MEATBAG")

if __name__ == "__main__":
    main()
