###### TRICKS
# Trick 1: Lambda Function vs. Regular Function
# This is a regular function
def Function(Parameter):
  return Parameter

# This is a lambda function
Function = lambda Parameter : Parameter

# Regular Function Example
def Add(a, b):
  return a + b
print(Add(3, 4))  # output: 7

# Lambda Function Example
Add = lambda a, b: a + b
print(Add(3, 4))  # output: 7


# Trick 2: Using Generators Inside Functions
lst = [1, 5, 6, 7, 8]
print(sum(num for num in lst))

# You can also do this
print(sum(range(10)))

# output: 27
#         45

# Trick 3: Checking the Usage of Memory
import sys
num = 2
char = 'Abc'
lst = ['Abc']

print(sys.getsizeof(num))    # 28
print(sys.getsizeof(char))   # 52
print(sys.getsizeof(lst))    # 72


# Trick 4: List Comprehensions
cities = ['Dublin', 'London', 'Oslo']

def visit(city):
  print("Welcome to  "+city)
  for city in cities:
    visit(city)

# output:
# Welcome to Dublin
# Welcome to London
# Welcome to Oslo

# Trick 5: Using the zip() function
name = ["Max", "Mike", "Dustin"]
roll_num = [10, 11, 12]

z = list(zip(name, roll_num))
print(z)     # output: [("Max", 10), ("Mike", 11), ("Dustin", 12)]

# Trick 6: **kwargs
dictionary  = ("a": 5, "b": 8)

def calculate(a, b):
  print(a + b)
  return

calculate(**dictionary)  # output: 13


# Trick 7: One-Liners
# Swap Two Variables
a, b = b, a

# Palindrome Python One Liner
phrase.find(phrase[::-1])

# Read a File
[line.strip() for line in open(filename)]

# Factorial of a Number
reduce(lambda x,y:x*y, range(1,n+1))

# Fibonacci Sequence
lambda x: x if x <=1 else fib(x-1) + fib(x-2)




