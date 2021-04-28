2. Inheritance and Polymorphism
"""Inheritance and polymorphism are the core concepts of OOP that enable efficient and consistent code reuse. 
Learn how to inherit from a class, customize n redefine methods, n review the differences between class-level data n instance-level data."""

2.1. Instance and class data
1. Instance and class data
Congratulations! Now you know the basics of creating classes. 
You might be asking: classes are neat, but how exactly do they help me make my code better? In this chapter, you'll learn about

2. Core principles of OOP
namely, Inheritance and Polymorphism, that, together with encapsulation, form the core principles of OOP. But before we get into it,

3. Instance-level data
you need to learn how to distinguish between instance-level data and class level data. 
Remember the employee class you defined in the previous chapter. 
It had attributes like name and salary, and we were able to assign specific values to them for each new instance of the class. 
These were instance attributes. We used self to bind them to a particular instance.

4. Class-level data
But what if you needed to store some data that is shared among all the instances of a class? 
For example, if you wanted to introduce a minimal salary across the entire organization. 
That data should not differ among object instances. 
Then, you can define an attribute directly in the class body. 
This will create a class attribute, that will serve as a "global variable" within a class. For example,

5. Class-level data
we can define min_salary, and set it to 30000. 
We can use this attribute inside the class like we would use any global variable, only prepended by the class name: 
for example, here we check if the value of salary attribute is greater than MIN_SALARY in the init method. 
Note that we do not use self to define the attribute, and we use the class name instead of self when referring to the attribute.

6. Class-level data
This min_salary variable will be shared among all the instances of the employee class. 
We can access it like any other attribute from an object instance, and the value will be the same across instances. 
Here we print the MIN_SALARY class attribute from two employee objects.

7. Why use class attributes?
So, the main use case for class attributes is global constants that are related to class, 
for example min/max values for attributes -- like the min_salary example -- or commonly used values: 
for example,if you were defining a Circle class, you could store pi as a class attribute.

8. Class methods
What about methods? Regular methods are already shared between instances: the same code gets executed for every instance. 
The only difference is the data that is fed into it. 
It is possible to define methods bound to class rather than an instance, but they have a narrow application scope, 
because these methods will not be able to use any instance-level data. 
To define a class method, you start with a classmethod decorator, followed by a method definition. 
The only difference is that now the first argument is not self, but cls, referring to the class, 
just like the self argument was a reference to a particular instance. 
Then you write it as any other function, keeping in mind that you can't refer to any instance attributes in that method. 
To call a class method, we use class-dot-method syntax, rather than object-dot-method syntax.

9. Alternative constructors
So why would we ever need class methods at all? The main use case is alternative constructors. 
A class can only have one init method, but there might be multiple ways to initialize an object. 
For example, we might want to create an Employee object from data stored in a file. 
We can't use a method, because it would require an instance, and there isn't one yet! 
Here we introduce a class method from_file that accepts a file name, 
reads the first line from the file that presumably contains the name of the employee, and returns an object instance. 
In the return statement, we use the cls variable -- remember that now cls refers to the class, so this will call the init constructor, 
just like using Employee with parentheses would when used outside the class definition.

10. Alternative constructors
Then we can call the method from_file by using class-dot-method syntax, 
which will create an employee object without explicitly calling the constructor.



2.2. Class-level attributes
Class attributes store data that is shared among all the class instances. 
They are assigned values in the class body, and are referred to using the ClassName. syntax rather than self. syntax when used in methods.

In this exercise, you will be a game developer working on a game that will have several players moving on a grid and interacting with each other. 
As the first step, you want to define a Player class that will just move along a straight line. 
Player will have a position attribute and a move() method. 
The grid is limited, so the position of Player will have a maximal value.

Instructions 1/2
-Define a class Player that has:
-A class attribute MAX_POSITION with value 10.
-The __init__() method that sets the position instance attribute to 0.
-Print Player.MAX_POSITION.
-Create a Player object p and print its MAX_POSITION.

