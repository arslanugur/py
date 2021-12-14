# You can raise exceptions by using the raise statement.
# Using the raise statement makes it easy for a coder to determine exceptions in their written codes 
print(1)        #
raise ValueError
print(2)
# You need to specify the type of the exception raised.

# Example:
try:
    a=int(input("Enter: ")) 
    if a<0: 
        raise Exception() 
    print("OK!") 
except Exception: 
    print("ERROR!")
#
# You can use the raise statement outside the except block
# https://www.quora.com/Can-we-use-a-raise-statement-outside-an-except-block-in-the-Python-language

# Example:
try:
  print(1 / 0)
except ZeroDivisionError:   # ZeroDivisionError
  raise ValueError          # ValueError
#
# They're all included in the output, because 'raise' is indented within the except block 



# Exceptions can be raised with arguments that give detail about them.
# Example:
name = "123"
raise NameError("Invalid name!")    # given detail

# Example:
password = input("enter password") 
if len(password) < 8: 
    raise ValueError("password should be more than 8 characters")
#


# Example:
user_input = str(input("Please enter your name:")) 
if User_input == "123": 
    print("invalid username")
#


# Example: to raise a ValueError exception, if the input is negative.
num = input(":")
if float(num) < 0:
    raise ValueError("Negative!")

# Example:
password = input("enter password: ") 
if len(password) < 8: 
    raise ValueError("password should be more than 8 characters")
else: 
    print(password)
#


# In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
# Example:
try:
    num = 5 / 0
except:
    print("An error occurred")  #
    raise   # ZeroDivisionError
#


# Example:
try: 
    x = int(input("Enter a number: ")) 
    num = x / 0 
except: 
    print("an error has occurred") 
    raise 
#    
    

    

# Example: Fibonacci
"""
    This code calculates the Fibonacci value.
    In input must be inserted the index
    The index must be a positive integer.
    To avoid PlayGround "Time limit exceeded" it 
    is suggested to insert an index from 1 to 34.
    If wrong input is inserted a random index is used.

    This code uses 
        try/except/finally (& raise)
        recursive function
        type conversion
        random
"""
import random
random.seed

def Fib(n):
    return 1 if (n < 3) else (Fib(n-1) + Fib(n-2))

try:
    fib_index_str = input("Insert Fibonacci index: ")
    print(fib_index_str + "\n")
    fib_index = int(fib_index_str)
    if fib_index <= 0:
        raise ValueError("Negative!")
    if fib_index > 34:
        raise ValueError("Too Big!")    
except Exception as e:
    print("*"*36)
    print("* Fibonacci Index must be an integer")
    if str(e) == "Negative!":
        print("* Index must be positive (> 0)")
    if str(e) == "Too Big!":
        print("* To avoid Time Limit index < 35")
    fib_index = random.randint(1, 34)
    print("* Selected random value index = " + str(fib_index))
    print("*"*36 + "\n")

finally:
    print("Fib(" + str(fib_index) + ") = " + str(Fib(fib_index)))  
#


