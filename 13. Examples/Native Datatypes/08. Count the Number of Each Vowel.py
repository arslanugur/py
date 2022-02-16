# Native Datatypes Examples
# Example: to Count the Number of Each Vowel

# In this program, you'll learn to count the number of each vowel in a string using dictionary and list comprehension.

# Source Code: Using Dictionary
# Program to count the number of each vowels
vowels = 'aeiou'    # string of vowels

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)    # Output: {'o': 5, 'i': 3, 'a': 2, 'e': 5, 'u': 3}

# Here, we have taken a string stored in ip_str. Using the method casefold(), we make it suitable for caseless comparisons. 
# Basically, this method returns a lowercased version of the string.

# We use the dictionary method fromkeys() to construct a new dictionary with each vowel as its key and all values equal to 0. 
# This is the initialization of the count.

# Next, we iterate over the input string using a for loop.

# In each iteration, we check if the character is in the dictionary keys (True if it is a vowel) and increment the value by 1 if true.




# Source Code: Using a list and a dictionary comprehension
# Using dictionary and list comprehension
ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# count the vowels
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)
# The output of this program is the same as above.

# Here, we have nested a list comprehension inside a dictionary comprehension to count the vowels in a single line.

# The dictionary comprehension runs for all vowel characters and the list comprehension inside the dictionary comprehension checks 
# if any characters in the string match that particular vowel.

# At the end, a list with 1s is generated for the number of each vowel character. 
# The sum() method is used to calculate the sum of the elements for each list.

# However, this program is slower as we iterate over the entire input string for each vowel.



