# OPERATOR PRECEDENCE
  # Operator precedence is a very important concept in programming. 
  # It is an extension of the mathematical idea of order of operations (multiplication being performed before addition, etc.) 
  # to include other operators, such as those in Boolean logic.

  # The below code shows that == has a higher precedence than or
print(False == False or True)     # True
print(False == (False or True))   # False
print((False == False) or True)   # True

print (True or False and False)
# It's True (!) because "and" goes first!
# You can check it against ((True or False) and False)
# which is False ! So you see that "and" has higher priority!

  # Python's order of operations is the same as that of normal mathematics: 
  # parentheses first, then exponentiation, then multiplication/division, and then addition/subtraction.
print(False == False)           # True
print(True or True)             # True
print(False == False or True)   # True
print(False or True )           # True
print(False == True )           # False
print(False == (False or True)) # False
print(False == False)           # True
print(True or True )            # True
print((False == False) or True) # True

# Example:
if 1 + 1 * 3 == 6:
   print("Yes")
else:
   print("No")  # No

# PEMDAS
# 1) Parentheses 2) Exponents 3) Multiplication || D-Division 4) A-Addition || S-Subtraction

# CHAINING MULTIPLE CONDITIONS
  # You can chain multiple conditional statements in an if statement using the Boolean operators.
  # For example, we can check if the value of a grade is between 70 and 100:
grade = 88
if(grade >= 70 and grade <= 100):
    print("Passed!") # Passed!
    
   # You can use multiple and, or, not operators to chain multiple conditions together.
  
# Example:
a = 7
b = 8
c = 6

if a < b or b < c and a < c:
    print("true 1")

if a < b or b < c and not a < c:
    print("true 2")

# the order of above logics is:
# a<b or (b<c and a<c)
# a<b or (b<c and (not a<c))

# Example:
x = 4
y = 2                                       # Short Version:
if not 1 + 1 == y or x == 4 and 7 == 8:     # if False:
  print("Yes")                              #   print('Yes')
elif x > y:                                 # elif True:
  print("No") # No                          #   print('No')
  
  # https://docs.python.org/3/reference/expressions.html#operator-precedence
  
  
  
