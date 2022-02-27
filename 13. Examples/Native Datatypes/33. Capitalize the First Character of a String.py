# Native Datatypes Examples
# Example: to Capitalize the First Character of a String


# Two strings are said to be anagram if we can form one string by arranging the characters of another string. 
# For example, Race and Care. Here, we can form Race by arranging the characters of Care.
# Example 1: Using list slicing
my_string = "programming is Lit"

print(my_string[0].upper() + my_string[1:])   # Programming is Lit


# In the above example, my_string[0] selects the first character and upper() converts it to uppercase. Likewise, my_string[1:] selects the remaining characters as they are. Finally they are concatenated using +.
# Example 2: Using inbuilt method capitalize()
my_string = "programming is Lit"

cap_string = my_string.capitalize()

print(cap_string)     # Programming is Lit

# Note: capitalize() changes the first character to uppercase; however, changes all other characters to lowercase.


