# If a, b and c are three sides of a triangle. Then,
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))


# Source Code
# Python Program to find the area of triangle
a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)    # Output: The area of the triangle is 14.70

# In this program, area of the triangle is calculated when three sides are given using Heron's formula.
# If you need to calculate area of a triangle depending upon the input from the user, input() function can be used.

