# list = [ ]
# dict = { }
# tp = ( )               a tuple can be sliced

# THE RULES OF SLICING
# List Slicing --> [start:stop:increment/decrement]
#                  [start: end: stepsize]
#        print(list[start:stop:step]) 
#        1. If (start<=stop and step is negative, in result is[] . 
#        2. If (start>=stop and step is positive, in result is []. 

# List slices provide a more advanced way of retrieving values from a list. 
# Basic list slicing involves indexing a list with two colon-separated integers. 
# This returns a new list containing all the values in the old list between the indices.
# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])       # [4, 9, 16, 25]
print(squares[3:8])       # [9, 16, 25, 36, 49]
print(squares[0:1])       # [0]

# Like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.


# Tip: To reverse the whole list use mylist[::-1] 
# Example:
mylist = [1, 2, 3, 4]
print(mylist[::-1])   # [4, 3, 2, 1] 
# The slicing of a list takes three arguments separated by colon. they are optional. 
# lower limit:upper limit: steps by default (if you don't specify) 
# lower limit is at index 0, upper limit is at the last value and steps is +1 
# so using ::-1 as in the example means don't slice anything off but give in reverse order. 


# STRINGS are essentially LISTS (or TUPLES to be more precise) in Python.
strn = "There can be only one"  # input 
print(strn[::-1])               # output: eno ylno eb nac erehT


# A nice little trick for dealing with ranges that are inclusive of the first value 
# but exclusive of last is to do the last minus the initial to know how many elements are in the range. 
# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])       # [4, 9, 16, 25]           6 - 2 = 4 
print(squares[3:8])       # [9, 16, 25, 36, 49]      8 - 3 = 5 
print(squares[0:1])       # [0]                      1 - 0 = 1 
# When you print the range you end up with [4, 9, 16, 25] which is 4 elements, [9, 16, 25, 36, 49] is 5 and [0] is 1. 
# This is a nice little trick when you're trying to trace code and figure out the output or something.



# Worth adding here as a reminder is that when you create a list and assign it to a variable, 
# you have to think of this variable as POINTING to the list rather than being EQUAL to it. 
# Whenever you assign another variable to the one you already have assigned the list, both variables point to THE SAME list object. 
# Any list modifications will affect ALL variables pointing to it. 
# Example: 
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
quadras = squares 
squares[9] = 100 
print(quadras) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 100]



# Example: List Slicing
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[2:6])           # [4, 9, 16, 25] 
print(squares[3:8])           # [9, 16, 25, 36, 49] 
print(squares[0:1])           # [0]
print(squares[::-1])          # [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
print(squares[::2])           # [0, 4, 16, 36, 64]  
print(squares[::-2])          # [81, 49, 25, 9, 1]
print(squares[3:9:2])         # [9, 25, 49]
print(squares[7:1:-1])        # [49, 36, 25, 16, 9, 4]
print(squares[1:8:3])         # [1, 16, 49] 





# Example:
my_list = [0, 1, 2, "skip", 6, 7, 8, 9] 
# you want to fill in the missing numbers in the sequence. 
# Your first attempt might be:
my_list[3] = [3, 4, 5] 
# But this would make the value of my_list be [0, 1, 2, [3, 4, 5], 6, 7, 8, 9], and that list in the middle of a list would cause problems. 
# But using the following list slice: my_list[3:4] = [3, 4, 5] 
# Now the value of my list is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], which is what we originally wanted! 
# you could use list slices that way at the following website:
# http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html


# You can also pass a value to a variable and then use that variable for list slicing. 
# Example: 
list = ["a","b","c"]
d = 0
e = 2
list_new = list[d:e]
print(list_new) # ['a', 'b']


# Example:
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])         # [16, 25, 36]


# Sample:
x = first index 
y = second index
print(list[x:y])  # prints from index x to index y - 1



# If the first number in a slice is omitted, it is taken to be the start of the list.
# If the second number is omitted, it is taken to be the end.
# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])     # [0, 1, 4, 9, 16, 25, 36]
print(squares[7:])     # [49, 64, 81]
# Slicing can also be done on tuples.

# Notice the colon before and after the 7 
# Before - means count all before 7 
# After - means count all after 7


# If you use any number biggger than last key, still the result is same
print(squares[7:100]) # [49,64,81]
print(squares[7:])    # [49,64,81]
# Also negatives work just fine till the second key dosn't cross the first key to the left: 
print(squares[7:-1])  # [49,64]
print(squares[7:-5])  # []



# Examples: Clone Arrays with [:]
    # A safe way to clone two arrays.
    # I know a method exists but this seems
    # like a shorter way.

arr_a = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
arr_b = arr_a

print("Before Change:")
print(arr_a)
print(arr_b)

