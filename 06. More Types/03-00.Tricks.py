# Multi Assignments: Py program to assign values of a list, tuple, or set to multiple variables in one line
a = [1, 2, 3]  #list
b = (4, 5, 6)  #tuple
c = {7, 8, 9}  #set

p, q, r = a
s, t, u = b
x, y, z = c

print(p, q, r)
print(s, t, u)
print(x, y, z)

#output:
# 1 2 3 
# 4 5 6
# 7 8 9
