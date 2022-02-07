# Functional Programming Examples:
# Example 1:
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)

print(len(list(nums)))  # 2

# Explanation:
nums = {1,2,3,4,5,6} # nums is a set --> A set of numbers from 1 to 6
# builds intersection with &: 
nums = {0,1,2,3} & nums # & will only include values that both sets have.
                        # The & is the intersect command that keeps item that is in both set: {0, 1, 2, 3} & {1, 2, 3, 4, 5, 6} = {1, 2, 3} 
# nums = {1, 2, 3}      # The intersection is {1,2,3}
nums = filter(lambda x: x > 1, nums) # filter is used to remove values that are not needed --> Filters out item that is greater than 1.
# list(nums) = [2, 3] 
print(len(list(nums))) # It's asking you to print out the length of nums. = 2


# Example 2:
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)

print(power(2, 3))     # power(2,3) = 2*power(2,2) = 2*2*power(2,1) = 2*2*2*power (2,0) = 2*2*2*1 = 8
# 2 3 2* f(2,2) 2* (2 * f(2,1))) 2* (2 * (2 * f(2,0))) 2* (2 * (2 * 1)) = 8

# This question is based on recursion principle.... 
# Consider the power(2,3) function. For the first call the value will be power(2,3).
# Thus at the end of first iteration the return value will be 2*power (2,2). 
# For the second call x remains same while y decreases by 1 so it will proceed as power(2,2).
# Now the return value will be {2*power(2,1)} which will be substituted in the place of power(2,2) in first iteration. 
# In third call function arguments are power(2,1). 
# Similarly the return value will be {2*power (2,0)} which will be substituted in the place of power(2,1).
# Finally the function call will be power(2,0) which covers the base case of y==0. Thus the return value will be 1. 
# This will take the place of power(2,0). 
# Now taking all the return values in one equation we will get {2*2*2*1} which is equal to 8.

# Explanation:
# x=2 y=3 if y=0 return 1 x * f(x,y-1) 2 * f(2, 3-1) ( y=2 ) 
# ( x is always 2 ) ( y is returned as 3-1 , ( as 2 ) ) 2 * (2, (2-1)) 
# ( x is always 2 ) ( y is returned as 2-1 , ( as 1 ) ) 2 * 2 * (2,(1-1)) 
# ( x is always 2 ) ( y is returned as 1-1 , ( as 0 ) ) WHEN y = 0(zero) IT RETURNS 1. 2 * 2 * 2 * 1 = 8

# y has nothing to do with returning the value, the y itself act as how many times the recursion would occur.
# In this question: it occured 3 times so: returned_value=x*x*x 8=2*2*2 repeating x are multiplied by only itself with the same value.

# Explanation:
# power(2,3) = 2 * power(2,2) 
# power(2,2) = 2 * power(2,1) 
# power(2,1) = 2* power(2,0) 
# power(2,0) = 1 Now let me do it reversed power(2,0) = 1 => power (2,1) 
# which is 2* power(2,0) = 2*1 
# power(2,1) = 2* power(2,0) = > power (2,2) 
# which is 2 * power(2,1) = 2 * 2*1 = 2*2 = 4 
# power(2,2) = 2 * power(2,1) => power (2,3) 
# which is 2* power(2,2) = 2*4 = 8 
# power(2,3) = 2 * power(2,2) => = 8

# Explanation:
# def power(x, y) x = 2 y = 3 
# the print function is, x * power(x , y-1) therefore, y - 1 = 3 - 1 = 2 
# so here, 2 * power(2,2) but, in power(2,2) = power(x,y) = x*power(x,y-1) therefore, 2 * ( 2 * power( 2, 2-1)) 
# so, 2 * ( 2 * power(2, 1)) therefore, 2 * ( 2 * ( 2 * power(2, 1-1))) 
# so, 2 * ( 2 * ( 2 * power(2,0))) 
# but if as per y == 0, so, power(2,0) = 1, therefore, 2 * ( 2 * ( 2 * 1)) 2 * ( 2 * ( 2)) 2 * ( 4) 8 8 is the output.

# Another Way:
ls=[] 
def func(x,y): 
  if y==0: 
    return 1 
  else: 
    ls.append(y) 
    return x, func(x, y-1)
#
print(func(2,3), ": y =", ls) # (2, (2, (2, 1))) : y = [3, 2, 1]

# x=2,y=3 y==(no equal) 0, therefore, return: x*power(x, y-1)=2*power(2,3-1)=2*power(2,2) hence,power(2,2)=4 so,2*4=8.


# Example 3: to calculate the expression x*(x+1) using an anonymous function and call it for the number 6.
a = (lambda x: x*(x+1))(6)
print(a)  # 42      # code runs: x = 6 x*(x+1) = 6 × (6+1) = 6 × 7 = 42. 
# lamda is a function, so this will make "a" a function. all functions takes arguments inside brackets. 
# a = (x, y) means a is tuple having 2 elements. a = (func(statement))(argument) is the correct form. 
# this is a = functin(argument) structure now.

# lambda is as a function like f(x) in the high math for instance: 
double = (lambda x , x + 2 ) 
# double() is a function double(2) == (lambda x :x + 2 )(2) 
# practice:
# f(x,y) in the math 
f = lambda x,y: (x + 2*y) / (2*x + y) 
f(2,3) == (lambda x,y: (x + 2*y) / (2*x+y))(2,3) 
# the same as put the paremetre in the function is okay f(2,3) == (lambda x,y : (x + 2*y)/(2*x+y),2,3)
  
# a=(lambda x:x*(x+1))(6) print(a) 
# this is same when you have some_word=(func,arg) for the case of variables, 
# the brackets for the function is closed and the argument placed in its own brackets. 
# so for variables it is var=(function())(argument)

# Example 4:

https://www.sololearn.com/learning/1073/2497/5345/2





