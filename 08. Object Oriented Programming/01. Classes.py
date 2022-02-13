# SECTION 1
# We have previously looked at two paradigms of programming 
# - imperative (using statements, loops, and functions as subroutines),
# - and functional (using pure functions, higher-order functions, and recursion).

# Another very popular paradigm is object-oriented programming (OOP).
# Objects are created using classes, which are actually the focal point of OOP. Function type of object is a method
# A method is basically a function that operates on that object
# The class describes what the object will be, but is separate from the object itself. 
# In other words, a class can be described as an object's blueprint, description, or definition.
# You can use the same class as a blueprint for creating multiple different objects.

# Classes are created using the keyword class and an indented block, which contains class methods (which are functions).
# Below is an example of a simple class and its objects.

# Example:
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

# This code defines a class named Cat, which has two attributes: color and legs.
# Then the class is used to create 3 separate objects of that class.

# Explanations:
# http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html
# classes-and-objects-the-basics It is the third edition of "How to think like a computer scientist: Learning with Python 3". 
# It is very well explained and clearly structured. Maybe it is a bit lengthy. 
# There is also a PDF-version available at: http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf

# In object oriented programming OOP module "self" is a reference to the same class. 
# Just like pointing at yourself and saying I or me. 
# In Visual Basic they use "Me" instead of self. In c/c++/java they use "this".

# The explanation will come in further slide, I think it would be better to include it here: 
# The __init__ method is the most important method in a class. 
# This is called when an instance (object) of the class is created, using the class name as a function. 
# All methods must have self as their first parameter, although it isn't explicitly passed, 
# Python adds the self argument to the list for you; you do not need to include it when you call the methods. 
# Within a method definition, self refers to the instance calling the method. 
# Instances of a class have attributes, which are pieces of data associated with them. 
# In this example, Cat instances have attributes color and legs. 
# These can be accessed by putting a dot, and the attribute name after an instance. 
# In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.
# https://www.tutorialspoint.com/python/python_classes_objects.htm

# Great explanation of self from https://pythontips.com/2013/08/07/the-self-variable-in-python-explained/ 
# "The first argument of every class method, including __init__, is always a reference to the current instance of the class. 
# By convention, this argument is always named self. 
# In the __init__ method, self refers to the newly created object; in other class methods, it refers to the instance whose method was called. 
# For example the below code is the same as the above code. However self is not a reserved keyword in python it’s just a strong convention. 
# Many people say that why do we have to write self? 
# Why can’t we have it set automatically like in Java? 
# Someone also filed a PEP (improvement suggestion) in which he suggested to remove the explicit assignment of self keyword. 
# However Guido Van Rossum (the maker of python) wrote a blogpost in which he told why explicit self has to stay. 
# http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html

# In Object Oriented Programming theory a method is a function that operates in an object. 
# In Python specifically all is is an object, so the answer "Function" is correct. 
# The Function class is the description of a function object, 
# a function object is created with the def keyword, the function name and its arguments (def function_name(args)

# Function is a type of method! Because functions are also called as methods.
# When a function is defined inside a class,it is a method.When defined else where outside a class it is a function.

# The method is a function, but why is such an unrelated issue with a lesson in which there was no mention of it. 
# It's very inconsistent in my opinion, and this compliance should be done in the future.

# Function and method are same. We say method in Object Oriented Programming languages like python,Java etc while function in procedural programming language like C.


# SECTION 2: __init__
# The __init__ method is the most important method in a class.
#  This is called when an instance (object) of the class is created, using the class name as a function.

# All methods must have self as their first parameter, although it isn't explicitly passed, Python adds the self argument to the list for you; 
# you do not need to include it when you call the methods. Within a method definition, self refers to the instance calling the method.

# Instances of a class have attributes, which are pieces of data associated with them.
# In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, and the attribute name after an instance.
# In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.
# Example: 
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)      # ginger
# In the example above, the __init__ method takes two arguments and assigns them to the object's attributes. The __init__ method is called the class constructor.

# Explanations:
class Cat: 
    def __init__(self, color, legs): 
        self.whichcolor = color 
        self.howmanylegs = legs 
 
felix = Cat("ginger", 4) 
print(felix.whichcolor)     # ginger
print(felix.howmanylegs)    # 4
        
