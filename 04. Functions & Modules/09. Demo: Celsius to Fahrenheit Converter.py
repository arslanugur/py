# To make a Celsius to Fahrenheit converter. 
# Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

# Sample Input: 0
# Sample Output: 32.0

# Sample Input: 18
# Sample Output: 64.4

# Sample Input: 36
# Sample Output: 96.8

# Note: The following equation is used to calculate the Fahrenheit value: 9/5 * celsius + 32

# Code:
celsius = int(input())

def conv(c):
	 f = 9/5 * c + 32
	 return f

fahrenheit = conv(celsius)
print(fahrenheit)


