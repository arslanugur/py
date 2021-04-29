3. Integrating with Standard Python
"""In this chapter, you'll learn how to make sure that objects that store the same data are considered equal, 
how to define and customize string representations of objects, and even how to create new error types. 
Through interactive exercises, you’ll learn how to further customize your classes to make them work more like standard Python data types."""

3.1. Operator overloading: comparison
1. Operator overloading: comparison
Fantastic work on inheritance! By now, you've learned enough about classes and objects to start effectively using them in your applications. 
In this chapter, you'll learn how to make your objects seamlessly integrate with standard Python operations.

2. Object equality
Have you tried to compare two custom objects? Here are two objects of the Customer class that have the same data. 
If we ask Python if these objects are equal, the answer is "no". 
In this situation, it might make sense: we can have two customers with the same name and account balance.

3. Object equality
But what if each customer has a unique ID number? 
Then two customers with the same ID should be treated as equal.. 
but they aren't The reason why Python doesn't consider two objects with the same data equal by default has to do with 
how the objects and variables representing them are stored.

4. Variables are references
If we try to just print the value of a customer object, 
we'll see "Customer at" and a string (which is actually a number in hexadecimal). 
Behind the scenes, when an object is created, Python allocates a chunk of memory to that object, 
and the variable that the object is assigned to actually contains just the reference to the memory chunk. 
In this code, we tell Python: allocate a chunk of memory for a customer object, and label it customer1. 
Then, allocate another chunk, and label it customer2. 
When we compare variables customer1 and customer2, we are actually comparing references, not the data. 
Because customer1 and customer2 point to different chunks in memory, they are not considered equal.

5. Custom comparison
But it doesn't have to be that way! You might have noticed that, for example, numpy arrays are compared using their data. 
Here, we initialize two numpy arrays with the same data, and Python considers them equal. Same with pandas DataFrames, and many other objects. 
So how can we enforce this for our custom classes?

6. Overloading __eq__()
We can define a special method for this. Remember the __init__ constructor that is implicitly called when an object is created? 
The underscore-underscore-eq-underscore-underscore method is implicitly called whenever two objects of the the same class are compared to each other. 
We can re-define this method to execute custom comparison code. 
The method should accept two arguments, referring to the objects to be compared. 
They are usually called self and other by convention. It should always return a Boolean value -- True or False. 
Here, we have a basic Customer class with id and name attributes, 
and we redefine the eq method to return True if the values of all the attributes are equal. 
We also added a diagnostic printout for illustration.

7. Comparison of objects
Now, if we create two objects containing the same data and try to compare them using double equality sign, 
we see from the diagnostic printout that the eq method is called, and the comparison returns "True". 
On the other hand, if we create two objects with different id values, the comparison will return "False"

8. Other comparison operators
Python allows you to implement all the comparison operators in your custom class using special methods like eq. 
When you use a "not equal" operator -- that is, exclamation point followed by the equality sign -- 
Python will automatically attempt to use the equality method, if it exists, and then negate the result, 
but if you'd like to have a custom "not equals" method, you could implement __ne__. 
You could also implement, for example, "ge" for greater than or equal operator, or "lt" for less than. 
Finally, there is a hash method that allows you to use your objects as dictionary keys and in sets. 
It is beyond the scope of this course, but briefly, it should assign an integer to an object, 
such that equal objects have equal hashes, and the object hash does not change through the object's lifetime.

3.2. Overloading equality
When comparing two objects of a custom class using ==, 
Python by default compares just the object references, not the data contained in the objects. 
To override this behavior, the class can implement the special __eq__() method, 
which accepts two arguments -- the objects to be compared -- and returns True or False. 
This method will be implicitly called when two objects are compared.

The BankAccount class from the previous chapter is available for you in the script pane. 
It has one attribute, balance, and a withdraw() method. 
Two bank accounts with the same balance are not necessarily the same account, 
but a bank account usually has an account number, and two accounts with the same account number should be considered the same.

Instructions
Try selecting the code in lines 1-7 and pressing the "Run code" button. 
Then try to create a few BankAccount objects in the console and compare them.
- Modify the __init__() method to accept a new parameter - number - and initialize a new number attribute.
- Define an __eq__() method that returns True if the number attribute of two objects is equal.
- Examine the print statements and the output in the console.

