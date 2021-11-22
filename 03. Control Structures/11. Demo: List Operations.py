# Problem 
# You are given a list of items. 

# Task
# Write a program that takes a num number as input, 
# reassigns the element with that index in the list to the value "x" 
# and outputs the updated list. 

# For example, for a given list [1, 2, 3, 4, 5] and input 3, 
# the output should be [1, 2, 3, "x", 5]. 

# Solution
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
input = int(input()) 
items[input] = "x" 
print(items)


# input: 3
# output: [1, 2, 3, 'x', 5, 6, 7, 8, 9, 10]
