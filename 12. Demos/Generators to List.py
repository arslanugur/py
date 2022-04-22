def infinite(x):
   while x < 10:
      yield x
      x += 1

l = [i for i in infinite(1)]
print(l)
print(l[0:4])

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4]

