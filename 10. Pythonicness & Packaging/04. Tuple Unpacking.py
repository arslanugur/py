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
print(d) # Output: Traceback (most recent call last): File "..\Playground\", line 2, in <module> a, b, c, d = numbers 
         #         ValueError: too many values to unpack (expected 4)

# Example:
numbers = (1, 2, 3) a, b, c = numbers print(a) print(b) print(c) a, b, c = (7, 8, 9) print(a) print(b) print(c) # OUTPUT: >>> 1 2 3 7 8 9
  
# If you have Tuple with more element then you need use this method: numbers = (1, 2, 3, 4) a, b, c= numbers[:3] print(a, b, c)



# What is the value of y after this code runs?
x, y = [1,2]
x,y = y,x     # 1  

# x, y = [1,2] x=1, y=2 However x,y = y,x Thus, 1,2 = 2,1 Therefore the first line x,y = 2,1 y = 1
# We are in the second line implicitly. The list in the first line is just to initialize the variables, but a tuple would work there too.

# [1,2] is reversed to [2,1] so afer that, [x,y] = [2,1] so, y = 1

# a,b = [1,2] as a = b = [1,2], a,b = [1,2] assigns the elements of the array to each variable a=1, b=2, 
# and a = b = [1,2] assigns the same array [1,2] to the variables a and b a, b = [1,2] print (a,b) 
# output a=1 and b=2 c = d = [1, 2] print (c,d) #output a=[1,2] and b=[1,2]

# Example:
numbers = (1, 2) #tuple unpacking concept
a, b = numbers
print("before swapping a is",a)
print("before swapingng b is",b)
a,b = b,a
print ("after swapping a is",a)
print ("after swapping b is",b)


# SECTION 2:
# A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables.
# Example:
a,b,*c,d = [1,2,3,4,5,6,7,8,9]
print(a)    # 1
print(b)    # 2
print(c)    # [3, 4, 5, 6, 7, 8]
print(d)    # 9
# a ---> 1 (a is 1st, 1 is 1st) b ---> 2 (b is 2ns, 2 is 2nd) d ---> 9 (d is last, 9 is also last) so what's left... *c ---> 3,4,5,6,7,8 


# Example:
a, b, *c, d = [1, 2, 3] 
print(a) 
print(b) 
print(c) 
print(d) # output: 1 2 [] 3

# Having more than one "*" would throw an error. Try this: *a, *b, c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9] print(a) print(b) print(c) print(d)

# https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators 
# especially the last chapter: Unpacking With the Asterisk Operators: * & **

# Example:
[*a] = 'Big in Japan'  # list
print(a)
[*a,] = 'Big in Japan' # list
print(a)
(*a,) = 'Big in Japan' # tuple
print(a)
(*a), = 'Big in Japan' # tuple
print(a)
*a, = 'Big in Japan'   # tuple 🔴🔵
print(a, '🔴🔵')

print(*a)           # unpack
print(''.join(a))

t = 'B','i','g','i','n','j','a','p','a','n'
print(t)


# Example:
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
type(a) # int --> same as b and d 
type(c) # list 


a,b,c,d,*e,f,g=range(20) a,b,c,d=1,2,3,4 f,g=19,20 so, e is 5-18 Len(e)=13

# More on function arguments and tuple unpacking together def func(*args): 
# function that return sum of arbitrary number of arguments return sum(args) 
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(func(*c)) # list c in function call is unpacked with *. >>>33 
# Actually this can be done in other way without *args but in that case, we have one argument in function, which is LIST 'c', 
# but, above we had 6 arguments (from list c, unpacked from it) def func(args): return sum(args) 
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(func(c))

print(func(a, b, *c, d))  

# If you add, e.g. 10 at the end, like: 
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(a) 
print(b) 
print(c) 
print(d) # Result is: 1 2 [3, 4, 5, 6, 7, 8, 9] 10


# Example:
a,b,b,d,*e,f,g = range(20)
print(len(e)) # 14

# Explanation:
a=0 b=1 c=2 d=3 e=[4,5,6,7,8,9,10,11,12,13,14,15,16,17] f=18 g=19 So len(e) = 14
# 20 - 6 = 14. # of values in range - # of variables taken = # of variables left over. *e takes left over values.
# range starts at 0, but the length count starts at 1


# Example: The values after processing this command is 
a=0 
b=1 
c=2
d=3 
e=[4,5,6,7,8,9,10,11,12,13,14,15,16,17]
f=18 
g=19
# But it's a long way to find the answer. One of the shorter way is: len(abcdfg)=6 and len (range(20) )=20. len(e)=20-6.

# Explanation:
# We can also count and do like it 
a,b,c,d,*e,f,g=range(20) print(len(*e)) a+b+c+d+f+g=total elements=>6 range => 20 left Elements len=>range-elements elements left length=>20-6=>14

# counted 14, which is correct per question/answer. Not sure of the logic but this is how I got it. From the discussion, 1 letter is not counted. 
# So in the question this question with 7 letters, only 6 are used 20-6=14
# 6 letters will grab one number each. The e will grab the rest in between!


# (1): range(20) really refers to the following bunch of numbers. 0, 1, 2, 3, 4, 5, ..., 16, 17, 18, 19 a, b, c, d, *e, f, g = range(20) 
# therefore means that we allocate the variables a, b, c, d, e, f and g to all the numbers above coming from range(20) as follows. 
# a = [0] b = [1] c = [2] d = [3] e= [4, ... ] 
# Now, let's run through through the variables from RIGHT TO LEFT, 
# so direction, until we get to the e-variable once again, allocating them once by one just like above. 
# (As they mentioned before in the lesson, sth like, 
# the "leftovers" of the iterable (the range(20) object HERE) get allocated to the variable 
# that's been prefaced with an asterisk ✴ (the e-variable HERE) right AFTER all other variables get allocated to their respective iterable values 
# (what values of the iterable the other variables are MEANT to be allocated))
# (2): g = [19] f = [18] e = [..., 17] COMBINING BOTH of what we said above for the e-variable, namely e = [4, ...] AND e = [..., 17] 
# it's clear that e-variable gets allocated to the list of numbers running from 4 to 17 INCLUSIVE. 
# Hence, e = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# (3): Finally, to answer the actual question we've got, 
# we just need to determine HOW MANY numbers in TOTAL such a list allocated to the e-variable contains. 
# How to count how many numbers are contained in the list allocated to the e-variable? 
# Of course, you could count em all up, but what if you had MANY numbers? 
# Then, it would be ridiculous, tedious and hellish to count em all up. 
# Range(20) had 20 characters, running up to 19 for 0, 19-0=19≠20❌, so try to add 1, so (19-0)+1=19+1=20=20✅. 
# So, generally speaking, to find HOW MANY numbers exist between any 2 given numbers, say x and y where y>x (y is greater than x), you just do (y-x)+1. 
# Now, consider once again the list of numbers allocated to the e-variable. 
# This list ran up to 17 from 4. (17-4)+1=13+1=14, so a TOTAL of 14 numbers are contained by the list allocated to the e-variable, 
# which in turn is equal to the length of such a list...

# just remember *=leftover when tuple unpacking. Thus 20-6[other variables]=14 left unassigned and * takes them

# range(20) [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19] *e start from 4 to 17,f=18,g=19 
# therefore: length of (*e) will be from 4 to 17 which equals 14 numbers. 
  
# a through d =4 f through g= 2 total length=20 20-4-2=14



