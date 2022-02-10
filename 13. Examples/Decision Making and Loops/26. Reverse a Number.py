# Decision Making and Loops Examples
# Example: Reverse a Number

# Example 1: Reverse a Number using a while loop
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))
# Output: 4321

# In this program, while loop is used to reverse a number as given in the following steps:
# First, the remainder of the num divided by 10 is stored in the variable digit. Now, the digit contains the last digit of num, i.e. 4.
# digit is then added to the variable reversed after multiplying it by 10. 
# Multiplication by 10 adds a new place in the reversed number. 
# One-th place multiplied by 10 gives you tenth place, tenth gives you hundredth, and so on. 
# In this case, reversed_num contains 0 * 10 + 4 = 4.
# num is then divided by 10 so that now it only contains the first three digits: 123.
# After second iteration, digit equals 3, reversed equals 4 * 10 + 3 = 43 and num = 12.
# After third iteration, digit equals 2, reversed equals 43 * 10 + 2 = 432 and num = 1.
# After fourth iteration, digit equals 1, reversed equals 432 * 10 + 1 = 4321 and num = 0.
# Now num = 0, so the test expression num != 0 fails and while loop exits. reversed already contains the reversed number 4321.


# Example 2: Using String slicing
num = 123456
print(str(num)[::-1])
# Output: 654321

# Using the string slicing concept, you can get reverse the string. ::-1 corresponds to start:stop:step. 
# When you pass -1 as step, the start point goes to the end and stop at the front.


