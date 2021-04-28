3. Decorators
"""
Decorators are an extremely powerful concept in Python. 
They allow you to modify the behavior of a function without changing the code of the function itself. 
This chapter will lay the foundational concepts needed to thoroughly understand decorators (functions as objects, scope, and closures), 
and give you a good introduction into how decorators are used and defined. 
This deep dive into Python internals will set you up to be a superstar Pythonista.
"""

3.1. Functions are objects - Video
1. Functions as objects
In this chapter, you are going to learn about decorators, a powerful way of modifying the behavior of functions. 
But first, we need to build up some foundational concepts that will make decorators easier to understand.

2. Functions are just another type of object
The main thing you should take away from this lesson is that functions are just like any other object in Python. 
They are not fundamentally different from lists, dictionaries, DataFrames, strings, integers, floats, modules, or anything else in Python.

3. Functions as variables
And because functions are just another type of object, you can do anything to or with them that you would do with any other kind of object. 
You can take a function and assign it to a variable, like "x". Then, if you wanted to, you could call x() instead of my_function(). 
It doesn't have to be a function you defined, either. 
If you felt so inclined, you could assign the print() function to PrintyMcPrintface, and use it as your print() function.

4. Lists and dictionaries of functions
You can also add functions to a list or dictionary. 
Here, we've added the functions my_function(), open(), and print() to the list "list_of_functions". 
We can call an element of the list, and pass it arguments. 
Since the third element of the list is the print() function, it prints the string argument to the console. 
Below that, we've added the same three functions to a dictionary, under the keys "func1", "func2", and "func3". 
Since the print() function is stored under the key "func3", we can reference it and use it as if we were calling the function directly.

5. Referencing a function
Notice that when you assign a function to a variable, you do not include the parentheses after the function name. 
This is a subtle but very important distinction. When you type my_function() with the parentheses, you are calling that function. 
It evaluates to the value that the function returns. 
However, when you type "my_function" without the parentheses, you are referencing the function itself. It evaluates to a function object.

6. Functions as arguments
Here's where things get really fun. 
Since a function is just an object like anything else in Python, you can pass one as an argument to another function. 
The has_docstring() function checks to see whether the function that is passed to it has a docstring or not. 
We could define these two functions, no() and yes(), and pass them as arguments to the has_docstring() function. 
Since the no() function doesn't have a docstring, the has_docstring() function returns False. 
Likewise, has_docstring() returns True for the yes() function.

7. Defining a function inside another function
Functions can also be defined inside other functions. 
These kinds of functions are called nested functions, although you may also hear them called inner functions, helper functions, or child functions.

8. Defining a function inside another function
A nested function can make your code easier to read. In this example, if x and y are within some bounds, foo() prints x times y. 
We can make that if statement easier to read by defining an in_range() function.

9. Functions as return values
There's also nothing stopping us from returning a function. 
For instance, the function get_function() creates a new function, print_me(), and then returns it. 
If we assign the result of calling get_function() to the variable "new_func", 
we are assigning the return value, "print_me()" to "new_func". We can then call new_func() as if it were the print_me() function.

3.2. Building a command line data app
You are building a command line tool that lets a user interactively explore a data set. 
We've defined four functions: mean(), std(), minimum(), and maximum() that users can call to analyze their data. 
Help finish this section of the code so that your users can call any of these functions by typing the function name at the input prompt.

Note: The function get_user_input() in this exercise is a mock version of asking the user to enter a command. 
It randomly returns one of the four function names. In real life, you would ask for input and wait until the user entered a value.

Instructions
Add the functions std(), minimum(), and maximum() to the function_map dictionary, like we did with mean().
The name of the function the user wants to call is stored in func_name. 
Use the dictionary of functions, function_map, to call the chosen function and pass data as an argument.

Hint
Remember that we want to reference the functions, not call them when adding them to the dictionary.
The functions are stored in the values of the dictionary. You can call those values like they were functions.

