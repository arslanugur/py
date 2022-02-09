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



https://www.sololearn.com/learning/1073/2467/5126/1
    comments




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
