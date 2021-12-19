# To write to files you use the write method, which writes a string to the file.
# Example:
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())              # output: This has been written to a file
file.close()

# The "w" mode will create a file, if it does not already exist.

