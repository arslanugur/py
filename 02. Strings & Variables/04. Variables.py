# A variable is something that holds a value that may change. 
# In simplest terms, a variable is just a box that you can put stuff in. 
# You can use variables to store all kinds of stuff, but for now, we are just going to look at storing numbers in variables.

# A variable allows you to store a value by assigning it to a name, which can be used to refer to the value later in the program.
# For example, in game development, you would use a variable to store the points of the player.

# To assign a variable, use one equals sign
user = "James" # In given example we assigned string "James" to user variable.

# Example: to create a variable "age" and assign the value 42 to it:
age = 42

# the way of multi variables assignment is called Sequence Unpacking.
a, b, c = 6, 5, 8 
print(a)    # 6
print(b, c) # 5 8


a, b = 0, 1 
a, b = b, a + b 
print(a)    # 1
print(b)    # 1


a, b = 0, 1 
a = b 
b = a + b 
print(a)    # 1
print(b)    # 2 

# why aren't they same above?
# it is because there is a simple way in a single line using sequence unpacking when you assign values to multiple variables

# Sequence unpacking 
  # Sequence can be a tuple, a list or string a, b = b, a + b 
  # the way of parenthesis omitted a, b = (b, a + b)
  # a normal tuple unpacking a, b = [b, a + b] 
  # or a normal list unpacking 
  # And an introduction to tuple packing 
t = 'It is', ' a ', 'tuple.' 
  # tuple packing, variable t is a tuple. print(t) 
  # Output: ('It is', ' a ', 'tuple.') 
  # The values of variables can be swapped in this way below. 
a, b = 0, 1 
a, b = b, a 
print(a, b)


# Example:
x = 7 
# We can make a comment by using '#'symbol
print(x)        # 7
y = x;x = 50    
# defining two varible in single line..
print(x,y)      # 50 7
# printing two variable in a singe ()...
# Note - Here y refers to x but later the value of x will be change.
# but the value of y is still going on...

# Example:
a, b, c = 5, 6, 10 
print(a+b+c) # 21



# Variable Names
  # Certain restrictions apply in regard to the characters that may be used in Python variable names. 
  # The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
  # the variables can start with an underscore
  # Not following these rules results in errors.  
this_is_a_normal_name = 7
123abc = 7  # SyntaxError: invalid syntax

  # Python is a case sensitive programming language. Thus, Lastname and lastname are two different variable names in Python.
  
  # You can sum up everything in three rules: 
  # 1: variable names can contain only letters, numbers and underscores (the only allowed special character) 
  # 2: variables cannot start with a number 
  # 3: variables cannot be named as special words that Python uses for something else. 
  # Those words are called special characters, and this prevent the user from making confusion. 
  # The words 'True' and 'False' are Boolean operands keywords, so neither of them can be the name of a variable. 
  # Remember that Python is case sensitive, so the lowercase version of 'true' and 'false' can be assigned to values.
  # letters, numbers, and underscores, NOT dashes or hyphens
  
  # Global and Local Variables aren't mentioned. 
  # "In Python, variables that are only referenced inside a function are implicitly global. 
  # If a variable is assigned a new value anywhere within the function's body, it's assumed to be a local."
  
  
  # Example: Correct
x=input() 
z=x 
var1=z 
print(var1)   

  # Example: Error
var1=z 
z=x 
x=input() 
print(var1) # NameError: name 'z' is not defined
  
  

