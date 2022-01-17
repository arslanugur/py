# SECTION 1
# So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
# String formatting provides a more powerful way to embed non-strings within strings. 
# String formatting uses a string's format method to substitute a number of arguments in the string.
# Example:
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
# Numbers: 4 5 6

# Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.

# Example:
# Numbers inside curly brackets{} are simply indexes of elements inside .format() bracket. 
msg = "Numbers: {0} {1} {3}".format(4,8,3,6) 
print(msg)  # Numbers: 4 8 6


# A couple of things to note: 
# You don't always need numbers in the curly brackets. 
# If you leave them blank, the format items listed are inserted in order, 
# Example:
nums = [4, 5, 6] 
msg = "Numbers: {} {} {}".format(nums[0], nums[1], nums[2])
print(msg) # Numbers: 4 5 6 
# You can use them to change the order of insertion, 
# Example:
nums = [4, 5, 6] 
msg = "Numbers: {2} {0} {0}".format(nums[0], nums[1], nums[2])
print(msg) # Numbers: 6 4 4 2
# Although nums are integers, when they are inserted into a string with format, they are no longer integers, 
# Example:
nums = [4, 5, 6] 
msg = "Numbers: {} {} {}".format(nums[0], nums[1], nums[2])
print(msg)
print(msg[0])
print(msg[9])
print(msg[11])
print(msg[9] + msg[11])
print(int(msg[9]) + int(msg[11]) 
# Numbers: 4 5 6, N, 4, 5, 45, 9
#

# Basically, in "Numbers: {0} {1}".format(nums[0], nums[1]), the nums[0] represents numbers in the list, so for you can replace with, 
# for example, "Numbers: {0} {1}".format(6, 7). This would lead to Numbers: 6 7. 
# The numbers in the curly braces represent the order in the format method. 
# So its "format([position 0], [position 1]) that correspond to the numbers in the curly braces: {0} {1} 
# Btw, you can use strings in the format method, too


# Another one variant of str.format: print("MyFourLetters: {0[3]}{0[0]}{1[2]}{1[1]}!".format("Abcd","cat")) and result is: MyFourLetters:dAta!
# More useful variant: a='Zero'; b='One'; c="Danger "; print("{2}{0[0]}{0[3]}{1[1]}{1[2]}".format(a,b,c)) #Outputs: Danger Zone
      


      
      
