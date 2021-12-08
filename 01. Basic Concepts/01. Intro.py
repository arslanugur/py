# Python is a high-level programming language, 
# with applications in numerous areas, including web programming, scripting, scientific computing, and artificial intelligence! 

# Printing text
  # to display "Hello world!".
  # In Python, we use the print statement to output text. 
print('Hello world!')
  # Note that the text should be enclosed into single or double quotes. 
  # The print statement needs to be followed by parentheses, which enclose the output we want to generate.
  
  # The print statement can also be used to output multiple lines of text.
print('Hello world!')
print('Hello world!')
print('Spam and eggs...') 
  # Python code often contains references to the comedy group Monty Python. 
  # This is why the words, "spam" and "eggs" are often used as placeholder variables in Python.

  # Placeholder variables are used for formatting strings. 
  # %s acts a placeholder for a string while %d acts as a placeholder for a number. 
  # Their associated values are passed in via a tuple using the % operator.
name = 'marcog'
number = 42 
print '%s %d' % (name, number)
  # will print marcog 42. Note that name is a string (%s) and number is an integer (%d for decimal).

  
  # To print in the same line: 
print('a', 'b', 'c', end=' ') 
print('x') 
  # That will print: a b c x 

  # Also: 
print('a', 'b', 'c', end='\t') 
print('x') 
  # Which will print a tabulation at the end of the statement: a b c x 
  
  # To print words separated by dots: 
print('a', 'b', 'c', sep='.')   # That will print: a.b.c 
  # To print in a new line: 
print('a', 'b', 'c', sep='\n') 
  # Which will print a line break after each argument, except the last one: a b c

  # We can also have multiple inputs to the "print" function. 
  # Whether there is space between your inputs depends on how you do it. 
  # No Space print('Hello'+'World') output --> HelloWorld 
  # Space print('Hello', 'World') output--> Hello World 
  # This may seem trivial now, but is useful when you have words stored as variables.
  
  
  
  # Print() is function that can accept any supporting data/parameter and output it as information to the console. 
  # Print("hello, python") 
  # The parameter here is a string (hello, python) 
  # You can do this too: 
myName = "He" 
Hobbies =" Coding" 
Print(myName+ " loves "+ Hobbies) # Output: He loves Coding
    
# Comments and Docstrings   
# In Python, a comment is created by inserting an octothorpe (otherwise known as a number sign or hash symbol: #). All text after it on that line is ignored.
# For example:
x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print (x // y)
# another comment

# Python doesn't have general purpose multiline comments, as do programming languages such as C.



# Docstrings
# Docstrings (documentation strings) serve a similar purpose to comments, as they are designed to explain code. 
# However, they are more specific and have a different syntax. 
# They are created by putting a multiline string containing an explanation of the function below the function's first line
# Example:
def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

shout("spam")

# Unlike conventional comments, docstrings are retained throughout the runtime of the program. 
# This allows the programmer to inspect these comments at run time.

