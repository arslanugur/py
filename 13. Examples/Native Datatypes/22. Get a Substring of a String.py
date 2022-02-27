# Native Datatypes Examples
# Example: to Get a Substring of a String

# Using String slicing
my_string = "I love python."

# prints "love"
print(my_string[2:6])

# prints "love python."
print(my_string[2:])

# prints "I love python"
print(my_string[:-1])

"""
Output:
love
love python.
I love python
"""

# String slicing works similar to list slicing. The working of above code can be understood in the following points.
#     [2:6]
#     You need to specify the starting index and the ending index of the substring. In this case, love starts at index 2 and ends at index 6.
#     [2:]
#     All the text from index 2 to the end are selected.
#     [:-1]
#     All the text before the last index is selected.



