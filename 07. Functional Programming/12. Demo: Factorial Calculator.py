#Banner
def decor(func):
    def wrap():
        print("================="*2)
        func()
        print("================="*2)
    return wrap

@decor
def print_text():
    print(" Welcome to Factorial Calculator")
    print(" Version:       0.1")
    print(" Author:        Uğur Arslan")
print_text()

#Factorial Function
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

#User Interaction
print("Enter a number > ")
num = int(input())
print(factorial(num))
print("\n\nBye")


