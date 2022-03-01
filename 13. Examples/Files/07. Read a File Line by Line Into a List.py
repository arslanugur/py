# Files Examples
# Example: to read a file line by line into a list
# Topics: Python File I/O

# Example 1: Using readlines()
# Let the content of the file data_file.txt be

# honda 1948
# mercedes 1926
# ford 1903

# Source Code
with open("data_file.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)

"""
Output:
['honda 1948\n', 'mercedes 1926\n', 'ford 1903']
['honda 1948', 'mercedes 1926', 'ford 1903']
"""

# readlines() returns a list of lines from the file.
#    First, open the file and read the file using readlines().
#    If you want to remove the new lines ('\n'), you can use strip().


# Example 2: Using for loop and list comprehension
with open('data_file.txt') as f:
    content_list = [line for line in f]

print(content_list)

# removing the characters
with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]

print(content_list)

"""
Output:
['honda 1948\n', 'mercedes 1926\n', 'ford 1903']
['honda 1948', 'mercedes 1926', 'ford 1903']
"""

# Another way to achieve the same thing is using a for loop. 
# In each iteration, you can read each line of f object and store it in content_list as shown in the example above.


