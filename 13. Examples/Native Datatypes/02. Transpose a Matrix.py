# Native Datatypes Examples
# Example: to Transpose a Matrix

# In this example, you will learn to transpose a matrix (which is created by using a nested list).

# In Python, we can implement a matrix as a nested list (list inside a list). We can treat each element as a row of the matrix.

# For example X = [[1, 2], [4, 5], [3, 6]] would represent a 3x2 matrix. 
# The first row can be selected as X[0]. And, the element in the first-row first column can be selected as X[0][0].

# Transpose of a matrix is the interchanging of rows and columns. It is denoted as X'. 
# The element at ith row and jth column in X will be placed at jth row and ith column in X'. 
# So if X is a 3x2 matrix, X' will be a 2x3 matrix.

# Here are a couple of ways to accomplish this in Python.

# Matrix Transpose using a Nested Loop
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
# 
"""
Output:
[12, 4, 3]
[7, 5, 8]
"""

# In this program, we have used nested for loops to iterate through each row and each column. 
# At each point we place the X[i][j] element into result[j][i].



# Matrix Transpose using Nested List Comprehension
''' Program to transpose a matrix using list comprehension'''
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)

# The output of this program is the same as above. 
# We have used nested list comprehension to iterate through each element in the matrix.



