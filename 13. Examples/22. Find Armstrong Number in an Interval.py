# Decision Making and Loops Examples
# Example: Find Armstrong Number in an Interval

# In this example, we will learn to find all the Armstrong numbers present in between two intervals in Python.

# A positive integer is called an Armstrong number of order n if
# abcd... = a^n + b^n + c^n + d^n + ...

# For example,
# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

# Visit this page to learn how you can check whether a number is an Armstrong number or not in Python.


# Source Code: Program to check Armstrong numbers in a certain interval
lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
#
"""
Output:
153
370
371
407
1634
"""
# Here, we have set the lower limit 100 in variable lower and upper limit 2000 in variable upper. 
# We have used for loop to iterate from variable lower to upper. 
# In iteration, the value of lower is increased by 1 and checked whether it is an Armstrong number or not.

# You can change the range and test out by changing the variables lower and upper. 
# Note, the variable lower should be lower than upper for this program to work properly.




