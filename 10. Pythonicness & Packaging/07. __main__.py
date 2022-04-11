# SECTION 1: __main__
# Most Python code is either a module to be imported, or a script that does something.
# However, sometimes it is useful to make a file that can be both imported as a module and run as a script.
# To do this, place script code inside if __name__ == "__main__".
# This ensures that it won't be run if the file is imported.
# Example:
def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")   #
#

# When the Python interpreter reads a source file, it executes all of the code it finds in the file. 
# Before executing the code, it defines a few special variables.
# For example, if the Python interpreter is running that module (the source file) as the main program, 
# it sets the special __name__ variable to have a value "__main__". 
# If this file is being imported from another module, __name__ will be set to the module's name.


# (1): I THINK that this mind-boggling lesson is trying to say the following perhaps in its own alien language. 
# There's a ton of Python code out there which are in the form of SCRIPTs that PERFORM some stuff by running/executing code. 
# You hit the RUN button, and bang! The code in the script gets run as usual and the script's code gets executed. 
# We've seen this a lot already. Also, there's a lot of Python modules out there. 
# Recall, MODULEs contain useful FUNCTIONS + VALUES, for example how the math module contained the functions cos sqrt as well as the value pi. 
# That's all a MODULE really is by the looks of it to me - just a bunch of useful FUNCTIONS + VALUES.
  
# You need to actually mess with files and import to understand what the lesson is about.
# Create a program, and try to use a function you defined in an other program by importing it. 
# Hopefully you'll see the problems and the interest of separating module from script
#   (script= any code that runs whenever you import a program, eg not functions which need to be called).

# just imagine this Programm and save it as test.py def function(): 
print("This is a module function") 
if __name__=="__main__": 
  print("This is a script") # Then open up a new file and write something like import test Or from test import function And then call function. 
# The stuff from if __name__ == main will not be executed

# (2): What this lesson is trying to teach in its language of its own, 
# hopefully, is how to actually CREATE a SINGLE Python file that can be treated in 2 ways - as a MODULE, 
# in the sense that you can import the whole .py file and then gain access to useful functions and/or values that you want, 
# as well as being able to run the whole .py file as if it were just an ordinary script like you've already seen and made many times. 2-in-1 kind I guess.
# BOTH abilities 1 AND 2 contained in just a SINGLE .py file:
# 1. Once you choose to IMPORT the whole .py file, 
# you right away gain access to useful functions and values, though NO actual code at all gets automatically EXECUTED/RUN automatically/right away after the IMPORT. 
# 2. Alternatively, you can simply RUN the whole .py file and observe it RUN like a usual ordinary SCRIPT that you've seen many times already so far. 
# BUT how do you actually CREATE such a .py file in the first place?
  
# That's misleading. All imported code gets executed. You place your script calls beneath if __name__ == "__main__": to execute as a script. 
# This is because when you execute a script solo, it runs as __main__. 
# When it's imported, the running program is __main__ so none of those executables get called.

# "Once you choose to IMPORT the whole .py file, you right away gain access to useful functions and values, 
# though NO actual code at all gets automatically EXECUTED/RUN automatically/right away after the IMPORT." This is wrong. 
# Code DOES automatically get run when imported. If you wish for your code to NOT get run when imported, you need to use functions and classes, 
# and place your calls to those functions/classes underneath the if __name__ == '__main__': test. 
# For example, File1 Print("Hello World") def Five(): print("5") File2 Import file1 
# When you run file2, it WILL run the code, but only will print "Hello World", since Five() was not called. You can call five via file1.Five()
    
# (3): Well, you just put the script code (all the code that you want to be actually EXECUTED after you RUN the .py file, 
# expecting probably some OUTPUT) just under the following line of code. 
# if __name__==__"main"__: 
# What gets placed ★just BELOW★ such a special line is to be considered as code which gets EXECUTED during RUNTIME of the .py file, 
# but NOT EXECUTED at all if you were to IMPORT the whole .py file as a MODULE. 
# In fact, what exactly PREVENTS the code ★just BELOW★ the special line from being executed 
# if you were to IMPORT the .py file as a MODULE is the very EXISTENCE of that special line, hence why it's SPECIAL in some sense I guess. 
# This is the REAL point of having that special line in!!! Also, what gets DEFINED ★ABOVE★ that special line
# I believe is to be considered as the functions + values you can gain access to using if you IMPORT the whole .py file as a MODULE.
    
    
# (4): Now, consider the following. Running it like an ordinary script, 
# we observe the OUTPUT of "This is a script" only, as shown. 
def function(): 
  print("This is a module function") 
  if __name__=="__main__": 
    print("This is a script") # OUTPUT: This is a script
