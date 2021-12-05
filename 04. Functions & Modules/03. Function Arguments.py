# Arguments
  # All the function definitions we've looked at so far have been functions of zero arguments, which are called with empty parentheses.
  # However, most functions take arguments.
  # The example below defines a function that takes one argument:
#
def print_with_exclamation(word): # the argument is defined inside the parentheses.
   print(word + "!")
    
print_with_exclamation("exclamation")
print_with_exclamation("explaination")
print_with_exclamation("examination")

# Example:
def print_with_exclamation(word): 
  print(word + 3)

print_with_exclamation(2) # 5
print_with_exclamation(6) # 9
print_with_exclamation(1) # 4 


# Example:
x = 1 

def MyFunction(xArgument):
  print(xArgument)
  xArgument += 1

MyFunction(x) 
print(x) 

# DIFFERENCE BETWEEN PARAMETER & ARGUMENT 
# Parameters are temporary variable names within functions. 
# The argument can be thought of as the value that is assigned to that temporary variable. 
# Within the function, parameters act as placeholders for the argument it is passed, 
# for instance, lets consider the following simple function to cube a number. 
def cube(number): 
  return number**3  # 'number' here is the parameter for the function 'cube'.  
# This means that anywhere we see 'number' within the function will act as a placeholder until number is passed an argument. 
# To pass an argument to a function is do something like, cube(3), 
# which would call the cube function and would assign the value of '3' (pass the argument '3') to the parameter 'number'. 
# Now wherever you see the parameter 'number' within the function, it will act like a variable with the value of 3. 
# So it will return 3 cubed which is 27. 
# Simply put: "parameters are the placeholders for arguments"


# Example:
def tesla(number): 
  print(“model” + number) 

tesla(“1”)
tesla(“2”)
tesla(“3”)


# Example:
def print_double(x):  # x is the argument in the function
   print(2 * x)

print_double(3) # think of 3 being stored in the variable x --> output: 6


# Example: to define a function that takes two arguments and prints their multiplication.
def print_mult(x, y)
   print(x * y)


# You can also define functions with more than one argument; separate them with commas.
def print_sum_twice(x, y):
   print(x + y)   # 13
   print(x + y)   # 13

# Math
# f(x) = 5x+8 
# x=1 
# f(x) = 13
print_sum_twice(5, 8)


# Example:
def print_sum_sub(x,y): 
    print(x+y)  # 13
    print(x-y)  # -3

print_sum_sub(5,8)


# Example:
def print_sum_n_times(x, y, n): 
    for i in range(n): 
        print(x + y) 
        
print_sum_n_times(5, 8, 3)



# Example:
def print_sum_twice(x, y): 
    for i in range(2): 
        print(x + y) 

print_sum_twice(5, 8) 


# Example:
def user(x,y): 
    print(f'add : {x+y}') # add : 6 
    print(f'sub : {x-y}') # sub : 2 
    print(f'mul : {x*y}') # mul : 8 
    print(f'div : {x/y}') # div : 2.0
    
user(4,2)




# Example:
password = input()
repeat = input() 

def validate(text1, text2): 
    if text1 == text2: 
        print("Correct") 
    else: 
        print("Wrong")


validate(password, repeat)



# Function arguments can be used as variables inside the function definition. 
# However, they cannot be referenced outside of the function's definition. 
# This also applies to other variables created inside a function.
def function(variable):
    variable += 1
    print(variable)

function(7)
print(variable) # This code will throw an error 
# because the variable is defined inside the function and can be referenced only there.
# Technically, parameters are the variables in a function definition, 
# and arguments are the values put into parameters when functions are called.

# Example:
def function(variable): 
    variable += 1 
    print(variable) 

function(7) # 8
# Because in the function call 7 was given as the variable value, 
# then the function did: variable += 1 is the same as var = var + 1 then var = 7 + 1 var = 8

# Example: to define a function that prints "Yes", if its parameter is an even number, and "No" otherwise.
def even(x):
   if x%2 == 0:
      print("Yes")
   else:
      print("No")
      
even(3) # No
even(2) # Yes


# Example:
def even(number):
    if number % 2 == 0:
        print(str(number) + " is an even number")
    else:
        print (str(number) + " is not an even number")
        
even(int(input("type a number: ")))



# Example:
def list_addition(x,y): 
    w = [] 
    if len(x)>len(y): 
        for i in y: 
            w += [x[y.index(i)] + i] 
            w += x[len(y):len(x)] 
    else: 
        for i in x: 
            w += [i + y[x.index(i)]] 
            w += y[len(x):len(y)] 
            print(w) 

x = [1,2,3,4,5,]
y = [2,5,15,5,3,1,6,7,] 

list_addition(x,y)
# [3, 1, 6, 7]
# [3, 1, 6, 7, 7, 1, 6, 7]
# [3, 1, 6, 7, 7, 1, 6, 7, 18, 1, 6, 7]
# [3, 1, 6, 7, 7, 1, 6, 7, 18, 1, 6, 7, 9, 1, 6, 7]
# [3, 1, 6, 7, 7, 1, 6, 7, 18, 1, 6, 7, 9, 1, 6, 7, 8, 1, 6, 7]



# Example:
def print_sum_twice(x, y):
  print(x + y) 
  print(x + y) 
  
e = input("enter 1: ") 
print(e) 
r = input("enter 2: ") 
print(r)
print_sum_twice(float(e), float(r))

# Example:
def sum_or_concat(x, y): 
    print(x + y) 

sum_or_concat(5, 8)         # 13 
sum_or_concat("hello","!")  # hello! 


# Example:
def divide(x, y): 
  print ("I have two numbers,", x, "and", y)
                                            # I have two numbers, 100 and 10
                                            # 10 fits 10 times in 100
                                            # and the remainder is 0
  print (y, "fits", int(x/y), "times in", x) 
                                            # I have two numbers, 25 and 4
                                            # 4 fits 6 times in 25
                                            # and the remainder is 1
  print("and the remainder is", x%y)
                                      # I have two numbers, 17 and 3
                                      # 3 fits 5 times in 17
                                      # and the remainder is 2
  
  print() # prints space

divide(100,10) 
divide(25,4)
divide(17,3)


