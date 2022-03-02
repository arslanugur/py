# Files Examples
# Example: to Get Line Count of a File
# Topics: Python enumerate(), Python File I/O, Python for Loop

# Example 1: Using a for loop
# The content of the file my_file.txt is
"""
honda 1948
mercedes 1926
ford 1903
"""
# Source Code
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len("my_file.txt"))

# Output: 3

# Using a for loop, the number of lines of a file can be counted.
#    Open the file in read-only mode.
#    Using a for loop, iterate through the object f.
#    In each iteration, a line is read; therefore, increase the value of loop variable after each iteration.


# Example 2: Using list comprehension
num_of_lines = sum(1 for l in open('my_file.txt'))

print(num_of_lines)

# Output: 3

#    Open the file in read-only mode.
#    Using a for loop, iterate through open('my_file.txt').
#    After each iteration, return 1.
#    Find the sum of the returned values.


