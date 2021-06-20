def main():
    output = ""
    print(output)
    for i in range(1, 101):
        if not i % 3:
            output += "fizz"
        if not i % 5:
            output += "buzz"
        
        print(f"{output or i}")
        output = ""

if __name__ == "__main__":
    main()
