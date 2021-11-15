# BOOLEANS
  # Another type in Python is the Boolean type. There are two Boolean values: True and False.
  # They can be created by comparing values, for instance by using the equal operator ==.
my_boolean = True
print(my_boolean)         # True

print(2 == 3)             # False

code = 2==3 
print(code)               # False

print("hello" == "hello") # True      # Be careful not to confuse assignment (one equals sign) with comparison (two equals signs).

# Booleans can be compared too. 
a = 5 == 2+3 
b = 3 == 3 
c = a == b 
print(c)       # True

# Example:
print((2==2)+(3==3))  # 2

code = 2==3 
print(code+(2==2))    # 1 --> booleans are treated as 0 and 1

# Example
a=str(1==1) 
print(a)    # True
b=str(1==2) 
print(b)    # False
print(a+b)  # string concatenation --> 'True' + 'False' --> TrueFalse
print((1==1)+(1==2))    # Py converts each boolean to the int type, where boolean True becomes integer 1 and boolean False becomes integer 0.  
                        # prints the string form of integer 1
print(int(1==1))        # prints the string form of integer 1 --> Python automatically converts Print input to string

# Example:
string = "8" 
integer = 8 
print(string == integer)      # False 
print(int(string) == integer) # True 
print(string == str(integer)) # True



# COMPARISON
  # Another comparison operator, the not equal operator (!=), evaluates to True if the items being compared aren't equal, and False if they are.
print(1 != 1)                 # False
print("eleven" != "seven")    # True
print(2 != 10)                # True

  #  "!=" is the opposite of "==" 
  # "True" != "False" --> # True
  # "True" != "True"  --> # False
  
  # Comparison operators are also called Relational operators.
 
# You can compare strings, floats, and integers to each other. 
# A string compared to a float or integer will always show as Not Equal, 
# but a float and integer with the same value will show as Equal: 
print("2" != 2)  # True 
print(3.0 != 3)  # False 
    
# Example:
# == and is comparison in python explained
# remember that == means equality
# but is means identity
a = 5
b = 5.0
print(a == b)     # == compares values so it is true
print(a is b)     # here it compares values but also type and since one is int and one float the reult is false

# Example: 
"Trump"=="President"  # False
pigs == fly           # False
print(7 != 8)         # False


  # Python also has operators that determine whether one number (float or integer) is greater than or smaller than another. 
  # These operators are > and < respectively.
print(7 > 5)    # True
print(10 < 10)  # False
  # Different numeric types can also be compared, for example, integer and float. 
  #(> means greater than) 
  #(< means less than)   
  
a= 1==1   # True
b= 2!=3   # False
c= 7>6    # True
x= a + b + c  # T + F + T
print(x)  # 3

print(2==2.0000000000000001)  # True 
print(2==2.000000000000001)   # False
print(2==float(2.0000000000000001)) #False

print( 7 > 7.0 )  # False --> 7 and 7.0 are the same
print(7.0 == 7)   # True  --> Only difference is the type 7 is an integer 7.0 is a float

print(1*0.1==0.1)   # True 
print(2*0.1==0.2)   # True
print(3*0.1==0.3)   # False 
print(4*0.1==0.4)   # True
print(5*0.1==0.5)   # True
print(6*0.1==0.6)   # False
print(7*0.1==0.7)   # False
print(8*0.1==0.8)   # True
print(9*0.1==0.9)   # True
print(10*0.1==0.10) # False


  # The greater than or equal to, and smaller than or equal to operators are >= and <=.
  # They are the same as the strict greater than and smaller than operators, except that they return True when comparing equal numbers. 
print(7 <= 8)   # True
print(9 >= 9.0) # True

  # Greater than and smaller than operators can also be used to compare strings lexicographically 
  # (the alphabetical order of words is based on the alphabetical order of their component letters).
  # For example:
print("Annie" > "Andy") # True

  # The first two characters from "Annie" and "Andy" (A and A) are compared. 
  # As they are equal, the second two characters are compared. 
  # Because they are also equal, the third two characters (n and d) are compared. 
  # And because n has greater alphabetical order value than d, "Annie" is greater than "Andy".
  
# Conclusion:
# == equals logics 2==3 gives false as 2 is different from 3 
# != equals illogics 2 != 3 gives true 
# >= / > / <= / < indicates something larger, smaller or equals something else python compares integers and strings too. 
# "too">"to" is true as 3 letters is more than 2 letters. 
# "sea"<"tea" is true as t comes after s in the alphabetical order. Lexicographically a < d = True, g > m = False
# print(9.0000000000000001 == 9.0) True

# Example:
a = 4 == 4 
b = 3 != 3 
c = 8 < 6 
d = 5<= 7 
print("a =", a, "\nb =", b, "\nc =", c, "\nd =", d, "\nSum =", a + b + c + d) 
# Output:
# a = True 
# b = False 
# c = False 
# d = True 
# Sum = 2

# Example:
print( 8.7 <= 8.70 )  # True


# 1.Booleans there are two types a.True b.False 
# 2.Comparison Operators 
  # a)(== #this is used to compare the values of both the side ) eg: 2==2.0 which is True & 3==2 which is False 
  # b)(!= #this implies that the values on both sides are not equal ) eg: 2!=3 which is true & 3!=3 which is False 
  # c)( >< #they say that the value in one side is greater than the other or vice-versa) eg :2<3 which is true & 2>3 which is False 
  # d)(>= ,<= # they are same like the last on except in the fact that they turn true when the values in the both sides are equal) 
       # eg:3>=2 which is True 3<=3 which is also True
                                                                                                        
# The value of alphabets increases as we go from 'a' to 'z'. 
# Every capital alphabet also follow this rule and apart this all capital alphabets have lesser value than 'a'. 
print('a' >'b' )        # False 
print('A' < 'a')        # True
print('a' > 'B')        # True                                                                                                       
print("Love" > "Life")  # True  --> it is because "o" comes after "i" . 



