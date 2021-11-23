# The item at a certain index in a list can be reassigned.
# For example:
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums) # [7, 7, 5, 7, 7]

# You can replace the item with an item of a different type.

a = ['x' , 'y']
b = a
b[0] = 'z' 
print(b) # ['z' , 'y'] 
print(a) # ['z' , 'y'] 

# Example:
moviequote = ['Frankly','my','dear','I','don\'t','give','a','hoot'] 
moviequote[7] = 'damn' 
print(moviequote)

# while Example:
nums = [7, 7, 7, 7, 7] 
x = 0 
while x < len(nums): 
    nums[x] = 5 
    x += 1 
    print(nums) 
# for Example:
nums = [7, 7, 7, 7, 7] 
for x in range(len(nums)): 
    nums[x] = 5 
    print(nums)

    
    
# Case1: 
nums = [7, 77, 77] 
nums[2] = 5 
print(nums)       # [7, 77, 5] 
# Case 2: 
nums = [7, 77, 77] 
print(nums[2][1]) # TypeError: 'int' object is not subscriptible
# Case 3: 
nums = [7, 77, "77"] 
print(nums[2][1]) # 7 
# Case 4: 
nums = [7, 77, "77"] 
nums[2][1] = 5 
print(nums)       # TypeError: 'str' object does not support item assignment 
  
        
# Case 1:
a = [1,2,3,4,5] 
a[1:4]= ["a","b","c"] 
print(a)         # [1, 'a' , 'b' , 'c' , 5] 
# Case 2:
a = [1,2,3,4,5] 
reassign = ["a","b","c"] 
a[1:4]= reassign 
print(a)         # [1, 'a' , 'b' , 'c' , 5]

# Example:
nums = [7, 7, 7, 7, 7]
nums[:2] = 1,2,3 
nums[3:5]= 4,5 
print(nums) # 1,2,3,4,5,7

# Example:
nums = [7, 7, 7, 7, 7]
nums[2] = input('Add number')
print(nums)

# Example:
x = [7,7,7,7,7]
x = [5 for i in x]
print(x) # [5,5,5,5,5]

# Example:
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input())
items[num]="x" 
print(items)

# Example:
x = 1 
nums = [7, 7, 7, 7, 7] 
for i in nums: 
    a = nums.index(i) 
    nums[a] = a*x+x 
    print(nums)

    
# A simple calculator, using list and if function: 
a=int(input('enter first number: ')) 
b=int(input('enter second number: ')) 
operation= input('enter the operation needed: ')
c=['+', '-','*','/'] 
if operation==c[0]: 
    print('your answer is: ' , a+b) 
if operation==c[1]: 
    print('your answer is: ' , a-b) 
if operation==c[2]: 
    print('your answer is: ' , a*b) 
if operation==c[3]: 
    print('your answer is: ' , a/b)
    
# Example:
nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])  # we are assigning nums[1] to nums[3]. That means 2 in the place of 4



# Lists can be added and multiplied in the same way as strings.
# For example:
nums = [1, 2, 3]
print(nums + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
print(nums * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# Example:
# The list can be multiplied with numbers and the result is equal to the string, 
# the list will repeat the value of the number 
B = [0] * 10
print(B) 
# output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Lists and strings are similar in many ways - strings can be thought of as lists of characters that can't be changed.

# For example, the string "Hello" can be thought of as a list, where each character is an item in the list. 
# The first item is "H", the second item is "e", and so on.

# Example:
nums = [1, 2, 3] 
numr = [7, 8, 9] 
nums = nums + numr 
print(nums)

# Extra Info:
# Difference between LIST and SPLIT function: 
s ='i love humanity' 
a =list(s) 
print(a) #output : ['i', ' ', 'l', 'o', 'v', 'e', ' ', 'h', 'u', 'm', 'a', 'n', 'i', 't', 'y']

s ='i love humanity'.split() 
print(s) #output : ['i', 'love', 'humanity'] 
# List function seperates each character 
# split functon seperates each word
    

# Example:
a = [0,1,2,3]
print(2*a)  # [0, 1, 2, 3, 0, 1, 2, 3]          print(2/a) --> Error
print(a+a)  # [0, 1, 2, 3, 0, 1, 2, 3]          print(2-a) --> Error

# Examples:
nums = [1, 2, 3] 
nums += 4 
print(nums) # error

nums = [1, 2, 3]
nums += [4]
print(nums) # output [1,2,3,4] 

nums = [1, 2, 3]
nums *= [4]
print(nums) # error

nums = [1, 2, 3]
nums *= 4
print(nums) # output [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]


# to create a list, reassign its 2nd element and print the whole list.
nums = [33, 42, 56]
nums[1] = 22        # Remember, the first element is always "0"
print(nums)


# Example:
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3])    # 7
else:
  print(nums[4])