Hint
You can define a class attribute right in the body of the class, the same way you would define a global variable.
position is an instance attribute, not a class attribute, so it will need to be accessed via self.

Code:
# Create a Player class
class Player:
    MAX_POSITION = 10
    
    def __init__(self):
      self.position = 0

# Print Player.MAX_POSITION  
print(Player.MAX_POSITION)   

# Create a player p and print its MAX_POSITITON
p = Player()
print(p.MAX_POSITION)


Instructions 2/2
Add a move() method with a steps parameter such that:
-if position plus steps is less than MAX_POSITION, then add steps to position and assign the result back to position;
-otherwise, set position to MAX_POSITION.
Take a look at the console for a visualization!

Hint
The move() method should be a regular method like you've written before, and should take a self argument.
Class attributes like MAX_POSITION are accessed using class name, but instance attributes like position are accessed using self.

Code:
class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter     
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
           self.position = self.position + steps 
        else:
           self.position = Player.MAX_POSITION
    
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()


2.3. Changing class attributes
You learned how to define class attributes and how to access them from class instances. 
So what will happen if you try to assign another value to a class attribute when accessing it from an instance? 
The answer is not as simple as you might think!

The Player class from the previous exercise is pre-defined. 
Recall that it has a position instance attribute, and MAX_SPEED and MAX_POSITION class attributes. 
The initial value of MAX_SPEED is 3.

Instructions 1/2
-Create two Player objects p1 and p2.
-Print p1.MAX_SPEED and p2.MAX_SPEED.
-Assign 7 to p1.MAX_SPEED.
-Print p1.MAX_SPEED and p2.MAX_SPEED again.
-Print Player.MAX_SPEED.
-Examine the output carefully.

Hint
You got this! Nothing here but calling print() and using an assignment (p1.MAX_SPEED = ...).

Code:
# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# Assign 7 to p1.MAX_SPEED
p1.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

Instructions 2/2
Even though MAX_SPEED is shared across instances, assigning 7 to p1.MAX_SPEED didn't change the value of MAX_SPEED in p2, or in the Player class.
So what happened? In fact, Python created a new instance attribute in p1, also called it MAX_SPEED, and assigned 7 to it, without touching the class attribute.
Now let's change the class attribute value for real.
Modify the assignment to assign 7 to Player.MAX_SPEED instead.

Hint
Change p1 to Player on line 9.

Code:
# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE---
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

You shouldn't be able to change the data in all the instances of the class through a single instance. 
Imagine if you could change the time on all the computers in the world by changing the time on your own computer! 
If you want to change the value of the class attribute at runtime, you need to do it by referring to the class name, not through an instance.

2.4. Alternative constructors
Python allows you to define class methods as well, using the @classmethod decorator and a special first argument cls. 
The main use of class methods is defining methods that return an instance of the class, but aren't using the same code as __init__().

For example, you are developing a time series package and want to define your own class for working with dates, BetterDate. 
The attributes of the class will be year, month, and day. 
You want to have a constructor that creates BetterDate objects given the values for year, month, and day, 
but you also want to be able to create BetterDate objects from strings like 2020-04-30.

You might find the following functions useful:
- .split("-") method will split a string at"-" into an array, e.g. "2020-04-30".split("-") returns ["2020", "04", "30"],
- int() will convert a string into a number, e.g. int("2019") is 2019 .

Instructions 1/2
Add a class method from_str() that:
- accepts a string datestr of the format'YYYY-MM-DD',
- splits datestr and converts each part into an integer,
- returns an instance of the class with the attributes set to the values extracted from datestr.

Hint
Did you remember the decorator?
There shouldn't be a self in this method, but there should be a cls!
The return statement should use cls() to create an instance.
The following code will return the year part of the datestr:

all_parts = datestr.split("-")
year = int(all_parts[0])

Remember that you can always refresh your memory about a function by typing help(function_name_here) in the console!

Code:
class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
         # Split the string at "-" and  convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)

