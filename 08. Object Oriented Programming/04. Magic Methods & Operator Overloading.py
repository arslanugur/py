# x.__setitem__(y, z) 
    # x => array -- to affect
    # __setitem__ => Magic method 
    # y => index -- to target
    # z => value -- to assign
    
    
# SECTION 1: Magic Methods
# Magic methods are special methods which have double underscores at the beginning and end of their names.
# They are also known as dunders.
# So far, the only one we have encountered is __init__, but there are several others.
# They are used to create functionality that can't be represented as a normal method.

# What is the magic method for creating an instance - __init__

# One common use of them is operator overloading.
# This means defining operators for custom classes that allow operators such as + and * to be used on them.
# An example magic method is __add__ for +. 
# Example:
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)   # 8
print(result.y)   # 16

# The __add__ method allows for the definition of a custom behavior for the + operator in our class.
# As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
# Once it's defined, we can add two objects of the class together.


# The magic method allow you to program the way a simple operator would work with your class or object. 
# This allows you to obtain complex operations within objects using known symbols like +, -, /, % etc. 
# I guess this is because there's no way python would know what an operation like object _a + object_b should return... an int? a str? a bool? a None? 
# should it add this to this? or use str operations? 
# so it gives you the liberty of designing the operation for the desired class. 
# I think the most helpful example is the object Vector2D, in which the + symbol is programmed to add the value of the x and y of both items respectively. 
# Without explicitly telling python what the + means in this case, then it would surely return something that wasn't intended to. 


# __methodName__ are mostly used to override operators behaviours. 
# If you call 21+21 Python calls behind the scene 21.__add__(21). 
# And the language has already implemented this __add__ method for the Integer class to perform an addition. 
# this means if you decide to override it you can now perform whatever you like for the '+' sign. 
# This case is quite rare, but when you deal with objects python has no idea how to add ra(or other opetor) two Dogs. 
# So you can decide that adding to dogs results in adding their age attribute for example. I hope I was clear PS: 
# When you have a 'r' before the method name like __radd__ this is the method which is called 
# if the left operand does not support the __add__ and operands aren't the same type. 
# Take a look at the doc if you're interested (https://docs.python.org/2/reference/datamodel.html#object.__radd__)


# (1): Recall that, any instance in the class Vector2D comes equipped with 2 attributes, namely x and y. 
# The following 2 lines of code create two instances of the class Vector2D - the instance named "first" comes with the attributes of x=5 and y=7, ,
# and the instance named "second" comes with the attributes of x=3 and y=9. 
# [These attributes are just pieces of data associated to the instance, 
# like how we can have a dog class with two instances in it, fido and Max, with the attributes of say, color, name and number of legs.] 
# first = Vector2D(5, 7) second = Vector2D(3, 9) The above 2 lines of code get followed by the line of code: result = first + second
# (2): Now, according to what @Benoit said, behind the scenes, every time u have a +, Python INTERPRETS the + as the method __add__ 
# So, for example, 21 + 35 would be interpreted by Python as 21.__add__(35) 
# However, we override this method, and tailor it to exactly what we personally desire. 
# The exact way we re-define it for our purposes is revealed to us by the following two lines of code that apply as part of the class Vector2D definition. 
# def __add__(self, others): return Vector2D(self.x + other.x, self.y + other.y) 
# Therefore, the "result = first + second" line of code gets interpreted as follows: result = first + second result = first.__add__(second) 
# Now, looking at the way we defined the __add__ method, and considering self = first and other = second, based on what @Andrii Pozdieiev said, we get the following.
# (3): result = Vector2D(first.x + second.x, first.y + second.y) 
# Now, remember how we earlier learnt that say if you had an instance, like say, fido, 
# and you had defined it to have the attribute of color = grey, then the code "fido.color" would RETURN the color-attribute associated to to the instance fido, which is grey? 
# Likewise, "first.x" would RETURN the x-attribute associated to the instance first, which is equal to 5, according to how we defined had defined it. 
# Hence, first.x = 5, and similarly second.x = 3, first.y = 7 and lastly second.y = 9. 
# Therefore, we get result = Vector2D(5 + 3, 7 + 9) result = Vector2D(8, 16) 
# So, result is an instance of the class Vector 2D, with the attributes of x=8 and y=16. 
# Consequently, result.x RETURNS the x-attribute of the result instance, which is 8, and hence print(result.x) would print 8. 
# Similarly result.y RETURNS the y-attribute of the result instance, which is 16, and hence print(result.y) would print 16.

        
# Python has many special methods like __add__, see the list below. 
# +, __add__(self, other), Addition; 
# *, __mul__(self, other), Multiplication; 
# -, __sub__(self, other), Subtraction; 
# %, __mod__(self, other), Remainder; 
# /, __truediv__(self, other), Division; 
# <, __lt__(self, other), Less than; 
# <=, __le__(self, other), Less than or equal to; 
# ==, __eq__(self, other), Equal to; 
# !=, __ne__(self, other), Not equal to; 
# >, __gt__(self, other), Greater than; 
# >=, __ge__(self, other), Greater than or equal to; 
# [index], __getitem__(self, index), Index operator; 
# in, __contains__(self, value), Check membership; 
# len, __len__(self), The number of elements; 
# str, __str__(self), The string representation Magic Method. dunders: abbr of double underscores； Operator Overloading: custom class


