# Native Datatypes Examples
# Example: to Check Whether a String is Palindrome or Not

# A palindrome is a string that is the same read forward or backward.

# For example, "dad" is the same in forward or reverse direction. 
# Another example is "aibohphobia", which literally means, an irritable fear of palindromes.
# Source Code
# Program to check if a string is palindrome or not
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
#
# Output: The string is a palindrome.

# Note: To test the program, change the value of my_str in the program.

# In this program, we have taken a string stored in my_str.

# Using the method casefold() we make it suitable for caseless comparisons. 
# Basically, this method returns a lowercased version of the string.

# We reverse the string using the built-in function reversed(). 
# Since this function returns a reversed object, we use the list() function to convert them into a list before comparing.




