# Decision Making and Loops Examples:
# Example: Check Armstrong Number

# In this example, you will learn to check whether an n-digit integer is an Armstrong number or not.

# A positive integer is called an Armstrong number of order n if
## abcd... = a^n + b^n + c^n + d^n + ...

# In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:
## 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

# Source Code: Check Armstrong number (for 3 digits)
# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
#
"""
Output 1

Enter a number: 663
663 is not an Armstrong number

Output 2

Enter a number: 407
407 is an Armstrong number
"""

# Here, we ask the user for a number and check if it is an Armstrong number.

# We need to calculate the sum of the cube of each digit. 
# So, we initialize the sum to 0 and obtain each digit number by using the modulus operator %. 
# The remainder of a number when it is divided by 10 is the last digit of that number. We take the cubes using exponent operator.

# Finally, we compare the sum with the original number and conclude that it is Armstrong number if they are equal.



# Source Code: Check Armstrong number of n digits
num = 1634

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
#
# You can change the value of num in the source code and run again to test it.



