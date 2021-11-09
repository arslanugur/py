# QUOTIENT
  # Floor division is done using two forward slashes 
  # and is used to determine the quotient of a division (the quantity produced by the division of two numbers).

# For example:
print( 20 // 6 )  # 3
                    # The code above will output 3, because 6 goes into 20 three times. 
                    # 20 divided by 3 equals 6 and + 2, in this case 6 is 20/3's quotient, 2 is its remainder
print(20/6)       # 3.33333333 
print (20%6)      # 2  
# You can also use floor division on floats.

# // equates to quotient, which simply means how many of the latter number is in the former number (e.g. three 6s in 20)
# % equates to remainder, which is a term for what is remaining after subtracting the quotient
# (e.g. two 0.5s fill up 1.25, and the remainder is 0.25)

# 4%2 = 0 ( Remainder ) 
# 4/2 = 2.0 ( Quotient... Float ) 
# 4//2 = 2 ( Quotient... Integer )

# how easily calculated: 
# 20//6 = 6 + 6 + 6 = 18         (answer 3) 
# 40//7 = 7 + 7 + 7 + 7 + 7 = 35 (answer 5)

print((2 * 0.5 ) + 0.25)  # 1.25

# 4/3 = 1.33333
# 4//3 = 1

# 10 // 4 = 2
# 10 % 4 = 2

print(7%(5//2)) # which means they want the quotient of 5//2 and that of remainder when divided by 7. 
                # So 5//2 means 2 divided by 5 and quotient is 2, next is 7%(2) which is 2 divided by 7 and the remainder is 1.
# 7 % ( 5 // 2) = 1 
# 5 // 2 = 2
# 7 % 2 # 7 ÷ 2 = 3.5 we pick up only 3 
# 7 - ( 3 × 2 ) = 1



# REMAINDER
    # The modulo operator is carried out with a percent symbol (%) and is used to get the remainder of a division.
    # Very Important: In future lessons what does % mean or how does it work.
    # For example:
print(20 % 6)     # 2
                  # 20 % 6 = 20 - 6 = 14 
                  #                   14 - 6 = 8 
                  #                            8 - 6 =  2 --> 20 % 6 = 2

                  # 20 % 6 = 6 + 6 + 6 = 18 --> 20 - 18 = 2
        
print(1.25 % 0.5) # 0.25
                  # 0.5 can go in 1.25 twice 0.5 * 2 = 1.0 
                  # Obviously the remainder would be 0.25
                  
                  # 1.25 % 0.5 = 1.25 - 0.5 = 0.75
                  #                           0.75 - 0.5 = 0.25 --> 1.25 % 0.5 = 0.25
          
# Remainder Examples
# 9 % 3 = 0 
# 10 % 3 = 1 
# 11 % 3 = 2 
# 11.9  % 3 = 2.9 
# 12 % 3 = 0

# All numerical operators can also be used with floats.

# First Way
print(76%((18+19)*2)) # 2
# Second Way
a = 18 + 19 
b = a * 2 
c = 76 % b 
print(c)  # 2 

# Example of using // and %
# There are 10 apples on the table. 
# Tasks:                                                # Solutions: 
# 1) How many children can you give 3 apples each?      # 10 // 3 = 3 children
# 2) How many apples are left?                          # 10 % 3 = 1 apple left

# Example:
print(7%(5//2)) # 1
   # (7%(5//2))
   # (7 % (2) )
   #  7 % 2     # 1
  
# Examples:
print(7%(5//2)) # 5 // 2 = 2 --> 7 % 2 = 1
print(7%(5%2))  # 5 % 2 = 1 --> 7 % 1 = 0






