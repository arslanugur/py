# SECTION 1
# Inheritance provides a way to share functionality between classes.
# Imagine several classes, Cat, Dog, Rabbit and so on. 
# Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name).
# This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
# Subclass and superclass in python... Meanwhile, subset and superset in math
# To inherit a class from another class, put the superclass name in parentheses after the class name.
# Example: 
class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()




# Example:
class Animal: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 

class Cat(Animal): 
    def sound(self): 
        print("Purr...") 
        
class Dog(Animal): 
    def sound(self): 
        print("Woof!") 
        
class Pig(Animal): 
    def sound(self): 
        print("Oink!") 

babe = Pig("Babe", "pink") 
print(babe.color) 
babe.sound()


# What you are saying totally makes sense. But this is just an example. 
# You can find another one, when you need both INHERITANCE and SPECIFIC methods. 
# E.g. add new class Human(Animal) and add new method def itsskills(self). 
# Rather than having this "itskills" for every Animal, you will have this itskill for Human only.

# What if I want the sub-class to have new attributes that the superclass doesn't have? 
# For example, suppose I want an "Animal" class with "color" and "name" attributes, 
# but then I want my "Dog" class to have a "tricks" attribute and my "Cat" class to have a "mice caught" attribute? 
# Would the sub-classes look like this? 
class Dog(Animal, tricks): 
    def __init__(Animal, tricks): 
        self.tricks = [] 

class Cat(Animal, mice_caught): 
    def __init__(Animal, mice_caught): 
        self.mice_caught = 0
#
# Nope. They need to look like this as second way: 
class Dog(Animal): 
    def __init__(self, name, color): 
        super().__init__(name, color) 
        self.tricks = [] 
        
class Cat(Animal): 
    def __init__(self, name, color, mice_caught=0): 
        super().__init__(name, color) 
        self.mice_caught = mice_caught 
# Little explanation: super() - calls a superclass (we can call methods or fields with it) self.tricks=[] and mice_caught=0 
# Default initial field and default attribute self.mice_caught = mice_caught 
# creating a field for this class only With above classes we can create objects like this: 
# cat1 = Cat("Vincent", "white") # mice_caught here is 0 (because it's default) cat2 = Cat("Blackwood", "black", 20) 
# # mice_caught == 20 cat3 = Cat("Yammy", "coral", mice_caught=5) 
# same as above, but here we call default attribute by name BTW calling default attribute by the name created 
# because we can create functions, that takes unlimited (figuratively) arguments in it.


# Example:
class Animal(): 
    def __init__(self,name,color): 
        self.name = name 
        self.color = color
        
class Cat(Animal): 
    def __init__(self,name,color,breed): 
        self.breed = breed 
        
taffy = Cat('Taffy','White','Persion') 
print(taffy.breed)                      # Persion
                

# Example:    
class Animal: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color
        
class Cat(Animal): 
    def purr(self): 
        print("Purr...") 
        
class Dog(Animal): 
    def bark(self): 
        print("Woof!")     
    def attitude(self): 
        print("tricks") 
        
fido = Dog("Fido", "brown") 
print(fido.color) 
fido.bark() 
fido.attitude()


# Python supports inheritance, it even supports multiple inheritance. 
# Classes can inherit from other classes. 
# A class can inherit attributes and behaviour methods from another class, called the superclass. 
# A class which inherits from a superclass is called a subclass, also called heir class or child class.

# Example of Inheritance in real life
# - Father gives his property to child, father got that properties from child’s grandfather, 
# so child is the taker and father is givers, hence father works as a base class and child as derived class,
# • you can explain is that the child couldn’t give its property to father so Inheritance is one sided 
# • why it is needed? so you can explain like same properties needed in multiple class you need not to write multiple times

# Example:
class Animal: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
        
class Cat(Animal): 
    def purr(self): 
        print("Purr...") 
        
class Dog(Animal): 
    def bark(self): 
        print("Woof!") 
        
billy = Cat("billy", "white") 
fido = Dog("Fido", "brown") 
print(fido.color) 
fido.bark() 
print(billy.name) 
billy.purr()

# https://www.python-course.eu/python3_inheritance.php

# So basically, my take on this, is that as long as each class inherits from the superclass, whatever is in the superclass, subclasses would have access to.

