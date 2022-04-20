# Using For Loop
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in lst:
  print(num)
#
#  1
#  2
#  ...
#  9

  
# Using * operator
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*lst)
# 1 2 ... 9


# Using While Loop
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


# Using Map
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(' '.join(map(str, lst)))
# 1 2 ... 9




