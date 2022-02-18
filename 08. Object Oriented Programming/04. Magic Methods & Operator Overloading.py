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


# (1): Recall that, any instance in the class Vector2D comes equipped with 2 attributes, namely x and y. The following 2 lines of code create two instances of the class Vector2D - the instance named "first" comes with the attributes of x=5 and y=7, and the instance named "second" comes with the attributes of x=3 and y=9. [These attributes are just pieces of data associated to the instance, like how we can have a dog class with two instances in it, fido and Max, with the attributes of say, color, name and number of legs.] first = Vector2D(5, 7) second = Vector2D(3, 9) The above 2 lines of code get followed by the line of code: result = first + second
# (2): Now, according to what @Benoit said, behind the scenes, every time u have a +, Python INTERPRETS the + as the method __add__ So, for example, 21 + 35 would be interpreted by Python as 21.__add__(35) However, we override this method, and tailor it to exactly what we personally desire. The exact way we re-define it for our purposes is revealed to us by the following two lines of code that apply as part of the class Vector2D definition. def __add__(self, others): return Vector2D(self.x + other.x, self.y + other.y) Therefore, the "result = first + second" line of code gets interpreted as follows: result = first + second result = first.__add__(second) Now, looking at the way we defined the __add__ method, and considering self = first and other = second, based on what @Andrii Pozdieiev said, we get the following.
# (3): result = Vector2D(first.x + second.x, first.y + second.y) Now, remember how we earlier learnt that say if you had an instance, like say, fido, and you had defined it to have the attribute of color = grey, then the code "fido.color" would RETURN the color-attribute associated to to the instance fido, which is grey? Likewise, "first.x" would RETURN the x-attribute associated to the instance first, which is equal to 5, according to how we defined had defined it. Hence, first.x = 5, and similarly second.x = 3, first.y = 7 and lastly second.y = 9. Therefore, we get result = Vector2D(5 + 3, 7 + 9) result = Vector2D(8, 16) So, result is an instance of the class Vector 2D, with the attributes of x=8 and y=16. Consequently, result.x RETURNS the x-attribute of the result instance, which is 8, and hence print(result.x) would print 8. Similarly result.y RETURNS the y-attribute of the result instance, which is 16, and hence print(result.y) would print 16.

        
# Python has many special methods like __add__, see the list below. +, __add__(self, other), Addition; *, __mul__(self, other), Multiplication; -, __sub__(self, other), Subtraction; %, __mod__(self, other), Remainder; /, __truediv__(self, other), Division; <, __lt__(self, other), Less than; <=, __le__(self, other), Less than or equal to; ==, __eq__(self, other), Equal to; !=, __ne__(self, other), Not equal to; >, __gt__(self, other), Greater than; >=, __ge__(self, other), Greater than or equal to; [index], __getitem__(self, index), Index operator; in, __contains__(self, value), Check membership; len, __len__(self), The number of elements; str, __str__(self), The string representation Magic Method. dunders: abbr of double underscores； Operator Overloading: custom class

# So I finally understood! sorry if it has been explained before but I just want also confirm I'm right. The magic method is simply telling the interpreter how to handle the operation between the two objects. You are adding functionality to your objects by allowing to operate between them. It doesn't matter if you use __add__ or __div__ or anything else as long as you match the operator with the magic method, the operation will do whatever you tell it to do in the class. I can use the the __add__ magic method and return the division of 2 numbers. To prove my statement above, I wrote this code to show it works. Without cheating, let me know what you think the output is. class SpecialString: def __init__(self, cont): self.cont = cont def __truediv__(self, other): return self.cont + other.cont no1 = SpecialString(4) no2 = SpecialString(2) print(no1 / no2)


# It has now started to make sense for me after reading through the comments here. My summary of understanding is, These two lines of codes first = Vector2D(5, 7) second = Vector2D(3, 9) just create two instances of the Vector2D class with the passed attributes(arguments). They do just that. Now this method __add__ inside the class Vector2D returns an instance of the class instead of values. def __add__(self, other): return Vector2D(self.x + other.x, self.y + other.y) This is where the operator '+' is 'overloaded' to operate on objects in a specified manner. Now this magic method is called in this line of code result = first + second We have to read this as other comments have pointed out as: result = first().__add__(second): With this call, the parameters (x & y, in this case 5 & 7) of the object 'first' becomes the parameters of 'self'(as the method is called on the object 'first') and the parameters (3 & 9) of the object 'second' becomes the parameters of 'other' defined in the method. 

# I have a theory of why the code is so confusing to look at. If you are having trouble try looking at this. class Vector2D: def __init__(self, x): self.x = x def __add__(self, other): return Vector2D(self.x + other.x) first = Vector2D(5) second = Vector2D(3) result = first + second print(result.x)



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


