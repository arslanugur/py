# Lists are used to store items.
# A list is created using square brackets with commas separating items.
words = ["Hello", "world", "!"]

# In the example above the words list contains three string items.
# A certain item in the list can be accessed by using its index in square brackets.
# For example:
words = ["Hello", "world", "!"]
print(words[0]) # Hello
print(words[1]) # world
print(words[2]) # !

# The first list item's index is 0, rather than 1, as might be expected.

# Example:
words = ["Hello", "world", "!"] 
print(words[-3]) 
print(words[-2]) 
print(words[-1]) 
# output: Hello world !

# Example:
ele1=3          # ELE = Empty List Element
ele2=4
subele1=4
subele2=6
vec=[ele1,ele2,[subele1,subele2]]
print(vec[2][1])  # sublist element = 6 --> The second set of square brackets is referring to the 2nd element in the sublist.

