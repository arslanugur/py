# Floats are used in Python to represent numbers that aren't integers (whole numbers).
# Some examples of numbers that are represented as floats are 0.5 and -7.8237591.
# They can be created directly by entering a number with a decimal point, or by using operations such as division on integers.
print( 3/4 )  # 0.75
print( 0.42 ) # 0.42

# Computers can't store floats perfectly accurately, 
# in the same way that we can't write down the complete decimal expansion of 1/3 (0.3333333333333333...). 
# Keep this in mind, because it often leads to infuriating bugs!


# dividing any two integers produces a float.
# A float is also produced by running an operation on two floats, or on a float and an integer.
print( 8 / 2 )    # 4.0
print( 6 * 7.0 )  # 42.0
print( 4 + 1.65 ) # 5.65

# A float can be added to an integer, because Python silently converts the integer to a float.
# Examples:
2 / 2 = 1.0 
2 // 2 = 1
2 // 2.0 = 1.0
2 + 1 = 3
2 + 1.0 = 3.0
5 + 1 = 6
5 + 1.0 = 6.0
5.0 + 1 = 6.0
5.00 + 1.0 = 6.0 
5. +1 = 6.0
5 + 1. = 6.0
print(1 + 2 + 3 + 4.0 + 5) = 15.0

# integer + float = float 
# float + float = float
# integer + integer = integer
# integer + integer + integer + float + integer = float

# Mathematical Reason: 1+2+3+4.0+5=15 or 15.0 ( In some scientific Calculators) 
# Technical Reason: float+float = float  integer+float = float 
# Float and integers are different data types and used differently. 
# Their memory representations are diff. Floats usually take higher memory. 


