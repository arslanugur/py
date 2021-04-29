4.  Best Practices of Class Design
"""How do you design classes for inheritance? Does Python have private attributes? Is it possible to control attribute access? 
You'll find answers to these questions (and more) as you learn class design best practices."""

4.1. Designing for inheritance and polymorphism
1. Designing for inheritance and polymorphism
In this final chapter, we'll talk about some good practices of class design. 
We'll cover two main topics: efficient use of inheritance, and managing the levels of access to the data contained in your objects.

2. Polymorphism
Polymorphism means using a unified interface to operate on objects of different classes. We've already dealt with it in Chapter 2.

3. Account classes
We defined a bank account class, and two classes inherited from it: a checking account class and a savings account class. 
All of them had a withdraw method, but the checking account's method was executing different code.

4. All that matters is the interface
Let's say we defined a function to withdraw the same amount of money from a whole list of accounts at once. 
This function doesn't know -- or care -- whether the objects passed to it are checking accounts, 
savings accounts or a mix -- all that matters is that they have a withdraw method that accepts one argument. 
That is enough to make the function work. It does not check which withdraw it should call -- the original or the modified. 
When the withdraw method is actually called, 
Python will dynamically pull the correct method: 
modified withdraw for whenever a checking account is being processed,and base withdraw for whenever a savings 
or generic bank account is processed. So you, as a person writing this batch processing function, 
don't need to worry about what exactly is being passed to it, only what kind of interface it has. 
To really make use of this idea, you have to design your classes with inheritance and polymorphism - the uniformity of interface - in mind

5. Liskov substitution principle
There is a fundamental object-oriented design principle of when and how to use inheritance properly, 
called "Liskov substitution principle" named after the computer scientist Barbara Liskov: 
A base class should be interchangeable with any of its subclasses without altering any properties of the surrounding program. 
Using the example of our Account hierarchy, that means that wherever in your application you use a bankaccount object instance, 
substituting a checking account instead should not affect anything in the surrounding program. 
For example, the batch withdraw function worked regardless of what kind of account was used.

6. Liskov substitution principle
This should be true both syntactically and semantically. 
On the one hand, 
the method in a subclass should have a signature with parameters and returned values compatible with the method in the parent class. 
On the other hand, 
the state of objects also must stay consistent; 
the subclass method shouldn't rely on stronger input conditions, should not provide weaker output conditions, 
it should not throw additional exceptions and so on.

7. Violating LSP
Let's illustrate some possible violations of LSP - 
Liskov substitution principle - on our account classes: for example, the parent's -- or base's -- withdraw method could require 1 parameter, 
but the subclass method could require 2. Then we couldn't use the subclass's withdraw in place of the parent's.
But if the subclass method has a default value for the second parameter, then there is no problem. 
If the subclass method only accepts certain amounts, unlike the base one, 
then sometimes the subclass could not be used in place of the base class, if those unsuitable amounts are used. 
If the base withdraw had a check for whether the resulting balance is positive, and only performed the withdrawal in that case, 
but the subclass did not do that, we wouldn't be able to use subclass in place of the base class, 
because it's possible that ambient program depends on the fact that the balance is always positive after withdrawal.

8. Violating LSP
There are other ways to violate LSP like changing attributes that weren't changed in the base class, or throwing additional exceptions 
that the base class didn't throw (because those new exceptions are guaranteed to be unhandled).

9. No LSP - no inheritance
The ultimate rule is that if your class hierarchy violates the Liskov substitution principle, then you should not be using inheritance, 
because it is likely to cause the code to behave in unpredictable ways somewhere down the road.

4.2. Polymorphic methods
To design classes effectively, you need to understand how inheritance and polymorphism work together.

In this exercise, you have three classes - one parent and two children - each of which has a talk() method. Analyze the following code:
class Parent:
    def talk(self):
        print("Parent talking!")     

class Child(Parent):
    def talk(self):
        print("Child talking!")          

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self)


p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()       
    
What is the output of the code above?
Parent talking!
Child talking!
Talkative Child talking!
Parent talking!

Polymorphism ensures that the exact method called is determined dynamically based on the instance. 
What do you think would happen if Child did not implement talk()?

