# The contents of a file that has been opened in text mode can be read using the read method.
# Example:
file = open("filename.txt", "r")

cont = file.read()
print(cont)         # This will print all of the contents of the file "filename.txt"

file.close()

# The reason for assigning the file to a variable: 
# In a real program, you might refer to that file in several different places in your code. 
# By using a variable, you have only one thing to change, if later you want to use file2 instead of file1. 
# Or if you change the directory path. 
# Not only is it easier to change one occurrence than 12 occurrences, 
# it also prevents bugs from you (or another programmer) forgetting that one remote occurrence deep in the code.


# To read only a certain amount of a file, you can provide a number as an argument to the read function. 
# This determines the number of bytes that should be read.
# You can make more calls to read on the same file object to read more of the file byte by byte. 
# With no argument, read returns the rest of the file. 
file = open("filename.txt", "r")  # open file in read mode 
print(file.read(16))              # byte 1-16 
print(file.read(4))               # byte 17-20 
print(file.read(4))               # byte 21-24 
print(file.read())                # all the rest 
file.close()                      # close file

# Just like passing no arguments, negative values will return the entire contents.

# Example: How many characters would be in each line printed by this code, if one character is one byte? --> 21 * 4 = 84
file = open("filename.txt", "r")
for i in range(21):
  print(file.read(4))     # The meaning of this line is print only 4 characters from the file
file.close()
# This code loops 21 lines. On each line there are 4 bytes. 1 byte = 1 character, So 4 characters per line

# Explanation:
# 1) file.open("filename.text","r")  to open a file called filename (txt means in text format) 
#                                    and we are gonna read("r" indicates to read the contents of the file) that file 
# 2) for i in range(21)              for loop runs infinitely until its gets stopped or it results in false here 
#                                    the range for loop has mentioned 21 means it should run 21 times(from i=0 to i=20) 
# 3)print(file.read(4))              the read pointer reads first four characters on 1st line n next four characters on next line and continues. 
#                                    totally it reads around 84 characters in 21 lines.




# After all contents in a file have been read, 
# any attempts to read further from that file will return an empty string, 
# because you are trying to read from the end of the file.
file = open("filename.txt", "r")
file.read()
print("Re-reading")     #
print(file.read())
print("Finished")       #
file.close()
# Just like passing no arguments, negative values will return the entire contents.



# You can reread an already read file by using the method ".seek(0)". 
# The .seek(0) method takes the cursor back to beginning of the file. 
# Also note that the argument in the .seek() method is an index indicating the position you want to place the cursor. 
# Example: 
file = open("test.py","w") 
file.write("Hello world")       #
file.close() 
file = open('test.py') 
print(file.read()) 
print(file.read()) 
print("re-reading")             #
file.seek(1)                    # ello world
print(file.read()) 




# Example: to open a file, read its content and print its length.
file = open("filename.txt", "r")    # Open the file in read mode
str = file.read()                   # Pour the content in to a variable
print(len(str))                     # Print length of the variable -- len will give the number of characters or words in the text, depends how you write. 
file.close()                        # Close the file
# Book chapters cannot be read from outside the book's cover. The same goes for files! In order to read a file, you must first open it.



# To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
# Example:
file = open("filename.txt", "r")
print(file.readlines())           # Output: ['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
file.close()

# You can also use a for loop to iterate through the lines in the file: 
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()
# Output:
# Line 1 text

# Line 2 text

# Line 3 text
# In the output, the lines are separated by blank lines, as the print function automatically adds a new line at the end of its output.

# To avoid the extra lines skipped. do this. 
file = open("filename.txt" , "r") 
lines = file.readlines() 
for line in lines: 
  print(line, end="") # This is the part that does it 
file.close()


# Example: file line list -> file line dictionary (fileLineList2fileLineDict)
  # Generating file
file = open("file.txt", "w")
file.write("""Linie1
Linie2
Linie3
""")
file.close()
  # Generating dictionary
file = open("file.txt" , "r")
var_dict = {}
line_number = 0
for line_text in file:
	var_dict.update({line_number + 1: line_text})
	line_number = line_number + 1
file.close()
print(var_dict)             # output: {1: 'Linie1\n', 2: 'Linie2\n', 3: 'Linie3\n'}


# Example: If the file test.txt has 7 lines of content, what will the following expression return?
len(open("test.txt").readlines()) # 7

# There are 7 lines in the file. 
# Using the .readlines () method gives us a list where each item in the list is 1 line. 
# The question is asking for the length (len) of the list. 
# len gives us the quantity of items, rather than the index. 
# Therefore the output would be 7 (the quantity) not 6 (the highest index) one thing this is useful for is for loops that use range () to iterate through a list. 
# Example: my_list = ["Amy", "Andy", "Michael", "Jordan"] for indx in range (len (my_list)): print (my_list[indx]) 
# Remember, the range () function counts from 0 to (but not including) the number given. range(7) is 0,1,2,3,4,5,6. quantity = 7
# So in cases like this, it would be from 0 to 3, which is exactly matching the numbers of the index. 


