# Functional programming is a style of programming that (as the name suggests) is based around functions.
# A key part of functional programming is higher-order functions. 
# We have seen this idea briefly in the previous lesson on functions as objects. 
# Higher-order functions take other functions as arguments, or return them as results.
# Example:
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))  # 20

# The function apply_twice takes another function as its argument, and calls it twice inside its body.


# Understanding this problem requires a basic understanding of an algebraic concept called "composition of functions." 
# Think back to algebra class in high school where you had to evaluate f(g(3)). 
# You first need to evaluate the inner function g, with an input of 3. 
# The output/result of g(3) becomes the input of the outer function f. 
# i.e. given f(x) = x + 2 and g(x) = 2x - 1 evaluate f(g(3)) 
# First, evaluate g(3). g(3) = 2(3) - 1 g(3) = 6 - 1 g(3) = 5 
# Second, take the result/output of g(3) which is 5, and plug it into the outer function f. 
# f(5) = (5) + 2 f(5) = 7 
# Thus, f(g(3)) = 7 Using that same understanding of composition of functions reconsider the problem below (I added line numbers). 
# 1. def apply_twice(func, arg): 
# 2. return func(func(arg)) 
# 3. 4. def add_five(x): 
# 5. return x + 5 
# 6. 7. print(apply_twice(add_five, 10)) 

# We have to work backwards to understand this. 
# On line 7, we are calling the function “apply_twice”, which has two arguments: a call to another function ”add_five” and the number 10. 
# Now jump to line 1. It becomes “ def apply_twice(add_five,10). 
# Line 2 becomes “return func(add_five,10)” 
# Since a function is within the parentheses, right away we jump to another function, add_five, on line 4. 
# This becomes “def add_five(10):” Line 5 becomes “return 10+5”. 
# So now we have the value of 15. Jumping back to line 2, we have “return func(15)”, which becomes “add_five(15)”. 
# We jump back to Line 4 and it becomes “def add_five(15):”, and line 5 becomes “return 15+5”, or 20. 
# So line 2 returns 20, which becomes the value of line 1, which is printed in line 7.

# In line 1 and 2 as per given example, here, func = add_five arg = 10 
# Let's consider the line 4 and 5, according to the function, 
# when u define the argument 'x', it will be added to 5; add_five = x+5 
# so, def apply_twice(add_five, 10) return add_five(add_five(10)) 
# calculating line 2 as per example add_five(add_five(10)) =5 + (5 + 10) =5 + 15 =20 so the answer is 20


# Here "func" is actually add_five (x) as it's put as an argument when apply_twice () is called in print (). 
# The second argument "arg" is replaced with an integer "10" in apply_twice (). 
# Now add_five () wich adds "5" to value of its argument. 
# Well , it gets argument in the following block; that's the 1st block in our code. 
# def apply_twice (func, arg): Return func (func (arg)) This block makes 10 as argument for add_five () as func is actually add_five (). 
# Our *print* statement "print (apply_twice(add_five, 10))" replaces func with add_five (). 
# Now See "return func (func (arg))" Here "arg" is replaced with 10 and func (add_five) adds five , you will get 15. 5 is added again to 15 . Result is 20.
# "return func (func (arg))"
# func (add_five (10))
# func (15)
# add_five (15) # 20 

# Example:
def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))  # 16

# Explanation:
# There are two functions: 
# mult = x*x
# test = x*x(mult) 
# When you compile it this is how it happens! 
# (mult, 2) = 2*2 (mult, 2) = 4
# test(mult, 2) = x*x(4) = 4*4 which is = 16. --> summary: x*x(x*x(2))
# Output is 16 because 2*2 = 4 taking 4 as argument 4*4 = 16
# print(test(mult, 2)) = (mult(mult, 2)) 
#                        (mult(2 * 2)) = (mult( 4)) = (4 * 4) = 16 

# Explanation:
# test(mult, 2) → mult(mult(2)) → mult(2 * 2) → mult(4) → 4 * 4 → 16 Hence, print(test(mult, 2)) --> 16
# mult is the same as "func" in the argument of the "test" function.
# Replacing we have: test(mult(mult(2))) # Now just use the second function "x*x" mult(mult(2)) mult(2*2) # 4 mult(4*4) # 16

