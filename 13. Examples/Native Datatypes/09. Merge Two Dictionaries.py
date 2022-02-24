# Native Datatypes Examples
# Example: to merge two dictionaries into one in Python programming

# Example 1: Using the | Operator
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)

# Output: {1: 'a', 2: 'c', 4: 'd'}

# In Python 3.9 and later versions, the | operator can be used to merge dictionaries.
# Note: If there are two keys with the same name, the merged dictionary contains the value of the latter key.

# Example 2: Using the ** Operator
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print({**dict_1, **dict_2})

# Output: {1: 'a', 2: 'c', 4: 'd'}

# In the above program, we have used ** to unpack dictionaries dict_1 and dict_2. Then, the dictionaries are merged by placing them inside {}.

# To know more about **kwargs, visit Python *args and **kwargs.
# Note: The above code works for Python 3.5 and above versions.


# Example 3: Using copy() and update()
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)

# Output: {2: 'b', 4: 'd', 1: 'a'}

# Here, we have first copied the elements of dict_2 to dict_3 using the dictionary copy() method. 
# Then, we updated dict_3 with the values of dict_1 using the dictionary update() method.


