# Python List Cheat Sheet
# Create a new list
xs = [1, "x", 3.1415]
ys = list(xs)

# Indexing
xs = [1, 2, 3]
xs[0]   # 1
xs[1]   # 2
xs[-1]  # 3
xs[-2]  # 2


# Length of List
xs = [1, 2, 1, 2]
length = len(xs)  # length = 4

# Assignment
xs = [1, 1, 1]
xs[-1] = 2
xs[0] = 2     # xs = [2, 1, 2]

# Append
.....


zora eğilim olsun, kolay zaten kolay


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




