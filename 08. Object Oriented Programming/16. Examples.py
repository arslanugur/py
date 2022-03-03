# Q1
# How is a property created?  - Using the property decorator

# A property can be declared in two ways. Creating the getter, setter methods for an attribute and then passing these as argument to property function. 
# [or] Using the @property decorator. http://stackabuse.com/python-properties I'm personally lost. Above is cut/paste

# Q2
# What is the difference between a class method and a static method?  - Class methods are passed the calling class, static methods aren't

# @class method def class_method_example(cls): pass in case of normal instance methods(functions): def normal_method(self): pass. difference is the "cls" and "self" arguements

#  I think "the" is to be removed from the sentence. 
# Class methods are passed by calling the class (cls), 
# static methods don't call the class (neither do they call an instance (self) 
# actually, static methods are simply functions that one writes inside a class for stylistic reasons when it is logically tied to the class. 
# That is, in order not to pollute the program with "free functions".

# A class method receives the class as implicit first argument, 
# just like an instance method receives the instance A class method is a method which is bound to the class and not the object of the class. 
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance. 
# It can modify a class state that would apply across all the instances of the class. 
# For example it can modify a class variable that will be applicable to all the instances. 
# Static Method A static method does not receive an implicit first argument. 
# A static method is also a method which is bound to the class and not the object of the class. A static method can’t access or modify class state. 
# It is present in a class because it makes sense for the method to be present in class. 
# https://www.google.com/amp/s/www.geeksforgeeks.org/class-method-vs-static-method-python/amp/

# Q3
# What are the usual parameter names for the calling instance and the calling class?  - self and cls

# This question confuses me. We all already know what calling method we should pass parameter "self"; 
# when we call ClassMethod (almost same as static method in other languages) we should pass "cls", but never both. 
# therefore this question is confusing. By the way, we don't HAVE TO use "self" or "cls", it is just naming convention. 
# We could use "this" and "instance", for example. 

# Remember it is just a tradition for the first parameter (positional passing) in two cases. You can break the rules, but it might cause more confusion.

# The distinction between "self" and "cls" is defined in PEP 8 . This is not a mandatory. It's a coding style. 
# PEP 8 says: Function and method arguments: Always use self for the first argument to instance methods. Always use cls for the first argument to class methods.

# They are just conventions you can pretty much use any in place of them. 
# class say: def __init__(self, content) : self.content = content def hello(self): print(self.content) 
# Will work same as class say: def __init__(any, content) : any.content = content def hello(any): print(any.content)

# Q4
# What method is called just before an object is instantiated?  - __init__

# actualy before run __new__(cls,...) to create object and then __init__(self,...) to initialize it: 
# Because __new__() and __init__() work together in constructing objects (__new__() to create it, and __init__() to customize it), 
# no non-None value may be returned by __init__(); doing so will cause a TypeError to be raised at runtime. 
# https://docs.python.org/3/reference/datamodel.html#object.__new__

# "__init__" is called as a constructor in object oriented terminology. 
# This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
# For example, class Point: """ Point class represents and manipulates x,y coords. """ def __init__(self): 
# """ Create a new point at the origin """ self.x = 0 self.y = 0


# to make the egg attribute strongly private and access it from outside of the class.
class Test:
  __egg = 7

t = Test()
print(t._Test__egg)

# Q5
# What is the automatic process by which unnecessary objects are deleted to free memory? - Garbage collection
# for more information about garbage collection https://docs.python.org/3/library/gc.html
# Garbage collection is a module that is used to delet the object from the memory that are no longer used.The name of garbage collection is gc.

# Q6
# to make a setter for the property name.
class Person:
  def __init__(self, name):
    self._name = name

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value
#



      
