# SECTION 1
# Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.
# Example:
numbers = (1, 2, 3)
a, b, c = numbers
print(a)  # 1
print(b)  # 2
print(c)  # 3

# This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side forms the tuple (b, a) which is then unpacked.

# Example:
numbers = (1, 2, 3) 
a, b, c = numbers 
print(a)    # 1
print(b)    # 2
print(c)    # 3
a, b = b, a 
print(a)    # 2
print(b)    # 1
print(c)    # 3

# In other languages, 
# you'd have to do this: temp = a a = b b = temp 
# In Python, you do this: a, b = b, a

# Fibonacci can be done like for i in range (n): a,b = b,a+b
# You can make Fibonacci in only 4 lines of code, with even variables initialization. 
a, b, n = 0, 1, int(input("Fibonacci: ")) 
for i in range (n): 
  print(b) 
  a, b = b, a+b # Of course in this is ultra compact way you don't have a control over the input.
# The shortest Fibonacci's series calculator I could make without external libraries.
# Only 4 rows; since it's ultra compact it doesn't have controls of some sort.
# Example:
a, b, n = 0, 1, int(input("How many numbers?\n"))
for i in range (n):
    print(a)
    a, b = b, a+b
#

# If the number of strings does not tally in the two field, it throws up an interesting error 
numbers = (1, 2, 3, 4) 
a, b, c, d, e = numbers 
print(a) 
print(b) 
print(c) 
print(d) 
print(e)  # output Traceback (most recent call last): File "..\Playground\", 
          # line 2, in <module> a, b, c, d, e = numbers ValueError: not enough values to unpack (expected 5, got 4) 

numbers = (1, 2, 3, 4, 5) 
a, b, c, d = numbers 
print(a) 
print(b) 
print(c) 
print(d) # Output Traceback (most recent call last): File "..\Playground\", line 2, in <module> a, b, c, d = numbers ValueError: too many values to unpack (expected 4)

# Example:
numbers = (1, 2, 3) a, b, c = numbers print(a) print(b) print(c) a, b, c = (7, 8, 9) print(a) print(b) print(c) OUTPUT: >>> 1 2 3 7 8 9
  
# If you have Tuple with more element then you need use this method: numbers = (1, 2, 3, 4) a, b, c= numbers[:3] print(a, b, c)



https://www.sololearn.com/learning/1073/2485/5193/2
  