# you should know that it is not necessary to write self as a word. 
# you can write it any thing like you can write instead of self obj or even your name but with one condition Which
# it has to be the the first argument cause it just a word refers to the object like garfield = Cat('white', 4) 
# now in the class itself.
# Example:
class Cat: 
    def __init__( myobject, color, legs):   # here garfield is just referring to the object of the class by using myobject so when you say garfield 
        myobject.catcolor = color           # catcolor it is actually like you are saying get myobject.catcolor 
        myobject.catlegs = legs
        
garfield = Cat("white", 4) 
print(garfield.catcolor)        # white
print(garfield.catlegs)         # 4

# Methods with double under score at the beginning and at their ends are called Magic Methods, for example, __init__

# Technically, 'self' is just a variable name. 
# E.g. you could use 'radio' instead, so 
class Cat: 
    def __init__(radio, color, legs): 
        radio.color = color 
        radio.legs = legs 

felix = Cat("ginger", 4) 
print(felix.color) # 'ginger', but because 'self' is universally used, it would be bad coding style to use a different variable name.
# 


# Example:
# Sometimes 'parameter' gets confused with 'argument'. 
# A parameter is a variable that is part of the definition of a function/method. 
# e.g. in 
def squared(a): 
    return a * a # a is a parameter. An argument is the actual value of the variable passed to the function when it is called. 
# e.g. in squared(5) 5 is an argument. 
# The value of the argument is passed to the parameter and operated on by the function/method. 
# In this example, the argument value 5 is passed to the parameter a and the function squared() returns 25

# Try changing assignments, like self.color = legs or self.color = "ginger" and run the code. 
# This helped me understand what was happening. I found the course explanation confusing, this helped clarify.


# Example:
def __init__(self,height,sex,age): 
    self.myheight = height 
    self.mysex = sex 
    self.myage = age

student = me("six feat","male",45) 
print(student.myheight)             # six feat 
print(student.mysex)                # male
print(student.myage)                # 45
# Think of self as student thus self = student (student is a class object) and remember the above code said whenever there is a self.myheight 
# it should print height (self.myheight=height) 
# so in a nut shell self.myheight is the same as student.myheight, therefore the height of the student is printed. 
# Same thing applies to the rest of the code


# Example:
class Cat: 
    def __init__(self, color, legs, age): 
        self.color = color 
        self.legs = legs 
        self.age = age 
        
boris = Cat("yellow", 4, 25) 
tom = Cat("red", 3, 16) 
felix = Cat("ginger", 4, 8) 
print(felix.legs)               # 4
print(tom.age)                  # 16
print(boris.color)              # yellow


# Example: to create a class and its constructor, taking one argument and assigning it to the "name" attribute. Then create an object of the class.
class Student:
    def __init__(self, name):
        self.name = name

test = Student("Bob")


# Example:
class Lokh:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ya = Lokh('Я', 23)
print(f'{ya.name} же не лох, мне {ya.age} года.')


# first I thought it was only a single underscore. vote me up if you thought the same
class Student:
    def __init__(self,name): 
        self.cocojambo = name 

test = Student("Bob") 
print(test.cocojambo) 
# It is not mandatory to set self.name inside constructor. 
# You can use any name for the variable, but for the clarity of the code is good to have the same name as the transmitted argument.

# It would be a good idea (i.e. would make things clearer for the student) 
# if it was explicitly mentioned in the first lesson that the underscore on each side of the __init__ is actually a double underscore. 
# That fact is not obvious with the font in which this is usually read; there is no break between the two underscore characters.

# 'self' is a parameter like 'name' in this example. 
# When the object 'test' is created as a specific instance of the class 'Student', 
# the argument "Bob" is passed to the parameter 'name' and the argument 'test' is passed to the parameter 'self'. 
# So when you want to print the 'name' attribute of 'test', you use 'print(test.name)'. 
# The __init__ function processes self.name = name, so test.name is returned as "Bob".


# SECTION 3: METHODS
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)            # Fido Woof!
fido.bark()

# Classes can also have class attributes, created by assigning variables within the body of the class. These can be accessed either from instances of the class, or the class itself.
# Example:
class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)            # 4
print(Dog.legs)             # 4
# Class attributes are shared by all instances of the class. 


# If the instance fido does not have a variable called legs then it will share with Dog.legs, 
# but if you later initialize fido.legs with a value then there will be two variables fido.legs and Dog.legs and they're independent. 
class Dog: 
    legs = 4 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color

