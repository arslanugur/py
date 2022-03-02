# Files Examples
# Example: to Extract Extension From the File Name
# Topics: Python Directory and Files Management, Python File I/O

# Example 1: Using splitext() method from os module
import os
file_details = os.path.splitext('/path/file.ext')
print(file_details)
print(file_details[1])

"""
Output:
('/path/file', '.ext')
.ext
"""

# os.path.splitext() gives a tuple with one item as the name of the file along with the path and the other is the extension of the file. 
# If you want the file extension only, you can print it as shown above file_details[1].
# Example 2: Using pathlib module
import pathlib
print(pathlib.Path('/path/file.ext').suffix)

"""
Output: .ext
"""

# Using suffix attribute from pathlib module, we can get the extension of a file. In the above example, .ext is the extension of file file.ext.

# Note: It works for python 3.4 and above.



  
