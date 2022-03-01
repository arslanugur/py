# Files Examples
# Example: to copy the content of a file to another file using Python.
# Topics: Python File I/O

# Using shutil module
from shutil import copyfile
copyfile("/root/a.txt", "/root/b.txt")

# The first parameter of copyfile() is the path of the source file and the second parameter is the path of the destination file. 
# The content of the destination file is replaced with the content of the source file.

# There are other methods copy(), cop2(), and copyfileobj() which serve the same purpose with some metadata changes.

# Method:         Preserves Permissions					Supports Directory as Destination					Copies Metadata					Supports file object
# -------------------------------------------------------------------------------------------------------------------------------------
# copy()          Yes                 					Yes                              					No             					No
# copyfile()	    No                            No                              					No            					No
# copy2()			    Yes                 					Yes                             					Yes           					No
# copyfileobj()   No					                  No                                        No            					Yes


