# To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
# The try block contains code that might throw an exception. 
# If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. 
# If no error occurs, the code in the except block doesn't run.
# For example:
try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")      # 
    print("due to zero division")   #
#

# In the code above, the except statement defines the type of exception to handle (in our case, the ZeroDivisionError).

# Example:
# try except example with 2 except cases 
# remove int() in num lines to provoke TypeError 
try: 
  num1 = int(input('Provide num1 ?')) 
  num2 = int(input ('Provide num2 ?')) 
  print (num1 / num2) 
  print("Done calculation") 
except ZeroDivisionError: 
  print("An error occurred") 
  print("due to zero division") 
except TypeError: 
  print ("You didn't type a number")
# 

# Example:
try:
  variable = 10
  print(10 / 2)   # 5.0
except ZeroDivisionError:
  print("Error")
print("Finished") # Finished


# The reason why its printing 5.0 and finished its because there is no exception(error) in the try code,So the except code and anything under it wont be excuted. 
# But if you check the second print function, its not under the except code, so it will be excuted. Check its Identation. 



# A try statement can have multiple different except blocks to handle different exceptions.
# Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
try:
    variable = 10
    print(variable + "hello")   # variable is integer type, but must be string type to get printing (variable+'hello')
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred") #
# the right code must contain retyping variable from int type to str type before adding: print(str(variable)+'hello')

#except TypeError: 
#  print("GETTING TYPE ERROR")
#except ValueError: 
#  print("VALUE ERROR OCCURED") 
#finally:
#  print("PROGRAM FINISHED !")


# Example:
try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")  #
#


# An except statement without any exception specified will catch all errors. 
# These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
# For example:
try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")  #
#

# Exception handling is particularly useful when dealing with user input.
# https://realpython.com/the-most-diabolical-python-antipattern/


# Example:
try: 
  word = "spam" 
  print(word / 0) 
except (ValueError): 
  print("Bad value") 
except (ZeroDivisionError): 
  print("0") 
except (TypeError): 
  print("Bad type") #
except: 
  print("An error occurred") 
finally: 
  print("Done!")  #
#


# Example:
pin = input() 
try: 
    p = int(pin) 
    print('Pin code is created') 
except ValueError: 
    print('Please enter a number')
#


# Example: Second solution 
pin = input() 
try: 
    p = int(pin) 
    print('Pin code is created') 
except ValueError: 
    print('Please enter a number')
#


# Example:
try:
  num1 = input(":")
  num2 = input(":")
  print(float(num1)/float(num2))
except:
  print("Invalid input")
#


# Example: Assertion Error
try:
    print(1)            # 
    assert 2 + 2 == 4
    print(2)            #
    assert 1 + 1 == 3
    print(3)
except AssertionError:
    print('Oops!')      #
#    


