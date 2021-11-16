# The if statement allows you to check a condition and run some statements, if the condition is True.
# The else statement can be used to run some statements when the condition of the if statement is False.

# As with if statements, the code inside the block should be indented.
x = 4
if x == 5:
    print("Yes")
else:             # Notice the colon after the else keyword.
    print("No")
    
# Example:
x = int(input("Enter a number: "))
if x == 5:
    print("Yes")
else: 
    if x < 5: 
        print("Less than 5") 
    else: 
        if x > 5: 
            print("Greater than 5")
            
# Example:
n= int(input("Enter a number"))
if (n>0):
  print("positive")
elif (n<0): 
  print("negative") 
else: 
  print("zero")
  
# Example:
x = (input("")) 
print("You are " + x + " years old.") 
if float(x) <= 70: 
    print("WOW! Yoy are a young person!") 
else:
    print("Never mind! Live young!") 
    print("In fact, your age doesn't have any matter ;)")
    
    
# Example:if 1 + 1 == 2:
if 2 * 2 == 8:
      print("8")
else:
      print("4")    # 4

        
# Every if condition block can have only one else statement.
# In order to make multiple checks, you can chain if and else statements.

# For example, the following program checks and outputs the num variable's value as text: 
num = 3
if num == 1:
    print("One")
else: 
    if num == 2:
        print("Two")
    else: 
        if num == 3: 
            print("Three")
        else: 
            print("Something else")
            
# Indentation determines which if/else statements the code blocks belong to.

# Example:
a = 3 
if a == 1: 
    print('a is 1') 
elif a == 3: 
    print('a is 3') 
elif a == 10: 
    print('a is 10') 
else: 
    print('a is not 1, 3 or 10')
    

# Example:
byear = int(input("Your birth year: ")) 
cyear = 2018 
if cyear - byear >= 21: 
    print("You can legally drink in the US") 
else: 
    if byear > cyear: 
        print("You are born in the future - how are you already learning to code") 
    else: 
        print(21 - cyear + byear, " years until you can legally drink in the US")

# Example:
side1 = int(input())
side2 = int(input())
side3 = int(input()) 

if side3**2 == side1**2 + side2**2: 
    print ("Right-angled")
else:
    print ("Not right-angled")
    
# Example:
x = 10
y = 20
if x > y:
   print("ten")
else:
   print("twenty")
    
    
    
# ELIF STATEMENTS
    # Multiple if/else statements make the code long and not very readable.
    # The elif (short for else if) statement is a shortcut to use when chaining if and else statements, making the code shorter.

    # The same example from the previous part can be rewritten using elif statements:     
num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3: 
    print("Three")
else: 
    print("Something else")

# As you can see in the example above, a series of if elif statements can have a final else block, which is called if none of the if or elif expressions is True.

# The elif statement is equivalent to an else/if statement. It is used to make the code shorter, more readable, and avoid indentation increase.    





















            
        
        
