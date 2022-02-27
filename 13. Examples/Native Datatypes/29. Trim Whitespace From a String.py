# Native Datatypes Examples
# Example: to Trim Whitespace From a String


# Example 1: Using strip()
my_string = " Python "
print(my_string.strip())    # Python

# strip() removes the leading and trailing characters including the whitespaces from a string.

# However, if you have characters in the string like '\n' and you want to remove only the whitespaces, 
# you need to specify it explicitly on the strip() method as shown in the following code.

my_string = " \nPython "
print(my_string.strip(" "))   # Python

# Example 2: Using regular expression
import re

my_string  = " Hello Python "
output = re.sub(r'^\s+|\s+$', '', my_string)

print(output)     # Hello python

# In the regex expression, \s denotes the whitespace and \ is the or operation. + one or more occurrences of the pattern left to it.

# Learn more about regex at Python RegEx.


