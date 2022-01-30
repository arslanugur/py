# SECTION 1
# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions that you don't want to modify.
# Example:
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

# We defined a function named decor that has a single parameter func. 
# Inside decor, we defined a nested function named wrap. The wrap function will print a string, then call func(), and print another string. 
# The decor function returns the wrap function as its result.
# We could say that the variable decorated is a decorated version of print_text - it's print_text plus something.
# In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version altogether so we always got our "plus something" version of print_text.
# This is done by re-assigning the variable that contains our function:
# Example:
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

print_text = decor(print_text)
print_text()

# Now print_text corresponds to our decorated version.

# 1. it's not obvious why we need to use nested wrap() - it should be made clear in comments 
# 2. it's not obvious what does "single function can have multiple decorators" 
#    - does that mean one can use @dec1 @dec2 def func() and decorators will be applied like func=dec1(dec2(func)) or something else 
# 3. last question should be reconsidered - @mydec is not the same as myfunc=mydec(myfunc)

# (1):
def decor(func): 
  def wrap(): 
       print("============") 
       func() 
       print("============")
  return wrap

def print_text(): 
    print("Hello world!") 
    
decorated = decor(print_text) 
decorated() 

# (2): 
# Also, note that if I simply REPLACE these 2 lines code by just: print_text() Then I end up with only "Hello world!" in output, devoid of ANY decoration whatsoever. 
# Hence, what it REALLY means, is that the print_text() function ALONE FAILS to give its output of "Hello world!" WITH the DECORATION we desperately wanted. 
# It wasn't really inclusive. 
# So, the question is, 
# HOW do we EXTEND the FUNCTIONALITY of the FUNCTION print_text WITHOUT making any direct modification whatsoever to the function itself? 
# More clearly, knowing that print_text() outputs just "Hello world!" by itself, 
# HOW do we make the output ALSO include the DECORATION we're after, WITHOUT any direct modification to the print_text function ITSELF? 

# (3): 
# Answer: by simply RE-ASSIGNING the VARIABLE containing the print_text function. 
# Hence, print_text = decor(print_text) print_text() we use the 2 above lines of code. 
# Bit like saying, re-assign the function print_text such that it now would come PRE-DECORATED for us ;) every single time it's called. 
# Therefore, all of the following code actually gives the DECORATED output of "Hello world!".

# (4): 
def decor(func): 
    def wrap(): 
        print("============") 
        func() 
        print("============") 
    return wrap 
 
 def print_text(): 
    print("Hello world!") 
 print_text = decor(print_text) 
 print_text() 
 
# In fact, what's so nice is that, basically, I can now have LOTS of code blocks following the above, 
# and then suddenly have "print_text()" all by ITSELF appearing, 
# and YET be 100% assured that this very simple looking ONE Line of code actually was responsible for not only providing an output of "Hello world!", 
# BUT ALSO WITH the nice DECORATION to surround it and hence make it look "nice" as we presumably wanted

# Decorators provide a simple syntax for calling higher-order functions. 
# By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it. 
# Sounds confusing—but it's really not, especially after we go over a number of examples.

# This was a little easier for me to read. 
def a(function): 
    def b(): 
        print("first line") 
        function() 
        print("last line") 
     return b 

def c(): 
    print("middle line") 
c = a(c) 
c();

# The wrap function only exists to allow a return value. 
# Without it the function cannot be assigned to the variable print_text. 
# If you try to assign it, print_text will only receive the default return value of None and attempting to call the function will produce an error. 


# The wrap function is confusing. The idea seems to be to show us different possibilities, but the situation chosen is not so realistic. 
# For my first understanding of this lesson, I simplified like this, and the result is the same : 
def decor(func): 
    print("============") 
    func() 
    print("============") 
def print_text() 
    print("Hello word!")

decor(print_text)


# First: I think that it's better to write last two lines in this way: decorated_print_text = decor(print_text) decorated_print_text() 
# Second: notice that ‘cause decorators modify a function’s behaviors, they take some function as input and return another as output. 
# Now consider code: wrap function has been defined in decor and then was returned by this function. wrap function do print_text plus some other tasks. 
# So the output of decor is a decorated version of print_text function that can be pointed by some variable and called whenever you want. 
# In my code this is decorated_print_text function. Without defining wrap function you can not return a function from decor. 
# Here is a good explanation: https://realpython.com/blog/python/primer-on-python-decorators/


def what_to_decorate(your_input): 
    def how_to_decorate(): 
        print("="*len(your_input)) 
        print(your_input) 
        print("="*len(your_input)) 
    return how_to_decorate 