Code:
# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)

By adding the functions to a dictionary, you can select the function based on the user's input. 
You could have also used a series of if/else statements, 
but putting them in a dictionary like this is much easier to read and maintain.

3.3. Reviewing your co-worker's code
Your co-worker is asking you to review some code that they've written and give them some tips on how to get it ready for production. 
You know that having a docstring is considered best practice for maintainable, reusable functions, 
so as a sanity check you decide to run this has_docstring() function on all of their functions.

def has_docstring(func):
  """Check to see if the function 
  `func` has a docstring.

  Args:
    func (callable): A function.

  Returns:
    bool
  """
  return func.__doc__ is not None
  
Instructions 1/3
Call has_docstring() on your co-worker's load_and_plot_data() function.

Code:
# Call has_docstring() on the load_and_plot_data() function
ok = has_docstring(load_and_plot_data)

if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")
  
Instructions 2/3
Check if the function as_2D() has a docstring.

Hint
Be sure to call has_docstring() and reference as_2D().

Code:
# Call has_docstring() on the as_2D() function
ok = has_docstring(as_2D)

if not ok:
  print("as_2D() doesn't have a docstring!")
else:
  print("as_2D() looks ok")
  
Instructions 3/3
Check if the function log_product() has a docstring.Check if the function log_product() has a docstring.

Hint
Be sure to call has_docstring() and reference log_product()

Code: to write a docstring for log_product()
# Call has_docstring() on the log_product() function
ok = has_docstring(log_product)

if not ok:
  print("log_product() doesn't have a docstring!")
else:
  print("log_product() looks ok")
  

3.4. Returning functions for a math game
You are building an educational math game where the player enters a math term, 
and your program returns a function that matches that term. 
For instance, if the user types "add", your program returns a function that adds two numbers. 
So far you've only implemented the "add" function. Now you want to include a "subtract" function.

Instructions
Define the subtract() function. It should take two arguments and return the first argument minus the second argument.

Hint
subtract() should be defined as a nested function, just like add() is.

Code:
def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(a, b):
      return a - b
    return subtract
  else:
    print("I don't know that one")
    
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))

Nice nested function! Now that you've implemented the subtract() function, you can keep going to include multiply() and divide(). 
I predict this game is going to be even bigger than Fortnite!
Notice how we assign the return value from create_math_function() to the add and subtract variables in the script. 
Since create_math_function() returns a function, we can then call those variables as functions.


3.5. Scope
1. Scope
Before we can dig into decorators, we must understand how scope works in Python. 
Scope determines which variables can be accessed at different points in your code.

2. Names
Names are very useful things, both in Python and in the real world. For instance, this is Tom.

3. Names
And this is Janelle. When we say "Tom", we know we are talking about the person on the left, and when we say "Janelle", 
we know we are talking about the person on the right.

4. Scope
If Janelle says, "Tom didn't go to work yesterday," we can be fairly sure she is talking about the Tom standing next to her,

5. Scope
And not some Tom in a different country. This is sort of how scope works in programming languages like Python.

6. Scope
Python has names too—variable names. When we say "print(x)" here, Python knows we mean the x that we just defined. 
What happens if we redefine x inside the function foo() though? 
In foo()'s print() statement, do we mean the x that equals 42 or the x that equals 7? 
Python applies the same logic we applied with Tom and Janelle and assumes we mean the x that was defined right there in the function. 
However, there is no y defined in the function foo(), so it looks outside the function for a definition when asked to print y. 
Note that setting x equal to 42 inside the function foo() doesn't change the value of x that we set earlier outside of the function.

7. Scope
Python has to have strict rules about which variable you are referring to when using a particular variable name. 
So when we typed print(x) in the function foo(), the interpreter had to follow those rules to determine which x we meant.

8. Scope
First, the interpreter looks in the local scope. When you are inside a function, 
the local scope is made up of the arguments and any variables defined inside the function.

