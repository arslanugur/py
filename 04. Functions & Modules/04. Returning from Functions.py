# Certain functions, such as int or str, return a value that can be used later.
# To do this for your defined functions, you can use the return statement.
print(max(1,2,3,4,5))  # 5
# For example:
def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))  # 7
z = max(8, 5)
print(z)          # 8

# The return statement cannot be used outside of a function definition.



# Example:
def func(z): 
  x = z/2 
  y = z*2 
  return [x,y] # return x and y in a array 
  
var = func(10)  #var = [x,y] 
print(var[0])   # 5.0
print(var[1])   # 20


# Example:
def divisible(x,y): 
    if x % y == 0: 
        print(x / y) 
    elif y % x == 0: 
        print(y / x) 
    else: 
        print(str(x) + " and " + str(y) + " are not divisible by each other.") 

divisible(10,2) # 5.0
divisible(2,10) # 5.0
divisible(3,7)  # 3 and 7 are not divisible by each other.



# Example: to define a function that compares the lengths of its arguments and returns the shortest one.
def shortest_string(x, y):
  if len(x) <= len(y):
    return x
  else:
    return y
  
print(shortest_string("Superman","Batman"))


# Once you return a value from a function, it immediately stops being executed. 
# Any code after the return statement will never happen.
# Example:
def add_numbers(x, y):  # to define a function that contains two arguments x and y
    total = x + y       # we add those two arguments to each other 
    return total        # we return there total to the next step in the main code, not in this function. As we need no more from it now, since we reached the "return" point
    print("This won't be printed") # the Fourth line in nonsense

print(add_numbers(4, 5))  # the fifth line,which is in the main code outside the function defined,will be executed, so the defined function will be printed as 9



# Example:
# First Case:
def sum(x,y):
    return x+y

sum(4,5)* 2 # 18

# Second Case:
def sum(x,y): 
    print(x+y)

sum(4,5)* 2 # ERROR 
# because when we use (print), we can only display things. 
# but when we use (return), we can either display and sum
# you can't do operations on: print()



# Example:
def max(x, y): 
    if x >=y: 
        return x 
    else: 
        return y 

x = int (input("Enter the first value: ")) 
y = int (input("Enter the second value: "))

print('The greater value between ', x , ' and ', y ,' is ', max(x, y)) 


  
# Example:
def maxmin(a, b): 
    if a > b: 
        return a, b 
    else: 
        return b, a 

more, less = maxmin(5,6) 
print(more) # 6 
print(less) # 5 
data = maxmin(5,6) 
print(data) # (6,5) 



# Example:
#if you want to return more than one value, and play with the values 
def add_substract(x, y): 
    add = x + y 
    substract = x - y 
    return add,substract,5,"word" 
    print("This won't be printed") 

x = add_substract(2,8) # thus creates a list x 
print(x[1]) # -6 --> printing the second element from the list 
print((add_substract(6,3)[3])) # word --> printing something directly from the returned list 

if add_substract(9,8)[1] < 0: 
    print("y is greater than x") 
else: 
    print("x is greater or equal with y")   # x is greater or equal with y
#


# Example: What is the highest number this function prints if called?
def print_numbers():
  print(1)
  print(2)
  return
  print(4)
  print(6)  # 2
#

  
# Example:
def bmi_calc(weight = float(input("Enter weight in pounds: ")), height = float(input("\nEnter height in inches: "))): 
    bmi = weight * 703 / height ** 2 
    if bmi <= 18.5: 
        print("\nUnderweight") 
    elif bmi <= 24.9: 
        print("\nNormal Weight") 
    elif bmi <= 29.9: 
        print("\nOverweight") 
    else: 
        print("\nObese") 
        
        return "\nYour BMI is " + str(bmi) 
        
print(bmi_calc())


