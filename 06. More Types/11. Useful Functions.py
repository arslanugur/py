# STRING FUNCTIONS
# Python contains many useful built-in functions and methods to accomplish common tasks.
# join - joins a list of strings with another string as a separator.
# replace - replaces one substring in a string with another.
# startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
# To change the case of a string, you can use lower and upper.
# The method split is the opposite of join turning a string with a certain separator into a list. 
# Some examples:
# join()
print(", ".join(["spam", "eggs", "ham"]))           # "spam, eggs, ham"
print("Hello ME".replace("ME", "world"))            # "Hello world"
# startswith()
print("This is a sentence.".startswith("This"))     # "True"
# endwith()
print("This is a sentence.".endswith("sentence."))  # "True"
# upper()
print("This is a sentence.".upper())                # "THIS IS A SENTENCE."
# lower()
print("AN ALL CAPS SENTENCE".lower())               # "an all caps sentence"
# split()                                           # split() = split(" ")
print("spam, eggs, ham".split(", "))                # "['spam', 'eggs', 'ham']"
print("spam, eggs, ham".split("a"))                 # ['sp', 'm, eggs, h', 'm']
print("this is a sentence.".capitalize())           # "This is a sentence."

# https://www.pythonforbeginners.com/dictionary/python-split

# These functions need dealing with individually. 
# At least do specific quizzes for join & split, two very frequently needed functions. Only quizzing on .upper seems odd.
# Also the all quiz should be easier - by all means do tortuous, tricky tests at the END of a unit, 
# but when you're encountering a new topic for the first time you need a super simple example that helps you understand simply.

# Example:
sent = "Hello have a nice day"
print(sent)               # Hello have a nice day 
sent1 = sent.split(" ") 
print(sent1)              # ['Hello', 'have', 'a', 'nice', 'day'] 
sent1[3] = "super" 
sent2 = " ".join(sent1) 
print(sent2.upper())      # HELLO HAVE A SUPER DAY 
sent3 = sent2.replace("day", "week")
print(sent3.lower())      # hello have a super week


# Example for the replace function: 
for i in range(5): 
  print(("Hello X").replace("X", str(i))) # Hello 0 Hello 1 Hello 2 Hello 3 Hello 4
#

# Example: to turn the string uppercase.
a = "Spam"
b = a.upper()
print(b)


# Example:
a = "Cool" 
b = a.upper()   # COOL
b = a.lower()   # cool
print(b)



# NUMERIC FUNCTIONS
# To find the maximum or minimum of some numbers or a list, you can use max or min.
# To find the distance of a number from zero (its absolute value), use abs.
# To round a number to a certain number of decimal places, use round.
# To find the total of a list, use sum.
# Some examples:
print(min(1, 2, 3, 4, 0, 2, 1))     # 0
print(max([1, 4, 9, 2, 5, 6, 8]))   # 9
print(abs(-99))                     # 99
print(abs(42))                      # 42
print(sum([1, 2, 3, 4, 5]))         # 15