# Explanation:
def test(function,argument):                            # def test (multiple,2): 
    return function(function(argument)                  #    return multiple(multiple(2))                    return multiple(2*2)            def multiple (2): 2 * 2

def multiple(x): x * x 

print(test(multiple, 2))                                # function(function(argument)) == > multiple(2*2) ===> multiple(4) def multiple(4): 4*4 the final answer is 16 


# Mathematically correct way is this.
# y = f2(f1(x)) 
# x = 2 
# f1(x) = x * x = 2 * 2 = 4 
# y = f2(f1(x)) = f1(x) * f1(x) = 4 * 4 = 16


# SECTION 2
# Pure Functions
# Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that depends only on their arguments.
# This is how functions in math work: for example, The cos(x) will, for the same value of x, always return the same result.
# Below are examples of pure and impure functions.
# Pure function:
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)
#

# Impure function:
some_list = []

def impure(arg):
  some_list.append(arg)
# The function above is not pure, because it changed the state of some_list.

# If the answer to all questions is "yes", your function is pure. 
# 1. Does my function depend only on its arguments and nothing else? OR Does my function always return the same result given the same arguments? 
# 2. Can I run my function anywhere in the script without causing any trouble or side effects whatsoever? 
# 3. Can I run my function with the same arguments many times and still return the same result each time? 
# 4. Is it true that my function does not change anything outside it, but only returns something? 
# 5. Can my function be used by other functions or scripts with equal success?

# Impure function change the state of a variable outside the function. 
# For instance, in a pure function
number1 = 3 
number2 = 2 
def pure_function(x,y): 
    temp=x+2*y 
    return temp/(x*2+y) 

print(pure_function(number1,number2)) 
# This function doesn't change the value of num1 and num2 so it is a pure function 
# However, the impure function does change the state of a variable outside the function.
# For instance, 
some_list=[] 

def impure_function(arg): 

some_list.append(arg) 

print(impure_function(arg='He is the best player'))
print(some_list) 
# The function change the state of the some_list and add a string to it. 
# You can also print the result of the list. PS: append function does not return anything! 

# https://www.quora.com/Whats-the-difference-between-pure-and-non-pure-functions-in-programming

# Example:
some_list = [] 
def impure(arg): 
    some_list.append(arg) 

impure(10)
print(some_list) # Output: [10] 
impure(10) 
print(some_list) # Output: [10, 10] 
# Every time you call the function with an argument it is modifying the original list instead of only performing operation for that specific call out. 
# The list now has two elements yet it started with zero elemnts.
# Entering the same arguments is providing different results.
def pure_function(x, y): 
    temp = x + 2*y 
    return temp / (2*x + y) 
    print(pure_function(3, 4)) # Output: 1.1 
    print(pure_function(3, 4)) # Output: 1.1 
# As you can see, entering the same arguments provides the same same results.
# Pure functions do not affect variables. it just returns a value while impure functions can change the state of a variable without returning anything.
# Impure functions can have a return statement. has side effects returns a value that doesnt depend only on their argument
# 1) a pure function can be used safely elsewhere. 
# 2) a pure function can be refactored without worrying about other parts of the program. As long as you aren’t changing what it returns. 

# Example: Pure Function
def func(x):
  y = x**2
  z = x + y
  return z
#
# simplifies to def function(x): 
# y = x**2 z = x + x**2 return z
# simplifies even further to def function(x): 
# y = x**2 
# z = x + x**2 return x + x**2 
# def function(x): return x + x**2 depends only on x, so it is a pure function.


# Example:
z = "I didn't changed" 
y = "I also didn't changed" 
def func(x): 
    y = x**2 
    z = x+y 
    return z 

func(5) 
print(z)    # I didn't changed
print(y)    # I also didn't changed
print(func(5)) # 30
# By using this code you can see clearly that the global "z" and "y" weren't changed by the values of the local "z" and "y". 
# The function is returnung only the value 30. It doesn't assign that value to the global variable "z". 
# If you want to change the global variable with that value, than you will need to do it like this: z=func(5) Conclusion: func(x) is pure

# The 'y' and 'z' variables are local inside the function only, even if variables with the same names are defined and used in other places outside the function. 
# The doubters are confusing the situation and never checked their facts. The function is 100% pure. 
# Code: 
z = 0 
y = 0 
x = 2 
def func(a): 
    y = a**2 
    z = a + y 
    x = 123 
    print("within func: z = " + str(z) + ", y = " + str(y) + ", x = " + str(x)) 
    return z 

print("prev outside func: z = " + str(z) + ", y = " + str(y) + ", x = " + str(x)) 
print(func(x)) 
print("post outside func: z = " + str(z) + ", y = " + str(y) + ", x = " + str(x)) 
# Outputs:
# prev outside func: z = 0, y = 0, x = 2
# within func: z = 6, y = 4, x = 123
# 6
# post outside func: z = 0, y = 0, x = 2


