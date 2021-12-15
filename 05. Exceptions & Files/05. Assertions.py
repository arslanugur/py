# An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
# An expression is tested, and if the result comes up false, an exception is raised.
# Assertions are carried out through use of the assert statement.
# Example:
print(1)  #
assert 2 + 2 == 4
print(2)  #
assert 1 + 1 == 3
print(3)  # AssertionError

# Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.

# You should use assertions when you are trying to catch your own errors, and exceptions when trying to catch other people's errors. 
# You should use exceptions to check the preconditions for the public API functions, and whenever you get any data that are external to your system. 
# You should use asserts for the functions or data that are internal to your system.

# https://www.tutorialspoint.com/python/assertions_in_python.htm
# https://en.m.wikipedia.org/wiki/Assertion_(software_development)

# Example:
def my_age(x): 
  assert x > 0 #here it will check whether age is negative or not, if negative it will halt the code 
  print("my age is: ", +x) 

my_age(20) # my age is: 20  (if you pass negative values accidently then it will show assertion error) my_age(-20) # assertion error


# Example: What is the highest number printed by this code?
print(0)
assert "h" != "w"   # the statement "h" != "w" equals True in boolean logic. 'h' != 'w' is not equal 
print(1)            #
assert False
print(2)            # AssertionError
assert True
print(3)

# Example:
print(1)            #
assert 2 + 2 == 4 
print(2)            #
assert 1 + 1 == 2 
print(3)            #


# Example:
assert 2 + 2 == 4 
print(2)          # 2
assert 1 + 1 == 3 
print(3)          # Assertion Error


# Example:
temp = -10
assert (temp >= 0), "Colder than absolute zero!"  # Assertion Error

# AssertionError exceptions can be caught and handled like any other exception using the try-except statement, 
# but if not handled, this type of exception will terminate the program.

# Example:
try: 
    temp = -10 
    assert (temp >= 0), "Colder than absolute zero!" 
except: 
    print("Error Bypassed") #
#


# Example:
def number_comparison(num1,num2): 
    if num1>num2: 
        return num1 
    elif num1<num2: 
        return num2 
    elif num1==num2: 
        return "equal" 
    else: 
        return "error" 
        print(number_comparison(76,78)) 

def checking_code(): 
    assert number_comparison(1,2)==2 
    assert number_comparison(5,3)==5 
    assert number_comparison(1,1)=="equal" 
    print("your code is right") # 
    
checking_code()

# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-raise_stmt
# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assert_stmt.

# Example: To check all the statements
age = 50
assert (age >= 18), "Access granted"
assert (age == 50), "last year of access"
assert (age != 65), "unknown error"
assert (age <= 75), "contact admin"
assert (age <= 50), "error"
assert (age == 16), "under age!"  # Assertion Error


# Example: to define a function that takes one argument. Assert the argument to be positive.
def my_func(x):
  assert x > 0, "Error!"
  print(x)
# assert does nothing if x > 0 is True and the program continues, if x > 0 is False it raises the exception "Error!"
my_func(-1) # Assertion Error
my_func(1)  # 1


# Example:
while True: 
    x = input("Enter a bigger number than 0: ") 

    try: 
        assert float(x) > 0 
        print("Yes, %s is bigger than %d." % (x, 0)) 
    except ValueError: 
        print("You did not enter a number.") 
    except AssertionError: 
        print("It is not bigger than 0.")
#


