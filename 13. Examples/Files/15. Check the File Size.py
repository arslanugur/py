# Files Examples
# Example: to Check the File Size
# Topics: Python Directory and Files Management


# Example 1: Using os module
import os

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)

# Output: 34

# Using stat() from the os module, you can get the details of a file. Use the st_size attribute of stat() method to get the file size.

# The unit of the file size is byte.
# Example 2: Using pathlib module
from pathlib import Path

file = Path('my_file.txt')
print(file.stat().st_size)

# Output: 34

# Using the pathlib module, you can do the same thing as shown above. The unit of the file size is byte.


