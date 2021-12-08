# Although they are created differently from normal variables, functions are just like any other kind of value.
# They can be assigned and reassigned to variables, and later referenced by those names. 
def multiply(x, y):
    return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))  # 28

# The example above assigned the function multiply to a variable operation. Now, the name operation can also be used to call the function.
# Example:
def multiply(x, y): 
  return x * y 

a = 4 
b = 7 
operation = multiply 
fish = operation 
chicken = fish 
hi = chicken 
print(hi(a, b)) # 28

# Example:
def number(x,y): 
  return x * y 

a = 10 
b = 5 
old = number 
year = old
print(year(a,b)) # 50

# Example:
def shout(word):
   return word + "!"  # returns the argument inputed with an exclamation mark 

speak = shout
output = speak("shout")
print(output) # shout!


# ** Functions can also be used as arguments of other functions.
def add(x, y):                            # if you call the "add" function, it will return the sum of the two parameters
    return x + y
    # The "do_twice" function takes the same two value parameters "x" and "y" and is working with these values. It also takes a function as third parameter.
                                          # func is simply another variable
def do_twice(func, x, y):                 # the function do_twice takes a function as its argument and calls it in its body
    return func(func(x, y), func(x, y))
# Inside "do_twice" the parameter-function "func" (in the following case the "add" function) is called three times

a = 5
b = 10
#"do_twice(add, a, b)" could be seen like: "add(add(a,b), add(a,b))" --> which will turn out to: add((5+10), (5+10)) --> add(15, 15)
print(do_twice(add, a, b))  # 30

# Example:
# func is replaced by add in memory as "func" is just a variable which is storing "add" when passed as arguments. 
def multiply(a,b): 
    return a * b 

operation = multiply 
print(operation(1,2)) # 2

# Example: to pass the function "square" as an argument to the function "test":
def square(x):
  return x * x

def test(func, x):

  print(func(x))

test(square, 42)  # 1764


