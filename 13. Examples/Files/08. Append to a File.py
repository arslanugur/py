# Files Examples
# Example: to Append to a File
# Topics: Python File I/O

# Open file in append mode and write to it

# The content of the file my_file.txt is
"""
honda 1948
mercedes 1926
ford 1903
"""

# The source code to write to a file in append mode is:
with open("my_file.txt", "a") as f:
   f.write("new text")

# The content of the file after appending a text to it is:
"""
honda 1948
mercedes 1926
ford 1903new text
""""
# Open the file in append 'a' mode, and write to it using write() method. Inside write() method, a string "new text" is passed. This text is seen on the file as shown above.

# If you want to learn more about different types of file opening modes, please refer to Python file I/O.



