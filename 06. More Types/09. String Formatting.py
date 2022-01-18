# SECTION 1
# So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
# String formatting provides a more powerful way to embed non-strings within strings. 
# String formatting uses a string's format method to substitute a number of arguments in the string.
# Example:
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
# Numbers: 4 5 6

# Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.

# Example:
# Numbers inside curly brackets{} are simply indexes of elements inside .format() bracket. 
msg = "Numbers: {0} {1} {3}".format(4,8,3,6) 
print(msg)  # Numbers: 4 8 6


# A couple of things to note:
# You don't always need numbers in the curly brackets. 
# If you leave them blank, the format items listed are inserted in order, 
# Example:
nums = [4, 5, 6] 
msg = "Numbers: {} {} {}".format(nums[0], nums[1], nums[2])
print(msg) # Numbers: 4 5 6 
# You can use them to change the order of insertion, 
# Example:
nums = [4, 5, 6] 
msg = "Numbers: {2} {0} {0}".format(nums[0], nums[1], nums[2])
print(msg) # Numbers: 6 4 4 2
# Although nums are integers, when they are inserted into a string with format, they are no longer integers, 
# Example:
nums = [4, 5, 6] 
msg = "Numbers: {} {} {}".format(nums[0], nums[1], nums[2])
print(msg)
print(msg[0])
print(msg[9])
print(msg[11])
print(msg[9] + msg[11])
print(int(msg[9]) + int(msg[11]) 
# Numbers: 4 5 6, N, 4, 5, 45, 9
#

# Basically, in "Numbers: {0} {1}".format(nums[0], nums[1]), the nums[0] represents numbers in the list, so for you can replace with, 
# for example, "Numbers: {0} {1}".format(6, 7). This would lead to Numbers: 6 7. 
# The numbers in the curly braces represent the order in the format method. 
# So its "format([position 0], [position 1]) that correspond to the numbers in the curly braces: {0} {1} 
# Btw, you can use strings in the format method, too


# Another one variant of str.format: 
print("MyFourLetters: {0[3]}{0[0]}{1[2]}{1[1]}!".format("Abcd","cat")) # MyFourLetters:dAta!
# More useful variant: 
a='Zero'; b='One'; c="Danger "; 
print("{2}{0[0]}{0[3]}{1[1]}{1[2]}".format(a,b,c)) # Danger Zone

# Example: a newer and cleaner version of this called F-strings. 
x = 12
y = 5
print(f"{x} is greater than {y}!") # 12 is greater than 5!



# Example: string formatting 
nums = [4, 5, 6] 
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2]) 
print(msg)  # Numbers: 6 6 6
msg = "Numbers: {0} {1} {2}".format(nums[2], nums[2], nums[2])
print(msg)  # another way of formating it will show commas - Numbers: 4, 5, 6
msg = "Numbers: %s, %s, %s" % (nums[0], nums[1], nums[2])
print(msg)  # Numbers: 5 4 5 6 4 6
msg = "Numbers: {2} {1} {2} {0} {1} {0}".format(nums[2], nums[0], nums[1])
print(msg)  # IndexError 
msg = "Numbers: {3} {4} {5}".format(nums[2], nums[2], nums[2])
print(msg)  # IndexError



# Example:
nums = [1955, 1998, 2003] 
msg = "Vietnam war: {0} - Kosovo war: {1} - Iraq war: {2}".format(nums[0], nums[1], nums[2]) 
print(msg)      

# Example:
nums = [4, 5, 6]
msg = "Numbers: %s, %s, %s" % (nums[0], nums[1], nums[2])
print(msg)  # Numbers: 4, 5, 6


# Example:
print("{0}{1}{0}".format("abra", "cad"))  # abracadabra


# SECTION 2
# String formatting can also be done with named arguments.
# Example:
a = "{x}, {y}".format(x=5, y=12)
print(a)                # 5, 12

# Example:
a = "{0}, {1}, {x}, {y}".format(1, 3, x=5, y=12) 
print(a)                # 1, 3, 5, 12
# but: 
a = "{0}, {1}, {x}, {y}, {2}".format(1, 3, x=5, y=12,15)
print(a)                # SyntaxError


# Example:
from random import randint 
greetings = ["Hello","Howdy","You smell funny"] 
title = ["Human.", "Trump!" , "Maid."] 
greeting = "{x}, {y}".format(x=greetings[randint(0,2)], y=title[randint(0,2)]) 
print(greeting)

# Example: possible to use a list as an argument 
a = "{x[1]}, {y}".format(x=[5,8,11,52], y=12) 
print(a)                # 8, 12

# Example:
a = "{x}, {y}".format(x=input(), y=input()) 
print(a) 

# String formatting with named arguments is much more understandable than with indexes.

# Example One-line Version:
print("{x}, {y}".format(x=5, y=12)) 

# Example:
var = 83338 
str = ("Hello {0}{ex} %s".format("World", ex="!") % (var))
print(str)        # Hello World! 83338

# Example:
str="{c}, {b}, {a}".format(a=5, b=9, c=7)             # if str = c,b,a, and c=7, b=9, a=5; str= 7,9,5.
print(str)        # 7, 9, 5

# Example:
str="{a},{b},{c}".format(a='python',b='is',c='fun')
print(str)        # python is fun





