# Bank card PIN System
# Exception Handling

# Explanation:
# We need to create a program that allows users to create their own PIN codes for their bank cards. 
# Each PIN code consists of digits. 
# Complete the program so that when the user enters a character, 
# the program stops and outputs "Please enter a number" and when the user enters only digits, the program outputs "PIN code is created".

# Sample Input: 44a5
# Sample Output: Please enter a number

# Note:
# Recall int() function, that occurs an error when the argument is not a number.


# Code:
pin = input()
try:
	#your code goes here
	int(pin)                            # input: 1584                     # input: hh88                     # input: 8845
	print("PIN code is created")        # output: PIN code is created     # output: Please enter a number   # output: PIN code is created
except ValueError:
	#and here
	print("Please enter a number")
#


