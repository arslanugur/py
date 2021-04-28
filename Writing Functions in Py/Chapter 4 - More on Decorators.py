4. More on Decorators
"""
Now that you understand how decorators work under the hood, 
this chapter gives you a bunch of real-world examples of when and how you would write decorators in your own code. 
You will also learn advanced decorator concepts like how to preserve the metadata of your decorated functions 
and how to write decorators that take arguments.
"""

4.1. Real-world examples
1. Real-world examples
You've learned a lot about how decorators work. 
This lesson will walk you through some real-world decorators so that you can start to recognize common decorator patterns.

2. Time a function
The timer() decorator runs the decorated function and then prints how long it took for the function to run. 
I usually wind up adding some version of this to all of my projects 
because it is a pretty easy way to figure out where your computational bottlenecks are. 
All decorators have fairly similar-looking docstrings because they all take and return a single function. 
For brevity, I will only include the description of the function in the docstrings of the examples that follow.

3. Time a function
Like most decorators, we'll start off by defining a wrapper() function. 
This is the function that the decorator will return. wrapper() takes any number of positional and keyword arguments 
so that it can be used to decorate any function. 
The first thing the new function will do is record the time that it was called with the time() function. 
Then wrapper() gets the result of calling the decorated function. We don't return that value yet though. 
After calling the decorated function, wrapper() checks the time again, and prints a message about how long it took to run the decorated function.
Once we've done that, we need to return the value that the decorated function calculated.

4. Using timer()
So if we decorate this simple sleep_n_seconds() function, you can see that sleeping for 5 seconds takes about 5 seconds, 
and sleeping for 10 seconds takes about 10 seconds. 
This is a trivial use of the decorator to show it working, but it can be very useful for finding the slow parts of your code.

5. Memoizing
Memoizing is the process of storing the results of a function so that the next time the function is called with the same arguments; 
you can just look up the answer. We start by setting up a dictionary that will map arguments to results. 
Then, as usual, we create wrapper() to be the new decorated function that this decorator returns. 
When the new function gets called, we check to see whether we've ever seen these arguments before. 
If we haven't, we send them to the decorated function and store the result in the "cache" dictionary. 
Now we can look up the return value quickly in a dictionary of results. 
The next time we call this function with those same arguments, the return value will already be in the dictionary.

6. Using memoize()
Here we are memoizing slow_function(). slow_function() simply returns the sum of its arguments. 
In order to simulate a slow function, we have it sleep for 5 seconds before returning. 
If we call slow_function() with the arguments 3 and 4, it will sleep for 5 seconds and then return 7. 
But if we call slow_function() with the arguments 3 and 4 again, it will immediately return 7. 
Because we've stored the answer in the cache, the decorated function doesn't even have to call the original slow_function() function.

7. When to use decorators
So when is it appropriate to use a decorator? 
You should consider using a decorator when you want to add some common bit of code to multiple functions. 
We could have added timing code in the body of all three of these functions, but that would violate the principle of Don't Repeat Yourself. 
Adding a decorator is a better choice.


4.2. Print the return type
You are debugging a package that you've been working on with your friends. 
Something weird is happening with the data being returned from one of your functions, 
but you're not even sure which function is causing the trouble. 
You know that sometimes bugs can sneak into your code when you are expecting a function to return one thing, 
and it returns something different. For instance, if you expect a function to return a numpy array, 
but it returns a list, you can get unexpected behavior. 
To ensure this is not what is causing the trouble, you decide to write a decorator, print_return_type(), 
that will print out the type of the variable that gets returned from every call of any function it is decorating.

Instructions
Create a nested function, wrapper(), that will become the new decorated function.
Call the function being decorated.
Return the new decorated function.

Hint
The new decorated function should take any positional and keyword arguments.
Don't forget to pass those positional and keyword arguments to the function being decorated.

Code:
def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

Now you can apply this decorator to every function in the package you are developing and run your scripts. 
Being able to examine the types of your return values will help you understand what is happening and will hopefully help you find the bug.

4.3. Counter
You're working on a new web app, and you are curious about how many times each of the functions in it gets called. 
So you decide to write a decorator that adds a counter to each function that you decorate. 
You could use this information in the future to determine whether there are sections of code that you could remove 
because they are no longer being used by the app.

Instructions
Call the function being decorated and return the result.
Return the new decorated function.
Decorate foo() with the counter() decorator.

