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

# Examples:
print((2==2)+(3==3))  # 2

code = 2==3 
print(code+(2==2))    # 1 --> booleans are treated as 0 and 1






a=str(1==1) print(a) b=str(1==2) print(b) print(a+b) print((1==1)+(1==2)) print(int(1==1)) a=str(1==1) The value of a is the string 'True' print(a) Prints True without quotes b=str(1==2) The value of b is the string 'False' print(b) Prints False without quotes print(a+b) Prints the string concatenation 'True' + 'False' i.e. it prints TrueFalse without quoted print((1==1)+(1==2)) When adding booleans, I think Python converts each boolean to the int type, where boolean True becomes integer 1 and boolean False becomes integer 0. So this prints the string form of integer 1 without quotes print(int(1==1)) Prints the string form of integer 1 (I think Python automatically converts Print input to string)




string = "8" integer = 8 print(string == integer) # False print(int(string) == integer) # True print(string == str(integer)) # True




a = true Error 
>>> b = false Error 
>>> a = True True 
>>> b = False False 
>>> a == 1 True 
>>> a == 2 False 
>>> b == 0 True 
>>> print(a) True 
>>> print(b) False 
>>> print(b==False) True 
>>> print(b=False) Error 
>>> print (a+b) 1 
>>> a + b 1 
>>> a + 10 11 
>>> c= a+b==1 
>>> c True 
>>> d= a+b >>> d 1 