# So I finally understood! sorry if it has been explained before but I just want also confirm I'm right. 
# The magic method is simply telling the interpreter how to handle the operation between the two objects. 
# You are adding functionality to your objects by allowing to operate between them. 
# It doesn't matter if you use __add__ or __div__ or anything else as long as you match the operator with the magic method, 
# the operation will do whatever you tell it to do in the class. 
# I can use the the __add__ magic method and return the division of 2 numbers. 
# To prove my statement above, I wrote this code to show it works. 
# Without cheating, let me know what you think the output is. 
class SpecialString: 
    def __init__(self, cont): 
        self.cont = cont 
    def __truediv__(self, other): 
        return self.cont + other.cont 
    
no1 = SpecialString(4) 
no2 = SpecialString(2) 
print(no1 / no2)            # 6


# It has now started to make sense for me after reading through the comments here. 
# These two lines of codes first = Vector2D(5, 7) second = Vector2D(3, 9) just create two instances of the Vector2D class with the passed attributes(arguments). 
# Now this method __add__ inside the class Vector2D returns an instance of the class instead of values. 
# def __add__(self, other): return Vector2D(self.x + other.x, self.y + other.y) This is where the operator '+' is 'overloaded' to operate on objects in a specified manner. 
# Now this magic method is called in this line of code result = first + second We have to read this as other comments have pointed out as: 
# result = first().__add__(second): 
# With this call, the parameters (x & y, in this case 5 & 7) of the object 'first' becomes the parameters of 'self'(as the method is called on the object 'first') 
# and the parameters (3 & 9) of the object 'second' becomes the parameters of 'other' defined in the method. 

# I have a theory of why the code is so confusing to look at. If you are having trouble try looking at this. 
class Vector2D: 
    def __init__(self, x): 
        self.x = x 
    def __add__(self, other): 
        return Vector2D(self.x + other.x) 
    
first = Vector2D(5) 
second = Vector2D(3) 
result = first + second 
print(result.x) # 8



# SECTION 2
# More magic methods for common operators:
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |

# The expression x + y is translated into x.__add__(y).
# However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
# There are equivalent r methods for all magic methods just mentioned.
# Example:
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

# Output:
# spam
# ============
# Hello world!

# In the example above, we defined the division operation for our class SpecialString.

# If you call a magic method on two objects that belong to different classes, 
# e.g x+y, but __add__ hasn't been defined for the class containing x, then it will search for a method __radd__ in the class containing y and perform it as y+x. 
# An example code might look like this: 
class Dog: 
    def __init__(self, name): 
        self.name = name 
        
class Cat: 
    def __init__(self,name): 
        self.name = name
    def __radd__(self,other): 
        return "\n".join(self.name, other.name) 
    
dog1 = Dog("Harry") 
cat1 = Cat("Ella") 
print(dog1 + cat1) 
# This will print: Ella Harry because there was no "add" method defined for the class Dog, 
# so instead it searched for "radd" in class Cat and performed cat1 + dog1 :)


