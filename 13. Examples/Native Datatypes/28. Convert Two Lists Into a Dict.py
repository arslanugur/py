# Native Datatypes Examples
# Example: to Convert Two Lists Into a Dictionary


# Example 1: Using zip and dict methods
index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = dict(zip(index, languages))
print(dictionary)                     # {1: 'python', 2: 'c', 3: 'c++'}

# We have two lists: index and languages. They are first zipped and then converted into a dictionary.
#   The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
#   Likewise, dict() gives the dictionary.


# Example 2: Using list comprehension
index = [1, 2, 3]
languages = ['python', 'c', 'c++']

dictionary = {k: v for k, v in zip(index, languages)}
print(dictionary)                     # {1: 'python', 2: 'c', 3: 'c++'}

# This example is similar to Example 1; the only difference is that list comprehension is being used for first zipping and then { } for converting into a dictionary.

# Learn more about list comprehension at Python List Comprehension.


