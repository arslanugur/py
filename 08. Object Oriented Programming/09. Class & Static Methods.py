# SECTION 1
# Methods of objects we've looked at so far are called by an instance of a class, which is then passed to the self parameter of the method.
# Class methods are different - they are called by a class, which is passed to the cls parameter of the method.
# A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.
# Class methods are marked with a classmethod decorator.
# Example:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())      # 25

# new_square is a class method and is called on the class, rather than on an instance of the class. It returns a new object of the class cls.
# Technically, the parameters self and cls are just conventions; they could be changed to anything else. 
# However, they are universally followed, so it is wise to stick to using them.

(1): class Rectangle: def __init__(self, width, height): self.width = width self.height = height def calculate_area(self): return self.width * self.height dd = Rectangle(6, 2) print(dd.calculate_area()) OUTPUT: >>> 12 >>> We set up a class called Rectangle, with 2 attributes, namely width and height.
(2): Also, we defined a calculate_area method for our Rectangle class. This calculate_area method doesn't even take any arguments, aside from the trivial self (the instance itself) argument. Yet, it returns self.width * self.height. Hence, the calculate_area method for the class Rectangle would basically take an instance of the class Rectangle that got supplied to it by us. Then, the method would determine its width and heights attribute, and then multiply these together and finally RETURN the result of this multiplication operation. We set up an INSTANCE named dd of the class Rectangle that has 6 and 2 as its width and height attributes respectively. So, dd.width = 6 and dd.height = 2. Hence, the code dd.calculate_area would perhaps be interpreted as follows.
(3): dd.calculate_area() return dd.width * dd.height return 6 * 2 return 12 So, print(dd.calculate_area()) would clearly print 12 as the OUTPUT. Note how for the calculate_area method, it ran "on" an instance, just like pretty much ALL of the methods we've covered so far really! In fact, the general syntax so far has been kinda like "instance_name.method()". Hence why I guess you could call em all INSTANCE methods.
(4): Here's a question for you: In the special case where you've got a SQUARE (so hence width = height), suppose with 5 as the length of each of its sides, then you'd have to write in something like square = Rectangle(5, 5) in order to actually define or set up the instance. Writing that 5 in there twice may not seem like so much of a BiG deal, but what if you had MANY squares? (Or if you were talking about 3D space, and had MANY cubes? Or even higher dimensional space?) Would be a very tedious tough job to deal with the repetition of the arguments you enter, right? To overcome this problem, what we can do is instead of being forced to enter TWICE the 5, we'd be better off with just entering it ONCE you know. As such, we gotta make an actual CHANGE to the set of parameters that get passed to the class constructor.
(5): In fact, in the instances we define, we'd better off with just supplying a SINGLE argument, for the 1 attribute side_lengh, rather than supplying the 2 (repeated 😔) arguments for the width and height attributes (both of which would obviously be same for all squares that we define when making them be instances of thee class Rectangle. But how do you actually do this in practice? Well, you need a "middle man" here to help us! You need a METHOD such that YOU give to it just a SINGLE 5, and it initialises an instance of the class Rectangle containing TWO of such 5s, one for the width and the other for the height of such an instance set up! Such a method would basically TAKE ONE value from you, bring up TWO of such values, and then pass it onto the class constructor you've pre-defined.
(6): This is known as a ★FACTORY METHOD★: as a method, it takes a set of arguments from you, transforms it to come up with ANOTHER set of arguments, and then passes this in turn to the pre-defined class constructor. But hang on a sec! Exactly how does it even know which class's constructor it's meant to actually PASS on that set of arguments TO??? Hence why they seem to have the general syntax of class_name.method() rather than instance_name.method(), and so they are CLASS methods which run "on" a CLASS.
(7): Q: What's the meaning/point of the line of code "@classmethod" BEFORE defining a class method? > This is a decorator. lt wraps a below class function so you can use a cls variable inside it. To keep it simple treat it like a annotation to mark method so it can be used without making an instance of a class. > So that means just as functions inside a class need the argument 'self' to be able to reference their own parameters, the class methods need a similar argument 'cls' to be able to reference their own parameters.    
(8): class Rectangle: def __init__(self, width, height): self.width = width self.height = height def calculate_area(self): return self.width * self.height @classmethod def new_square(cls, side_length): return cls(side_length, side_length) square = Rectangle.new_square(5) print(square.calculate_area()) I think the following interpretations get made.
(9): square = Rectangle.new_square(5) square = Rectangle(5, 5) So, square is an INSTANCE of the CLASS Rectangle, and it has 5 and 5 as its width and height attributes respectively. Hence, it makes sense to say that square.width = 5 and square.height = 5. Therefore, I think the following interpretations get made. square.calculate_area() return square.width * square.height return 5 * 5 return 25 So, print(square.calculate_area()) should print 25 as OUTPUT, which is true if you Try It Yourself...