# (1): Look at the code in the example there from bottom to top. 
# So you got some __truediv__ method involvement, indicated by the "/" in the line "print(spam / hello)". 
# Also, you've got two instances of the SpecialString class, namely spam and hello. 
# spam, being an instance of the SpecialString class, has "spam" as its cont-attribute. 
# Likewise, the hello instance of the class has "Hello world!" as its cont-attribute. 
# Indeed, absolutely any instance of the SpecialString class would come equipped with just a single attribute, namely a cont-attribute. 
# [[[Like how Dog class can have many instances, like fido, husky etc, 
# each of which come equipped with a number of ATTRIBUTES like say color, number of legs, number of teeth etc, 
# determined by the way the Dog class got defined]]]
# (2): Recall that the magic method for "/" is __truediv__ 
# So, Python INTERPRETS "spam / hello" as the following. 
# [see the way __truediv__ magic method is actually defined here] spam / hello spam.__truediv__(hello) 
# Now, the rest pretty much follows from APPLYING the DEFINITION we have here of __truediv__ magic method. 
# Also, remember that the thing on the LEFT of ".__truediv__" gets taken as self whilst the thing on the RIGHT of it gets taken as other. 
# So, self=spam and other=hello. Also, spam.cont refers to the cont-attribute of the instance spam, which is the string "spam". 
# Similarly, hello.cont refers to the cont-attribute of the instance hello, which is the string "Hello world!". 
# Hence, Python presumably would make the following interpretations. return "\n".join([self.cont, line, other.cont]) return "\n".join([spam.cont, line, hello.cont])
# (3): return "\n".join(["spam", line, "Hello world!"]) 
# Basically, what the last line means is that, I've got a LIST of MULTIPLE STRINGS here, and I want to join em all up using another STRING as a SEPARATOR. 
# I've got strings given by "spam", line and "Hello world!", and I wish to join em all up using the string "\n" (aka new line) as a separator. 
# [[[definition of join method from a previous lesson: join - joins a list of strings with another string as a separator]]] 
# WHAT'S LINE????!! Well, as discussed already, hello.cont refers to the cont-attribute of the instance hello, which is the string "Hello world!". 
# So, len(other.cont) really gets interpreted as len("Hello world!") aka the number of characters in the string "Hello world!", which is 12. 
# Hence, line = "=" * 12, so line = "============". return "\n".join(["spam", "============", "Hello world!"]) 
# So, OUTPUT: >>> spam ============ Hello world! >>>


# For the numeric classes which come with Python (int, float, etc) operators such as addition +, multiplication *, etc are already defined. 
# However, if you define your own class Animal, and you want to sum two animals instances, it won't work right away, as Python will not know what to sum Animals mean. 
# Therefore, you need to tell to Python where to do when it finds animal1 + animal2. 
# In order to do so, you should define the method __sum__(self, other) in your Animal class. 
# When Python finds animal1 + animal2, it will now call animal1.__sum__(animal2). 
# In the case this fails, because __sum__ is not defined, it will try to call the reverse sum method __rsum__ on the second object: animal2.__rsum__(animal1). 

# Here's their example with the "r" method included: 
class SpecialString: 
    def __init__(self, cont): 
        self.cont = cont 
    def __truediv__(self, other): 
        line = "=" * len(other.cont) 
        return "\n".join([self.cont, line, other.cont]) 
    def __rtruediv__(self, other): 
        line = "=" * len(self.cont)
        return "\n".join([other, line, self.cont]) 

spam = "spam" 
hello = SpecialString("Hello world!") 
print(spam / hello) 
# Notice that spam is NOT a special string, but it still works 
# because python was able to use the rtrueDivide (r for reverse) that swaps the terms around and my implementation assumes the other arg is a regular string. 


# Example:
class SpecialString:
    def __init__(self, cont): 
        self.cont = cont 
    def __truediv__(self, other): 
        selfline = "=" * len(self.cont) 
        otherline = "=" * len(other.cont) 
        return "\n".join([self.cont, selfline, otherline, other.cont]) 
    
spam = SpecialString("spam") 
hello = SpecialString("Hello world!") 
print(spam / hello) # output: spam ==== ============ Hello World!


# Here is a example of rtruediv: 
class Pair_of_numbers:
    def __init__(self, x, y): 
        self.x = x 
        self.y = y
    def __truediv__ (self, other):
        return Pair_of_numbers(self.x / other.x, self.y / other.y) 
    
