# Introduction Examples
# Example: For positive numbers
# Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))  # Output: The square root of 8.000 is 2.828

# In this program, we store the number in num and find the square root using the ** exponent operator. 
# This program works for all positive real numbers. But for negative or complex numbers, it can be done as follows.



# Source code: For real or complex numbers
# Find square root of real or complex numbers
# Importing the complex math module
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
# Output: The square root of (1+2j) is 1.272+0.786j

# In this program, we use the sqrt() function in the cmath (complex math) module.
# Note: If we want to take complex number as input directly, like 3+4j, we have to use the eval() function instead of float().
# The eval() method can be used to convert complex numbers as input to the complex objects in Python. To learn more, visit Python eval() function.


