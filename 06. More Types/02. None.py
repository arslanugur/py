# The None object is used to represent 'the absence of a value'.
# It is similar to null in other programming languages.
# Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable.
# When entered at the Python console, it is displayed as the empty string. 
print(None) # None

# empty     = a blank sheet of paper 
# None/null = no paper

# None is a special value that says "no object here". 
# Things like "if" simply interpret that to mean False. 
# You can assign None to variables, as you can with other values, but you don't have to. 
# Also, note the following code with its output. 
if None: 
  print("None got interpreted as True") 
else: 
  print("None got interpreted as False") # Output: None got interpreted as False
#


# Example:
actor = ["Sylvester","Star"] 
def func(): 
  print("The name is:") 

age = func()                                    # the function is not returning any values. So printed as None
print(actor[0] + " " + actor[1][:3] + str(age)) 
# Output: The name is: Sylvester StaNone


# The None object is returned by any function that doesn't explicitly return anything else. 
# Example:
def some_func():
    print("Hi!")  # Hi!

var = some_func()
print(var)        # None


# A Different Way
def some_func():
  print("Hi!")    # Hi!
  return("End")   # End

var = some_func() 
print(var)        



# To understand, I add return value 
def some_func(): 
  print("Hi!") 
  return("finish")  # When print is executed, we return value "finish" 
var = some_func()   # We call the function and store in the variable var 
print(var)          # We just print the return value "finish" of some_func() Result: Hi ! 
# var = some_func() finish 
# return value ------ 
# Let's try with the some_func() inside print def some_func(): print("Hi!") return("finish") 
# When print is executed, we return value "finish" some_func() 
# We call the function print(some_func()) 
# we call again the function that return "finish" Result: Hi! 
# some_func() Hi! #print(some_func()) finish #return value 
# The point is with print(var), we don't call the function, we just collect the result of variable 
# When we don't put return("finish") we return "None" because we don't have a return value 
# print() function is just a way to watch how the function works, what we can't see.


# here is the tricks: 
# check carefully that the some_func() doesn't have a return statement so it's returning none object.. 
# so when var = some_func() is called some_func is called first(so it prints hi) then it is returning none..


# If the function actually does a return then the var will print. 
def some_func(): 
  print("Hi!") 
  return("Ho!") 

var = some_func() 
print(var) 
print("2nd var: " + var) # Output: Hi! Ho! 2nd var: Ho!



# NOTE: "print" does not return anything. So the output is always "NONE".
#       Always test the output if you wanna make sure it doesn't return a value.
# Example:
foo = print()
if foo == None:
   print(1)         # 
else:
   print(2)
#



# Example: 
hoo = '' 
poo = print('any text')     # any Text
foo = print() 
print(hoo == None)          # False
print(poo == None)          # True
print(foo == None)          # True
# 1. hoo is assigned to empty string. But this is string! An object which not equals to None. 
# 2. poo is assigned to what print function returns. But it returns nothing! 
#    So the text was just printed, and the variable poo is not the text (a string) but None. 
# 3. Same thing as in the second point(2.), function print() returns nothing. And in this case it prints nothing, only transits to new line.



# print function always returns nothing, even it has a value between brackets. 
# Because this function only prints value and doesn't assign value to the variable. 
# x = print() 
# print nothing and x has no value x = print(5) 
# print 5 and x has no value 
# x = print("Hi") # print Hi and x has no value




# Example:
print('------None Playing-------')

x = 'None'
print(x)
# x is a variable with a value (type string) assigned.
y = None
print(y)
# y is a variable with the ¿object? None assigned. Its the same to say "empty". None represents the nothing. y have nothing! 

if x == y:
    print('yes!')
elif x == None and not y == None:
    print('x is empty. y is not')
elif y == None and not x == None:
    print('y is empty. x is not')
else:
    print('Incorrect. The answer is line 18')
 
 
print('------Bool Function  Playing---------')


#a cool boolean function use:
if bool(y) == False:
    print('y is the nothing, comfirmed')
if bool(x) == True:
    print('and x is something, confirmed')
 
 
print('-----Empty things Playing----------')


#Lets probe with "some" empty value...
if bool([]) == True:
    print('OMG...a empty list is something!, is not nothing')
else:
    print('Wait...a empty list is really nothing? Simple: If your object called life is empty, you dont have nothing.')
# I probe the same writting h = [] and bool(h) == True and gives me the same...


print('------Objects Playing------------')

#I refuse to deprime, so...
if([]==None):
    print('Well...at least a empty object is the same that a None object... ')
else:
    print('Nope. Theyre differents objects. They cannot be compared. Its like say 4==[4]')

#And what if...?
h = [None]
if h == None:
    print('I break the system')
else:
    print('I dont break the system. Why?')
#h is a list with nothing inside. nothing is nothing. 

#going deeper...
if (h[0] == None):
    print('It is obvious!. but can you add a object to another? yes, the same way you can put a list inside a list')
else:
    print('See? The answer seems to be Yes!')
    
#and deeper...    
if (bool(h[0])==False):
    print('yeah. cause bool(None)==False)')
else:
    print('For what??? Why??')

    
print('-------Strange Things Playing------')

if bool([])==bool(None):
    print('Its the same to say False==False, right? Cause a bool gives false if the argument is empty')
else:
    print('If this is printed, I really need help')

### CONCLUSIONS OF THE GAMEPLAY
# None is a object that represent emptyness, or "vaccum", or nothing.
# bool() is a function who returns True if the argument is NOT empty. And false if the argument is empty. None is empty by definition. 
# None is a object, and its different from any other object, empty or no. 
# To see it like vacuum. With nothing inside, but vacuum itself. 



