# Native Datatypes Examples
# Example: to Parse a String to a Float or Int

# Example 1: Parse string into integer
balance_str = "1500"
balance_int = int(balance_str)

# print the type
print(type(balance_int))

# print the value
print(balance_int)

# Output
# <class 'int'>
# 1500

# int() can be used to parse a string to an integer. The argument passed balance_int is the string. 
# As shown in the above example, you can see the type of the string changed to int.

# Note: The string must be a numeral value.
# Example 2: Parse string into float
balance_str = "1500.4"
balance_float = float(balance_str)

# print the type
print(type(balance_float))

# print the value
print(balance_float)

# Output
# <class 'float'>
# 1500.4

# float() can be used to parse a string to an integer. Similar to Example 1, the string is passed as an argument to float().
# Example 3: A string float numeral into integer
balance_str = "1500.34"
balance_int = int(float(balance_str))

# print the type
print(type(balance_int))

# print the value
print(balance_int)

# Output
# <class 'int'>
# 1500

# If the string is a float numeral, you can convert it into a float type using float(), and then parse it to an integer using int().



