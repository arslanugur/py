# SECTION 1
# Recursion is a very important concept in functional programming.
# The fundamental part of recursion is self-reference - functions calling themselves. 
# It is used to solve problems that can be broken up into easier sub-problems of the same type.

# Recursion is a way of programming or coding a problem, in which a function calls itself one or more times in its body. 
# Usually, it is returning the return value of this function call. 
# If a function definitionfulfils the condition of recursion, we call this function a recursive function.

# A classic example of a function that is implemented recursively is the factorial function, which finds the product of all positive integers below a specified number.
# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). 
# To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!.
# Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials.
# Below is a recursive implementation of the factorial function. 
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

print(factorial(5))     # 120

# The base case acts as the exit condition of the recursion.

# It is basically saying. x = 5 If x is 1....return one If not, return x * (x-1) 
# That is.... 5 *(5-1) = 5 *4...now x is 4 4 *(4-1) = 4*3...now x is 3 3 *(3-1) = 3*2...now x is 2 2 *(2-1) = 2*1...now x is 1 5 * 4 * 3 * 2 * 1 = 120.

# The example code factorial is an infinite recursive function, 
# because it doesn't check if the inputted number is a positive integer or not. If I input a negative number it will crash!

# 1. User must enter a number and store it in a variable. 
# 2. The number is passed as an argument to a recursive factorial function. 
# 3. The base condition is that the number has to be lesser than or equal to 1 and return 1 if it is. 
# 4. Otherwise the function is called recursively with the number minus 1 multiplied by the number itself. 
# 5. The result is returned and the factorial of the number is printed. 
# Found at https://www.sanfoundry.com/python-program-find-factorial-number-recursion/



# Example:
def factorial(x): 
  assert x >=0,"Enter a positive number" 
  assert round(x)==x, "Enter an integer" 
  if x == 1 or x ==0: 
    return 1 
  else: 
    return x * factorial(x-1)
print(factorial(5)) 
# Pay attention the negative number or using a float. 
# It is better to go with assert with the extra argument so you know what is the error. 
# You could raise, but in the end assert == raise if.

# Example:
return 5 * factorial(4)
return 4 * factorial(3)
return 3 * factorial(2)
return 2 * factorial(1)
return 1
return 2 * 1
return 3 * 2
return 6 * 4 
return 24 * 5
return 120
# Each time factorial is called, it creates a new stack frame and the next frame is executed before the previous one returns. 
# Once you hit `return 1`, that last frame (the base case) returns and pops off the stack, and then the previous, etc. 
# As each stack frame returns and pops off the stack, I picture it kind of 'unwinding' the recursion. 

# https://youtu.be/Mv9NEXX1VHc
# https://www.youtube.com/watch?v=Mv9NEXX1VHc 
# https://www.youtube.com/watch?v=Qk0zUZW-U_M

# Recursion is possible with python but a good coder should not use recursion as the code is difficult to understand 
# and as there are some memory risk by filling the stack (each time the function calls itself, the computer has to keep the call in memory).

# Same using lambda: 
fact = lambda x: 1 
if x==1 
else x*fact(x-1) 
print(fact(5))


# 0! = 1 is not accounted for. Neither are negative values nor non-integers. Border checking is a very important part of programming!


# I made the following addition to the code for 0! = 1, and to check for negative, non-integer and non-numerical input!
def factorial(x):
    if x == 0 or x == 1: 
        return 1
    else:
        return x * factorial(x-1) 
  
ui = input() 
try:
    ui = float(ui)
    if ui != round(ui) or ui < 0:
        print("You entered: " + str(ui) + "\nTry again with a positive integer!")
    else:
        ui = int(ui)
        print(str(ui)+ "! = " + str(factorial(ui)))
except ValueError:
    print("You entered: " + str(ui) + "\nTry again with a positive integer!")
#    

# ui is a variable I used for user input. 
# The 'try' and 'except' blocks raise a ValueError if the user enters a string instead of a number, as the float() function will not work on strings.
# 'if ui != round(ui)' tests for non-integers; e.g 5.3 != 5, and 'ui < 0' tests for negative input. 
# Hence the 'if' block runs if user inputs decimal or negative number. 'else' block runs if user inputs a positive i

# 5*4 =20 20*3=60 60*2=120 def factorial(x): if x == 1: return 1 else: return x * factorial(x-1) print(factorial(5))

# Here's another explanation in case people were having trouble wrapping their head around the problem. 
# We ara going to use "stack" and "pyramid" interchangeably. 
# "Stack" is the official term, but visualizing what is happening as a "pyramid" might help some folks better. 
# I will diagram the stack/pyramid further down in my comment. 
# Our problem: def factorial(x): if x == 1: return 1 else: return x * factorial(x-1) print(factorial(5)) 1. We pass integer 5 as an argument to the factorial function. 5 does not equal 1 so we return 5 * "another call to the same function". This is where the bottom of our stack/pyramid starts. Think of 5 as the ground floor of our stack/pyramid. 2. Now we start building the second layer of our stack/pyramid. We now run our function again with (x-1) aka (4) as the argument. 4 does not equal 1, so we return 4 * "another call to the same function". Our second layer now looks like: 4 *. 3. This continues for 3 and 2, each building their own layer of the s


# Another Example:
"""Functional Programming - Recursion""" 
def Recursion(x): 
  if x==0: 
    return (0) 
  elif x==1: 
    return (1) 
  else: 
    return (Recursion(x-1)+Recursion(x-2)) 

print(Recursion(5)) # 5 
# Explanation:
# After giving 5, 
# Result of Recursion(5): Recursion(4) + Recursion(3) 
# Result of Recursion(4): Recursion(3) + Recursion(2) 
# Result of Recursion(3): Recursion(2) + Recursion(1) 
# Result of Recursion(2): Recursion(1) + Recursion(0) 
# Result of Recursion(1): 1 
# Result of Recursion(0): 0 
# Recursion(4) + Recursion (3) 
  # = Recursion(3) + Recursion(2) + Recursion(2) + Recursion(1) 
  # = Recursion(2) + Recursion(1) + Recursion(1) + Recursion(0) + Recursion(1) + Recursion(0) + 1 
  # = Recursion(1) + Recursion(0) + 1 + 1 + 0 + 1 + 0 + 1 
  # = 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 = 5
#

# What is the base case of a recursive function? ---> A case that doesn't involve any further calls to that function

# The same factorial function can be defined as: 
def factorial(x): 
  if x == 0: 
    return 1 
    return x * factorial(x-1)
#


# SECTION 2
# Recursive functions can be infinite, just like infinite while loops. These often occur when you forget to implement the base case.
# Below is an incorrect version of the factorial function. It has no base case, so it runs until the interpreter runs out of memory and crashes.
def factorial(x):
    return x * factorial(x-1)

print(factorial(5))      # RecursionError

# Comment: https://www.sololearn.com/learning/1073/2465/5111/1

