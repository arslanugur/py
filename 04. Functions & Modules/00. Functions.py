# LAMBDA FUNCTION
# Lambda function is used as a substitute of traditional function as declaring 
# and using lambda function is easy when we want to do only a single operation.
# Example:
lambda_cube = lambda y: y*y*y
print(lambda_cube(5)) # 125

# MAP FUNCTION
# The map() function executes a specified function for each item in an iterable
# Example:
# double number using map and lambda
nums = [1, 2, 3, 4]
# syntax: map(function, iterable)
result = map(lambda x: x+x, nums)
print(list(result)) # [2, 4, 6, 8]

# FILTER FUNCTION
# The filter() function returns an iterator were the items are filtered through a function to test of the item is accepted or not.
# Example:
# filter all odd numbers
seq = [0, 1, 2, 3, 5, 8, 13]  # sequence
# syntax: filter(function, iterable)
result = filter(lambda x: x%2!=0, seq)
print(list(result)) # [1, 3, 5, 13]


# ZIP FUNCTION
# The purpose of python zip() method is to map the similar index of multiple containers so that they can be used just using as single entity
# Example:
name = ['one', 'two', 'three']
value = [1, 2, 3]

# syntax: zip(iterable1, iterable2 ...)
result = zip(name, value)
print(result)   # [('one', 1), ('two', 2), ('three', 3)]


# ENUMERATE FUNCTION
# enumerate() function adds a counter to an iterable and returns it in a form of enumerated object.
# This enumerated object can then because directly for loops or converted into list or tuples using type cast functions.
# Example:
seq = ['one', 'two', 'three']
# syntax: enumerate(iterable1, [start = 1])
result = enumerate(seq, start = 1)
print(list(result)) # [(1, 'one'), (2, 'two'), (3, 'three')]



