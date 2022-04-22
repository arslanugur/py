def main():
    filename = input("enter a file name: ")
    file = open(filename,"r")
    m = file.read(20)
    print(m)

    for i in range(3):
        char = input("search character: ")
        file.seek(0)
        n = file.read()
        count = 0
        for c in n:
            if c == char:
                count += 1

        perc = 100*(count/len(n))
        print(f"{char} found {count} times. which is {perc}% of the total character")
        file.close




if __name__ == "__main__":
    main()
    
    