# To check if an item is not in a list, you can use the not operator in one of the following ways:
nums = [1, 2, 3]
print(not 4 in nums)    # True
print(4 not in nums)    # True
print(not 3 in nums)    # False
print(3 not in nums)    # False


# Example: 
nums = [1, [4,5], 2, 3] 
print(4 in nums)        # False
print(5 in nums)        # False
print([4,5] in nums)    # True
print(4 in nums[1]      # True


# Example:
nums = [1, 2, 3, '4'] 
print(not '4' in nums)  # False
print(4 not in nums)    # True
print(not 3 in nums)    # False
print(3 not in nums)    # False
      

# Example: to print "Yes" if the list contains 'z':
letters = ['a', 'b', 'z']
if "z" in letters:
  print("Yes")  # Yes
      
# Example:
fruit=input("Enter fruit name: ") 
basket=["mango","apple","orange"] 
if not fruit in basket: 
    print(fruit+" is not in basket") 
else: 
    print(fruit+" is in basket") 
# Enter fruit name: apple
# apple is in basket

   
# Example:
nums = [1, 2, 3]
x = input("What number would you like to check for?: ") 
if not int(x) in nums: 
    print("There is no " + x + " in nums") 
else: 
    print("There is a " + x + " in nums!") 
      
      
      
# Simple Example:
print("i" in "team")    # False
print("i" in "win")     # True      # Life Lesson: There's no i in team but there is in win))


# Example:
# Someone stole iPhone in this room filled with 3 people excluding me. 
# who is culprit? John--Rocky-- Dave? 
John = ['wallet', 'ring', 'knife', 'pen'] 
Rocky = ['paper', 'pen', 'Samsung'] 
Dave = ['cigarette', 'keys', 'wallet', 'iphone'] 
print('iphone' in John) 
print('iphone' in Rocky) 
print('iphone' in Dave)


# Example:
words = "spamegg"
print("spam" in words)  # True
print("egg" in words)   # True
print("meg" in words)   # True


# Example: How you can check whether or not a string is a substring of another string.
list1 = ["robert downey", "tony", "holmes", "stark"]
print("downey" in list1[0]) # True 


# Question Example:
# you can also add any element to the last of the list of any type by using 
list.append(element)
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits) #output [apple, banana, cherry, orange]

# The question said re-assign its 2nd element. 
# Anything inside the LIST is call ELEMENT 
# We have in the list [33, 42, 56] so 42 is the 2nd element which make it index 1 nums = [33, 42, 56] nums[1] = 22 print(nums) 
# Remember that 33 is index 0, 42 is index 1 and 56 is index 2


# To check if an item is in a list, the in operator can be used.
# It returns True if the item occurs one or more times in the list, and False if it doesn't. 
words = ["go", "your", "own", "way", 7]
print("go" in words)        # True
print("your" in words)      # True
print("away" in words)      # False
print(7 in words)           # True 
print("7" in words)         # False

# The in operator is also used to determine whether or not a string is a substring of another string.


# Example:
tools = ["wrench","putty knife","jigsaw",["nut","bolt","washer"],"hacksaw"]
print("washer" in tools[3]) # True

tools = ["wrench","putty knife","jigsaw",["nut","bolt","washer"],"hacksaw"]
print("washer" in tools) # False

tools = ["wrench","putty knife","jigsaw",["nut","bolt","washer"],"hacksaw"]
print(tools[2][3:5] in tools[4]) # True                                    # tools[2] = "jigsaw" [3:5] = "saw"

tools = ["wrench","putty knife","jigsaw",["nut","bolt","washer"],"hacksaw"]
print(tools[2][3:5] in tools) # False

# the function will not search for substrings within the whole list of elements, but it will search within specific elements of the list
# it is useful to my understanding of the function.

print(tools[3][0:1])    # ['nut']
print(tools[3][0])      # nut

    
# Example:
nums = [1, 2, 3, [7, 8]]
req = int(input("Search: "))

if req in nums:
    print("Yes")
elif req in nums[3]:
    print("In nested list")
else:
    print("No")
# input: 2  output: Yes
# input: 7  output: In nested list
# input: 4  output: No