# Example:  https://en.wikipedia.org/wiki/IEEE_754#Rounding_rules
a = 3.652
print(round(a,1) # 3.7 
print(round(a,0) # 4.0 
print(round(a,3) # (or any number higher than 3) will give 3.652

# Examples:
print(round(5.6184,2))      # 5.62 
print(round(4656.46279,-3)) # 5000

# Example: 
i = 98765.4321
print(round(i))       # 98765 (rounds to full number)
print(round(i,1))     # 98765.4 (rounds to 1 decimal)
print(round(i,2))     # 98765.43 (rounds to 2 decimals)
print(round(i,3))     # 98765.432 (rounds to 3 decimals)
print(round(i,4))     # 98765.4321 (rounds to 4 decimals)
print(round(i,-1))    # 98770.0 (rounds to nearest 10) 
print(round(i,-2))    # 98800.0 (rounds to nearest 100)
print(round(i,-3))    # 99000.0 (rounds to nearest 1000)
print(round(i,-4))    # 100000.0 (rounds to nearest 10000)

# Example:
print(round(3.5))         # 3 
print(round(3.5000001))   # 4 
print(round(-3.4))        # -3 
print(round(-3.5))        # -4  since it chooses the smaller number and -4 < -3 


# it happens: (2.5 rounds to 2, 3.5 rounds to 4) because of binary collision with these decimal numbers. 
# Try this trick that you'll find how deep is rabbit hole
print(0.1+0.1+0.1)                      # for 3 times 0.1     # 0.30000000000000004
print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1)  # 8 times the same    # 0.7999999999999999
# Decimals are so hard for binary system (computer tells straight conversely)

# Example:
sum = sum([i for i in range (5)]) 
print(sum)  # 10


# sum, min and max can also take dictionaries as inputs, 
# but remember that by default, keys will be attached, not values, which may sound quite counter intuitive! (unless you use the method .values())
print(max({i: i*2 for i in range(5)}))          # 4
print(max({i: i*2 for i in range(5)}.values())) # 8

# Example: py uses the engineering notation of "j" and not "i" 
print(abs(3+4j))  # 5.0

# Examples:
print(round(1.5))   # 2 
print(round(2.5))   # 2
print(round(3.5))   # 4
print(round(4.5))   # 4
print(round(5.5))   # 6
print(round(6.5))   # 6
print(round(7.5))   # 8
print(round(8.5))   # 8
print(round(102.5)) # 102
print(round(101.5)) # 102 

print(round(-1.5))  # -2
print(round(-2.5))  # -2
print(round(-3.5))  # -4
print(round(-4.5))  # -4
print(round(-5.5))  # -6
print(round(-6.5))  # -6
# being round off is odd, it becomes the next counting whole number irrespective of the sign 
# if number is even the result is the number

print(max({i: i*2 for i in range(5)}))          # 4
print(max({i: i*2 for i in range(5)}.values())) # 8


# Example:
a = min([sum([11, 22]), max(abs(-30), 2)])
print(a)    # 30
# So, the sum of 11 and 22 is 33 
# The absolute value of -30 is 30, because it is 30 numbers away from 0
# Between 30 and 2, 30 is bigger, "max" is responsible for determing the bigger number
# Now we are left with a=min([33,30]), "min" deals with determing the smallest number. Since 30 is smaller than 33, it's going to print out 30.
# a = 30



# LIST FUNCTIONS
# Often used in conditional statements, all and any take a list as an argument, 
# and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise).
# The function enumerate can be used to iterate through the values and indices of a list simultaneously.
# Example:
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")      # All larger than 5

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")   # At least one is even

for v in enumerate(nums):
    print(v)
"""
Output:
(0, 55)
(1, 44)
(2, 33)
(3, 22)
(4, 11)
"""

# For the .enumerate function, you can specify what index number you want to start with. 
# Example: 
for v in enumerate(nums, -1): 
print(v) # (-1, 55) (0, 44) (1, 33) (2, 22) (3, 11)
# https://docs.python.org/3/library/functions.html?highlight=enumerate#enumerate

# Example:
nums = [55, 44, 33, 22, 11] 
abc = [i > 25 for i in nums] 
print(abc) # [True, True, True, False, False]



# You may skip the square brackets. And then instead of a list, a generator will be sent to the function. 
# It is good practice for optimization 
# because the function any() iterates the elements till first True value and immediately returns True (or till the end and returns False, if they all are False). 
# As well as the function all() iterates the elements till first False (or till the end if they all are True).  
# For example, in the code any([i % 2 == 0 for i in numbers]) 
# all values of the expression (i % 2 == 0) will be calculated and stored in the list, only after that they all are passed to the function any(). 
# In the code any(i % 2 == 0 for i in numbers) values will be calculated 
# and passed to the function any() one by one till first True (44 % 2 == 0) and the rest of the values will not be calculated at all.  
# So, sometimes using a generator may reduce the running time of your code.



# The main logic
# Creating an empty list 
logic = list() 
print(all(logic)) # True - no False elements
print(any(logic)) # False - No True elements
# https://docs.python.org/3/library/functions.html?highlight=all#all

# So here is important 'enumerate' function it just making tuples of two numbers first just index and other is importing from the mentioned list.
# Example
nums = [ 55, 44, 33, 22, 11] 
for v in enumerate[nums] 
# as we did not starting index so print(v) gives print(v) (0,55) (1,44) (2,33) (3,22) (4,11) 
# but if we were try for v in enumerate[nums,2] 
# then print(v) gives print(v) (2,55) (3,44) (4,33) (5,22) (6,11) 


nums = [55, 44, 33, 22, 11] 
ab = [i>5 for i in nums] 
print(ab)
cd = [i%2==0 for i in nums] 
print(cd) 
ab = any([i>5 for i in nums]) 
print(ab)
cd = all([i%2==0 for i in nums]) 
print(cd) 
ab = all([i>5 for i in nums]) 
print(ab)
cd = any([i%2==0 for i in nums])
print(cd)
if all([i > 5 for i in nums]):
print("All larger than 5")
if any([i % 2 == 0 for i in nums]): 
print("At least one is even") 
for v in enumerate(nums, -2): 
print(v)


# Example:
nums = [-1, 2, -3, 4, -5]

if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)  #
#
# It will print 2 because, abs return the distance between 0 to given parameter in abs function. 
# All function check all is true(here is not). 
# first of all see the for loop, 
# 1) i in nums is =-1 , abs(-1)=1, 1<3=true 
# 2) i in nums is =2 , abs(2)=2, 2<3=true 
# 3) i in nums is =-3 , abs(-3)=3, 3<3=false 
# 4) i in nums is =4 , abs(4)=4, 4<3=false 
# 5) i in nums is =-5 , abs(-5)=5, 5<3=false
# To understand this question, first solve the negative value, I.e abs(-1) = 1 abs(-3) = 3 abs(-5) = 5 
# Therefore we have: nums=[1,2,3,4,5] Then the conditions: all abs is not less than 3, so the program print 2.


# The code is first taking the absolute value of a numbers (meaning all values will be positive). 
# Then it asks if after the numbers have been made positives are the numbers ALL less than 3 if so then it would print 1 else it would print 2 

# To understand this question, first solve the negative value, I.e abs(-1) = 1 abs(-3) = 3 abs(-5) = 5 
# Therefore we have: nums=[1,2,3,4,5] 
# Then the conditions: all abs is not less than 3, so the program print 2.


# Examples: 
print(i for i in nums)            # <generator object <genexpr> at 0x01C60390> # Some random memory location 
print([i for i in nums])          # [-1, 2, -3, 4, -5] 
print([abs(i) < 3 for i in nums]) # [True, True, False, False, False] 
# It contains list of boolean and input of function all() and any() MUST BE list of True/False. 


