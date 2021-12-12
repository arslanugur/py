# To ensure some code runs no matter what errors occur, you can use a finally statement. 
# The finally statement is placed at the bottom of a try/except statement. 
# Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks.
try:
    print("Hello")                              #
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")                    #
finally:
    print("This code will run no matter what")  #
#

# The finally statement will run even if there is an uncatched exception. 
# This can be handy for instance to assure that all used files will be closed or to delete objects. 
try: 
  print("1"+1)            # TypeError
except ZeroDivisionError: 
  print("Divided by zero") 
finally: 
  print("This code will run")     #
  print("This code will NOT run") #
#


# Example:
try: 
  print("Hello")                                #
  print(1 / 0) 
  print(2*3) 
except ZeroDivisionError: 
  print("Divided by zero")                      #
finally: 
  print("This code will run no matter what")    # 'print (2 * 3)' is not executed since an error is found in 'print (1/0)'
#


# Example:
try:
	print(1 / 0)
except ZeroDivisionError:
	print("Divided by zero")    #
finally:
	print("This code will run no matter what")  #

print("... and the program continues because the ZeroDivisionError was handled!")   #

print("\n-------------------------")    #
print("Let's go to the next try:")  #

try:
    print(5/0)                                      # ZeroDivisionError
except TypeError:
    print("Wrong error type")
finally:
    print("This code will also run no matter what") #

print("This code cannot be reached anymore, because the ZeroDivisionError was not handled and the program crashed!")

# https://stackoverflow.com/questions/11551996/why-do-we-need-the-finally-clause-in-python


# the finally code should be used: 
# when there are commands that must be executed to make sure that important steps are made like closing databases, in case of an unexpected error. 
# In case of the expected error (Zerodivision) the program keeps on running, even after the finally code, 
 
try: 
  print("Hello") 
  print(1 / 0) 
except ZeroDivisionError: 
  print("Divided by zero") 
finally: 
  print("This code will run no matter what") 
  print("programm will proceed") 

# but in the second half of my example, when an unexpected error occurs, only the finally code is run and the rest of the program is aborted.
try: 
  print("Hello") 
  print(1 / "0") 
except ZeroDivisionError: 
  print("Divided by zero") 
finally: 
  print("This code will run no matter what") 
  print("program aborted")
#

# Example:
try:
  print(1)  # 
except:
  print(2)
finally:
  print(3)  #
#


# Example:
# 'try:' part will always run first, and then you have two situation: 
#  1. If "try" part executed correctly, "except:" part will be ignored 
#  2. If any error in "try:" part, it will still run until error happened. 
# when error happened, the rest of "try:" part will be ignored, and then jump into "except:" part immediately. 
# No matter what happened(at both situations), the "finally" part always run. (even some error also happened in 'except' part...) 
# The 'finally' part runs looks like the key word 'finally' just doesn't exist, but still some different. 
# If try/except crashed, the rest code won's execute, but "finally" will still execute before the code crashed. 
# Example:
try: 
  print(1)      # 
  print(2/0)    # ZeroDivisionError
  print(2) 
except: 
  print(3/0)    # ZeroDivisionError
finally: 
  print(4)      # 4 will always printed out
  print(5)      #
#


# Code in a finally statement even runs if an uncaught exception occurs in one of the preceding blocks.
try:
    print(1)                            #
    print(10 / 0)                       # ZeroDivisionError
except ZeroDivisionError:
    print(unknown_var)                  # NameError
finally:
    print("This is executed last")      # 
#





