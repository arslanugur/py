# This program shows how we can create same program without the use of recursion in python, 
# Also explains how use of recursion makes our work easy.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
def factorial_1(n):
    num = n
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            n = n * (num-1)
            num -= 1
        return n

print("======================================")
print("         Recursion")
print("======================================")
x = int(input("Please Enter a number: "))
print(x)
print("Factorial of",x,"through recursion method is",factorial(x))
print("Factorial of",x,"without using recursion method is",factorial_1(x))

