# Py Built-in Methods

# 01. abs(x)
# Return the absolute value of a number. The argument may be an int, a floating point number, or an object implementing __abs__(x).
# If the argument is a complex number, its magnitude is returned
a = abs(-7.25)
print(a)      # 7.25

x = abs(3+5j)
print(x)      # 5.8309..


# 02. all(iterable)
# Return True if all elements of the iterable are true (or if the iterable is empty)
myList1=[0, 1, 1]
myList2=[True, "a", 10]

print(all(myList1))   # False
print(all(myList2))   # True


# 03. any(iterable)
# Return True if any element of the iterable is true. If the iterable is empty, return False.
myList1=[0, 1, 1]
myList2=[True, "a", 10]

print(any(myList1))   # True
print(any(myList2))   # True


# 04. ascii(object)
# Returns a string containing a printable representation of an object for non-alphabets or invisible characters such as tab, carriage return, form feed etc.
x=ascii("My name is Ståle")
print(x)  # 'My name is St\xe5le'


# 05. bin(x)
# Convert an integer number to a binary string prefixed with "0b".
x=bin(36)
print(x)  # 0b100100
y=bin(1)
print(y)  # 0b1



# 06. bool(x)
# Converts a value to the bool class object containing either True or False
x=bool(1) # int
print(x)  # True
L=[]
y=bool(L) # Empty List
print(y)  # False
z=bool("Abc") # String
print(z)    # True



# 07. callable(object)
# The callable() method returns True if the object passed is callable, Fallse if not.
def x():
  a=5
  
print(callable(x))  # True
y=5
print(callable(y))  # False


# 08. chr(i)
# Return the string representing a character whose Unicode code point is the integer i.
# For Example, chr(97) returns the string 'a', while chr(8364) returns the string '$'. This is the inverse of ord().
x=chr(97)
print(x)  # a
y=chr(8364)
print(y)  # Euro Symbol

breakpoint()
bytearray()
bytes()
classmethod()
compile()
complex()           clear()       copy()

delattr()
dict()
dir()
divmod()

enumerate()
eval()
exec()

filter()
float()
format()
frozenset()

getattr()
globals()

hasattr()
hash()
help()
hex()

id()
input()
int()
isinstance()
issubclass()
iter()

len()
list()
locals()

map()
max()
min()
next()

oct()
open()
ord()
objects()

pow()
print()
range()
reversed()
round()

set()
slice()
sorted()
str()
sum()
super()

tuple()
type()

zip()