print("\nAfter arr_b[0] is assigned to 2:")
arr_b[0] = 2
print("arr_a: %s" % arr_a)
print("arr_b: %s" % arr_b)
print("# Both are changed.")

print("\nA safe way to clone array using [:]:")
arr_b = arr_a[:]
print("arr_b = arr_a[:]: %s" % arr_b)
arr_b[1] = 2
print("arr_b[1] = 2: %s" % arr_b)
print("arr_a is not affected: %s" % arr_a)


# Example: To take the first two elements of the list:
list = ["a", "b", "c", "d"]
a = list[0:2]         # [:2]  # slices don't display the last number. [0:1] will display a only. [0:2] will display a,b
                              # [0:2] means [first index: last index -1] and we get 0,1 if we need "abc" then list[0:3] = 0,1,2
                              # it's 0:2 Because the CUT its before to the two
                              # for example, you need the first 2 elements and
                              # You have list = ["0", "1", "2", "3"] list[0:2] list = [/"0", "1", /"2", "3"] / Its the cut
#


# List slices can also have a third number, representing the step, to include only alternate values in the slice. 
# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])         # [0, 4, 16, 36, 64]
print(squares[2:8:3])       # [4, 25]
# [2:8:3] will include elements starting from the 2nd index up to the 8th with a step of 3.




# The structure is: print(squares[start, stop, step]) 
# Example:
# squares = [1, 3, 4, 7, 9, 2, 5, 11, 12] 
# The index of the first element in an array is 0 and the index of the last element is numberOfElementsIntheArray-1. 
# In our case, 1 has the index 0, and 12 has the index 8. 
# The first element in our array is 1. 
# 1 -> index = 0 
# 2 -> index = 5 
# 3 -> index = 1
# 4 -> index = 2 
# 5 -> index = 6 
# 7 -> index = 3
# 9 -> index = 4
# 11 -> index = 7
# 12 -> index = 8  
# print(squares[2:6:2]) 
# start : 2 ; stop : 6 ; step : 2 output:[4, 9] 
# Steps: 
# 1) 1st element is 4 ( index = 2 ) 
# 2) 2nd element is 9 ( index = 4 -> 2(index of the last element)+2(step)=4 ) 
# 3) the next element should have the index 6 ( index = 6 -> 4+2=6 ), but the last possible element is the element with the index = stop-1. 
# In our case stop is 6, so the last possible element should have the index 5. 
# It's like in math...an interval [2,6), but we talk about indexes. 6 not∈ [2,6) 
# Another example: print(squares[2:8:1] output : [4, 7, 9, 2, 5, 11]


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[2:8:3])
print(squares[2:8])   # Firstly print(squares[2:8]) gives output (4,9,16,25,36,49)
                      # Then (:3) means (+3rd) elements in result starting from first i.e.(4,25).. 
                      # Similarly [2:8:2] will give output (4,16,36){(+2nd) elements in result,starting from first}

# print(squares[2:8:3]) - 2 is the starting point,8 is the ending point,3 means that every third element from the first before ,so first,2 squares =4(first one),
# then select the third element from the 2(which is 5 (2+3)) , 5 squares is 25, 
# and now we cant get anymore (because 5+3=8(which is the ending point) and the final output will be [4,25]


# Example:
list = [ "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten" ] 
print(list[::1])          # [ "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten" ] 
print(list[::2])          # [ "One", "Three", "Five", "Seven", "Nine" ]
print(list[::3])          # [ "One", "Four", "Seven", "Ten" ]
# formula: index = element_index + step example: list[ : 10 : 3 ] start = 0 finish = 10 step = 3 index = 0 + 3 = 3 index = 3 + 3 = 6 index = 6 + 3 = 9

# It will take steps wherever it can, by the multiple of the step number. 
# For example: 
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[0:10:2])    # [0, 4, 16, 36, 64] 
# This will print from the first number to the last number but "steps over" every second number (the step number is 2) 
# It won't print 81 because it isn't a multiple of 2 in the list index (it's 9). It also won't print the 10th number because it doesn't exist.

# You can also take a step to backward 
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(sqs[7:1:-2]) # [49, 25, 9]



# Example:
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])                          # [1, 25, 81]


# [begining :last :interval] 
# where 
# -'begining' is the first value we take 
# -'last' is the last value which is not included 
# -'interval' is a number that will send back,from begining to last, every value in its interval. 
# Example: 
list = [0,1,2,3,4,5,6] 
print(list[::2]) # prints every 2 values


# Example:
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(sqs[1::4]) 
# In this question [ start : stop : jump ] 
# sqs[ 1 : : 4 ] means as per index it starts - index[1] = 1 jump(4) - index[5] = 25 jump(4) - index[9] = 81


