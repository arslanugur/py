# Regular Expressions Example: Phone Number Validator
"""
You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9. 
Output "Valid" if the number is valid and "Invalid", if it is not. 

Sample Input        81239870          81234567        57345672
Sample Output       Valid             Valid           Invalid

Note: You can use a regular expression to check if the input matches the given pattern.
"""

# Problem Solve:
import re

number = input()

check = r"[189][0-9]{7,7}$"

valid = re.search (check,number)

if valid:
    print ("Valid")
else:
    print ("Invalid")
#    


# Second Way
import re
#phone number validator in two ways
a = input()

start=r"^[189]"

if re.match(start,a) and len(a) ==8:
	print("Valid")
else:
	print("Invalid")
#	

  
# Third Way: Without regex
a = input()
num = 0
v = 0
if len(a) ==8:
	num = 1
	
if a[0] in "189":
	v = 1
	
if num > 0 and v > 0:
	print("Valid")
else:
	print("Invalid")
#


# Fourth Way:
import re

innum = input()
def isInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False


def count_number(number):
	counter = 0
	counter_number = number
	while counter_number > 0:
		counter_number //= 10
		counter += 1
	return counter


def digit_selector(number, selected_digit, total):
	total_counter = total
	calculated_select = total_counter - selected_digit
	number_selected = int(number / (10**calculated_select))
	while number_selected > 10:
		number_selected -= 10
	return number_selected


def main():
	if isInt(innum) is True:
		x = int(innum)
		total_digits = count_number(x)
		digit_1 = digit_selector(x, 1, total_digits)
		if len(innum) == 8:
			if digit_1 == 1 or digit_1 == 8 or digit_1 == 9:
				print('Valid')
			else:
				print('Invalid')	
		else:
			print('Invalid')
	else:
		print('Invalid')


if __name__ == '__main__':
	main()
#