run_this = what_to_decorate(input()) 
run_this() 
# if the variable "run_this" is replaced by a REAL function, then the line "print(your_input)" could be it's argument.


# A decorator is a function that modifies another function using functions.*** 

# Decorators wrap a function, modifying its behavior. 
# https://realpython.com/primer-on-python-decorators/ 



# SECTION 2
# In our previous example, we decorated our function by replacing the variable containing the function with a wrapped version.
# Example:
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

print_text = decor(print_text)

print_text();


# This pattern can be used at any time, to wrap any function.
# Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
# If we are defining a function we can "decorate" it with the @ symbol like: 
# Example:
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text();

# This will have the same result as the above code.
# A single function can have multiple decorators.


# To understand the last statement about multiple decorators, try this: 
def decor(func): 
  def wrap(): 
    print("============") 
    func() 
    print("============") 
  return wrap 
  
def decor1(func): 
  def wrap1(): 
    print("**************") 
    func() 
    print("**************") 
  return wrap1 

@decor 
@decor1 

def print_text(): 
  print("Hello world!") 

print_text(); 
#


# Example:
def decor(func): 
  def wrap(): 
    print("============") 
    func() 
    print("============") 
  return wrap 
  
def decor1(func): 
  def t(): 
    print("ttt") 
    func() 
    print("tttt") 
  return t 
  
@decor 
@decor1 
@decor1

def print_text(): 
print("Hello world!") 
print_text();

# if you suspect a certain function f of one argument not to be correct, 
# add "@verbose" before "def f(x):" in your program, where def verbose(f): 
# def r(x): y=f(x) print ( "called with argument ",x) print("returned ",y) 
# return y return r every call of f will print what was entered and returned in f... 
# eg @verbose def s(x): return x**2 print(f(3)+f(4)) will output called with argument 3 returned 9 called with argument 4 returned 16 25 
# When f seems reliable, just remove "@verbose" before "def f(x):" 

# Example with two decorators within the same function
def decor(func): 
  def wrap(): 
    print("============") 
    func() 
    print("============") 
  return wrap 
  
@decor 

def print_text(): 

print("Hello world!") 

@decor 

def print_text2(): 
print("This is my world") 
print_text(); 
print_text2(); 


# It turns out that even though you're returning the wrapper, 
# You also need the inside of the wrapper to return something or you'll end up printing None in addition to your input, 
# or run code that results in a NoneType error when you attempt to call the function. 
# Here's what finally worked for me in the Uppercasing challenge: 
text = input() 
def uppercase_decorator(func): 
    def wrapper(text): 
    #your code goes here 
    return text.upper() 
    return wrapper 
    
@uppercase_decorator 

def display_text(text): 
    print(text) 
    print(display_text(text))
#

def decor(func): 
    def wrap(): 
        print("====") 
        func() 
        print("====") 
    return wrap         # Instead of: def decor(func): print("====") func() print("====")
#

# https://jeffknupp.com/blog/2013/11/29/improve-your-python-decorators-explained/

# Example:
def california(func): 
    def waves(): 
        print(44*"-") 
        func() 
        print(44*"-")
    return waves 
    
def texas(func): 
    def guns(): 
        print(72*"-") 
        func() 
        print(72*"-") 
    return guns 
    
@california 
def surf_report(): 
    print(" Your are lucky because it is barreling!") 
    
@texas 
def status(): 
    print(" Your are lucky because you'll get 50% off in all products at Walmart") 

a = input('Where do you want to go? \n' "California or Texas?\n") 
print("\nAs you chose " + a + "," + "\n") 
b = str(a) 
def choices(): 
    if b == "California": 
        surf_report(); 
    else: 
        if b == "Texas": 
            status(); 
        else: 
            print("you did not choose the right answer. \n \n Try it again!") 

choices();

# Which statement can be used to achieve the same behavior as my_func = my_dec(my_func)?    ---> @my_dec


# First Example Way:
def easy_decor(func):
    def my_style(): 
        print("============") 
        func() 
        print("============") 
    return my_style 

@easy_decor 
def print_text(): 
    print("Hello world!") 
    print_text();

# Second Example Way:
def easy_decor(func): 
    def my_style(): 
        print("============") 
        func() 
        print("============") 
    return my_style 

def print_text(): 
    print("Hello world!") 
    print_text = easy_decor(print_text) 
    print_text(); 
# So as you can see the only difference in these two ways of coding are "@easy_decor" and "print_text = easy_decor(print_text)"

# https://realpython.com/primer-on-python-decorators/



