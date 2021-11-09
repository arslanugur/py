# Besides addition, subtraction, multiplication, and division, 
# Python also supports exponentiation, which is the raising of one number to the power of another. 
# This operation is performed using two asterisks.
print(2**5) # 2**5 = 2^5 = 2*2*2*2*2 = 32

# You can chain exponentiations together. In other words, you can rise a number to multiple powers. For example, 2**3**2.
print(8**2)           # 8 * 8 = 64
print(36**1/2)        # 6
print(9**1/2)         # √9 = 3
print(9.0**(1.0/2.0)) # 3
print(8**(1/3))       # 2.0  # ∛8 # ∛8 = 8⅓ = 2   # 8.0**(1/3) = 2.0
                      # 2.0**3 = 8.0  # 2³ = 8  # 2³*1/3 
# to output 5 raised to the 3rd power.
print(5**3) # 5**3 = 5^3 5^3 = 5 × 5 × 5 = 125

# You can also use floats in exponentiation.
# For example, the following code will result in the square root of 9: 
print(9 ** (1 / 2)) # 3.0

# when there are multiple exponential operations, Python always starts from right to left. 
# i.e. precedence is for the last exponential operation.
print( 2 ** 3 ** 4 ** 0.5 ) # 512.0
print( 2 ** 3 ** 2.0 )      # 512.0
print( 2 ** 9.0 )           # 512.0


