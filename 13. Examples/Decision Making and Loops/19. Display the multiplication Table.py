# Decision Making and Loops Examples
# Example: Display the multiplication Table

# This program displays the multiplication table of variable num (from 1 to 10).

# In the program below, we have used the for loop to display the multiplication table of 12.

# Multiplication table (from 1 to 10) in Python
num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
#

"""
Output

12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
"""

# Here, we have used the for loop along with the range() function to iterate 10 times. 
# The arguments inside the range() function are (1, 11). Meaning, greater than or equal to 1 and less than 11.

# We have displayed the multiplication table of variable num (which is 12 in our case). 
# You can change the value of num in the above program to test for other values.


