# SECTION 1
# Generators are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
# They can be created using functions and the yield statement.
# Example:
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
#
for i in countdown():
    print(i)          # 5,4,3,2,1
#

# The yield statement is used to define a generator, 
# replacing the return of a function to provide a result to its caller without destroying local variables.

# Examples: 
def countdown(i):
    i = 9
    while i > 0: 
        yield i 
        i -= 1 
 
    for i in countdown(i):
        print(list(countdown(9))) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
#

def countdown(i):
    i = 9
    while i > 0: 
        yield i 
        i -= 1 
        
for i in countdown(9): 
    print(list(countdown(9))) # [9, 8, 7, 6, 5, 4, 3, 2, 1] * 9
#

def countdown(i): 
    i = 9
    while i > 0: 
        yield i 
        i -= 1 
        
for i in countdown(9):
    print(list(countdown(i)))   # [9, 8, 7, 6, 5, 4, 3, 2, 1]
                                # [8, 7, 6, 5, 4, 3, 2, 1] 
                                # [7, 6, 5, 4, 3, 2, 1] 
                                # [6, 5, 4, 3, 2, 1] 
                                # [5, 4, 3, 2, 1] 
                                # [4, 3, 2, 1] 
                                # [3, 2, 1] 
                                # [2, 1] 
                                # [1]
#



# less confusing version:
def countdown(i): 
    while i > 0: 
        yield i 
        i -= 1 
        for x in countdown(9): 
            print(list(countdown(x)))
#

# Here is the difference between generators and normal functions or lists (the simple way): 
# Let's say that you're attending a 2 hour long lecture. 
# If you write notes: you can have infinite memory if you transfer everything to paper. 
# So no matter how much was told in the lecture, 
# you can just write it all down then it's all yielded (written down then and there) so low memory usage. Like with generators. 
# But if you had to remember everything from the lecture 
# then you have to consume a lot of memory storage space for a long time and keep it all in your head. Like with functions and lists.


# Think of it like your phone's media player. You can do three things to a single track of audio: Play, pause, and stop. 
# Play = Calling a function Pause = yield Stop = return. 
# Playing a song after pausing picks up at the time you paused, whereas stopping makes it return all the way to the beginning. Same idea here. 
# Yielding pauses the function as it is, with your next call returning to the line right after yeild. 
# Return makes the next call restart at the beginning of the function. 
# I feel like all the pointless terminology makes this much more complicated than it actually is.


# Example:
def count(): 
    i = 5 
    while i>0: 
        yield i 
        i-=1 
    x=count() 
    
    for i in x: 
        print(i) 
        if i==3: 
            break       # 5 4 3     
    for i in x: 
        print(i)        # 2 1


# Example:
def countdown(): 
    i=5 
    while i > 0: 
        yield i 
        i -= 1 

print(list(countdown())) 

for i in countdown(): 
print(i) 
# yield is useful in returning the values to another function that calls it without destroying the variables. 
# Using return here will produce an error, namely "int object is not iterable" but this can be achieved with yield 
# As we know that statements after return do not get executed, the loops stop at the return statement. 
# And then the variables get destroyed after return or at the end of loop. 
# But in yield that doesnt happen, the code written after yield gets executed and loop ends only because of the condition written. 
# So yield makes a list of these variables' values and returns the same at the end of the loop. 
# And these values can be used by other functions. And can be worked on, as a list is an iterable.


# Yield enables i value to use outside a loop (for example to print it before it changes again) like in this example. 
# We use just one print but with yield it prints out 3 lines in every loop. 
def countdown(): 
    i = 5 
    while i > 0: 
        yield("cycle {}: ".format(i)) yield("yield A: {}".format(i))
        i -= 1 
        yield("yield B: {}".format(i)) for i in countdown(): print("Result: {}".format(i)) 
# Output: -------------- 
# Result: cycle 5: 
# Result: yield A: 5 
# Result: yield B: 4 
# Result: cycle 4: 
# Result: yield A: 4 
# Result: yield B: 3 
# Result: cycle 3: 
# Result: yield A: 3 
# Result: yield B: 2 
# Result: cycle 2: 
# Result: yield A: 2 
# Result: yield B: 1 
# Result: cycle 1: 
# Result: yield A: 1 
# Result: yield B: 0