# SECTION 3
# Using pure functions has both advantages and disadvantages.
# Pure functions are:
# - easier to reason about and test. They are easier to analyze
# - more efficient. 
#   Once the function has been evaluated for an input, 
#   the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. 
#   This is called memoization. https://en.wikipedia.org/wiki/Memoization
# - easier to run in parallel. 

#   Imagine you have to execute sum=f(30)+f(40). 
#   Since pure functions don't change the value of the variables outside it (ergo the call of f(30) is absolutely independent from the call of f(40) ), 
#   You may execute both in parallel, that is to mean, at the same time in different hardware (different computers, processors, etc), 
#   speeding up the execution compared to executing one after the other

#   pure functions are difficult to write


# The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O (Input/Output), 
# since this appears to inherently require side effects.
# They can also be more difficult to write in some situations.

# Think of pure math functions that will give the same result everytime you input the same numbers. 
# Example; x/y = z, now if 4/2, it will always equal 2. It's use is self explanatory. 
# Impure math functions can change everytime a new parameter is introduced.
# For example (num x/num y) = numz, so what if y = 1 USD and y = x GBP?, the return will always be different, thus impure. 
# This example is also how and why, impure math functions are equally used in real life programming. Exchange rates are useful real world examples of variables that often change.


# Memoization Explained:
# Memoization is whereby the result of a previous section can be referred and used to get the result of the next without having to go through a lot of work. 
# Example: 
#                   If you write 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 and asked for an answer, you will take time to do that and get 10 
# If I add another +1 at the end 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 
# You will instantly say 11 That is memoization. You will not go back to adding the whole list of 1s. 
# Practical example can be in calculation of factorials. 
# Once you know that 3! is 6 (ie 1 * 2 * 3) then if I asked you 4! you simply take 3! * 4 = 24 other than doing it over again as 1 * 2 * 3 * 4 
# Now let us apply Memoization: 9! = 362880 find 10! Answer: Simply 9! * 10 = 3628800

# Easiest Explanation:
# function f is pure, and g is impure, because isTuesday() might give a different result based on when you're running the program. 
# def f(x): return x + 1 def g(x): if isTuesday(): return x + 1 else: return x


# "Memoization" is the general term for any operation that stores, or "memoizes," previously computed values in order to avoid having to compute them again and reduce running time. 
# In concrete programming applications, the term "tail-recursion" is often used to refer to the specific use-case in which the return value specifically includes the memoized data. 
# This might seem like a pedantic distinction, but the difference is clear if you understand runtime environments, and has important performance implications. 
# Every func call generates what's called a "stack frame" in memory that contains all of the values necessary to describe a function and return to the instruction that called it
# If a recursive function returns a subsequent function call for a value that hasn't yet been computed, then the calling function's stack frame must be kept alive and in memory. 
# There is tremendous computational overhead for this task, which is then compounded over many (potentially even thousands, in this era of Big Data) functions


# Why we are learning about advantages of each as if we have a choice which to use? 
# It looks to me like it depends on the kind of input you expect. Why use impure functions to calculate math? No?
# It depends in how you structure your application. A small JS app with really impure functions is built because no plan. 
# I just wired everything together across functions because i was trying to solve a problem and learn programming at the same time. That's my amateur understanding anyway.

# Imagine you have to execute sum=f(30)+f(40). 
# Since pure functions don't change the value of the variables outside it (ergo the call of f(30) is absolutely independent from the call of f(40)), 
# you may execute both in parallel, that is to mean, at the same time in different hardware (different computers, processors, etc), 
# speeding up the execution compared to executing one after the other.

# PURE FUNCTIONS are hard to write because they only depend on their own values, so programming a complex functionality using a IMPURE FUNCTION requires less lines of code? 

# In practice, I think the reason pure functions are harder to write than impure functions is that 
# they require you to conceptualize what you're trying to accomplish in your code in a more abstract, generalized way, rather just modifying data directly. 
# If you "just want it to work" it can feel quicker to write impure because it's accomplishing that one task you're focused on in the moment. 
# A pure function, while it might take longer to write, on the other hand should be reusable and save time later on while also cutting down on repeated code.

# Pure functions don't change any states and are entirely dependent on the input, they are simple to understand. 
# The return value given by such functions is the same as the output produced by them. 
# The arguments and return type of pure functions are given out by their functions signature.