# It took me a while but I understand r methods as follows: If you call a magic method on two objects that belong to different classes, e.g x+y, but __add__ hasn't been defined for the class containing x, then it will search for a method __radd__ in the class containing y and perform it as y+x. An example code might look like this: class Dog: def __init__(self, name): self.name = name class Cat: def __init__(self,name): self.name = name def__radd__(self,other): return "\n".join(self.name, other.name) dog1 = Dog("Harry") cat1 = Cat("Ella") print(dog1 + cat1) This will print: Ella Harry because there was no "add" method defined for the class Dog, so instead it searched for "radd" in class Cat and performed cat1 + dog1 :)


# (1): Look at the code in the example there from bottom to top. So you got some __truediv__ method involvement, indicated by the "/" in the line "print(spam / hello)". Also, you've got two instances of the SpecialString class, namely spam and hello. spam, being an instance of the SpecialString class, has "spam" as its cont-attribute. Likewise, the hello instance of the class has "Hello world!" as its cont-attribute. Indeed, absolutely any instance of the SpecialString class would come equipped with just a single attribute, namely a cont-attribute. [[[Like how Dog class can have many instances, like fido, husky etc, each of which come equipped with a number of ATTRIBUTES like say color, number of legs, number of teeth etc, determined by the way the Dog class got defined]]]
# (2): Recall that the magic method for "/" is __truediv__ So, Python INTERPRETS "spam / hello" as the following. [see the way __truediv__ magic method is actually defined here] spam / hello spam.__truediv__(hello) Now, the rest pretty much follows from APPLYING the DEFINITION we have here of __truediv__ magic method. Also, remember that the thing on the LEFT of ".__truediv__" gets taken as self whilst the thing on the RIGHT of it gets taken as other. So, self=spam and other=hello. Also, spam.cont refers to the cont-attribute of the instance spam, which is the string "spam". Similarly, hello.cont refers to the cont-attribute of the instance hello, which is the string "Hello world!". Hence, Python presumably would make the following interpretations. return "\n".join([self.cont, line, other.cont]) return "\n".join([spam.cont, line, hello.cont])
# (3): return "\n".join(["spam", line, "Hello world!"]) Basically, what the last line means is that, I've got a LIST of MULTIPLE STRINGS here, and I want to join em all up using another STRING as a SEPARATOR. I've got strings given by "spam", line and "Hello world!", and I wish to join em all up using the string "\n" (aka new line) as a separator. [[[definition of join method from a previous lesson: join - joins a list of strings with another string as a separator]]] HANG ON!!! WHAT'S LINE????!! Well, as discussed already, hello.cont refers to the cont-attribute of the instance hello, which is the string "Hello world!". So, len(other.cont) really gets interpreted as len("Hello world!") aka the number of characters in the string "Hello world!", which is 12. Hence, line = "=" * 12, so line = "============". return "\n".join(["spam", "============", "Hello world!"]) So, OUTPUT: >>> spam ============ Hello world! >>>


# This is what I get (I hope it can help you): For the numeric classes which come with Python (int, float, etc) operators such as addition +, multiplication *, etc are already defined. However, if you define your own class Animal, and you want to sum two animals instances, it won't work right away, as Python will not know what to sum Animals mean. Therefore, you need to tell to Python where to do when it finds animal1 + animal2. In order to do so, you should define the method __sum__(self, other) in your Animal class. When Python finds animal1 + animal2, it will now call animal1.__sum__(animal2). In the case this fails, because __sum__ is not defined, it will try to call the reverse sum method __rsum__ on the second object: animal2.__rsum__(animal1). 


# Here's their example with the "r" method included: class SpecialString: def __init__(self, cont): self.cont = cont def __truediv__(self, other): line = "=" * len(other.cont) return "\n".join([self.cont, line, other.cont]) def __rtruediv__(self, other): line = "=" * len(self.cont) return "\n".join([other, line, self.cont]) spam = "spam" hello = SpecialString("Hello world!") print(spam / hello) Notice that spam is NOT a special string, but it still works because python was able to use the rtrueDivide (r for reverse) that swaps the terms around and my implementation assumes the other arg is a regular string. 


# class SpecialString: def __init__(self, cont): self.cont = cont def __truediv__(self, other): selfline = "=" * len(self.cont) otherline = "=" * len(other.cont) return "\n".join([self.cont, selfline, otherline, other.cont]) spam = SpecialString("spam") hello = SpecialString("Hello world!") print(spam / hello) output: spam ==== ============ Hello World!


# #Here is a example of rtruediv: class Pair_of_numbers: def __init__(self, x, y): self.x = x self.y = y # def __truediv__ (self, other): # return Pair_of_numbers(self.x / other.x, self.y / other.y) class Pair_of_numbers2: def __init__(self, x, y): self.x = x self.y = y def __rtruediv__ (self, other): return Pair_of_numbers(self.x / other.x, self.y / other.y) pair_1 = Pair_of_numbers(10,5) pair_2 = Pair_of_numbers2(2,5) result = pair_1 / pair_2 print (result.x) print (result.y) ''' the result is 0.2 1.0 Because there is no method named __truediv__ in Pair_of_numbers (the method is commented by #)then the pair_1 / pair_2 will do __rtruediv__ : pair_2.__rtruediv__(pair_1) 2/10==0.2 1/1=1.0 If you drop the symbol '#' at the __truediv__ line in the class Pair_of_numbers pair_1 /pair_2 will do pair_1.__truediv(pair_2) the result will be changed as 5.0 1.0 10/2==5.0 1/1==1.0 '''


