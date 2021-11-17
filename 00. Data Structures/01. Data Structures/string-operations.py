# String Operations

# The in operator can be used to check if a string is part of another string.

# For example:
x = "Asimovs Laws are fictional, but they inspire real-world engineers to create the first truly helpful robot."
if "robot" in x:
   print("Yes")
# output: Yes

# The not in operator can be used to check if a string is not part of another string.


# What is the output of this code?
res = 0
s = 'xyz'
if 'x' in s:
   res += 1
elif 'a' in s:
   res += 1
print(res)
# output: 1


# Concatenation - Strings can be added together:
print("A" + 'I')    # output: AI

# Strings can also be multiplied by integers. This produces a repeated version of the original string.
print("go" * 3) # output: gogogo
print(4 * '3')    # output: 3333

# Strings can't be multiplied by other strings. Strings also can't be multiplied by floats, even if the floats are whole numbers.


# Guess the output:
a = "abra"
b = "cad"
x = a + b + a
print(x)           # output: abracadabra