# SECTION: NEGATIVE SLICE
# Negative values can be used in list slicing (and normal list indexing). 
# When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list. 
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])                            # [1, 4, 9, 16, 25, 36, 49, 64]

# If a negative value is used for the step, the slice is done backwards.
# Using [::-1] as a slice is a common and idiomatic way to reverse a list.

# Worth noting is that STRINGS are esentially LISTS in Python, so: 
# Example: 
strn = "There can be only one"
print (strn[::-1])  # output: eno ylno eb nac erehT

# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[1:-1])                            # [1, 4, 9, 16, 25, 36, 49, 64]
print(squares[1:-2])                            # [1, 4, 9, 16, 25, 36, 49]
print(squares[1:-3])                            # [1, 4, 9, 16, 25, 36]
print(squares[1:-4])                            # [1, 4, 9, 16, 25]
print(squares[1:-5])                            # [1, 4, 9, 16]


# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[:])   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[:2])  # [0, 1] 
print(squares[:3])  # [0, 1, 4] 
print(squares[:-1]) # [0, 1, 4, 9, 16, 25, 36, 49, 64] 
print(squares[:-2]) # [0, 1, 4, 9, 16, 25, 36, 49] 
print(squares[:-3]) # [0, 1, 4, 9, 16, 25, 36] 


# Example:
list = [0,1,2,3,4,5,6,7,8,9] 
slice= list([A:B:C]) 
# C should be added to "index A" until it reaches "index B". 
# But for negetive numbers you need to pay attention to the equivalent positive index (eg: indx -1 = indx 9) 
# for positive A and B If A<B then C must be positive If A>B then C must be negetive
# for negetive A and B If A<B then C must be positive If A>B then C must be negetive
# when A and B are not of the same sign you have to look at the index which they refer to. 
# Then decide about the sign of the C.
# Eg1. Slice= List([1:-2:C]) 1 refers to number 1 -2 refers to number 8 of index 8 
# So moving from index 1 to index 8 requires a positive C 
# Eg2. Slice= List([8:-3:C]) 8 refers to number 8 -3 refers to number 7 of index 7 
# So moving from index 8 to index 7 requires a negetive C 


# [:1:-1]   -- -1 from last

# Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[7:1:-1]) # print(square[start from 7th index: end at 1 : every 1 step backward])              # output: [49, 36, 25, 16, 9, 4]
# The end(1 index) would not include in the slice. 
print(squares[7:1:-2]) # print(square[start from 7th index: end at 1 : every 2 step backward])              # output: [49, 25, 9]
# The end(1 index) would not include in the output, and the (2 index) not include in the output because of that every -2 steps.

# http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html

# Example:
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])                          # [49, 36]
# Here we have a negative step (-1) - we'll get the elements in reversed order. 
# So, starting backward (from highest to lowest element's index), 
# we make the first slice before index 7, 
# and then the other - before index 5: list 
# sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
# index  0  1  2  3   4   5 ¦ 6   7 ¦ 8   9 slices 2nd 1st 
# And we'll get 2 elements between the slices in reversed order: [49, 36]
    

# We need to start the slicing from index 7 and then continue till index 5 in step of 1. 
# The index count will always be from the beginning. 
# Note that we can go in the reverse direction because the step is -1. 
# Below results will further explain what I am trying to say. 
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(sqs[7:6:-1])                          # [49] 
print(sqs[7:4:-1])                          # [49, 36, 25]
print(sqs[7:3:-1])                          # [49, 36, 25, 16]
print(sqs[7:2:-1])                          # [49, 36, 25, 16, 9]
print(sqs[7:1:-1])                          # [49, 36, 25, 16, 9, 4]

print(square[2:6])                          # Here we make one slice before index 2, and then another - before index 6: 
# list [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
# index 0  1¦ 2  3   4   5 ¦ 6   7   8   9 slices 1st 2nd 
# So we'll get 4 elements between the slices: [4, 9, 16, 25]


# When working with indices, always consider the cursor point. 
# Say we have list = [0,1,4,9,16,25,36,49,81]. 
# If we have to slice list[:4], we can visualize it with the cursor point. 
# Consider 'll' is the cursor point and it is placed at the beginning of each element, like : [ll0, 1, 4, 9, ll16, 25, 36, 49, 81]. 
# So to slice, we can move from the 1st cursor point to the 2nd and collect everything in between which would yield [0,1,4,9] in this case. 
# If negative step is used, then we can just place the cursor point at the end of each element like [0, 1, 4, 9, 16, 25ll, 36, 49ll, 81] 
# and to slice list[7:5:-1], we can move from the 2nd cursor point to the 1st and collect everything in between in reverse order, which would yield [49, 36] in this case.


