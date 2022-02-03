# SECTION 1
# The module itertools is a standard library that contains several functions that are useful in functional programming.
# One type of function it produces is infinite iterators.
# The function count counts up infinitely from a value.
# The function cycle infinitely iterates through an iterable (for instance a list or string).
# The function repeat repeats an object, either infinitely or a specific number of times.
# Example:
from itertools import count

for i in count(3):
    print(i)
    if i >=11:
        break
#

# Good to add at this point (as this might actually come in handy) that count has two arguments: 
# count(x, y) where x is a start value and y is the increment/decrement pace (with y being a positive or negative number, respectively). 
# So count(4, 5) will produce: 4 9 14 19 24 . . . whereas count(20, -3) will give us: 20 17 14 11

# Example:
from itertools import repeat 
# Gimme a list which has "Seinfeld" string 5 times 
print(list(repeat("Seinfeld", 5))) 
# Gimme a list with number 77 appearing 5 times 
print(list(repeat(77, 5))) 
# give a list with INFINITE times "Seinfeld" string appearing 
# KILL program ASAP to save urself 
print(list(repeat("Seinfeld"))) # ['Seinfeld', 'Seinfeld', 'Seinfeld', 'Seinfeld', 'Seinfeld'] [77, 77, 77, 77, 77]


# Examples: Small examples of three functions of itertools: 
# 1. Count 2. Cycle 3. Repeat 
# Count Example: (prints numbers 3 to 5) 
for i in count(3): 
  print(i) 
  if i>5: 
    break         # 3 4 5 
# 
# Cycle Example: (prints mylist few times)
mylist=[1,2,3,4,5] 
for i in cycle(mylist): 
  print(mylist) 
  if i>3: 
    break         # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] 
#                    
# Repeat Example: 
mylist=[1,2,3,4,5] 
print(list(repeat(mylist,3))) # [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]] 
mylist=['apple','milk','jiuce']
counter = 0
for each_element in cycle(mylist):
  counter += 1
  print(counter, each_element)
  if counter == 10:
    break           # 1 apple 2 milk 3 jiuce 4 apple 5 milk 6 jiuce 7 apple 8 milk 9 jiuce 10 apple 
#
# Note: the point to note is without the "cycle" keyword in the for loop, 
# the loop will stop looping when it reaches the end of list, 
# however, becoz of "cycle" function, it reloops from beginning again, until coun


# Example: Same behaviour can be achieved with a generator like below: 
def count(start, step=1): 
    i = start 
    while True: 
        yield i 
        i += step 

for x in count(3):
    print(x)
    if x >= 11:
        break 
#


# Example:
from itertools import count
for i in count(3,0.55):
    print(i)
    if i >=11:
        break   
# 

# for what reason we need to use count. count(start, step) Ok... but we using for. 
# So... what the real difference with range? range(start, stop, step) 
# Only because it can counting for infinite? Or because range default is stop and count default is start? 
# From my point of view it's little useless function. And if we need infinite count we can use generator. 
# So. Can someone give me a good reason to use count?

# from itertools import repeat p=0 for i in repeat(3): p=p+1 print(i) if p>=11: break

# same output with the following code. 
from itertools import count 
for i in count(3): 
    if i <= 11: 
        print(i)
#

# https://docs.python.org/3/library/itertools.html

# Example:
for i in repeat(5,9): 
    print(i) # output :- 5 5 5 5 5 5 5 5 5 "nine fives"
#

# This could be a useful reference as we change gears and move from Functional Programming to Object Oriented Programming in the next module. 
# It also links to itertools. https://docs.python.org/3/howto/functional.html
  
# Same code can be written with Range function. 
for i in range(3,12): 
    print(i)
# 

# Example: To import the cycle function from the itertools module.
from itertools import cycle             # from (module name) import (function name)             # Modules are in libraries

# Example:
for i in "python": 
    print(i)
# The above code outputs just the following: p y t h o n 
# now try cycle infinitely from itertools import cycle for i in cycle("python"): print(i) 
# Output: p y t h o n p y t h o n  still doing printing infinitely that could be useful 
# especially if u used break like you define a variable = 0 
# and u increase the variable with every t in python and when it hits number of repeats you break the for loop
# wish that helped you understanding the difference
# or in something like stop=0 for i in cycle("python"): print(i) if stop ==8: break stop =stop+1

# In english readability, this code would mean : 
# *from* the library itertools, 
# *import* a function called 'cycle' into my library/code.


# Answer: from itertools import cycle 
# As They Have Said to Only import "cycle" class/function from the itertools module... 
# importing all function/classes will be: from itertools import * OR, import itertools 
# Format: import {module-name} or from {module-name} import {class/function}



https://www.sololearn.com/learning/1073/2466/5117/1




BEGINNER LEVEL PROGRAMMING PROJECTS 
https://www.sololearn.com/post/4869/?ref=app 
  https://www.sololearn.com/post/4870/?ref=app 
    https://www.sololearn.com/post/4873/?ref=app 
      https://www.sololearn.com/post/4874/?ref=app

        
        



