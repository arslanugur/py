# Example: to define a function that takes two numbers as arguments and returns the smaller one.
def min(x, y):
  if x<=y:
    return x
  else:
    return y
# 


# Example:  to define a function that calculates the sum of all numbers from 0 to its argument.
def sum(x): 
  res = 0 
  for i in range(x):
    res += i
  return res 

print(sum(10))  # 45


# Example:
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))  # 6
# here's how this works: 
# func(4) sets the range in the for loop to range(4)={0,1,2,3} res is set to 0 for loop starts i=0 so res+=i is 0 
# and the new res value next i=1 so res+=i is 1 and the new res value next i=2 so res+=i is 3 
# and the new res value last i=3 so res+=i is 6 and the new res value the loop now exits (the indented code is the loop code) 
# the function func(4) now returns the last calculated res value, which is 6 
# so print(func(4)) prints the value returned by the function which is the res value of 6.

# At every increment from 0-3(range 4) there is an addition of the sum of the increment. 
# loop=1: res=0 res=0+1 res=1 loop=2 res=1 res=1+2 res=3 loop=3 res=3 res=3+3 res=6 The answer is: 6.
    
# even I was confused, res=0 res+=i means,res=res+i question is of 4 so that means four steps, let i be 0,and res be 0
# then, res=0+0 =0 let i be 1,and res be 0(from the answer obtained) 
# then, res=0+1 =1 let i be 2,and res be 1(from the answer obtained)
# then, res=1+2 =3 let i be 3,and res be 3(from the answer obtained) 
# then, res=3+3 =6 therefore,the answer is 6.




# How would you refer to the randint function if it was imported like this?
from random import randint as rnd_int
# Answer: rnd_int

# Example: What is the highest number output by this code?
def print_nums(x):
  for i in range(x):
    print(i)
  return      # if return is deleted from code  # output: 0 1 2 3 4 5 6 7 8 9 

print_nums(10)  # 0

# As we learned in this module, return is a construction used in the code block of a function definition
# after the return instruction is inserted the code block will stop executing anything so: 

# Program takes 0, verifies that is in range of 10 and prints 0 
# Because of the return statement program stops executing the code 

# res += i is the same as: res = res + i 
# So we have res = 0 to start with and it goes within the loop. 
# If we are printing the value 4 of the range it means there are 4 steps. 
# So it starts: 
# first loop: res = 0 (the value os res) + 0 (value of i) 
# second loop: res = 0 (current value of res) + 1 (value of i on the second loop) 
# third loop: res = 1 (current value of res) + 2 (value of i on the third loop) 
# forth and final loop: res = 3 (current value of res) + 3 (value of i on the last loop since python counts from 0) 
# so in the end res = 6. the confusion might be in the res = 0 since it is in the function. 
# but remember, it is not inside the loop...so it doesn't go back to 0 on each loop. 



