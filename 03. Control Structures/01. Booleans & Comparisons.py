# BOOLEANS
  # Another type in Python is the Boolean type. There are two Boolean values: True and False.
  # They can be created by comparing values, for instance by using the equal operator ==.
my_boolean = True
print(my_boolean)         # True

print(2 == 3)             # False

code = 2==3 
print(code)               # False

print("hello" == "hello") # True      # Be careful not to confuse assignment (one equals sign) with comparison (two equals signs).

# Booleans can be compared too. 
a = 5 == 2+3 
b = 3 == 3 
c = a == b 
print(c)       # True

# Example:
print((2==2)+(3==3))  # 2

code = 2==3 
print(code+(2==2))    # 1 --> booleans are treated as 0 and 1

# Example
a=str(1==1) 
print(a)    # True
b=str(1==2) 
print(b)    # False
print(a+b)  # string concatenation --> 'True' + 'False' --> TrueFalse
print((1==1)+(1==2))    # Py converts each boolean to the int type, where boolean True becomes integer 1 and boolean False becomes integer 0.  
                        # prints the string form of integer 1
print(int(1==1))        # prints the string form of integer 1 --> Python automatically converts Print input to string

# Example:
string = "8" 
integer = 8 
print(string == integer)      # False 
print(int(string) == integer) # True 
print(string == str(integer)) # True



# COMPARISON
  # Another comparison operator, the not equal operator (!=), evaluates to True if the items being compared aren't equal, and False if they are.
print(1 != 1)                 # False
print("eleven" != "seven")    # True
print(2 != 10)                # True







