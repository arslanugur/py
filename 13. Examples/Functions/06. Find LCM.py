# Function Examples
# Example: to find the LCM of two numbers

# The least common multiple (L.C.M.) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.

# For example, the L.C.M. of 12 and 14 is 84.
# Program to Compute LCM

# Python Program to find the L.C.M. of two input number
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))   # Output: The L.C.M. is 216

# Note: To test this program, change the values of num1 and num2.
# This program stores two number in num1 and num2 respectively. These numbers are passed to the compute_lcm() function. The function returns the L.C.M of two numbers.
# In the function, we first determine the greater of the two numbers since the L.C.M. can only be greater than or equal to the largest number. 
# We then use an infinite while loop to go from that number and beyond.
# In each iteration, we check if both the numbers perfectly divide our number. 
# If so, we store the number as L.C.M. and break from the loop. Otherwise, the number is incremented by 1 and the loop continues.
# The above program is slower to run. 
# We can make it more efficient by using the fact that
# the product of two numbers is equal to the product of the least common multiple and greatest common divisor of those two numbers.

# Number1 * Number2 = L.C.M. * G.C.D.

# Here is a Python program to implement this.
# Program to Compute LCM Using GCD

# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))

# The output of this program is the same as before. We have two functions compute_gcd() and compute_lcm(). 
# We require G.C.D. of the numbers to calculate its L.C.M.

# So, compute_lcm() calls the function compute_gcd() to accomplish this. 
# G.C.D. of two numbers can be calculated efficiently using the Euclidean algorithm.

# Learn more about methods to calculate G.C.D in Python.


