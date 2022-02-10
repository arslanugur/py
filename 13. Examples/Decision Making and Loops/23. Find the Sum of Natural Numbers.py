# Decision Making and Loops Examples
# Example: Find the Sum of Natural Numbers

# In this program, you'll learn to find the sum of n natural numbers using while loop and display it.

# In the program below, we've used an if...else statement in combination with a while loop to calculate the sum of natural numbers up to num.

# Source Code: Sum of natural numbers up to num
num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
# Output: The sum is 136

# Note: To test the program for a different number, change the value of num.

# Initially, the sum is initialized to 0. And, the number is stored in variable num.

# Then, we used the while loop to iterate until num becomes zero. 
# In each iteration of the loop, we have added the num to sum and the value of num is decreased by 1.

# We could have solved the above problem without using a loop by using the following formula.
# n*(n+1)/2
# For example, if n = 16, the sum would be (16*17)/2 = 136.


