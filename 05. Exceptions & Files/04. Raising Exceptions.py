# You can raise exceptions by using the raise statement.
print(1)        #
raise ValueError
print(2)
# You need to specify the type of the exception raised.

# Example:
try:
    a=int(input("Enter: ")) 
    if a<0: 
        raise Exception() 
    print("OK!") 
except Exception: 
    print("ERROR!")
#

# Example:
try:
  print(1 / 0)
except ZeroDivisionError:   # ZeroDivisionError
  raise ValueError          # ValueError
#