# easier code: 
class Animal: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
#
class Cat(Animal): 
    def voise(self): 
        print("Purr...") 
#
class Dog(Animal): 
    def voise(self): 
        print("Woof!") 
#    
fido = Cat("Fido", "brown") 
print(fido.color) 
fido.voise() 
fido=Dog("Fido","brown") 
print(fido.color)
fido.voise()


# Example: Which piece of code shows a new class Spam inheriting from Egg?
class Spam(Egg):
# Spam inheriting from (Egg)? "Egg" is the object from which the "Spam" is coming from. So the answer is... class Spam(Egg).

# Syntax: class Subclass(Superclass) OOP concept: subclasses inherit from superclasses.

# The answer is : class Spam(Egg): Explanation: 
# With the function "class", you define a class, then you name it "Spam", 
# but you call( ) for "Egg", which the question says it's a class itselfs.


# Example:
class Person: 
    def __init__(self, fname, lname): 
        self.firstname = fname 
        self.lastname = lname 
        
    def printname(self): 
        print(self.firstname, self.lastname) 
# Use the Person class to create an object, and then execute the printname method: x = Person("John", "Doe") x.printname()


# SECTION 2
# A class that inherits from another class is called a subclass.
# A class that is inherited from is called a superclass.
# If a class inherits from another with the same attributes or methods, it overrides them. 
# Example:
class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")       #

husky = Dog("Max", "grey")
husky.bark()
# In the example above, Wolf is the superclass, Dog is the subclass.


# (1): Basically, Wolf got created as a class, with ATTRIBUTES (pieces of data that MUST be associated WITH each and every instance of the class) name and color, 
# and with just a single METHOD, namely the bark method, which just prints out "Grr...". 
# THEN, a class called Dog got created, and we made it INHERIT the Wolf class, making the Wolf class become the superclass here 
# and the Dog class become the subclass (like how child INHERITS characteristics off his parents, 
# like say strong eyesight and being tall, and parents, in some sense atleast, are "super" whereas the child is "sub"-ordinate). 
# (2): Now, because Dog class INHERITED FROM the Wolf class, what it means is that the ATTRIBUTES + METHODS of the Wolf class get "copy and past" to the Dog class. 
# So, each and every instance of not only the Wolf class but ALSO the Dog class MUST be associated with the ATTRIBUTES of name and color. 
# Additionally, for an instance of EITHER the Wolf or Dog classes, it is possible to use the method bark, since both classes now are "equipped" with it. 
# It doesn't matter if it's Wolf or even Dog class, STILL the bark METHOD will work! Then, "def bark(self):" came in after class "Dog(Wolf):". 
# BUT the Dog class was ALREADY "equipped" with the bark ★★METHOD★★, so it means that here actually the bark METHOD is being OVERWRITTEN, specifically for the Dog class!
# Hence why we get Woof output when bark method got deployed with an instance of the Dog class, namely the "husky" instance of the Dog class, 
# which in turn we had defined to come with the attributes of "Max" as its name and "grey" as it's color.


# Example:
class Wolf: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
    def bark(self): 
        print("Grr...") 
        
class Dog(Wolf): 
    def bark(self): 
        print("Woof") 
        
husky = Wolf("Max", "grey") 
husky.bark() 
husky = Dog("Max", "grey") 
husky.bark() # OUTPUT: Grr... Woof 
# --- Using the example above, I see it as in that one makes clear what class they are using by mentioning "Wolf" or "Dog" in the object husky.
                            

# When we inherit the superclass, it's __init__ method is also inherited. 
# But what if we want to add extra parameters in addition to the parent class's parameter. 
# class Person: def __init__(self, name, age, gender ): self.name = name self.age = age self.gender = gender class Student(Person): def __init__(self, name, age, gender, stream, section, house_name): Person.__init__(self, name, age, gender ) self.stream = stream self.section = section self.house_name = house_name that's it! When we define subclass's __init__ method it overrides superclass's __init__ method. This is why we need to call the __init__ method of the superclass. :--- Person.__init__(self, ...)
                

class Wolf: 
    def __init__(self, name, color): 
        self.setname = name 
        self.setcolor = color 
    def bark(self): 
        print("Grr...") 
        