9. Scope
If the interpreter can't find the variable in the local scope, it expands its search to the global scope. 
These are the things defined outside the function.

10. Scope
Finally, if it can't find the thing it is looking for in the global scope, the interpreter checks the builtin scope. 
These are things that are always available in Python. 
For instance, the print() function is in the builtin scope, which is why we are able to use it in our foo() function.

11. Scope
I actually skipped a level in that diagram. 
In the case of nested functions, where one function is defined inside another function, 
Python will check the scope of the parent function before checking the global scope. 
This is called the nonlocal scope to show that it is not the local scope of the child function and not the global scope.

12. The global keyword
Note that Python only gives you read access to variables defined outside of your current scope. 
In foo() when we set x equal to 42, Python assumed we wanted a new variable in the local scope, not the x in the global scope. 
If what we had really wanted was to change the value of x in the global scope, 
then we have to declare that we mean the global x by using the global keyword. 
Notice that when we print x after calling foo() now, it prints 42 instead of 7 like it used to. 
However, you should try to avoid using global variables like this if possible, because it can make testing and debugging harder.

13. The nonlocal keyword
And if we ever want to modify a variable that is defined in the nonlocal scope, we have to use the "nonlocal" keyword. 
It works exactly the same as the "global" keyword, but it is used when you are inside a nested function, 
and you want to update a variable that is defined inside your parent function.


3.6. Understanding scope
What four values does this script print?
Code:
x = 50

def one():        # one() is only modifying a local copy of x, not the global x.
  x = 10

def two():
  global x
  x = 30

def three():
  x = 100
  print(x)

for func in [one, two, three]:
  func()
  print(x)
  
output: 50, 30, 100, 30

one() doesn't change the global x, so the first print() statement prints 50.
two() does change the global x so the second print() statement prints 30.
The print() statement inside the function three() is referencing the x value that is local to three(), so it prints 100.
But three() does not change the global x value so the last print() statement prints 30 again.


3.7. Modifying variables outside local scope
Sometimes your functions will need to modify a variable that is outside of the local scope of that function. 
While it's generally not best practice to do so, it's still good to know-how in case you need to do it. 
Update these functions so they can modify variables that would usually be outside of their scope.

Instructions 1/3
Add a keyword that lets us update call_count from inside the function.

Hint
call_count is defined in the global scope.

Code:
call_count = 0

def my_function():
  # Use a keyword that lets us update call_count 
  global call_count
  call_count += 1
  
  print("You've called my_function() {} times!".format(
    call_count
  ))
  
for _ in range(20):
  my_function()
  

Instructions 2/3
Add a keyword that lets us modify file_contents from inside save_contents()

Hint
From the perspective of the code in save_contents(), variables defined in read_files() are in the nonlocal scope.

Code:
def read_files():
  file_contents = None
  
  def save_contents(filename):
    # Add a keyword that lets us modify file_contents
    nonlocal file_contents
    if file_contents is None:
      file_contents = []
    with open(filename) as fin:
      file_contents.append(fin.read())
      
  for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
    save_contents(filename)
    
  return file_contents

print('\n'.join(read_files()))


Instructions 3/3
Add a keyword to done in check_is_done() so that wait_until_done() eventually stops looping.

Hint
The final print statement should print: "Work done? True"

Code:
def wait_until_done():
  def check_is_done():
    # Add a keyword so that wait_until_done() 
    # doesn't run forever
    global done
    if random.random() < 0.1:
      done = True
      
  while not done:
    check_is_done()

done = False
wait_until_done()

print('Work done? {}'.format(done))

By adding global done in check_is_done(), 
you ensure that the done being referenced is the one that was set to False before wait_until_done() was called. 
Without this keyword, wait_until_done() would loop forever 
because the done = True in check_is_done() would only be changing a variable that is local to check_is_done(). 
Understanding what scope your variables are in will help you debug tricky situations like this one.

