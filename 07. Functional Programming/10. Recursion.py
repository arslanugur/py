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
# Our problem: def factorial(x): if x == 1: return 1 else: return x * factorial(x-1) print(factorial(5)) 
# 1. We pass integer 5 as an argument to the factorial function. 5 does not equal 1 so we return 5 * "another call to the same function". 
# This is where the bottom of our stack/pyramid starts. Think of 5 as the ground floor of our stack/pyramid. 
# 2. Now we start building the second layer of our stack/pyramid. 
# We now run our function again with (x-1) aka (4) as the argument. 4 does not equal 1, 
# so we return 4 * "another call to the same function". Our second layer now looks like: 4 *. 
# 3. This continues for 3 and 2, each building their own layer of the s


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

# When trying to execute the following code "Time Limit Exceeded" is printed. 
def factorial(x): 
    try: 
        return x * factorial(x-1) 
    except: 
        print(x) 

print(factorial(5))
#

# Every time you call a function, computers store your current place (and often some variables) before going (deeper) 'into" the code you're calling; 
# a strategy that lets you "return" and restore your state. 
# The storage area (or: "call stack") is limited in size, 
# so if you continue to go deeper (without returning) you will eventually exhaust space on the call stack and reach the maximum depth. 
# Recursion is just a special case of going deeper, i.e., a function that calls into itself.

# Example:
def factorial(x): 
    if x == 1: 
        return 1 
    else: 
        return x * factorial(x-1) 

print(factorial(5)) 

# The pattern: 
# Step 1: 5 * factorial(5-1) #This will create 5*factorial(4) leading back to the function def factorial(4) 
# Step 2: 4*factorial(4-1) 
# Step 3: 3*factorial(3-1) 
# Step 4: 2*factorial(2-1) 
# Step 5: factorial(1) 
# This returns 1 since it meets the "if" criteria. 
# Step 6: 5*4*3*2*1 or 5*4*3*2*factorial(1) 
# This will stop the infinite loop.
     
# Example: How much is maximum recursion depth?
def recursion(n): 
    if n <= 0: 
        return
    print(n)
    
n = 5
recursion(n - 1) 
recursion(1000) 
# The maximum depth might be 998 by default


# Example: Write the even and odd numbers from a sequential list ordered with a recursive function 
def recorreList(A):
    if (len(A) <= 1):
        return
        
    if A[0] % 2 == 0:
        print (A[0]," ",end="")
        
    recorreList(A[2:])
    print (A[1]," ",end="")
        

