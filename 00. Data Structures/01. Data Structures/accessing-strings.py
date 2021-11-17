# Accessing Strings

# Strings can be thought of as a sequence of characters. Each character in the string has its unique position (or index).
# You can access a character of a string using its index:
str = "Hello"
print(str[2])   # output: l

# The code above accesses the 3rd character of the string. The index starts from 0, meaning that the first character has the index 0.


# You can also use negative indices, which access the characters of the string counting from the end.
# For example:
x = "Hello"
print(x[-1])  # output: o

# The code above accesses the last character of the string.


# You can loop through the characters in a string using a for loop:
x = "Hey"
for c in x:
    print(c)
# output: h
#         e
#         y

# During each iteration, the variable c will represent the current character of the string.



# to create a valid for loop:
text = "some text goes here"
  for x in text:
   print(x)

  
