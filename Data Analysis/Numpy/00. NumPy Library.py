# THE NUMPY LIBRARY
# The NumPy library (NumPy, Numerical Python) is a package of high-level mathematical and numerical functions and tools 
# that are designed to work with the numpy array object. 
# A numpy array is a high performance multidimensional data structure and is all around more efficient and convenient than a Python list. 

# A Python program using the numpy library may require installing the package. 
# Additionally, a program that uses the package must include the statement:
import numpy


# THE NUMPY ARRAY
# Python deals primarily with lists and doesn't have a native array structure, 
# so to understand the numpy array it's important to have a basic understanding of arrays. 
# A one-dimensional array can be directly compared to a Python list because they both store a list of numbers. 
# Similarly, the data in an array are called elements and they are accessed using brackets [ ]. 
# A two-dimensional array has a grid structure with rows and columns. 
# And a three-dimensional array can be thought of as a stack of two-dimensional arrays. 

# Numpy arrays are a fixed size, indexed starting at 0, and contain elements of all the same type. 
# They are ndarray objects and are created using the np.array() function.
# Example:
import numpy as np
b = np.array([1, 2, 3, 4])

# The code above creates a one-dimensional array with four constants. 
# Numpy arrays refer to dimensions as axes and the number of axes is rank. Therefore, b is an array of rank 1. 

# There are several numpy functions for describing an array and its elements, as demonstrated in the code below:
import numpy as np

# Create an array of rank 2
my_arr = np.array([[1,2,3,4], [5,6,7,8]])

print(my_arr)
print(my_arr[1, 2]) # access a single element
print(my_arr.ndim) # the rank
print(my_arr.shape) # n rows, m columns
print(my_arr.size) # number of elements 
print(type(my_arr)) # element type

# Note the use of brackets when creating the array. Brackets are also used when accessing an element.

# The number of elements in each row of an array must be equal. 
# Otherwise if you ask the size of the array it will output only number of rows.
# Example:
my_arr = np.array([[1,2,3,4],[3,4,6],[5,6,7,8]])      # if you ask it to print the size of the array, it will show output :- 3
# but if all the elements of each row is equal like this
my_arr = np.array([[1,2,3,4],[3,4,6,7],[5,6,7,8]])    # output will be :- 12



"""
# Example - Given the list: 
my_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]],[[9, 10], [11, 12]],]
my_arr = np.array(my_list)

#rank: my_arr.ndim, is the number of outermost elements of my_list. There are 3 of them:
[[1, 2], [3, 4]],
[[5, 6], [7, 8]],
[[9, 10], [11, 12]]
# Hence, my_arr has the rank of 3.

• shape: my_arr.shape, presenting the number of elements from the outermost ‘level’ to the innermost ‘level’, in the type of a tuple object.
e.g. the shape is (3, 2, 2).

• size: my_arr.size, is the number of the innermost elements: 12 (= 3*2*2).

P/s 1: all elements at the same ‘level’ must have the same ‘structure’.
P/s 2: provided an array shape, you can figure out the rank (as the first element of the shape tuple) and the size (as the multiplication of tuple elements).

# Code  
import numpy as np
my_list = [
			[[1, 2], [3, 4]],
			[[5, 6], [7, 8]],
			[[9, 10],[11, 12]],
		   ]
my_array = np.array(my_list)
my_rank = my_array.ndim # 3, number of outermost elements of the list
my_shape = my_array.shape # (3, 2, 2) ,= (<no.outermost elements>, <no.outers>, ..., <no.innermosts>)
my_size = my_array.size # 12, number of innermost elements of the list
print(my_array[0, 1, 0])
print(my_rank)
print(my_shape)
print(my_size)
print(type(my_array))
"""

  
  
ndim is not the rank of the matrix. 
Orherwise tge output of following prog would be different since we have no linear independencie.
# Code:
import numpy as np

# Create an array of rank 2
my_arr = np.array([[1,2,3,4], [2,4,6,8]])

print(my_arr)
print(my_arr[1, 2]) # access a single element
print(my_arr.ndim) # the rank
print(my_arr.shape) # n rows, m columns
print(my_arr.size) # number of elements 
print(type(my_arr)) # element type




# As pointed out by some of you, .ndim does not return the 'rank' of a matrix, but the number of dimensions in a matrix. 
# I've made some additions to the code above to help explain things a bit better.
# Code:
import numpy as np

# to explain .ndim better, lets use the analogy of a line (1 dimensional), a rectangle (2 dimensional), and a cuboid (3 dimensional)

# Create a 3 x 4 matrix (2 dimensional since the matrix does not have a height, and is more like a flat rectangle)
my_arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

print(my_arr)
# can use - to access elements from the end of the array just like with lists
print(my_arr[-1, -2]) # access a single element
print(my_arr.ndim)    # the number of dimensions
print(my_arr.shape)   # n rows, m columns
print(my_arr.size)    # number of elements 
print(type(my_arr))   # element type

# create a 2 x 3 x 4 (3 dimensional matrix with a height, like a cuboid) matrix of zeros 
a = np.zeros((2,3,4))
print(a)       # 2 stacks of 3 rows x 4 columns
print(a.ndim)  # prints 3

# create a 1 x 4 vector or one dimensional array (imagine a straight line)
b = np.array([1,2,3,4])
print(b.ndim)  # prints 1




  
# Example:
import numpy
hb = numpy.array([[4,7,6,4], [5,7,75,578], [57,574,86,3]])
print(hb)
print(hb[2, 3])
print(hb.ndim)
print(hb.shape)
print(hb.size)
print(type(hb))


