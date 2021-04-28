1. OOP Fundamentals
"""In this chapter, you'll learn what object-oriented programming (OOP) is, how it differs from procedural-programming, 
and how it can be applied. You'll then define your own classes, and learn how to create methods, attributes, and constructors."""

1.1. What is OOP?
2. Procedural vs OOP
Until now, you have probably been coding in so-called procedural style: your code was a sequence of steps to be carried out. 
This is common when doing data analysis: you download the data, process, and visualize it.

3. Thinking in sequences
Procedural thinking is natural. You get up, have breakfast, go to work. 
This sequential viewpoint works great if you are trying to plan your day. 
But if you are a city planner, you have to think about thousands of people with their own routines. 
Trying to map out a sequence of actions for each individual would quickly get unsustainable. 
Instead, you are likely to start thinking about patterns of behaviors. 
Same thing with code. The more data it uses, the more functionality it has, the harder it is to think about as just a sequence of steps.

4. Procedural vs OOP
Instead, we view it it as a collection of objects, and patterns of their interactions - like users interacting with elements of an interface. 
This point of view becomes invaluable when designing frameworks, like application program interfaces or graphical user interfaces, 
or building tools like pandas DataFrames! It will help you organize your code better, making it more reusable and maintainable.

5. Objects as data structures
The fundamental concepts of OOP are objects and classes. 
An object is a data structure incorporating information about state and behavior. 
For example, an object representing a customer can have a certain phone number and email associated with them, 
and behaviors like placeOrder or cancelOrder. 
An object representing a button on a website can have a label, and can triggerEvent when pressed. 
The distinctive feature of OOP is that state and behavior are bundled together: 
instead of thinking of customer data separately from customer actions, we think of them as one unit representing a customer. 
This is called encapsulation, and it's one of the core tenets of object-oriented programming.

6. Classes as blueprints
The real strength of OOP comes from utilizing classes. 
Classes are like blueprints for objects. They describe the possible states and behaviors that every object of a certain type could have. 
For example, if you say "every customer will have a phone number and an email, and will be able to place and cancel orders", 
you just defined a class! This way, you can talk about customers in a unified way.

7. Classes as blueprints
Then a specific Customer object is just a realization of this class with particular state values.

8. Objects in Python
In Python, everything is an object. Numbers, strings, DataFrames, even functions are objects. 
In particular, everything you deal with in Python has a class, a blueprint associated with it under the hood. 
The existence of these unified interfaces, is why you can use, for example, any DataFrame in the same way. 
You can call type() on any Python object to find out its class. 
For example, the class of a numpy array is actually called ndarray (for n-dimensional array).

9. Attributes and methods
Classes incorporate information about state and behavior. 
State information in Python is contained in attributes, and behavior information -- in methods. 
Take a numpy array: you've already been using some of its methods and attributes! 
For example, every numpy array has an attribute "shape" that you can access by specifying the name of the array, then dot, and shape. 
It also has methods, like max and reshape, which are also accessible via dot.

10. Object = attributes + methods
Attributes (or states) in Python objects are represented by variables -- like numbers, or strings, or tuples, in the case of the numpy array shape. 
Methods, or behaviors, are represented by functions. 
Both are accessible from an object using the dot syntax. You can list all the attributes and methods that an object has by calling dir() on it. 
For example here, we see that a numpy array has methods like trace and transpose.

1.2. OOP termininology
That was a lot of terminology at once -- classes, objects, methods, attributes… 
Before you start writing your own object-oriented code, make sure you have a solid grasp on the main concepts of OOP.

Classes and objects both have attributes and methods, 
but the difference is that a class is an abstract template, while an object is a concrete representation of a class.


1.3. Exploring object interface
The best way to learn how to write object-oriented code is to study the design of existing classes. 
You've already learned about exploration tools like type() and dir().

Another important function is help(): calling help(x) in the console will show the documentation for the object or class x.

Most real world classes have many methods and attributes, and it is easy to get lost, 
so in this exercise, you will start with something simpler. 
We have defined a class, and created an object of that class called mystery. 
Explore the object in the console using the tools that you learned.

Instructions 1/3
Question: What class does the mystery object have?
--->  __main__.Employee

Instructions 2/3
So the mystery object is an Employee! Explore it in the console further to find out what attributes it has.
-Print the mystery employee's name attribute.
-Print the employee's salary.