class Pair_of_numbers2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __rtruediv__ (self, other): 
        return Pair_of_numbers(self.x / other.x, self.y / other.y) 
    
pair_1 = Pair_of_numbers(10,5)
pair_2 = Pair_of_numbers2(2,5)
result = pair_1 / pair_2
print (result.x)
print (result.y)
# the result is 0.2 1.0 Because there is no method named __truediv__ in Pair_of_numbers (the method is commented by #)
# then the pair_1 / pair_2 will do __rtruediv__ : pair_2.__rtruediv__(pair_1) 2/10==0.2 1/1=1.0 
# If you drop the symbol '#' at the __truediv__ line in the class Pair_of_numbers pair_1 /pair_2 will do pair_1.__truediv(pair_2) 
# the result will be changed as 5.0 1.0 10/2==5.0 1/1==1.0

# What is A() ^ B() evaluated as, if A doesn't implement any magic methods? --> B().__rxor__(A())

# The explanation mentions something called "r methods", but no example is given, so I have no context to pick the " rxor" line as the right answer in question 2. 
# It doesn't match the examples at all. Are "r methods" covered elsewhere or did this come out of the blue for everyone else?

# This is tricky, but the previous lesson states: "However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called." 
# Here, we're told that A() doesn't implement magic methods. If A() and B() are different types, then answer is B().__rxor__(A()). 
# Do we have to assume that A() and B() are different types, or is that known somehow? 

# Here's some code that shows how Python works with magic methods. 
# only 1 magic method implemented class A: def __or__(self, other): return ("A or") 
# several magic methods 
class B: 
    def __or__(self, other): 
        return ("B or") 
    def __ror__(self, other): 
        return ("B ror") 
    def __xor__(self, other): 
        return ("B xor") 
    def __rxor__(self, other): 
        return ("B rxor") 
# compare classes directly print(str(A() ^ B())) 
# B rxor - xor is not implemented for A print(str(B() ^ A())) # B xor 
# create instances and compare a=A() b=B() print(str(a | b)) 
# A or print(str(b | a)) # B or print(str(a ^ b)) 
# B rxor - xor is not implemented for A print(str(b ^ a)) 
# B xor print(str(a & b)) 
# TypeError: unsupported operand type(s) for &: 'A' and 'B' 


# According to python.org, ‘r’ stands for ‘reflected’. 
# These methods are used when the classes are different types but you don’t want to modify the first type. 
# For example, if you wanted to do: 8 + Meter(5) It would first look at the __add__ method for integer and raise a NotImplemented error 
# because it does not know how to add an integer with this new Meter class. 
# You wouldn’t want to overload the __add__ method on integer or you’de have all sorts of weird behavior throughout your program since adding integers is used everywhere. 
# Therefore you write a ‘__radd__’ or ‘reflexive add’ method to our example ‘Method’ class which will tell Python how to handle the add operation between these two types. 
# Python was designed in such a way so that if the left operand doesn’t support that operation, 
# it will call the reflexive version of the method on the other class automatically for this very reason. 
# That way we don’t need to overwrite the magic method on the first class. Hope this helps.

# The explanation class A: def __init__(self, x, y): self.x=x self.y=y 
class B: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def __radd__(self, other): 
        return A(self.x + other.x, self.y + other.y) 

one = A(1, 1) 
sec = B(2, 3) 
print('Type of object one,', type(one)) 
print('\nType of object sec,', type(sec)) 
# if type(one) is type(sec): print('\nTrue, type of A() is same as type of B().\n') else: print('\nFalse, A() and B() are different types.\n') 
# The expression one + sec is translated into one.__add__(third). 
# However, if one hasn't implemented __add__, and one and sec are of different types, then sec.__radd__(one) is called. 
# new = one + sec print('Attributes of new object --> ', new.x, ',', new.y) 

# i guess this program might help in getting the use of __radd__ 
class a: 
    def __init__(self,x,y):
        self.x=x;
        self.y=y; 
        
class b: 
    def __init__(self,x,y): 
        self.x=x; 
        self.y=y; 
    def __radd__(self,other): 
        return a(self.x+other.x,self.y+other.y); 
    
