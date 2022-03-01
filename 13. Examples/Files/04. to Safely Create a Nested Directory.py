# Files Examples
# Example: to Safely Create a Nested Directory using Python
# Topics:     Python Directory and Files Management
#             Python Modules
#             Python Exception Handling Using try, except and finally statement

# There are different ways to create a nested directory depending on the versions of python you are using. 
# For this example, we will create directories as shown in the image below.

# Directory Structure:
# /root
#   |--/dirA
#   |     |--/dirB
#   |     |


# Example 1: Using pathlib.Path.mkdir
# For python 3.5 and above, you can use pathlib.Path.mkdir to create a nested directory.
from pathlib import Path
Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)

#     Import class Path from pathlib library.
#     Call the module mkdir() with two arguments parents and exist_ok.
#     By default, parents is set False. In this case, if the parent directory is not present, then FileNotFoundError is thrown. 
#       For example, if you want to create a nested directory /folder1/folder2/folder3, ,
#       and folder1 (parent) does not exist already, then FileNotFoundError is raised by default. So, we set it to True.
#     exist_ok is False by default. If the directory already exists, FileExistsError is raised. Set it to True to prevent this error.

# Note: You should provide the full path (absolute path) of the directory (not relative path). 
# If the directory already exists, the above code does not raise an exception.

# Example 2: Using os.makedirs
# For python 3.2 and above, you can use os.makedirs.,
import os
os.makedirs("/root/dirA/dirB")

#     Using method makedirs() from module os, a nested directory can be created in a simple way.
#     The parameter passed is the nested directory we wanted to create.

# You should provide the full path (absolute path) of the directory (not relative path). 
# If the directory already exists, the above code does not raise an exception.


# Example 3: Using distutils.dir_util
import distutils.dir_util

distutils.dir_util.mkpath("/root/dirA/dirB")

# This example is also similar to Example 2. Here mkpath() is used instead of makedirs().
# You should provide the full path (absolute path) of the directory (not the relative path). 
# If the directory already exists, the above code does not raise an exception.

# Example 4: Raising an exception if directory already exists
import os

try:
    os.makedirs("/dirA/dirB")
except FileExistsError:
    print("File already exists")

# This example is similar to Example 2.
#    The statement is put inside the try block.
#    If the directory is already present, FileExistsError is caught by the except block and runs the statements inside the block.


    