A = [x for x in range(10)]
print(A)
recorreList(A)
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0  2  4  6  8  9  7  5  3  1  
"""

# Example:
def factorial(x): 
    if x == 1: 
        return 1 
    elif x==0: 
        return 1 
    else: 
        return x* factorial(x-1) 

print("The Factorial is: ",factorial(int(input('Enter Number: '))))


# Example: The recursive function does not have a stopping condition, It will give a runtime error
def sum_to(x):
   return x + sum_to(x-1)

print (sum_to(5))   # RecursiveError, RuntimeError
# Its base case is not defined in this incidence. So it will just run like the energizer bunny))

# The sum_to(x-1) argument continues to run infinitely without a base case to stop it. 
# sum_to(x) will do: x + sum_to(x-1) (x-1) becomes the new x so The previous x remains and the new x runs. 
# 1st_run: 5 + sum_to(4) 
# 2nd_run: 5 + 4 + sum_to(3) 
# 3rd_run: 5 + 4 + 3 + sum_to(2) 
# 4th_run: 5 + 4 + 3 + 2 + sum_to(1) 
# 5th_run: 5 + 4 + 3 + 2 + 1 + sum_to(0) 
# 6th: 5 + 4 + 3 + 2 + 1 + 0 + sum_to(-1) 
# Infinite: 5 + 4 + 3 + 2 + 1 + 0 + -1 + -2 + -n


# SECTION 3
# Recursion can also be indirect. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions.
# Example:
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(17))   # True
print(is_even(23))  # False

# First of all, we all know.. NOT TRUE = FALSE & NOT FALSE = TRUE.. 
# Now, I can't give you demo for "print(is_odd(17))" Because it will take many hours to write it down.. 
# So, here I have given answer for "print(is_odd(3))". On that basis you will understand rest of the values.. 
# Here, instead writing return, I just wrote "ret" for less coding.. 
# "is_odd(3)" "ret not is_even(3)" "ret not (is_odd (3-1))" "ret not (is_odd(2))" "ret not (ret not is_even(2))" 
# "ret not (ret not (is_odd(2-1)))" "ret not (ret not (is_odd(1)))" "ret not(ret not (ret not is_even(1)))" 
# "ret not(ret not (ret not (is_odd(1-1))))" "ret not(ret not (ret not (is_odd(0))))" "ret not(ret not (ret not (ret not is_even(0))))"

# Generalizing: is_even(x) will return x number of NOTs during the recursion to the base case of x==0 is TRUE. 
# So, if x is even, the even number of NOTs cancel and return TRUE. If x is odd, the odd NOTs change TRUE to FALSE. 
# Likewise, is_odd(x) returns (x+1) NOTs before getting to x==0 in the recursion. 
# So if x is even, it will return an odd number of NOTs, changing TRUE to FALSE. 
# Likewise, if x is odd, an even number of NOTs will cancel out and return TRUE.

#isodd5 #=not(iseven5) #=not(isodd4) #=not(not(iseven4)) #=not(not(isodd3)) #=not(not(not(iseven3))) #=not(not(not(isodd2))) 
#=not(not(not(not(iseven2)))) #=not(not(not(not(isodd1)))) #=not(not(not(not(not(iseven1))))) #=not(not(not(not(not(isodd0))))) 
#=not(not(not(not(not(not(iseven0)))))) #=not(not(not(not(not(not(True)))))) #=not(not(not(not(not(False))))) 
#=not(not(not(not(True)))) #=not(not(not(False))) #=not(not(True)) #=not(False) #=True


# I would say that if you insist on using recursion on finding whether the number is even or odd, I would use it like that: 
def is_even(x): 
    if x == 0: 
        return True 
    elif x == 1: 
        return False 
    else: 
        x -= 2 
        return is_even(x) 
    
def absolute_x(x):
    return abs(x) 

number_to_evaluate = -258 
absolute_number = absolute_x(number_to_evaluate) 
base_string = "Number " + str(number_to_evaluate) + " is " + ("even" if is_even(absolute_number) else "odd") 
print(base_string)                  # Output: Number -258 is even
# Makes more sense and no need to jump between two methods in recursion. 
# Subtracting 2 from even number will eventually give 0 and for odd numbers will eventually give 1.

# I have written this for myself to understand for is_odd(5) and is_even(3). 
# Hopefully somebody will find this useful too 
# def is_even(x): if x == 0: return True else: return is_odd(x-1) def is_odd(x): return not is_even(x) 
# print(is_odd(5)) print(is_even(3)) is_odd(5) return not is_even(5) not is_even(5) 
# return not is_odd(5-1) not not is_even(4) = is_even(4) is_odd (4-1) not is_even(3) 
# not is_odd(3-1) not not is_even(2) = is_even(2) is_odd(2-1) not is_even(1) not is_odd(1-1) not not is_even(0) = is_even(0) True 
# is_even(3) return is_odd(3-1) not is_even(2) not is_odd(2-1) not not is_even(1) = is_even(1) is_odd(1-1) not is_even(0) not True False

# In code playground I've added print statements that show what is going on 
# I had to lower the number because with the print statements this gets too much for code playground
# Example:
def is_even(x):
    print("call to is_even where x = " + str(x))
    if x == 0:
        print("since x is 0 we hit our base and return True for this call of is_even")
        return True
    else:
        print("x is not 0 on this call of is_even so we check if the number below is odd")
        return is_odd(x-1)

def is_odd(x):
    print("call to is_odd where x = " + str(x))
    print("we check if this current value is the opposite of even")
    resultFromIsEven = is_even(x)
    print("our result from is_even with x = " + str(x) + " comes back as " + str(resultFromIsEven))
    result = not (resultFromIsEven)
    print("so the call of is_odd where x = " + str(x) + " is returned as " + str(result) )
    return result


print(is_odd(7))
# print(is_even(23))

# The easiest way to understand this is to count the number of 'not'. as 'not' 'not' True = True; 'not' 'not' 'not' True = False. 
# the var 'x' will always ends in '0' but the amount on 'not' he generated defines the final answer True or False. 
# for example if we look at is_odd (2) - we will get 3 'not' 's for 2,1 and 0 (before running in is_even)


# These modifications below may help understanding the alternating calls to both functions. 
# Run this code and inspect the output statements backwards, 
# noting that (not is_even 0) is always True: def is_even(x): if x == 0: print (": ", end="") return True else: print ("(is_even " + str(x) + ")", end="") 
# return is_odd(x-1) def is_odd(x): print ("(not is_even " + str(x) + ")", end="") return not is_even(x) print(is_odd(3)) print(is_even(3))


# Example:
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)

print(fib(4))       # 5

# Explanation:
# fib(4) = fib(3) + fib(2) = (fib(2) + fib(1)) + (fib(1) + fib(0)) = ((fib(1) + fib(0)) + 1) + (1 + 1) = ((1+1)+1) + 2 = 3 + 2 => fib(4) = 5
# This is a bad code to calculate Fibonacci, it requires excessive amount of time when x is higher. 
# Because python calculates same fib(x) more than one time, for example in this code fib(1) is calculated for 3 times and fib(0) for 2 times. 
# This is where u should use "memoization" technique.

# Fibonacci=1,1,2,3,5,8,13,21,34... f(0)=1 f(1)=1 f(2)=f(1)+f(0)=1+1=2 f(3)=f(2)+f(1)=(f(1)+f(0))+1=3 f(4)=f(3)+f(2)=(f(2)+f(1))+(f(1)+f(0))=5

# Example:
def fib(x): 
    if x==0 or x==1: 
        print(x) 
        return 1 
    else: 
        print(x) 
        return fib(x-1)+fib(x-2) 

print(fib(4)) # 4 3 2 1 0 1 2 1 0 5 


# Example: 
def fib(x): 
    if x==0 or x==1: 
        return 1 
    else: 
        return fib(x-1)+fib(x-2) 
for x in range(20): 
    print(fib(x))
#

# https://blog.penjee.com/wp-content/uploads/2015/06/fibonacci-recursion-demonstration-animation-python.gif