fido = Dog("Fido", "brown") 
print(fido.legs)            # 4
fido.legs=7 
print(fido.legs)            # 7
print(Dog.legs)             # 4
Dog.legs=6 
print(Dog.legs)             # 6
print(fido.legs)            # 7


# Example: With this code you got it easy: 
class Dog: 
    legs = 4 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
    def bark(self): 
        return "woof" 

fido = Dog("Fido", "brown") 
dado = Dog("toll", "late") 
print("The " + fido.color + " " + fido.name + " " + fido.bark() + " a lot!")    # The brown Fido woof a lot!
print("Fido legs before: " + str(fido.legs))                                    # Fido legs before: 4 
print("Dado legs before: " + str(dado.legs))                                    # Dado legs before: 4 
fido.legs = 4 
Dog.legs = 5
print("Fido legs after: " + str(fido.legs))                                     # Fido legs after: 4
print("Dado legs after: " + str(dado.legs))                                     # Dado legs after: 5
                            

# Example:
class Dog: 
    legs = 4 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 

rufus = Dog("Rufus III", "black") 
print(rufus.name, "is", rufus.color, "and has", Dog.legs, "legs.") # Rufus III is black and has 4 legs.

# Example: to calculate area of rectangle using class. It is working as expected, but don't know how it works
class rectangle: 
    def __init__(self, length=0, bredth=0): 
        self.length = length 
        self.bredth = bredth 
    def area(self): 
        self.length = int(input('Enter Length: ')) 
        self.bredth = int(input('Enter Bredth: ')) 
        
area = self.length * self.bredth 
print(area) 
rectangle().area()
        

# Example:
class point: 
    def __init__(self, x=0, y=0): 
        self.x = x 
        self.y = y 
    def distance_from_orizin(self):
        a = self.x**2
        b = self.y**2
        c = .5
        return((a+b)**c) 

p = point(3,4) 
q = p.distance_from_orizin() 
print(q)    # 5.0


# Example: to create a class with a method sayHi().
class Student:
  def __init__(self, name):
        self.name = name
  def sayHi(self):
    print("Hi from "+ self.name)

s1 = Student("Amy")
s1.sayHi()


# Self must be the first parameter in ever method that you create within the class. 
# This allows for inheritance -> which allows the class to inherit the properties or methods within it.

# def self self 
# Explanation: : explains to the program that the class name ends def takes out all the work of declaring variables 3 times within code 
# self needs to refer to itself self then is reused to print the argument hi 

# so just think of it like when you want to put a function inside of the class you put self as a perimeter for that function 
# then when you want to plug back into that function you say variable. Function... or print variable. 
# Perimeter... Etc it's algebraic it's all about associations the terminology will trip you up 
# I learned all this without understanding what all these terms mean like I just see how it works 
# but the terms will confuse you and I'm just not the kind of person that learns with terms

# SECTION 4: Classes
# Trying to access an attribute of an instance that isn't defined causes an AttributeError. This also applies when you call an undefined method.
# Example:
class Rectangle: 
    def __init__(self, width, height):
        self.width = width
        self.height = height

rect = Rectangle(7, 8)
print(rect.color)

# why every time we have type like, self.width=width or self.name=name can it be made default inside the program definition? 
# what is the point of typing? can it be typed in any other ways?
# You do not have to assign the parameter to self.parameter, 
# you could assign it an initial value directly: class go(): def __init__(self): self.name="Sam" self.legs=2 print(go.legs) -> 2 
# Note that when you do this, you must remove these parameters from __init__. 
# As you can see, when I implement a class, the initial values of name and legs will be Sam and 2 respectively. 
# By assigning name to self.name 
# for example, you leave the initial value to be determined when an object of the class is implemented: 
class go(): 
    def __init__(self,name,legs): 
        self.name=name 
        self.legs=legs 
        
man = go("Carson",3) 
print(man.legs) # 3 --> This creates an object of class go with name Carson and 3 legs and prints the number of legs man has.


