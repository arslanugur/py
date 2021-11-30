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

         

# To be technically clear, here's a snippet taken from the section on ranges in the official Python docs. 
# The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for loops. 
# class range(stop) 
# class range(start, stop[, step]) 

# The arguments to the range constructor must be integers (either built-in int or any object that implements the __index__ special method). 
# If the step argument is omitted, it defaults to 1. 
# If the start argument is omitted, it defaults to 0. 
# If step is zero, ValueError is raised. 
# For a positive step, the contents of a range r are determined by the formula r[i] = start + step*i where i >= 0 and r[i] < stop." 
# So then... The default step is 1. 
# So, the range 3,8 starts at 3, increments by 1 until the value is 1 less than the stop.
# Basically it's like... r=3 while r < 8: print(r) 
# Personally not intuitive imo, neither is starting a range at 0. It's just how it works. 



# RANGE - THE THIRD ARGUMENT      
# range can have a third argument, which determines the interval of the sequence produced, also called the step. 
numbers = list(range(5, 20, 2))     # (start, stop, step)
print(numbers)      # [5, 7, 9, 11, 13, 15, 17, 19]
         
# We can also create list of decreasing numbers, using a negative number as the third argument, for example list(range(20, 5, -2)).


# If the interval of sequence is negative and the second element is greater than the first: 
numbers = list(range(0, 10, -2)) 
print(numbers) # []

# If the interval of sequence is negative but the second element is smaller than the first: 
numbers = list(range(10, 0, -2)) 
print(numbers) # [10, 8, 6, 4, 2]  


# Example:
numbers = list(range(5, 20, 4//2)) 
print(numbers) #  [5,7,9,11,13,15,17,19]


# Example:
numbers = list(range(5, 20, 2)) 
j=0 
while j< len(numbers): 
    if numbers[j]% 3 != 0: 
        print(numbers[j]) 
        j+=1 
        # 5 7
        # 5 7 11 13 17 19


# Example:
numbers = list(range(5, -5, -2)) 
print(numbers)  # [5, 3, 1, -1, -3]
         
         
# list(range(A:B:C)), the value of C should be added to A in a way that it gradually reaches B.
# If A=1 and B=10, C has to be a POSITIVE value. So it can be added to A to reach B.
# If A=-10 and B=-1, C has to be a POSITIVE value. It's same as the previous case.
# If A=1 and B=-10, C has to be a NEGATIVE value. Because, it should be added to A to reach B.
# If A=-1 and B=-10, C has to be a NEGETIVE value. It's same as the previous case.


# This is just a way of understanding range() arguments.
# When range has three arguments, it can be understood in the way for loop has arguments in C, C++, etc: 
range(5, 20, 2) # Python
for(int i = 5; i < 20; i += 2)  # some languages         
# Thus, it can be rewritten as:- 
range(first_arg, second_arg, third_arg) # in Python 
for(int i = first_arg, i < second_arg, i += third_arg) # in languages like C, C++



# If you put the integer greater than the range, it gives the first element as output. 
nums = list(range(5,20,100))
print(nums)     # [5] --> The first element will be showcased
         
         
# Example:
nums = list(range(3, 15, 3))
print(nums[2])  # 9
# print(nums)   # [3, 6, 9, 12] <-- created list range 
                #  0  1  2  3   <-- index
         
# for LOOPS and RANGE
# The for loop is commonly used to repeat some code a certain number of times.
# This is done by combining for loops with range objects.         
for i in range(5):
    print("to write this five times with range")
#   print(i)

# You don't need to call list on the range object when it is used in a for loop, 
# because it isn't being indexed, so a list isn't required.

# Example:
for i in range(10,50,10): 
    print("Wealth! "+str(i)) 
    # Wealth! 10 
    # Wealth! 20 
    # Wealth! 30 
    # Wealth! 40


# Example:
for i in range(10): 
    if i==3: 
        print("We are skipping 'i' here!") 
        continue 
    elif i==8: 
        print("We are breaking the loop here!") 
        break 
    else: 
        print("Python!",i) 
# output:
# Python! 0
# Python! 1
# Python! 2
# We are skipping 'i' here!
# Python! 4
# Python! 5
# Python! 6
# Python! 7
# We are breaking the loop here!


# Example: loop in loop 
for i in range(4): 
    for a in range(4): 
        if a <= i: 
            print('*', end=' ') 
        else: 
            print(' ', end=' ') 
print() # output: *       * *     * * *   * * * * 
     

# Example:
items = ["A", "B", "C", "D", "E"] 
n = len(items) 
for i in range(n):
    print(str(i + 1) + ". " + items[i]) # output: 1. A 2. B 3. C 4. D 5. E

# Example: to create a for loop that prints only the even values in the range:
for i in range(0, 20, 2):
  print(i)  # 0, 2 ... , 18 --> that mean it returns all even numbers in range from 0 to 20
            # even numbers - numbers which can be devided by 2 without the rest
            # odd numbers - numbers which can not be devided by 2 without the rest
for i in range[0,20,3]
  print(i)  # return will looks like: 0 3 6 9 12 15 18 so it result with either some even and odd numbers



