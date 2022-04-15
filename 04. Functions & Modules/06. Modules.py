# ALL PYTHON MODULES (List of Modules)
# https://docs.python.org/3/py-modindex.html
# os, math, time, datetime, random, smtplib, tkinter, sqlite3, csv

# Modules are pieces of code that other people have written to fulfill common tasks, such as generating random numbers, performing mathematical operations, etc.

# The basic way to use a module is to add import module_name at the top of your code, 
# and then using module_name.var to access functions and values with the name var in the module.

# For example, the following example uses the random module to generate random numbers: 
import random

for i in range(5):
    value = random.randint(1, 6)    # random integer
    print(value)    # 5 5 3 2 1
#

# The code uses the randint function defined in the random module to print 5 random numbers in the range 1 to 6.

# Example: to try the same example with a larger interval for randint: 
for i in range(5): 
  value = random.randint(1,10) 
  print(value) # 1 9 5 8 8
#


# Example: A larger range but smaller randint: 
for i in range(10): 
  value = random.randint(1,3) 
  print(value) # 2 3 3 3 3 2 1 3 1 3 
#


# Example: Guess Number Game
import random 
player = 0 
tries = 0 
computer = random.randrange(1,11) 
while True: 
    player = int(input("Your move: ")) 
    tries = tries + 1 
    if player > computer: 
        print("Too High!") 
    elif player < computer: 
        print("Too Low!") 
    else: 
        print("You got it! It's", computer)
        print("Number of tries:", tries, "\n") 
        tries = 0 
        computer = random.randrange(1,11) 
#

# Example:
import math             # math module is being used in this code
num = 10
print (math.sqrt(num))


# There is another kind of import that can be used if you only need certain functions from a module.
# These take the form from module_name import var, and then var can be used as if it were defined normally in your code.
# For example, to import only the pi constant from the math module: 
from math import pi
print(pi)           # 3.141592653589793

# Use a comma separated list to import multiple objects. 
# For example: 
from math import pi, sqrt

# * imports all objects from a module. For example: from math import *
# This is generally discouraged, as it confuses variables in your code with variables in the external module.


# Example: Area Calculation
from math import pi 
radius = int(input("Enter Radius: ")) 

def perim(): 
    return(2*pi*radius) 
    
def area(): 
    return( pi*radius**2) 
    
print("Perimeter:", round(perim(), 2)) 
print("Area:",round(area(), 2)) 


# Example: to import only the sqrt and cos functions from the math module:
from math import sqrt, cos 
print(sqrt(64)) # 83.0
print(cos(0))   # 1.0


# You can import a module or object under a different name using the as keyword. 
# This is mainly used when a module or object has a long or confusing name.
# For example:
from math import sqrt as square_root
print(square_root(100))               # 10.0

# Example:
import math as m      # An error occurs 
print(math.sqrt(25))

# Correct Way
import math as m
print(m.sqrt(100))  # 10.0


# Explains:	
import math 
print(dir(math))
# Output:
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 
 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 
 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 
 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 
 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 
 'tan', 'tanh', 'tau', 'trunc']


# What error is caused by importing an unknown module? - ImportError
import completed_future_code



