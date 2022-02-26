# Native Datatypes Examples
# Example: to Concatenate Two Lists

# Example 1: Using + operator
list_1 = [1, 'a']
list_2 = [3, 4, 5]

list_joined = list_1 + list_2
print(list_joined)      # Output: [1, 'a', 3, 4, 5]

# In this example, + operator is used to concatenate two lists.
# Example 2: Using iterable unpacking operator *
list_1 = [1, 'a']
list_2 = range(2, 4)

list_joined = [*list_1, *list_2]
print(list_joined)      # Output: [1, 'a', 2, 3]

# * operator allows unpacking inside the list or tuple.
# Example 3: With unique values
list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_joined = list(set(list_1 + list_2))
print(list_joined)      # Output: [1, 2, 3, 'a']

# If you want the unique items from a concatenated list, you can use list() and set(). set() selects the unique values and list() converts the set into list.
# Example 4: Using extend()
list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_2.extend(list_1)
print(list_2)       # Output: [1, 2, 3, 1, 'a']

# Using extend(), you can concatenate a list to another list as shown in example above.



