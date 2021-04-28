1. Best Practices
"""
We'll cover docstrings and why they matter and how to know when you need to turn a chunk of code into a function. 
You will also learn the details of how Python passes arguments to functions, as well as some common gotchas 
that can cause debugging headaches when calling functions.
"""

1.1. Docstrings
1. Docstrings
You've probably spent a lot of time using functions that someone else wrote. 
In this course, you'll learn how to write functions that others can use. 
Docstrings are a Python best practice that will make your code much easier to use, read, and maintain.

2. A complex function
Look at this split_and_stack() function. 
If you wanted to understand what the function does, what the arguments are supposed to be, and what it returns, 
you would have to spend some time deciphering the code.

3. A complex function with a docstring
With a docstring though, it is much easier to tell what the expected inputs and outputs should be, as well as what the function does. 
This makes it easier for you and other engineers to use your code in the future.

4. Anatomy of a docstring
A docstring is a string written as the first line of a function. 
Because docstrings usually span multiple lines, they are enclosed in triple quotes, Python's way of writing multi-line strings. 
Every docstring has some (although usually not all) of these five key pieces of information: 
what the function does, what the arguments are, what the return value or values should be, info about any errors raised, and anything else you'd like to say about the function.

5. Docstring formats
Consistent style makes a project easier to read, and the Python community has evolved several standards for how to format your docstrings. 
Google-style and Numpydoc are the most popular formats, so we'll focus on those.

6. Google Style - description
In Google style, the docstring starts with a concise description of what the function does. 
This should be in imperative language. 
For instance: "Split the data frame and stack the columns" instead of "This function will split the data frame and stack the columns".

7. Google style - arguments
Next comes the "Args" section where you list each argument name, followed by its expected type in parentheses, and then what its role is in the function. 
If you need extra space, you can break to the next line and indent as I've done here. 
If an argument has a default value, mark it as "optional" when describing the type. 
If the function does not take any parameters, feel free to leave this section out.

8. Google style - return value(s)
The next section is the "Returns" section, where you list the expected type or types of what gets returned. 
You can also provide some comment about what gets returned, but often the name of the function and the description will make this clear. 
Additional lines should not be indented.

9. Google-style - errors raised and extra notes
Finally, if your function intentionally raises any errors, you should add a "Raises" section. 
You can also include any additional notes or examples of usage in free form text at the end.

10. Numpydoc
The Numpydoc format is very similar and is the most common format in the scientific Python community. 
Personally, I think it looks better than the Google style. 
It takes up more vertical space though, 
so this course will either use Google-style or leave out the docstrings entirely to keep the examples compact and legible.

11. Retrieving docstrings
Sometimes it is useful for your code to access the contents of your function's docstring. 
Every function in Python comes with a __doc__ attribute that holds this information. 
Notice that the __doc__ attribute contains the raw docstring, including any tabs or spaces that were added to make the words line up visually. 
To get a cleaner version, with those leading spaces removed, you can use the getdoc() function from the inspect module. 
The inspect module contains a lot of useful methods for gathering information about functions.

1.1. Crafting a docstring
You've decided to write the world's greatest open-source natural language processing Python package. 
It will revolutionize working with free-form text, the way numpy did for arrays, pandas did for tabular data, and scikit-learn did for ML.

The first function you write is count_letter(). 
It takes a string and a single letter and returns the number of times the letter appears in the string. 
You want the users of your open-source package to be able to understand how this function works easily, so you will need to give it a docstring. 
Build up a Google Style docstring for this function by following these steps.

Instructions 1/4
Copy the following string and add it as the docstring for the function: Count the number of times `letter` appears in `content`.
Hint: Use a triple-quoted string so that your docstring can span multiple lines.
  
