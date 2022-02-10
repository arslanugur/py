# Decision Making and Loops Examples
# Example: Compute the Power of a Number

# Example 1: Calculate power of a number using a while loop
base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))
# Output: Answer = 81

# In this program, base and exponent are assigned values 3 and 4 respectively.
# Using the while loop, we keep on multiplying the result by base until the exponent becomes zero.
# In this case, we multiply result by base 4 times in total, so result = 1 * 3 * 3 * 3 * 3 = 81.


# Example 2: Calculate power of a number using a for loop
base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))
# Output: Answer = 81

# Here, instead of using a while loop, we've used a for loop.
# After each iteration, the exponent is decremented by 1, and the result is multiplied by the base exponent number of times.
# Both programs above do not work if you have a negative exponent. For that, you need to use the pow() function in the Python library.


# Example 3: Calculate the power of a number using pow() function
base = 3
exponent = -4

result = pow(base, exponent)

print("Answer = " + str(result))
# Output: Answer = 0.012345679012345678

# pow() accepts two arguments: base and exponent. In the above example, 3 raised to the power -4 is calculated using pow().



