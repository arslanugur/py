# Adding Words

# You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
# The function should be able to take a varying number of words as the argument.

"""
Sample Input:
this
is
great

Sample Output:
this-is-great
"""

# Recall, using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.

# Code:
def concatenate(*args): #Taking all the words using '*args'.
	result = None
	for i in args:
		if result == None:
			result = i
		else:  #Case where other than last word.
			result += "-" + i
	return result #Returning the result.

print(concatenate("I", "love", "Programming", "!"))



