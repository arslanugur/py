# Function Examples
# Example: to Convert Decimal to Binary Using Recursion

# Decimal number is converted into binary by dividing the number successively by 2 and printing the remainder in reverse order.
"""
2 / 34    0
2 / 17    1
2 / 8     0
2 / 4     0
2 / 2     0
2 / 1     1 
"""
# (34)_10 = (100010)_2

# Source Code: Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 34

convertToBinary(dec)
print()     # Output: 100010

# You can change the variable dec in the above program and run it to test out for other values.

# This program works only for whole numbers. It doesn't work for real numbers having fractional values such as: 25.5, 45.64 and so on. 
# We encourage you to create Python program that converts decimal numbers to binary for all real numbers on your own.