# I think the self.method line creates a method with name 'method', and this can be called on an object by running object.method. 
# In the example, .width is a method, and it is assigned to return the value of the first object parameter, here also called width. 
# They don't have to share a name, but it makes sense if they do. 
# See the following example in which the method is called breadth instead (but the parameter is still called width). 
# It is just a question of naming, but I think it makes it a bit clearer as to what each line if the example code does: 
class Rectangle: 
    def __init__(self, width, height): 
        self.breadth = width 
        self.height = height 
        
rect = Rectangle(7, 8) 
print(rect.breadth) # 7

# Example:
class Rectangle: 
    def __init__(self, w, h): 
        self.width = w 
        self.height = h 
        
rect = Rectangle(7, 8) 
print(rect.width)   # 7


# Example:
# you could also change to class Rectangle: def __init__(self, w, h): self.w = w self.h = h rect = Rectangle(7, 8) print(rect.w) 
# the verbose syntax for setting initial attribute values is: 
# self <which is a placeholder for instance-names> . attribute-name = attribute <parameter of __init__>

# Using single (or even double) letter names might seem tempting, 
# but are arguably a bad habit to fall into if you are considering taking up programming professionally (or contributing to open source projects online). 
# Most lint tools require names or identifiers to be 3 characters or longer, and stylistically using full words is considered better practice vs. algebraic symbols. 
# Just some things to keep in mind. It might not seem like a big deal, but bad programming habits can catch on quickly early on and will be hard to break later.


# I think is if you wanted an instance to hold a list of values such as a manager and how many employees he's in charge of 
class Manager: 
    def __init__(self, list_emp = None): 
        if list_emp == None: 
            self.list_emp = [] 
         else: 
            self.list_emp = list_emp # because you don't generally want to pass mutable data types such as a list in the init method.
#

# Example:
class Dog:
    def __init__(self,color_color,name)
    self.Dogs_color = color_color 
    self.Dogs_owners_name = name 
    
my_class = Dog("white","abby") 
print(my_class.Dogs_color)
print(my_class.Dogs_owners_name) # white abby 
        

# Example:
class Rectangle: 
    def __init__(self, width, height, color): 
        self.width = width 
        self.height = height 
        self.color = color 
        
rect = Rectangle(7, 8, "blue") 
print(rect.color)               # blue now it works


# Example:
class Monster(): 
    def __init__(self): 
        self.name = "" 
        self.health = 0 
        self.weight = 0 
     def decrease_health(self, amount): 
        self.health -= amount 
        if self.health <= 0: 
            print("Monster died") 
        else: print("Monster has", self.health, "HP") 
            
dranagul = Monster() 
dranagul.health = 50 
dranagul.decrease_health(10) 
dranagul.decrease_health(40) # Output: Monster has 40 HP Monster died


# Example:
class Rectangle: 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
        self.area = width * height 
        
rect = Rectangle(7, 8) 
print(rect.area) # prints 56
# https://docs.python.org/3/tutorial/classes.html#

# Example:
class Rectangle: 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 
        
rect = Rectangle(7, 8) 
rect.color ="Blue" 
print(rect.color)


# Example:
class Rectangle: 
    def __init__(self, width, height, color): 
        self.width = width 
        self.height = height 
        self.color = color 
        try: 
            rect = Rectangle(7,9) 
        except: 
            NameError 
        try: 
            rect = Rectangle(rect.color) 
        except: 
            AttributeError 
            
rect = Rectangle(7,9,"red") 
print("Rectangle has \nwidth :", rect.width ,"\nheight:", rect.height, "\n""and the color is", rect.color, "It works" )


# Example:
#classes - class means the design of the car 
# arguments means its specifications, also called attributes or parameters ,here the arguments are colour,variant and no. of seats 
# objects are created using the class design,they are also called as instances 
# here 'a','b' and 'c' are three cars of same class i.e, three cars of same design but different specifications 
# the use of self is explained below. 
class cars: 
    def __init__(self,colour,variant,seats=4): 
        self.colour=colour 
        self.variant=variant 
        self.seats=seats 
     def model(self): 
        print('convertible') 
        
a = cars('red','petrol',4) 
# here self takes the object name,it refers to the object name everytime you create a new object 
# self.colour=colour means a.colour=red #self.variant=variant means a.variant=petrol 
# self.seats=seats means a.seats=4 b=cars('blue','diesel',2) c=cars('yellow','electric') print(a.colour) print(b.variant) print(c.seats) a. Model() 
# here car 'c' we did not specify the no of seats, so it takes default.