Hint
dir()returns all the attributes and methods of an object. The last few lines of the output of dir(mystery) are
[...,
 '_is_current',
 'email',
 'give_raise',
 'name',
 'promote',
 'rank',
 'salary',
 'terminate']
 
 Code:
 # Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

Instructions 3/3
Natasha -- our mystery employee -- has their salary stored in the attribute .salary.

Give Natasha a raise of $2500 by using a suitable method (use help() again if you need to!).
Print the salary again.

Hint
Don't forget that methods are functions, so they should be called with appropriate parameters!
If you are overwhelmed by the output of help(object_name_here), 
try calling help() on a particular method instead, e.g. help(object_name_here.confusing_method).

Code:
# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)

You can use help() to explore an unfamiliar object.
Notice how descriptive names of attributes and methods, together with the methods' docstrings, 
helped you figure out class functionality even when you didn't know how it was implemented.
Keep this in mind when writing your own classes!


1.4. Class anatomy: attributes and methods
1. Class anatomy: attributes and methods
Great job so far! Now that you know how to work with existing objects and classes, you'll learn how to create your own!

2. A basic class
To start a new class definition, all you need is a class statement, followed by the name of the class, followed by a colon. 
Everything in the indented block after will be considered a part of the class. 
You can create an "empty" class -- like a blank template -- by including the pass statement after the class declaration. 
Even though this class is empty, we can already create objects of the class by specifying the name of the class, followed by parentheses. 
Here, c1 and c2 are two different objects of the empty class Customer. 
We want to create objects that actually store data and operate on it -- in other words have attributes and methods.

3. Add methods to a class
Defining a method is is simple. 
Methods are functions, so the definition of a method looks just like a regular Python function, with one exception: 
the special self argument that every method will have as the first argument, possibly followed by other arguments. 
We'll get back to self in a minute, first let's see how this works. 
Here we defined a method "identify" for the Customer class that takes self and a name as a parameter and prints "I am Customer" plus name when called. 
We create a new customer object, call the method by using object-dot-method syntax and pass the desired name, and get the output. 
Note that name was the second parameter in the method definition, but it is the first parameter when the method is called. 
The mysterious self is not needed the method call.

4. What is self?
So what was that self? Classes are templates. 
Objects of a class don't yet exist when a class is being defined, 
but we often need a way to refer to the data of a particular object within class definition. 
That is the purpose of self - it's a stand-in for the future object. 
That's why every method should have the self argument -- 
so we could use it to access attributes and call other methods from within the class definition even when no objects were created yet. 
Python will handle self when the method is called from an object using the dot syntax. 
In fact, using object-dot-method is equivalent to passing that object as an argument. 
That's why we don't specify it explicitly when calling the method from an existing object.

5. We need attributes
By the principles of OOP, the data describing the state of the object should be bundled into the object. 
For example, customer name should be an attribute of a customer object, instead of a parameter passed to a method. 
In Python attributes -- like variables -- are created by assignment, 
meaning an attribute manifests into existence only when a value is assigned to it.

6. Add an attribute to class
Here is a method set_name with arguments self (every method should have a self argument) and new_name. 
To create an attribute of the Customer class called "name", all we need to do is to assign something to self-dot-name. 
Remember, self is a stand-in for object, so self-dot-attribute should remind you of the object-dot-attribute syntax. 
Here, we set the name attribute to the new_name parameter of the function. When we create a customer, it does not yet have a name attribute. 
But after the set_name method was called, the name attribute is created, and we can access it through dot-name.

7. Using attributes in class definition
Equipped with the name attribute, now we can improve our identification method! 
Instead of passing name as a parameter, we will use the data already stored in the name attribute of the customer class. 
We remove the name parameter from the identify method, and replace it with self-dot-name in the printout, which, via self, 
will pull the name attribute from the object that called the method. 
Now the identify function will only use the data that is encapsulated in the object, instead of using whatever we passed to it.


1.5. Understanding class definitions
Objects and classes consist of attributes (storing the state) and methods (storing the behavior).

Before you get to writing your own classes, you need to understand the basic structure of the class, 
and how attributes in the class definition relate to attributes in the object. 
In this exercise, you have a class with one method and one attribute, as well as the object of that class.

