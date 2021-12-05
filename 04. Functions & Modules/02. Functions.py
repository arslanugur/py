# In addition to using pre-defined functions, you can create your own functions by using the def statement.
# Here is an example of a function named my_func. It takes no arguments, and prints "three" three times. 
# It is defined, and then called. The statements in the function are executed only when the function is called.
def my_func():      # The code block within every function starts with a colon (:) and is indented.
    print("three")  # print("spam\n" * 3)
    print("three")
    print("three")

my_func()

# Second way:
def my_func(): 
  x = 0 
  while x < 3: 
    print("three") 
    x = x+1

my_func()

# Third Way:
def my_func(): 
  for x in range(3): 
    print("three") 

my_func()

# Example: to define a function named hello:
def hello():
  print("Hi!")

# 1. A function is defined by a keyword 'def' 
# 2. The name of the function is followed by two parentheses, which may or may not have variable/s (which are called arguments of the function). 
# 3. After the name & parentheses, there is need to put a colon ':' between a function name & its body. 
# 4. After colon, break the line & indent what the function must do. 
# 5. Lastly, define the output of the function, eg 'print()' or keep the output for future use using 'return' 
# 6. Call the function A good way of recalling what the function does. 
#     (a) Imagine you have a pet (define it) - say its a "cat". This becomes the function name. 
#     (b) What does it do when its name is called. Maybe it says "meow". That is what goes into the code block 
#     (c) Call it "cat!" when it hears its name it says "meow"!



# You must define functions before they are called, in the same way that you must assign variables before using them. 
hello()

def hello():
    print("Hello world!")
#





# ADVANCED EXAMPLES
# Example: BMI
# This strip of code computes the BMI (Body Mass Index) of an individual using values received for Height (in metres) and Weight (in kg).
def bmi_calculator(W, H, indiv_name):
    bmi = W/H**2

    print ("Hello " + indiv_name + ", your BMI is " + str(round(bmi, 2)) + ".")

    if bmi < 18.5:
        print ("You are UNDERWEIGHT.")
    elif bmi >= 18.5 and bmi < 25:
        print ("You have a HEALTHY WEIGHT.")
    elif bmi >= 25 and bmi < 30:
        print ("You are OVERWEIGHT.")
    elif bmi >= 30 and bmi < 35:
        print ("You are OBESE.")
    elif bmi >= 35 and bmi < 40:
        print ("You are SEVERLY OBESE.")
    else:
        print("You are MORBIDLY OBESE.")
        
        
bmi_calculator (60, 1.75, "Joseph")
    # Edit the arguments given to diplay a different result.   


# Example: Which other set of whole numbers fulfil Pythagoras' Theorem?
import numpy as np 
import math


def pyth_triple_finder(a,z):
# Function to generate Pythagorean Triples within the range of numbers a, and z.
    base = list(np.array(list(range(a,z)))**2)
    p_triple =[]

    for square in base:
        max_num = base.index(square)
        for i in range(max_num):           
            for j in range(max_num):
                if (base[i] + base[j+1]) == square:
                    pyth_triple = sorted( [math.sqrt(square), math.sqrt(base[i]), math.sqrt(base[j+1])] )
                    if pyth_triple not in p_triple:
                        p_triple.append(pyth_triple)
    
    print ('The Pythagorean Triples in the selected range are:')

    # To return the results...
    pt_array = np.array(p_triple)
    p_triple0 = list(pt_array.astype(int))
    
        # To see the results...
    for i in range(len(p_triple0)):
        print (p_triple0[i])
        
    return p_triple0
# Calling this function with the limits specified as arguments will result in the sets of Pythagorean triples within that range. 

# Calling the function:
pyth_triple_finder(1,11)




# Example: Diamonds
# These functions do the same thing, create a diamond with the specified size. 
# If size (n), is odd, it creates a diamond of size n, else, a diamond of size n-1.
def diamonds1 (n):
    n = (n - 1) if n%2==0 else n
    mid = '* '*(n)
    l = list(range(1, n, 2))
    for num in l:
        print (('  '*((n-num)//2))+('* '*num))
    print (mid)
    for num in l[::-1]:
        print (('  '*((n-num)//2))+('* '*num))


diamonds1(9)

# Make space...
print('')

def diamonds2 (n):
    n = (n - 1) if n%2==0 else n 
    i = 1
    while i < n:
        print (('  '*((n-i)//2))+('* '*i))
        i += 2      
    while i > 0:    
        print (('  '*((n-i)//2))+('* '*i))
        i -= 2

diamonds2(9)

# Make space...
print('')

def diamonds3 (n):
    size = n*2 if n%2!=0 else (n-1)*2
    temp = ["{:{}{}}".format('* '*num, '^', size) for num in range(1,(n+1),2)]
    for line in temp: print (line)        
    for line in temp[-2::-1]: print (line)

diamonds3(9)



