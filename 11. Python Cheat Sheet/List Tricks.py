# Python List Cheat Sheet

# Create a new list
x = [1, "x", 3.1415]
y = list(x)

# Indexing
x = [1, 2, 3]
x[0]   # 1
x[1]   # 2
x[-1]  # 3
x[-2]  # 2

# Length of List
x = [1, 2, 1, 2]
length = len(x)  # length = 4

# Assignment
x = [1, 1, 1]
x[-1] = 2
x[0] = 2     # x = [2, 1, 2]

# Append
x = [1,1]
y = [3,3]
x.append(2)   # x = [1,1,2]
x.append(y)   # x = [1, 1, 2, [3, 3]]

# Extend
x = [1,2]
y = [3,4]
x.extend(y) # x = [1,2,3,4]

# Insert
x = [1,3]
x.insert(1,2)  # x = [1,2,3]

# Remove
xs = [1,2,3]
xs.remove(2)  # xs = [1, 3]

# Slicing
start = 5
stop = 15
step = 2
x = list(range(20))
print(x[start:stop:step])   # [5,7,9,11,13]

# Min/Max
x = [1,2,3]
m = max(x)  # m = 3

# Sum
x = [1, 1, -2]
s = sum(x)  # s = 0

# Sort
x = [3,1,4,2]
x.sort()    # x = [1,2,3,4]

#-----------------------------------#

# 4 Ways to Print List Items
# 01. Using For Loop
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in lst:
  print(num)
#
#  1
#  2
#  ...
#  9

  
# 02. Using * operator
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*lst)
# 1 2 ... 9


# 03. Using While Loop
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i=0
while i < len(lst):
  print(lst[i])
  i += 1
#
#  1
#  2
#  ...
#  9


# 04. Using Map
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(' '.join(map(str, lst)))
# 1 2 ... 9

#-----------------------------------#