Instructions 2/2
For compatibility, you also want to be able to convert a datetime object into a BetterDate object.
-Add a class method from_datetime() that accepts a datetime object as the argument, and uses its attributes .year, .month and .day
to create a BetterDate object with the same attribute values.

Hint
Any datetime object has a .year, .month, and .date attributes, For example, the following code will return the month of today's date:

# create a datetime obect with today's date
today = datetime.today()
today.month

You just need to pass these values into the cls().

Code:
# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, dateobj):
      year, month, day = dateobj.year, dateobj.month, dateobj.day
      return cls(year, month, day) 


# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)

There's another type of methods that are not bound to a class instance - static methods, defined with the decorator @staticmethod. 
They are mainly used for helper or utility functions that could as well live outside of the class, 
but make more sense when bundled into the class. Static methods are beyond the scope of this class, but you can read about them here.
https://docs.python.org/3/library/functions.html#staticmethod

2.5. Class inheritance
1. Class inheritance
Welcome back! Now that you got the basics of classes and instances down, we'll get to the essence of OOP.

2. Code reuse
Object-oriented programming is fundamentally about code reuse. There are millions of people out there writing code, so there's a good chance

3. Code reuse
that someone has already written code that solves a part of your problem! 
Modules like numpy or pandas are a great tool that allows you to use code written by other programmers. 
But what if that code doesn't match your needs exactly? 
For example, you might want to modify the to_csv method of a pandas DataFrame to adjust the output format. 
You could do that by importing pandas and writing a new function, but it will not be integrated into the DataFrame interface. 
OOP will allow you to keep interface consistent while customizing functionality.

4. Code reuse
You will also often find yourself reusing your own code over and over. 
For example, when building a website with a lot of graphical elements like buttons 
and check boxes, no matter what the element is, the basic functionality is the same: you need to be able to draw it and click on it. 
There are a few details that differ based on the type of the element, but a lot of the code will be the repeated. 
Should you copy-paste the basic code for draw and click for every new element?

5. Code reuse
Wouldn't it be better to have a general data structure like GUIelement that implements the basic draw and click functionality only once?

6. Inheritance
We can accomplish this with inheritance. 
Class inheritance is mechanism --
by which we can define a new class that gets all the the functionality of another class plus maybe something extra without re-implementing the code.

7. Example hierarchy
Let's say you have a basic bank account class that has a balance attribute and a withdraw method. In your company, you work with several types of accounts.

8. Example hierarchy
For example, a SavingsAccount also has an interest rate and a method to compute interest, 
but it will also still have a balance, and you definitely should be able to withdraw from it. 
By inheriting methods and attributes of SavingsAccount from BankAccount, 
you'll be able to reuse the code you already wrote for the BankAccount class.

9. Example hierarchy
You could have a CheckingAccount class, that also has a balance, and a withdraw method, but maybe that method is slightly different:

10. Example hierarchy
it modifies the amount to be withdrawn to include a fee. 
With inheritance, we'll be able to customize the withdraw method to first adjust the amount if necessary, 
and then use the method from the BankAccount class -- again, without rewriting it.

11. Implementing class inheritance
How do we implement this? Declaring a class that inherits from another class is very straightforward: 
you simply add parentheses after the class name, and then specify the class to inherit from. 
Here, we define a rudimentary BankAccount class and a seemingly empty SavingsAccount class inherited from it.

12. Child class has all of the the parent data
"Seemingly" because SavingsAccount actually has exactly as much in it as the BankAccount class. 
For example, we can create an object -- even though we did not define a constructor -- 
and we can access the balance attribute and the withdraw method from the instance of SavingsAccount, 
even though these features weren't defined in the new class.

13. Inheritance: "is-a" relationship
That's because inheritance represents "is-a" relationship: a savings account is a bank account, just with some extra features. 
This isn't just theoretical -- that's how Python treats it as well. 
Calling isinstance function on a savingsaccount object shows 
that Python treats it like an instance of both savingsaccount and BankAccount classes, which is not the case for a generic BankAccount object. 
Right now, though, this class doesn't have anything that the original account class did not have.


