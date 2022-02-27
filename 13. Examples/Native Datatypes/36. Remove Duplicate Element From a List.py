# Native Datatypes Examples
# Example: to Remove Duplicate Element From a List


# Example 1: Using set()
list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))    # [1, 2, 4, 6]

# In the above example, we first convert the list into a set, then we again convert it into a list. 
# Set cannot have a duplicate item in it, so set() keeps only an instance of the item.
# Example 2: Remove the items that are duplicated in two lists
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))    # [4, 6, 7, 8]

# In the above example, the items that are present in both lists are removed.
#     Firstly, both lists are converted to two sets to remove the duplicate items from each list.
#     Then, ^ gets the symmetric difference of two lists (excludes the overlapping elements of two sets).



    
