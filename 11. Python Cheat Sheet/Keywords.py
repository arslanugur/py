# KEYWORD: False, True
# Description: Boolean data type
# Code:
False == (1 > 2)
True == (2 > 1)


# KEYWORD: and, or, not
# Description: Logical operators        # Code
#               and: Both are True        True and True # True
#               or: Either is true        True or False # True
#               not: Flips Boolean        not False     # True

# KEYWORD: break
# Description: Ends loop prematurely
# Code:
while True:
  break # Fİnite loop

# KEYWORD: continue
# Description: Finishes current loop iteration
# Code:
while True:
  continue
  print("42")  # dead code

# KEYWORD: class
# Description: defines new class
# Code:
class Coffee:
  # Define your class 


# KEYWORD: def
# Description: defines a new function or class method
# Code:
def say_hi():
  print('hi')
  

# KEYWORD: if, elif, else                       # Code:
# Description: Conditional execution:           x = int(input("ur val: "))
#               "if" condition == True?         if x > 3:       print("Big")
#               "elif" condition == True?       elif x == 3:    print("3")
#               fallback: else branch           else:           print("Small")


# KEYWORD: for, while
# Code: for loop
for i in [0, 1, 2]:
  print(i)
# Code: while loop does the same
j = 0
while j < 3:
  print(j); 
  j = j + 1
  

# KEYWORD: in
# Description: Sequence membership
# Code:
42 in [2, 39, 42] # True

# KEYWORD: is
# Description: Same object memory location
# Code:
y = x = 3
x is y      # True
[3] is [3]  # False


# KEYWORD: None
# Description: Empty value constant
# Code:
print() is None   # True


# KEYWORD: lambda
# Description: Anonymous function
# Code:
(lambda x: x+3) (3) # 6

# KEYWORD: return
# Description: Terminates function. Optimal return value defines function result
# Code:
def increment(x):
  return x + 1
increment(4)    # returns 5


