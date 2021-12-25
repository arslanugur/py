# this below line of code writes "Hello world!" to a file
file.write("Hello world!")

# To write to files you use the write method, which writes a string to the file.
# Example:
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())              # output: This has been written to a file
file.close()

# The "w" mode will create a file, if it does not already exist.

# w   ---> write mode
# w+  ---> write and read mode


# When a file is opened in write mode, the file's existing content is deleted.
# do not use "write", if you want to add something to your file. use append for this.
# this "write" overwrites the file 
file = open("newfile.txt", "w")
file.write("Some new text")       # 2
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")     # 1
print(file.read())
print("Finished")                 # 3
file.close()

# As you can see, the content of the file has been overwritten.

# Example:
file = open("newfile.txt", "w") 
file.write("Some initial text")     # 2
file.close() 
file = open("newfile.txt", "r") 
print("Reading initial contents")   # 1
print(file.read()) 
print("Finished")                   # 3
file.close() 

file = open("newfile.txt", "w") 
file.write("Some new text")         # 5
file.close() 
file = open("newfile.txt", "r") 
print("Reading new contents")       # 4
print(file.read()) 
print("Finished")                   # 6
file.close()


# To edit an existing file without losing previous data use append(a) instead of write(w)
# Example: 
file = open("newfile.txt", "a") 
file.write("\nThis has been written again to a file") 
file.close()

# Example:
file = open("newfile.txt", "r")     # You ask your computer to open new file and read it 
print("Reading initial contents")   # Prints "Reading initial contents" in Result or as output 
print(file.read())                  # your computer starts reading the content shown as some initial text in Result or output 
print("Finished")                   # Prints Finished in the Results 
file.close()                        # You command your computer to close the file 
file = open("newfile.txt", "w")     # You ask your computer to open new file and write what you command it in the next line 
file.write("Some new text")         # You write some text but your not asking the computer to print what is written in the 
file file.close()                   # You command your computer to close the file 
file = open("newfile.txt", "r")     # You ask your computer to open new file and read i




# Example:
file = open("newfile.txt", "w") 
file.write("Some new text") 
file.write("can you") 
file.close() 

file = open("newfile.txt", "w") 
file.write("oh dear")           # 2
file.close() 

file = open("newfile.txt", "r") 
print("Reading new contents")   # 1
print(file.read()) 
print("Finished")               # 3
file.close()



# The write method returns the number of bytes written to a file, if successful.
msg = "Hello world!"                # we define a variable msg as hello world!
file = open("newfile.txt", "w")     # we create a new file called newfile.txt with the method w
amount_written = file.write(msg)    # redefine the file as amount_written and write msg into it which also tells the computer to tell the amount of character there are present
print(amount_written) # 12          # we print what is after the equals
file.close()                        # close

# To write something other than a string, it needs to be converted to a string first.

# What happens here is they use open() with 'w' mode, while write() will return the bytes that successfully written, 
# that's why here we get 12 from write() with open() in 'w' mode; whereas in the previous lesson they used open() in 'r' mode combined with read() to get the actual content.


# This shows the diff between printing the msg (integer) and actually printing (displaying) its content: 
msg = input("Try to add something to the file:\n") # input
file = open("newfile.txt", "w") 
amount_written = file.write(msg) 
print("Your input has", amount_written, "bytes.\n") 
file.close() 

file = open("newfile.txt", "r") 
print("Now let's see what you wrote:\n") 
print(file.read()) 
file.close()
  

# Example:
To understand this correctly you have to understand what bytes are in this context. 
Bytes are simply number of alphabets and/or characters used(characters like *space*, ! , ?, etc). 
let's identify the number of bytes in the following: 
Learnsolo = 9bytes (you guessed 9 too? correct!!!) 
programming = 11bytes 
shut up! = 8bytes( considering the "space" between shut and up, and the "!")



# Example:
names = ["John", "Oscar", "Jacob"] 
file = open("names.txt", "w+")      # write down the names into the file for name in names: 
file.write(name + "\n") 
file.close() 
file= open("names.txt", "r")        # output the content of file in console print(file.read()) file.close()


# Example:
names = ["John", "Oscar", "Jacob"] 
file = open("names.txt", "w+")      # write down the names into the file 
for i in names: 
  file.write(i + "\n") 
  file.close() 
file= open("names.txt", "r")        # output the content of file in console print(file.read()) file.close()


