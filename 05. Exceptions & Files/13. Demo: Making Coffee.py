# Making Coffee
# Exception Handling

# A coffee vending machine makes 5 types of coffee:
# coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

# Each coffee option has its own number, starting with 0. 
# Write a program that will take a number from the customer as input from the customer and serve the corresponding coffee type. 
# If the customer enters a number that is out of the accepted range, the program should output "Invalid number". 
# Regardless of coffee option result, the program should output "Have a good day" at the end. 


# Sample Input: 7
# Sample Output:
#                Invalid number
#                Have a good day 

# Remember, that the first element of the list has 0 index.

# Code:
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
	#your code goes here
	print(coffee[choice])
except:
	#and here
	print('Invalid number')
finally:
	#and finally here
 print('Have a good day')
#

# Input:  2                     # Input:  0                   # Input:  8
# Output: Espresso              # Output: Café Latte          # Output: Invalid number
#         Have a good day       #         Have a good day     #         Have a good day




