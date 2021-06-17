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
"""
output:
Traceback (most recent call last):
  File "file0.py", line 1, in <module>
    bad_dict = {
TypeError: unhashable type: 'list'
"""
# This means that you can use strings, integers, booleans, and any other immutable type as dictionary keys.

# Another Way:
bad_dict = { 
      tuple([1, 2, 3]): "one two three",
}
# but that's because the tuple is created from the list, and then it's stored as a key. The dict never gets to see the list
#  the point is to use immutable tuple. You can create it either this way: tuple([1,2,3]) or this way: (1,2,3).

"""
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
"""

# Demo: Car Data
# You are working at a car dealership and store the car data in a dictionary:
car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red'
} 
# Your program needs to take the key as input and output the corresponding value.
"""
Sample Input: year
Sample Output: 2018
"""
# Code:
car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

print(car[input()])
"""
Input: brand
Output: BMW
"""

# DICTIONARY FUNCTIONS
# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
# Example:
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
"""
TRUE
FALSE
TRUE
"""

# Example:
num = { 1:"one", 2:"two", 3:"three" } 
print(1 in num) #True
print(2 not in num) #False
print(4 not in num) #True
print("three" in num) #False
print("one" in num.values()) #True

# Dict Methods
Dict.update('hi') 
Dict.keys() 
Dict.values() 
list(Dict.keys()),print(Dict.sort()) 
Dict.pop('hi') 
Dict.popitem() #return randomly 
Dict.str() #to be printable text 
Dict.len() 
Dict.cmp(dict1,dict2) #comparing

# to print "Yes" if the key 112 is present in the dictionary named "pairs".
if 112 in pairs:   # key is "112" and dict is "pairs"
      print("Yes") # answer will be if 112 in pairs : print("Yes")      

# A useful dictionary function is get. 
# It does the same thing as indexing, 
# but if the key is not found in the dictionary it returns another specified value instead.
# Example:
pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))

print()

for i in pairs.keys():
    print(i)


print()
"""
[2, 3, 4]
42
not found

1
orange
12

45
31
11
"""
# To determine how many items a dictionary has, use the len() function.

# Example: the sum of dict values 
lew = { 'a' : 5 , 'b' : 7 , 'c' : 9 } 
print (sum(lew.values())) #output: 21

# Example:
fib = {1:1, 2:1, 3:2, 4:3}
print(fib.get(4, 0) + fib.get(7, 5))
# output:     3     +         5     = 8

# Example:
fib={
    1:10, 2:20, 3:30, 4:40
}
print(fib.get(4,0) + fib.get(7,5))    # 45
print(fib.get(2,5) + fib.get(17,11))  # 31
print(fib.get(1,3000) + fib.get(5,1)) # 11

# Example:
fb = {1:"one" ,2:"two", 3:"three" } 
print(fb.get(3,1) + fb.get(2,2))
# output: threetwo

# Example:
d={1:"apple",2:"ball"} 
print(d.get(1, "fruit" )) #output: apple 
print(d.get(3,"animal"))  #output: animal



# TUPLES
# Tuples are very similar to lists, except that they are immutable (they cannot be changed).
# Also, they are created using parentheses, rather than square brackets.
# Example:
words = ("spam", "eggs", "sausages")

# You can access the values in the tuple with their index, just as you did with lists:
words = ("spam", "eggs", "sausages",)
print(words[0]) # output: spam

# Trying to reassign a value in a tuple causes an error. 
words = ("spam", "eggs", "sausages",)
words[1] = "cheese" # error

# Like lists and dictionaries, tuples can be nested within each other.

# Tuples are generally immutable and they are small in size than lists. 
# Tuples are great for storing stuff that mustn't be changed throughout the program. 
# We can create an empty tuple by this. my_tuple = () 
# And we actually do not need parentheses to create a tuple. 
# Example:
my_tuple = (1,2,3,4,5,6)
my_tuple = list(my_tuple)
my_tuple[1] = "Two"
print(tuple(my_tuple))
# output: (1, 'Two', 3, 4, 5, 6)

# Example:
words = (1, [2, 3], 4) 
print(words) # output: (1, [2, 3], 4) 
words[1][0] = 55 
print(words) # output: (1, [55, 3], 4)

# Example:
words = ("spam", "eggs", "sausages")
print(words[0]) # spam
print(words[1]) # eggs
print(words[-2]) # eggs

print(type(words[1])) # <class 'str'>
print(type(words)) # <class 'tuple'>

print(id(words[0])) # randomly 139812822421424
print(len(words)) # 3

try:
    words[0] = "maps"
    print(id(words[0]))
except: "immutable type"
    #print("Error, immutable type")

print()

list1 = [1, 2, 3]
print(list1) # [1, 2, 3]
print(type(list1)) # <class 'list'>

list2 = tuple(list1)
print(list2) # (1, 2, 3)
print(type(list2)) # <class 'tuple'>

# Examples: to create a list, dictionary, and tuple:
# list
list = ["one", "two"]
# dictionary 
dict = {1:"one", 2:"two"}
# tuple 
tp = ("one", "two")

# Examples:
# Here, list does what it's supposed to.
print(list('hello')) # output: ['h', 'e', 'l', 'l', 'o']

# We redefine list.
list = lambda x: x[::-1] # output: olleh
print(list('hello'))

# Let's clean up this mess
del list


# Tuples can be created without the parentheses by just separating the values with commas.
# Examples:
my_tuple = "one", "two", "three"
print(my_tuple[0]) #output: one
# Tuples are faster than lists, but they cannot be changed.


# Example:
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
expression = input()
for i in contacts:
    
    for y in i:
        if y == expression:
            print(y, "is", i[1])
        break
    else:
        if y != expression:
            print("Not found")
# Input: Bob Output: Bob is 18


# Examples:
list = ["item1", "item2", "item3"]
#start coun from 1
print(list[1]) #output: item2
print("\n \n")


#start count from 1 but defined initialy
dic = {1:'one', 2:'to', 3:'three', 4:2, 5:" ", 6:'and', 7:'seven'}
print(dic[1]+dic[5]+dic[2]+dic[5]+dic[7]) #output: one to seven
print("\n \n")


#start count from zero
tup = (0,'one',2,'three',4,'five')
print(tup[1]) #output: one
print("\n \n")

unpa = [1,2,3,3,3,3,3,3,3,4]
a, b, *c, d = unpa
print(d) #output: 4
print(c) #output: [3, 3, 3, 3, 3, 3, 3]
print(b) #output: 2
print(a) #output: 1

# Example: Nested Tuple
tuple = (1, (1, 2, 3))
print(tuple[1]) # output: (1, 2, 3)
# tuple[0] = 1 
# tuple[1] = (1,2,3) 
# tuple[1][0] = 1

# TUPLE UNPACKING