res = a(0,0); 
one = a(1,1); 
sec = b(2,2); 
res = one+sec; 
print(res.x,'-',res.y); #output 3-3 eventhough class a didnt define its magic method__add__,the class b defined __radd__ and that is the use of radd


# SECTION 3
# Python also provides magic methods for comparisons.
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=

# If __ne__ is not implemented, it returns the opposite of __eq__.
# There are no other relationships between the other operators.
# Example:
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs
"""
>spam>eggs
e>spam>ggs
eg>spam>gs
egg>spam>s
eggs>spam>
"""
# As you can see, you can define any custom behavior for the overloaded operators.

# (1): At this point, Plz plz plz see Hélder Lima's useful reply to the nice question of Evgeny Satanovsky. 
# This will help remind your of the List Slices lessons we had before. 
# Additionally, observe the following code and its output. 
print("eggs"[:0]) # e
print("eggs"[:1]) # eg
print("eggs"[:2]) # egg
print("eggs"[:3]) # eggs
print("eggs"[:4]) 

# http://cscircles.cemc.uwaterloo.ca/visualize#mode=display
# (2): First of all, we create a class called SpecialString, with just a single attribute, 
# namely the cont-attribute (similar to how a dog-class can have color, number of legs, number off teeth, age attributes). 
# We then CUSTOMISE the exact behaviour of the comparison operator > by using the __gt__ magic method. 
# Some :( scary-looking way is indeed used for such customisation, 
# but you know what, once you break down each of the bits and pieces of it all and look at the way things got defined in the first place, it should all hopefully make sense. 
# We create 2 instances of the SpecialString class - the instances spam and eggs. 
# The spam instance is equipped with its cont-attribute equal to the string "spam" whilst the eggs instance is equipped with its cont-attribute equal to the string "eggs". 
# Therefore, we know that spam.cont would RETURN the string "spam" and eggs.cont would RETURN the string "eggs".
# (3): The FINAL line of the code in the example would get perhaps interpreted as the following. spam > eggs spam.__gt__(eggs) 
# Now, you just apply the customised way we had defined the __gt__ magic method. 
# Remember the the thing on the LEFT side of __gt__ gets taken as self, and the thing on the RIGHT side of it gets taken as other. 
# Hence, self=spam and other=eggs here. for index in range(len(other.cont)+1): result = other.cont[:index] + ">" + self.cont result += ">" + other.cont[index:] 
# By taking self=spam and other=eggs, the above part of the code simplifies to the following. 
# for index in range(len(eggs.cont)+1): result = eggs.cont[:index] + ">" + spam.cont result += ">" + eggs.cont[index:]
# (4): Now, I did mention before that, spam.cont would RETURN the string "spam" and eggs.cont would RETURN the string "eggs". 
# Hence, above code simplifies to the following. for index in range(len("eggs")+1): result = "eggs"[:index] + ">" + "spam" result += ">" + "eggs"[index:] 
# The string "eggs" has just 4 characters, so len("eggs") would RETURN 4. 
# Hence, len("eggs")+1 simplifies to 4+1, so 5. 
# So, the above code block simplifies to the following. 
# for index in range(5): result = "eggs"[:index] + ">" + "spam" result += ">" + "eggs"[index:]

# (5): Now you just iterate through the 2 indented lines of code, taking index=0,1,2,3,4 each one at a time. 
# For example, with index=0: 
result = "eggs"[:0] + ">" + "spam" 
result += ">" + "eggs"[0:] 
result = "" + ">" + "spam" 
result += ">" + "eggs" 
result = ">spam" 
result += ">eggs" 
result = ">spam>eggs"   
# Of course, AFTER each iteration gets done, the value assigned to the variable result gets printed out, OUTPUT, 
# because print(result) is also included on the code block in the example they've got, it's just that I've left it out so far.


# I find it unnecessarily confusing that SL uses the same word for the object as the argument. 
# Using a descriptive variable name in place of 'cont' would be nice too. 
# The following code produces exactly the same result but makes it easier to follow what's going on: 
class SpecialString: 
    def __init__(self, food_type): 
        self.food_type = food_type 
    def __gt__(self, other): 
        for index in range(len(other.food_type)+1): 
            result = other.food_type[:index] + ">" + self.food_type 
            result += ">" + other.food_type[index:] 
            print(result)
            
