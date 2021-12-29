# Good practice to avoid wasting resources by making sure that files are always closed after they have been used. 
# One way of doing this is to use try and finally
try:
   f = open("filename.txt")

   print(f.read())

finally:
   f.close()
# 

# This ensures that the file is always closed, even if an error occurs.

# Finally block won't work properly if FileNotFoundError occurred. 
# So, we can make another try~except block in finally: 
# Example:
try: 
  f = open("filename.txt") 
  print(f.read()) e
  except FileNotFoundError: 
    print("No such file or directory") 
finally: 
try: 
  f.close() 
except: 
  print("Can't close file") 
# Or we can force our program to open our py file. 
# Like this: 
try: 
  f = open("filename.txt") 
  print(f.read()) 
except FileNotFoundError: 
  print("No such file or directory") 
  f = open(__file__, "r") # open itself 
finally: 
  f.close() 
# In other cases when we catch FileNotFoundError f.close() makes error too (and program will stop). 
# Note: second variant is faster, IMHO, because it didn't using one more try~except block.


# Example: The close() function will get called in this code
try:
  f = open("filename.txt")
  print(f.read())
  print(1 / 0)
finally:      # Remember that: finally: is always called, regardless of exceptions or errors. Since f.close() is within finally:, it will be called
  f.close()
#


# An alternative way of doing this is using with statements. 
# This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement. 
# Code:
with open("filename.txt") as f:
   print(f.read())
# The file is automatically closed at the end of the with statement, even if exceptions occur within it.  

# this "with", "as" file handling is way more intuitive than the traditional open close

# https://www.python.org/dev/peps/pep-0343/
# https://docs.python.org/3/reference/compound_stmts.html

# You can also change the 'f' to any name of your desire. 
# Example:
# 1. with open("filename.txt") as nice:
# 2. print(nice.read()) Here i changed the 'f' to 'nice', and used the 'nice' to read the file. 
# (Remember what 'as' is used for in the module: import math as new)
   
# Example: to create a valid with statement, reading the contents of the file.
with open("test.txt") as f:
  print(f.read())



# Example:
try: f = open("nonexistent.txt") 
  print(f.read()) 
except FileNotFoundError: 
  print("No such file or directory") 
finally: 

try: 
  f.close() 
except: 
  print("Can't close file") 
  print('duck')
  
try: 
  f = open("nonexistent.txt") 
  print(f.read()) 
finally: 
  f.close() 
  print('duckduck')
# The code would move on, in this example, even if the file doesn't exist, it still prints "duck", 
# but after the second part, if the file doesn't exist, the program terminates and doesn't print "duckduck". 
# And "open(__file__)" opens your current ".py" file, 
# because it will always exist, as itself long as you are running the program from a ".py" file, 
# since if it the code runs, it means the file exists.


# The following is a standard way to manage exception handling when opening and reading a file. 
# Notice the nesting of exception handling to cater for closing an already open file. 
try: # ... to open file. 
  myFile = open("sample.txt") 
try: # ... to read file. 
  print(file.read()) 
except: # ... handle read errors. 
  raise 
finally: # ... close my open file. 
  myFile.close() 
except: # ... handle open and read errors. 


# Example:
try: 
  f = open("file", "w") 
try: 
  f.write('Hello World!') 
finally: 
  f.close() 
except: 
  print('Wrong')
# A much cleaner way of doing this is using the with statement: 
# try: with open("output", "w") as outfile: outfile.write('Hello World') except: print 'Wrong'



# Example: This is the code for book title 
file = open("/usercode/files/books.txt", "r") 
for i in file: 
  if i[-1]=="\n": 
    print(i[0]+str(len(i)-1))
  else:
    print(i[0]+str(len(i))) 
file.close()


# Example: A more effective method is using the 'with' operator. 
with open('example.txt', 'r') 
as f: print(f.read())
# This simple 2-liner opens your file and only keeps it open while the code inside the 'with' statement is running then closes it. 
# To break it down: 
with open('example', 'r') 
as f: # - with - ensures the file is only open while we are working with it. 
open('example.txt', 'r') # opens 'example.txt' in read-only mode
as f # assigns a variable to open('example.txt', 'r'). - Equivalent to f = open('example.txt', 'r') : - 
# Required for syntax purposes print(f.read()) - prints(f.read())
# prints the content of the file we opened earlier under the f variable Note: This WILL NOT catch errors



# Heres what I came up with for the book titles problem. 
file = open("/usercode/files/books.txt", "r") 
books = file.readlines() # makes a list containing each line from books.txt as a list item. 
for book in books: 
  letter = (book[0]) # this variable stores the first letter (index 0) of each book 
  if book == books[-1]: # index -1 of the "books" list will look at the last item in "books" this way, if someone added more books to books.txt, our code will still work. 
    length = str(len(book)) # store the number of characters. Since this is for the last item in books, it will not have "\n" at the end so we can store the length as is. 
                            # We also changed it to a string so that we can add it to our "letter" variable in the next step. 
    print(letter + length) 
  else: 
    length = str(len(book)-1) # this subtracts 1 from every book that isn't the last on the list. This corrects the lengths that have the "\n" on the end. 
    print(letter + length)
    file.close()
#



# WRITE - READ on CSV files
# write to a file
try:
# w option open file on write mode for editing/creating
    file = open("newfile.csv", "w")
    file.write("spam,eggs,ham")
    print("File created!")
finally:
    file.close()

#read that file 
try:
# r option open file on read only mode
    file = open("newfile.csv", "r")
    print("File is loading...")
    print("Loaded content : " + file.read())
    print ("\n") #one line space for easy reading
    
finally:
    file.close()

#try to split its content 
try:
   f = open("newfile.csv","r")
   ff = f.read()
   print ("We read and split it by comma:")
   print (ff.split(","))
   print ("\n") #one line space for easy reading  
   