3.8. Closures - Video
1. Closures
The last topic I need to explain before discussing decorators is how closures work in Python.

2. Attaching nonlocal variables to nested functions
A closure in Python is a tuple of variables that are no longer in scope, but that a function needs in order to run. 
Let's explain this with an example. 
The function foo() defines a nested function bar() that prints the value of "a". foo() returns this new function, 
so when we say "func = foo()" we are assigning the bar() function to the variable "func". 
Now what happens when we call func()? As expected, it prints the value of variable "a", which is 5. But wait a minute, 
how does function "func()" know anything about variable "a"? "a" is defined in foo()'s scope, not bar()'s. 
You would think that "a" would not be observable outside of the scope of foo(). That's where closures come in. 
When foo() returned the new bar() function, 
Python helpfully attached any nonlocal variable that bar() was going to need to the function object. 
Those variables get stored in a tuple in the "__closure__" attribute of the function. 
The closure for "func" has one variable, and you can view the value of that variable by accessing the "cell_contents" of the item.

3. Closures and deletion
Let's examine this bit of code. Here, x is defined in the global scope. 
foo() creates a function bar() that prints whatever argument was passed to foo(). 
When we call foo() and assign the result to "my_func", we pass in "x". 
So, as expected, calling my_func() prints the value of x. Now let's delete x and call my_func() again. 
What do you think will happen this time? If you guessed that we would still print 25, then you are correct. 
That's because foo()'s "value" argument gets added to the closure attached to the new "my_func" function. 
So even though x doesn't exist anymore, the value persists in its closure.

4. Closures and overwriting
Notice that nothing changes if we overwrite "x" instead of deleting it. 
Here we've passed x into foo() and then assigned the new function to the variable x. 
The old value of "x", 25, is still stored in the new function's closure, even though the new function is now stored in the "x" variable. 
This is going to be important to remember when we talk about decorators in the next lesson.

5. Definitions - nested function
Let's go over some of the key concepts again to be sure you understand. 
A nested function is a function defined inside another function. 
We'll sometimes refer to the outer function as the parent and the nested function as the child.

6. Definitions - nonlocal variables
A nonlocal variable is any variable that gets defined in the parent function's scope, and that gets used by the child function.

7. Definitions - closure
A closure is Python's way of attaching nonlocal variables to a returned function so that the function can operate even when it is called outside of its parent's scope.

8. Why does all of this matter?
We've gone pretty deep into the internals of how Python works, and you must be wondering, "Why does all of this matter?" 
Well, in the next lesson we'll finally get to talk about decorators. 
In order to work, decorators have to make use of all of these concepts: functions as objects, nested functions, nonlocal scope, and closures. 
Now that you have a firm foundation to build on, understanding how decorators work should be easy.


3.9. Checking for closure
You're teaching your niece how to program in Python, and she is working on returning nested functions. 
She thinks she has written the code correctly, but she is worried that the returned function won't have the necessary information when called. 
Show her that all of the nonlocal variables she needs are in the new function's closure.

Instructions 1/3
Use an attribute of the my_func() function to show that it has a closure that is not None.

Hint
Remember that the attribute you need starts and ends with double underscores (__).

Code:
def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__ is not None)

Instructions 2/3
Show that there are two variables in the closure.

Hint
In Python, a closure is a tuple of objects.
The length of this closure should be 2.

Code:
def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)

# Show that there are two variables in the closure
print(len(my_func.__closure__) == 2)

Instructions 3/3
Get the values of the variables in the closure so you can show that they are equal to [2, 17], the arguments passed to return_a_func().

Hint
Each item in the closure is called a "cell".
Each cell has "contents" that stores the value of one variable.

Code:
def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])