# Example:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(lista[:-3])   # output: [0, 1, 2, 3, 4, 5, 6] --> Creates a list with 3 elements except the end 
print(lista[::-3])  # output: [9, 6, 3, 0]          --> Creates a reverse list of 3 on 3 starting from the end


# Example:
# Range start = 9 Range end = 0 Count 1 
sqs = [0,1,2,3,4,5,6,7,8,9]
print(sqs[9:0:-1])  # output: [9, 8, 7, 6, 5, 4, 3, 2, 1] 
# Range start = 9 Range end = 5 Count = 1
sqs = [0,1,2,3,4,5,6,7,8,9]
print(sqs[10:5:-1]) # output: [9, 8, 7, 6] 
# If you put -2 will give this output 
# Range start = 9 Range end = 0 Count = 2 
sqs = [0,1,2,3,4,5,6,7,8,9]
print(sqs[10:0:-2]) # [9, 7, 5, 3, 1]



# Examples:
# Why the first index of a list was included and the second was excluded. 
# Realised that this allows a nice way to recompose the full list: 
mylist = [0,1,2,3]
part1 = [:2]
part2 = [2:]
print(part1 + part2) # [0,1,2,3]


# make list 
nums = [1, 2, 3, 4, -3] 
print(nums[::-1])       # [-3, 4, 3, 2, 1] 
# make tuple 
nums = (0, 2, 3, 4, -3) 
print(nums[::-1])       # (-3, 4, 3, 2, 0) 


# When the second number in a slice is omitted, it is taken to be the "end", but the last index is included in the slice. 
# At the other hand, if you write the second number as the last index number, then that index gets excluded from the slice.


# So, I'm getting confused a bit with list ranges. 
# If I have a list with 5 elements (0-4), and I use this notation, 
# then I'd I use list(2:4) it will actually omit the last element. 
# If I did list(2:5) I should get index error. 
# But if I do list(2:) 
# I'd actually get all elements from index 2 up to and including the last element.


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[:-2])
print(squares[2:-2])


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
print(squares[:7]) 
print(squares[4:-2])


I noticed there are still quite a few questions on this comment thread. 
Here are some examples I created that helped me understand how slice interacts with list squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
#slice used to return the beginning of the range to the index #before the 7th index in the list print(squares[:7]) print() 
#slice used to return from the 7th index to end of the range in the list. print(squares[7:]) print() 
#Using Slice to return an empty sequence. print(squares[10::]) print() 
#using slice to return a sequence of the complete list print(squares[::]) print() 
#using slice to return a sequence of the list backwards #note: this doesn't reverse the list in place like 
#the list.reverse() function would. print(squares[::-1]) print() 
#using slice in steps(offset) to start at the beginning of the list 
#and go right by 2 print(squares[::2]) print() 
#using slice in steps(offset) to start at the end and go left by 2 print(squares[::-2])



# Example:
serie_A = [['Juventus', 90],['Inter', 88],['Atalanta', 83],['Lazio', 79],['AsRoma', 71],['Napoli', 65],['AcMilan', 61]] 
champion = serie_A[:1]
champions_league = serie_A[:3]
cl_playoffs = serie_A[4:5]
europa = serie_A[6:]
print(champion)



# Tuples are very similar to lists, BUT they are IMMUTABLE, meaning that they CANNOT be CHANGED at all in anyway whatsoever. 
# As such, they are faster to deal with for computers as they are STATIC. 
# Slicing is JUST a means of RETRIEVING values, so just chill, it's not at all there to MODIFY values at all!

# I don't think there was any mention of slicing tuples, and I remembered it being a thing for lists so I got this wrong, I went back to both the tuple lesson and the list slices lesson and couldn't find anything about slicing tuples. At first my code in Code playground didn't seem to work (I think my tuple was too short for the range I set at first) but this code does as I'd expect. I've not tested every list slice variation, but it seems to work with the same syntax as for lists tuple = (1,2,3,4,5) print(tuple[1:-1])

# Example:
tuple = (0, 1, 4, 9, 16, 25, 36, 49, 64, 81) 
print(tuple[2:6]) # Result: (4, 9, 16, 25) So, the tuple also can slice.

# https://docs.python.org/3/library/stdtypes.html#typesseq

# list slicing reverses the list 'numbers' --> numbers[::-1]    --> cause it's [index1:index2:step], where index1 is default to 0, index2 is default to last in the list.

# [index of the first object: index of one after the last: step]

# None means EMPTY is returned by functions that dont have a return statement whereas, 0 is a VALUE and False too.

# Example:
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42))) # 44
# nums[:2] will print ( 55,44) and min(55,44) will print 44 at last max (44,42) will print 44 so the answer will come out to be 44




