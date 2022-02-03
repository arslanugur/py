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


# SECTION 2
# There are many functions in itertools that operate on iterables, in a similar way to map and filter.
# Some examples:
# takewhile - takes items from an iterable while a predicate function remains true;
# chain - combines several iterables into one long one;
# accumulate - returns a running total of values in an iterable. 
# Example:
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)                                     # [0, 1, 3, 6, 10, 15, 21, 28]
print(list(takewhile(lambda x: x<= 6, nums)))   # [0, 1, 3, 6]
# 0+1, 1+2, 3+3, 6+4, 10+5, 15+6, 21+7, 28+8    # Total + NextSequenceInRange

# accumulate goes like this:
# if 0 is there, add numbers up to 0(0+0=0) 
# if 1 is there, add numbers up to 1(0+1=1) 
# if 2 is there, add numbers up to 2(0+1+2=3) 
# if 3 is there, add numbers up to 3(0+1+2+3=6) 
# if 4 is there, add numbers up to 4(0+1+2+3+4=10) and so on

# Example:
print(list(chain([1,3,2], [3,5,9]))) 
print(list(chain(["man","nan"], ["pan"]))) # output: [1, 3, 2, 3, 5, 9] ['man', 'nan', 'pan'] just to illustrate an example of the CHAIN function

# Difference between filter and takewhile is that filter takes all the elements which satisfy the predicate function 
# while takewhile will stop taking elements the moment an element doesn't satisfy the predicate function

# A way to help you understand lessons and improve your problem solving skills is to read the program and its results, 
# then type out the program yourself and go over it line by line. 
# Why does it print what it prints? in this case: nums = list(accumulate(range(8))) 
# nums holds the value list(accumulate(range(8))) 
# list is telling it to print in list form (i.e. in brackets []) 
# accumulate is saying that it is going to return the individual values add to it's predecessor one at a time 
# range is just limiting it to remain in the range of 8 (i.e. 0-7) 
# print(nums) will produce: >>> [0, 1, 3, 6, 10, 15, 21, 28] 
# Breakdown: 
# range = 0, 1, 2, 3, 4, 5, 6, 7 
# so 0=0, 1+0=1, 2+1=3, 3+3=6, 4+6=10, 5+10=15, 6+15=21, 7+21=28 
# it moves through the range one at a time ACCUMULATING as it processes. 
# print(list(takewhile(lambda x: x<= 6, nums))) 
# x is the placeholder for nums """ 
# it will take the result of nums printed and print the sequence as long as the output is equal to or less than 6. the lambda is our parameter to set

# Example: 
from itertools import takewhile,chain 
mylist = [0,1,3,6,10,15,2,1] 
print(mylist) # [0, 1, 3, 6, 10, 15, 2, 1]
a = lambda x:x<=6 
tw = list(takewhile(a,mylist)) 
fl = list(filter(a,mylist)) 
ch = list(chain(tw,fl)) 
print(tw)   # [0, 1, 3, 6]
print(fl)   # [0, 1, 3, 6, 2, 1]
print(ch)   # [0, 1, 3, 6, 0, 1, 3, 6, 2, 1] 


# the difference between takewhile and filter 
# filter goes through all the elements of the iterabele takewhile checks the condition as long as it is True. when it hit False, it exits the iterable.

# print(list(takewhile(lambda x: x<=6, nums))) 
# This takes the values of nums and puts them into the variable x one at a time. 
# For the values that result in the expression being true it prints the value in a list.

# takewhile-get the values of the sequence, until the value of the predicate function for its elements is true; 
# dropwhile-receiving sequence values starting with an element for which the value of the predicate function will cease to be true. 
# From itertools import takewhile, dropwhile Numbers = [1, 5, 8, 5, 1] Predicate = lambda x: x <6 For value in takewhile (predicate, numbers): 
# Print (value) Print () For value in dropwhile (predicate, numbers): Print (value) Output >>> 1 >>> 5 >>> 8 >>> 5 >>> 1


# I found some facts about takewhile function. 
# I experimented with four operators(<, <=, >, >=) and those working normally in 'takewhile' were < and <=. 
# I think it's because the iteration process starts with the first element. 
# So if the first element doesn't satisfy the predicate function, it won't start any iteration. Hence all you can see is an empty list. 
# However, this is not the case when the condition changes. 
# If you change <= to > and 6 to -1 in this example, you will see the whole list. 
# In conclusion, all four operators are valid in takewhile function. 
# But what makes the output valid is whether the predicate function is satisfied or not.

# Idk why an example of chain is not shown on the lesson, but here it goes: 
from itertools import accumulate, takewhile, chain 
nums = list(accumulate(range(8))) 
print(nums)                                                                 # [0, 1, 3, 6, 10, 15, 21, 28]
print(list(takewhile(lambda x: x<= 6, nums)))                               # [0, 1, 3, 6] 
print(list(chain(accumulate(range(8)),takewhile(lambda x: x<= 6, nums))))   # [0, 1, 3, 6, 10, 15, 21, 28, 0, 1, 3, 6] 


# Example:
from itertools import accumulate 
def sigma(n): '''Returns sum of integers from 0 to n''' 
    if n == 0: 
        return 0 
    return n + sigma(n-1) lst1 = [sigma(i) for i in range(8)] 
lst2 = list(accumulate(range(8))) print(lst1 == lst2)
    
range(8) = 0,1,2,3,4,5,6,7 accumulate = 0,0+1,0+1+2,0+1+2+3,0+1+2+3+4,0+1+2+3+4+5,0+1+2+3+4+5+6,0+1+2+3+4+5+6+7


https://www.sololearn.com/learning/1073/2466/5117/2


        
        



