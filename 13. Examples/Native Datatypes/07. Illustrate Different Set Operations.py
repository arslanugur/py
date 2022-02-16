# Native Datatypes Examples
# Example: to Illustrate Different Set Operations

# In this example, we have defined two set variables and 
# we have performed different set operations: union, intersection, difference and symmetric difference.

# Python offers a datatype called set whose elements must be unique. 
# It can be used to perform different set operations like union, intersection, difference and symmetric difference.
# Source Code
# Program to perform different set operations like in mathematics

# define three sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)

"""
Output:
Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}
Intersection of E and N is {2, 4}
Difference of E and N is {8, 0, 6}
Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}
"""

# In this program, we take two different sets and perform different set operations on them. This can equivalently done by using set methods.


