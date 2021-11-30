# FizzBuzz is a well known programming assignment, asked during interviews.

# The given code solves the FizzBuzz problem and uses the words "Fizz" and "Buzz".
# It takes an input n and outputs the numbers from 1 to n.
# For each multiple of 3, print "Fizz" instead of the number.
# For each multiple of 5, prints "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, output "FizzBuzz".

# You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range.
# Remember, the continue statement can be used to skip a loop iteration.

n = int(input())

for x in range(1, n):
	if x % 2 == 0:  # Skip the even numbers
		continue      # Skip loop iteration
	elif x % 3 == 0 and x % 5 == 0:
		print("FizzBuzz")
	elif x % 3 == 0:
		print("Fizz")
	elif x % 5 == 0:
		print("Buzz")
	else:
		print(x)
    
# output:
# input: 15
# 1
# Fizz
# Buzz
# 7
# Fuzz
# 11
# 13

