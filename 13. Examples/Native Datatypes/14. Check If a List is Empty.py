# Native Datatypes Examples
# Example: to Check If a List is Empty

# Example 1: Using Boolean operation
my_list = []
if not my_list:
    print("the list is empty")      # Output: the list is empty

# If my_list is empty then not returns True.

# It is the most pythonic way of testing emptiness. If you want to learn more about boolean truth value, you can refer to Truth Value Testing.
# Example 2: Using len()
my_list = []
if not len(my_list):
    print("the list is empty")      # Output: the list is empty

# In this example, length of list is used to check if there is any element in the list. If the length of a list is 0, then the list is empty.
# Example 3: Comparing with []
my_list = []
if my_list == []:
    print("The list is empty")      # Output: The list is empty
    
# [] is an empty list, therefore if my_list has no elements, then it should be equal to [].




