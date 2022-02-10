# Function Examples
# Example: to Find Sum of Natural Numbers Using Recursion

# In the program below, we've used a recursive function recur_sum() to compute the sum up to the given number.
# Source Code: Python program to find the sum of natural using recursive function

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num)) # Output: The sum is 136
# 


# Note: To test the program for another number, change the value of num.



