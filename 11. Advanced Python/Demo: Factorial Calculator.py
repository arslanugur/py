def main():
    print("\nTo calculate the factorial of a number press 1 \nTo Quit this program press 0")
    res = int(input("input:"))
    if res == 1:
        prog()
    elif res == 0:
        return 0
    else:
        print("invalid input!")
        main()

def prog():
    init = input("Find the factorial of: ")
    value = int(init)
    if value == 0:
        print("Result = 0")
        main()
    elif value == 1:
        print("Result = 1")
        main()
    elif value < 0:
        print("Value must be greater than 0")
        main()
    else:
        ans = fact(value)
        print(f"Result = {ans}")
        main()

def fact(y):
    z = 1
    while y>0 and y-1 != 0:
        z = z*(y*(y-1))
        y = y-2
    return z


if __name__ == "__main__":
    main()
#


