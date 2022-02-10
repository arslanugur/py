# Introduction Examples
# Solve Quadratic Equation
# This program computes roots of a quadratic equation when coefficients a, b and c are known. 

# The standard form of a quadratic equation is:

# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0

# The solutions of this quadratic equation is given by:
# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)



# Source Code
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

d = (b**2) - (4*a*c)  # calculate the discriminant

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

# Output:
# Enter a: 1
# Enter b: 5
# Enter c: 6
# The solutions are (-3+0j) and (-2+0j)

# We have imported the cmath module to perform complex square root. 
# First, we calculate the discriminant and then find the two solutions of the quadratic equation.

# You can change the value of a, b and c in the above program and test this program.