2.6. Understanding inheritance
Inheritance is a powerful tool of object-oriented languages 
that allows you to customize functionality of existing classes without having to re-implement methods from scratch.

In this exercise you'll check your understanding of the basics of inheritance. 
In the questions, we'll make use of the following two classes:

class Counter:
    def __init__(self, count):
       self.count = count

    def add_counts(self, n):
       self.count += n

class Indexer(Counter):
   pass
   
Instructions
Classify the cards into the correct buckets. Are the statements true or false?

Hint
In the video SavingsAccount was inherited from BankAccount. 
The objects of the class SavingsAccount were both instances of SavingsAccount and BankAccount.
In absence of any other methods, the child class (in this case, Indexer) will use the methods of the Counter class if they are called from an instance.

-Inheritance represents is-a relationship
-Running ind = Indexer() will cause an error
-Class Indexer is inherited from Counter
-If ind is an Indexer object, then isinstance(ind, Counter) will return True. 

The fact that the instances of a child class are also instances of the parent class allows you 
to create consistent interfaces that Alex mentioned in the video. 
Any place that a Counter could go -- for example, as an argument to a function, 
you will be able to use Indexer instead because it has the same methods and attributes as Counter.



2.7. Create a subclass
The purpose of child classes -- or sub-classes, as they are usually called - is to customize and extend functionality of the parent class.

Recall the Employee class from earlier in the course. 
In most organizations, managers enjoy more privileges and more responsibilities than a regular employee. 
So it would make sense to introduce a Manager class that has more functionality than Employee.

But a Manager is still an employee, so the Manager class should be inherited from the Employee class.

Instructions 1/2
Add an empty Manager class that is inherited from Employee.
Create an object mng of the Manager class with the name Debbie Lashko and salary 86500.
Print the name of mng.

Hint
Use the pass statement to create an empty class.
The name of the class to inherit from should go in parentheses.

Code:
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  pass

# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)

Instructions 2/2
Remove the pass statement and add a display() method to the Manager class that just prints the string "Manager" followed by the full name, e.g. "Manager Katie Flatcher"
Call the .display()method from the mnginstance.

Hint
There's nothing special about the display() method in the Manager class: just add it like you'd add any method to a class.

Code:
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
    self.salary += amount

        
# MODIFY Manager class and add a display method
class Manager(Employee):
  def display(self):
    print("Manager ", self.name)


mng = Manager("Debbie Lashko", 86500)
print(mng.name)

# Call mng.display()
mng.display()

The Manager class now includes functionality that wasn't present in the original class (the display() function) 
in addition to all the functionality of the Employee class. Notice that there wasn't anything special about adding this new method.


2.8. Customizing functionality via inheritance
1. Customizing functionality via inheritance
Great job so far! In the previous video, you learned that inheritance allows us to encode is-a relationships between classes.

2. Hierarchy
For example, a SavingsAccount is a special kind of BankAccount that has all the bankaccount functionality, 
but also contains additional properties like an interest rate and a method to compute interest.

3. What we have so far
Here's where we stopped in the last video. We could already create SavingsAccount objects, 
but they did not have any functionality that bank account did not have. Let's start customization by

4. Customizing constructors
adding a constructor specifically for SavingsAccount. 
It will take a balance parameter, just like BankAccount, and an additional interest_rate parameter. 
In that constructor, we first run the code for creating a generic bankaccount by explicitly calling the init method of the bankAccount class. 
Notice that we use BankAccount-dot-init to tell Python to call the constructor from the parent class, and we also pass self to that constructor. Self in this case is a SavingsAccount -- that's the class we're in -- but remember that in Python, instances of a subclass are also instances of the parent class. so it is a BankAccount as well, and we can pass it to the init method of BankAccount. Then we can add more functionality, in this case just initializing an attribute. You actually aren't required to call the parent constructor in the subclass, or to call it first -- you can use new code entirely -- but you'll likely to almost always use the parent constructor.