# What is A() ^ B() evaluated as, if A doesn't implement any magic methods? --> B().__rxor__(A())

# I don't understand this question. The explanation mentions something called "r methods", but no example is given, so I have no context to pick the " rxor" line as the right answer in question 2. It doesn't match the examples at all. Are "r methods" covered elsewhere or did this come out of the blue for everyone else?

# This is tricky, but the previous lesson states: "However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called." Here, we're told that A() doesn't implement magic methods. If A() and B() are different types, then answer is B().__rxor__(A()). Do we have to assume that A() and B() are different types, or is that known somehow? 




# Here's some code that shows how Python works with magic methods. # only 1 magic method implemented class A: def __or__(self, other): return ("A or") # several magic methods class B: def __or__(self, other): return ("B or") def __ror__(self, other): return ("B ror") def __xor__(self, other): return ("B xor") def __rxor__(self, other): return ("B rxor") # compare classes directly print(str(A() ^ B())) # B rxor - xor is not implemented for A print(str(B() ^ A())) # B xor # create instances and compare a=A() b=B() print(str(a | b)) # A or print(str(b | a)) # B or print(str(a ^ b)) # B rxor - xor is not implemented for A print(str(b ^ a)) # B xor print(str(a & b)) # TypeError: unsupported operand type(s) for &: 'A' and 'B' 


# #Here is a example of rtruediv: class Pair_of_numbers: def __init__(self, x, y): self.x = x self.y = y # def __truediv__ (self, other): # return Pair_of_numbers(self.x / other.x, self.y / other.y) class Pair_of_numbers2: def __init__(self, x, y): self.x = x self.y = y def __rtruediv__ (self, other): return Pair_of_numbers(self.x / other.x, self.y / other.y) pair_1 = Pair_of_numbers(10,5) pair_2 = Pair_of_numbers2(2,5) result = pair_1 / pair_2 print (result.x) print (result.y) ''' the result is 0.2 1.0 Because there is no method named __truediv__ in Pair_of_numbers (the method is commented by #)then the pair_1 / pair_2 will do __rtruediv__ : pair_2.__rtruediv__(pair_1) 2/10==0.2 1/1=1.0 If you drop the symbol '#' at the __truediv__ line in the class Pair_of_numbers pair_1 /pair_2 will do pair_1.__truediv(pair_2) the result will be changed as 5.0 1.0 10/2==5.0 1/1==1.0 '''


# According to python.org, ‘r’ stands for ‘reflected’. These methods are used when the classes are different types but you don’t want to modify the first type. For example, if you wanted to do: 8 + Meter(5) It would first look at the __add__ method for integer and raise a NotImplemented error because it does not know how to add an integer with this new Meter class. You wouldn’t want to overload the __add__ method on integer or you’de have all sorts of weird behavior throughout your program since adding integers is used everywhere. Therefore you write a ‘__radd__’ or ‘reflexive add’ method to our example ‘Method’ class which will tell Python how to handle the add operation between these two types. Python was designed in such a way so that if the left operand doesn’t support that operation, it will call the reflexive version of the method on the other class automatically for this very reason. That way we don’t need to overwrite the magic method on the first class. Hope this helps.


# The explanation class A: def __init__(self, x, y): self.x=x self.y=y class B: def __init__(self, x, y): self.x = x self.y = y def __radd__(self, other): return A(self.x + other.x, self.y + other.y) one = A(1, 1) sec = B(2, 3) print('Type of object one,', type(one)) print('\nType of object sec,', type(sec)) if type(one) is type(sec): print('\nTrue, type of A() is same as type of B().\n') else: print('\nFalse, A() and B() are different types.\n') # The expression one + sec is translated into one.__add__(third). # However, if one hasn't implemented __add__, and one and sec are of different types, then sec.__radd__(one) is called. new = one + sec print('Attributes of new object --> ', new.x, ',', new.y) # More details in the link below: # https://code.sololearn.com/cHMbVJab8DhI/?ref=app


# i guess this program might help in getting the use of __radd__ class a: def __init__(self,x,y): self.x=x; self.y=y; class b: def __init__(self,x,y): self.x=x; self.y=y; def __radd__(self,other): return a(self.x+other.x,self.y+other.y); res=a(0,0); one=a(1,1); sec=b(2,2); res=one+sec; print(res.x,'-',res.y); #output 3-3 eventhough class a didnt define its magic method__add__,the class b defined __radd__ and that is the use of radd


# https://www.sololearn.com/learning/1073/2470/5135/1


