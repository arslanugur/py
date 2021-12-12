# 2651 = 86
# 3342 = 66
# 9017 = 98
# 6113 = ??

def solve (num):
    
    res = ""
    firstDigit = 0
    nextDigit = 1

    # If the number is even
    if len(num)%2==0:
        for i in range(int(len(num)/2)):
            res+= str(int(num[firstDigit]) + int(num[nextDigit]))
            firstDigit+=2
            nextDigit+=2

    # If the number is odd
    else:
        for i in range (int (len(num)/2)):
            res+= str(int(num[firstDigit]) + int(num[nextDigit]))
            firstDigit+=2
            nextDigit+=2

        res+= num[len(num)-1]

    return "The result of " + num + " is " + res
    
print ("*** Brain Teaser ***")
print (solve (input("Insert the number: ").replace(" ", "")))


