# You can use if statements to run code if a certain condition holds.
# If an expression evaluates to True, some statements are carried out. Otherwise, they aren't carried out.
# An if statement looks like this:
if expression:
   statements

# Python uses indentation (white space at the beginning of a line) to delimit blocks of code. 
# Depending on program's logic, indentation can be mandatory. As you can see, the statements in the if should be indented.

# In Game Design
# In-String operations is essential to most games! - 
# It is useful for game mechanics like upgrades, leveling, ranking, and unlocking new things!
# Examples: 
# if Lancelot defeated the dragon: P1 won the game 
# if P1 is level 72: P1 unlocks perk Night Vision 
# if P1 beats level 1: P1 unlocks level 2

# Example:
age = float(input("Enter age: "))
print(age)

if age < 18: 
  print("Sorry! You are not eligible to vote") 
else:
  print ("You can Vote! ")
     
# Be always careful while coding in Python due to indentation. You have tackled many "indentation error" in a code.    
# Indent = Tabs

# http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html

# Example:
weight = float(input("How many pounds does your suitcase weigh? ")) 
if weight > 50: 
  print("There is a £25 charge for luggage that heavy.") 
  print("Thank you for your business.")
  
# The if statements are like doors, when you open them you have to come in
# All lines below "if", belonging to the statement. 


# Here is an example if statement:
if 10 > 5:
    print("10 greater than 5")

print("Program ended")

# The expression determines whether 10 is greater than 5. Since it is, the indented statement runs, and "10 greater than 5" is output. 
# Then, the unindented statement, which is not part of the if statement, is run, and "Program ended" is displayed.

# Notice the colon at the end of the expression in the if statement
y = int(input("enter your d.o.b. year\n")) 
print("your age is : ",2021-y)

# Example:
a = 2018 
b = input() 
if a < int(b): 
    print ("invalid birth date")
    
else: 
    print (str(a - int(b)) + " years")
    
# Example:
spam = 7

if spam > 5:
   print("five")

if spam > 8:
   print("eight")

# To perform more complex checks, if statements can be nested, one inside the other.
# This means that the inner if statement is the statement part of the outer one. This is one way to see whether multiple conditions are satisfied. 

# Example:
num = 12
if num > 5:
    print("Bigger than 5")          # Bigger than 5
    if num <=47:
        print("Between 5 and 47")   # Between 5 and 47
        
  # Indentation is used to define the level of nesting.
  # Inner if statements runs only if they're True as first one. Also, don't forget that if statement runs only when it's True.  
  
# Example:
num = int(input('Enter a number: ')) 
if num >= 5: 
    print("Bigger than 5") 
    if num <=47: 
        print("Between 5 and 47") 
    else: 
        print("Sorry Number is not between 5 and 47")
        
    
# Example:
x = int(input("Enter score:"))

if x >= 30:
    print("F")
if x >= 50: 
    print("C") 
if x >= 60: 
    print("B") 
if x >= 70: 
    print("AB") 
if x >= 100:
    print("A")
        
# Example:
num = 7

if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7") # 3


