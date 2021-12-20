# To open a text file, use: 
fh = open("hello.txt", "r") 

# To read a text file, use: 
fh = open("hello.txt","r") 
print(fh.read()) 

# To read one line at a time, use: 
fh = open("hello".txt", "r") 
print(fh.readline()) 

# To read a list of lines use: 
fh = open("hello.txt.", "r") 
print(fh.readlines()) 

# To write to a file, use: 
fh = open("hello.txt","w") 
write("Hello World") 
fh.close() 

# To write to a file, use: 
fh = open("hello.txt", "w") 
lines_of_text = ["a line of text", "another line of text", "a third line"] 
fh.writelines(lines_of_text)
fh.close()

# To append to file, use: 
fh = open("Hello.txt", "a") 
write("Hello World again") 
fh.close

# To close a file, use 
fh = open("hello.txt", "r") 
print(fh.read()) 
fh.close()
          

