# SECTION 1
# Properties provide a way of customizing access to instance attributes.
# They are created by putting the property decorator above a method, 
# which means when the instance attribute with the same name as the method is accessed, the method will be called instead.
# One common use of a property is to make an attribute read-only.
# Example:
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)      # False
pizza.pineapple_allowed = True      # AttributeError

# So the @property decorator just removes parentheses when you call a function. 
# Look. Without @property: class Pocket: def myMoney(self): return '$100' a = Pocket() print(a.myMoney()) 
# RESULT: $100 And now with the @property decorator: class Pocket: @property def myMoney(self): return '$100' a = Pocket() print(a.myMoney) 
#RESULT: $100 Now it looks like a variable. But it's not. It's still a function that returns '$100'. You just don't need to type "()" when calling it. 
# So what if someone tries to take some of your money(all of them)? a.myMoney = '$0' 
# RESULT: AttributeError: can't set attribute Of course, couse it's a function! It's not a variable. You can't change it. You can't modify it. You can only call it. 
# Even though it looks like a variable. class Pizza: @property def isTasty(self): return True myPizza = Pizza() print( myPizza.isTasty ) 
# RESULT: True myPizza.isTasty = False 
# RESULT: AttributeError


# A property is a function with no argument and can be called without parentheses. 
# Hence, it syntactically behaves as an attribute when called, except it cannot be assigned. 
# Also, it is more than a attribute because it can perform calculation. 


# If you have variable in your class that you want no one from the outside to access, 
# you basically create a method with the exact same name as your variable with @property decorator. 
# So whenever someone from the outside tries to MODIFY your variable, they'll catch an error because you cannot modify a method, right? 
# So basically your variable becomes strictly read-only.

# How I realized that the @properties are used to indicate the properties of the class attribute which can not be changed? 
# Example: 
class Pizza: 
  def __init__(self, toppings): 
    self.toppings = toppings 
    self.weight = "1 kg" 
    self._form = "circle" 
    self.pieces = 8 
    @property 
  def isBig(self): 
    if self.weight=="1 kg": 
      return True 
    else: 
      return False 
    @property 
   
  def form(self): 
    return self._form 
  
pizza = Pizza(["cheese", "tomato"]) 
print(pizza.isBig, pizza.form, pizza.pieces) 
pizza.pieces = 4 # pizza.form="fourscuare" - error here 

# let's turn method into read-only attribute using '@property'



https://www.sololearn.com/learning/1073/2472/5144/2





