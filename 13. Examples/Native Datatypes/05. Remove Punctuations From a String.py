# Native Datatypes Examples
# Example: to Remove Punctuations From a String

# This program removes all punctuations from a string. 
# We will check each character of the string using for loop. 
# If the character is a punctuation, empty string is assigned to it.

# Sometimes, we may wish to break a sentence into a list of words.

# In such cases, we may first want to clean up the string and remove all the punctuation marks. Here is an example of how it is done.
# Source Code
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''   # define punctuation

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

# Output: Hello he said and went

# In this program, we first define a string of punctuations. Then, we iterate over the provided string using a for loop.

# In each iteration, we check if the character is a punctuation mark or not using the membership test. 
# We have an empty string to which we add (concatenate) the character if it is not punctuation. 
# Finally, we display the cleaned up string.


