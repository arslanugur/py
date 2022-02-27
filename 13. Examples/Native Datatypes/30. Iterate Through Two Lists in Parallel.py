# Native Datatypes Examples
# Example: to Iterate Through Two Lists in Parallel

# Example 1: Using zip (Python 3+)
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

for i, j in zip(list_1, list_2):
    print(i, j)
"""
Output:
1 a
2 b
3 c
"""

# Using zip() method, you can iterate through two lists parallel as shown above.

# The loop runs until the shorter list stops (unless other conditions are passed).
# Example 2: Using itertools (Python 2+)
import itertools

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']

# loop until the short loop stops
for i,j in zip(list_1,list_2):
    print(i,j)

print("\n")

# loop until the longer list stops
for i,j in itertools.zip_longest(list_1,list_2):
    print(i,j)
"""
Output:
1 a
2 b
3 c


1 a
2 b
3 c
4 None
"""

# Using the zip_longest() method of itertools module, you can iterate through two parallel lists at the same time. 
# The method lets the loop run until the longest list stops.