Hint
The __eq__() method should accept two arguments, usually called self and other.
When adding parameters to __init__(), remember that parameters without default values should be placed before parameters that have default values.

Code:
class BankAccount:
     # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number
      
    def withdraw(self, amount):
        self.balance -= amount 

    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return self.number == other.number    
    
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
    
    
Notice that your method compares just the account numbers, but not balances. 
What would happen if two accounts have the same account number but different balances? 
The code you wrote will treat these accounts as equal, but it might be better to throw an error - an exception - 
instead, informing the user that something is wrong. 
At the end of the chapter, you'll learn how to define your own exception classes to create these kinds of custom errors.

3.3. Checking class equality
In the previous exercise, you defined a BankAccount class with a number attribute that was used for comparison. 
But if you were to compare a BankAccount object to an object of another class that also has a number attribute, 
you could end up with unexpected results.

For example, consider two classes
Code1:
class Phone:
  def __init__(self, number):
     self.number = number

  def __eq__(self, other):
    return self.number == \
          other.number

pn = Phone(873555333)

Code2:
class BankAccount:
  def __init__(self, number):
     self.number = number

  def __eq__(self, other):
    return self.number == \
           other.number

acct = BankAccount(873555333)

Running acct == pn will return True, even though we're comparing a phone number with a bank account number.
It is good practice to check the class of objects passed to the __eq__() method to make sure the comparison makes sense.

Instructions
Both the Phone and the BankAccount classes have been defined. Try running the code as-is using the "Run code" button and examine the output.

Modify the definition of BankAccount to only return True if the number attribute is the same and the type() of both objects passed to it is the same.
Run the code and examine the output again

Hint
Calling type on an object will return its type, for example type("Hello") is str. You need to compare the classes of self and other.

Code:
class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))    

acct = BankAccount(873555333)      
pn = Phone(873555333)
print(acct == pn)class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))    

acct = BankAccount(873555333)      
pn = Phone(873555333)
print(acct == pn)

Now only comparing objects of the same class BankAccount could return True. 
Another way to ensure that an object has the same type as you expect is to use the isinstance(obj, Class) function. 
This can helpful when handling inheritance, as Python considers an object to be an instance of both the parent and the child class. 
Try running pn == acct in the console (with reversed order of equality). What does this tell you about the __eq__() method?

3.4. Comparison and inheritance
What happens when an object is compared to an object of a child class? Consider the following two classes:

class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True

class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True
        
The Child class inherits from the Parent class, and both implement the __eq__() method that includes a diagnostic printout.

Instructions 1/1
Question: Which __eq__() method will be called when the following code is run?
p = Parent()
c = Child()

p == c 

Feel free to experiment in the console -- the classes have already been defined for you.

Child's __eq__() method will be called.
Python always calls the child's __eq__() method when comparing a child object to a parent object.

3.5. Operator overloading: string representation
1. Operator overloading: string representation
Great job with comparison! Let's continue to improve the integration of our custom classes with Python's built-in operators.

2. Printing an object
In the last video, we discovered that calling print on an object of a custom class returns the object's address in memory by default. 
But there are plenty of classes for which the printout is much more informative. 
For example, if we print a numpy array or a DataFrame, we'll see the actual data contained in the object.

3. str vs repr
There are two special methods that we can define in a class that will return a printable representation of an object. 
The double-underscore-str-double-undersrore method is executed when we call print or str on an object, 
and the repr method is executed when we call repr on the object, or when we print it in the console without calling print explicitly. 
The difference is that str is supposed to give an informal representation, suitable for an end user, and repr is mainly used by developers. 
The best practice is to use repr to print a string that can be used to reproduce the object -- 
for example, with numpy array, this shows the exact method call that was used to create the object. 
If you only choose to implement one of them, chose repr, because it is also used as a fall-back for print when str is not defined.

4. Implementation: str
Let's start by implementing the str method. It shouldn't accept any arguments besides self, and it should return a string. 
Here, the string representation of a customer will consist of the word Customer, 
then on the next line , name, colon, followed by the customer's name, then balance, colon, and the customer's balance. 
Just a quick reminder: the triple quotes are used in Python to define multi-line strings, 
and the format method is used on strings to substitute values inside curly brackets with variables. 
If we create a customer object now and call print on that object, we will see a user-friendly output.

