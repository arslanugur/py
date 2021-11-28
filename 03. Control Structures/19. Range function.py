# The range() function returns a sequence of numbers.
# By default, it starts from 0, increments by 1 and stops before the specified number.

# The code below generates a list containing all of the integers, up to 10.
numbers = list(range(10))
print(numbers)
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# In order to output the range as a list, you need to explicitly convert it to a list, using the list() function.


# Examples:
print(list(range(5)))               # [0,1,2,3,4] 
print(list("Hello"))                # ['H' , 'e' , 'l' , 'l' , 'o'] ✔️ 
# "range" is a built-in function which can be used for creating a sequence of integer 
numbers = [1, 2, 3, 4, 5, 6, 7]
print(range(5))                     # range(0, 5)
print(range(0, 5))                  # range(0, 5)
print(list(range (5)))              # [0,1,2,3,4]
print(list(range (0,5)))            # [0,1,2,3,4]
print(list(range (1,5)))            # [1,2,3,4]
print(list(range (1,10,2)))         # [1,3,5,7,9] 
print(list(range (1,10,-1)))        # [] 
print(list(range (10,1,-1)))        # [10,9,8,7,6,5,4,3,2] 
print(list(range(1,5,1.67)))        # type error

# Range versus List Range differs from a List 
# because a range object stores only start, end, step instead of individual elements whereas a list object actually saves each elements. 
# In the case of large sequential integer elements, range uses little memory comparing to list. 
# When you want to explicitly see what a range object represents, convert to list and print it.

# Range Example with Negative nums: 
# Need to print list with negative nums from -1 to -20 (3th parameter = step). 
numbers = list(range(-1,-21,-1)) 
print(numbers)                    # [-1, -2, -3 ... -19, -20]

# Example: Find Age with Range
findAge= list(range(1991,2021)) 
print(len(findAge)) #28

# Example:
a = list(range(5))      # output: [ 0, 1, 2, 3, 4 ]       # Notice it prints 5 values starting from Zero.
b = list(range(20,25))  # output: [ 20, 21, 22, 23, 24 ]  # Notice it prints 20 but stops at 24.
c = list(range(6,12, 2) # output: [ 6, 8, 10 ]            # Notice the third value is the increment.


# Example:
col = [] 
sum = 0 
for j in range(20): 
    col.append(sum) 
    sum += j 

print(col[7]) # 21

# Example:
numbers = list(range(10)) 
for i in numbers:
    numbers.remove(i)

print(numbers)      # [1, 3, 5, 7, 9]

# Example:
numbers= range(10) 
print(numbers) # output: range(0,10)

# Example:
nums = list(range(5))
print(len(nums))    # total 5 items (0,1,2,3,4) 
print(nums[4])      # 4

# Example:
list = [10,11,12,13,14]
len(list) == 5 # remember indexing starts at 0
list[0] == 10 
list[1] == 11 
list[2] == 12 
list[3] == 13 
list[4] == 14




# TWO ARGUMENTS IN RANGE
# If range is called with one argument, it produces an object with values from 0 to that argument.
# If it is called with two arguments, it produces values from the first to the second.
# For example:
numbers = list(range(3, 8))
print(numbers)  # [3, 4, 5, 6, 7]
print(range(20) == range(0, 20))    # True
# Remember, the second argument is not included in the range, so range(3, 8) will not include the number 8. 

# Example:
numbs=list(range(0,11,2)) 
print(numbs) # output will be: [0,2,4,6,8,10] 
# because number 2, the 3th number in 'range ', is the distance between 'list ' numbers

# Example:
nums = list(range(10,0,-1))
print(nums) # output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Example:
numbers = list(range(-5,1))
print(numbers)  # output: [-5, -4, -3, -2, -1, 0]


# Example:
numbers = list(range(0, 10))
print(numbers)                      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers == range(0, 10))      # False
print(range(10) == range(0, 10))    # True

# Example:
nums = list(range(5, 8))
print(len(nums))    # 3     # 5 = 1; 6 = 2; 7 = 3       # 8 - 5 = 3


# Examples:
# Note: List is used here 
# so it stores each number in the range in a list. without it, 
# your output would be [0, 5] instead of [0, 1, 2, 3, 4, 5]. 

a = list(range(5)) # output: [ 0, 1, 2, 3, 4 ] 
# Notice it prints 5 values starting from Zero. 
b = list(range(20,25)) # output: [ 20, 21, 22, 23, 24 ] 
# Notice it prints 20 but stops at 24. 
c = list(range(6,12, 2) # output: [ 6, 8, 10 ] 
# Notice the third value is the increment.

# Example: List vs Range
# "list" is a function which creates lists. 
list(range(5))  # [0,1,2,3,4]
list("Hello")   # ['H' , 'e' , 'l' , 'l' , 'o']

# "range" is a built-in function which can be used for creating a sequence of integer numbers
list(range(5))         # [0,1,2,3,4]
list(range(0,5))       # [0,1,2,3,4]
list(range(1,5))       # [1,2,3,4]
list(range(1,10,2))    # [1,3,5,7,9]
list(range(1,10,-1))   # []
list(range(10,1,-1))   # [10,9,8,7,6,5,4,3,2]
list(range(1,5,1.0))   # Error
list(range(1,5,1.67))  # Error


# "it's worthy to note that the range function takes three arguments: the beginning value, the ending value, and the step. See example below " 
a = range (10, 20, 2) #creates a range from 10 to 20 every 2 steps 
b = list(a) 
print(a) 
print(b) 
# output: range(10, 20, 2) [10, 12, 14, 16, 18]

         
"""
To be technically clear, here's a snippet taken from the section on ranges in the official Python docs. 
"The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops. 
class range(stop) 
class range(start, stop[, step]) 

The arguments to the range constructor must be integers (either built-in int or any object that implements the __index__ special method). 
If the step argument is omitted, it defaults to 1. 
If the start argument is omitted, it defaults to 0. 
If step is zero, ValueError is raised. 
For a positive step, the contents of a range r are determined by the formula r[i] = start + step*i where i >= 0 and r[i] < stop." 
So then... The default step is 1. 
So, the range 3,8 starts at 3, increments by 1 until the value is 1 less than the stop.
Basically it's like... r=3 while r < 8: print(r) 
Personally not intuitive imo, neither is starting a range at 0. It's just how it works. 
"""