5. Create objects with a customized constructor
Now when we create an instance of the SavingsAccount class, the new constructor will be called, 
and in particular, the interest_rate attribute will be initialized.

6. Adding functionality
In the exercises, you saw you can add methods to a subclass just like to any other class. 
In those methods you can use data from both the child and the parent class. 
For example here, we add a compute_interest method that returns the amount of interest in the account.. 
Don't worry about the exact formula, just notice that we multiply the balance attribute - 
which was inherited from the BankAccount parent - 
by an expression involving the interest_rate attribute that exists only in the child SavingsAccount class.

7. Customizing functionality
Now let's talk about customizing functionality. SavingsAccount inherits the withdraw method from the parent BankAccount class. 
Calling withdraw on a savings instance will execute exactly the same code as calling it on a generic bank account instance. 
We want to create a CheckingAccount class, which should have a slightly modified version of the withdraw method: 
it will have a parameter and adjust the withdrawal amount.

8. Customizing functionality
Here's an outline of what that could look like. 
Start by inheriting from the parent class, add a customized constructor that also executes the parent code, a new deposit method, and a withdraw method, 
but we add a new argument to withdraw - fee, that specifies the additional withdrawal fee. 
We compare the fee to some fee limit, and then call the parent withdraw method, passing a new amount to it -- with fees subtracted. 
So this method runs almost the same code as the BankAccount's withdraw method without re-implementing it - just augmenting. 
Notice that we can change the signature of the method in the subclass by adding a parameter, 
and we again, just like in the constructor, call the parent version of the method directly by using parent-class-dot syntax and passing self.

9. Comparison
Now when you call withdraw from an object that is a CheckingAccount instance, the new customized version will be used, 
but when you call it from regular BankAccount, the basic version will be used. 
The interface of the call is the same, and the actual method that is called is determined by the instance class. 
This is an application of polymorphism, and we'll learn more about it later in the course. 
Another difference is that for a CheckingAccount instance, we could call the method with 2 parameters. 
But trying this call for a generic BankAccount instance would cause an error, 
because the method defined in the BankAccount class was not affected by the changes in the subclass.


2.9. Method inheritance
Inheritance is powerful because it allows us to reuse and customize code without rewriting existing code. 
By calling methods of the parent class within the child class, we reuse all the code in those methods, making our code concise and manageable.

In this exercise, you'll continue working with the Manager class that is inherited from the Employee class. 
You'll add new data to the class, 
and customize the give_raise() method from Chapter 1 to increase the manager's raise amount by a bonus percentage whenever they are given a raise.

A simplified version of the Employee class, as well as the beginning of the Manager class 
from the previous lesson is provided for you in the script pane.

Instructions 1/2
Add a constructor to Manager that:
-accepts name, salary (default 50000), and project (default None)
-calls the constructor of the Employee class with the name and salary parameters,
-creates a project attribute and sets it to the project parameter.

Hint
To call a method from a parent class inside the child class, 
use the syntax Parent.method_name and pass the instance variable as the first argument.


Code:
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
  # Add a constructor 
    def __init__(self, name, salary=50000, project=None):
        # Call the parent's constructor   
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project
  
    def display(self):
        print("Manager ", self.name)
  
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
  # Add a constructor 
    def __init__(self, name, salary=50000, project=None):
        # Call the parent's constructor   
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project
  
    def display(self):
        print("Manager ", self.name)
  

Instructions 2/2
Add a give_raise() method to Manager that:
-accepts the same parameters as Employee.give_raise(), plus a bonus parameter with the default value of 1.05 (bonus of 5%),
-multiplies amount by bonus,
-uses the Employee's method to raise salary by that product.

Hint
You could write this method in one line: it consists only of the call to Employee.give_raise() with two parameters. 
One of those parameters is amount * bonus.

Code:
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)