# Generators are used to create iterators, but with a different approach. 
# Generators are simple functions which return an iterable set of items, one at a time, in a special way. 
# When an iteration over a set of item starts using the for statement, the generator is run. 
# Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. 
# The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.

# Example:
def countdown(): 
    i=5 
    while i > 0: 
        yield i 
        i -= 1 
        print(i/2) 

for i in countdown(): 
    print(i)            # 5, 2.0, 4, 1.5, 3, 1.0, 2, 0.5, 1, 0.0

# The term, yield, is used in an agricultural sense like a fruit tree that yields ripe fruit for you to pluck. 
# You get your fruit then leave, and meanwhile it grows more fruits to be plucked next time you come back. 
# A return statement is more like chopping down the tree and harvesting whatever fruit it has at the time. 
# For the next batch of fruit you need to start over and plant a new tree.

# Example:
def countdown(): 
    i=5 
    while i > 0: 
        print(i) 
    i -= 1

for i in countdown():
    print(i) 
countdown()     # this one produces same result but why using yield I really don't get it can someone explain me better about generator using this code


# Check these mixed generators with map, filter and lambdas examples: 
def countdown(): 
    i=5 
    while i > 0: 
        yield i 
        i -= 1 

l2 = list(countdown()) 
print(l2) # [5,4,3,2,1] 
l3 = [i for i in countdown()] 
print(l3) # [5,4,3,2,1] # squared values of a generator 
l4 = list(map(lambda x: x**2, countdown())) 
print(l4) # [25, 16, 9, 4, 1] # squared and greater than 10 
l5 = list(filter(lambda b: b > 10, map(lambda c: c**2, countdown()))) 
print(l5) # [25, 16]


# yield statement is used in functions to turn them into generators?


# while return is used to return a value from function, yield "trasforms" a simple function in a special function which called generator. 
# This function has the property to be called on each element of its argument. 
# A simple function takes an argument and all job is made on all of it, like if argument is one object, 
# generator divides argument to a serie of single object and works on/return every single value with yield statement. 
# for example: if you want to slide on a list with function you have to do a for/while loop inside function 
# but every single item remain a little piece of a bigger object which is our original parameter. 
# with yield statement you can operate on single element of argument like if it is a single object without relations with previous or next element of parameter. 
# this is HOW I understood difference between return and yield, I hope to help someone

# play - call a function, stop - return, pause - yield


# Yield is a keyword that is used like return, except the function will return a generator. 
# Each time the function is called, yield will return the next value, until there is no value to return.


# Generators are good if you working with large dataset that might overwhelm your memory.
# https://realpython.com/introduction-to-python-generators/


# SECTION 2
# Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
# In fact, they can be infinite!
def infinite_sevens():
  while True:
    yield 7
#       

for i in infinite_sevens():
  print(i)
#
# In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

# The generator creates and then "yields" only one value at a time. 
# This saves time in creating because instead of the entire list being created before passing, only one value is created then passed. 
# Also saves space because only one the current value exists. 

# https://www.programiz.com/python-programming/generator

# Yield is like "return" in def functions. But at return, the funtions stops and returns its value. 
# With yield, it just returns 1 value and pause. When you call the function again (in a loop or something), it continues where it was left. 
# A normale functions always starts at the beginning.

# You can use yield generators for calculating large sets of data, 
# where you don't know if you are going to need all results or dont want to waste memory allocating the whole sets/lists. 
# Because they will give one result at the time u can iterate over really big amounts of data or a infinite range of numbers without filling ur memory or even crashing ur computer. 
# For more info you can refer to: PEP-0255


# Example:
def countdown():
    i=5
    while i >= -5:
        yield i
        i -= 1

for i in countdown():
    if (i > 0):
      print(i,15*" ","|")
      
    elif (i==0):
     print(i,4*" ",10*"-","o",10*"-")
     
    else:  
      print(i,14*" ","|")
