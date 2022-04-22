rows = 5
for i in range(0, rows):
  for j in range(0, i+1):
    print("*", end='')
    print("\r")
#


# Second Way
rows = 5
for j in range(1, rows+1):
  print("*"*j)
#


