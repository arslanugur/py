# SECTION 1: Function Arguments
# Python allows to have function with varying number of arguments.
# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. 
# The arguments are then accessible as the tuple args in the body of the function.
# Example:
def function(named_arg, *args):
    print(named_arg)                # 1
    print(args)                     # (2, 3, 4, 5)

function(1, 2, 3, 4, 5)

# The parameter *args must come after the named parameters to a function.
# The name args is just a convention; you can choose to use another.

# Example:
def my_func(x, *args): 
  print(x) 
  print(args)

my_func(8) # 8 ()
# 8 is a named argument so it is passing directly to function.... 
# and bcz while calling the function no value is passing to *args thats why it will print an empty tuple

# Example:
# You need to put the individual team names in quotation marks to make them strings. 
# Otherwise, they are variables that you have not defined.
def current_team(team_name, *players_name): #Remember to put a space between parameters according to PEP! 
  print(team_name) 
  print(players_name)
  
current_team("India", "Sachin", "Sehwag", "Ganguly") # Output: India ('Sachin', 'Sehwag', 'Ganguly')

# Example:
def my_func(x, *args): 
  print(x) 
  print(args)
  
my_func(999, 1, 2, 3) # OUTPUT: 999 (1, 2, 3)
# you can use *args alone without a named argument

# Example:
def function(*args):
  print(args)
  
function(1,2,3,4,5) # Output : (1, 2, 3, 4, 5)

# Example:
def function(x, y, food="pizza"): 
  print(food) 
  print(x) 
  print(y)
  
function(1, 2)
function(3, 4, "tacos") # output: pizza 1 2 tacos 3 4

# Example:
def multiply(first,*args): 
  for i in args: 
    print(i*first) 
    
multiply(5,2,3,4,5,6) # Result: 10 15 20 25 30

# It would also have been helpful for reading the documentation, which has been confusing me for months precisely because it has things like *args and **kwargs in it!
# Kwargs is for dictionary arguments in python


# Example:
def f(x, *y): 
  return x + y 
f(1, 2, 3, 4, 10000) # will return error: TypeError: unsupported operand type(s) for +: 'int' and 'tuple', 
# so we have to ''unpack'' tuple in some way (for this case) to perform desired maths operations. 
def f(x, *y): 
  return x + sum(y) 
f(1, 2, 3, 4, 10000) # result: 10010 --- 1 + sum(2, 3 , 4, 10000)

# When you define function with parameters that involve '*', Python treats it like tuple (when you call function). 
# As it takes (in above example), parameter x which is '1' and parameter(s) '*y' which is everything else.
# '*' in function definition (to repeat) mean that you can call as many arguments as you want. 
# BUT in this case you cannot sum integer and tuple directly, so you have first to sum these numbers in tuple and then to add that to integer. 
# Thats why we have to write sum(y) as '*y' is tuple

# You can actually use named parameters after *args but they become keyword-only arguments. 
def spam(*eggs, egg): 
  print(egg) 
spam(1, 2, egg=3) #3 
spam(1, 2, 3) #TypeError spam() needs keyword-only argument egg
  

# To understand this, let's try the code without * : 
def function(named_arg, args): 
  print(named_arg) 
  print(args) 
  
function(1, 2, 3, 4, 5) # Output : TypeError: function() takes 2 positional arguments but 5 were given 
# This means that you said in line 1 that function has 2 arguments (named_arg , args) while in line 5 you said that function has 5 arguments (1, 2, 3, 4, 5) 
# The importance of the * is that it makes the argument after it a tuple containing all remaining values.


# This is useful for creating subclasses with additional __init__ arguments or assignments. 
# Example:
class SubClass(Class): 
  def __init__(self, new_arg, *args, **kwargs):   # **kwargs (standing for keyword arguments) allows u to handle named arguments that u haven't defined in advance.
    super(Class, self).__init__(*args, **kwargs) 
    self.new_assignment = new_arg
#

# Example:
def function( named_arg, b, *a): 
  print(b) 
  print(a) 
  print(named_arg) 
  
function(44, "g", 2,6,7) # Output: g (2,6,7) -> Tuple 44

# Example:
def function(named_arg, *args): 
  print(named_arg) 
  print(args) 
  
function((1,2,3),1, 2, 3, 4, 5) # output: (1,2,3) (1,2,3,4,5)


# Example:
def my_funct(named_arg, *args): 
  print(named_arg) 
  print(args) 
  