'''Example of factory methods''' 
class Vehicle: 
    def __init__(self, make, model, vehicleclass, fuel): 
      self.make = make 
      self.model = model 
      self.vehicleclass = vehicleclass 
      self.fuel = fuel 
      
    def show_info(self): 
      print("Make: {0}, model: {1}, class: {2}, fuel: {3}".format(self.make, self.model, self.vehicleclass, self.fuel)) 
      @classmethod 
      
    def petrol4x4(cls, make, model): 
      return cls(make, model, "4x4", "petrol") 
      @classmethod 
      
    def dieselvan(cls, make, model): 
      return cls(make, model, "van", "diesel") #Usage 
    
a = Vehicle.petrol4x4("Fiat", "500x") 
b = Vehicle.dieselvan("Volkswagen", "Transporter") 
a.show_info() 
b.show_info() # Continues in reply
# same vehicles could be also created like this 
c = Vehicle("Fiat", "500x","4x4", "petrol") 
d = Vehicle("Volkswagen", "Transporter", "van", "diesel") 
c.show_info() 
d.show_info() # but which one is easier to use. 
# The first example using @classmethod in addition to cleaner and easier code enforces some standards on data, 
# eg. someone could provide 4x4 as "4 x 4" and if we were to list all 4x4 vehicles those defined differently would not be listed without extra work.
# https://realpython.com/instance-class-and-static-methods-demystified/
# Lets try simply with animals. @Classmethod is just the way to create class instances where its arguments are created in a way you want. 
# So, assume we have class Animal that takes name, weight(in kg), number of eyes, number of legs. 
# To create instances of such class, we write John=Animal("John",70,2,2) Huge_Spyder=Animal("Huge_Spider",1,8,6) 
# Assume, among our database will be like hundreds of people and spyders, assume all people have 2 eyes and 2 legs and all spyders 8 eyes and 6 legs, 
# so we dont want to enter that similar data, each time we see human or spyder. 
# So (using @classmethod) we can create class instances where creating human instance it will get 2 eyes 2 legs (and 8 and 6 for spider), 
# all input we need is just name and weight John=Animal.human("John",85) Huge_Spider=Animal.spider("Huge_Spider",1) 
# Printing those instances, we get John,85,2,2 and Huge_Spider,1,8,6 . We achieve it by creating pattern (@classmethod) that handle arguments of new class instance. 


# Example: to make sayHi() a class method.
class Person:
  def __init__(self, name):
    self.name = name
    @classmethod    #decoration
    
  def sayHi(cls):   #function inside
    print("Hi")
#

# what I understood from class method is: 
# You don't need an attribute to call classmethod, but you need an attribute to call class function. 
# Below, I have commented classmethod lines and output print line related to classmethod. 
# below is the normal case, i.e. to call function sayHi, I have to give an attribute inside that function. 
# To use call method, I don't have to use attitude name. It can be done commenting def sayHi(self) lines and 1st output line.
# Example:
class Person: 
  def __init__(self, name): 
    self.name = name 
  def sayHi(self): 
    print("Hi") # @classmethod # def sayHi(cls): # print ("Hi") Person.sayHi ("Pankaj") # Person.sayHi ()

# https://realpython.com/instance-class-and-static-methods-demystified/        


# SECTION 2
# Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.
# They are marked with the staticmethod decorator.
# Example:
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
#

# Static methods behave like plain functions, except for the fact that you can call them from an instance of the class. 

# @classmethod and @staticmethod allow the use of defined in the class methods without creating an object of that class

# The key to understanding this is experience. 
# So far, Java is the only language I understand completely, 
# and these options like static and private variables or methods are not new for me, as Java itself is an OOP as well. 

# A simple example to understand static method: 
class Car(object): 
  wheels = 4 
  def __init__(self, make, model): 
    self.make = make 
    self.model = model 
    
mustang = Car('Ford', 'Mustang') 
print(mustang.wheels) # 4 print Car.wheels # 4 A Car always has four wheels, regardless of the make or model. 
# Instance methods can access these attributes in the same way they access regular attributes: through self (i.e. self.wheels). 
# There is a class of methods, though, called static methods, that don't have access to self. 
# Just like class attributes, they are methods that work without requiring an instance to be present. 
# Since instances are always referenced through self, static methods have no self parameter.

# Differences between "class" and "static" methods: http://lifecs.likai.org/2014/03/really-understanding-python.html

