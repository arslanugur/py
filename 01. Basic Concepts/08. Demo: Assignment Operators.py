x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6


# Example: difference (subtraction) between the multiplication of the two numbers inputted from the user and the sum of x, y, z? 
a = int(input('1st number: '))
b = int(input('2nd number: '))
result = (a*b) - (x+y+z) # to assign to a variable named 'result'
print(result)


# Example: calculate y without a remainder of x
result = y // x # full division
print(result)

# Example: what is mod 3 of the sum? 
total = (x+ y+ z)
result = total % 3
print(result)


# Example: calculate y to the x'th power 
result = y ** x
print(result)

# x, *y, z = numbers ---> What is the cube of the z value?
numbers = 1, 5, 7, 10, 6   # to assign to the values xyz numbers
x , *y , z = numbers # to assign five elements to three variables
print(y)
result = z ** 3   # the cube of the value 'z'
print(result)


# Example: x, *y, z = numbers --> what is 'the sum of the values of y' according to the operation? 
numbers = 1, 5, 7, 10, 6 
x , *y , z = numbers
result = y[0] + y[1] + y[2]
print(result)


