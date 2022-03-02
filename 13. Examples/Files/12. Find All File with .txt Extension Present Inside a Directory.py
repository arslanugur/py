# Files Examples
# Example: to Find All File with .txt Extension Present Inside a Directory
# Topics: Python File I/O, Python Directory and Files Management, Python for Loop

# Example 1: Using glob
import glob, os

os.chdir("my_dir")

for file in glob.glob("*.txt"):
    print(file)
"""
Output:
c.txt
b.txt
a.txt
"""

# Using glob module, you can search for files with certain extensions.
#   os.chdir("my_dir") sets the current working directory to /my_dir.
#   Using a for loop, you can search for files with .txt extension using glob().
#   * denotes all files with a given extension.

# Example 2: Using os
import os

for file in os.listdir("my_dir"):
    if file.endswith(".txt"):
        print(file)
"""
Output:
a.txt
b.txt
c.txt
"""

# In this example, we use endswith() method to check the .txt extension.
#     Using a for loop, iterate through each file of directory /my_dir.
#     Check if the file has extension .txt using endswith().

# Using os.walk
import os

for root, dirs, files in os.walk("my_dir"):
    for file in files:
        if file.endswith(".txt"):
            print(file)
"""
Output:
c.txt
b.txt
a.txt
"""
# This example uses the walk() method of the os module.
#     Using a for loop, iterate through each files of my_dir.
#     Check if the file has extension .txt using endswith().


