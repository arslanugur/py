# Function Examples
# Example: to Return Multiple Values From a Function

# Example 1: Return values using comma
def name():
    return "John","Armin"

# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2 = name()
print(name_1, name_2)
"""
Output:
('John', 'Armin')
John Armin
"""
# When you return multiple values using comma(s), they are returned in the form of a tuple. 
# As shown in the code above, two strings "John" and "Armin" are returned with a single return statement.


# Example 2: Using a dictionary
def name():
    n1 = "John"
    n2 = "Armin"

    return {1:n1, 2:n2}

names = name()
print(names)
# Output: {1: 'John', 2: 'Armin'}

# When you return values using a dictionary, it is easy for you to keep track of the returned values using the keys. 
# The return statement returns the two variables in the form a dictionary.


