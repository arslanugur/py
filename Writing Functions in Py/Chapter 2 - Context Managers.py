2. Context Managers
"""
If you've ever seen the "with" keyword in Python and wondered what its deal was, then this is the chapter for you! 
Context managers are a convenient way to provide connections in Python and guarantee 
that those connections get cleaned up when you are done using them. 
This chapter will show you how to use context managers, as well as how to write your own.
"""


2.1. Using context managers
1. Using context managers
In this lesson, I'll introduce the concept of context managers and show you how to use these special kinds of functions.

2. What is a context manager?
A context manager is a type of function that sets up a context for your code to run in, runs your code, and then removes the context. 
That's not a very helpful definition though, so let me explain with an analogy.

3. A catered party
Imagine that you are throwing a fancy party, and have hired some caterers to provide refreshments for your guests.

4. A catered party
Before the party starts, the caterers set up tables with food and drinks.

5. A catered party
Then you and your friends dance, eat, and have a good time.

6. A catered party
When the party is done,

7. A catered party
the caterers clean up the food and remove the tables.

8. Catered party as context
In this analogy, the caterers are like a context manager. 
First, they set up a context for your party, which was a room full of food and drinks. 
Then they let you and your friends do whatever you want. 
This is like you being able to run your code inside the context manager's context. 
Finally, when the party is over, the caterers clean up and remove the context that the party happened in.

9. A real-world example
You may have used code like this before. The "open()" function is a context manager. 
When you write "with open()", it opens a file that you can read from or write to. 
Then, it gives control back to your code so that you can perform operations on the file object. 
In this example, we read the text of the file, store the contents of the file in the variable "text", 
and store the length of the contents in the variable "length". 
When the code inside the indented block is done, the "open()" function makes sure that the file is closed before continuing on in the script. 
The print statement is outside of the context, so by the time it runs the file is closed.

10. Using a context manager
Any time you use a context manager, it will look like this. The keyword "with" lets Python know that you are trying to enter a context.

11. Using a context manager
Then you call a function. You can call any function that is built to work as a context manager. 
In the next lesson, I'll show you how to write your own functions that work this way.

12. Using a context manager
A context manager can take arguments like any normal function.

13. Using a context manager
You end the "with" statement with a colon as if you were writing a for loop or an if statement.

14. Using a context manager
Statements in Python that have an indented block after them, 
like for loops, if/else statements, function definitions, etc. are called "compound statements". 
The "with" statement is another type of compound statement. 
Any code that you want to run inside the context that the context manager created needs to be indented.

15. Using a context manager
When the indented block is done, the context manager gets a chance to clean up anything that it needs to, 
like when the "open()" context manager closed the file.

16. Using a context manager
Some context managers want to return a value that you can use inside the context. 
By adding "as" and a variable name at the end of the "with" statement, you can assign the returned value to the variable name. 
We used this ability when calling the "open()" context manager, which returns a file that we can read from or write to. 
By adding "as my_file" to the "with" statement, we assigned the file to the variable "my_file".
                        
2.2. The number of cats
You are working on a natural language processing project to determine what makes great writers so great. 
Your current hypothesis is that great writers talk about cats a lot. 
To prove it, you want to count the number of times the word "cat" appears in "Alice's Adventures in Wonderland" by Lewis Carroll. 
You have already downloaded a text file, alice.txt, with the entire contents of this great book.

Instructions
Use the open() context manager to open alice.txt and assign the file to the file variable.
Hint
Remember the keywords with and as when calling a context manager like open().
                        
Code:
# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

                        
2.3. The speed of cats
You're working on a new web service that processes Instagram feeds to identify which pictures contain cats (don't ask why -- it's the internet). 
The code that processes the data is slower than you would like it to be, so you are working on tuning it up to run faster. 
Given an image, image, you have two functions that can process it:

- process_with_numpy(image)
- process_with_pytorch(image)
Your colleague wrote a context manager, timer(), that will print out how long the code inside the context block takes to run. 
She is suggesting you use it to see which of the two options is faster. Time each function to determine which one to use in your web service.

Instructions
Use the timer() context manager to time how long process_with_numpy(image) takes to run.
Use the timer() context manager to time how long process_with_pytorch(image) takes to run.

Hint
The timer() context manager does not take any arguments.
The timer() context manager doesn't yield a value, so you don't need an as <variable name> in your with statement.

Code: 
image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
  print('Pytorch version')
  process_with_pytorch(image)
  
Now that you know the pytorch version is faster, 
you can use it in your web service to ensure your users get the rapid response time they expect.
You may have noticed there was no as <variable name> at the end of the with statement in timer() context manager. 
That is because timer() is a context manager that does not return a value, 
so the as <variable name> at the end of the with statement isn't necessary. 
In the next lesson, you'll learn how to write your own context managers like timer()

2.4. Writing context managers - Video
1. Writing context managers
Now that you know how to use context managers, I want to show you how to write a context manager for other people to use.

2. Two ways to define a context manager
There are two ways to define a context manager in Python: 
by using a class that has special __enter__() and __exit__() methods or by decorating a certain kind of function.

