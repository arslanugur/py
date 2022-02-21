# SECTION 1
# The lifecycle of an object is made up of its creation, manipulation, and destruction.

# The first stage of the life-cycle of an object is the definition of the class to which it belongs.
# The next stage is the instantiation of an instance, when __init__ is called. 
# Memory is allocated to store the instance. 
# Just before this occurs, the __new__ method of the class is called. This is usually overridden only in special cases.
# After this has happened, the object is ready to be used. 

# Other code can then interact with the object, by calling functions on it and accessing its attributes.
# Eventually, it will finish being used, and can be destroyed.

# __new__ method is automatically performed when you use __init__ method. 
# __new__ creates the object in the memory and __init__ sets up object's attributes.

# https://www.agiliq.com/blog/2012/06/__new__-python/ 

# OBJECT = INSTANCE of a class 
# INSTANTIATION = creating a object from a class 
# ATTRIBUTE = variables belonging to an object 
# INITIALIZATION = assigning a value to an empty variable 
# METHOD = function belonging to an object (which is also an ATTRIBUTE) 
# Those concepts (and OOP itself) are the same throughout languages. 
# If you have enough time, it's good to read about OOP in other courses (Java, C++, etc.). 
# Don't need to learn from the start, just read about OOP, and something helpful is always there. 
# OOP is difficult because it starts from abstract, which is contrary to the natural perception of human being. 
# But if you keep going, some day you will realize you think it's a matter of fact.

# I make an object of class without using __init__. Why does it work? class A: def hi(s): print('hi') a = A() a.hi()

# This conflict all started when the course content described the special method __init__, as a constructor, which is not, __init__ is an initializer. 
# The every class constructor is built and called implicitly in python, and calls __init__ if it's present, if not it will create the instance anyway. 

# Which stage corresponds to the __init__ method being called?  # instantiation

# it is instantiational, because __init__calls for the instance on the list.

# To initialize something is to set it to its initial value. To instantiate something is to create an instance of it. 
# __init__ is used to initialize and object that has just been instantiated. 
# Initializing can also happen elsewhere in the code too (ie, counter = 0), or not at all. 
# So its not a "stage" in creating an object. However instantiating is, which will call __init__ if it's there


# SECTION 2
# When an object is destroyed, the memory allocated to it is freed up, and can be used for other purposes.
# Destruction of an object occurs when its reference count reaches zero. 
# Reference count is the number of variables and other elements that refer to an object.
# If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it can be safely deleted.

# In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well.
# The del statement reduces the reference count of an object by one, and this often leads to its deletion.
# The magic method for the del statement is __del__.
# The process of deleting objects when they are no longer needed is called garbage collection.
# In summary, an object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). 
# The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. 
# When an object's reference count reaches zero, Python automatically deletes it.
# Example:
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42> 
c = [a]  # Increase ref. count  of <42> 

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42> 
c[0] = -1  # Decrease ref. count  of <42>

# Lower level languages like C don't have this kind of automatic memory management.

# So in the first half we made this object <42> and then we setup b and c variables which referred to this object. 
# So <42> became a reference to b and c. then in the second half, we redefined b and c so that they weren't referring <42> any longer. 
# So <42> lost its references. This is the basic idea right? a = dog b = a*2 c = a*3 So b and c both use dog. 
# but then we change b and c b=0 c=0 now b and c stopped using dog! 
# And if we delete a, then nothing references dog anymore! And so with 0 references, dog is deleted from memory. 

# To anyone who may be lost right now, I'll explain OPP in this comment, so keep reading. 
# First off, OOP stands for Object Oriented Programming, in case you didn't know. 
# Python is an OPP which means everything object or a reference to an object. 
# For example when you open up your python IDLE and type in a=42, Python does not set the value 42 to equal a, that would be insane. 
# What actually happens when you type in a=42 is Python create an Object (int 42) and a reference to the object by the name of "a". 
# To help you understand even better. If you create a second statement b=a, 
# Python does not actually set "b" equal to "a", instead python creates another reference by the name of "b" and points it to the existing object "int 42". 
# To solidify this idea let's change the value of one of these references. 
# If you now type into the IDLE shell a+=3, what will happen is Python will create a new Object "int 45" and point the "a" to that new object. 
# so now a will equal 45 and b will equal 42.


a = [1,2,3,4,5] 
print(a)      # [1,2,3,4,5]
b = a b.pop(0) 
print(a)      # [2,3,4,5]
# So, I changed my philosophy in python not to call it "variables" but "memory location" with "names". 
# A memory location can have many names as you wish. 
# All names refer to a single memory location containing any data, such as string/number/string/False/True. 
# So, if a memory location don't have any referenced name anymore (using del or operation above), 
# this memory location will be freed/deleted from a program. (this is called garbage collection) 
# All things are object in Python... including names and function. 
# For me, I just acknowledge it after playing with it a little while. 
# For further information, refer to: 
# http://www.staff.ari.uni-heidelberg.de/kruijssen/pycourse/html/14.html 
# https://stackoverflow.com/questions/21983014/why-does-values-of-both-variable-change


# py The function `sys.getrefcount(object)` returns the number of the references count from some object, class, function, etc., 
# It's much better explaining with classes. `python 
import sys 

class Dog: 
  def __init__(self): 
    print('Dog created!') 
    
charlie = Dog() 
sys.getrefcount(charlie) # Start with 2 references 
# Two references of this object maybe one is for reference in memory or in the Python main stack. 
bella = charlie 
sys.getrefcount(charlie) # Increased to 3 references 
sys.getrefcount(bella) # 3 references same as Charlie del charlie 
# Or delete bella it's the same sys.getrefcount(bella) 
# Decrease to 2 references del bella 
# This references is lost and the garbage collector destroy the variable in the memory address.


# What is __del__ the magic method for? --- del instance




