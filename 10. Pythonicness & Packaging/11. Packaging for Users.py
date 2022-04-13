# SECTION 1
# The previous lesson covered packaging modules for use by other Python programmers. 
# However, many computer users who are not programmers do not have Python installed. 
# Therefore, it is useful to package scripts as executable files for the relevant platform, such as the Windows or Mac operating systems. 
# This is not necessary for Linux, as most Linux users do have Python installed, and are able to run scripts as they are.

# For Windows, many tools are available for converting scripts to executables. 
# For example, py2exe, can be used to package a Python script, along with the libraries it requires, into a single executable.
# PyInstaller and cx_Freeze serve the same purpose.

# For Macs, use py2app, PyInstaller or cx_Freeze.

# Which of these does not convert Py scripts to Windows executables? ---> PyExecutable

# Which of these isn't a file used in creating a package? --> __py2exe__.py

# What is PEP 8? ---> Guidelines for writing code

# Example:
def func(**kwargs):
  print(kwargs)
  print(kwargs["zero"])
  
func(a = 0, zero = 8) # OUTPUT: {'a': 0, 'zero': 8} 8 
# kwargs is a DICTIONARY with 2 Key:Value pairs - the FIRST has string "a" as its Key and Value 0, 
# whereas the SECOND has string "zero" as its Key and Value 8. 
# kwargs["zero"] RETURNS to the Value of the item in the kwargs dictionary that's got its Key as string "zero". Hence, kwargs["zero"] RETURNS 8


# **kwargs is the keyword argument. It takes both a and zero. They both are made keys of the dictionary kwargs and the respective values. 
# The print statement prints the value of the key 'zero'. Thus the anz is 8


# Example: What is sum of the numbers printed by this code? 
for i in range(10): 
  try: 
    if 10/i == 2.0:
      break
  except ZeroDivisionError: 
      print(1)
    else:
      print(2)
# 9           it raises zeroDivision error and prints 1. Then it continues to print 2 another 4 times. So answer is 9
# Why 10/i is not generating any zeroDivision error? 
# i is in range(10) which is equal to the tuple (0, 1, ..., 9), so i will be equal to 0 in the first iteration that will raise to zeroDivision error. 
# It will generate zero division exception , which will be caught and as a result print(1) will get executed
# we have for i in rang(10) so for loop wl execute until i==10 attains or an break statement gets encountered 
# so at 1st when i=0 , an ZeroDivisionError gets occurred and "" 1 "" is printed and then i gets incremented
# so when if 10/i == 2.0 is checked ,....the if cond is false 
# so else part gets executed hence 2 is printed and then i is incremented, 
# the same occurs till i=5 where if cond gets true and break statement gets executed ... so 1 + 2 + 2 + 2 + 2 = 9

# for range(10) = [0,1,2,3,4,5,6,7,8,9] Now if 10/0 == 2 then print(1) then looping... 
# 10/1 == 2 print(2) again 10/2 == 2 print(2) again 10/3 == 2 print(2) again 10/4 == 2 print(2) again 10/5 == 2 here conditon is True. 
# so break Now 1 + 2 + 2 + 2 + 2 = 9

# for i=0 we will get exception, thus 1; 
# for i=1 we will get false condition, so "else" will be executed, thus 2; 
# for i=2 we will get false condition, so "else" will be executed, thus 2; 
# for i=3 we will get false condition, so "else" will be executed, thus 2; 
# for i=4 we will get false condition, so "else" will be executed, thus 2; 
# for i=5 we'll finally get true condition, so we will execute "break". SUM is equal to 9.

# For i in range(10) try: if 10/i==2: break except ZeroDivisionError: print(1) else print(2) 
# Solution: range(10)=0,1,2,3,4,5,6,7,8 and 9. 
# In the code, the program breaks only when 10/i==2, which is 5. 
# Therefore, the program will run from 0 to 4. And, if a division by zero, print 1 else print 2. 
# So, for i=0, output= 1 for i=1, output=2 for i=2, output=2 for i=3, output=2 for i=4, output=2 
# Therefore, the sum of numbers printed by the code= 1+2+2+2+2=9.


# Example: to Swap the variable values with one single statement.
a=7; b= 42
a,b = b,a
# The b, a variables on the right side are treated as a tuple, in this case (42,7). 
# You can unpack a tuple by defining on the left side the variables that will hold the values for each one.