my_function(1, 2, 3, 4, 5) 
print(named_arg) = 1 
# It’s much more too easy peasy that (named_arg) will always be defined from the first num inside a function. 
# In this example: 
function(1, 2, 3, 4, 5) 
print(named_arg) = 1 
print(args) = (2, 3, 4 , 5) 
# it’s much more complexer and the (*args) got not installed as decoration too !! 


# It's important that using *args enables you to pass an arbitrary number of arguments to function ❗❗❗ 
def fun(*args): 
  print(args) 
  
fun() # ( ) fun(1) # (1,) fun(1, 2) # (1, 2) # e.t.c.


# How is *args accessed inside a function? -- as the tuple args
# Why is it accessible as a Tuple? Because Tuples in Python are immutable. 
# Arguments are given from "outside" each time when you calling function. So it should be tuple, because it couldn't be changeable.

# A quick example of using *args:
print("Get the average number:\n") 
number_1 = int(input("1st number:\n>>")) 
number_2 = int(input("2nd number:\n>>")) 
number_3 = int(input("3rd number:\n>>")) 
number_4 = int(input("4th number:\n>>")) 
number_5 = int(input("Give me last number:\n>>")) 
def average(greeting, *args): 
  print(greeting)
  print(sum(args)/len(args)) 
  
average("\nHere is your average:", number_1, number_2, number_3, number_4, number_5)

# The arguments are then accessible as the tuple args in the body of the function. 
# And you can notice that the content inside the green box is the distinguishing of *args and args

# You can use any word after (asterisk)* e.g.: *arg, *args, *arguments, *any_words etc. 
# Remember starred expressions are only allowed as assignment targets and as star-args in function call, using them anywhere else is an error
# The asterisk basically means "look into" that object and unpack it. It is used for unpacking values in a object instead of using the object. 
# A function(mylist) will have a list as argument whereas a function(*mylist) will have all the values in the list as arguments. 
# For a dictionary, * will give access to the keys while ** will give you access to the values attached to the keys. 

# So the "tuple *args" makes no sense, only args can be a variable (here a tuple). *args means "unpack arg (whether it is a tuple a list or any container object)"


# SECTION 2: Default Values
# Named parameters to a function can be made optional by giving them a default value.
# These must come after named parameters without a default value.
# Example:
def function(x, y, food="spam"):
    print(food)

function(1, 2)        # spam
function(3, 4, "egg") # egg
# In case the argument is passed in, the default value is ignored.
# If the argument is not passed in, the default value is used.

# so when print(food) is called it runs the first function ie (x , y food = spam) as its specified to print "spam" 
# and the second argument when run prints "egg" as it is declared in the second function?
# 1 goes to x, 2 goes to y then x and y takes 3 & 4 accordingly and result is egg

# Example:
# In place of the default value, we can pass integer too... def function(x,y,food="spam"): print(food) function(1,2) function(3,4,5) Output : spam 5

# If you have more than one optional argument and you want to skip one, you can use the following syntax: 
def function(x, y, food = "spam", drink = "water"): 
  print(food) 
  print(drink) 
  
function(1, 2) 
function(3, 4, "egg") 
function(1, 2, drink = "dye")

# From what I understood, since function is (x, y, food="spam") and all function does is print(food), Python will ignore the first two arguments. 
# Thus, you'll only see spam and egg in the output. You might also try pasting this to see if it's clearer: 
def function(x, y, food="spam"): 
  print(food) 
  print(x,y) 
  
function(1, 2) 
function(3, 4, "egg") # output: spam 1 2 egg 3 4

# Example:
import math 
def log(x, base=10): 
  return 

math.log(x,base) 
print(log(100))   # 2
print(log(100,2)) # 10
# log(1024, 2) = 10
# log(100, 2) = somewhere between 6 and 7.

# Example:
from math import log 
for i in range(1, 101): 
  print(log(i, 2))
#

# One important thing to mention is that the default value should be IMMUTABLE (unless you know what you are doing)! 
# Otherwise it will be shared for all the calls of this function. 
# Be aware of this, it may confuse you. One common mistake is to set an empty list like this: 
def find_less_than(x, l, found_so_far=[]): 
  for i in range(x): 
    if i in l: 
      found_so_far.append(i) 
      return found_so_far 
print(find_less_than(2, [1, 2, 3])) 
print(find_less_than(5, [5, 6, 7])) # It will produce: [1] [1]


# Some practical example: 
def circle_volume(r, pi=3.14, c='cm'): 
  return str(round(2 * r * pi)) +' '+ c print(circle_volume(5)) 