class Dog(Wolf): 
    def ibark(self): 
        print("Woof") 

husky = Dog("Max", "grey")
husky.ibark() # Woof

# Two things cleared up this section for me: 
# (1) A Patric pointed out the "it" they refer to is "subclass methods or attributes" 
# (2) what this code is specifically showing is that bark() is defined twice. 
# The first time it is defined from the superclass Wolf, the second time from the subclass Dog. 
# This opens up a question- when bark is called from an object /instance in the subclass Dog- what rules? 
# The answer is- whichever method is in the subclass Dog. 
# This was counter-intuitive for me, because in the previous lesson we learned that subclasses get the same attributes as superclasses. 
# On the other hand, using wolves and dogs as examples, it makes intuitive sense. 
# Dogs are a subclass of wolves because they share certain fundamental attributes in common, 
# but dogs have specific functionalities (barking lovingly into owner's eyes) that wolves do not have. 
# So the later generation subclass should have their versions of methods overiding earlier generations.,

# Example:
class cat: 
    def __init__(self,color,name,legs,fur,gender): 
        self.color=color 
        self.name=name 
        self.legs=legs 
        self.fur=fur 
        self.gender=gender 
        
    def purr(self):
        return "meawww" 
    def description(self):
        return "{} {} {} {} {} {} {} {}".format("she is a",self.gender,"cat with",self.color+" "+ self.fur,"fur","and",self.legs,"legs") 
    
kobala = cat("black","kobala",4,"short","female") 
print(kobala.color) 
print(kobala.purr()) 
print(kobala.description()) 
print(kobala.__dict__)

# Example:
class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)    #

B().method()

# Q: Why is the last line "B().method()" and NOT simply "B.method()"??? 
# A: Because class A has NO ATTRIBUTES at all! 
# Class B inherited from class A, so the attributes+methods of class A got "copy & pasted" to B. 
# Hence, class B has NO ATTRIBUTES at all, just like class A, simply the method "method()" that prints out 1, which in turn is overwritten by "method()" that prints out 2. 
# Now, suppose that instead of the FINAL line of code in the question's example, 
# we've got the following two lines, where right side of first line has empty parentheses just because class B has NO ATTRIBUTES at all. 
# some_instance = B() some_instance.method() "B().method()" just simplifies the above 2 linea of code into a single one really - DRY principle I guess. 
# Hopefully, it now makes sense why we have the final line of code in the question's example as ""B().method()" rather than "B.method()".


# Example:
class Dog: 
    legs = 4 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
        
fido = Dog("Fido", "brown") 
print(fido.legs)    # 4
print(Dog.legs)     # 4

# Actually, this has nothing to do with class B not having any attributes. 
# Basically what happened is an instance of B got created but wasn't stored in a variable, 
# being "used on the fly" (method() got called in the same line of instantiation). 
# Here, try this code: 
class SomeClass: 
    some_attribute = 'my attribute' 
    def some_method(self): 
        print('my method')

SomeClass().some_method()
# You can access the class def's attribute without brackets, but for the methods, you need them. 
# Pay attention to the self parameter, which is passed in the methods. Without a class instance no 'self', hence the instantiation with ().


# this is a great explanation! I didn't know attributes could be accessed without instantiating a class. 
# After thinking about this, though, I noticed one should be careful about doing so, 
# because some attributes are only declared in the __init__ method, and you must have an instance object to access those. 
# I guess these attributes would be analogous to Java's non-static attributes. 
# So I came up with this: 
class SomeClass: 
    static_attr = 'this does not need instantiation' 
    def __init__(self): 
        self.nonstatic_attr = 'this needs instantiation' 
        print(SomeClass.static_attr) # gets printed print(SomeClass.nonstatic_attr) 
        # raises AttributeError print(SomeClass().nonstatic_attr) # gets printed
#

# Example:
class Wolf: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
    def bark(self): 
        print("Grr...") 
        
class Dog(Wolf): 
    def bark(self): 
        print("Woof") 

husky = Dog("Max", "grey") 
husky.bark() 
Dog("Max", "grey").bark() # Woolf Woolf


# Example:
class Wolf: 
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
        
    def bark(self): 
        print("Grr...") 
        
class Dog(Wolf): 
    def bark(self): 
        print("Woof") 
        
