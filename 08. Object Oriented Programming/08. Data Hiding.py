# SECTION 1
# A key part of object-oriented programming is encapsulation, 
# which involves packaging of related variables and functions into a single easy-to-use object - an instance of a class.
# A related concept is data hiding, which states that implementation details of a class should be hidden, 
# and a clean standard interface be presented for those who want to use the class.
# In other programming languages, this is usually done with private methods and attributes, 
# which block external access to certain methods and attributes in a class.

# The Python philosophy is slightly different. 
# It is often stated as "we are all consenting adults here", meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. 
# Hence there are no ways of enforcing a method or attribute be strictly private.
# However, there are ways to discourage people from accessing parts of a class, such as by denoting that it is an implementation detail, 
# and should be used at their own risk.


# 1. Every piece of explanation about every topic in every lesson should be supported by contextual code snippets that complement the text. 
# This enables the learners to understand and retain the concepts more effectively. 
# 2. Links to previous lessons and concepts should be made available inside every lesson. 
# For example, if I forget what a method is or what dictionaries are and need to quickly refresh my memory, 
# there should be a link that takes me to the respective pages of those concepts. 
# Or a persistent glossary of all concepts should be accessible by swiping from the edge of the screen.

# More details and examples about data hiding in Python here: http://radek.io/2011/07/21/private-protected-and-public-in-python/

# MAIN BENEFIT OF DATA HIDING 
# Let's say that you have in your class a variable called 'atdep'. 
# If the attribute 'atdep' is public, the user of the class can change its value to something unwanted and does braking the working of the functions in that class. 
# So you should not have 'atdep' as public, 
# so two underscores before it '__atdep' should do the job of hiding it. 
# Same concept for some class methods and for magic methods. 
# Data hiding is just the technique of hiding the attributes and methods inside a class which are not relevant for the user to call. 
# Finally, in python you cannot really hide data, so the '__atdep' attribute can be accessed using objects of that class. 
# You just need to add before it 'instanceName._className'


# Encapsulation is just the technique of bundling the information in a single unit in a way as to hide what should be hidden and make visible what should be visible.


# What is a private method in Python? -- A method external code is discouraged from using


# "Strictly speaking, private methods are accessible outside their class, just not easily accessible. Nothing in Python is truly private." 
# http://www.diveintopython.net/object_oriented_framework/private_functions.html

# "A method external code is discouraged from using" does match what Python uses instead of a "truly private" method (according to the previous page), 
# but the lesson never called this a private method, and made it sound like there are no private methods in Python. 
# The lesson said there is no way to make a method truly private in Python, 
# and that in other programming languages, private methods are ones that can't be accessed outside a class. 
# This means "A method that can't be accessed from outside a class" must be wrong, 
# but it also makes it seem like Python doesn't have any private methods.


# SECTION 2
# Weakly private methods and attributes have a single underscore at the beginning.
# This signals that they are private, and shouldn't be used by external code. 
# However, it is mostly only a convention, and does not stop external code from accessing them.
# Its only actual effect is that from module_name import * won't import variables that start with a single underscore.
# Example:
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)              # Queue([1, 2, 3])
queue.push(0)
print(queue)              # Queue([0, 1, 2, 3])
queue.pop()
print(queue)              # Queue([0, 1, 2])
print(queue._hiddenlist)  # [0, 1, 2]

# In the code above, the attribute _hiddenlist is marked as private, but it can still be accessed in the outside code.
# The __repr__ magic method is used for string representation of the instance.

