# Multi Assignments: Py program to assign values of a list, tuple, or set to multiple variables in one line
a = [1, 2, 3]  #list
b = (4, 5, 6)  #tuple
c = {7, 8, 9}  #set

p, q, r = a
s, t, u = b
x, y, z = c

print(p, q, r)
print(s, t, u)
print(x, y, z)

#output:
# 1 2 3 
# 4 5 6
# 7 8 9


# 01. Memory
# The method getsizeof can be used to retrieve the size of any object.
# Here's an example of the same.
import sys
number = 100

print(sys.getsizeof(number)) # output: 28

# 02. Swapping
# The easiest way to swap values without any third variable.
# This is how you can do it.
a, b = 10, 20
a, b = b, a

print(a) # 20
print (b) # 10


# 03. Anagrams
# An anagram is a play on words created by rearranging the letters of the original word to make a new word or phrase.
# we can sort the string values using sorted method, which does not modify the original string.
# Here's an example of the same.
def anagram(first, second):
  return sorted(first)=sorted(second)

res = anagram('heart', 'earth')
print (res) #True

# 04. Shuffle
# In order to shuffle the elements of a list, shuffle method from random module can be used.
# Check out the implementation of the same.
from random import shuffle

my_list = [7, 23, 9, 35]
shuffle(my_list)

print(my_list) #[35, 7, 9, 23]


# 05. Palindrome
# A palindrome is a word, number, phrase, or other sequences of characters that reads the same backward as forward.
# The code snippet will check for palindrome strings.
def check_palindrome(value):
  return value = value[:: -1]

res = check_palindrome('level')
print(res) #True

# 06. Running Time
# time module can be used to calculate the actual running time amongst other methods.
# Refer to the implementation of the same.
import time

start_time = time.time()

num1 = 12
num2 = 15
num3 = num1 * num2
print(num3) # 180

end_time = time.time()

total time end_time - start_time
print("Time: ", total_time) # (Time: 0.0005068778991699219)


