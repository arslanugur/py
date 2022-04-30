# 01. USE TYPE HINTING
# Bad Practice
def calc_square(number):
  return number ** 2

# Good Practice
def calc_square(number: float) -> float:
  return number ** 2

# Type hinting does not mean static typing. 
# It is only a hint for other developers and for yourself that indicates, which types are expected and returned.


# 02. USE DOCSTRINGS
def add_function(x, y):
  """Calculates the sum of the two parameters
  
  :param x: the first number
  :param y: the second number
  :return: the sum of both numbers
  """
return x + y

# Docstrings provide a detailed explanation of a function, including its parameters and its return value.

 
# 03. ONE STATEMENT PER LINE
# Bad Practice
if x < 10: 
  print("x is less than 10")

if (x % 2 == 0 or x % 3 == 0) and (x > 20 or x % 5 == 0):
  print("Hello World!")

# Good Practice
if x < 10:
  print("x is less than 10")

cond1 = x % 2 == 0 or x % 3 == 0
cond2 = x > 20 or x % 5 == 0

if cond1 and cond2:
  print("Hello World!")

# One clear statement per line increases the readability of the code.





