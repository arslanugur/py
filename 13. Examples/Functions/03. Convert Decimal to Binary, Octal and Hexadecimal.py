# Function Examples
# Example: Convert Decimal to Binary, Octal and Hexadecimal

# The decimal system is the most widely used number system. 
# However, computers only understand binary. 
# Binary, octal and hexadecimal number systems are closely related, and we may require to convert decimal into these systems.

# The decimal system is base 10 (ten symbols, 0-9, are used to represent a number) and similarly, binary is base 2, octal is base 8 and hexadecimal is base 16.

# A number with the prefix 0b is considered binary, 0o is considered octal and 0x as hexadecimal. 
# For example:
60 = 0b11100 = 0o74 = 0x3c

# Source Code: Python program to convert decimal into other number systems
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
"""
Output:
The decimal value of 344 is:
0b101011000 in binary.
0o530 in octal.
0x158 in hexadecimal.
"""

# Note: To test the program for other decimal numbers, change the value of dec in the program.
# In this program, we have used built-in functions bin(), oct() and hex() to convert the given decimal number into respective number systems.
# These functions take an integer (in decimal) and return a string.


