# Native Datatypes Examples
# Example: to Check If a String Is a Number (Float)


# Using float()
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print(isfloat('s12'))       # False
print(isfloat('1.123'))     # True

# Here, we have used try except in order to handle the ValueError if the string is not a float.
#    In the function isfloat(), float() tries to convert num to float. If it is successful, then the function returns True.
#    Else, ValueError is raised and returns False.
# For example, 's12' is alphanumeric, so it cannot be converted to float and False is returned; whereas, '1.123' is a numeric, so it is successfully converted to float.