the values she passed to return_a_func() are still accessible to the new function she returned, 
even after the program has left the scope of return_a_func().
Values get added to a function's closure in the order they are defined in the enclosing function (in this case, arg1 and then arg2), 
but only if they are used in the nested function. 
That is, if return_a_func() took a third argument (e.g., arg3) that wasn't used by new_func(), then it would not be captured in new_func()'s closure

3.10. Closures keep your values safe
You are still helping your niece understand closures. 
You have written the function get_new_func() that returns a nested function. 
The nested function call_func() calls whatever function was passed to get_new_func(). 
You've also written my_special_function() which simply prints a message that states that you are executing my_special_function().

You want to show your niece that no matter what you do to my_special_function() after passing it to get_new_func(), 
the new function still mimics the behavior of the original my_special_function() because it is in the new function's closure.

Instructions 1/3
Show that you still get the original message even if you redefine my_special_function() to only print "hello".

Hint
Update the definition of my_special_function() to print the new message.

Code:
def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Redefine my_special_function() to just print "hello"
def my_special_function():
  print("hello")

new_func()

Instructions 2/3
Show that even if you delete my_special_function(), you can still call new_func() without any problems.

Hint
Delete a variable in Python with the del() function.Hint
Delete a variable in Python with the del() function.

Code:
def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(my_special_function)

# Delete my_special_function()
del(my_special_function)

new_func()

Instructions 2/3
Show that you still get the original message even if you overwrite my_special_function() with the new function.

Hint
Assign the result of return_a_func() to the variable my_special_function.

Code:
def my_special_function():
  print('You are running my_special_function()')
  
def get_new_func(func):
  def call_func():
    func()
  return call_func

# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()

you can modify, delete, or overwrite the values needed by the nested function, 
but the nested function can still access those values because they are stored safely in the function's closure. 
You could run into memory issues if you wound up adding a very large array or object to the closure, and has resolved to keep her eye out for that sort of problem.

3.11. Decorators
1. Decorators
Now that you know functions can be passed around as variables, and you understand scope and closures, we can talk about decorators.

2. Functions
So what is a decorator? Let's say you have a function that takes some inputs and returns some outputs.

3. Decorators
A decorator is a wrapper that you can place around a function that changes that function's behavior.

4. Modify inputs
You can modify the inputs,

5. Modify outputs
modify the outputs,

6. Modify function
or even change the behavior of the function itself.

7. What does a decorator look like?
You may have seen decorators in Python before. 
When you use them, you type the "@" symbol followed by the decorator's name on the line directly above the function you are decorating. 
Here, the "double_args" decorator modifies the behavior of the multiply() function. 
double_args is a decorator that multiplies every argument by two before passing them to the decorated function. 
So 1 times 5 becomes 2 times 10, which equals 20. 
That seems kind of magical that we can alter the behavior of functions, so let's peel back the layers and see how it works. 
We will build the double_args decorator together in this lesson.

8. The double_args decorator
Let's continue to use the multiply() function as the function we are decorating. 
Now, decorators are just functions that take a function as an argument and return a modified version of that function. 
To start off, let's not have double_args modify anything. It just takes a function and immediately returns it. 
If we call this version of double_args() that does nothing and pass it the multiply function 
and then assign the result to the variable "new_multiply", then we can call new_multiply(1, 5) 
and get the same value we would have gotten from multiply(1, 5).

9. The double_args decorator
In order for your decorator to return a modified function, it is usually helpful for it to define a new function to return. 
We'll call that nested function "wrapper()". 
All wrapper() does is take two arguments and passes them on to whatever function was passed to double_args() in the first place. 
If double_args() then returns the new wrapper() function, the return value acts exactly the same as whatever function was passed to double_args(), 
assuming that the function passed to double_args() also takes exactly two arguments. 
So, double_args() is still not doing anything to actually modify the function it is decorating. 
Once again, we'll pass multiply() to double_args() and assign the result to new_multiply(). 
If we then call new_multiply(), which is now equal to the wrapper() function, wrapper() calls multiply() 
because it is the function that was passed to double_args(). 
So wrapper() calls multiply() with the arguments 1 and 5, which returns 5.