husky = Dog("Max", "grey") 
husky.bark() # here the bark by wolf is "Grr..." 
# again bark is def by dog as "Woof" 
# so the by call bark it gives the #recently assigned value. 
# in question section the method is #called for B() refers that it has #no attributes.
                    

# Clear explanation why ' 1' does not get printed out .class A and class B have same function name( i.e; method) and class B inheriting properties of class A . 
# Now class B defining a function def method(self) (with same name as class A) which overwrite the function of class A as a result '2' will be printed. 
# In short overwrite of a function gives output 2.

# let me explain why ' 1' does not printed .class A and class B have same function name( i.e; method) and class B inheriting properties of class A . Now class B defining a function def method(self) (with same name as class A) which overwrite the function of class A as a result '2' will be printed. In short overwrite of a function gives output 2

# SECTION 3
# Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class.
# Example:
class A:
    def method(self):
        print("A method")   # 
    
class B(A):
    def another_method(self):
        print("B method")   #
    
class C(B):
    def third_method(self):
        print("C method")   #
    
c = C()
c.method()
c.another_method()
c.third_method()
# However, circular inheritance is not possible.

# (1): Class A has NO ATTRIBUTES at all, but it does have a SINGLE method, namely "method()", which takes no arguments at all and prints out "A method". 
# Attributes + Methods of class A are inherited by class B, so it means that the attributes + Methods of class A get "copy & pasted" onto class B. 
# Hence, now class B is equipped with now 1 but rather 2 Methods: "method()" which prints "A method" AND "another_method()" which prints "B method".
# (2): Next, Attributes + Methods of class B (2 Methods and no attributes whatsoever) get "copy & pasted" onto class C. 
# Hence, class C now has 3 Methods and no attributes, and these 3 Methods which are the following: "method()" which prints "A method", 
# AND "another_method()" which prints "B method", AND "third_method()" which prints "C method". 
# So, class C comes equipped with ALL these 3 ↑ Methods actually!
# Hence, why we're totally ALLOWED to use absolutely ANY of these 3 Methods for any instance/object of the class C, such as the instance"c" they've got there in the example.

# I have a simple explanation of the lesson: class A: method - >A method class B(A): 
# another method - > (A method) and B method class C(B): 
# Third method - > (A method), (B method) and C method c = C() -> " C() contains (in other words, inherits") all methods above", 
# so, c.method() c.another_method() c.third_method() The output is: A method B method C method
                
# Circular reference means both classes inherit from each other and it's prohibited.
# Inheritance was used to show parent-child relationship 
# and therefore it's obvious that we couldn't have a class which is both parent and child class to the same class at the same time.
# Circular class Pikachu ( Raichu ) ⚡ class Raichu ( Pikachu ) ⚡ ✅ 'Top-down' hierarchy class Raichu ( Pikachu ) ⚡ class Pikachu ( Pichu ) ⚡ class Pichu ( Pokemon )

# It's interesting to note that in this way, in Python you can have the so called "diamond problem" (sometimes referred to as the "deadly diamond of death"). 
# This refers to the ambiguity that arises "when two classes B and C inherit from a superclass A, and another class D inherits from both B and C. 
# If there is a method "m" in A that B or C (or even both of them) )has overridden, 
# and furthermore, if does not override this method, then the question is which version of the method does D inherit? It could be the one from A, B or C."

# More example: 
class Animal:
    def __init__(self, name, color): 
        self.name = name 
        self.color = color 
    def move(self): 
        print('moving...') 
        
class Wolf(Animal): 
    legs = 4 
    def bark(self): 
        print('barking...') 
        
class Dog(Wolf): 
    def play_dead(self): 
        print('playing dead...') 

dog_1 = Dog('Shadow', 'Black') 
dog_1.move() # moving... dog_1.bark() # barking... dog_1.play_dead() # playing dead... print(dog_1.legs) # 4



# Two things to learn here. 
# 1. It doesnt matter if you call the class directly or transform it into a variable first (its just done fore #style reasons iI guess). 
# 2. if you define the same mathods with the same name within a Class these will be used not the one #where the class inherits from . 
# See example; 
class A: 
    def method(self): 
        print("A method") 
        
class B(A): 
    def another_method(self): 
        print("B method") 
        
