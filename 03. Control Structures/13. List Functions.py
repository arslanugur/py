# APPEND METHOD
# The append method adds an item to the end of an existing list.
# For example:
nums = [1, 2, 3]
nums.append(4)
print(nums)   # [1, 2, 3, 4]

# The dot before append is there because it is a method of the list class. 
# Methods will be explained in a later lesson.

# Example:
dollar = [1,25] 
gold = dollar     # gold = [1,25] 
dollar = [1,25,35]  # changing the value of dollar 
print(gold)       # variable 'gold' is not updated and output is [1,25]




# LEN FUNCTION
# To get the number of items in a list, you can use the LEN FUNCTION. 
nums = [1, 3, 5, 2, 4]
print(len(nums))  # 5

# Example:
s = [1,2] 
e = s
b = e
s.append(3)         # s += [3] and s = s.insert(2,3) also update both 'b' and 'e' to [1,2,3]
print(s)  # [1,2,3] 
print(e)  # [1,2,3] 
print(b)  # [1,2,3] 


# Example:
nums = [10,9,8,7,6,5]
nums.extend([4,3,2,1])
print(nums)             # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
nums = [10,9,8,7,6,5] 
nums.append([4,3,2,1])
print(nums)             # [10, 9, 8, 7, 6, 5, [4, 3, 2, 1]]
nums = [10,9,8,7,6,5] 
nums += [4,3,2,1] 
print(nums)             # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



# Unlike the index of the items, len does not start with 0. So, the list above contains 5 items, meaning len will return 5. 
# len is written before the list it is being called on, without a dot.

# Example:
nums = [1, 3, ["foo", "bar"], 5, 2, 4] 
print(len(nums)) # 6

# Example:
nums = [1, 2, 3,[1,2,3], 4, 5, 6] 
print(len(nums[3])) # 3


# Example:
letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))   # 4


# Example:
A = "ac37k" 
print(len(A))     # 5 
B = [1,2,"Hello","World"]
print(len(B))     # 4 
B = [1,2,"Hello","World"]
print(len(B[2]))  # 5 
B=[[1,2],"Hello","World"] 
print(len(B[0]))  # 2

# Example:
nums = [1, 3, 5, 2, 4]
nums.append([7, 8])
print(len(nums)) # 6 

nums = [1, 3, 5, 2, 4] 
print(len(nums + [6, 7])) # 7 

# Example:
items = [2, 4, 6, 8, 10, 12, 14] 
x = len(items) // 2 
print(x) # 3


# INSERT METHOD
# The INSERT METHOD is similar to append, except that it allows you to insert a new item at any position in the list, as opposed to just at the end.
words = ["Python", "fun"]
index = 1
words.insert(index, "is")   # or words.insert(1,"is")
print(words)    # ['Python', 'is', 'fun']

# Elements, that are after the inserted item, are shifted to the right.
nums = [2, 7, 4, 3, 0] 
nums.insert(-1, 5) 
print(nums)     # [2, 7, 4, 3, 5, 0] 


# Examples:
a = 3
b = "Hello"
c = 4 

A = [1, 2, a, b, "World", [c, 5, "c"] ] 
print(A) # [1, 2, 3, "Hello", "World", [4, 5, "c"] ]

A = [1, 2, a, b, "World", [c, 5, "c"] ] 
A.insert(1,"TEST")
print (A) # [1, "TEST", 2, 3, "Hello", "World", [4, 5, "c"] ]
A = [1, 2, a, b, "World", [c, 5, "c"] ]
A[5].insert(2,"TEST")
print (A) # [1, 2, 3, "Hello", "World", [4, 5, "TEST", "c"] ] 
A = [1, 2, a, b, "World", [c, 5, "c"] ]
A[4].insert(2,"TEST") # ERROR: (str) object has no attribute 'insert' 


# Example:
words = ["Python", "fun"] 
index = 1 
words.insert(index, "is") 
words.remove("fun") 
index=2 
words.insert(index, "awesome") 
print(words)  # ['Python', 'is', 'awesome']


# Example:
list = ["is", "mind"] 
put1 = 0 
put2 = 2 
put3 = 4 
list.insert(put1, "Where") 
list.insert(put2, "my") 
list.insert(put3, "now.") 
print(list)   # ['Where', 'is', 'my', 'mind', 'now.'] 


# The index method finds the first occurrence of a list item and returns its index.
# If the item isn't in the list, it raises a ValueError.
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r')) # 2
print(letters.index('p')) # 0
print(letters.index('z')) # Value Error: 'z' is not in list


# There are a few more useful functions and methods for lists.
# max(list)         :Returns the list item with the maximum value
# min(list)         :Returns the list item with minimum value
# list.count(item)  :Returns a count of how many times an item occurs in a list
# list.remove(item) :Removes an object from a list
# list.reverse()    :Reverses items in a list.

# For example, you can count how many 42s are there in the list using:
# items.count(42)
# where items is the name of our list.