5. Implementation: repr
Similarly, we can implement the repr method, which also accepts one argument self and returns a string. 
Following best practices, we make sure that repr returns the string that can be used to reproduce the object, 
in this case, the exact initialization call. Then if we try to print the object in the console, we'll see the the output of repr. 
Moreover, in this class we didn't define the str method, so repr will be used as a fallback for the actual print method as well. 
Notice the single quotes around the name in the return statement. 
Without the quotes, the name of the customer would be substituted into the string as-is, 
but the point of repr is to give the exact call needed to reproduce the the object, where the name should be in quotes. 
Notice also that we can use single quotes inside double quotes and vice versa.

3.6. String formatting review
Before you start defining custom string representations for objects, make sure you are comfortable working with strings and formatting them. 
If you need a refresher, take a minute to look through the official Python tutorial on string formatting.
https://docs.python.org/3/library/stdtypes.html#str.format

In this exercise, consider the following code
my_num = 5
my_str = "Hello"

f = ...
print(f)

where the definition for f is missing.
Here are a few possible variants for the definition of f:
1 --->  f = "my_num is {0}, and my_str is {1}.".format(my_num, my_str)
2 --->  f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str)
3 --->  f = "my_num is {n}, and my_str is '{s}'.".format(n=my_num, s=my_str)
4 --->  f = "my_num is {my_num}, and my_str is '{my_str}'.".format()

Instructions 1/1
Question: Pick the definition of f that will make the code above print exactly the following:

my_num is 5, and my_str is "Hello".

There is only one correct answer! Feel free to use the script pane or console to experiment. ---> 2

To recap: to format a string with variables, you can either use keyword arguments in .format ('Insert {n} here'.format(n=num)), 
refer to them by position index explicitly (like 'Insert {0} here'.format(num)) or implicitly (like 'Insert {} here'.format(num)). 
You can use double quotation marks inside single quotation marks and the way around, 
but to nest the same set of quotation marks, you need to escape them with a slash like \".

3.7. String representation of objects
There are two special methods in Python that return a string representation of an object. 
__str__() is called when you use print() or str() on an object, 
and __repr__() is called when you use repr() on an object, print the object in the console without calling print(), 
or instead of __str__() if __str__() is not defined.

__str__() is supposed to provide a "user-friendly" output describing an object, 
and __repr__() should return the expression that, when evaluated, will return the same object, ensuring the reproducibility of your code.

In this exercise, you will continue working with the Employee class from Chapter 2.

Instructions 1/2
Add the __str__() method to Employee that satisfies the following:

If emp is an Employee object with name "Amar Howard" and salary of 40000, then print(emp) outputs

Employee name: Amar Howard
Employee salary: 40000

