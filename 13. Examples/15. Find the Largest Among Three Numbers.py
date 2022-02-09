# Decision Making and Loops Examples:
# Example: Find the Largest Among Three Numbers

# In this program, you'll learn to find the largest among three numbers using if else and display it.

# In the program below, the three numbers are stored in num1, num2 and num3 respectively. 
# We've used the if...elif...else ladder to find the largest among the three and display it.
# Source Code:
# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
# 
# Output: The largest number is 14.0
# Note: To test the program, change the values of num1, num2 and num3.


