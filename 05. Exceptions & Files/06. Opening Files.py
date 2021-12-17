# You can use Python to read and write the contents of files.
# Text files are the easiest to manipulate. Before a file can be edited, it must be opened, using "the open function". open() - to access files
myfile = open("filename.txt")

# The argument of the open function is the path to the file. 
# If the file is in the current working directory of the program, you can specify only its name.

# You can specify the mode used to open a file by applying a second argument to the open function.
# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.

# Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
# Example:
open("filename.txt", "w")       # write mode
open("filename.txt", "r")       # read mode
open("filename.txt")            # read mode
open("filename.txt", "wb")      # binary write mode

# You can use the + sign with each of the modes above to give them extra access to files. 
# For example, r+ opens the file for both reading and writing.
# https://www.tutorialspoint.com/python3/python_files_io.htm


# Example: to open a file called "test.bin" in binary read mode.
file = open("test.bin","rb")
#          ("filename","Read Binary")

# Once a file has been opened and used, you should close it.
# This is done with the close method of the file object. 

# Example:
file = open("filename.txt", "w")
# do stuff to the file
file.close()  # to close a file stored in a variable "file" 

# We will read/write content to files in the upcoming lessons.
# https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python

# Example:
try: 
  f = open ("textfile.txt" "r") 
  print(f.read) 
  f.close() 
finally:
    f.close()
#


# In Python there also exists other modes:
# "r+" - Opens a file for both reading and writing. The file pointer placed at the beginning of the file. 
# "w+" - Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing. 
# "a+" - Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. 
#                                                     If the file does not exist, it creates a new file for reading and writing. It can also be combined with "b".


# Example:
file = open('a.txt','w+') 
file.write('Hello, World!')
file = open('a.txt') 
con = file.read() 
print(con) 
file.close()


# Example:
txt = "game.txt" 
f = open(txt,"w") 
f.write("Im building a game") 
f.close() 
f = open(txt,"a") 
f.write(" using unity engine") 
f.close() 
f = open(txt,"r") 
print(f.read()) 
f.close()



FILE MODES: 
"r"   Read from file - YES                    # read (default)
      Write to file - NO 
      Create file if not exists - NO 
      Truncate file to zero length - NO 
      
Cursor position - BEGINNING 
"r+"  Read from file - YES                    # for reading and writing 
      Write to file - YES 
      Create file if not exists - NO 
      Truncate file to zero length - NO 
      
Cursor position - BEGINNING 
"w"   Read from file - NO                     # open for writing, truncating the file first
      Write to file - YES 
      Create file if not exists - YES 
      Truncate file to zero length - YES 
    
Cursor position - BEGINNING 
"w+"  Read from file - YES                    # w+ is not commonly used because you already know there is nothing to read. so, not much point in reading an empty file. 
      Write to file - YES
      Create file if not exists - YES 
      Truncate file to zero length - YES      # truncate the file first (deletes the content of file everything you open with "w" or "w+")

Cursor position - BEGINNING 
"a"   Read from file - NO                     # append
      Write to file - YES                     # open for writing, appending to the end of the file if it exists 
      Create file if not exists - YES 
      Truncate file to zero length - NO 
    
Cursor position - END 
"a+"  Read from file - YES 
      Write to file - YES 
      Create file if not exists - YES 
      Truncate file to zero length - NO 

      
'b': binary mode 
't': text mode (default) 
'+': open a disk file for updating (reading and writing) 
'U': universal newlines mode (deprecated) What does "exclusive creation" mean? 
'x': open for exclusive creation, failing if the file already exists
"x" is similar to "w". But for "x", if the file exists, raise FileExistsError. For "w", it will simply create a new file / truncate the existed file.
I test the "x" mode and find some: It can not be used with "r/w/a" "x" is only writeable. 
"x+" can write and read The file must not exist before open The file will be created after open So, 