food_01 = SpecialString("spam") 
food_02 = SpecialString("eggs") 
food_01 > food_02 

# So this one definitely stumped me too for a bit, 
# this example is written as an excellent test question as it does have some parts that really make you think and could trick you, but try this version. 
# Exactly the same but written not to confuse.
class SpecialString: 
    def __init__(self, cont): 
        self.cont = cont 
    def __gt__(self, other): 
        for var in range(len(other.cont)+1): 
            result = other.cont[:var] + ":)" + self.cont 
            result = result + ":)" + other.cont[var:] 
            
print(result) 
spam = SpecialString("spam") 
eggs = SpecialString("eggs") 
spam > eggs # So I have replaced "index" with "var", because that's all it is(a variable) how it's being used here. 
# A bit confusing at is being used within the actual indexing. 
# I have also replaced ">" with ":)"(smiley face) as when ">" is being used in quotes it is just a character to break up the self.cont and other.cont . 
# Lastly I just wrote out the result += portion in full as it will help make it more obvious what is act
                
# Example:
# http://www.pythontutor.com/visualize.html#mode=edit 
# Input the code here and you can see a step by step visualization of what is going on. 
# Also, I wrote the 5 iterations which are generated by the code spam > eggs out like this, and that helped me understand it better. 
# Hope it helps someone else too! 
>spam>eggs means eggs[:0] + >spam> + eggs[0:] 
e>spam>ggs means eggs[:1] + >spam> + eggs[1:] 
eg>spam>gs means eggs[:2] + >spam> + eggs[2:] 
egg>spam>s means eggs[:3] + >spam> + eggs[3:] 
eggs>spam> means eggs[:4] + >spam> + eggs[4:]


# Example:
class X: 
    def __init__(self, data): 
        self.instance = data 
    def __gt__(this, another): 
        for i in range(len(another.instance)+1): 

result = another.instance[:i] + ">" + this.instance + ">" + another.instance[i:] 
print(result) 
first = X("left") 
second = X("right") 
first > second


# where to use - 
class Robot: 
    def __init__(self,power,height): 
        self.power = power 
        self.height = height 
    def __add__(self,other): 
        return Robot(self.power+other.power,self.height) 
    def __gt__(self,other): 
        if self.height > other.height: 
            print(True) 
        else: 
            print(False) 
            
r1 = Robot(100,6) 
r2 = Robot(50,5) 
new_r = r1+r2 # creates new robot/obj #by combining powers/attribute r1 > r2 # checks if r1 is taller than r2

# this lessons are very nice and all but not very clear and im no genius but thats why i use this program to try to understand phyton but dont seem to get it


# What is __le__ a magic method for?    x <= y
# These magic methods are quite easy to remember. 
# Use first letters: 
# < less than __lt__ 
# <= less or equal __le__ 
# == equal __eq__ 
# != not equal __ne__ 
# > greater than __gt__ 
# >= greater or equal __ge__
    
# SECTION 4
# There are several magic methods for making classes act like containers.
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in

# There are many other magic methods that we won't cover here, 
# such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.
# Example:
# We have overridden the len()
import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))  # 0
print(len(vague_list))  # 0
print(vague_list[2])    # D
print(vague_list[2])    # C

# We have overridden the len() function for the class VagueList to return a random number.
# The indexing function also returns a random item in a range from the list, based on the expression.

# (1): Recall, the module random contains the function randint which can be used to generate a random integer. 
# For example, consider the following code and its OUTPUT, where we run it twice. 
from random import randint 
for i in range(3): 
    value = randint(1, 6) 
    print(value)    # 1st time: 5 5 1
                    # 2nd time: 5 6 2
