# Native Datatypes Examples
# Example: to Create a Long Multiline String


# Example 1: Using triple quotes
my_string = '''The only way to
learn to program is
by writing code.'''

print(my_string)
"""
Output:
The only way to
learn to program is
by writing code.
"""

# You can use '''(multiline string)''' or """(multiline string)""" to print a multiline string as shown above.
# Example 2: Using parentheses and a single/double quotes
my_string = ("The only way to \n"
        	"learn to program is \n"
        	"by writing code.")

print(my_string)

"""
Output:
The only way to
learn to program is
by writing code.
"""

# If you use (" ") syntax, you need to specify the newlines explicitly using \n.
# Example 3: Using \
my_string = "The only way to \n" \
        	"learn to program is \n" \
        	"by writing code."

print(my_string)
"""
Output:
The only way to
learn to program is
by writing code.
"""

# You can use \ as in the above example code to write a multiline string.