# Suppose if I was in the middle of making my own .py file, 
# and I suddenly needed to bring in the very much USEFUL and difficult to define/construct function known as function(), 
# as DEFINED in the above code example. In this case, I would ideally like to IMPORT the .py file (containing the code) ABOVE as a MODULE. 
# This would allow me to gain access to the USEFUL function known as function(), 
# WITHOUT all of sudden having some code that gets out of nowhere EXECUTED against my will😭, namely the code print("This is a script").
        
# (5): Hence, by an IMPORT of the ABOVE .py file as a MODULE, 
# not only do I again access to the supposedly useful and hard-to-define/construct function known as function(), 
# but also there's absolutely no extra OUTPUT all of a sudden, namely no OUTPUT against my will of "This is script".

# 1) slightly modify 1st script in slide : def function(): print("This is a module function from",__name__ )
if __name__=="__main__": print("This is a script") function() you get output: 
# This is a script This is a module function from __main__ because function was defined while __name__ evaluated to __main__ 
# 2) now let's make a module from these instructions (in CP, type stuff below or open "ecscriptmodule.py" that I publicly saved) : 
### creating a module ### 
file="test.py"; f=open(file,'w') 
text=""" def function(): print("This is a module function from",__name__ ) if __name__=="__main__": print("This is a script") """ 
f.write(text); f.close() 
### module created ### import test ; test.function() 
# you get output This is a module function from test because function was defined in test environment; 
# moreover, "if" clause was skipped for same reason : __name__ evaluated to "test" 

# Basically, you can write some code (code A), save it, and import it as a module to another code (code B) you write. 
# As a module, you can only obtain the functions that are in code A. 
# Code A won't actually be run when imported into code B 
# (it's similar to how you can import math and only get the functions that you call as outputs when running, e.g., math.max()). 
# By itself, Code A will run just like any other code we've written so of.


# Example: *args
def func_1(x, y, food="spam"):
    x += 5
    food += "m"
    print(x, y, food)

func_1(1, 2)
func_1(3, 4, "egg_")



def func_2(x, y, *args):
    x += 5
    #food += "m"
    print(x, y, *args)

# вызовы функции с аргументами
func_2(1, 2)
func_2(3, 4, "egg_", [1, 3, 7, ( 5,45, 8)])

help(type)




# Most Python code is either a module to be imported, or a script that is run directly through terminal. 
# Every module in python has a special attribute called __name__ . 
# The value of __name__ attribute is set to '__main__' when module run as main program. 
# Otherwise the value of __name__ is set to contain the name of the module. 
# When the Python interpreter reads a source file, it executes all of the code it finds in the file. 
# Before executing the code, it defines a few special variables. 
# For example, if the Py interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". 
# If this file is being imported from another module, __name__ will be set to the module's name. 
# So when we import module the value of __name__ is set to the module name, else when we run it directly it's value is equal to "__main__" 
# file new_module.py foo = 100 def hello(): print("i am from new_module.py") if __name__ == "__main__": print


# when you import a file or "module" to a program your working on, you are running that code in your program. 
# if i have a program def factorial(number): do_some_math_stuff(number) if __name__=="factorial program": factorial(number) 
# if i save my prog as factorial prog i can import it into another program im making and it will run the code in the if __main__=='__name__' statement. 
# this is because if i import and my code runs in the background of the file 
# if is checking to see if my name=='__what ever the name of your file is'__ in other words its basically checking to see 
# if you program was imported if i ran my code as a script meaning i didn't import it and just ran it. 
# the name would always be __main__ because this is just the default of a name if your running as a script

# Simply speaking, the expression __name__=="__main__" will be met ONLY this .py file is treated as a main program of the project, 
# which accounts from the __name__ attribute of the file is default value "__main__" while modules have its own name for this attribute. 
# Technically, the if statement judged as what the .py file is treated and so you can make things work differently.


https://www.sololearn.com/learning/1073/2488/5199/2

