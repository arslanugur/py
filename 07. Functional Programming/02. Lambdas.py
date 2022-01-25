# SECTION 1
# Creating a function normally (using def) assigns it to a variable automatically.
# This is different from the creation of other objects - such as strings and integers - which can be created on the fly, without assigning them to a variable.
# The same is possible with functions, provided that they are created using lambda syntax. Functions created this way are known as anonymous.
# This approach is most commonly used when passing a simple function as an argument to another function. 
# The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, and the expression to evaluate and return.
# Code:
def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)

# Lambda functions get their name from lambda calculus, which is a model of computation invented by Alonzo Church.

# lambda -> keyword x -> input argument to the anonymous function. 2*x*x -> the expression to compute. 5 -> the function argument. Passed as x. 
# So basically we are defining a lambda function and calling it at the same time with the argument 5 I am not thinking too much on the applications of this at this time. 

# lambda is just unnamed funcion. it can be useful to perform any expression 
# If you dont know value or may be its variable 
# in this case you can use lambda if you want result of x**2+2*x this expression it can be achieved by lamda without any function.

# We use lambda functions when we require a nameless function for a short period of time. 
# In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments). 
# Lambda functions are used along with built-in functions like filter(), map() etc. 
# Example of a lambda function: 
double = lambda x: x*2 print(double(5)) # 10 
# Example of filter(): 
my_list = [1, 5, 4, 6, 8, 11, 3, 12] 
new_list = list(filter(lambda x: (x%2 == 0), my_list)) 
print(new_list) # [4, 6, 8, 12] 
# Example of map(): 
my_list = [1, 5, 4, 6, 8, 11, 3, 12] 
new_list = list(map(lambda x: x*2, my_list)) 
print(new_list) # [2, 10, 8, 12, 16, 22, 6, 24]c

# Lambda makes it possible to use small anonymous functions. 
# Lambdas are throw away functions used where they have been created NB:Lambda Syntax Lambda argument_list: expression. 
# 1.lists in lambda consists of a number of arguments separated by a comma 
# 2.expressions refer to the arithmetic expression using the list of arguments. 
#   Example: f = lambda x,y,: x+y f=(1,1) # 2

# The dfference between normal function and anonymous or lambda function : 
# 1- In Python, anonymous function (They are also called lambda function)is a function that is defined without a name. 
# 2- Normal functions are defined using the (def) keyword, Anonymous functions are defined using the lambda . A lambda function in python has the following syntax. 
# Syntax of Lambda Function: lambda arguments: expression Lambda functions can have any number of arguments but only one expression. 
# The expression is evaluated and returned. Lambda functions can be used wherever function objects are required. 

# What about comprehension lists using lambdas? 
# calculate cubes in the list from1 to 20.. 
cubes = [(lambda x: x**3)(x) for x in range(1, 21)] # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]


# Lambda is a single line function 
# Example: 
square = (lambda x: x**2) 
print(square(2)) # 4 because lambda 2: 2**2

# comparing lambda to a normal function
def normal(t): 
  return t**2
  
normal(2) # 4 
y= lambda x: x**2 # y(2) 4 


# SECTION 2
# Lambda functions aren't as powerful as named functions.
# They can only do things that require a single expression - usually equivalent to a single line of code.
# Examples: 
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4)) # 0

#lambda function 
print((lambda x: x**2 + 5*x + 4) (-4))  # 0

# In the code above, we created an anonymous function on the fly and called it with an argument.

# Note that a PERFECTLY FINE SUBSTITUTE code for the bit "print(polynomial(-4))" are the following. 
# Give them a try, and just observe how you'll surely get the exact same output. ;) "print((polynomial) (-4))" OR even: "print((polynomial)(-4))" 
# So, in the code "print(polynomial(-4))", the "polynomial" part of it may well be surrounded with parentheses, 
# so "polynomial" becomes "(polynomial)" instead, and yet not affect the output at all. 
# Now, just compare the following 2 lines: "print((polynomial) (-4))" print((lambda x: x**2 + 5*x + 4) (-4)) 
# So, (lambda x: x**2 + 5*x + 4) is just a FUNCTION, and its argument is (-4), SIMILAR to how (polynomial) is just a FUNCTION, and its argument is (-4)

# Lambdas are simple one line function code that makes your code simpler for example: 
# to add two numbers 
# using function def add(x, y): return (x+y) 
# using lambda lambda x, y: x+y

# The formula behind the problem is algebraically seen as x² + 5x + 4 
# It is worked out in the following manner: x**2 + 5*x + 4 where x=(-4) =(-4)**2 + 5*(-4) + 4 =16 + -20 + 4 = 0

# Lambda also works with multiple arguments: 
#named function 
def polynomial(x, a, b, c): 
  return a*x**2 + b*x + c
print(polynomial(6, 3, 4, 5)) # 137

#lambda function  
print((lambda x, a, b, c: a*x**2 + b*x + c) (6, 3, 4, 5))   # 137