4.3. Square and rectangle
The classic example of a problem that violates the Liskov Substitution Principle is "the Circle-Ellipse problem", 
sometimes called the Square-Rectangle problem.

By all means, it seems like you should be able to define a class Rectangle, with attributes h and w (for height and width), 
and then define a class Square that inherits from the Rectangle. After all, a square "is-a" rectangle!

Unfortunately, this intuition doesn't apply to object-oriented design.

Instructions 1/4
Create a class Rectangle with a constructor that accepts two parameters, h and w, and sets its h and w attributes to the values of h and w.
Create a class Square inherited from Rectangle with a constructor that accepts one parameter w, 
and sets both the h and w attributes to the value of w.

Hint
There's nothing tricky in this exercise, so if you're having problems, check the usual suspects: are you using self? 
Correct punctuation? Correct number of parameters and correct attribute names?

Code:
# Define a Rectangle class
class Rectangle:
    def __init__(self, h, w):
      self.h, self.w = h, w

# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
      self.h, self.w = w, w  
      
Instructions 2/4
Question: The classes are defined for you. Experiment with them in the console.

For example, in the console or the script pane, create a Square object with side length 4. Then try assigning 7 to the h attribute.

What went wrong with these classes?
---> The 4x4 Square object would no longer be a square if we assign 7 to h.

Instructions 3/4
A Square inherited from a Rectangle will always have both the h and w attributes, but we can't allow them to change independently of each other.
-Define methods set_h() and set_w() in Rectangle, each accepting one parameter and setting h and w.
-Define methods set_h() and set_w() in Square, each accepting one parameter, and setting both h and w to that parameter in both methods.

Hint
A template method is provided for each class: just replace h with w!
Be careful with parameter names, especially when copy-pasting: make sure you really mean h or w when you're using them!

Code:
class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h
      
# Define set_h to set h       
    def set_h(self, h):
      self.h = h

# Define set_w to set w
    def set_w(self, w):
      self.w = w   
      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 
      
# Define set_h to set w and h 
    def set_h(self, h):
      self.h = h
      self.w = h
      
# Define set_w to set w and h 
    def set_w(self, w):
      self.w = w   
      self.h = w  
      
Instructions 4/4
Question
Later in this chapter you'll learn how to make these setter methods run automatically when attributes are assigned new values, 
don't worry about that for now, just assume that when we assign a value to h of a square, now the w attribute will be changed accordingly.

How does using these setter methods violate Liskov Substitution principle?
---> Each of the setter methods of Square change both h and w attributes, while setter methods of Rectangle change only one attribute at a time, 
so the Square objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant.
Remember that the substitution principle requires the substitution to preserve the oversall state of the program. 
An example of a program that would fail when this substitution is made is a unit test for a setter functions in Rectangle class.


4.4. Managing data access: private attributes
Got It!
1. Managing data access: private attributes
In the next two lessons, we'll talk about managing data access.

2. All class data is public
All class data in Python is technically public. Any attribute or method of any class can be accessed by anyone. 
If you are coming from a background in another programming language like Java, this might seem unusual or an oversight, but it is by design. 
The fundamental principle behind much of Python design "we are all adults here". 
It is a philosophy that goes beyond just code, and describes how the Py community interacts with each other: u should ve trust in ur fellow developers.

3. Restricting access
That said, there are a few ways to manage access to data. 
We can use some universal naming conventions to signal that the data is not for external consumption; 
then, there are special kinds of attributes called properties that allow you to control how each attribute is modified. 
Finally, there are special methods that you can override to change how attributes are used entirely. 
We'll cover the first two options in this chapter, and you are unlikely to ever need anything beyond that.

4. Naming convention: internal attributes
Let's start with naming conventions. 
The first and most important convention is using a single leading underscore to indicate an attribute 
or method that isn't a part of the public class interface, and can change without notice. 
This convention is widely accepted among Python developers, so you should follow it both as a class developer and as a class user. 
Nothing is technically preventing you from using these attributes, 
but a single leading underscore is the developer's way of saying that you shouldn't. 
The class developer trusts that you are an adult and will be able to use the class responsibly. 
This convention is used for internal implementation details and helper functions. 
For example, a pandas DataFrame has an underscore-is_mixed_type attribute that indicates whether the DataFrame contains data of mixed types, 
and the datetime module contains a _ymd2ord function 
that converts a date into a number containing how many days have passed since January 1st of year 1.