10. The double_args decorator
Now let's actually modify the function our decorator is decorating. 
This time, wrapper() will still call whatever function is passed to double_args(), 
but it will double every argument when it calls the original function. 
See how it calls func() with a times 2 and b times 2? 
As usual, we will call double_args() on the multiply() function and assign the result to new_multiply(). 
Now, what happens when we call new_multiply() with 1 and 5 as arguments? 
Well, new_multiply() is equal to wrapper(), which calls multiply() after doubling each argument. 
So 1 becomes 2 and 5 becomes 10, giving us 2 times 10, which equals 20.

11. The double_args decorator
We're almost there. This time, instead of assigning the new function to "new_multiply", we're going to overwrite the "multiply" variable. 
Now calling multiply() with arguments 1 and 5 gives us 20 instead of 5. 
Remember that we can do this because Python stores the original multiply function in the new function's closure.

12. Decorator syntax
When I first showed you the double_args() decorator at the beginning of this lecture, 
I used "@double_args" on the line before the definition of multiply(). 
This is just a Python convenience for saying "multiply" equals the value returned by calling double_args() with "multiply" as the only argument. 
The code shown here on the left is exactly equivalent to the code on the right.


3.12. Using decorator syntax
You have written a decorator called print_args that prints out all of the arguments 
and their values any time a function that it is decorating gets called.

Instructions 1/2
Decorate my_function() with the print_args() decorator by redefining my_function().

Hint
A decorator is a function that takes another function as its only argument and returns a modified version of that function.

Code:
def my_function(a, b, c):
  print(a + b + c)

# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function)

my_function(1, 2, 3)

Instructions 2/2
Decorate my_function() with the print_args() decorator using decorator syntax.

Hint
Add an @ symbol before the decorator name when you apply it to a function.
Don't use parentheses when using decorator syntax.

Code:
# Decorate my_function() with the print_args() decorator
@print_args
def my_function(a, b, c):
  print(a + b + c)

my_function(1, 2, 3)

Note that @print_args before the definition of my_function is exactly equivalent to my_function = print_args(my_function). 
Remember, even though decorators are functions themselves, 
when you use decorator syntax with the @ symbol you do not include the parentheses after the decorator name.


3.13. Defining a decorator
Your buddy has been working on a decorator that prints a "before" message 
before the decorated function is called and prints an "after" message after the decorated function is called. 
They are having trouble remembering how wrapping the decorated function is supposed to work. 
Help them out by finishing their print_before_and_after() decorator.

Instructions
Call the function being decorated and pass it the positional arguments *args.
Return the new decorated function.

Hint
The function being decorated is passed into print_before_and_after() as the argument func.
The new decorated function is defined inside of print_before_and_after().

Code:
def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)

The decorator print_before_and_after() defines a nested function wrapper() that calls whatever function gets passed to print_before_and_after(). 
wrapper() adds a little something else to the function call by printing one message before the decorated function is called and another right afterwards. 
Since print_before_and_after() returns the new wrapper() function, we can use it as a decorator to decorate the multiply() function.

4. More on Decorators
"""
Now that you understand how decorators work under the hood, 
this chapter gives you a bunch of real-world examples of when and how you would write decorators in your own code. 
You will also learn advanced decorator concepts like how to preserve the metadata of your decorated functions 
and how to write decorators that take arguments.
"""

4.1. Real-world examples
4.2. Print the return type
4.3. Counter
4.4. Decorators and metadata
4.5. Preserving docstrings when decorating functions
4.6. Measuring decorator overhead
4.7. Decorators that take arguments
4.8. Run_n_times()
4.9. HTML Generator
4.10. Timeout(): a real world example
4.11. Tag your functions
4.12. Check the return type
4.13. Great job!