Hint
The function being decorated gets passed to counter() as an argument.
After applying the decorator to a function, the resulting decorated function is the one that was defined inside the decorator.
Remember that when using decorator syntax, you don't add the parentheses.

Code:
def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func(*args, **kwargs)
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))


Now you can go decorate a bunch of functions with the counter() decorator, let your program run for a while, 
and then print out how many times each function was called.
It seems a little magical that you can reference the wrapper() function from inside the definition of wrapper() as we do here on line 3. 
That's just one of the many neat things about functions in Python -- any function, not just decorators.


4.4. Decorators and metadata - Video
Got It!
1. Decorators and metadata
One of the problems with decorators is that they obscure the decorated function's metadata. 
In this lesson, I'll show you why it's a problem and how to fix it.

2. Function with a docstring
Here we have a nice function, sleep_n_seconds(), with a docstring that explains exactly what it does. 
If we look at the docstring attribute, we can see the text of the docstring.

3. Other metadata
We can also access other metadata for the function, like its name and default arguments.

4. A decorated function
But watch what happens when we decorate sleep_n_seconds() with the timer() decorator as we've done here. 
When we try to print the docstring, we get nothing back. 
Even stranger, when we try to look up the function's name, Python tells us that sleep_n_seconds()'s name is "wrapper".

5. The timer decorator
To understand why we have to examine the timer() decorator. 
Remember that when we write decorators, we almost always define a nested function to return. 
Because the decorator overwrites the sleep_n_seconds() function, when you ask for sleep_n_seconds()'s docstring or name, 
you are actually referencing the nested function that was returned by the decorator. 
In this case, the nested function was called wrapper() and it didn't have a docstring.

6. functools.wraps()
Fortunately, Python provides us with an easy way to fix this. 
The wraps() function from the functools module is a decorator that you use when defining a decorator. 
If you use it to decorate the wrapper function that your decorator returns, 
it will modify wrapper()'s metadata to look like the function you are decorating. 
Notice that the wraps() decorator takes the function you are decorating as an argument. 
We haven't talked about decorators that take arguments yet, but we will cover that in the next lesson.

7. The metadata we want
If we use this updated version of the timer() decorator to decorate sleep_n_seconds() 
and then try to print sleep_n_seconds()'s docstring, we get the result we expect.

8. The metadata we want
Likewise, printing the name or any other metadata now gives you the metadata from the function 
being decorated rather than the metadata of the wrapper() function.

9. Access to the original function
As an added bonus, using wraps() when creating your decorator also gives you easy access to the original undecorated function via the __wrapped__ attribute. 
Of course, you always had access to this function via the closure, but this is an easy way to get to it if you need it.


4.5. Preserving docstrings when decorating functions
Your friend has come to you with a problem. 
They've written some nifty decorators and added them to the functions in the open-source library they've been working on. 
However, they were running some tests and discovered that all of the docstrings have mysteriously disappeared from their decorated functions. 
Show your friend how to preserve docstrings and other metadata when writing decorators.

Instructions 1/4
Decorate print_sum() with the add_hello() decorator to replicate the issue that your friend saw - that the docstring disappears.

Hint
Remember that decorator syntax starts with an @ symbo

Code:
def add_hello(func):
  def wrapper(*args, **kwargs):
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

# Decorate print_sum() with the add_hello() decorator
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)


Instructions 2/4
To show your friend that they are printing the wrapper() function's docstring, 
not the print_sum() docstring, add the following docstring to wrapper():
"""Print 'hello' and then call the decorated function."""

Hint
Remember that docstrings always go on the first line after the function definition.

Code:
def add_hello(func):
  # Add a docstring to wrapper
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper

@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)


Instructions 3/4
Import a function that will allow you to add the metadata from print_sum() to the decorated version of print_sum().

Hint
The function you need is in the functools module.
You can use dir(functools) to see all of the functions in the functools module.

Code:
# Import the function you need to fix the problem
from functools import wraps

def add_hello(func):
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)


Instructions 4/4
Finally, decorate wrapper() so that the metadata from func() is preserved in the new decorated function.

Hint
wraps() is a decorator that takes an argument.

Code:
from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)