# Example:
words =["t","e","n","e","t"] 
words.reverse() 
print(words) # ['t', 'e', 'n', 'e', 't']

# https://www.geeksforgeeks.org/list-methods-python/



# Example:
lst = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(sum(lst, []))                       # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Example:
changes = [1,2] 
changes.extend((3,4)) 
print(changes)              # [1, 2, 3, 4]
changes.extend(range(5,10)) 
print(changes)              # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Examples:
nums = [1, 2, 3] 
nums.append(4) 
print(nums)       # [1,2,3,4]

nums = [1,2,3] 
nums += [4]       # or print(nums+[4])
print(nums)       # [1,2,3,4] 

nums = [1,2,3] 
nums[2] = 3,4 
print(nums)       # [1,2, (3,4)]

# Example:
list_methods = ['append', 'copy', 'count', 'insert', 'clear', 'remove']
del(list_methods[-1])
print(list_methods)  # ['append', 'copy', 'count', 'insert', 'clear']


# Example:
nums=[[2]]*3 
nums[0].append(7) 
nums[1].append(3) 
print(nums)         # [[2, 7, 3], [2, 7, 3], [2, 7, 3]]
nums=[[2],[2],[2]] 
nums[0].append(7) 
nums[1].append(3) 
print(nums)         # [[2, 7], [2, 3], [2]]


# Examples:
list0=[1,2,3]
list0.pop()
print(list0) # [1,2]

list1=[2,3,4] 
print(list1.pop(2)) # 4 

list2=[3,4,5] 
list2.remove(4) 
print(list2) # [3,5] 

list3=[4,5,6] 
del list3[1] 
print(list3) # [4,6] 


# Example:
nums = [1, 2, 3] 
nums.append(4) 
print(nums) # [1,2,3,4]
nums += [3,6,8] 
print(nums) # [1,2,3,4,3,6,8]


# Example:
words = ["hello"]
words.append("world")
print(words[1]) # world

words = ["hello"]
words.append("world")
print(words[1]) # world
print(words) # ['hello', 'world']


nums = ["hello"] 
nums.append("world") 
print(nums[1][4]) # d


# Example:
nums = [9, 8, 1, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))  # 7
print(nums)       # [9, 8, 11, 1, 6, 5, 4]

# Examples:
# 1. Different between the function 'append' and 'pop' 
num=[1,2,3,4] 
num.append(5) 
print(num)      # [1,2,3,4,5] 
num.pop() 
print(num)      # [1,2,3,4] 
num.pop() 
print(num)      # [1,2,3] 

# 2. Different between the function 'remove' and 'pop' 
num=[1,2,3,4] 
num.remove(0) 
print(num)      # error, don't exist in the item 

num.pop(0) 
print(num) # output : [2,3,4] 

# The function 'sort' (Displayed in alphabetical order) 
num=['z','u','j','l','s','p','w'] 
num.sort() 
print(num) #  ['j', 'l', 'p', 's', 'u', 'w', 'z']


# Example:
letters = ['p','A', 'q', 'r','u','k','h','s', 'p', 'u','z','Z'] 
print(letters.index('r'))   # 3
print(letters.index('p'))   # 0
print(letters.index('u'))   # 4
print(max(letters))         # z
print(min(letters))         # A
print(letters.count('p'))   # 2
print(letters.count('Z'))   # 1
letters.remove('A') 
print(letters)              # ['p', 'q', 'r', 'u', 'k', 'h', 's', 'p', 'u', 'z', 'Z']
letters.reverse() 
print(letters)              # ['Z', 'z', 'u', 'p', 's', 'h', 'k', 'u', 'r', 'q', 'p']
print(letters.count('p'))   # 2
print(max(letters))         # z
print(min(letters))         # Z



# Example: finding all the indexes of a particular item in a list.
m=[1,2,3,1] 
i=0 
for a in m: 
  if a == 1: 
    print('index of one is:',i,) 
    i+=1 
  else: 
    i+=1 
# index of one is: 0
# index of one is: 3

# Example:
list.append('z')
print(len(list))  # it adds z to the list then print (len(list) to see how many entities are in that list


# Example:
i= int(input('Give me number: ')) 
x = i + 10 
nums = [] 
while i <= x: 
  nums.append(i) 
  i += 1 
  print(nums)
# Give me number: 5
[5]
[5, 6]
[5, 6, 7]
[5, 6, 7, 8]
[5, 6, 7, 8, 9]
[5, 6, 7, 8, 9, 10]
[5, 6, 7, 8, 9, 10, 11]
[5, 6, 7, 8, 9, 10, 11, 12]
[5, 6, 7, 8, 9, 10, 11, 12, 13]
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  

# Example:
i= int(input('Give me number: ')) 
x = i + 10 
nums = [] 
while i <= x: 
  nums.append(i) 
  i += 1 
print(nums)
# Give me number: 5
[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]



