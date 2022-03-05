# Advanced Examples
# Example: to Represent enum
# Topics: Python Object Oriented Programming

# Example:
# Using enum module
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3

# print the enum member
print(Day.MONDAY)

# get the name of the enum member
print(Day.MONDAY.name)

# get the value of the enum member
print(Day.MONDAY.value)

"""
Output:
Day.MONDAY
MONDAY
1
"""

# Here, we have class Day with the object Enum as its argument. 
# name and value are the attributes of Enum which give the name and value of the member MONDAY respectively.

# You can refer to the official documentation of enum for more information.


