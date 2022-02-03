## INTRO
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


## DICTIONARIES
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

## DICTIONARY FUNCTIONS
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



## TUPLES
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

## TUPLE UNPACKING
# Tuple unpacking allows you to assign each item in a collection to a variable.
# Example:
numbers = (1, 2, 3)
a, b, c = numbers
print(a) # 1
print(b) # 2
print(c) # 3

# This can be also used to swap variables by doing a, b = b, a , since b, a 
# on the right hand side forms the tuple (b, a) which is then unpacked.

# You can also unpack with list: a, b, c = [1, 2, 3]

# Example: to swap two variables.
x, y = [1, 2]
x, y = y, x
# output: 1
# Firstly, a list can be changed x, y = [1, 2] 
# x = 1 and y = 2 (The value of x is packed to 1 and y to 2. )
# x, y is 1 before 2 
# x, is at index 0, so 1 
# y, is at index 1, so 2 
# Remember again list can be changed, so: 
# If the list x, y = y, x 
# it means x become y and y = x 
# so x is now 2 and y is now 1 The question is to give the value of y, so y=1


# To swap the value of two variable. There are two four way of doing so
# First way >>>
x = 10
y = 5

temp = x
x = y
y = temp

print("value of x is",x) # value of x is 5
print("value of y is",y) # value of y is 10

# Second way >>>
x = 20
y = 15

x = x^y
y = x^y
x = x^y

print("value of x is",x) # value of x is 15
print("value of y is",y) # value of y is 20

# Third way >>>
x = 30
y = 25

x,y = y,x

print("value of x is",x) # value of x is 25
print("value of y is",y) # value of y is 30

# Fourth way >>>
x = 40
y = 35

x = x + y
y = x - y
x = x - y

print("value of x is",x) # value of x is 35
print("value of y is",y) # value of y is 40


# A variable that is prefaced with an asterisk (*) takes all values 
# from the collection that are left over from the other variables.
# Example:
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a) # 1
print(b) # 2
print(c) # [3, 4, 5, 6, 7, 8]
print(d) # 9
# c will get assigned the values 3 to 8.

# Example:
a, b, c, d, *e, f, g = range(20) # range(20) means 0 to 20 --> 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 
# a, b, c, d, *e, f, g, = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 
# hence, a = 0 b = 1 c = 2 d = 3 *e= 4 to 17, f = 18, g = 19 len(e) means length of the e variable 

print(len(e)) # 14


## SETS
# Sets are similar to lists or dictionaries.
# They are created using curly braces, and are unordered, which means that they can't be indexed.

# Due to the way they're stored, 
# it's faster to check whether an item is part of a set using the in operator, rather than part of a list.

# Example:
num_set = {1, 2, 3, 4, 5}

print(3 in num_set) # True

# Sets cannot contain duplicate elements.

"""
Use sets when: 
      - You want values to be unique 
      - When order does not matter Sets: 
            Unordered, Unindexed but Hashed 
            To create an empty set: 
                  >> not_set = { } <-- dictionary
                  >> my_set = set( ) <-- set
"""   

# Example: The speed difference for the different collection types is huge. And not only sets are fast for lookups.
import timeit

mylist = []
mydict = {}
mytuple = ()
myset = {}

num_rounds = 1
num_size = 2

# create data
for i in range(num_size):
	mylist.append(i)
	mydict[i] = i
mytuple = tuple(mylist)
myset = set(mylist)

"""
Rounds:  1
Length List:  2
Length Dict:  2
Length Tuple:  2
Length Set:  2
List Time:   2.7995556592941284e-06
Dict Time:   1.7993152141571045e-06
Tuple Time:  1.7005950212478638e-06
Set Time:    1.4994293451309204e-06
"""

# Every elements in a set are unique and obviously immutable ( but sets are mutable). 
# The runtime to find any element in a set is O(1) (on an average; 
# but in the worst case it'll be O(n)), whereas in list, it is O(n). 
# So to check an element in list ( of n length) python has to do work equal to some factor of n; 
# but in case of a set it is some constant. 
# And keep this in mind, new = {} creates an empty dictionary; 
# to create an empty set you have to use, new = set().


# Sets are unordered. Also, Sets are faster, unique, mutable.
# For example: 
# If there are 3 elememts, you will get {1, 2, 3} OR {1, 3, 2} OR {2, 1, 3} OR {2, 3, 1} OR {3, 1, 2} Or {3, 2, 1}. 
# The orders are completely random and unordered. 
# Therefore, don't be surprised when your set outputs the values in different order.

# Example:
set_1 = {"a", "b", "a"} 
set_2 = {"a", "b"} 
print (set_1 == set_2) # True

# https://en.m.wikipedia.org/wiki/Set_theory

# Example:
letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print(1) # "e" not in letters ---> True, "e" in letters ---> False
else: 
  print(2) #output: 1


# You can use the add() function to add new items to the set, and remove() to delete a specific element:
# Example:
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)  # {1, 2, 3, 4, 5, 6}
nums.add(-7)
nums.remove(3)
print(nums) # {1, 2, 4, 5, 6, -7}

# Duplicate elements will automatically get removed from the set. 

# The len() function can be used to return the number of elements of a set.

# Example:
num1 = {1, 2, 3} 
num2 = { 1, 4, 5, 6} 
print(num1.union(num2)) #output: {1, 2, 3, 4, 5, 6}

# https://www.w3schools.com/python/ref_set_add.asp
# https://www.w3schools.com/PYTHON/ref_set_remove.asp

# Example: to create a set, add the letter "z" to it, and print its length.
nums = {"a", "b", "c", "d"} # Curly braces mark a set. 
nums.add("z") # use .add function to add elements. 
print(len(nums)) # like list, use len to get length.



# Sets can be combined using mathematical operations.
# The union operator | combines two sets to form a new one containing items in either.
# The intersection operator & gets items only in both.
# The difference operator - gets items in the first set but not in the second.
# The symmetric difference operator ^ gets items in either set, but not both. 

# Example:
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second) # {4, 5, 6}
print(first - second) # {1, 2, 3}
print(second - first) # {8, 9, 7}
print(first ^ second) # {1, 2, 3, 7, 8, 9}

# Sets are great tools for quick filters if you take the time to learn the operators. 
# Otherwise, you end up iterating through lists constantly

# Example:
a = {0,1,2,3,4,5,6,7}
b = {5,6,7,8,9,10}

print(a | b) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# joined and remove commons
print("\n \n")
print(a & b) # {5, 6, 7}
# print commons only
print("\n \n")
print(a - b) # {0, 1, 2, 3, 4}
# remove mutual of b from a and print a
print("\n \n")
print(b - a) # {8, 9, 10}
# remove mutual of a from b and print b
print("\n \n")
print(a ^ b) # {0, 1, 2, 3, 4, 8, 9, 10}
#joined, remove commons and print different

# Set Methods
a = {1,2,3} 
b = {2,3,4} 

a.union(b) 
a.difference(b) 
a.symmetric_difference(b) 
a.update(b) 
a.difference_update(b) 
a.symmetric_difference_update(b)

"""
a | b == b | a 
a & b == b & a 
a ^ b == b ^ a 
a - b != b - a
"""

# Example:
a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b) #output: 3 (intersection --> &)



## LIST COMPREHENSIONS










