# Boolean logic is used to make more complicated conditions for if statements that rely on more than one condition.
# Python's Boolean operators are and, or, not.
# The and operator takes two arguments, and evaluates as True if, and only if, both of its arguments are True. Otherwise, it evaluates to False. 
print(1 == 1 and 2 == 2)  # True
print(1 == 1 and 2 == 3)  # False
print(1 != 1 and 2 == 2)  # False
print(2 < 1 and 3 > 6)    # False

# Boolean operators can be used in expression as many times as needed.

# Example:
if (1 == 1) and (2 + 2 > 3):
  print("true")
else:
  print("false")  # true


  
# BOOLEAN OR
  # The or operator also takes two arguments.
  # It evaluates to True if either (or both) of its arguments are True, and False if both arguments are False
  # Example:
print(1 == 1 or 2 == 2) # True
print(1 == 1 or 2 == 3) # True
print(1 != 1 or 2 == 2) # True
print(2 < 1 or 3 >  6)  # False

  # Besides values, you can also compare variables.

# Example:
age = 18 
money = 1000
if age > 17 or money <= 500:
  print ('Welcome to the bar')  # Welcome to the bar
elif age < 18 or money < 999:
 print ('Go Home')


# BOOLEAN NOT
  # Unlike other operators we've seen so far, not only takes one argument, and inverts it.
  # The result of not True is False, and not False goes to True
print(not 1 == 1) # False
print(not 1 > 7)  # True

  # You can chain multiple conditional statements in an if statement using the Boolean operators.

# Example:
if not True:
   print("1")   # the result of "not true" is "False". So, if it's False, in an if statement, it is not executed (unless it the case in which it is a condition in an elif)
elif not (1 + 1 == 3):
   print("2")   # 2
else:
   print("3")
    
    
# DeMorgan's theorems: 
  (not a) or (not b) == not(a and b)
  (not a) and (not b) == not(a or b) 
# Distributivity: 
  (a and b) or (a and c) == a and (b or c) (a or b) and (a or c) == a or (b and c) 
# Involution: 
  not(not a) == a 
# Absorption: 
  a or (a and b) == a a and (a or b) == a 
# Commutativity: 
  a and b == b and a a or b == b or a 
# Associativity: 
  a and (b and c) == (a and b) and c a or (b or c) == (a or b) or c
# Dominance: 
  a and False == False a or True == True 
# Identity: 
  a and True == a a or False == a 
# Idempotence: 
  a and a == a a or a == a 
# Complementarity: 
  a and not a == False a or not a == True         # (a and b) and (a and c) == a and b and c. 
# Don't forget that `and` has precedence over `or`
  

# Example:
x = input("Never gonna ")
print(x)
if x == "give you up" or x == "let you down" or x == "run around and desert you" or x == "make you cry" or x == "say goodbye" or x == "tell a lie and hurt you":
    print ("True")
else:
    print ("False")
    
    
# Example:
x = int(input("Is your age older than 18?")) 
if x == 18: 
    print("You are 18!")
elif x < 18 and x > 0: 
    print("No") 
elif x >= 100 or x <= 0: 
    print("You can't be serious")
else:
    print("Yes")


# Example:
age=int(input("Please Enter Your Age Here :"))
if age<=0:
    print("You haven't been Born Yet !")
if age<=17 and age>0:
    print("You are a Minor & ")
if age<=3:
    print("You are a Toddler")
if age<=5 and age>3:
    print("You are a Preschooler")
if age<=12 and age>5:
    print("You are a Gradeschooler")
if age<=17 and age>12:
    print("You are a Teen")
if age>=18:
    print("You are an Adult & ")
if age<=20:
    print("You are a Young Adult")
if age>=21 and age<70:
    print("You are a Mature Adult")
if age>=70 and age<=100:
    print("You are a Senior Citizen")
if age>100:
    print("You are Immortal !")


# Example:
x=int(input('What year were you born? ')) 
if (x>=1944 and x<=1964): 
    print ('Hey Boomer!') 
elif (x>=1965 and x<=1979): 
    print ('You are a booring Gen X!') 
elif (x>=1980 and x<=1994): 
    print ('You are a lazy Milennial!') 
elif (x>=1995 and x<=2015): 
    print('Hey Gen Z!') 
    
    
# Q Example:
a = str(input("Are you a girl or a boy ?\n")) 
b = int(input("How old are you ?\n")) 
if (a == "girl" and b >= 18): 
  print("Hello beautiful\n")
else: 
  print("Goodbye !!\n")
    
# Q Example:
username = str(input("Set a Username: "))
print(username)
password = str(input("Set a Passowrd: "))
print('*****')
previoususername = str(input("Your Username: "))
print(previoususername)
previouspassword = input("Your Password: ")
print('*****')
if (previoususername == username and previouspassword == password):
    print("Login successfully")
elif (previoususername != username and previouspassword == password):
    print ("Your username is incorrect")
elif (previoususername == username and previouspassword != password):
    print("Your Password is incorrect")
else:
    print("Login failed")
    
    
# Q Example:
hour = int(input())
day = int(input())
if 10 <= hour < 21 and 1 <= day <= 5:
    print("Open")
else:
    print("Closed") 
    
# Q Example:
hour = int(input()) 
day = int(input()) 
x = (hour >= 10 and hour <= 21) 
y = (day >= 1 and day <= 5) 
if (x == True and y == True): 
    print("Open") 
else: 
    print("Closed")


    
