# Decision Making and Loops Examples
# Example: Print all prime numbers within an interval using for loops and display it.

# A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
# 2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6.

# Source Code
# Python program to display all the prime numbers within an interval
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
#
# Output
# Prime numbers between 900 and 1000 are: 907, 911 ... 991, 997

# Here, we store the interval as lower for lower interval and upper for upper interval, and find prime numbers in that range. 
# Visit this page to learn how to check whether a number is prime or not.


