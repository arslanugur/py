# Native Datatypes Examples
# Example: to Access Index of a List Using for Loop

# Example 1: Using enumerate
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
    print(index, val)

"""
Output:
0 21
1 44
2 35
3 11
"""

# Using enumerate(), we can print both the index and the values.

# Pass two loop variables index and val in the for loop. You can give any name to these variables.
# Print the required variables inside the for loop block.

# The function of enumerate() is to add a counter (i.e. index) to the iterate and return it. 
# If you want to learn more about enumerate(), please visit Python enumerate().


# Example 2: Start the indexing with non zero value
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list, start=1):
    print(index, val)

"""
Output:
1 21
2 44
3 35
4 11
"""

# The value of the parameter start provides the starting index.
# Example 3: Without using enumerate()
my_list = [21, 44, 35, 11]

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)

""""    
Output:
0 21
1 44
2 35
3 11
"""
# You can access the index even without using enumerate().

# Using a for loop, iterate through the length of my_list. Loop variable index starts from 0 in this case.
# In each iteration, get the value of the list at the current index using the statement value = my_list[index].
# Print the value and index.




    
