# Assignment Operators
x = 5
y = 10
z = 20  # variable = value

# Second Way
x, y, z = 10, 40, 30 

# what if we change the values
x, y = y, x # bu şekilde değişir

# Explain:
x = x + 20 # assign a new value or x += 5 
z -= 3
y *= 2
x /= 2
z %= 2 
y //= 3 # full division
y **= 5 # exponentiation
z *= x  # multiply z and x and reflect to z
print(x, y, z)

# Explain:
# how to use assignment operators on the list
values = 1, 2, 3 # tuple list example

x, y, z = values # the values in the tuple will transfer to xyz tuple
print(x, y, z)   
# prints 123 but if we delete one of values, it would be error
# two elements in a list cannot transfer into three values, it would be error ---> not enough
# if there is an extra elemednt in the list 'values', it would be error ---> too many

# but if we add an asterisk at the beginning of one of the variables, it goes to that variable as an array. 
values = 1, 2, 3, 4, 5 

x, *y, z = values 
print(x, y, z) 

# creates a list for 'z'
# print(x, y, z[0]) --> prints only 3

# Explain:
print(values)
print(type(values)) # prints type -->  class 'tuple'



