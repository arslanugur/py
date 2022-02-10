# Function Examples
# Example: Find HCF or GCD

# In this example, you will learn to find the GCD of two numbers using two different methods: function and loops and, Euclidean algorithm

# The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers is the largest positive integer that perfectly divides the two given numbers. 
# For example, the H.C.F of 12 and 14 is 2.

# Source Code: Using Loops
# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))   # Output: The H.C.F. is 6


# Here, two integers stored in variables num1 and num2 are passed to the compute_hcf() function. 
# The function computes the H.C.F. these two numbers and returns it.

# In the function, we first determine the smaller of the two numbers since the H.C.F can only be less than or equal to the smallest number. 
# We then use a for loop to go from 1 to that number.

# In each iteration, we check if our number perfectly divides both the input numbers. 
# If so, we store the number as H.C.F. At the completion of the loop, we end up with the largest number that perfectly divides both the numbers.

# The above method is easy to understand and implement but not efficient. A much more efficient method to find the H.C.F. is the Euclidean algorithm.

# Euclidean algorithm
# This algorithm is based on the fact that H.C.F. of two numbers divides their difference as well.
# In this algorithm, we divide the greater by smaller and take the remainder. 
# Now, divide the smaller by this remainder. Repeat until the remainder is 0.

# For example, if we want to find the H.C.F. of 54 and 24, we divide 54 by 24. 
# The remainder is 6. Now, we divide 24 by 6 and the remainder is 0. Hence, 6 is the required H.C.F.
# Source Code: Using the Euclidean Algorithm
# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)

# Here we loop until y becomes zero. The statement x, y = y, x % y does swapping of values in Python. Learn more about swapping variables in Python.
# In each iteration, we place the value of y in x and the remainder (x % y) in y, simultaneously. When y becomes zero, we have H.C.F. in x.


