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


# Example: to create an "isAdult" property.
class Person:
  def __init__(self, age):
    self.age = int(age)
    
  @property  
  def isAdult(self):
    if self.age > 18:
      return True
    else:
      return False
# if you do not put property, then it is a function. With property it behaves like an attribute (you do not use parantheses when you call it).

# The adult age starts at 18, therefore it should be def isAdult(self): if self.age >= 18: return True else: return False

# SECTION 2 - setter and getter functions
# Properties can also be set by defining setter/getter functions.
# The setter function sets the corresponding property's value.
# The getter gets the value.
# To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
# The same applies to defining getter functions.
# Example:
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

# (1) Example:
class Pizza: 
    def __init__(self, toppings): 
        self.toppings = toppings 
        self._pineapple_allowed = False 
        
    @property 
    def pineapple_allowed(self): 
        return self._pineapple_allowed 
    
    @pineapple_allowed.setter 
    def pineapple_allowed(self, value): 
        if value: 
            password = input("Enter the password: ") 
        if password == "Sw0rdf1sh!": 
            self._pineapple_allowed = value 
        else: 
            raise ValueError("Alert! Intruder!") 
            
pizza = Pizza(["cheese", "tomato"]) 
print(pizza.pineapple_allowed) 
pizza.pineapple_allowed = True 
print(pizza.pineapple_allowed) 
# OUTPUT: False 
# Enter the password: Sw0rdf1sh! True

# There is a mismatch between the Example and the Result - password input phrases are different. 
# In the Example the password input phrase is "Enter the password:" 
# and the corresponding output in Result is "Enter password to permit pineapple:".
# (2): We create an instance called pizza of the class Pizza, with its toppings-attribute equal to the LIST of strings given by ["cheese", "tomato"]. 
# So, you know that the code pizza.toppings would RETURN the list of strings ["cheese", "tomato"].
# (3): Now, let's Move onto understanding the OUTPUT of the code print(pizza.pineapple_allowed) 
# First of all, recall that the @property decorator turns the method that's defined just below "@property" into a read-only ATTRIBUTE. 
# Then, consider the following code block. def pineapple_allowed(self): return self._pineapple_allowed 
# Taking self=pizza in 👆, consider the following interpretations that I think occur. pizza.pineapple_allowed pizza._pineapple_allowed False 
# Last line follows since right at the start of the definition of the class Pizza, it was mentioned "self._pineapple_allowed = False". 
# Seems like this applies for ANY instance, parameterised by self, and so for the instance pizza being taken as self, 
# we see that pizza._pineapple_allowed would RETURN False. 
# Hence, print(pizza.pineapple_allowed) would print False in the OUTPUT, which clearly occurs! 

# (4): Next, you've gotta deal with the code line pizza.pineapple_allowed = True 
# So, you've got a PROPERTY (a method turned into a read-only ATTRIBUTE due to "@property" just above its definition), 
# run "on" the object/instance called pizza (=self) , which is ★SET★ equal to a value, namely the True (Boolean) value. 
# You're basically just trying to ★SET★ a PROPERTY EQUAL to a value.
    
# (5): @pineapple_allowed.setter def pineapple_allowed(self, value): if value: password = input("Enter the password: ") 
# if password == "Sw0rdf1sh!": self._pineapple_allowed = value else: raise ValueError("Alert! Intruder!") 
# I suspect that the following interpretations get made perhaps by Python. pizza.pineapple_allowed = True pineapple_allowed(pizza, True) 
# So, self=pizza, and value=True get taken. Hence, user gets prompted "Enter the password: ", and the result gets stored as the variable password.

# (6): Next, because the user inputted password IS an EXACT MATCH with "Sw0rdf1sh!", the following code gets executed right away. self._pineapple_allowed = value 
# Of course, putting in self=pizza AND value=True make it clearer to see what this code means, since you then get the following. 
# pizza._pineapple_allowed = True In other words, for the pizza instance, 
# the ATTRIBUTE _pineapple_allowed has turned into the value True (from False as was defined in the class definition's very beginning). 
# So, it makes sense to say that now pizza._pineapple_allowed has become equal to True.

# (7): Lastly, there's the code line print(pizza.pineapple_allowed). 
# The argument of the print function I'd suspect to be interpreted as follows. 
# pizza.pineapple_allowed pizza._pineapple_allowed True Hence, print(pizza.pineapple_allowed) is really just print(True), causing clearly True to be OUTPUT.

# Example:
class Class1:
    def __init__(self, value): 
        self.__var = value # Чтение 
        
    @property 
    def v(self): 
        return self.__var # Запись 
    
    @v.setter 
    def v(self, value): 
        self.__var = value # Удаление 
        
     @v.deleter 
    def v(self): 
        del self.__var # Запись 
        
c1 = Class1(5) 
c1.v = 35 # Чтение 
print(c1.v) # Удаление 
del(c1.v) # 35

# Sometimes it is recommended to protect attributes of classes to avoid bugs or protect data. 
# So you can use the "@property". Python know there will be a method instead of attribute and provide a getter/setter. 
# But you can edit the method and getter/setter but you don't have to. It is just optional. 
# This code should only be an example for the usage of editing the setter. (password protection) 
# If you use the @property method you can set the value with "=". 
# This is different to other methods. So you have normally: User --> Attribute User <-- Attribute 
# And if you want to avoid that every user can change the values of attributes: 
# User --> Setter with pw protection --> Attribute and: User <-- Getter <-- Attribute 
# An example for a getter with pw protection could be, that you want to check account balance. 
# You have to enter your pin to "print" the account balance.

# This lesson mentions the 'getter' keyword but does not explain how to use it. 
# Even the official Python documentation does not explain how! 
# So, I looked into it and came up with this example. 
# The lesson uses the '@property' decorator to do two things in one step: 
# it declares the 'pineapple_allowed' method as a property and then defines the 'getter' method for that property. 
# @property def pineapple_allowed(self): return self._pineapple_allowed 
# In order to do the same thing using the 'getter' keyword, we need to rewrite this code as two separate steps. 
# The first step is to declare the 'pineapple_allowed' method as a property using the '@property' decorator; 
# However, this time, we don't define the 'getter' method. 
# We just supply an empty function with no parameters and put the 'pass' statement in the execution block. 
# The 'pass' statement is a placeholder that does nothing. Here's what the first step looks like: @property def pineapple_allowed(): pass

# Define a decorator that would be used to add a setter to the property egg. --- @egg.setter

# to define a setter, we use a decorator of the same name as the property, followed by a dot and also the setter keyword. 
# So (@) + (decorator name) + (.) + (setter keyword). Hope this was helpful. Therefore, the answer will be @egg.setter 

# This setter is really good for data validation. 
# But I still cannot find the difference between property and getter. 
# The only thing I know is that property can make the attribute read-only. Who can help me?