class C(B): 
    def method(self): 
        print("AA method") 
    def another_method(self): 
        print("BB method") 
    def third_method(self): 
        print("C method") 
        
C().method() 
C().another_method() 
C().third_method()  # giving us the output: AA method BB method C method

# circular inheritance means both classes inheriting one another. means class A inherits B and clasa B inherits A .

# i.e class A inherit class B class B inherit class C class C inherit class A

# it seems that circular inheritance is not allowed from a subclass to superclass, which means that a subclass may inherit from a superclass, 
# however, a superclass cannot inherit back from the same subclass it has been inherited from it

# What is the result of this code? 
class A: 
    def method(self): 
        print(1) 
        
class B(A): 
    def method(self): 
        print(2) 
        
B().method() # when B().method() runs，result is 2 from B AND this example shows c.method runs, result is from class A WHY?


# Example:
class A:
  def a(self):
    print(1)

class B(A):
  def a(self):
    print(2)    # 

class C(B):
  def c(self):
    print(3)

c = C()
c.a()

# the function in subclass override the one in superclass

# (1): We define the class A which comes equipped with no attributes at all but with the a() method that takes no arguments and prints 1. 
# Then, we define the class B to inherit A class, so attributes + methods of A class get "copied & pasted" onto B class. 
# So, class B comes equipped with method a() which takes no arguments and prints 1. 
# However, we define the class B to have the method a() that takes no arguments and prints 2, 
# but this certainly OVERRIDES the a() method it had previously received due to inheritance from the A class.
# (2): Next, we define C class to inherit from B class, so attributes + methods of B class get "copied & pasted" onto C class. 
# Hence, class C comes equipped with the method a() which takes no arguments and prints 2, as well as the method c() that takes no arguments and prints 3. 
# We define an an instance of the C class which has no attributes at all, 
# but because it's an instance of the C class, we certainly are ALLOWED to deploy the ANY of the 2 methods, a() and c(), that come equipped with the C class. 
# We choose to deploy the a() method with the instance "c" of class C, hence using the a() method of class C actually. Therefore, we get 2 as the output.


# SECTION 4
# The function super is a useful inheritance-related function that refers to the parent class. 
# It can be used to find the method with a certain name in an object's superclass.
# Example:
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()
# super().spam() calls the spam method of the superclass.
# Output:
# 2
# 1


# This code modification might make things more clear. And because you can't go wrong with superspam! 
class A: 
    def spam(self): 
        print(1) 
        
class B(A): 
    def spam(self): 
        print(2) 
    def superspam(self): 
        super().spam() 

B().spam() 
B().superspam()

# Example:
class Human: 
    def __init__(self,name,size): 
        self.name=name 
        self.size=size 
    def present(self): 
        print("{0}: {1} cm".format(self.name,self.size)) 
        
class Worker(Human): 
    def __init__(self,name,size,job): 
        super().__init__(name,size) 
        self.job=job 
    def present(self): 
        super().present() 
        print(self.job) 
        
w = Worker("Bob",185,"trader") 
w.present()
                            
# Example:
class A: 
    def spam(self): 
        print(1) 
        
class B(A): 
    def spam(self): 
        print(2) 
        
class C(B): 
    def spam(self): 
        print(3) 
        super().spam() 
        super().super().spam() 
        
C().spam() # Output: 3 2 Traceback: <AttributeError> 

# But this does: 
class A: 
    def spam(self): 
        print(1) 
        
class B(A): 
    def spam(self): 
        print(2) 
    def getSuper(self): 
        return super() 
        
class C(B): 
    def spam(self): 
        print(3) 
        super().spam() 
        super().getSuper().spam() 
        
C().spam() 


# Example:
# For the people who can't understand why there is a "2" and a "1" printed. 
# Basically in the end of the code there is a "B().spam()" which makes the "Class B(A)" code run, right? 
# So if you look it up you will see that it says print (2) first and then ~the trick part~ it shows "super().spam()." 
# This will make it go to the Class A {the superclass} and run its "print (1)" 
# because that is what its "def spam" in Class A does, it prints the number


# Example:
class A: 
    def spam(self): 
        print(1) 
        
class B(A): 
    def spam(self): 
        print(2) 
        super().spam() 
        