# 31 cm # here, we only needed to call first arg. r print(circle_volume(5, c='km')) 
# 31 km # here, we wanted to change measure unit so we had to name default arg and change it in function call. 
# In case that we just typed 'km' it would affect first default value which is 'pi=3.14'. print(circle_volume(5, 2)) 
# 20 cm # here we changed first default value but kept intact other one


# Here is an example. 
# class calculates the perimeter of a rectangle 
# if h and w are not given then they are 10 each 
# if Perimeter object is created with one parameter it replaces h = 10 
# if Perimeter object is created with two parameters they replace h = 10 and w = 10 
class Perimeter(object): 
  def __init__(self, h = 10, w = 10): 
    self.h, self.w = h,w def 
    rectangle(self): 
      perim = self.h*2 + self.w*2 
      return perim # h = 7, w = 10 
    
a = Perimeter(7) # h = 4, w = 9 
b = Perimeter(4, 9) # h = 10, w = 10 
c = Perimeter() 
print(a.rectangle()) 
print(b.rectangle()) 
print(c.rectangle())


# Example:
def function(x, y, food="spam"): 
  print((x+y)*food) 
  
function(1, 2) 
function(3, 4, "egg") # returns: spamspamspam eggeggeggeggeggeggegg

# Example:
func(x,y,food='samosa'): ✅
func(x,food='samosa',y): ❌


# What is wrong with this function definition? -- A non-default argument follows a default argument.
def function(x, y = 7, z, *argums): 
# *args is called *argums, *argums is the last argument


# There is two use case for this: 
# 1. Suppose *args is passed after default argument. 
# 2. Suppose non-default argument is passed as well after default one. 
# 1. if we use *args after default arguments. 
def function(x,y,food="spam", *args): 
    print("food : ",food) 
    print("args : ",args)
function(1,2) 
function(3,4,"egg") 
function(3,4,5) 
function(3,4,"egg",5,6) 
function(3,4,"egg","bread",6) 
"""
Output:
food :  spam
args :  ()
food :  egg
args :  ()
food :  5
args :  ()
food :  egg
args :  (5, 6)
food :  egg
args :  ('bread', 6)
"""

# 2. Suppose non-default argument is passed as well after default one. 
def function(x,y,food="spam",z,*args): 
    print(food) 
function(1,2) 
function(3,4,"egg") 
function(3,4,5) 
function(3,4,"egg",5,6) 
function(3,4,"egg","bread",6) # Output: File "named_func.py", line 1 def function(x,y,food="spam",z,*args): 
                              #         SyntaxError: non-default argument follows default argument
#


# Example:
def function1(named_arg, food = "spam", *args): 
    print(named_arg) 
    print(food) 
    print(args) 
    
function1(1, 2, 3, 4, 5, "egg") # Output: 1 2 (3,4,5,egg) 

def function2(named_arg, food = "spam", *args): 
    print(named_arg) 
    print(food) 
    print(args) 
    
function2(1, 2, 3, 4, 5, food = "egg") # Output: TypeError: function2() got multiple values for argument 'food' 
def function3(named_arg, *args, food = "spam"): 
    print(named_arg) 
    print(food) 
    print(args) 
    
function3(1, 2, 3, 4, 5,"egg") # Output: 1 spam (2,3,4,5,egg) 

def function4(named_arg, *args, food = "spam"): 
    print(named_arg) 
    print(food) 
    print(args) 
    
function4(1, 2, 3, 4, 5,food = "egg") # Output: 1 egg (2,3,4,5)


# Example: Non default arg cannot follow a default arg ! 
def fun1(a="who is you", b="True", x, y): 
    print(a,b,x,y) # File "<stdin>", line 1 SyntaxError: non-default argument follows default argument
#


  
# SECTION 3: Function Arguments
# **kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.
# Example:
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)                       # {'a': 7, 'b': 8}

my_func(2, 3, 4, 5, 6, a=7, b=8)

# a and b are the names of the arguments that we passed to the function call.
# The arguments returned by **kwargs are not included in *args.

# Example:
def my_func(x, y=7, *args, **kwargs): 
    print(x)        # 2
    print(y)        # 3
    print(args)     # (4, 5, 6)
    print(kwargs)   # {'a': 7, 'b': 8}
    
my_func(2, 3, 4, 5, 6, a=7, b=8)

# Example:
# The only way to print the Y's default value is to pass only one argument to this function. 
def my_func(x, y=7, *args, **kwargs): 
    print(x) 
    print(y) 
    print(args) 
    print(kwargs) 
    
