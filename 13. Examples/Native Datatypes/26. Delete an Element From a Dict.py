# Native Datatypes Examples
# Example: to Delete an Element From a Dictionary

# Example 1: Using del keyword
my_dict = {31: 'a', 21: 'b', 14: 'c'}
del my_dict[31]
print(my_dict)    # {21: 'b', 14: 'c'}

# In the code above, the key:value pair with key as 31 is deleted using del keyword. del keyword gives a KeyError if the key is not present in the dictionary.
# Example 2: Using pop()
my_dict = {31: 'a', 21: 'b', 14: 'c'}
print(my_dict.pop(31))    # a
print(my_dict)            # {21: 'b', 14: 'c'}

# Pass the key 31 as an argument to the pop() method. It deletes the key:value pair with key as 31 as shown in the output.

# pop() also returns the value of the key passed.


