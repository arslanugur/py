# You have already seen exceptions in previous code. They occur when something goes wrong, due to incorrect code or input. 
# When an exception occurs, the program immediately stops.
# The following code produces the ZeroDivisionError exception by trying to divide 7 by 0. 
num1 = 7
num2 = 0
print(num1/num2)  # ZeroDivisionError


# How to avoid the exception with a polite user warning: 
num1 = 7 
num2 = 0 
if num2 != 0: 
  print(num1/num2) 
else: 
  print("You are trying to divide a number by zero")
#

# The two main types are syntax errors and exceptions. 
# With a syntax error, the code can't run at all. 
# With an exception, the code runs until it gets to the exception and then stops. 
# You can handle exceptions with 'try' and 'except' (later in the course) but you can't handle syntax errors. 

# https://docs.python.org/3.8/tutorial/errors.html

# An error will stop the code from compiling and executing. 
# An exception produces an error during execution but doesn't necessarily stop compilation.
# An exception is an error specifically caused by a flaw in your code mostly from user input

# Different exceptions are raised for different reasons.
# Common exceptions:
#   ImportError: an import fails;
#   IndexError: a list is indexed with an out-of-range number;
#   NameError: an unknown variable is used;
#   SyntaxError: the code can't be parsed properly;
#   TypeError: a function is called on a value of an inappropriate type;
#   ValueError: a function is called on a value of the correct type, but with an inappropriate value.

# Python has several other built-in exceptions, such as ZeroDivisionError and OSError. Third-party libraries also often define their own exceptions.
# https://docs.python.org/3.7/library/exceptions.html

# Examples:
#   ImportError: an import fails; 
import some_module 

#   IndexError: a list is indexed with an out-of-range number; 
l=[1,2,3,4,5] 
print(l[5]) 

#   NameError: an unknown variable is used; 
print(k) 

#   SyntaxError: the code cannot be parsed properly; 
str=Hello world 

#   TypeError: a function is called on a value of an inappropriate type;
from math import sqrt 
print(sqrt("abc")) 

#   ValueError: a function is called on a value of the correct type, but with an inappropriate value; 
from math import sqrt 
print(sqrt(-23))


# TypeError exception is raised by this code  # String + Integer = Type Error
print("7" + 4)
# you can fix the code by declaring the 7 an integer. which converts the string type to integer ie: 
print(int("7") + 4) # output: 11