In the new class, the use of the default values ensured that the signature of the customized method was compatible with its signature in the parent class. 
But what if we defined Manager's'give_raise() to have 2 non-optional parameters? 
What would be the result of mngr.give_raise(1000)? 
Experiment in console and see if you can understand what's happening. 
Adding print statements to both give_raise() could help!


2.10. Inheritance of class attributes
In the beginning of this chapter, you learned about class attributes and methods that are shared among all the instances of a class. 
How do they work with inheritance?

In this exercise, you'll create subclasses of the Player class from the first lesson of the chapter, 
and explore the inheritance of class attributes and methods.

The Player class has been defined for you. 
Recall that the Player class had two class-level attributes: MAX_POSITION and MAX_SPEED, with default values 10 and 3.

Instructions 1/2
Create a class Racer inherited from Player,
Assign 5 to MAX_SPEED in the body of the class.
Create a Player object p and a Racer object r (no arguments needed for the constructor).
Examine the printouts carefully. Next step is a quiz!

Hint
Make sure that Racer inherits from Player. The syntax is class Child(Parent):

Code:
class Racer(Player):
    MAX_SPEED = 5
    
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)

Instructions 2/2
Question: Which of the following statements about inheritance of class attributes is correct?

Class attributes CAN be inherited, and the value of class attributes CAN be overwritten in the child class
But notice that the value of MAX_SPEED in Player was not affected by the changes to the attribute of the same name in Racer.

Hint
Examine the output and the Racer definition carefully. 
print(r.MAX_POSITION) returns 10 even though MAX_POSITION is not defined explicitly in the Racer class

print(r.MAX_POSITION) returns 10 even though MAX_POSITION is not defined explicitly in the Racer class, so it was inherited from Player. 
Moreover, MAX_SPEED was explicitly defined in Racer without errors.

Examine from print(r.MAX_SPEED) and compare it to print(p.MAX_SPEED).


2.11. Customizing a DataFrame
In your company, any data has to come with a timestamp recording when the dataset was created, 
to make sure that outdated information is not being used. 
You would like to use pandas DataFrames for processing data, but you would need to customize the class to allow for the use of timestamps.

In this exercise, you will implement a small LoggedDF class that inherits from a regular pandas DataFrame 
but has a created_at attribute storing the timestamp. 
You will then augment the standard to_csv() method to always include a column storing the creation date.

Tip: all DataFrame methods have many parameters, and it is not sustainable to copy all of them for each method you're customizing. 
The trick is to use variable-length arguments *args and **kwargsto catch all of them.

Instructions 1/2
Import pandas as pd.
Define LoggedDF class inherited from pd.DataFrame.
Define a constructor with arguments *args and **kwargs that:
    calls the pd.DataFrame constructor with the same arguments,
    assigns datetime.today() to self.created_at.

Hint
You should call pd.DataFrame.__init__() inside the __init__() method for your class

Code:
# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
    
ldf = LoggedDF({"col1": [1,2], "col2": [3,4]})
print(ldf.values)
print(ldf.created_at)


Instructions 2/2
Add a to_csv() method to LoggedDF that:
copies self to a temporary DataFrame using .copy(),
creates a new column created_at in the temporary DataFrame and fills it with self.created_at
calls pd.DataFrame.to_csv() on the temporary variable.

Hint
Don't forget to pass *args and **kwargs in your call to pd.DataFrame.to_csv()

Code:
# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
  def to_csv(self, *args, **kwargs):
    # Copy self to a temporary DataFrame
    temp = self.copy()
    
    # Create a new column filled with self.created at
    temp["created_at"] = self.created_at
    
    # Call pd.DataFrame.to_csv on temp with *args and **kwargs
    pd.DataFrame.to_csv(temp, *args, **kwargs)
    

Using *args and **kwargs allows you to not worry about keeping the signature of your customized method compatible. 
Notice how in the very last line, you called the parent method and passed an object to it that isn't self. 
When you call parent methods in the class, they should accept some object as the first argument, 
and that object is usually self, but it doesn't have to be!    


