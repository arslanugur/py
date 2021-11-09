# CONCATENATION
# As with integers and floats, strings in Python can be added, using a process called concatenation, which can be done on any two strings. 
print("pen"+"pineapple"+"apple"+"pen") # penpineappleapplepen
print("pen"+"pineapple "+"apple"+"pen") # penpineapple applepen

# Even if your strings contain numbers, they are still added as strings rather than integers. 
print("2" + "2")  # 22

# Adding a string to a number produces an error, as even though they might look similar, they are two different entities.

# Example:
x = '2'
y = '2'
print('2'+'2')  # 22
# or
print (x+y)     # 22 

# why add two strings together and not just type two words?
# think about an app that takes a string "the time is" and then concatenates that with a variable that is the time, say "5.30", 
# then you can add them together and it gives you the time. 
# You can't keep updating your sentence with a string "the time is blah" every time the time changes can you?

print(1+2+2)}      # 5
print("1"+"2"+"5") # 125

# Example:
print("example"+'123'+'@'+"email"+".com") # example123@email.com 


# Example:
x = 10
y = 5
print ("sum of",x,"and",y,"is",x+y) # sum of 10 and 5 is 15





# STRING OPERATIONS
    # Strings can also be multiplied by integers. This produces a repeated version of the original string. 
    # The order of the string and the integer doesn't matter, but the string usually comes first. 
print("seven" * 3)  # sevensevenseven
print(3 * '7')    # 777 (as str, not int)

    # Strings can't be multiplied by other strings. Strings also can't be multiplied by floats, even if the floats are whole numbers.
# str + int → Error 
# str * str → Error 
# str + str → strstr 
# str * int → strstrstr...

print("Python" * 3)                   # PythonPythonPython 
print("Python\n" * 3)                 # Python Python Python
print("Python\nC" * 3)                # Python CPython CPython C
print("Python\nC" * 3 + "Python")     # Python CPython CPython CPython
print("C"+"Python\nC" * 3 + "Python") # CPython CPython CPython CPython 

 
print('spam' * 3)     # spamspamspam
print(7 * "72")       # 72727272727272
print("hell ya" * 0)  #
print("hi" *2 *3)     # hihihihihihi
print ('hi' *2 **3)   # hihihihihihihihi