5. Naming convention: pseudoprivate attributes
Another naming convention is using a leading double underscore. 
Attributes and methods whose names start with a double underscore are the closest thing Python has to "private" fields 
and methods of other programming languages. 
In this case, it means that this data is not inherited - at least, not in a way you're used to, because Python implements name mangling: 
any name starting with a double underscore will be automatically prepended by the name of the class when interpreted by Python, 
and that new name will be the actual internal name of the attribute or method. 
The main use of these pseudo-private attributes is to prevent name clashes in child classes: 
you can't control what attributes or methods someone will introduce when inheriting from your class, 
and it's possible that someone will unknowingly introduce a name that already exists in you class, thus overriding the parent method or attribute! 
You can use double leading underscores to protect important attributes and methods that should not be overridden. 
Finally, be careful: leading AND trailing double underscores are only used for build-in Python methods like init, 
so your name should only start -- but not end! -- with double underscores.

4.5. Attribute naming conventions
In Python, all data is public. Instead of access modifiers common in languages 
like Java, Python uses naming conventions to communicate the developer's intention to class users, 
shifting the responsibility of safe class use onto the class user.

Python uses underscores extensively to signal the purpose of methods and attributes. 
In this exercise, you will match a use case with the appropriate naming convention.

Instructions
Drag the cards into the bucket representing the most appropriate naming convention for the use case.
_name    - a helper method that checks validity of an attribute's value but isn't considered a part of class's public interface
__name   - A 'version' attribute that stores the current version of the class and shouldn't be passed to child classes, who ill have their own versions.
__name__ - A method that is run whenever the object is printed

The single leading underscore is a convention for internal details of implementation. 
Double leading underscores are used for attributes that should not be inherited to aviod name clashes in child classes. 
Finally, leading and trailing double underscores are reserved for built-in methods.

4.6. Using internal attibutes
In this exercise, you'll return to the BetterDate class of Chapter 2. 
Your date class is better because it will use the sensible convention of having exactly 30 days in each month.

You decide to add a method that checks the validity of the date, but you don't want to make it a part of BetterDate public interface.

The class BetterDate is available in the script pane.

Instructions
Add a class attribute _MAX_DAYS storing the maximal number of days in a month - 30.
Add another class attribute storing the maximal number of months in a year - 12. 
Use the appropriate naming convention to indicate that this is an internal attribute.
Add an _is_valid() method that returns True if the day and month attributes are less than or equal to the corresponding maximum values, and False otherwise. 
Make sure to refer to the class attributes by their names!

Hint
You are free to choose your own name for the second class attribute. All that's required is that it starts with a certain special character…
You can use the ClassNameHere.attr syntax to access the class attributes inside the class.

Code:
# MODIFY to add class attributes for max number of days and months
class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTHS = 12
    
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    
    # Add _is_valid() checking day and month values
    def _is_valid(self):
        return (self.day <= BetterDate._MAX_DAYS) and \
               (self.month <= BetterDate._MAX_MONTHS)
         
bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())

Notice that you were still able to use the _is_valid() method as usual. 
The single underscore naming convention is purely a convention, 
and Python doesn't do anything special with such attributes and methods behind the scenes. 
That convention is widely followed, though, so if you see an attribute name with one leading underscore in someone's class - don't use it! 
The class developer trusts you with this responsibility.

4.7. Properties
1. Properties
You'll learn about properties, which are a special kind of attribute that allow customized access.

2. Changing attribute values
In the beginning of Chapter 1, u worked with an Employee class where you defined methods like set_salary that were used to set the values for attributes. 
Later, you learned about using the constructor to initialize the attributes. 
You also learned that you can access and change the attributes directly by assignment. 
But this means that with a simple equality we can assign anything to salary: a million, a negative number, or even the word "Hello". 
Salary is an important attribute, and that should not be allowed.

3. Changing attribute values
So how do we control attribute access, validate it or even make the attribute read-only? 
We could modify the set_salary method, but that wouldn't help, because we could still use the dot syntax and assignment via equality.