# (1): The minor change I made to get this ^ from the example code helps, at least for me, to get it all to make some sense.
# (2): We got a class called Queue, equipped with just a single attribute, namely the attribute hidden_list, for a very clear reason I'll soon explain. 
# This is like how you before we had a Dog class containing multiple instances of the class, 
# such as fido and max, which are Dogs, multiple Dogs, as they're all instances of the Dog class. 
# I THINK we've got a RESTRICTION though on the attribute we provide to all instances of our Queue class. 
# This is shown by the bit of code "self._hiddenlist = list(contents)". 
# Seems to me as if this is trying to say that the attribute assigned to any instance of the Queue class MUST be a LIST of contents. 
# In fact, if you avoid this and REPLACE "queue = Queue([1, 2, 3])" by "queue = Queue(99)", or any other integer instead of that 99, 
# you'd get some output containing the following. line 3, in __init__ self._hiddenlist = list(contents) TypeError: 'int' object is not iterable
# (3): Moving on, the code "queue = Queue([1, 2, 3])" means that we set up an instance of the class Queue, 
# such that its _hiddenlist attribute is equal to the list [1, 2, 3]. 
# The code "print(queue)" intuitively prints "Queue([1, 2, 3])", since after all that's what the object queue is equal to anyway. 
# Now, suppose you had fido instance with grey as its color-attribute, where fido is an instance of the class Dog. 
# Then, the code fido.color would clearly RETURN grey, and hence print(fido.color) would OUTPUT grey. 
# Likewise, since here you've got queue with its _hiddenlist attribute equal to the list [1, 2, 3], 
# and queue is an instance of the class Queue, it follows that the code queue._hiddenlist would RETURN the LIST [1 2, 3], 
# and hence print(queue.hiddenlist) would OUTPUT list [1, 2, 3], and in fact this matches what actually occurs! 
# (4): But note how queue doesn't even EXPLICITLY look like a LIST at all, nor does it look as if it was EXPLICITLY assigned as a variable to a list, 
# but yet it's actually associated to a list. 
# So in some sense I guess you do have a hidden list lying here, 
# and hence why you've got the list under the ATTRIBUTE named _hiddenlist, because it really is something we wish to hide, a private method, 
# and because you want to DISCOURAGE external code from accessing it, you've got a single underscore _ just at the START of its name to indicate this.
# (5): Next, we consider the ★push★ method that got defined. 
# Though, note how just before this, there's the following line of code. 
# self._hiddenlist = list(contents) This to me says that, don't worry!!! "self._hiddenlist" just means a LIST of contents! Nothing else! 
# Just treat it like that and keep it nice and simple, cos it really is nothing more to it than that, honestly. 
# Now look again at the way we define the ★push★ method. 
# Observe how, aside from the trivial self argument, it takes just a single argument, namely "value" as its argument. 
# def push(self, value): self._hiddenlist.insert(0, value) More like: def push(self, value): list(contents).insert(0, value)
# (6): More like: define some push method, for just this class Queue, which would DEMAND, aside from the instance/object of the class, a value as its argument. 
# Then, this method would insert this value into index 0 position of the LIST of contents it for supplied to it as list(contents), 
# which is equal to self._hiddenlist, which is equal to the _hiddenlist ATTRIBUTE of the self object. 
# Here, the self object is taken to be queue and as such its _hiddenlist ATTRIBUTE is equal to the LIST [1, 2, 3], 
# and hence self._hiddenlist is taken to be equal to the LIST [1, 2, 3], which is considered as list(contents) aka the "list of contents" here. 
# So, according to our context here, you just got the following interpretations I THINK. queue.push(0) queue._hiddenlist.insert(0, 0) [1, 2, 3].insert(0, 0)
# (7): Because queue._hiddenlist really refers to the _hiddenlist ATTRIBUTE of the instance queue. 
# So, insert into the list [1, 2, 3], at index 0 position, the value 0. 
# Therefore, the _hiddenlist ATTRIBUTE of the queue instance gets immediately CHANGED to [0, 1, 2, 3]. 
# Hence, despite the queue object still being an instance of the Queue class, 
# it's now got its one and only ATTRIBUTE, its _hiddenlist ATTRIBUTE, as actually equal to the list [0, 1, 2, 3]. 
# In the Python/code language here, this would be said as "queue = Queue([0, 1, 2, 3])". Of course, print(queue) then outputs Queue([0, 1, 2, 3]).
# (8): Afterwards, we've got the pop method defined which, aside from the taking an instance (self) as its argument, 
# doesn't seem to actually DEMAND any arguments at all! 
# Hence, we would expect it to REMOVE ★AND★ RETURN the FINAL item of the list supplied to it. 
# Why should we actually be expecting this? 
# Well, see the definition of this pop method here: "list.pop([i]) Remove the item at the given position in the list, and return it. 
# If no index is specified, a.pop() removes and returns the last item in the list. 
# (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. 
# You will see this notation frequently in the Python Library Reference.)" ~ From here: https://docs.python.org/3.1/tutorial/datastructures.html
# (9): def pop(self): return self._hiddenlist.pop(-1) I THINK the code queue.pop() would get interpreted as follows, 
# where the instance queue gets taken as self in the above definition of the pop method. queue.pop() queue._hiddenlist.pop(-1) [0, 1, 2, 3].pop(-1) 
# Which basically CHANGES the LIST [0, 1, 2, 3] to the one you'd get if you "pop out" (hence the method's intuitive name) or DELETE the element at index position -1. 
# But what's index position -1 element anyway??? 
# Well, index 0 element is 0, index 1 element is 1 etc, so you go towards the RIGHT of your list with INCREASING index. 
# On the other hand, with DECREASING index you go the other way, towards the LEFT. So, index -1 element is clearly 3. 
# Hence, you DELETE the element 3 to get from LIST [0, 1, 2, 3] to the LIST [0, 1, 2].
# (10): Therefore, queue.pop() would CHANGE the _hiddenlist ATTRIBUTE of the instance queue to make it turn into the LIST [0 1, 2], 
# hence erasing the FINAL element of the list permanently. 
# Also, queue.pop() would RETURN the erased element, namely 3, 
# but because there's no print function here with its argument as queue.pop(), 
# it stands to reason that there's nothing to actually OUTPUT here despite 3 being RETURNED. 
# You finally print the queue instance, giving you Queue([0, 1, 2]).


