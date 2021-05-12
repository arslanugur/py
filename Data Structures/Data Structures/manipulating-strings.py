# String Functions

"""
String have many useful functions:
count(str) returns how many times the str substring appears in the given string.
upper() converts the string to uppercase.
lower() converts the string to lowercase.
replace(old, new) replaces all occurrences of old with new.
len(str) returns the length of the string (number of characters).
"""

# Take a look at this code for examples:
x = "This is some text"

print(x.count("s"))                       # output: 3
print(x.upper())                          # output: THIS IS SOME TEXT
print(x.lower())                          # output: this is some text
print(x.replace("some text", "awesome"))  # output: This is awesome
print(len(x))                             # output: 17

# Note, that these functions return a new string with the corresponding manipulation.


# What is the output of this code?
x = 'abc'
x = x * len(x)      # len(x) = 3  # 'abc' 3 * 'abc' = 'abcabcabc' --It means the string 'abc' will be multiply by the length of the string, 
print(x.count('a')) # output: 3 times 'a' in 'abcabcabc'