Code: Crafting a docstring
# Add a docstring to count_letter()
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`."""
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

Instructions 2/4
Now add the arguments section, using the Google style for docstrings. Use str to indicate a string.
Hint:
The arguments section should begin with Args:.
Each argument in the docstring takes the form name (type): description.
  
Code: 
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  # Add a Google-style arguments section
  Args:
    content (str): The string to search.
    letter (str): The letter to search for.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

Instructions 3/4
Add a returns section that informs the user the return value is an int.
Hint: Remember that the section should start with Returns:.

Code: 
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  # Add a returns section
  Returns:
    int
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('"letter" must be a single character string.')
  return len([char for char in content if char == letter])
    
    
Instructions 4/4
Finally, add some information about the ValueError that gets raised when the arguments aren't correct.
Hint: The section about errors begins with Raises:.

Code:
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

1.2. Retrieving docstrings
You and a group of friends are working on building an amazing new Python IDE 
(integrated development environment -- like PyCharm, Spyder, Eclipse, Visual Studio, etc.). 
The team wants to add a feature that displays a tooltip with a function's docstring whenever the user starts typing the function name. 
That way, the user doesn't have to go elsewhere to look up the documentation for the function they are trying to use. 
You've been asked to complete the build_tooltip() function that retrieves a docstring from an arbitrary function.

Note that in Python, you can pass a function as an argument to another function. 
I'll talk more about this in chapter 3, but it will be useful to keep in mind for this exercise.

Instructions 1/3
Begin by getting the docstring for the function count_letter(). Use an attribute of the count_letter() function.

Hint:
We don't want to call the function (e.g. count_letter()). 
Instead, treat the function as an object (e.g. count_letter.<attribute_name>).
Try running dir(count_letter) in the shell to see a list of all of the attributes that the function has.

Code: Retrieving docstrings
# Get the docstring with an attribute of count_letter()
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

Instructions 2/3
Now use a function from the inspect module to get a better-formatted version of count_letter()'s docstring.
Hint:
Try running dir(inspect) in the shell to see the names of all of the available functions in the inspect module.

Code:
import inspect

# Get the docstring with a function from the inspect module
docstring = inspect.getdoc(count_letter)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

or "return" instead of "print" above
print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))

Instructions 3/3
Use the inspect module again to get the docstring for any function being passed to the build_tooltip() function.
Hint:
In build_tooltip() the function argument is the function whose docstring we want to get.
Try running dir(inspect) in the shell to see the names of all of the available functions in the inspect module.

Code:
def build_tooltip(function):
  """Create a tooltip for any function that shows the 
  function's docstring.
  
  Args:
    function (callable): The function we want a tooltip for.
    
  Returns:
    str
  """
  # Use 'inspect' to get the docstring
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))

  
1.3. Docstrings to the rescue!
Some maniac has corrupted your installation of numpy! 
All of the functions still exist, but they've been given random names. 
You desperately need to call the numpy.histogram() function and you don't have time to reinstall the package. 
Fortunately for you, the maniac didn't think to alter the docstrings, and you know how to access them. numpy has a lot of functions in it, 
so we've narrowed it down to four possible functions that could be numpy.histogram() in disguise: numpy.leyud(), numpy.uqka(), numpy.fywdkxa() or numpy.jinzyxq().

Examine each of these functions' docstrings in the IPython shell to determine which of them is actually numpy.histogram().
-numpy.leyud() - appears to be the numpy.reshape() function.
-numpy.uqka() - This is the numpy.argsort() function.
-numpy.fywdkxa() - is actually numpy.histogram() 
-numpy.jinzyxq() - looks like numpy.eye().

1.4. DRY and "Do One Thing"
1. DRY and "Do One Thing"
DRY (also known as "don't repeat yourself") and the "Do One Thing" principle are good ways to ensure that your functions are well designed and easy to test. Let's see how.

2. Don't repeat yourself (DRY)
When you are writing code to look for answers to a research question, it is totally normal to copy and paste a bit of code, tweak it slightly, 
and re-run it. However, this kind of repeated code can lead to real problems. 
In this code snippet, I load my train, validation, and test data, and plot the first two principal components of each data set. 
I wrote the code for the train data set, then copied it and pasted it into the next two blocks, updating the paths and the variable names.

3. The problem with repeating yourself
But one of the problems with copying and pasting is that it is easy to accidentally introduce errors that are hard to spot. 
If you'll notice in the last block, I accidentally took the principal components of the train data instead of the test data. Yikes!

4. Another problem with repeating yourself
Another problem with repeated code is that if you want to change something, you often have to do it in multiple places. 
For instance, if we realized that our CSVs used the column name "label" instead of "labels", we would have to change our code in six places. 
Repeated code like this is a good sign that you should write a function. So let's do that.

5. Use functions to avoid repetition
Wrapping the repeated logic in a function and then calling that function several times makes it much easier to avoid the kind of errors introduced by copying and pasting. 
And if you ever need to change the column "label" back to "labels", 
or you want to swap out PCA for some other dimensionality reduction technique, you only have to do it in one or two places.

6. Problem: it does multiple things
However, there is still a big problem with this function.

7. Problem: it does multiple things
First, it loads the data.

8. Problem: it does multiple things
Then it plots the data.

9. Problem: it does multiple things
And then it returns the loaded data. This function violates another software engineering principle: Do One Thing. 
  Every function should have a single responsibility. Let's look at how we could split this one up.

10. Do One Thing
Instead of one big function, we could have a more nimble function that just loads the data and a second one for plotting. 
We get several advantages from splitting the load_and_plot() function into two smaller functions. 
First of all, our code has become more flexible. Imagine that later on in your script, you just want to load the data and not plot it. 
That's easy now with the load_data() function. Likewise, if you wanted to do some transformation to the data before plotting, 
you can do the transformation and then call the plot_data() function. 
We have decoupled the loading functionality from the plotting functionality.

11. Advantages of doing one thing
The code will also be easier for other developers to understand, and it will be more pleasant to test and debug. 
Finally, if you ever need to update your code, functions 
that each have a single responsibility make it easier to predict how changes in one place will affect the rest of the code.

12. Code smells and refactoring
Repeated code and functions that do more than one thing are examples of "code smells", which are indications that you may need to refactor. 
Refactoring is the process of improving code by changing it a little bit at a time. 
This process is well described in Martin Fowler's book, "Refactoring", which is a good read for any aspiring software engineer.

1.5. Extract a function
While you were developing a model to predict the likelihood of a student graduating from college, 
you wrote this bit of code to get the z-scores of students' yearly GPAs. 
Now you're ready to turn it into a production-quality system, so you need to do something about the repetition. 
Writing a function to calculate the z-scores would improve this code.

# Standardize the GPAs for each year
df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()
df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()
df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()
df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()

Note: df is a pandas DataFrame where each row is a student with 4 columns of yearly student GPAs: y1_gpa, y2_gpa, y3_gpa, y4_gpa

Instructions
Finish the function so that it returns the z-scores of a column.
Use the function to calculate the z-scores for each year (df['y1_z'], df['y2_z'], etc.) from the raw GPA scores (df.y1_gpa, df.y2_gpa, etc.).

Hint:
Notice how 
(df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std() 
is only performing operations on df.y1_gpa. 
So you should be able to pass df.y1_gpa as the column argument to the standardize() function.
  
Code: Extract a function
def standardize(column):
  """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
  # Finish the function so that it returns the z-scores
  z_score = (column - column.mean()) / column.std()
  return z_score

# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df.y1_gpa)
df['y2_z'] = standardize(df.y2_gpa)
df['y3_z'] = standardize(df.y3_gpa)
df['y4_z'] = standardize(df.y4_gpa)


1.6. Split up a function
Another engineer on your team has written this function to calculate the mean and median of a list. 
You want to show them how to split it into two simpler functions: mean() and median()
  
def mean_and_median(values):
  """Get the mean and median of a list of `values`

  Args:
    values (iterable of float): A list of numbers

  Returns:
    tuple (float, float): The mean and median
  """
  mean = sum(values) / len(values)
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]

  return mean, median

Instructions 1/2
Write the mean() function

Code: Split up a function
def mean(values):
  """Get the mean of a list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the mean() function
  mean = sum(values) / len(values)
  return mean

Instructions 2/2
Write the median() function.

Code: Split up a function
def median(values):
  """Get the median of a list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the median() function
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]
  return median

1.7. Pass by assignment
1. Pass by assignment
The way that Python passes information to functions is different from many other languages. 
It is referred to as "pass by assignment", which I will explain in this lesson.

2. A surprising example
Let's say we have a function foo() that takes a list and sets the first value of the list to 99. 
Then we set "my_list" to the value [1, 2, 3] and pass it to foo(). 
What do you expect the value of "my_list" to be after calling foo()? If you said "[99, 2, 3]", then you are right. 
Lists in Python are mutable objects, meaning that they can be changed. 
Now let's say we have another function bar() that takes an argument and adds ninety to it. 
Then we assign the value 3 to the variable "my_var" and call bar() with "my_var" as the argument. 
What do you expect the value of "my_var" to be after we've called bar()? If you said "3", you're right. 
In Python, integers are immutable, meaning they can't be changed.

3. Digging deeper
Let's look at another example to understand what's going on. Imagine that this gray bar is your computer's memory.

4. Digging deeper
When we set the variable "a" equal to the list [1, 2, 3], the Python interpreter says, "Okay, now 'a' points to this location in memory."

5. Digging deeper
Then if we type "b = a", the interpreter says, "Okay, now 'b' points to whatever 'a' is pointing to."

6. Digging deeper
So if we were to append 4 to the end of "a", both variables get it because there is only one list.

7. Digging deeper
Likewise, if we append 5 to "b", both variables get it.

8. Digging deeper
However, if we assign "a" to a different object in memory, that does not change where "b" is pointing. 
Now, things that happen to "a" are no longer happening to "b", and vice versa.

9. Pass by assignment
How does this relate to the example functions we saw earlier?

10. Pass by assignment
When we assign a list to the variable "my_list", it sets up a location in memory for it.

11. Pass by assignment
Then, when we pass "my_list" to the function foo(), the parameter "x" gets assigned to that same location.

12. Pass by assignment
So when the function modifies the thing that "x" points to, it is also modifying the thing that "my_list" points to.

13. Pass by assignment
In the other example, we created a variable "my_var" and assigned it the value 3.

14. Pass by assignment
Then we passed it to the function bar(), which caused the argument "x" to point to the same place "my_var" is pointing.

15. Pass by assignment
But the bar() function assigns "x" to a new value, so the "my_var" variable isn't touched. 
In fact, there is no way in Python to have changed "x" or "my_var" directly, because integers are immutable variables.

16. Immutable or Mutable?
There are only a few immutable data types in Python because almost everything is represented as an object. 
The only way to tell if something is mutable is to see if there is a function or method that will change the object without assigning it to a new variable.

17. Mutable default arguments are dangerous!
Finally, here is a thing that can get you into trouble. foo() is a function that appends the value 1 to the end of a list. 
But, whoever wrote this function gave the argument an empty list as a default value. 
When we call foo() the first time, we get what you would expect, a list with one entry. 
But, when we call foo() again, the default value has already been modified! 
If you really want a mutable variable as a default value, consider defaulting to None and setting the argument in the function.

1.8. Mutable or immutable?
The following function adds a mapping between a string and the lowercase version of that string to a dictionary. 
What do you expect the values of d and s to be after the function is called?
Code:
def store_lower(_dict, _string):
  """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`

  Args:
    _dict (dict): The dictionary to update.
    _string (str): The string to add.
  """
  orig_string = _string
  _string = _string.lower()
  _dict[orig_string] = _string

d = {}
s = 'Hello'

store_lower(d, s)

---> d = {'Hello': 'hello'}, s = 'Hello'

Hint:
Think about whether dictionaries and strings are mutable or immutable.

Dictionaries are mutable objects in Python, so the function can directly change it in the _dict[_orig_string] = _string statement. 
Strings, on the other hand, are immutable. When the function creates the lowercase version, it has to assign it to the _string variable. 
This disconnects what happens to _string from the external s variable.

1.9. Best practice for default arguments
One of your co-workers (who obviously didn't take this course) has written this function for adding a column to a panda's DataFrame. 
Unfortunately, they used a mutable variable as a default argument value! 
Please show them a better way to do this so that they don't get unexpected behavior.

def add_column(values, df=pandas.DataFrame()):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  df['col_{}'.format(len(df.columns))] = values
  return df

                       
Instructions
Change the default value of df to an immutable value to follow best practices.
Update the code of the function so that a new DataFrame is created if the caller didn't pass one.
                        
Hint
Try running add_column(values=range(10)) in the IPython shell multiple times to see why using a mutable value like a DataFrame is a bad idea.
The value None is an immutable value commonly used in Python to mean "no value".

                        
Code: Best practice for default arguments
# Use an immutable variable for the default argument 
def better_add_column(values, df=None):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  # Update the function to create a default DataFrame
  if df is None:
    df = pandas.DataFrame()
  df['col_{}'.format(len(df.columns))] = values
  return df



