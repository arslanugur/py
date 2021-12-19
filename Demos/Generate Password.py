# Example:
import random

lower = "abcdefghijklmnopqqrstuvxyz"
upper = "ABCDEFGHIJKLMNOPQSTUVXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = lower + upper + numbers + symbols
length = 16
password = "".join(random.sample(all, length))
print(password)


# Example:
import random
print("What will password include?: ")
print("1. Lowercase Only")
print("2. Lowercase and Uppercase")
print("3. Lowercase and Uppercase Letters and Numbers ")
print("4. Lowercase and Uppercase Letters, Numbers and Special Characters ")
option = int(input("Option: "))
length = int(input("Password Length: "))

option1 = "abcdefghijklmnopqrstuvwxyz"
option2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
option3 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
option4 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

if(option == 1):
    password =  "".join(random.sample(option1,length ))
elif(option == 2):
    password =  "".join(random.sample(option2,length ))
elif(option == 3):
    password =  "".join(random.sample(option3,length ))
elif(option == 4):
    password =  "".join(random.sample(option4,length ))

print ("Your Password is Ready: {0}".format(password))


