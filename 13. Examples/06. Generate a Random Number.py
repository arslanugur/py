# To generate random number in Python, randint() function is used. This function is defined in random module.

# Source Code
# Program to generate a random number between 0 and 9
import random # importing the random module

print(random.randint(0,9))

# Output: 5

# Note that we may get different output because this program generates random number in range 0 and 9. 
# The syntax of this function is:
random.randint(a,b)

# This returns a number N in the inclusive range [a,b], meaning a <= N <= b, where the endpoints are included in the range.