# Example:
# We can do several things with the attributes: 
# give them as parameters, use default values if none is pass as an argument, 
# create them inside the class with a pre-defined value or as the result of a math operation: 
class Rectangle: 
    def __init__(self, width=1, height=1): 
        # Two parameters with 1 as default to both self.width = width 
        # Value form the argument or 1 self.height = height 
        # Value form the argument or 1 self.color = 'blue' 
        # Attribute created with any value self.area = width * height 
        # Attribute created out of a math formula 
rect = Rectangle() 
print(rect.width, rect.height, rect.area, rect.color) 
rect = Rectangle(5) 
print(rect.width, rect.height, rect.area, rect.color) 
rect = Rectangle(5, 2) 
print(rect.width, rect.height, rect.area, rect.color) 
            

# Example:
class square: 
    def __init__(self,width,height): 
        self.width = int(input("please enter the width:\n")) 
        self.height = int(input("please enter the height:\n")) 
        
sel.area = width * height 
print("the area of the square is:\n") 
print(sel.area)


# Example:
class Rectangle: 
    def __init__(self, width, height,color): 
        self.width = width 
        self.height = height 
        self.color = color 
        
rect = Rectangle(7, 8,"blue") 
print(rect.color)               # blue
        
# AttributeError is caused by trying to access unknown attributes?




    
#SINIFLAR
#bi class oluşturcaz
"""
class Person: #büyük harfle başla
    pass #pass keywordu yer tutucu olarak kullanılabilir, pass yazmadan geçer 
    #normalde att ya da met kullanmak gerekli
    #class kapsamı içinde tanımlayabileceğimiz ifadeler
    # attributes        # methods

#bi object tanımlayalım
p1 = Person() #küçük harfle başla
    #person classını p1 objesini tanımlamak için kullanıcaz #değişken tanımlamaya benziyor 
p2 = Person() #ikinci bi pbje daha, tipi yine person
print(p1) #p1e bellek üze bi adres verir #objectin de bi person tipi old söyler
print(p2) #p1in aksine farklı bi adreste tanımlanır
print(type(p1)) #tiplerini yazdırırsak class ve person classı olur bu class str ya da int gibi 
print(p1 == p2) #dersek bunlar farklı old gösteirir False
"""

# ATTRIBUTES
# Class Attributes
class Person:
    #pass artık ihtiyaç yoksilelim
    address = 'no info' 
# const içinden o objedeki bilgiyle ilgili bi adres bilgisi eklemek yerine 
# yani addressi direk class att olarak tanımlayabiliriz çünkü her zman kullanmıyacağız
#ki gereken bilgileri yani olmazsa olmazları obj att yapmak daha iyi

# Object Attributes
    #constructor method ile obj attr yapıcaz (yapıcı metod)
    #method tanımlaması yaparsak
    def __init__(self, name, year): #const örnek init methodu
#init methdunun parametreleri olacak
#ilki self isminde bi parametre
#classdan türettiğimiz p1 ya da p2 objesi burda self 
#yani obj üzerine bi şey yapılacaksa burda self kullanılacak
#diğer özelliklerde self sonrası gelir ,name , age gibi
#userın gönderdii name ve year bilgileri aktarılacak
        self.name = name
        self.year = year
#önemli olan p1 objesinden self.name veye .year alanına ulaşılabiliyor olmak
#init oluşturulan her bir obje için mutlak çalıştırıyor almasından yapıcı metod
#cons gönderdiğimiz bilgiler böylece obje içinde yer alacak

        print('init metodu çalıştı')
#self için parametre göndermeye gerek yok kendiliinden p1 ve 2 objelerini temsil ediyor
p1 = Person(name ='Jack', year = 1990) #('init metodu çalıştı')
#parametreleri gönderirken isimlerini de belirtebiliriz okunabilirlik için  name= ...
p2 = Person(name = 'John', year = 2000) #('init metodu çalıştı')
#update etmek istediğimizde peki
p1.name = 'George'
p2.address = 'London'

#p objelerinin değerlerini ekrana yazdırırsak
#aşağıda yapılan işlemin adı 
#accessing object attributes
print(f'p1 name: {p1.name}, year: {p1.year}, address: {p1.address}')
print(f'p2 name: {p2.name}, year: {p2.year}, address: {p2.address}')



print(p1)
print(p2)