4. Restricted and read-only attributes
There is a precedent for such attribute management with classes that you already know. 
For example, if you have a pandas DataFrame with two columns, you can set the columns attribute to a list of 2 strings -- new names for the columns. 
But if you try to set the attribute to a list of different length, you'd get an error. 
Or, consider the shape attribute -- it cannot be changed at all!

5. @property
We can implement similar behavior using the property decorator. 
Start by defining an "internal" attribute that will store the data. 
As we learned in the previous video, it is recommended to start the name with one leading underscore. 
Here, we defined a underscore-salary attribute. 
Next, we define a method whose name is the exact name we'd like the restricted attribute to have, and put a decorator "property" on it. 
In our case that method is called salary, without underscore, because that's how we'd like to refer to it. 
If we were writing a DataFrame class, this could be "columns", or "shape". 
The method just returns the actual internal attribute that is storing the data. 
To customize how the attribute is set, we implement a method with a decorator "attribute name"-dot-setter: salary-dot-setter in our case. 
The method itself is again named exactly the same as the property -- salary - 
and it will be called when a value is assigned to the property attribute. 
It has a self argument, and an argument that represents the value to be assigned. 
Here we raise an exception if the value is negative, otherwise change the internal attribute. 
So there are two methods called salary -- the name of the property -- that have different decorators. 
The method with property decorator returns the data, and the method with salary dot setter decorator implements validation and sets the attribute.

6. @property
How does this work in practice? We can use this property just as if it was a regular attribute 
(remember the only real attribute we have is the internal underscore-salary). 
Use the dot syntax and equality sign to assign a value to the salary property. 
Then, the setter method will be called. If we try to assign a negative value to salary, an exception will be raised.

7. Why use @property?
Properties are useful because the user of your class will not have to do anything special. 
They won't even be able to distinguish between properties and regular attributes. 
You, on the other hand, now have some control over the access.

8. Other possibilities
There are a few other things you can do with properties: 
if you do not define a setter method, the property will be read-only, like Dataframe shape. 
A method with an attribute-name-dot-getter decorator will be called 
when the property's value is just retrieved, and the method with the attribute-name-dot-deleter -- when an attribute is deleted.


4.8. What do properties do?
You could think of properties as attributes with built-in access control. 
They are especially useful when there is some additional code you'd like to execute when assigning values to attributes.

Which of the following statements is NOT TRUE about properties?
---  Properties can be used to implement "read-only" attributes
---> Properties can prevent creation of new attributes via assignment
---  Properties can be accessed using the dot syntax just like regular attributes
---  Properties allow for validation of values that are assigned to them

This statement is indeed not true! Properties control only one specific attribute that they're attached to. 
There are ways to prevent creating new attributes, but doing so would go against the "we're all adults here" principle.

4.9. Create and set properties
There are two parts to defining a property:
-first, define an "internal" attribute that will contain the data;
-then, define a @property-decorated method whose name is the property name, and that returns the internal attribute storing the data.

If you'd also like to define a custom setter method, there's an additional step:
- define another method whose name is exactly the property name (again), 
    and decorate it with @prop_name.setter where prop_name is the name of the property. 
    The method should take two arguments -- self (as always), and the value that's being assigned to the property.

In this exercise, you'll create a balance property for a Customer class - a better, 
more controlled version of the balance attribute that you worked with before.

Instructions 1/4
Create a Customer class with the __init__() method that:
-takes parameters name and new_bal,
-assigns name to the attribute name,
-raises a ValueError if new_bal is negative,
-otherwise, assigns new_bal to the attribute _balance (with _).

Hint
Did you use the underscore in the name of one of the attributes?
To raise an error, use raise ErrorTypeHere("Optional message here").

Code:
# Create a Customer class
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  
        

Instructions 2/4
Add a method balance() with a @property decorator that returns the _balance attribute.

Hint
Did you remember self?
Is your balance() returning a value?

Code:
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance
        
        
Instructions 3/4
Define another balance() method to serve as a setter, with the appropriate decorator and an additional parameter:
-Raise a ValueError if the parameter is negative,
-otherwise assign it to _balance ;
-print "Setter method is called".

Hint
There are two parts to the decorator. The first part is the name of the property (in this case, balance).
__init__() is doing the same thing to new_bal as your method should do to its parameter.