my_func(2) # Then you will see: 2 7 [] {} 

# Example:
# You can use only one print function: 
def my_func(x, y=7, *args, **kwargs): 
    print("x = {}, y = {}, args = {}, kwargs = {}".format(x, y, args, kwargs)) 
    
my_func(2, 3, 4, 5, 6, a=7, b=8)


# Example:
def my_func(x,*args,y=7, **kwargs): 
    print(x) 
    print(args) 
    print(y) 
    
my_func(2,3,4,5) # OUTPUT: 2 (3,4,5) 7 # default value of y


# Its very useful when you want to call a function and dont remember where to put what as a parameter. 
# Eg suppose there is a function (myFunc) expecting a boolean, an integer and a string. 
# Now you can use **kwargs and pass them as : myFunc(my_str='CD', my_bool=True, my_int=5). The names will follow a standard convention.

# https://stackoverflow.com/questions/37909719/understanding-function-arguments-in-python/37910898#37910898

# ⭐args & ⭐⭐kwargs: Demystified https://realpython.com/python-kwargs-and-args/


# Use of *args 
def use_of_args(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2)
    print("arg3:", arg3) 
    
args = ("TWO", 3) 
use_of_args(1, *args) # Output : arg1: 1 arg2: TWO arg3: 3 

# Use of **kwargs 
def use_of_kwargs(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3)
# 
kwargs = {"arg2": "TWO", "arg3": 3} 
# you can pass this too, order doesn't matter. 
kwargs = {"arg3": 3, "arg2": "TWO"} 
use_of_kwargs(1, **kwargs) # Output : arg1: 1 arg2: TWO arg3: 3


# Example:
def function(*args, **kwargs): 
    print(args) 
    print(kwargs) 
    
function() 
function(1, a=1) 
function(1,2, a=1,b=2) # e.t.c output: () {} (1,) {'a': 1} (1, 2) {'a': 1, 'b': 2}


# Example:
def my_func(x, y=6, *args, **kwargs): 
    print(x) 
    print(y) 
    print(args) 
    print(kwargs) 
    
my_func(48, g=0) # OUTPUT: 48 6 () {'g': 0}

# Example:
def my_func(x, y= 7, *args, **kwargs): 
    print("x= {}".format(x)) 
    print("y= {}".format(y)) 
    print("args= {}".format(args)) 
    print("kwargs= {}".format(kwargs)) 
    
my_func(2, 3, 4, 5, 6, a= 7, b= 8) # OUTPUT: x= 2 y= 3 args= (4, 5, 6) kwargs= {'b': 8, 'a': 7}

# In case you don't want to change the value of y; 
def my_func(x, *args, y=7, **kwargs): 
    print(x) 
    print(y) 
    print(args) 
    print(kwargs) 
    
my_func(2, 3, 4, 5, 6, a=7, b=8) # 2 7 (3, 4, 5, 6) {'a': 7, 'b': 8}


# Example:
def my_func(*args, **kwargs): 
    print(*args)    # (2, 3, 4, 5, 6)
    print(kwargs)   # {'a': 7, 'b': 8}

my_func(2, 3, 4, 5, 6, a=7, b=8)


# What kind of object is kwargs?  -- a dictionary
# *args --> tuple 
# **kwargs --> dictionary

# Example:
def function(*args, **kwargs): 
    print(args)     # ()
    print(kwargs)   # {}
    
function()

# Example:
def my_func(x, y=7, *args, **kwargs): 
    print(x) 
    print(y) 
    print(args) 
    print(kwargs) 
    
my_func(2, 3, 4, 5, 6, a=7, b=8) # 2 3 (4, 5, 6) {'a': 7, 'b': 8} 
# **kwargs is actually one of the PARAMETERS of the my_func function. 
# However, from the above ☝👆 it's clear that print(kwargs) OUTPUTS the DICTIONARY {'a': 7, 'b': 8}. 
# Hence, the code kwargs itself RETURNS a DICTIONARY. So, kwargs is really a DICTIONARY.

# Recap: A single asterisk (*) - *args is a 'Tuple' argument A double asterisk (**) - **kwargs is a 'dictionary' KeywordArgument


# Example:
def my_func(x, y=7, *args, **kwargs): 
    print(kwargs) 
    print(*kwargs) 
    
my_func(2, 3, 4, 5, 6, a=7, b=8) # {'a': 7, 'b': 8} a b




