import random as r

def main():
    list = []
    sum = 0

    for i in range(1,25):
        list.append(r.randint(145, 210))

    for height in list:
        sum += height
    
    average = round((sum/(len(list)) * 100))/100

    print(f"The list of heights is {list}")
    print(f"The average height is {average}")

if __name__ == "__main__":
    main()
