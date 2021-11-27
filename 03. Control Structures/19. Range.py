# The range() function returns a sequence of numbers.
# By default, it starts from 0, increments by 1 and stops before the specified number.

# The code below generates a list containing all of the integers, up to 10.
numbers = list(range(10))
print(numbers)
# output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# In order to output the range as a list, you need to explicitly convert it to a list, using the list() function.

"it's worthy to note that the range function takes three arguments: the beginning value, the ending value, and the step. See example below " 
a = range (10, 20, 2) #creates a range from 10 to 20 every 2 steps 
b = list(a) 
print(a) 
print(b) 
# output: range(10, 20, 2) [10, 12, 14, 16, 18]


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

# Range v.s. List Range differs from a List 
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
print(nums[4])  # 4
