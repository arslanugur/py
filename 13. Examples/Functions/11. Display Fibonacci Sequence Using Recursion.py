# Function Examples
# Example: to Display Fibonacci Sequence Using Recursion

A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
This means to say the nth term is the sum of (n-1)^th and (n-2)^th term.

# Source Code: Python program to display the Fibonacci sequence
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
#
"""
Output
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34
"""

# Note: To test the program, change the value of nterms.
# In this program, we store the number of terms to be displayed in nterms.
# A recursive function recur_fibo() is used to calculate the nth term of the sequence. 
# We use a for loop to iterate and calculate each term recursively.



