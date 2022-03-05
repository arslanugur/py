# Introduction Examples
# Topics: Python Input, Output and Import, Python Data Types, Python Operators

# Example 1: Add Two Numbers
# This program adds two numbers
num1 = 1.5
num2 = 6.3

sum = num1 + num2 # Add two numbers
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  # Display the sum
# Output: The sum of 1.5 and 6.3 is 7.8



# Example 2: Add Two Numbers With User Input
# The program below calculates the sum of two numbers entered by the user..

# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2) # Add two numbers

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  # Display the sum

# Output:
# Enter first number: 1.5
# Enter second number: 6.3
# The sum of 1.5 and 6.3 is 7.8

# In this program, we asked the user to enter two numbers and this program displays the sum of two numbers entered by user.

# We use the built-in function input() to take the input. 
# Since, input() returns a string, we convert the string into number using the float() function. Then, the numbers are added.

# Alternative to this, we can perform this addition in a single statement without using any variables as follows.
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))
# Although this program uses no variable (memory efficient), it is harder to read.


