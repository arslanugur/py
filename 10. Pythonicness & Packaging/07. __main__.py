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

# Question
# Which variable couldn't be accessed if this code was imported as a module?
x = 1
y = x 
if __name__=="__main__":
    z = 3
# z

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do

# SECTION 2
# If we save the code from our previous example as a file called codeexample.py, 
# we can then import it to another script as a module, using the name codeexample.
# codeexample.py
def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")   #
#

# some_script.py
import codeexample

codeexample.function()          # This is a module function

# Basically, we've created a custom module called as codeexample, and then used it in another script.


# __name__ is just a global environmental variable, which equals "__main__" 
# when your code is used as a main program or equals module's name when your code is used as a module imported by another code


# Example:
file = "module.py" 
f = open(file, 'w+') 
text = ''' # A Python Module def up():
            print("This is a module function") 
            if __name__=="module":
            print("This is a script inside module because __name__ is equal of file") 
            if __name__=="__main__": 
            print("This is a script that will not be printed") ''' 
f.write(text) 
f.close() 
import codeexample
codeexample.up()


# __name__ holds the name of python script currently running.. 
# And if __name__ == __main__ 
# if the current file is the main file ( i.e. NOT BEING IMPORTED)


# (1): For the next quiz, seems to important to know what's going on behind the scenes. 
# Remember 1st lesson, end bit of lesson I'm the yellow-shaded box. 
# Recall the following code. 
def function(): 
    print("This is a module function") 
    
if __name__=="__main__": 
    print("This is a script") # See the 2nd code block, what it's saying to you, just an if statement, right? 
    # IF the (special) VARIABLE __name__ is an EXACT MATCH with the string "__main__", 
    # THEN print the string "This is a script". That's all. 
    # Because the Python INTERPRETER is RUNNING the code, I believe it had INTERPRETED the above code as follows.
#

# (2): 
def function(): 
    print("This is a module function") 
    
if "__main__"=="__main__": 
    print("This is a script") 
    # Observe how the special variable __name__ had its VALUE suddenly SET as equal to the string "__main__". 
    # Why??? Because we RAN THIS .py file (/MODULE/SOURCE FILE) itself as the (main) program. 
    # See 1st lesson, end bit, yellow-shaded box. Clearly, the if statement if True, so print("This is a script") gets executed...
#

# (3): Alternatively, IF this .py file gets IMPORTED into another script as a module, then __name__ becomes equal to the module's name instead. 
# For instance, consider the example of this 2nd lesson right here. 
import codeexample codeexample.function() Gets perhaps INTERPRETED as follows. 
def function(): 
    print("This is a module function")
    
if __name__=="__main__": 
    print("This is a script") 
    
codeexample.function()
#

# (4): 
def function(): 
    print("This is a module function") 
if codeexample=="__main__": 
    print("This is a script") 
function() # Hence, you get the OUTPUT of "This is a module function".
#


# "__main__" here represents the name used to save the file being run. 
# if the file is being run directly as a script i.e you write some code and try to run it, 
# the name used to save the file will replace "__main__" and the if condition will check. 
# for example, if the file is saved as file1, and the script is being run directly, 
# the interpreter sees is as __name__="file1" and since we are indeed dealing with the file named file1, the code under the if condition will run. 
# Now let's create a new file say file2. if file1 is imported as a module into file2, __name__="file1", still holds 
# but now we are running from 'file2' which means that the line of code if __name__=="__main__": will not run 
# because now we are in file2 and __name__=!"file1"

# in Java any script code is written in the main function. 
# In python it's just written in the file.__name__=__main__ is used to find out if the code is being imported as a module or just being run

# Example: to print “Welcome” if the script is imported, and “Hi” if it is not imported
if __name__== “__main__”:           # if not imported __main__ will be the entry point (like Main in C#) main
    print(“Hi”)                     # and True print("hi") # and "hi" will print. 
else:                               # if it is imported __main__ shell become a variable taking the name of the Module and the if statement above will be Not true or False
    print(“Welcome")                # and therefore, print("welcome") else will print "Welcome". 
#
# The screwy part for me was that the questions starts with what happens 
# when Its imported (the False and printing "welcome") while the second part else (the False, is actually after the True, that is first). 
# So the re-arrangement had to be done. Just a bit tricky. 
# Point to remember: __main__ becomes the name of the Module IF imported and therefore its Not anymore __main__. 
# Then the "if statement: if __name__== "_main_": becomes False and it goes to the Else. 
# If must be True or __main__ must stay and be __main__ for If to be True. 

# Explanation:
# The if condition checks whether this is the " __main__ program or not. 
# If it's a main program ( not a imported one), print the corresponding statment. Else, ( if it's imported), print "Welcome"



# Example:
          if __name__ == "__main__":
  def inside_function():
    print ("this means that we are in the main file (where the variable '__name__' is set to the name of the file we are currently in, and the same filename == '__main__') \n")
    
else:
  def outside_function():
    print("This message is available as imported only when you are in another file")

try:
  print(1)
  inside_function()
except:
  print("This is not the main file")

try:
  print(2)
  outside_function()
except:
  print("this is only available when we are in another file") 
#


# One need to study this question carefully for a clearer understanding: 
# It says: print "Welcome" if the script is imported or print "Hi" if it's not imported. 
# If the script __name__ has not been saved as a file. 
# it doesn't exist and nothing was imported into __main__. "Hi" will be displayed if it's true 
# line 1. if __name__=="__main__" 
# line 2. print ("Hi") #it is not imported line 
# 3. else line 4 print ("Welcome") #it is imported. 
# Assuming the source file with the script __name__ was saved as name.py and has the following code. 
# For instance: def function (): print (this is a module function) 
# The code will print "Welcome" in this order if the file name.py exist. 
# line 1. if __name__=="__main__" 
# line 2. print ("Welcome") #it is imported 
# line 3. else line 4 print ("Hi") #it is not imported.