Code:
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        
        # Print "Setter method is called"
        print("Setter method is called")
        

Instructions 4/4
Create a Customer named Belinda Lutz with the balance of 2000 and save it as cust.
Use the dot syntax and the = to assign 3000 to cust.balance.
Print cust.balance.
In the console, try assigning -1000 to cust.balance. What happens?

Hint
You can access properties just as if they were regular attributes - using the dot syntax.

Code:
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")
        
# Create a Customer        
cust = Customer("Belinda Lutz", 2000)

# Assign 3000 to the balance property
cust.balance = 3000

# Print the balance property
print(cust.balance)

Now the user of your Customer class won't be able to assign arbitrary values to the customers' balance. 
You could also add a custom getter method (with a decorator @balance.getter) 
that returns a value and gets executed every time the attribute is accessed.

4.10. Read-only properties
The LoggedDF class from Chapter 2 was an extension of the pandas DataFrame class 
that had an additional created_at attribute that stored the timestamp when the DataFrame was created, 
so that the user could see how out-of-date the data is.

But that class wasn't very useful: we could just assign any value to created_at after the DataFrame was created, 
thus defeating the whole point of the attribute! Now, using properties, we can make the attribute read-only.

The LoggedDF class from Chapter 2 is available for you in the script pane.

Instructions
Use the "Run code" button to run the code and verify that it's possible to assign an arbitrary value to created_at.
-Modify the code to make the created_at attribute into a read-only property. Don't forget the internal attribute!
Use "Run code" again to verify that assignment now causes an error.
-Put the code assigning a value to ldf.created_at into a try-except block that catches AttributeError exception and prints "Could not set attribute!" when the exception is caught.

Hint
This is pretty involved! Here's the gist of what you'd need to do:
-change all reference to created_at within the class to use internal attribute _created_at instead;
-after that, add a @property-decorated method created_at() to the class that does nothing except returning that internal attribute;
-put ldf.created_at = '2035-07-13' into a try: block, followed by except AttributeError:, and print a message from the except block.

Code:
import pandas as pd
from datetime import datetime

# MODIFY the class to turn created_at into a read-only property
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()
    
    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   
    
    @property  
    def created_at(self):
        return self._created_at

ldf = LoggedDF({"col1": [1,2], "col2":[3,4]})

# Put into try-except block to catch AtributeError and print a message
try:
    ldf.created_at = '2035-07-13'
except AttributeError:
    print("Could not set attribute")
    
Notice that the to_csv() method in the original class was using the original created_at attribute. 
After converting the attribute into a property, 
you could replace the call to self.created_at with the call to the internal attribute that's attached to the property, 
or you could keep it as self.created_at, in which case you'll now be accessing the property. Either way works!

4.11. Congratulations!
Overview
You learned how to think about your code in terms of classes and objects; how to create attributes and methods. 
You explored inheritance and polymorphism -- two ideas that allows you to leverage and customize existing code in powerful ways. 
You also learned the distinction between class-level data and instance-level data. What does it mean for two objects to be equal? 
Turns out, it can mean anything you want, as you learned in chapter 3. 
You defined custom equality functions, readable string representations, even built your own exceptions. 
Finally, you learned what makes a relationship between classes suitable for inheritance, 
how Python handles private vs public data, and how to use properties to manage data access.

3. What's next?
So, where can you go from here? You could start by expanding your knowledge of functionality available in Python. 
For example, learn about mix-in classes and multiple inheritance -- a highly debated feature of Python 
that isn't present in many other object-oriented languages. 
You could learn how to override more built-in operators, like arithmetic operators, or the length operator; 
how to customize attribute access even more using special methods; how to create your own iterator classes that you could use to index loops. 
You could learn about abstract base classes used to create interfaces, or how leverage dataclasses -- a new type of class that is especially suitable for data storage.

4. What's next?
Also consider learning more about object-oriented design, which is based on SOLID principles. 
Solid is an acronym, and you've already learned about the "L" is SOLID -- the Liskov substitution principle, 
but the other 4 letters are just as important. 
Finally, I encourage you to learn more about design patterns -- reusable solutions addressing most common problems in software design.