finally:
   f.close()
   
   
#now we are assigning values to a list
words =ff.split(",")
print ("Now assigning splitted content to List")   
#we can use list and print it by loop
for word in words:
    print (word)
#
      
      
      

# Examples: Handling files tests (with different handling of Files and exception)
# Test 0
try:
    print("Test 0:\ntry to open in r mode (default) new file\n","- "*20)
    file = open("file.txt")
    print("Reading initial contents")
    print(file.read())
    print("Finished")
    file.close()
except:
    print("\nFile not exist - not possible open it\n")

# Test 1
try:
    print("\nTest 1:\nopen in a mode new file, try to read it\n","- "*20)
    file = open("file.txt", "a")
    amount_written = file.write("New text\n")
    print("Amount written is:",amount_written)
    print("Reading contents")
    print(file.read())
    print("Finished")
except:
    print("\nFile opened but not possible to read it\n")
finally:
    file.close()

# Test 2
try:
    print("\nTest 2:\nopen in w mode new file, try to read it\n","- "*20)
    file = open("newfile.txt", "w")
    amount_written = file.write("Some new text\n")
    print("Amount written is:",amount_written)
    print("Reading contents")
    print(file.read())
    print("Finished")
except:
    print("\nFile opened but not possible to read it\n")
finally:
    file.close()

# Test 3
try:
    print("\nTest 3:\nopen in r mode a file, try to write it\n","- "*20)
    file = open("newfile.txt", "r")
    print("Reading contents")
    print(file.read())
    print("Finished")
    amount_written = file.write("Some other new text\n")
    print("Amount written is:",amount_written)
except:
    print("\nNot possible to write file in r mode\n")
finally:
    file.close()
    
# Test 4
try:
    print("\nTest 4:\nopen in w+ mode a file, try to read it\n","- "*20)
    file = open("newfile.txt", "w+")
    amount_written = file.write("Again some new text\n")
    print("Amount written is:",amount_written)
    print("Reading new contents")
    print(file.read())
    print("Finished")
    print("\nFile opened in w+ mode: possible read it")
    print("Nothing read: pointer at the end of file")
    print("Old file content deleted\n")
    file.seek(0)
    print("Reading new contents")
    print(file.read())
    print("Finished")
    print("\nPointer moved at start of file\n")
except:
    print("File opened in w+ mode: not possible to read it\n")  #False
finally:
    file.close()
    
# Test 5
try:
    print("\nTest 5:\nopen in r+ mode a file, try to write it\n","- "*20)
    file = open("newfile.txt", "r+")
    print("Reading contents")
    print(file.read())
    print("Finished")
    amount_written = file.write("Some other text\n")
    print("Amount written is:",amount_written,"\n")
except:
    print("\nFile opened in r+ mode: not possible to write it\n") #False
finally:
    file.close()
    
# Test 6
try:
    print("\nTest 6:\nopen in a mode a file, try to read it\n","- "*20)
    file = open("newfile.txt", "a")
    amount_written = file.write("add again some other new text\n")
    print("Amount written is:",amount_written)
    print("Reading new contents")
    print(file.read())
    print("Finished")
    print("\nFile opened in a mode: possible to read it") #False
    print("Nothing read since pointer is at the end of file")
    print("Old file content deleted\n") #False
except:
    print("\nNot possible to read file in a mode\n")
finally:
    file.close()
    
# Test 7
try:
    print("\nTest 7:\nopen in a+ mode a file, try to read it\n","- "*20)
    file = open("newfile.txt", "a+")
    amount_written = file.write("last line of new text\n")
    print("Amount written is:",amount_written)
    print("Reading new contents")
    print(file.read())
    print("Finished")
    print("\nPossible to read file in a+ mode")
    print("Nothing read pointer at the end of file")
    print("Old file content NOT deleted\n")
    file.seek(0)
    print("Reading new contents")
    print(file.read())
    print("Finished")
    print("\nPointer moved at start of file\n")
except:
    print("\nFile opened in a+ mode: not possible to read it\n") #False
finally:
    file.close()
    
# Test 8
try:
    print("\nTest 8:\nopen in r mode file, read more lines\n","- "*20)
    file = open("newfile.txt", "r")
    print("Reading contents")
    print(file.read())
    print("Finished\n")
except:
    print("error")
finally:
    file.close()
    
# Test 9
try:
    print("\nTest 9:\nopen in r mode existing file, read all\n","- "*20)
    file = open("newfile.txt", "r")
    print("Reading contents")
    print(file.readlines())
    print("Finished\n")
except:
    print("error")
finally:
    file.close()
    
# Test 10
try:
    print("\nTest 10:\nopen in r mode file, read single lines\n","- "*20)
    file = open("newfile.txt", "r")
    print("Reading contents")
    for line in file:
       print(line)
    print("Finished\n")
except:
    print("error")
finally:
    file.close()
    
# Test 11
try:
    print("\nTest 11:\nopen in r mode file, read characters\n","- "*20)
    file = open("newfile.txt", "r")
    print("Reading contents")
    print("First 16 characters", "#"*10)
    print(file.read(16))
    print("Following 40 characters", "#"*10)
    print(file.read(40))
    print("Following 4 characters", "#"*10)
    print(file.read(4))
    print("until the end", "#"*10)
    print(file.read())
    print("Following 4 characters", "#"*10)
    print(file.read(4))
    print("until the end", "#"*10)
    print(file.read())
    print("Finished\n")
except:
    print("error")
finally:
    file.close()

# Test 12
with open("newfile.txt") as f:
    print("\nTest 12:\nopen with with as\n","- "*20)
    print("Reading contents")
    for line in f:
       print(line)
    print("Finished")
    


