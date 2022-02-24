# Native Datatypes Examples
# Example: to make a flattened list from a nested list in Python

# Example 1: Using List Comprehension
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)

# Output: [1, 2, 3, 4, 5, 6, 7]

# This is one of the simplest pythonic ways of flattening a list.

# Using list comprehension access the sublist from my_list, then access each element of the sublist.
# Each element num is stored in flat_list.
# Learn more about list comprehension at Python List Comprehension.


# Example 2: Using Nested for Loops (non pythonic way)
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7]
# Create an empty list flat_list.
# Access each element of the sublist using a nested loop and append that element to flat_list.

# Example 3: Using itertools package
import itertools

my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = list(itertools.chain(*my_list))
print(flat_list)    # Output: [1, 2, 3, 4, 5, 6, 7]

# Using itertools module, we can create a flattened list.

# chain() method from itertools module returns each element of each iterable (i.e. sub lists ).
# list() converts those returned values into a list.


# Example 4: Using sum()
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = sum(my_list, [])
print(flat_list)    # Output: [1, 2, 3, 4, 5, 6, 7]

# Provide two arguments to the sum() method: my_list and an empty list (i.e. [ ]).
# sum() combines my_list and [ ] to produce a flattened list.


# Example 5: Using lambda and reduce()
from functools import reduce

my_list = [[1], [2, 3], [4, 5, 6, 7]]
print(reduce(lambda x, y: x+y, my_list))    # Output: [1, 2, 3, 4, 5, 6, 7]

# In the above example, reduce() applies the lambda function to all the elements of my_list.
# Learn more about lambda expressions at Python Anonymous/Lambda Function.


