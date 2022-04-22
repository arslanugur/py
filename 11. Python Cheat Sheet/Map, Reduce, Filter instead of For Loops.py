# How to replace your py for loops with Map, Filter & Reduce

# For Loops are a Swiss army knife for problem solving,
# but, when it comes to scanning code to get a quick read of what you have done, they can be overwhelming.

# Three techniques - map, filter, reduce - help remedy the for loop mania by offering functional altternatives that describe why you are iterating.

# Don't do this every time
list1 = [1,2,3,4,5]
for i in list1:
  if i % 2 == 0:
    print(i)      # 2, 4
#





# map() function
# this func returns a map object(which is an iterator) of the results after applying the given func to each item of a given iterable (list, tuple etc.)
# Code with For loop
def add(n):
  return n + n

number = (1, 2, 3, 4)
for i in numbers:
  print(add(i))
#

# Syntax: map(fun, iter)
# Code 1 with Map() function
def add(n):
  return n + n

number = (1, 2, 3, 4)
result = map(add, numbers)
print(list(result))       # 2 4 6 8

# Code 2 with Map() function
number = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))       # 2 4 6 8




# filter() function
# this method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# Syntax: filter(function, sequence)
# Code 1:
# function that are filters vowel
def fun(var):
  letters = ['a','e','i','o','u']
  return True if var in letters else False

string = list('python')
filtered = filter(fun, string)
print(tuple(filtered))    # 'o'

# Code 2:
seq = [0,1,2,3,5,8,13]
result = filter(lambda x: x%2 == 0, seq)
print(list(result))     # [0, 2, 8]





# reduce() function
# this function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
# this function is defined in "functools" module.
# Example with For loop
# add the list of elements
def sumTwo(a,b):
  return a + b

val = [1, 2, 3, 4]
res = 0
for i in val:
  res = sumTwo(i, res)
print(res)    # 10

# Syntax: reduce(fun, seq)
# Code 1 with reduce()
from functools import reduce
# returns the sum of two elements
def sumTwo(a,b):
  return a+b

result = reduce(sumTwo, [1, 2, 3, 4])
print(result)     # 10

# Code 2 with reduce()
# initializing list
lis = [1,3,5,6,2]

# Using reduce to compute sum of list
print(functools.reduce(lambda a,b: a + b, lis))   # 17

# Using reduce to compute maximum element from the list
print(functools.reduce(lambda a,b: a if a > b else b, lis))   # 6




# Bonus
# enumerate() function
# Often, when dealing with iterators, we also get a need to keep a count of iterations.
# Py eases the programmer's task by providing a built-in function enumerate() for this task.
# This method adds a counter to an iterable and returns it in a form of enumerating object.
# This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.
# Example
l1 = ["one", "two", "three"]
s1 = "py"

print(list(enumerate(l1)))      # [(0, 'one'),(1, 'two'),(2, 'three')]

# changing start index to 10 from 0
print(list(enumerate(s1, 10)))      # [(10, 'p'), (11, 'y')]

for enu in numerate(l1):
  print(enu)
# Output:
# (0, 'one')
# (1, 'two')
# (2, 'three')