# The most important thing to keep in mind from this example is that __repr__ is an operator overloading for whenever the class is printed out. 
# Without this operator, everytime you had: print(queue) would normally print something in the sorts of: <__main__.Queue object at 0x7f39e0cdbef0> 
# so, instead of that, everytime we print the Queue list, 
# our operator overloading is printing the string "Queue({})", where {} is the current value of self._hiddenlist 
# Now, I'm not sure what <__main__.Queue object at 0x7f39e0cdbef0> means, 
# but I'm guessing that's some sort of memory address or something like that.

# Here's a better explanation. 
class car(): 
  def __init__(self, model="Ford"): 
    self.__model = model ,
  
  def color(self, color): 
    self.__color = color 
    print(str(self.__model) + " is " + str(self.__color)) 
    
c1 = car() 
print(c1.__model) # this will show an error. If you have "self.model" instead of "self.__model", print(c1.model) will work. c1.color("red") 
# this will print. The purpose of encapsulation(data hiding) is to prevent data modification. 
# For example, "self.model" equals "Ford". I can modify it to "Chevy"like this c1.model = "Chevy". 
# However, I can't modify it with "self.__model".

# for folks who are confused about the __repr__ ,this is just a magic method to print instance of a class,for this example it is print(queue),
# we defined this magic method by ourselves and hence whenever it is written as print(queue),it prints that thing which is defined

# What is the purpose of prefacing a method name with a single underscore? --- To mark it as private

# https://radek.io/2011/07/21/private-protected-and-public-in-python/


# SECTION 3
# Strongly private methods and attributes have a double underscore at the beginning of their names. 
# This causes their names to be mangled, which means that they can't be accessed from outside the class.
# The purpose of this isn't to ensure that they are kept private, 
# but to avoid bugs if there are subclasses that have methods or attributes with the same names.
# Name mangled methods can still be accessed externally, but by a different name. 
# The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
# Example:
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)   # 7

s = Spam()
s.print_egg()
print(s._Spam__egg)         # 7
print(s.__egg)              # AttributeError

# Basically, Python protects those members by internally changing the name to include the class name.


# Differences with TWO underscores and with ONE underscore. 
''' variable egg with two underscores ''' 
class Spam: 
  __egg = 7 
  def print_egg(self): 
    print(self.__egg) 
    
s = Spam() 
s.print_egg() # 7 
print(s._Spam__egg) # 7 #print(s.__egg) #AttributeError: 'Spam' object has no attribute '__egg' 
''' variable egg with one underscore ''' 
class Spam: 
  _egg = 7 
  def print_egg(self): 
    print(self._egg) 
    
s = Spam() 
s.print_egg() # 7 #print(s._Spam_egg) #AttributeError: 'Spam' object has no attribute '_Spam_egg' print(s._egg) # 7




# (1): Before diving into the example they've got there, it may help for you to consider the following which I got from somewhere else. 
# I've even questioned it and got a solid nicce answer, as shown below. 
# Example:
class Spam: 
  egg = 7 
  def print_egg(self): 
    print(self.egg) 
    
s = Spam() 
# First, the __init__(self) method is called the initializer. It is NOT mandatory to include an initializer method. 
# The egg = 7 above is a class variable. This variable is common to ALL INSTANCES of the class Spam. 
# So if you do s1 = Spam() s2 = Spam() s1.egg and s2.egg will both be 7. 
# You can also access egg with Spam.egg, or s1.egg or s2.egg. It's all the same egg.
# (2): The other thing to note is that if you try to access an INSTANCE method or variable and python doesn't find one, 
# it'll look at the CLASS dictionary to see if there's a CLASS method or variable of THAT name. 
# Which is why self.egg works here. So one of reasons you'd need an initializer method is to initialize instance members of a class. 
# There are none here, just a variable belonging to the class. 
# Q: Please can you explain last paragraph further? 
# We've got the class Spam here, and s=Spam(), as well as s1=Spam() and s2=Spam(), would be all INSTANCES of the class Spam, 
# but all without any attributes whatsoever according to my understanding. 
# Aren't these 3 instance members of the class Spam? 
# A: Those 3 (s, s1, and s2) are instances of Spam. However they have no instance attributes defined in the initializer of Spam.
# (3): Ok let's use better python terminology. I use multiple languages daily any my terminology gets jumbled. 
# Look at this example: 
class SomeClass: 
    count = 5 # this is class attribute 
    def __init__(self,x): 
        self.count = x; # this is an instance attribute 
        
    def print_instance_variable(self): 
        print(self.count) 
        @classmethod 
        
    def print_class_variable(cls): 
        print(cls.count)
        