#      


# https://www.oreilly.com/content/2-great-benefits-of-python-generators-and-how-they-changed-me-forever/


# Example: Infinite Prime Generator
def primes():
    yield 2
    cur_primes = [2]
    n = 2
    while True:
        n += 1
        for p in cur_primes:
            if n % p == 0:
                break
        else:
            cur_primes.append(n)
            yield n

l = primes()
print(next(l))
print(next(l))
print(next(l))


# How to create a generator in Python? It is fairly simple to create a generator in Python. 
# It is as easy as defining a normal function, but with a yield statement instead of a return statement. 
# If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. 
# Both yield and return will return some value from a function. 
# The difference is that while a return statement terminates a function entirely, 
# yield statement pauses the function saving all its states and later continues from there on successive calls.


# Example:
def is_prime(num):
    return [i for i in range(2,num) if num%i == 0] == []

def get_prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
            num += 1

for i in get_prime():
    print(i)
#


# Example: To create a prime number generator, that yields all prime numbers in a loop. (Consider having an is_prime function already defined):
def get_primes():
  num = 2
  while True:
    if is_prime(num):
      yield num
    num += 1
#

# Example:
def is_prime(num):
    for i in range(2,num): 
        if num % i == 0: 
            return False 
            return True     # It returns False if number is not prime, and True if number is prime
#

# Example:
def isPrime(n): 
    for i in range(2,n): 
        if n%i==0: 
            return False 
            return True 

def getPrime(m): 
    while m<20: 
        if isPrime(m): 
            yield m
            m+=1 
            print(list(getPrime(7))) 
# [7,11,13,17,19] 
# the curious thing is when " if n%i==0: return False return True " When indentation "return True" in line with "if",
# the result is different as below: [7,9,11,13,15,17,19]


# Example:
def is_prime(num): 
    return [i for i in range(2,num) 
    if num%i == 0] == []
#


# Example to edit:
def isPrime(n): 
    for i in range(2,n): 
        if n%i==0:
            return False 
            return True 

def getPrime(m): 
    while m<50: 
        if isPrime(m): 
        yield m 
        m+=1 
        print(list(getPrime(9))) # [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47] 
#


# SECTION 3
# Finite generators can be converted into lists by passing them as arguments to the list function.
# Example:
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))    # [0, 2, 4, 6, 8, 10]

# Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage. 
# Furthermore, we do not need to wait until all the elements have been generated before we start to use them. 

# Example: Probably 3 ways of doing this
def numbers(x): 
    for i in range(x): 
        if i % 2 == 0: 
            yield i 

print(list(numbers(11)))                                # [0, 2, 4, 6, 8, 10]
print(list([x for x in range(11) if x % 2 == 0]))       # [0, 2, 4, 6, 8, 10]
print(list(filter((lambda x: x % 2 == 0), range(11))))  # [0, 2, 4, 6, 8, 10]
print([x for x in range(11) if x%2==0])                 # [0, 2, 4, 6, 8, 10]


# "return" vs "yield"
# They haven't the same purpose and we don't use them in the same way. 
# 1- yield generalises the list comprehension concept. Let's talk about the lesson's example. 
# With yield, the function produces a generator. No list is actually built. 
# To instantiate the list, we build it outside the function with the builtin function list(). 
# 2- with return, the function produces a "ready to use" object. Here, we should have built the list inside the function. 
# 3- let's use now another simple example. We want to get the square of a number: def sq(x): return x*x or def sq(x): yield x*x 
# In the first case, the function returns a number you can directly use: print("The square of 11 is", sq(11)) 
# In the second case, the function yields a generator that you have to use to build a list containing one number, 
# then index the list to finally get the number: print("The square of 11 is", list (sq(11))[0])


# Example:
def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))    # ['s', 'sp', 'spa', 'spam']

# Example:
def make_world(): 
    x="12345" 
    for i in "asd": 
        x=x+i 
        yield x 

print(list(make_world())) # ['12345a', '12345as', '12345asd']