Instructions
Arrange the code blocks in the order that will produce the output 6 when run.
Don't forget to indent the blocks correctly using the <> buttons to the left of the ☰ icon!

Hint
You should define a class before defining objects of that class.
The self variable can only appear in the class definition.
In class definition, attributes are declared by assignment.
An attribute of an object cannot be referenced before it is created.

Code:
class MyCounter:
	def set_count(self, n):
		self.count = n

mc = MyCounter()
mc.set_count(5)
mc.count = mc.count + 1

Notice how you used self.count to refer to the count attribute inside a class definition, 
and mc.count to refer to the count attribute of an object. 
Make sure you understand the difference, and when to use which form


1.6. Create your first class
Time to write your first class! In this exercise, you'll start building the Employee class you briefly explored in the previous lesson. 
You'll start by creating methods that set attributes, and then add a few methods that manipulate them.

As mentioned in the first video, an object-oriented approach is most useful when your code involves complex interactions of many objects. 
In real production code, classes can have dozens of attributes and methods with complicated logic, 
but the underlying structure is the same as with the most simple class.

Your classes in this course will only have a few attributes and short methods, 
but the organizational principles behind the them will be directly translatable to more complicated code.

Instructions 1/3
Create an empty class Employee.
Create an object emp of the class Employee by calling Employee().
Try printing the .name attribute of emp object in the console. What happens?

Hint
You need a class statement and a pass statement.
To create an object cust of the class Customer, we used cust = Customer() in the video.
Don't forget to indent and use proper punctuation!

Code:
# Create an empty class Employee
class Employee:
    pass

# Create an object emp of class Employee  
emp = Employee()


Instructions 2/3
Modify the Employee class to include a .set_name() method that takes a new_name argument, 
and assigns new_name to the .name attribute of the class.
Use the set_name() method on emp to set the name to 'Korel Rossi'.
Print emp.name.

Hint
This is exactly like the .set_name() method of Customer in the video. Check the slides and follow along!

Code:
# Include a set_name method
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Print the name of emp
print(emp.name)


Instructions 3/3
Follow the pattern to add another method - set_salary() - 
that will set the salary attribute of the class to the parameter new_salary passed to method.
Set the salary of emp to 50000.
Try printing emp.salary before and after calling set_salary().

Hint
The set_salary() method, when being defined, should take two parameters: self, and a value to set the salary to.
On the other hand, when called on an object, you should pass only one parameter to set_salary() - the value to set salary to.
To refer to attributes within the class definition, you need to use the self.attr_name syntax.

Code:
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method  
  def set_salary(self, new_salary):
    self.salary = new_salary 
  
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

You created your first class with two methods and two attributes. 
Try running dir(emp) in the console and see if you can find where these attributes and methods pop up!

1.7. Using attributes in class definition
In the previous exercise, you defined an Employee class with two attributes and two methods setting those attributes. 
This kind of method, aptly called a setter method, is far from the only possible kind. 
Methods are functions, so anything you can do with a function, you can also do with a method. 
For example, you can use methods to print, return values, make plots, and raise exceptions, 
as long as it makes sense as the behavior of the objects described by the class (an Employee probably wouldn't have a pivot_table() method).

In this exercise, you'll go beyond the setter methods and learn how to use existing class attributes to define new methods. 
The Employee class and the emp object from the previous exercise are in your script pane.

Instructions 1/3
Print the salary attribute of emp.
Attributes aren't read-only: use assignment (equality sign) to increase the salary attribute of emp by 1500, and print it again.

Hint
No self involved here! Outside the class definitions, attributes belong to specific objects, 
and can only be accessed from those objects using the dot syntax.
You can increase the value of x by 10 by using x = x + 10.

Code:
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 
  
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)

Instructions 2/3
Raising a salary for an employee is a common pattern of behavior, so it should be part of the class definition instead.
Add a method give_raise() to Employee that increases the salary by the amount passed to give_raise() as a parameter.

Hint
The method is a one-liner; in the previous step of this exercise, 
you already wrote the code to increase the salary attribute for a particular object. 
Now adapt that code to make it into a function, with the amount of the raise as a parameter instead of fixed at 1500.
Don't forget that emp does not exist in a class definition -- only self!
The definition of give_raise() should feature two parameters, one of which is the amount of the raise.

