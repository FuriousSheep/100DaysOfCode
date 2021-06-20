import random as r

def main():
    list = []
    for i in range(1, 20):
        list.append(r.randint(3000, 30000))

    print(f"The random list of scores is {list}")
    print(f"The highest score is {max(list)}")

if __name__ == "__main__":
    main()
