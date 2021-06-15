# INTRO
# About Python collection types, lambda functions, generators, decorators, OOP, and much more.
# To build real-world projects and solve several programming challenges. 

      #Code:
n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:   # n[1:3] means n is equal to 4,6 
  res *= x         # res*=x means res=res*x

print(res)         # output: 24

# The loop runs for first time and take the value of x as 4
# So,the value of res changed to 1*4=4 .And secondly x=6
# So, the value of res will be 4*6=24. Lastly res=24

# https://blog.devgenius.io/indexing-vs-slicing-in-python-de01cd99c499#:~:text=What%20are%20Indexing%20and%20Slicing


# DICTIONARIES
# Python provides a number of built-in collection types, to store multiple values.
# Lists are one of these collection types, and they allow you to store indexed values:
x = ['hi', 'hello', 'welcome']
print(x[2]) # output: welcome

# Each item of a list has an index, which is automatically set.
# Dictionaries are another collection type and allow you to map arbitrary keys to values.
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
# Example:
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])     # output: 24
print(ages["Mary"])     #         42

# Each element in a dictionary is represented by a key:value pair.

# Code:
x = [ 'Dave', 'Marry', 'John'] 
y = [24, 42, 58] 
d = dict(zip(x, y)) 
print(d['Marry'])       # output: 42

# Code:
cars = {
   "BMW": "blue",
   "Volvo": "red"} 

# Only immutable objects can be used as keys to dictionaries. 
     # Immutable objects are those that can't be changed.
# So far, the only mutable objects you've come across are lists and dictionaries.

bad_dict = {
    [1, 2, 3]: "one two three", 
}
'''
output:
Traceback (most recent call last):
  File "file0.py", line 1, in <module>
    bad_dict = {
TypeError: unhashable type: 'list'
'''
# This means that you can use strings, integers, booleans, and any other immutable type as dictionary keys.

# Another Way:
bad_dict = { 
      tuple([1, 2, 3]): "one two three",
}
# but that's because the tuple is created from the list, and then it's stored as a key. The dict never gets to see the list
#  the point is to use immutable tuple. You can create it either this way: tuple([1,2,3]) or this way: (1,2,3).

'''
A dictionary key must be of a type that is immutable.
# Immutable (Valid keys): 
String ""
Numbers (int, float)
Tuple  ()
Boolean
Frozenset 

# Mutable (Invalid keys):
List []
Dictionary {:}
Sets {}
'''

# Demo: Car Data
# You are working at a car dealership and store the car data in a dictionary:
car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red'
} 
# Your program needs to take the key as input and output the corresponding value.
'''
Sample Input: year
Sample Output: 2018
'''
# Code:
car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

print(car[input()])
'''
Input: brand
Output: BMW
'''

# DICTIONARY FUNCTIONS
