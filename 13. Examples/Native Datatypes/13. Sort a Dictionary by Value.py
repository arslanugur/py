# Native Datatypes Examples
# Example: to sort a Python dictionary by value.

# Example 1: Sort the dictionary based on values
dt = {5:4, 1:6, 6:3}

sorted_dt = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}
print(sorted_dt)    # Output: {6: 3, 5: 4, 1: 6}

#    Here, key=lambda item: item[1] returns the values of each key:value pair.
#    From each key:value pair of dt.item(), sorted() sorts the items based on values.
# Learn more about sorted() and its parameter key at Python sorted().

# Example 2: Sort only the values
dt = {5:4, 1:6, 6:3}

sorted_dt_value = sorted(dt.values())
print(sorted_dt_value)      # Output: [3, 4, 6]

# In this example, sorted() is used for sorted values only. The values are fed into sorted() using dt.values().