class C(B): 
    def spam (self): 
        print(3) 
        super().spam() 
        
C().spam() # output: 3 2 1 


# Example:
class A: 
    def spam(self): 
        print(1) 
    def parent(self): 
        print("I am parent") 
        
class B(A): 
    def spam(self): 
        print(2) 
        super().spam() 
        super().parent() 
        
c=B() 
c.spam() # output: 2 1 I am parent


# Example:
class A: 
    def spam(self): 
        print(1) 
        
class B(A): 
    def spam(self): 
        print(2) 
        super().spam() 
        
B().spam() # OUTPUT: 2 1 
# Second Example:
class A: 
    def spam(self): 
        print(1) 

class B(A): 
    def spam(self): 
        print(2) 
        
B().spam() # OUTPUT: 2 # It seems like with super(). it calls both of the classes: it prints class A and B, so 2 and 1.
                                                
# What is the superclass of a class?    The class it inherits from      # Superclass of a class == Father of a child        
# A super class is simply what the normal class inherits from. 

# if in the case of the indirect inheritance the superclass was considered the first class to inherit its attributes and methods or the last one to inherit them, 
# so I ran the following code and that helped me understand the answer to the above question. 
class A: 
    def method(self): 
        print("A method") 
        
class B(A): 
    def method(self): 
        print("B method") 
        
class C(B): 
    def method(self): 
        print("C method") 
        
class D(C): 
    def method(self): 
        print("D method") 
        super().method() 
        
d = D() d.method() # D method C method # as you can see, for this example the superclass for D would be class C


# The class from which a class inherits is called the parent or superclass. 
# A class which inherits from a superclass is called a subclass, also called heir class or child class. 
# Superclasses are sometimes called ancestors as well.







# Nesne tabanlı prpgramlama  - Kalıtım
# Classların birbirinden miras almasıyla olan bi durum

# Person class; name, surname, age, eat() metodu, walk() metodu
# Student ya da Teacher classes; Person class görevlerini bunlara da olmasını isterim
# Student(Person) , Teacher(Person) tüm özellikler onlarda da var
# Person için tanımlanan bütün özellikler attributes ve methods Student ve Teacher parçası olcak
# yani aynı özellikleri tekrar tekrar oluşturmaya gerek yok
# Student ya da Teacher classa öğrenci/öğretmen özellikleri de eklenebilcek
# Person sadece standard yani temel sınıf
# Animal() --- Dog(Animal), Cat(Animal), Horse(Animal)
# Example:
class Person():
    def __init__(self):
        print('Person Created')

class Student(Person):
    def __init__(self):
        Person.__init__(self)  #stu, person init metodunu bu şekilde alır
        print('Student Created')


#persondan türetilen bi p1 objesi tanımlarsak
#p1 = Person()
s1 = Student() #Person Created
#student objesini çağırmak personın init metodunu tekrar çağırmak demek
#Studenta bi init metodu eklersek



#SECOND PART
class Person():
    def __init__(self, fname, lname):
        self.firstname = fname #bi alan türetip dışardan gönderdiğimiz firstname atamak istesin
        self.lastname = lname
        print('Person Created')

    def who(self):
        print('I am a person')

    def play(self):
        print('I am playing..')

class Student(Person):
    def __init__(self, fname, lname, snumber):
        Person.__init__(self, fname, lname) #person bigilerini alması gerekir temel sınıf çünkü
        self.studentNo = snumber
        print('Student Created')

    #OVERRIDE: aynı isimdeki obj att metodun temel sınıftaki class att metodu ezmesi
    def who(self):
        print('I am a student') #çünkü artık personın o özelliğine gerek yok

    def say(self):
        print('Highway to Hell')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)  # Person.__init__(self, fname, lname) aynısı ama daha kısası 
        self.branch = branch

    def who(self):
        print(f'I am a {self.branch}')

    def say(self):
        print('Johnny B. Goode')


p1 = Person('Guitar', 'Player')
s1 = Student('Angus', 'Young', 1)
t1 = Teacher('Chuck', 'Berry', 'GTeacher')
print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNo))
#str yerine f str de kullanabilirdik

p1.who()
s1.who() #stu üzerinden de aynı elemana ulaşabiliriz
t1.who()

p1.play()
s1.play()
s1.say()
t1.say()