3. Two ways to define a context manager
This course is focused on writing functions, and some of you may not have been introduced to the concept of classes yet, 
so I will only present the function-based method here.

4. How to create a context manager
There are five parts to creating a context manager. First, you need to define a function. 
Next, you can add any setup code your context needs. This is not required though. 
Third, you must use the "yield" keyword to signal to Python that this is a special kind of function. 
I will explain what this keyword means in a moment. After the "yield" statement, 
you can add any teardown code that you need to clean up the context.

5. How to create a context manager
Finally, you must decorate the function with the "contextmanager" decorator from the "contextlib" module. 
You might not know what a decorator is, and that's ok. We will discuss decorators in-depth in the next chapter of this course. 
For now, the important thing to know is that you write the "at" symbol, 
followed by "contextlib.contextmanager" on the line immediately above your context manager function.

6. The "yield" keyword
The "yield" keyword may also be new to you. When you write this word, it means that you are going to return a value, 
but you expect to finish the rest of the function at some point in the future. 
The value that your context manager yields can be assigned to a variable in the "with" statement by adding "as <variable name>". 
Here, we've assigned the value 42 that my_context() yields to the variable "foo". By running this code, 
you can see that after the context block is done executing, the rest of the my_context() function gets run, printing "goodbye". 
Some of you may recognize the "yield" keyword as a thing that gets used when creating generators. 
In fact, a context manager function is technically a generator that yields a single value.

7. Setup and teardown
The ability for a function to yield control and know that it will get to finish running later is what makes context managers so useful. 
This context manager is an example of code that accesses a database. 
Like most context managers, it has some setup code that runs before the function yields. 
This context manager uses that setup code to connect to the database.

8. Setup and teardown
Most context managers also have some teardown or cleanup code when they get control back after yielding. 
This one uses the teardown section to disconnect from the database.

9. Setup and teardown
This setup/teardown behavior allows a context manager to hide things like connecting and disconnecting from a database 
so that a programmer using the context manager can just perform operations on the database without worrying about the underlying details.

10. Yielding a value or None
The database() context manager that we've been looking at yields a specific value - the database connection - 
that can be used in the context block. Some context managers don't yield an explicit value. 
in_dir() is a context manager that changes the current working directory to a specific path 
and then changes it back after the context block is done. 
It does not need to return anything with its "yield" statement.

2.5. The timer() context manager
A colleague of yours is working on a web service that processes Instagram photos. 
Customers are complaining that the service takes too long to identify whether or not an image has a cat in it, 
so your colleague has come to you for help. 
You decide to write a context manager that they can use to time how long their functions take to run.

Instructions
Add a decorator from the contextlib module to the timer() function that will make it act like a context manager.
Send control from the timer() function to the context block.

Hint
Remember that context managers use yield to return control to the context.
timer() does not return a specific value when it yields control.

Code:
# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)

your colleague can now use your timer() context manager to figure out which of their functions is running too slow. 
Notice that the three elements of a context manager are all here: 
a function definition, a yield statement, and the @contextlib.contextmanager decorator. 
It's also worth noticing that timer() is a context manager that does not return an explicit value, 
so yield is written by itself without specifying anything to return.

2.6. A read-only open() context manager
You have a bunch of data files for your next deep learning project that took you months to collect and clean. 
It would be terrible if you accidentally overwrote one of those files when trying to read it in for training, 
so you decide to create a read-only version of the open() context manager to use in your project.

The regular open() context manager:
-takes a filename and a mode ('r' for read, 'w' for write, or 'a' for append)
-opens the file for reading, writing, or appending
-yields control back to the context, along with a reference to the file
-waits for the context to finish
-and then closes the file before exiting

Your context manager will do the same thing, except it will only take the filename as an argument and it will only open the file for reading.

Instructions
Yield control from open_read_only() to the context block, ensuring that the read_only_file object gets assigned to my_file.
Use read_only_file's .close() method to ensure that you don't leave open files lying around.

Hint
The open() function creates a reference to a file.
The function open_read_only() should send that file back to the context.
You close a file with the .close() method of a file object.

Code:
@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())
  
Every time you use with open_read_only() your files are safe from being accidentally overwritten. 
This function is an example of a context manager that does return a value, so we write yield read_only_file instead of just yield. 
Then the read_only_file object gets assigned to my_file in the with statement 
so that whoever is using your context can call its .read() method in the context block.

2.7. Advanced topics - Video
1. Advanced topics
You've learned a lot about how to using and writing context managers. 
In this lesson, we'll cover nested contexts, handling errors, and how to know when to create a context manager.

2. Nested contexts
Imagine you are implementing this copy() function that copies the contents of one file to another file. 
One way you could write this function would be to open the source file, store the contents of the file in the "contents" variable, 
then open the destination file and write the contents to it. 
This approach works fine until you try to copy a file that is too large to fit in memory.

