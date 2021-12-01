# Conditional Statements
# Conditional statement blocks: if - else
# Until now, passed from a code block to another block
# Now, passing with a condition from a code block to another block: true, false
# to change the way of app

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


# if "username" is wrong, you can send "password id wrong" to the user
# Purpose: to transmit certain code blocks under certain conditions 
# Example:
if 3>2:     # there must be a "true" or "false" value from the conditon
            # print is used for a certain conditional statement
    print('welcome back')
# if 3 > 3  # if it were like that, it wouldn't work
# if 3 == 3 # 'welcome back'
# if True   # 'welcome back'


# Example:
isLoggedIn = True   # user logged in?
if isLoggedIn:
    print('LoggedIn')

# Second Way
if isLoggedIn == True:  # true == true
    print("LoggedIn")   # always to tab once for print
    
    
# Example: Define a variable 
username = 'chanchan'
password = '123456'
isLoggedIn = (username == 'chanchan') and (password == '123456') 
# two comparisons is done, username equals chanchan?
# two questions must be true, then operator sends true
# to generate a value of bool type using operator 
if isLoggedIn:
    print('Welcome Home')


# Example:
username = 'arslanugur'
password = '123456'
if (username == 'arslanugur') and (password == '123456'):
    print('Password is confirmed')
# your info is wrong in if statement, else activates
else:
    print('You dont remember your name or number?!')


# Example: Which one is wrong?: username or password? What if the user wants to know?
username = 'arslanugur'
password = '123456'
if (username == 'arslanugur'):
    if (password == '123456'):
        print('thats it')
    else: # what if the password is wrong, because if-else blocks is only about password)
        print('your passed wrong way')
else:
    print('You dont remember your name?!')
# can be easier with the command "elif"


# Example:
temp = -5
freezing = 0
raining = False
snowing = True
if temp < freezing and (raining == True or snowing == True):
    print('Bad weather!')

temp = 10
if temp >= 10:
    print('Warm')
if temp >= 20:
    print('Hot')



