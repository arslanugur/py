# list = [ ]
# dict = { }
# tp = ( )

# List Slicing --> [start:stop:increment/decrement]

# List slices provide a more advanced way of retrieving values from a list. 
# Basic list slicing involves indexing a list with two colon-separated integers. 
# This returns a new list containing all the values in the old list between the indices.
# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])       # [4, 9, 16, 25]
print(squares[3:8])       # [9, 16, 25, 36, 49]
print(squares[0:1])       # [0]

# Like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.


# Tip: To reverse the whole list use mylist[::-1] 
# Example:
mylist = [1, 2, 3, 4]
print(mylist[::-1])   # [4, 3, 2, 1] 
# The slicing of a list takes three arguments separated by colon. they are optional. 
# lower limit:upper limit: steps by default (if you don't specify) 
# lower limit is at index 0, upper limit is at the last value and steps is +1 
# so using ::-1 as in the example means don't slice anything off but give in reverse order. 


# STRINGS are essentially LISTS (or TUPLES to be more precise) in Python.
strn = "There can be only one"  # input 
print(strn[::-1])               # output: eno ylno eb nac erehT


# A nice little trick for dealing with ranges that are inclusive of the first value 
# but exclusive of last is to do the last minus the initial to know how many elements are in the range. 
# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])       # [4, 9, 16, 25]           6 - 2 = 4 
print(squares[3:8])       # [9, 16, 25, 36, 49]      8 - 3 = 5 
print(squares[0:1])       # [0]                      1 - 0 = 1 
# When you print the range you end up with [4, 9, 16, 25] which is 4 elements, [9, 16, 25, 36, 49] is 5 and [0] is 1. 
# This is a nice little trick when you're trying to trace code and figure out the output or something.



# Worth adding here as a reminder is that when you create a list and assign it to a variable, 
# you have to think of this variable as POINTING to the list rather than being EQUAL to it. 
# Whenever you assign another variable to the one you already have assigned the list, both variables point to THE SAME list object. 
# Any list modifications will affect ALL variables pointing to it. 
# Example: 
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
quadras = squares 
squares[9] = 100 
print(quadras) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 100]



# Example: List Slicing
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[2:6])           # [4, 9, 16, 25] 
print(squares[3:8])           # [9, 16, 25, 36, 49] 
print(squares[0:1])           # [0]
print(squares[::-1])          # [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
print(squares[::2])           # [0, 4, 16, 36, 64]  
print(squares[::-2])          # [81, 49, 25, 9, 1]
print(squares[3:9:2])         # [9, 25, 49]
print(squares[7:1:-1])        # [49, 36, 25, 16, 9, 4]
print(squares[1:8:3])         # [1, 16, 49] 




# Example:
my_list = [0, 1, 2, "skip", 6, 7, 8, 9] 
# you want to fill in the missing numbers in the sequence. 
# Your first attempt might be:
my_list[3] = [3, 4, 5] 
# But this would make the value of my_list be [0, 1, 2, [3, 4, 5], 6, 7, 8, 9], and that list in the middle of a list would cause problems. 
# But using the following list slice: my_list[3:4] = [3, 4, 5] 
# Now the value of my list is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], which is what we originally wanted! 
# you could use list slices that way at the following website:
# http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html


# You can also pass a value to a variable and then use that variable for list slicing. 
# Example: 
list = ["a","b","c"]
d = 0
e = 2
list_new = list[d:e]
print(list_new) # ['a', 'b']


# Example:
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])         # [16, 25, 36]


# Sample:
x = first index 
y = second index
print(list[x:y])  # prints from index x to index y - 1



# If the first number in a slice is omitted, it is taken to be the start of the list.
# If the second number is omitted, it is taken to be the end.
# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])     # [0, 1, 4, 9, 16, 25, 36]
print(squares[7:])     # [49, 64, 81]
# Slicing can also be done on tuples.

# Notice the colon before and after the 7 
# Before - means count all before 7 
# After - means count all after 7


# If you use any number biggger than last key, still the result is same
print(squares[7:100]) # [49,64,81]
print(squares[7:])    # [49,64,81]
# Also negatives work just fine till the second key dosn't cross the first key to the left: 
print(squares[7:-1])  # [49,64]
print(squares[7:-5])  # []


# Why the first index of a list was included and the second was excluded. 
# Realised that this allows a nice way to recompose the full list: 
mylist = [0,1,2,3]
part1 = [:2]
part2 = [2:]
print(part1 + part2) # [0,1,2,3]



------------------------------