# (2): We create a class called VagueList, defining it have just a single attribute, namely the cont-attribute. 
# Also, we define the VagueList class to be equipped with 2 customised methods, namely the __getitem__ and __len__ methods. 
# We set up an instance of the VagueList class, calling such an instance as vague_list. 
# We make the list of 5 strings given by ["A", "B", "C", "D", "E"] be equal to the cont-attribute of this vague_list instance. 
# Therefore, vague_list.cont would RETURN this list of 5 strings. Now, consider len(vague_list). 
# Based on the way we overloaded/overridden the magic method __len__ (the way we customised its definition for the VagueList class), 
# it seems as if len(vague_list) might be interpreted as follows. 
# Also, I think we take self as vague_list, so that self.cont becomes vague_list.cont, 
# hence self.cont is really equal to the list of 5 strings given by ["A", "B", "C", "D", "E"].
# (3): random.randint(0, len(self.cont)*2) random.randint(0, len(["A", "B", "C", "D", "E"])*2) random.randint(0, 5*2) random.randint(0, 10) 
# This just gives you a number between 0 and 10 (INCLUSIVE) RANDOMLY. 
# For the example, it looks as if the len(vague_list) in print(len(vague_list)) had RETURNED 6 
# FIRST, making 6 be observed in the OUTPUT thanks to the print function applied. 
# Second time of print(len(vague_list)) looks to have given the OUTPUT of 7 due to 7 being RETURNED the second time we had called len(vague_list). 
# Once again, this 7, along with the 6 were RANDOM, so if u run it urself, u may get say, 8 and 7, 6 and 5, 9 and 10 etc. 
# BUT, whatever you get, for sure both of these numbers are restricted due to the condition that they MUST be integers between 0 and 10 (INCLUSIVE).
# (4): Next, consider vague_list[2]. 
# Consider the way we had overloaded/overridden the __getitem__ magic method (the way we customised its definition for the VagueList class). 
# So, it seems as if vague_list[2] might be interpreted as the following. 
# Also, I reckon that we take self as vague_list and index as 2. 
# Hence, self.cont equals to vague_list.cont aka the cont-attribute of the instance vague_list, which is the list of 5 strings given by ["A", "B", "C", "D", "E"]. 
# self.cont[index + random.randint(-1, 1)] ["A", "B", "C", "D", "E"][2 + random.randint(-1, 1)] 
# May look baffling, but perhaps the following looks clearer. letters_list = ["A", "B", "C", "D", "E"] letters_list[2 + random.randint(-1, 1)]
# (5): So, we just RETURN the element of letters_list that has its index given by the number 2 + random.randint(-1, 1), 
# which means 2 + some random integer between -1 and 1 (INCLUSIVE), so index = 2 + (-1,1), hence index = (1,3), so index = 1,2,3. 
# Thus, a random choice among "B", "C", "D" would be RETURNED by vague_list[2]. 
# Therefore, a random choice among B, C, D would be printed by print(vague_list[2]). 
# Also, interesting to see how this held TRUE BOTH times we ran print(vague_list[2]), as we got D followed by C. 
# I got D followed by B when I personally ran print(vague_list[2]) on Try It Yourself.

# I removed random module to make thia code simpler and easier to understand 
class VagueList: 
    def __init__(self, cont): 
        self.cont = cont 
    def __getitem__(self, index): 
        return self.cont[index] 
    def __len__(self): 
        return len(self.cont)*2 
    
vague_list = VagueList(["A", "B", "C", "D", "E"]) 
print(len(vague_list)) 
print(vague_list[2]) 
print(vague_list[3]) # output would be 10, C, D as length is 5 and with the condition its 5*2 so its 10 where as index 2 lies at C and 3 lies D

# I found this section the weak point in an otherwise superb tutorial app. 
# Some of the concepts are somewhat complex and the explanation is brief. 
# http://www.rafekettler.com/magicmethods.html is useful in clarifying. 

# Example:
def __getitem__(self, index): 
    return self.cont[index + random.randint(-index, ((len(self.cont)-1) - index))] 
### __getitem__ seems to generate indices not random enough, so to say. If we ask the program to print vague_list[2], 
# as in the given example, it won't print any element of the list (there are 5 of them), but rather any of the elements indexed with 1, 2, or 3. 
# I mean, we will get "B", "C", or"D". 

# Example:
import random class VagueList: 
    def __init__(self, cont): 
        self.cont = cont 
    def __len__(self): 
        return (len(self.cont)*random.randint (1,2)) 
    
vague_list = VagueList(["A", "B", "C", "D", "E", "F"])
print(len(vague_list))  # This will return two random results - 6 or 12.


