# Decision Making and Loops Examples
# Example: Check if a Number is Odd or Even

# In this example, you will learn to check whether a number entered by the user is even or odd.

# A number is even if it is perfectly divisible by 2. 
# When the number is divided by 2, we use the remainder operator % to compute the remainder. 
# If the remainder is not zero, the number is odd.


# Source Code
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
#
# Output 1
# Enter a number: 43
# 43 is Odd

# Output 2
# Enter a number: 18
# 18 is Even

# In this program, we ask the user for the input and check if the number is odd or even. 
# Please note that { } is a replacement field for num.


