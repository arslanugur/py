# Files Examples
# Example: to Get the File Name From the File Path
# Topics: Python File I/O, Python Strings

# Example 1: Using os module
import os

# file name with extension
file_name = os.path.basename('/root/file.ext')

# file name without extension
print(os.path.splitext(file_name)[0])

# Output: file

# basename() gives the name of the last file/folder of the path, whereas splitext() splits the file name into filename and extension.

import os

print(os.path.splitext(file_name))

# Output: ('file', '.ext')

# Example 2: Using Path module
from pathlib import Path

print(Path('/root/file.ext').stem)

# Output: file

# Using stem attribute of Path module, the file name can be extracted as shown above.

# It works for python 3.4 and above.


