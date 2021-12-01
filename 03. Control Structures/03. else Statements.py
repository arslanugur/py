# The if statement allows you to check a condition and run some statements, if the condition is True.
# The else statement can be used to run some statements when the condition of the if statement is False.

# As with if statements, the code inside the block should be indented.
x = 4
if x == 5:
    print("Yes")
else:             # Notice the colon after the else keyword.
    print("No")
    

# Example:
x = 10
y = 20 
if x > y:
    print('x is bigger than y')
else:
    print('yeah is beggie than x')


# Example:
# what if x and y are the same value, but the code remains the same --> the value in "else"
# to edit we need to change the operator --> if x >= y:
# but using the command "elif", would bbe more reasonable
x = 20
y = 20 
if x > y:
    print('x is bigger than y')
elif x == y:
    print('x and y are the same equal') 
# As the condition numbers increase, we can also increment the "elif" command in the same way to check each condition 
else:
    print('y is bigger than x')


# Example: input from the user
x = int(input('x: '))   # coming value from the input turns integer not to be seen as str 
y = int(input('y: '))
if x > y:
    print('x is bigger than y')
elif x == y:
    print('x and y are the same equal') 
else:
    print('y is bigger than x')


# Example: to take a value from the user
num = int(input('no: '))
if num > 0:
    print('number is positive')
elif num < 0:       # the number is smaller than 0 --> if the number is negative 
    print('number is negative')
else:               # for the other statement
    print('number is null/zero')

    
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
n = int(input("Enter a number"))
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


# Example:
num = 7 
if num == 5: 
    print("Number is 5") 
if num == 11: 
    print("Number is 11") 
if num == 7: 
    print("Number is 7") 
else: 
    print("Number isn't 5, 11 or 7")
    
    # 1. if statement: python uses if statement to run a programme if certain conditions hold 
    # 2. else statement: python runs else statement when a if stement is false 
    # 3.elif statement: elif statement is a simple form of else if statement 
    # and it is followed by a final else block never forget the colon (:) at the end of these statements
    
    # 'elif' means 'else if'. It is executed if the 'if' statement is not True. 
    # But, A 'nested if' is put inside another 'if block' and is executed if the outer 'if' is True.

# Example:
color = input() 
if color == 'red': 
    print(1) 
elif color == "green":
    print(2)
elif color == "black":
    print(3)
    
    
# Example:
sonic = 300

if sonic < 390: 
    print('sonic is getting faster')
elif sonic < 320: 
    print('sonic is walking fast') 
else: 
    print('sonic is not running now') 
# when the variable sonic is 300, 
# both sonic<32 and sonic<39 conditions are true. 


# Question Example:
w = float(input()) 
h = float(input()) 
bmi = w/(h**2) 
if bmi < 18.5: 
    print (" you are thin!") 
if 18.5 <= bmi < 25: 
    print ("you are normal") 
if 25 <= bmi < 30: 
    print ("get exercise!") 
if 30 <= bmi: 
    print ("you are overweight!")

    
# Question Example:    
def game(a,b): 
    human = a 
    comp = b 
    if human == "rock" and comp == "paper": 
        human = -1 
            print(human) 
        elif human == "rock" and comp == "scissors": 
        human = +1 
            print(human) 
        elif human == "paper" and comp == "rock": 
        human = +1 
            print(human) 
        elif human == "scissors" and comp == "rock": 
        human = -1 
            print(human) 
        elif human == "paper" and comp == "scissors": 
        human = -1 
            print(human) 
        elif human == "scissors" and comp == "paper": 
        human = +1 
            print(human) 
        elif human!= "rock" and human!= "paper" and human!= "scissors": 
            print("wrong choice, try again")
        elif comp!= "rock" and comp!= "paper" and comp!= "scissors": 
            print("network error") 
        game("scissors","paper")



  