Hint
You can use triple quotes """ to define multi-line strings. Alternatively, you can use the special \n character to start a new line.
The best way to insert values of variables into strings is by using .format() or f-strings, but you can also use string concatenation. 
for example "My name is " + name will concatenate the string "My name is " with the variable name.

Code:
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      
    # Add the __str__() method
    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)


Instructions 2/2
Add the __repr__() method to Employee that satisfies the following:

If emp is an Employee object with name "Amar Howard" and salary of 40000, then repr(emp) outputs

Employee("Amar Howard", 40000)

Hint
-Don't forget to add the quotation marks around the name! 
You can use double quotes inside a string defined with single quotes and vice versa, 
or you can escape the quotation marks symbol like this: \"
-The best way to insert values of variables into strings is by using .format() or f-strings, 
but you can also use string concatenation. for example "My name is " + name will concatenate the string "My name is " with the variable name.

Code:
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
      
    # Add the __repr__method  
    def __repr__(self):
        s = "Employee(\"{name}\", {salary})".format(name=self.name, salary=self.salary)      
        return s      

emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))

You should always define at least one of the string representation methods for your object 
to make sure that the person using your class can get important information about the object easily.

3.8. Exceptions
1. Exceptions
Welcome back! Let's talk about exceptions. We'll start with a brief recap, and then learn how to define custom exceptions.

2. Errors are exceptions
Some statements in Python will cause an error when you try to execute them, 
for example dividing by zero, combining objects of incompatible types, and many others. 
These errors are called exceptions. Many exceptions have special names, like ZeroDivisionError or TypeError that you see here. 
If exceptions not handled correctly, they will stop the execution of your program entirely. 
This often makes sense -- for example, if I'm trying to use a variable that 
I never defined, something must have gone very wrong with my script -- but other times it's undesirable. 
For example, a division by zero error might be caused by missing data, which isn't always a good reason to terminate the program.

3. Exception handling
Instead, you might want to execute special code to handle this case. 
To catch an exception and handle it, use the try-except-finally code: wrap the code that you're worried about in a try block, 
then add an except block, followed by the name of the particular exception you want to handle, 
and the code that should be executed when the exception is raised. Then if this particular exception does happen, 
the program will not terminate, but execute the code in the except block instead. You can also have multiple exception blocks. 
And finally, you can use the optional "finally" block that will contain the code that runs no matter what. 
This block is best used for cleaning up like, for example, closing opened files.

4. Raising exceptions
Sometimes, you want to raise exceptions yourself, for example when some conditions aren't satisfied. 
You can use the raise keyword, optionally followed by a specific error message in parentheses. 
The user of the code can then decide to handle the error using try/except.

5. Exceptions are classes
In Python, exceptions are actually classes inherited from built-in classes BaseException or Exception. 
Here's a glimpse into the huge built-in exception class hierarchy. 
For example, there's a general class of arithmetic errors, of which zero division error is a subclass.
https://docs.python.org/3/library/exceptions.html

6. Custom exceptions
You can define your own exceptions in Python! 
Custom exception classes are useful because they can be specific to your application and can provide more granular handling of errors. 
To define a custom exception, just define a class that inherits from the built-in Exception class or one of its subclasses. 
The class itself can be empty - inheritance alone is enough to ensure that Python will treat this class as an exception class. 
For example, let's define a BalanceError class that inherits from Exception. 
Then, in our favorite customer class we raise an exception if a negative balance value is passed to the constructor.

7. Exception in constructor
If we attempt to create a customer with a negative account balance, the BalanceError exception is raised. 
In the first chapter, we dealt with this situation by merely printing a message, and then creating an object with zero balance. 
Handling it with exceptions is better, because in this case, the constructor terminates, 
and the customer object is not created at all, instead of being implicitly created with account balance set to zero, despite the error. 
This sends a clear signal to the user of the Customer class that something went wrong. The user, on their side,

8. Catching custom exceptions
can decide to handle this exception using try-except block if they want, but we, the author of the code, do not make this decision for them. 
For example here, the BalanceError is caught in the except block and if that occurs, a customer is instead created with zero balance.

3.9. Catching exceptions
Before you start writing your own custom exceptions, let's make sure you have the basics of handling exceptions down.

In this exercise, you are given a function invert_at_index(x, ind) that takes two arguments, a list x and an index ind, 
and inverts the element of the list at that index. For example invert_at_index([5,6,7], 1) returns 1/6, or 0.166666 .

Try running the code as-is and examine the output in the console. 
There are two unsafe operations in this function: first, if the element that we're trying to invert has the value 0, 
then the code will cause a ZeroDivisionError exception. 
Second, if the index passed to the function is out of range for the list, the code will cause a IndexError. 
In both cases, the script will be interrupted, which might not be desirable.

Instructions
Use a try - except - except pattern (with two except blocks) inside the function to catch and handle two exceptions as follows:
-try executing the code as-is,
-if ZeroDivisionError occurs, print "Cannot divide by zero!",
-if IndexError occurs, print "Index out of range!"
You know you got it right if the code runs without errors, and the output in the console is:

0.16666666666666666
Cannot divide by zero!
None
Index out of range!
None

Hint
The general structure of the body of the function should be

try:
   # Some code
except FirstErrorName:
   # Code to run when FirstErrorName occurs
except SecondErrorName:   
   # Code to run when SecondErrorName occurs
   
with FirstErrorName and SecondErrorName substituted by the appropriate errors. Don't forget colons and indentation!

Code:
# MODIFY the function to catch exceptions
def invert_at_index(x, ind):
  try:
    return 1/x[ind]
  except ZeroDivisionError:
    print("Cannot divide by zero!")
  except IndexError:
    print("Index out of range!")
 
a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))


Of course, this is only a toy example to illustrate the structure: you can do much more in the except block than just print a message. 
For example, it might make sense for a function to return a special value when an error occurs. 
It's important to note, though, that this code will only be able to handle the two particular errors specified in the except blocks. 
Any other error would still terminate the program.

3.10. Custom exceptions
You don't have to rely solely on built-in exceptions like IndexError: you can define your own exceptions more specific to your application. 
You can also define exception hierarchies. 
All you need to define an exception is a class inherited from the built-in Exception class or one of its subclasses.

In Chapter 1, you defined an Employee class and used print statements and default values 
to handle errors like creating an employee with a salary below the minimum or giving a raise that is too big. 
A better way to handle this situation is to use exceptions. 
Because these errors are specific to our application (unlike, for example, a division by zero error which is universal), 
it makes sense to use custom exception classes.

Instructions 1/3
Define an empty class SalaryError inherited from the built-in ValueError class.
Define an empty class BonusError inherited from the SalaryError class.

Hint
You can define an empty class with the pass statement.

Code:
# Define SalaryError inherited from ValueError
class SalaryError(ValueError): pass

# Define BonusError inherited from SalaryError
class BonusError(SalaryError): pass


Instructions 2/3
Complete the definition of __init__() 
to raise a SalaryError with the message "Salary is too low!" if the salary parameter is less than MIN_SALARY class attribute.
There's no need for else because raise terminates the program anyway.

Hint
Refer to class attributes using ClassName.attr_name syntax.
To raise an exception with a specific error message, you can use raise ExceptionName("Error message here").

Code:
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_RAISE = 5000

  def __init__(self, name, salary = 30000):
    self.name = name
    
    # If salary is too low
    if salary < Employee.MIN_SALARY:
      # Raise a SalaryError exception
      raise SalaryError("Salary is too low!")
      
    self.salary = salary
      
Instructions 3/3
Examine the give_bonus() method, and the rewrite it using exceptions instead of print statements:
    raise a BonusError if the bonus amount is too high;
    raise a SalaryError if the result of adding the bonus would be too low.     


Hint
Refer to class attribute using ClassName.attr_name syntax.
To raise an exception with a specific error message, you can use raise ExceptionName("Error message here").

Code:
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
       raise BonusError("The bonus amount is too high!")
        
    if self.salary + amount <  Employee.MIN_SALARY:
       raise SalaryError("The salary after bonus is too low!")
      
    self.salary += amount
    
Notice that if you raise an exception inside an if statement, you don't need to add an else branch to run the rest of the code. 
Because raise terminates the function, the code after raise will only be executed if an exception did not occur.

3.11. Handling exception hierarchies
Previously, you defined an Employee class with a method get_bonus() that raises a BonusError and a SalaryError depending on parameters. 
But the BonusError exception was inherited from the SalaryError exception. How does exception inheritance affect exception handling?

The Employee class has been defined for you. It has a minimal salary of 30000 and a maximal bonus amount of 5000.

Instructions 1/2
Question: Experiment with the following code

emp = Employee("Katze Rik", salary=50000)
try:
  emp.give_bonus(7000)
except SalaryError:
  print("SalaryError caught!")

try:
  emp.give_bonus(7000)
except BonusError:
  print("BonusError caught!")

try:
  emp.give_bonus(-100000)
except SalaryError:
  print("SalaryError caught again!")

try:
  emp.give_bonus(-100000)
except BonusError:
  print("BonusError caught again!")  
  
and select the statement which is TRUE about handling parent/child exception classes:
---> except block for a parent exception will catch child exceptions

Instructions 2/2
Question: Experiment with two pieces of code:

Code1:
emp = Employee("Katze Rik",\
                    50000)
try:
  emp.give_bonus(7000)
except SalaryError:
  print("SalaryError caught")
except BonusError:
  print("BonusError caught")
  
Code2:
emp = Employee("Katze Rik",\
                    50000)
try:
  emp.give_bonus(7000)
except BonusError:
  print("BonusError caught")
except SalaryError:
  print("SalaryError caught")
      

(one catches BonusError before SalaryError, and the other -SalaryError before BonusError)
Select the statement which is TRUE about the order of except blocks:

---> It's better to include an except block for a child exception before the block for a parent exception, 
      otherwise the child exceptions will be always be caught in the parent block, and the except block for the child will never be executed.

It's better to list the except blocks in the increasing order of specificity, i.e. children before parents, 
otherwise the child exception will be called in the parent except block.