# What's the MEANING/INTERPRETATION of "(lambda x: x**2 + 5*x + 4)"? 
# Perhaps something like: 
# An anonymous/TEMPORARY FUNCTION created on the fly (the lambda bit!), which demands just a single argument from you, parameterised by x, such that (the : bit!) 
# it evaluates and RETURNS the result of the expression x**2 + 5*x + 4, aka x² + 5x + 4 

# Why in the entry example ',' is used and here (). So here my try to explain the differnce in usage. 
print(my_func(lambda x: 2*x*x, 5)) 
# used as argument to function 'my_func' so ',' is used print ((lambda x: 2*x*x)(5)) 
# pass an argument directly to lambda function requires to pass them in own(), no ',' is used here. 
print((lambda x,y : x*y)(4,5)) 
# if lambda requires 2 arguments then again ',' is used but in combination with () 
print(lambda x: 2*x*x) 
# generates the lambda function 
A = (lambda x: 2*x*x) 
# Assign a name to a lambda function print(A(5)) 
# use it with function call syntax is also possible.


# Example:
print((lambda x: 6*x))        # <function <lambda> at 0x7f32d580fd30>
print(((lambda y: 3+y)(4)))   # 7

# You can also have default values in the parameters (but remember that the default parameters must come after all the non-default parameters), as in: 
print ((lambda x, y=3: (x*x, y*y)) (2)) # (4, 9) 
# you can also use other functions inside your lambda, and this is useful 
# because you do it all in one statement: from math import factorial print ((lambda x: factorial(x)+1) (4)) #outputs 25

# Example: to create a lambda function that returns the square of its argument, and call it for the number 8.
a = (lambda x: x*x) (8)

# "a" is the name of you function. The "(8)" is where you put the variable that your function is using and the middle part defines what the function is supposed to do. 
# So its X = x * x for x = 8 -> X = 8 * 8 -> X = 64 -> print(a(8)) # Output:64 
# another example is a= (lambda x: x+x) (2) -> print(a(2)) # Output: 4

# Example:
a = (lambda x:x*2)(5) 
print(a) # 10 ---> it means: x=5 and x*2=? it is 10


# Some examples:
def sqr(x): 
  return x*x 
print(sqr(2))   # 4
print((sqr)(3)) # 9 having () doesnt matter new_name = sqr 
# now we have one more name for sqr
new_name = lambda x: x*x*x
print(new_name(4)) # 64
# now new_name is the name for this lambda function ( x cube ) 
print(new_name(5)) # 125 
print((lambda x: x*x)(6))   # 36 here we call this lambda ( x square ) with argument

ş
# SECTION 3
# Lambda functions can be assigned to variables, and used like normal functions.
# Example: 
double = lambda x: x * 2
print(double(7))              # 14

# However, there is rarely a good reason to do this - it is usually better to define a function with def instead.

# Examples:
# lambda with 2 variables 
sum = lambda x, y: x + y 
print(sum(7,8))           # 15

# lambda without variables: 
print((lambda: 5)())      # 5

# lambda with 2 variables: 
print((lambda x, y: x + y)(1,2))  # 3


# Example:
double = lambda x: x * 2 
print(double(7)) 
print((lambda x: x*2) (7)) 
# BOTH of the above ↑ code blocks give the SAME OUTPUT. 
# Also, BOTH of the following ↓ code blocks give the SAME OUTPUT. 
sum = lambda x,y: x+y 
print(sum(7,8)) 
print((lambda x,y: x+y) # (7,8)) 
# I suppose the one line code block in real case is good for those who are lazy and/or want minimal lines of code overall for the sake of clarity/layout.

# lambda can use if within it. 
mayor = lambda x, y : x if x > y else y 
print (mayor(5,6)) # 6

# Those who care about efficiency, please keep in mind that "def" functions are very very faster than "lambda" functions, 
# especially when it comes to parametric integrations and diffrentiations. ✔️ Use def if you care about time.


# Lambda with an if statement 
l = lambda x: 'YES' if x%2 == 0 else 'NO' 
print (l(10))   # YES 
print (l(9))    # NO

 
# Nested lambda:
((lambda x:(lambda y: x+y))(9)) (4)


# Example:
double=lambda x:x*2 
print(double(7))        # 14
print(lambda x:x*2)     # --> with value x=7
print(7*2)              # 14


# Example:
triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))    # 13

# Explanations:
# First you have triple(3) which means ×*3=3*3=9 so you see add(triple(3),4) will be add(9,4)=x+y=9+4=13
# triple(3) x : x*3 9 = 3*3 so triple is 9 triple == 9 add (triple, 4) x, y : x + y 9, 4 :9 + 4 9 + 4=13 13
# triple = 3*3 (9) triple(add = 3 + 9) (13)

# triple = lambda x: x*3 add = lambda x,y: x+y print(add(triple(3), 4)) print((lambda x,y: x+y) ((lambda x: x*3) (3),4)) 
# BOTH of the above 2 code blocks give. the EXACT SAME output of 13. 

# triple(3) = lambda x: 3*3 = 9 Therefore triple(3) = 9 
# Print(add (9,4)) add = lambda x,y: x + y Where 9 and 4 are "x" and "y" respectively Therefore Add = lambda x,y : 9+ 4 = 13 The answer is 13



