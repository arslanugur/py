# Native Datatypes Examples
# Example: to Split a List Into Evenly Sized Chunks

# In this example, you will learn to split a list into evenly sized chunks in different ways.

# Example 1: Using yield
def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list, chunk_size)))     # Output: [[1, 2], [3, 4], [5, 6], [7, 8], [9]]

# In the above example, we have defined a function to split the list.

#    Using a for loop and range() method, iterate from 0 to the length of the list with the size of chunk as the step.
#    Return the chunks using yield. list_a[i:i+chunk_size] gives each chunk. 
#       For example, when i = 0, the items included in the chunk are i to i + chunk_size which is 0 to (0 + 2)th index. 
#       In the next iteration, the items included are 2 to 2 + 2 = 4.

# Learn more about yield at Python Generators.
# You can do the same thing using list compression as below.

chunk_size = 2
list_chunked = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
print(list_chunked)     # Output: [[1, 2], [3, 4], [5, 6], [7, 8], [9]]

# Learn more about list comprehension at Python List Comprehension.
# Example 2: Using numpy
import numpy as np

my_list = [1,2,3,4,5,6,7,8,9]
print(np.array_split(my_list, 5))       # Output: [array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8]), array([9])]

# array_split() is a numpy method that splits a list into equal sized chunks. Here, the size of the chunk is 5.

# Note: You need to install numpy on your system.