# The key is those in those bottom 5 lines: 
vague_list = VagueList(["A", "B", "C", "D", "E"]) # means that a list with 5 items is created. 
print(len(vague_list)) # normally prints 5, the length of that list. 
# However, len was redefined by def __len__(self): return random.randint(0, len(self.cont)*2) 
# which means that it returns a random number between 0 and the length of the list, 5, times 2, which means a random number between 0 and 10. 
# As for print(vague_list[2]), normally this prints the item indexed under 2, which would be C. 
# However, def __getitem__(self, index): return self.cont[index + random.randint(-1, 1)] redefines that retrieval, 
# and instead gets the index 2 plus or minus 1, getting either index 1, 2, or 3. Thus, it chooses B, C, or D at random.

# Magic methods just add custom functionality to simple operators. 
# Eg. You would want the multiplication operator (*) to work differently for matrices than for simple numbers. 


# Which magic method call is made by x[y] = z? --> x.__setitem__(y, z)
# https://minhhh.github.io/posts/a-guide-to-pythons-magic-methods

# Example:
mylist = [1,2,3,4,5,6,7]
mylist.__setitem__(2,10)
print(mylist) # [1, 2, 10, 4, 5, 6, 7] 
# basically x is your iterable, in this case MyList.[1...7] 
# y is the index position in the iterable. 
# z is the new values you want to put in the index position specified by y. 
mylist.__getitem__(2) # 10


# Example:
import random class Any_List: 
    def __init__(self,list): 
        self.list=list 
    def __setitem__(self, index, letter): 
        self.list[abs(index-random.randint(0,len(self.list)))-1]=letter 
        
anylist = Any_List(["a","b","c","d"]) 
anylist[2] = "z" 
anylist[3] = "p" 
anylist[1] = "q" 
print(anylist.list) 
# The program receives an index and sets the element assigned to that index in the list. 
# I made the program to set the elements assigned to indices randomly. 


# Array Example:
# Ages = [a, b, c, g, e, f] #note that our array here is Ages 
# the magic method we can use to modify elements of Array ages is called __setitems__ 
# And we wanted to change the element ‘g’ which is at index 3 to ‘d’ 
# We could say Ages.__setitem__(3, d) 
# An output of our array will now return Agnes = [a, b, c, d, e, f] 
# Because element at index 3 is now represented by letter ‘d’ instead of ‘g’ previously




# Example:
import random

class VagueList:
    def __init__(self, cont): #создаем тело класса с атрибутом cont
        self.cont = cont

    def __getitem__(self, index): #метод класса, в теле которого мы должны указать число за место атрибута index
        return self.cont[index + random.randint(-1, 1)] # берет элемент из cont с индексом, 
                                                        # равным сумме числа, введённого нами и рандомного числа : -1 или 0. 
                                                        # То есть, если мы ввели число 3, то индексом cont может быть или 3, или 2.

    def __len__(self):  #метод без атрибутов, который просто выводит что-то на основе заранее определённых данных.
        return random.randint(0, len(self.cont)*2) #выводится рандомное число из списка из чисел от нуля до двойного числа элементов в cont

vague_list = VagueList(["A", "B", "C", "D", "E"]) #это список букв, над которым возможны манипуляции класса VagueList 
print(len(vague_list))  #выводится число элементов списка vague_list 
print(len(vague_list))  #вновь. Но ответы могут быть разными, так как мы, определив метод __len__, 
                        # сделали так, чтоб выводилось рандомное число из списка (списка не как формата данных, а простого перечисления чисел) от 0 до числа, 
                        # равного удвоенному числу элементов списка cont (в нашем случае vague_list). 
                        # Это число может быть больше числа элементов списка, так как максимальное значение - удвоенное количество элементов списка
print(vague_list[2])    #элемент с индексом 2
print(vague_list[2])    #вновь. Как сказано выше, может быть стандартным, а может быть на 1 меньше стандарта 
                        # (стандарт это и есть наше число, которое мы ввели в квадратных скобках). Вот пример на списке с числами, может, тут яснее будет.
print("~"*10)           #это просто декорация, чтоб была видна граница между ответами, она не несет за собой какой-то кодовый смысл
num_list = VagueList([1,2,3,4,5,6,7])
print(len(num_list))
print(len(num_list))
print(num_list[3])