Code:
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, amount):
        self.salary = self.salary + amount

emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)


Instructions 3/3
Methods don't have to just modify the attributes - they can return values as well!
-Add a method monthly_salary() that returns the value of the .salary attribute divided by 12.
-Call .monthly_salary() on emp, assign it to mon_sal, and print.

Hint
Did you forget the self again?
monthly_salary() should not have any arguments besides self.

Code:
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12
    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)

You might be wondering: why did we write these methods when all the same operations could have been performed on object attributes directly? 
Our code was very simple, but methods that deal only with attribute values often have pre-processing and checks built in: 
for example, maybe the company has a maximal allowable raise amount. 
Then it would be prudent to add a clause to the give_raise() method that checks whether the raise amount is within limits.


1.8. Class anatomy: the __init__ constructor
1. Class anatomy: the __init__ constructor
Welcome back! In the previous lesson, you learned how to define methods and attributes in classes.

2. Methods and attributes
You learned that methods are functions within class with a special first argument self, 
and that attributes are created by assignment and referred to using the self variable within methods. 
In the exercises, you created an Employee class, and for each attribute you wanted to create, 
you defined a new method, and then called those methods one after another. 
This could quickly get unsustainable if your classes contain a lot of data.

3. Constructor
A better strategy would be to add data to the object when creating it, like you do when creating a numpy array or a DataFrame. 
Python allows you to add a special method called the constructor that is automatically called every time an object is created. 
The method has to be called underscore underscore init underscore underscore 
(the exact name and double underscores are essential for Python to recognize it). 
Here we define the init method for the customer class. 
The method takes on one argument, name, of course in addition to the self argument that should be there for any method. 
In the body of the method, we create the name attribute, set its value to the name parameter, and print a message. 
So now, we can pass the customer name in the parentheses when creating the customer object, 
and the init method will be automatically called, and the name attribute created.

4. Add parameters
We can add another parameter -- say, account balance -- to the init method, and create another attribute -- also called balance, 
that will also be initialized during object creation. 
We can now create a customer by calling Customer with two parameters in parentheses.

5. Default arguments
The init constructor is also a good place to set the default values for attributes. 
For example, here we set the default value of the balance argument to 0, 
so we can create a Customer object without specifying the value of the balance, 
but the attribute is created anyway, and is initialized to the default value 0.

6. The right place to define attributes
So, there are two ways to define attributes: we can define an attribute in any method in a class; 
and then calling the method will add the attribute to the object. 
Alternatively, we can define them all together in the constructor. 
If possible, try to avoid defining attributes outside the constructor. 
Your class definition can be hundreds lines of code long, 
and the person reading it would have to comb through all of them to find all the attributes. 
Moreover, defining all attributes in the constructor ensures that all of them are created when the object is created, 
so you don't have to worry about trying to access an attribute that doesn't yet exist. 
All this results in more organized, readable, and maintainable code.

7. Best practices
While we're on the subject of best practices, let's quickly go over a few more conventions that will make your code more reader-friendly.

8. Best practices
To name your classes, use camel case, which means that if your class name contains several words, 
they should be written without delimiters, and each word should start with a capital letter. 
For methods and attributes, it's the opposite -- words should be separated by underscores and start with lowercase letters.

9. Best practices
Here's a secret: the name "self" is a convention. 
You could actually use any name for the first variable of a method, it will always be treated as the object reference regardless. 
For example, if you are a Java programmer, you might be tempted to use "this", and if you are me, you might be tempted to use "kitty". 
Don't do it, and always use "self".

10. Best practices
Finally, classes, like functions, allow for docstrings which are displayed when help() is called on the object. 
Remember the first lesson of the course, and use the docstrings to make the life of the person using your class easier.


1.9. Correct use of __init__
Python allows you to run custom code - 
for example, initializing attributes - any time an object is created: you just need to define a special method called __init__(). 
Use this exercise to check your understanding of __init__() mechanics!

Which of the code blocks will NOT return an error when run?

class Counter:
	def __init__(self, count, name):
		self.count = 5
		self.name = name

c = Counter(0, "My counter")
print(c.count)

The printout, however, will be 5, while the person writing the code likely expected 0. That's why documentation is important!


