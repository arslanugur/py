# DIFFERENCE BETWEEN FUNCTION AND METHOD
# FUNCTIONS
# 1. Function is a block of code or group of statements which is called independently by its name without associating to an object
# 2. Parameters or arguments are passed explicitly 
# 3. Functions are not associated with any class or object of a class
# 4. Py has many inbuilt functions such as sorted(), int(), float(), max(), min() et cetera

# Syntax:
def function(par1, par2, par n):
  # statement
  # statement
  
  # statement n
  
# Code:
# Define function to check even numbers
def even(n):
  if n%2 == 0
    return f"{n} is an even number"
  else:
    return f"{n} is not an even number"
# Call function to print the result
print(even(2))
print(even(5))
# output:
# 2 is an even number
# 5 is not an even number


# METHODS
# 1. Method is also similar to function which is called dependently by its name associating to an object
# 2. Method is implicitly passed the object on which it is invoked
# 3. Methods are associated with an object of a class
# 4. Py has many inbuilt methods such as randint(), sqrt(), randrange() et cetera

# Syntax:
class class_name
  def method(par1, par2, par n)
    # statement
    # statement
    
    # statement n

# Code:
# Create class
Class Even:
  # Define method to check even numbers
  def even_numbers(self, n):
    if n%2 == 0:
      return f"{n} is an even number"
    else:
      return f"{n} is not an even number"
# Create object of class Even
obj = Even()
# Call method to print the result
print(obj.even_numbers(2))
print(obj.even_numbers(5))
# output:
# 2 is an even number
# 5 is not an even number