# 1) Normal methods - They belong to instances (objects) and can be called only from instances (objects). 
# They are meant to work with data that belongs to instances (objects). 
# 2) Class methods - They belong to the class and can be called both from the class and the instance (objects). 
# They are meant to work with data that belongs to the class. 
# 3) Static methods - You can say they belong to the class, but they don't usually work with data from the class or instances (objects). 
# They are just pieces of code attached to the class. 
# Python doesn't have the special word "this", like in JavaScript for example, so it uses something else. 
# Python will silently pass the class or the instance when executing a method. class myClass: 
# 1) def myNormalMethod( silentPass, param1, param2, ... ) 
# Python will pass the INSTANCE (object) that is doing the method call because this is how Normal Methods work. 
# The convention is to write 'self' instead of 'silentPass', but it's just a variable. 
# Example call: # myInstance001.myNormalMethod(arg1, arg2, ... ) 
# - myInstance001 will be passed to silentPass automatically behind the scenes, do not pass it manually in the list of arguments 
# 2) @classmethod def myClassMethod( silentPass, param1, param2, ... ) 
# Python will pass the CLASS that is doing the method call because this is how Class Methods work. 
# The convention is to write 'cls' instead of 'silentPass', but it's just a variable. 
# Example calls: 
# myInstance001.myClassMethod( arg1, arg2, ... ) - myClass will be passed to silentPass automatically behind the scenes, do not pass it manually 
# myClass.myClassMethod( arg1, arg2, ... ) - same as above 
# 3) @staticmethod def myStaticMethod( param1, param2, .. ) 
# No silentPass here because this is how Static Methods work. 
# Example calls: 
# myInstance001.myStaticMethod( arg1, arg2, ... ) - no silent pass # myClass.myStaticMethod( arg1, arg2, ... ) - no silent pass 


# On a separate note - given that __init__ is executed only when an instance (object) is created, you can use it to strictly separate class from instance attributes and methods. 
# For example, if you do this: class myClass: attr1 = "abc" ...then the class and all instances will have an attribute called attr1. 
# But if you do this: class myClass: def __init__( self ): self.attr1 = "abc" ...then only instances will have an attribute called attr1. 
# Same can be done for methods: 
class myClass:
    def commonMethod(self):
        print("commonMethod called")
    def __init__( self ):
        def temporary_function():
            print("instanceMethod called")
            self.instanceMethod = temporary_function
        
myInstance = myClass()
commonMethod() #NameError 
temporary_function() #NameError 
instanceMethod() #NameError 
myClass.commonMethod() #TypeError 
myClass.temporary_function() #AttributeError 
myClass.instanceMethod() #AttributeError 
myInstance.commonMethod() #"commonMethod called" 
myInstance.temporary_function() #AttributeError
myInstance.instanceMethod() #"instanceMethod called" 
# Actually, myClass.commonMethod() can work but you have to manually pass the class or the instance, like so: 
myClass.commonMethod( myClass ) #"commonMethod called" 
myClass.commonMethod( myInstance ) #"commonMethod called" 
myClass.commonMethod( "This is a random string" ) #"commonMethod called" 
# Here it doesn't matter what you pass because the method just prints to the console, but if you work with data then it matters what you pass. 
# This is just a curious example, but try to avoid it and use Class Methods instead.

# Example:
class Pizza: 
  def __init__(self, toppings): 
    self.toppings = toppings 
    @staticmethod 
  def validate_topping(topping): 
    if topping == "pineapple": 
      raise ValueError("No pineapples!") 
    else: 
      return True 
    
  def __repr__(self): 
    return "Pizza({})" . format(self.toppings) 
  
ingredients = ["cheese", "onions", "spam"] 
# List Functions often used in conditional statements, all and any take a list as an argument, 
# and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise). 
# if all([Pizza.validate_topping(i) for i in ingredients]): pizza = Pizza(ingredients) print(pizza) # Output: Pizza(["cheese", "onions", "spam"])
          
# The class method operates with methods or properties of the actual class, while the static method does not need any data about the actual class. 

# i will try to explain this line of code if all(Pizza.validate_topping(i) for i in ingredients): 
# after this the instruction pointer will go to method under @staticmethod 
# after this it will compare every element of ingredients with "pineapple" . 
# if any element in ingredients matches with pineapple than the programme will stop executing and will raise ValueError : "No pineapples " . 
# if there is no pineapple in the ingredients it will return true . 
# so as we know that if true: #then it will execute whatever is present under this "if" condition.
  
https://www.sololearn.com/learning/1073/2473/5143/1
amor enew