# If a file write operation is successful, which one of these statements will be true?
file.write(msg) == len(msg)
# this question is wrong, if thinking about ASCII, 
# but today when we talk about character, probably are thinking of UTF-8, and then one character is not a byte anymore.

# First of all, bits and bytes. 1 bit is a binary value, which means it is either a 0 or a 1. 
# 1 byte, on the other hand, is a value that is made up of 8 bits. Why 8 bits? 
# Historically, because that is the number of bits you needed to write a single ASCII character. 
# Capital letter 'A' would be 01000001 small letter 'a' would be 01100001. 
# Which brings us to a simple conclusion that one letter does indeed equal 1 byte or 8 bits.



# In the lesson it is mentioned that "The write method returns the number of bytes written to a file, if successful." 
# so based on that, below is the example, suppose we have a message variable msg = 'abcd' then the length of message variable msg will be: 
# len(msg) which will be 4 now the write method will return the no. 
# of bytes written (assuming 1 byte = 1 character) so, amt_written = file.write(msg) will be equal to 4 
# so, file.write(msg) == len(msg) is true as both are equal to 4


# Bytes define length. Assume 1 byte = 1 character. 

# Example about Explaination  
msg = "Hello world!" 
file = open("newfile.txt", "w") 
print(file.write(msg)) 
print(len(msg)) 
file.close() 

#also try this: 
msg = "Hello world!" 
file = open("newfile.txt", "w") 
if file.write(msg)==len(msg): 
  print("true") 
else: 
  print("false") 
file.close() #note # 1 bit= 0 or 1 1 byte=1 character and, 1 byte=8 bits
  
  

          


# Example to edit:
# You can use the append method if you just want to add something to the end which we learn later, but... 
# to keep from deleting everything that's stored in a file while using the write method you can save the contents of the file beforehand in a variable: 
file = open("newfile.txt", r) 
copy = file.read() 
file.close() 
file = open("newfile.txt", w) 
file.write(copy + \n + "whatever you want") 
file.close()



# Example to edit:
# You shouldn't open a file in 'w' mood. 
# The 'w' mood automatically creates a file if it doesn't exist. 
# So just use a new file name and then write in that file 
# example: 
f1 = open("a_new_file_name.txt", "w") 
f1.write("Write here whatever you want to write") #this will automatically create a new file
  



# Example to edit:
file = open("newfile.txt", "r") 
print("Reading initial contents") 
print(file.read()) 
print("Finished") 
file.close() 
This opens an existing text file that contains "some initial text" already written in it. 
You print "Reading initial contents" separately from the file, then read what's actually in the file, "some initial text". 
Finally you print "Finished" before closing the file. 
Nothing about the file changed as a result of this first block. 
It still only has "some initial text" written in it. 
file = open("newfile.txt", "w") 
file.write("Some new text") 
file.close() 
This overwrites the initial file, "Some new text" before closing the file. 
Now the file only has that line "Some new text" written in it. 
file = open("newfile.txt", "r") 
print("Reading new contents") 
print(file.read()) 
print("Finished") 
file.close() 
This opens our file, prints "Reading new contents" separately, reads the only line of text in the file, "Some new text", before print
  
  



# Now lets write a code that saves the text you type as notepad 
files(.txt) # a simple text editor. 
            # Step 1 : To write the text and save it as a file in a specific location 
file_text = str(input("Enter text :\n\t")) 
file_name = str(input("Enter the file name :\n\t")) + ".txt" 
file = open("text\\location\\" + file_name , "w+") 
file.write(file_text) 
file.close() #Step 2 : To give a preview of your file (unnecessary and only works on a python IDE - but no harm done) 
file = open("text\\location\\" + file_name , "r") 
print("Preview :\n\t) 
print(file.read()) 
file.close() 
# IMPORTANT NOTE: The location i have given "text\\location\\" is just an example and a correct location must be written by the programmer. 
# The location for a file in the desktop will look somewhate like this: C:\Users\User name\Desktop The above must be converted as : "C:\\Users\\User name\\Desktop\\"





# Example:
file = open("Calc.txt", "w") 
file.write("This is a basic calculator! Use it for basic operations") 
file.close() 
file = open("Calc.txt", "r") 
print(file.read()) 
file.close() 
print("Options:") 
print("Enter 'Add' for addition") 
print("Enter 'Sub' for subtraction") 
print("Enter 'Mul' for multiplication") 
print("Enter 'Div' division") 
user_input = raw_input("Enter your option: ") #using "raw_input()" 