if __name__ == '__main__':
    s = SomeClass(1) 
    s.print_instance_variable() # 1 
    s.print_class_variable() # 5 
    print(SomeClass.count) # 5 
    print(s.count) # 1 
    s2 = SomeClass(2) s2.print_class_variable() #5 
    s2.print_instance_variable() #2 
    print(s2.count) #2 
# The COMMENTS are what gets OUTPUT.
# (4): So when you have a definition like this class SomeClass: count = 5 you're defining an attribute that belongs to the entire class. 
# Every instance of SomeClass will have count == 5. When you get to the initializer def __init__(self,x): self.count = x; 
# this is an instance attribute self.count defines an instance attribute. 
# This will defer among every instance of SomeClass, depending on what you provide as a parameter. 
# In the above example, we first have a self.count of 1. Notice how this is different from the class attribute, despite them sharing a name.
# (5): So now even though we have two separate instances of SomeClass, which we call s and s2, 
# and s and s2 have different values for their instance attributes, they still share the same class attribute count. 
# On lines 19 and 20 we access them directly. Notice how print(s.count) Prints 1, because it's accessing the instance attribute count. 
# And print(SomeClass.count) Prints 5, because it's accessing the class attribute count.
# (6): Also, print(s2.count) Prints 2. 
# Remember, you can name class attributes and instance attributes the same thing, in which case you have to access them properly with the proper scope. 
# Also, if you define a class attribute you can access it from an instance of a class, provided there are no instance attributes of the same name. 
# I kind of dislike this feature, since it tends to confuse people learning.


# Example:
class Spam: 
    __egg = 7 
    _egg = 14 
    egg = 21 
    def print_egg(self): 
        print(self.__egg) 
        print(self._egg) 
        print(self.egg) 
        
s1= Spam() 
s1.print_egg() # 7 /n 14 /n 21 
print(s1.__egg)# Attribute error 
print(s1._egg) # 14 
print(s1.egg) # 21 So how to get (__egg)and why is attribute error? It is because of double underscore. 
# To get __egg, try this way out:- 
print(s1._Spam__egg) #7
        

# Let me explain on my behalf as i am doing python not from so long , but i will answer this very simply. 
class Spam: 
    __egg = 7 #__egg=7 is a class variable can be accessed in class anywhere and mentioned strongly private 
    def print_egg(self): 
        print(self.__egg) #intance attribute access __egg because its inside the class 
        
s = Spam() 
s.print_egg() #not a private method, hence accessible 
print(s._Spam__egg) #__egg is accessible when _single underscore used with classname 
print(s.__egg) #not accessible because it kept private with __underscore but can be accessible when calling with _singleunderscore with classname and __egg with double only. 
# similarly if we will define print_egg method as strongly private then it can not accessible outside directly
# Example:
class Spam: 
    __egg = 7 
    def __print_egg(self): 
        print(self.__egg) 
        
s = Spam() 
s.__print_egg() # will produce an attribute error because method is kept private but s._Spam__print_

# They are three methods 
# 1.public:public method hasn't underscore.we can access any ware 
# 2._protected:single underscore methods. we can also access from outside 
# 3.__private:a method has double underscore.we can't possible to access outside of the class.if we want to access we should use. 
# Single underscore with class name and private method _classname__method name that's simple no need to feel confusion here


# Example:
# даже просто по выводу этот код делает тему намного яснее, чем ее объяснили даже сами сололерны. В общем, тут мы видим, как...
# мы создали класс
class Spam:
    #создали переменную __egg с двойным подчёркиванием. То есть имя 'искажено', как в теме сказали.
    __egg = 7
    # я решил сделать ещё одну переменную, чтоб вы увидели, в чем разница.
    egg = 8
    # этот метод применим как к первой, так и ко второй переменной. Он...
    def print_egg(self):
        # ... выводит на экран значение переменной.
        print(self.egg)     # 8
# создаем экземпляр
s = Spam()
# это выведет нам вторую переменную...
s.print_egg()
# а это первую, потому что мы ее вызвали чуть другим способом, как указано в уроке.
print(s._Spam__egg)         # 7
print('Надеюсь, помогло :)')# Надеюсь, помогло :)

# How would the attribute __a of the class b be accessed from outside the class? _b__a
# For those who didn't get the logic: 
# In theory section, it is mentioned that strongly private attributes have "double underscore" 
# hence it is __a and the class name is b 
# The format for this question is: _classname__attribute (remember: 
# This double underscore is the part of attributes which makes them strongly private) 
# Hence answer should be: _classname__attribute _b__a

# in given data b is class and a is attribute(privatemethod) and it accessed by externally as.. _class__attribute _b__a




