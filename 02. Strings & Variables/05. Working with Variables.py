# You can use variables to perform corresponding operations, just as you did with numbers and strings: 
x = 7
print(x)
print(x + 3)
print(x)
# As you can see, the variable stores its value throughout the program.


# Variables can be reassigned as many times as you want, in order to change their value.
# In Python, variables don't have specific types, so you can assign a string to a variable, and later assign an integer to the same variable. 
x = 123.456
print(x)

x = "This is a string"
print(x + "!")

# However, it is not good practice. To avoid mistakes, try to avoid overwriting the same variable with different data types.

# Example:
x = 7 
print('x'+'3')      # x3 
print(str(x) + '3') # 73 
print(x*'3')        # 3333333

# Example:
x = 2 
print(x) # output: 2 
a = x    # you created (defined) a second storage (variable). 
print(a) # output: 2 
x = 3 
print(x) # output: 3
print(a) # output: 2

# We declared that [x = 2]. In another instance, we declared that [a = x]. 
# We are not saying that [a] equals whatever happens to [x], only that [a] has the same value as [x] since we first declared [x]. 
# If we change [x] after the fact, only [x] will change; [a] still equals what we assigned it, which is [2], since [x] was equal to [2] when we assigned [a]. 
# Now that [x] equals [3], [a] still remains [2] since that was the value of [x] when we originally declared variable [a].
  

x="Hey " 
y="Jimi " 
z="Joe" 
print(x + y + z)  #  
z="Hendrix" 
print(x+y+z) 
a=3 
b=9 
c = a*b 
print(c) 
d=c/a 
print(int(d)) 
# output: Hey Jimi Joe Hey Jimi Hendrix 27 9
  

# Various ways to print variables in python  
Animal = "gorillas" 
Food = "bananas" 
print("I think " + Animal + " like " + Food + "!") # 1st 
print("I think {0} like {1}!".format(Animal, Food)) # 2nd
print(f"I think {Animal} like {Food}!") # 3rd



# Two types of variables in python 
  # 1) Local variables: Local variables are the variables that declared inside the function and have scope within the function.  
  # 2) Global variables: Global variables can be used throughout the program, and its scope is in the entire program. 
  # We can use global variables inside or outside the function. A variable declared outside the function is the global variable by default.

  
  
  