That's a wrap! Your friend was concerned that they couldn't print the docstrings of their functions. 
They now realize that the strange behavior they were seeing was caused by the fact 
that they were accidentally printing the wrapper() docstring instead of the docstring of the original function. 
After adding @wraps(func) to all of their decorators, they see that the docstrings are back where they expect them to be.


4.6. Measuring decorator overhead
Your boss wrote a decorator called check_everything() that they think is amazing, and they are insisting you use it on your function. 
However, you've noticed that when you use it to decorate your functions, it makes them run much slower. 
You need to convince your boss that the decorator is adding too much processing time to your function. 
To do this, you are going to measure how long the decorated function takes to run and compare it to how long the undecorated function would have taken to run. 
This is the decorator in question:

def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    check_outputs(result)
    return result
  return wrapper
  
Instructions
Call the original function instead of the decorated version by using an attribute of the function 
that the wraps() statement in your boss's decorator added to the decorated function.

Hint
Check the video exercise to see how to access the original function via an attribute that wraps() adds.
Alternatively, you could run lines 1-4 of the exercise in the IPython Shell and then call dir(duplicate) to see a list of the attributes of the duplicate() function.

Code:
@check_everything
def duplicate(my_list):
  """Return a new list that repeats the input twice"""
  return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

Your function ran approximately 10,000 times faster without your boss's decorator. 
At least they were smart enough to add @wraps(func) to the nested wrapper() function so that you were able to access the original function. 
You should show them the results of this test. Be sure to ask for a raise while you're at it!

4.7. Decorators that take arguments - Video
1. Decorators that take arguments
Sometimes it would be nice to add arguments to our decorators. To do that, we need another level of function nesting.

2. run_three_times()
Let's consider this silly run_three_times() decorator. If you use it to decorate a function, it will run that function three times. 
If we use it to decorate the print_sum() function and then run print_sum(3,5), it will print 8 three times.

3. run_n_times()
Let's think about what we would need to change if we wanted to write a run_n_times() decorator. 
We want to pass "n" as an argument, instead of hard-coding it in the decorator. 
If we had some way to pass n into the decorator, 
we could decorate print_sum() so that it gets run three times and decorate print_hello() to run five times. 
But a decorator is only supposed to take one argument - the function it is decorating. 
Also, when you use decorator syntax, you're not supposed to use the parentheses. So what gives?

4. A decorator factory
To make run_n_times() work, we have to turn it into a function that returns a decorator, rather than a function that is a decorator. 
So let's start by redefining run_n_times() so that it takes n as an argument, instead of func. 
Then, inside of run_n_times(), we'll define a new decorator function. 
This function takes "func" as an argument because it is the function that will be acting as our decorator. 
We start our new decorator with a nested wrapper() function, as usual. 
Now, since we are still inside the run_n_times() function, we have access to the n parameter that was passed to run_n_times(). 
We can use that to control how many times we repeat the loop that calls our decorated function. 
As usual for any decorator, we return the new wrapper() function. 
And, if run_n_times() returns the decorator() function we just defined, then we can use that return value as a decorator. 
Notice how when we decorate print_sum() with run_n_times(), we use parentheses after @run_n_times. 
This indicates that we are actually calling run_n_times() and decorating print_sum() with the result of that function call. 
Since the return value from run_n_times() is a decorator function, we can use it to decorate print_sum().

5. Expanded code
This is a little bit confusing, so let me show you how this works without using decorator syntax. 
Like before, we have a function, run_n_times() that returns a decorator function when you call it. 
If we call run_n_times() with the argument 3, it will return a decorator. 
In fact, it returns the decorator that we defined at the beginning of this lesson, run_three_times(). 
We could decorate print_sum() with this new decorator using decorator syntax. 
Python makes it convenient to do both of those in a single step though. 
When we use decorator syntax, the thing that comes after the @ symbol must be a reference to a decorator function. 
We can use the name of a specific decorator, or we can call a function that returns a decorator.

6. Using run_n_times()
To prove to you that it works the way we expect here is print_sum() decorated with run_n_times(3). 
When we call print_sum() with the arguments 3 and 5, it prints 8 three times. 
And we can just as easily decorate print_hello(), which prints a hello message, with run_n_times(5). 
When we call print_hello(), we get five hello messages, as expected.


4.8. Run_n_times()
4.9. HTML Generator
4.10. Timeout(): a real world example
4.11. Tag your functions
4.12. Check the return type
4.13. Great job!
