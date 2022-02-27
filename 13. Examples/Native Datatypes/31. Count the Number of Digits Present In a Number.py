# Native Datatypes Examples
# Example: to Count the Number of Digits Present In a Number

# Example 1: Count Number of Digits in an Integer using while loop
num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))      # Number of digits: 4

# In this program, the while loop is iterated until the test expression num != 0 is evaluated to 0 (false).
#     After the first iteration, num will be divided by 10 and its value will be 345. Then, the count is incremented to 1.
#     After the second iteration, the value of num will be 34 and the count is incremented to 2.
#     After the third iteration, the value of num will be 3 and the count is incremented to 3.
#     After the fourth iteration, the value of num will be 0 and the count is incremented to 4.
#     Then the test expression is evaluated to false and the loop terminates.

# Example 2: Using inbuilt methods
num = 123456
print(len(str(num)))    # 6

# In the above example, we first convert the integer value into string by using str(). Then, we find the length of the string using len().