3. Nested contexts
What would be ideal is if we could open both files at once and copy over one line at a time. 
Fortunately for us, the file object that the "open()" context manager returns can be iterated over in a for loop. 
The statement "for line in my_file" here will read in the contents of my_file one line at a time until the end of the file.

4. Nested contexts
So, going back to our copy() function, if we could open both files at once, 
we could read in the source file line-by-line and write each line out to the destination as we go. 
This would let us copy the file without worrying about how big it is. In Python, nested "with" statements are perfectly legal. 
This code opens the source file and then opens the destination file inside the source file's context. 
That means code that runs inside the context created by opening the destination file has access to both the "f_src" and the "f_dst" file objects. 
So we are able to copy the file over one line at a time like we wanted to!

5. Handling errors
One thing you will want to think about when writing your context managers is: 
What happens if the programmer who uses your context manager writes code that causes an error? 
Imagine you've written this function that lets someone connect to the printer. 
The printer only allows one connection at a time, 
so it is imperative that "p.disconnect()" gets called, or else no one else will be able to print! 
Someone decides to use your get_printer() function to print the text of their document. 
However, they weren't paying attention and accidentally typed "txt" instead of "text". 
This will raise a KeyError because "txt" is not in the "doc" dictionary. And that means "p.disconnect()" doesn't get called.

6. Handling errors
So what can we do? You may be familiar with the "try" statement. 
It allows you to write code that might raise an error inside the "try" block and catch that error inside the "except" block. 
You can choose to ignore the error or re-raise it. The "try" statement also allows you to add a "finally" block. 
This is code that runs no matter what, whether an exception occurred or not.

7. Handling errors
The solution then is to put a "try" statement before the "yield" statement in our get_printer() function 
and a "finally" statement before "p.disconnect()". 
When the sloppy programmer runs their code, they still get the KeyError, 
but "finally" ensures that "p.disconnect()" is called before the error is raised.

8. Context manager patterns
If you notice that your code is following any of these patterns, you might consider using a context manager. For instance, in this lesson we've talked about "open()", which uses the open/close pattern, and "get_printer()", which uses the connect/disconnect pattern. See if you can find other instances of these patterns in code you are familiar with.

1 Adapted from Dave Brondsema's talk at PyCon 2012: https://youtu.be/cSbD5SKwak0?t=795

2.8. Context manager use cases
Which of the following would NOT be a good opportunity to use a context manager?
---  A function that starts a timer that keeps track of how long some block of code takes to run.
---> A function that prints all of the prime numbers between 2 and some value n.
---  A function that connects to a smart thermostat so that it can be programmed remotely.
---  A function that prevents multiple users from updating an online spreadsheet at the same time 
        by locking access to the spreadsheet before every operation.

Starting and stopping a timer is an example of the START/STOP pattern.
Connecting to a thermostat and disconnecting afterward is an example of the CONNECT/DISCONNECT pattern.
Locking access to an online spreadsheet and then releasing the lock is an example of the LOCK/RELEASE pattern.

2.9. Scraping the NASDAQ
Training deep neural nets is expensive! You might as well invest in NVIDIA stock since you're spending so much on GPUs. 
To pick the best time to invest, you are going to collect and analyze some data on how their stock is doing. 
The context manager stock('NVDA') will connect to the NASDAQ and return an object 
that you can use to get the latest price by calling its .price() method.

You want to connect to stock('NVDA') and record 10 timesteps of price data by writing it to the file NVDA.txt.

Instructions
Use the stock('NVDA') context manager and assign the result to nvda.
Open a file for writing with open('NVDA.txt', 'w') and assign the file object to f_out so you can record the price over time.

Hint
To assign the result of a context manager to a variable, use as <variable name>.
The 'w' argument in the open() function opens the file in write-only mode.

Code:
# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open 'NVDA.txt' for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))
      
Super stock scraping! Now you can monitor the NVIDIA stock price and decide when is the exact right time to buy. 
Nesting context managers like this allows you 
to connect to the stock market (the CONNECT/DISCONNECT pattern) and write to a file (the OPEN/CLOSE pattern) at the same time.


2.10. Changing the working directory
You are using an open-source library that lets you train deep neural networks on your data. 
Unfortunately, during training, this library writes out checkpoint models (i.e., 
models that have been trained on a portion of the data) to the current working directory. 
You find that behavior frustrating because you don't want to have to launch the script from the directory where the models will be saved.

You decide that one way to fix this is to write a context manager that changes the current working directory, lets you build your models, 
and then resets the working directory to its original location. 
You'll want to be sure that any errors that occur during model training don't prevent you from resetting the working directory to its original location.

Instructions
Add a statement that lets you handle any errors that might occur inside the context.
Add a statement that ensures os.chdir(current_dir) will be called, whether there was an error or not.

Hint
try blocks can be followed by except, else, and finally blocks.

Code:
def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)
    
Now, even if someone writes buggy code when using your context manager, 
you will be sure to change the current working directory back to what it was when they called in_dir(). 
This is important to do because your users might be relying on their working directory being what it was when they started the script. 
in_dir() is a great example of the CHANGE/RESET pattern that indicates you should use a context manager.
