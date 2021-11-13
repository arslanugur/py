# Example:
seven = "7"
seven = seven + "0"
seventythree = int(seven) + 3
print(float(seventythree))  # 73.0

# To solve this question, you have to look at the set of code line by line. 
# Line 1: seven = “7” 
# This assigns “7” to the variable 'seven'. Note that this value is a string and not an integer value. 
# Line 2: seven = seven + “0” By adding the value of these two strings together, one is concatenating two strings together so the result is “70”. 
# The result is not 0 because you are adding string values and not integer values. 
# Line 3: seventythree = int(seven) + 3 
# This first converts the string to an integer, then adds 3 to the integer. 70 + 3 = 73.
# This value is then assigned to the variable 'seventythree'. 
# Line 4: print(float(seventythree)) 
# This converts the 73 to a float first (into 73.0) before printing this value out. Therefore, the output of this code is 73.0
# str(7) + str(0) = "70" int("70") = 70 float(70+3) = 73.0

# Example:
age = int(input())  # input: 25   # Firstly, string '25' is converted into int. 
print(age+8)        # output: 33 

# int() converts from a string to an integer. 
# But int("42.0") raises an error. 
# However, to avoid errors, you can use this trick: print(int(float("42.0")) # 42

# Example:
x = 5
y = x + 3
y = int(str(y) + "2")
print(y)  # 82

# it stores 8 as string which makes it not add as 8+2 = 10 but as 8 and 2= 82 tricky part is 8 is stored as string and not int
# 1. x = 5 
# 2. y = x + 3 --> 5 + 3 --> 8 
# 3. y = int(str(y) + "2") --> str(y) means "8" (y = 8, str = string), str(y) + "2" means "8" + "2" = 82 (They are strings, not numbers that's why it's not 10), 
# so int(str(y) + "2") means "82" as an integer --> 82 
# 4. print(y) --> print(82)

# Example: to declare a variable, add 5 to it and print its value.
x = 4
x += 5    # represents x = x+5
print(x)  # 9

# Example:
x = 3
num = 17
print(num % x)  # remainer --> 2
                # % Modulo Operator

# Another example:
# 32 % 6 = 2 
# 32 / 6 = 5 
# 5 * 6 = 30
# 32 - 30 = 2 --> remainder is 2 

# Example: to take a name as input and output a Welcome message, containing the input?
name = input()
print("Welcome, " + name)


# Example
name = "Aretha"
surname = "Franklin"
age = 30
 
print("Her name is "+ name + " "+ surname + " and \nI'm "+ str(age) + " y/o.")    
                                                           # from int to str
# Second Way 
greeting = "Her name is "+ name + " "+ surname + " and \nShe is "+ str(age) + " y/o."
print(greeting)

print(name[0])      # A
print(greeting[2])  # r

# Example:
greeting = 'Her name is '+ name + ' '+ surname + ' and \nShe is '+ str(age) + ' years old'
print(len(greeting)) # There are 52 Characters
# SECOND WAY
  # length = len(greeting)
  # print(length)

# Examples about String Formatting
print(greeting[length-1]) # to find the last character
print(greeting[2:5])      # from second index to the fifth index
print(greeting[3:])       # from third index to the last index
print(greeting[:15])      # from 0 to 15
print(greeting[2:40:2])   # from 2 to 40 but takes once in each two characters



# Example:
name = 'Floyd\'s song'
# SECOND WAY
# message = f'Hello {name}'
# print(message)   
message = 'Hello {}'
print(message.format(name))   # Hello Floyd's song


# Extras:
name = 'OtisRedding'
print(dir(name)) # shows what you can do with that?
print(help(str)) # descript about str





  
  