1.10. Add a class constructor
In this exercise, you'll continue working on the Employee class. 
Instead of using the methods like set_salary() that you wrote in the previous lesson, 
you will introduce a constructor that assigns name and salary to the employee at the moment when the object is created.

You'll also create a new attribute -- hire_date -- which will not be initialized through parameters, but instead will contain the current date.

Initializing attributes in the constructor is a good idea, 
because this ensures that the object has all the necessary attributes the moment it is created.

Instructions 1/3
Define the class Employee with a constructor __init__() that:
-accepts two arguments, name and salary (with default value0),
-creates two attributes, also called name and salary,
-sets their values to the corresponding arguments.

Hint
To set a default value of a parameter x, use the syntax def my_func(x=value).
The constructor method should be called __init__ -- with both leading and trailing double underscores.
Other than the name, there's nothing special about __init__() -- create it like you would create any other method.

Code:
class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    
    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)

Instructions 2/3
The __init__() method is a great place to do preprocessing.
-Modify __init__() to check whether the salary parameter is positive:
  - if yes, assign it to the salary attribute,
  - if not, assign 0 to the attribute and print "Invalid salary!".

Hint
You can start with:

if salary > 0:
   self.salary = salary
   
Code:
class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
        
   
   # ...Other methods omitted for brevity ... 
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

Instructions 3/3
Import datetime from the datetime module. This contains the function that returns current date.
Add an attribute hire_date and set it to datetime.today().

Hint
The double mention of datetime in the instructions is not a typo: one of them is the name of a module, 
and the other - the name of a class in that module.
To import X from module Y use syntax from Y import X (backwards).
Don't forget to use self. when defining attributes!

Code:
# Import datetime from datetime
from datetime import datetime

class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
        
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.hire_date)

Notice how you had to add the import statement to use the today() function. You can use functions from other modules in your class definition, 
but you need to import the module first, and the import statement has to be outside class definition.


1.11. Write a class from scratch
You are a Python developer writing a visualization package. 
For any element in a visualization, you want to be able to tell the position of the element, 
how far it is from other elements, and easily implement horizontal or vertical flip .

The most basic element of any visualization is a single point. 
In this exercise, you'll write a class for a point on a plane from scratch.

Instructions
Define the class Point that has:

- Two attributes, x and y - the coordinates of the point on the plane;
- A constructor that accepts two arguments, x and y, that initialize the corresponding attributes. 
  These arguments should have default value of 0.0;
- A method distance_to_origin() that returns the distance from the point to the origin. The formula for that is sqrt(x^2 + y^2)
- A method reflect(), that reflects the point with respect to the x- or y-axis: 
    - accepts one argument axis,
    - if axis="x" , it sets the y (not a typo!) attribute to the negative value of the y attribute,
    - if axis="y", it sets the x attribute to the negative value of the x attribute,
    - for any other value of axis, prints an error message.

Note: You can choose to use sqrt() function from either the numpy or the math package, 
but whichever package you choose, don't forget to import it before starting the class definition!

To check your work, you should be able to run the following code without errors:

pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())

and return the output
(-3.0,0.0)
5.0

Hint
Don't forget self! Every time you refer to an attribute within a method, you should use the self.attr syntax.
If you're using a function from a module (e.g. numpy), did you remember to import the module?
x^2 in Python should be written as x ** 2.
The first few lines of the reflect() method could, for example, be:

if axis == "x":
  self.y = - self.y

Code:
# For use of np.sqrt
import numpy as np

class Point:
    """ A point on a 2D plane
    
   Attributes
    ----------
    x : float, default 0.0. The x coordinate of the point        
    y : float, default 0.0. The y coordinate of the point
    """
    def __init__(self, x=0.0, y=0.0):
      self.x = x
      self.y = y
      
    def distance_to_origin(self):
      """Calculate distance from the point to the origin (0,0)"""
      return np.sqrt(self.x ** 2 + self.y ** 2)
    
    def reflect(self, axis):
      """Reflect the point with respect to x or y axis."""
      if axis == "x":
        self.y = - self.y
      elif axis == "y":
        self.x = - self.x
      else:
        print("The argument axis only accepts values 'x' and 'y'!")
        
Notice how you implemented distance_to_origin() as a method instead of an attribute. 
Implementing it as an attribute would be less sustainable - 
you would have to recalculate it every time you change the values of the x and y attributes to make sure the object state stays current.








