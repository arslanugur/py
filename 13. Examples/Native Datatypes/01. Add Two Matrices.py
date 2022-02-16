# Native Datatypes Examples
# Example: to Add Two Matrices

# In this program, you'll learn to add two matrices using Nested loop and Next list comprehension, and display it.

# In Python, we can implement a matrix as a nested list (list inside a list). We can treat each element as a row of the matrix.

# For example X = [[1, 2], [4, 5], [3, 6]] would represent a 3x2 matrix. 
# First row can be selected as X[0] and the element in first row, first column can be selected as X[0][0].

# We can perform matrix addition in various ways in Python. Here are a couple of them.
# Source code: Matrix Addition using Nested Loop

# Program to add two matrices using nested loop
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)  
# 
"""
Output:
[17, 15, 4]
[10, 12, 9]
[11, 13, 18]
"""

# In this program we have used nested for loops to iterate through each row and each column. 
# At each point, we add the corresponding elements in the two matrices and store it in the result.
# Source Code: Matrix Addition using Nested List Comprehension
  
# Program to add two matrices using list comprehension
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)
#    

# The output of this program is the same as above. We have used nested list comprehension to iterate through each element in the matrix.
# List comprehension allows us to write concise codes and we must try to use them frequently in Python



