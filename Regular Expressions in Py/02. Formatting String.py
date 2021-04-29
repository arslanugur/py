2. Formatting Strings
You will learn the main approaches that can be used to format 
or interpolate strings in python using a dataset containing information scraped from the web. 
You will explore the advantages and disadvantages 
of using positional formatting, embedding expressing inside string constants, and using the Template class.

2.1. Positional formatting
1. Positional formatting
The next step of our journey is string formatting. In this video, we'll talk about positional formatting.

2. What is string formatting?
String formatting is also called string interpolation. It is the process of inserting a custom string in a predefined text. 
Here, we see an example. Don't panic. We are going to explain this later. 
As data scientist, you will use it to insert a title in a graph, show an error message or pass a statement into a function.

3. Methods for formatting
The modern versions of Python have three main approaches to string formatting: positional formatting, covered in this video, 
formatted strings literals, and template methods, covered in following videos.

4. Positional formatting
Positional formatting works in the following way. We put placeholders defined by a pair of curly braces in a text. 
We call the string dot format method. Then, we pass the desired value into the method. 
The method replaces the placeholders using the values in order of appearance. Let's examine the example. 
We define a string and insert two placeholders. We pass two strings to the method which will be passed to get the following output.

5. Positional formatting
We can use variables for both the string and the values passed to the method. 
In the example code, we defined a string with placeholders along with two other variables. 
We apply the format method to the string using the two defined variables. 
The method reads the string and replaces the placeholders with the given values. And we get the output seen in the slide.

6. Reordering values
We can add index numbers into the curly braces. This affects the order in which the method replaces placeholders. 
In the example, we left the placeholders empty. The method replaces them with the values in the given order. 
And we get the output shown here. If we add the index numbers, the replacement order changes accordingly. 
Now, the output changes as you can observe.

7. Named placeholders
We can also introduce keyword arguments that are called by their keyword name. 
In the example code, we inserted keywords in the placeholders. 
Then, we call these keywords in the format method. 
We then assign which variable will be passed for each of them resulting in the following output.

8. Named placeholders
Let's examine this code. We have defined a dictionary with keys: tool and goal. We want to insert their values in a string. 
Inside the placeholders, we can specify the value associated with the key tool of the variable data using bracket notation. 
Pay attention to the code. Data is the dictionary specified in the method and tool is the key present in that dictionary. 
So, we get the desired output shown in the slide. Be careful! You need to specify the index without using quotes.

9. Format specifier
We can also use format specifiers inside the curly braces. 
This defines how individual values are presented. We’ll use the syntax index colon specifier. 
One of the most common format specifiers is float represented by the letter f. 
In the code, we specified that the value passed with index 0 will be a float, getting the displayed output. 
We could also add dot two f indicating that we want the float to have two decimals as seen in the resulting output.

10. Formatting datetime
Python has a module called datetime that allows us to, for example, get the date and time for today. 
You can see that the format returned is very particular. 
We can use format specifiers such as percentage y, m, d, h 
and capital m to adjust the format to something more familiar to us as you can observe in the slide.


2.2. Put it in order!
Your company is analyzing the best way to provide users with different online courses. 
Your job is to scrape Wikipedia pages searching for tools used in Data Science subfields. 
You'll store the tool and field name in a database. 
After a text analysis, you realize that the information is provided in a specific position of the text 
but sometimes the field name is given first and the tool after that, while in other cases it's the other way around.

You decide to use positional formatting to handle these situations because it provides a way to reorder placeholders.

The text of one article has already been saved in the variable wikipedia_article. Also, the empty list my_list is already defined. 
You can use print() to view the variable in the IPython Shell.

Instructions 1/4
Assign the substrings going from the 4th to the 19th character inclusive, 
and from the 22nd to the 44th character inclusive of wikipedia_article to the variables first_pos and second_pos, respectively. 
Adjust the strings to be lowercase.

Hint
To select a substring going from the mth to the nth character of a variable, use variable[m-1:n]. 
To adjust the cases of a string to lowercase, use string.lower().

Code:
# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

Instructions 2/4
Define a string with the text "The tool is used in" adding placeholders after the word tool and the word in for future positional formatting. 
Append it to the list my_list.

Hint
To add placeholders to a string for positional formatting, you need to use curly braces; e.g This is for {} formatting.

Code:
# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

Instructions 3/4
Define a string with the text "The tool is used in" adding placeholders after the word tool 
and in but reorder them so the second argument passed to the method will replace the first placeholder. Append to the list my_list.

Hint
To reorder the placeholders, add numbers to them assigning inverse order of appearance, e.g This is a {1} for {0} formatting. 
Remember that the first element has index 0.

Code:
# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")


Instructions 4/4
Complete the for-loop so that it uses the .format() method and the variables first_pos and second_pos to print out every string in my_list.

Hint
To use the .format() method on string with the variables var1 and var2, use string.format(var1, var2).

Code:
# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

# Use format to print strings
for my_string in my_list:
  	print(my_string.format(first_pos, second_pos))
    
Positional formatting is one of the most common use-case for string formatting. 
It is suitable when there is few elements you want to concatenate!

2.3. Calling by its name
You have created your database with the tools and the different Data Science subfields they are used in. 
The company is considering creating courses using these tools and sending personalized emails to the users recommending the different topics. 
They have asked you to make this process more time-efficient. 
To do this, you want to create a template email with a standard message changing the different tools and corresponding field name.

First, you want to try doing this with just one example as a proof of concept. 
You use positional formatting and named placeholders to call the variables in a dictionary.

The variable courses containing one tool and one field name has been saved. 
You can use print(courses) to view the variable in the IPython Shell.

Instructions 1/2
Create a dictionary assigning the first and second element appearing in the list courses to the keys "field" and "tool" respectively.

Hint
Select the nth element of a list using list[n-1].

Code:
# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }
        

Instructions 2/2
Complete the placeholders accessing inside to the elements linked with the keys field and tool in the dictionary data.
Print out the resulting message using the .format() method, passing the plan dictionary to replace the data placeholders.

Hint
Remember that you can access a value associated to a key in a dictionary inside placeholders using {dictionary[key]}.
To pass a dictionary to replace the placeholders in my_message using positional formatting, 
use my_string.format(p=dictionary) where p is the dictionary used in the placeholders.

Code:
# Create a dictionary
plan = {
  		"field": courses[0],
        "tool": courses[1]
        }

# Complete the placeholders accessing elements of field and tool keys in the data dictionary
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

# Use the plan dictionary to replace placeholders
print(my_message.format(data=plan))

For accessing elements in a dictionary when using the str.format() method, you need to use dict[index] without using quotes for index. 
The method converts it automatically to the string "index" when it is looked up in the dict.

2.4. What day is today?
It's lunch time and you are talking with some of your colleagues. 
They comment that they feel that every morning someone should send them a reminder of what day 
it is so they can check in the calendar what their assignments are for that day.

You want to help out and decide to write a small script that takes the date and time of the day so that every morning, 
a message is sent to your colleagues. You can use the module datetime along with named placeholders to achieve your goal.

The date should be expressed as Month day, year, e.g. April 16, 2019 and the time as hh:mm, e.g. 16:30.

You write down some specifiers to help you: %d(day), %B (monthname), %m (monthnumber), %Y(year), %H (hour) and %M(minutes)

You can use the IPython Shell to explore the module datetime.

Instructions
Import the function datetime from the module datetime .
Obtain the date of today and assign it to the variable get_date.
Complete the string message by adding to the placeholders named today and the format specifiers to format the date as month_name day, year and time as hour:minutes.
Print the message using the .format() method and the variable get_date to replace the named placeholders.

Hint
Use: from module import function.
Remember that you can use the function datetime to access .now() and obtain today's date.
Add a name to a placeholder using text {name}. Format date using %B %d, %Y and time %H:%M.
To replace a named placeholder with a value in my_string, use my_string.format(named=value).

Code:
# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Format date
print(message.format(today=get_date))

Datetime is a good module to work with dates but you always need to format them using the format specifiers

2.5. Formatted string literal
1. Formatted string literal
Modern versions of Python introduced a new powerful string formatting: formatted string literal method.

2. f-strings
The strings defined by this method are called f-strings. They have a minimal syntax as you can see in the slide. 
To defined them, you need to add the prefix f before the string. 
Inside quotes, you put your text along with curly braces, which identify placeholders where you insert the expressions. 
In the example code, we have two variables, way and method. 
Then, we define an f-string. Inside curly braces, we pass the two variables. 
The method replaces the placeholders with the variables. And we obtain the following output.

3. Type conversion
f-strings allow us to convert expressions into different types. 
We can use exclamation mark s for strings, r for printable representation of strings, or a to escape non-ascii characters. 
Let's imagine we define the variable name as you can see in the slide. The variable should be surrounded by quotes in the resulting string. 
We can add after the variable the exclamation r conversion. This will return a printable representation of the string. 
In the output, we can see that quotes are surrounding the variable.

4. Format specifiers
We can also use format specifiers such as e for scientific notation, d for digit and f for float. 
In the example code, we define a variable containing a number. 
Then, we insert it in the f-string. We specify that we want it to have only two decimals. And we get the following string.

5. Format specifiers
We can also format datetime. We only need to insert the variable containing the datetime object. 
After that, we placed a colon and the specifiers month name, day and year. 
And we get the string containing the date as we see on the code.

6. Index lookups
Do you remember when we accessed dictionaries from the string format method? 
To insert the value associated with a specific key, we specify the index without quotes. 
Let's try the same to access dictionaries in f-strings. 
As we see in the code, Python raises an error telling us that it cannot find the variable. 
This is due to the fact we need to surround the index with quotes.

7. Escape sequences
In the first video, we said that a string is anything appearing inside quotes. 
If the string contains quotes as well, one of the ways to escape the error raised is to add a backslash before the quotes.

8. Escape sequences
What does this have to do with f-strings? We said that indexes required quotes. f-strings follow the same rule as strings. 
If Python finds a second quote, it understands that this is a closing mark. So we could escape the quotes by adding backslash. 
But, we can observe in the code that backslashes are not allowed in the f-string expression. 
So our only solution is to use single quotes to get the desire output as we can observe in the slide.

9. Inline operations
One of the biggest advantages of f-strings is that they allow us to perform inline operations. 
In the example, we define two numeric variables. We then insert them into the f-string. We can also multiply them inside the expression. 
And we get the result of that operation in the output.

10. Calling functions
We can also call functions inside the expression of f-strings. 
In the example, we define a function. Then, we call this function and pass two numbers inside the expression in the f-string. 
This will return the value in the final string as we can observe in the slide.

2.6. Literally formatting
While analyzing the text from Wikipedia pages, you read that Python 3.6 introduced f-strings.

You remember that you've created a website that displayed data science facts but it was too slow. 
You think that it could be due to the string formatting you used. 
Because f-strings are very fast and easy to use, you decide to rewrite that project.

The variables field1, field2 and field3 containing character strings as well as the numeric variables fact1, fact2, fact3 and fact4 have been saved.

If you want to explore the variables, you can use print() to view them in the IPython Shell.

Instructions 1/3
Complete the f-string to include the variable field1 with quotes and the variable fact1 as a digit.

Hint
For an f-string, use the syntax f"string {variable}". 
After the variable inside the expression, use the type !r to convert to string and show the quotes, and :d for specifying digits.

Code:
# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1:d}st century")


Instructions 2/3
Complete the f-string to include the variable fact2 using exponential notation, and the variable field2.

Hint
For f-string, use the syntax f"string {variable}". 
After the variable inside the expression use :e for specifying that you want exponential notation.

Code:
# Complete the f-string
print(f"About {fact2:e} of {field2} in the world")


Instructions 3/3
Complete the f-string to include field3 together with fact3 rounded to 2 decimals, and fact4 rounded to one decimal.

Hint
For f-string, use the syntax f"string {variable}". For specifying number of n decimals in a float, 
use :.nf after the variable inside the expression.

Code:
# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")

f-strings were introduced to provide a readable and concise way to include the value of Python expressions inside strings. 
They are very fast and the most common specifiers and type conversions can be included.
 
2.7. Make this function
Wow! You are excited to see how fast and easy f-strings worked. So you plan to rewrite some more of your old code.

Now you know that f-strings allow you to evaluate expressions where they appear and include function and method calls. 
You decide to use them in a project where you analyze 120 tweets to check if they include links to different news. 
In that way, you expect the code to be cleaner and more readable.

The variables number1, number2,string1, and list_links have already been pre-loaded.

If you want to explore the variables, you can use print() to view them in the IPython Shell.

Instructions 1/3
Inside the f-string, include number1,number2 and the result of dividing number1 by number2 rounded to one decimal.

Hint
To perform an operation between var1 and var2 inside a f-string, use f"{var1 * var2}". 
Remember that you can use the format specifier :.nf to indicate the number n of decimals.

Code:
# Include both variables and the result of dividing them 
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2:.1f} tweets per min")

Instructions 2/3
Inside the f-string, use .replace() to replace the substring https with an empty substring in string1.

Hint
To call the function .replace() on my_string inside a f-string, use f"text {my_string.replace()}". 
Remember escape sequences are not allowed; different quotes need to be used for the f-string and the strings inside .replace().

Code:
# Replace the substring http by an empty string
print(f"{string1.replace('https', '')}")

Instructions 3/3
Inside the f-string, get list_links length, multiply it by 100 and divide it by 120. Round the result to two decimals.

Hint
To get the length of my_list inside an f-string, use the syntax f"text {len(my_list)}". 
Remember that you can use the format specifier :.nf to indicate the number n of decimals.

Code:
# Divide the length of list by 120 rounded to two decimals
print(f"Only {(len(list_links)*100/120):.2f}% of the posts contain links")

One of the biggest advantages of using f-strings is 
that they allow you evaluate expressions inside calling functions and performing inline operations.


2.8. On time
Lastly, you want to rewrite an old real estate prediction project. 
At the time, you obtained historical information about house prices and used it to make a prediction on future values.

The date was in the datetime format: datetime.datetime(1990, 3, 17) but to print it out, you format it as 3-17-1990. 
You also remember that you defined a dictionary for each neighborhood. 
Now, you believe that you can handle both type of data better with f-strings.

Two dictionaries, east and west, both with the keys date and price, have already been loaded. 
You can use print() to view them in the IPython Shell.

Instructions 1/2
Inside the f-string, access the values of the keys price and date in east dictionary. Format the date to month-day-year.

Hint
To access a value of key in dict inside a f-string, use f"{dict['key']}". To format the date, use the specifiers %m, %d and %Y.

Code:
# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

Instructions 2/2
Inside the f-string, access the values of the keys price and date in west dictionary. Format the date to month-day-year.

Hint
To access a value of key in dict inside a f-string, use f"{dict['key']}". To format the date, use the specifiers %m, %d and %Y.

Code:
# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")

In f-strings, you need to use a literal for the value of 'index' otherwise you can not use a variable as an index. 
Don't forget that escape sequences are not allowed so you need to use different quotes than the one used to define the f-string.
 
2.9. Template method
1. Template method
In this video, we'll take a closer look at the last string formatting method, template strings.

2. Template strings
Template strings have a simpler syntax. They are slow. And they don't allow the use of format specifiers. 
Yet, they are very suitable in some specific situations. 
Specially, when working with externally formatted strings that you don't have control over.

3. Basic syntax
Template strings do not belong to the Python core features. You need to import the Template class from the string module. 
First, you need to create the template string. 
For that, you use the Template constructor that takes only the string, as you can observe in the slide. 
Template strings use dollar signs to identify placeholders or identifiers. 
Then, you need to call the method that substitutes the identifier by the string values. 
For that, you use the identifier name equal the replacement string. And we'll get the output shown in the slide.

4. Substitution
We can place many identifiers as well as variables when using Template strings. 
In the example code, we define two variables containing strings. We can create a template having two identifiers with a designated name. 
Afterward, we call the method substitute to assign the identifiers to the different variables. And we get the following output.

5. Substitution
Sometimes we need to add extra curly braces after the dollar sign to enclose the identifier. 
This is required when valid characters follow the identifier but are not part of it. Let's clarify this. 
In the example, we need to add the ending -ing immediately after the first identifier. We need to include curly braces. 
If we don't do it, Python believes that -ing belong to the identifier name. We replace it by the variable noun obtaining the shown output.

6. Substitution
Let's imagine now that you are working with numbers and you want to include the dollar sign as part of a string. 
Because they are use for identifiers, you will need to escape this character by adding an extra dollar sign. 
And get the correct output as seen in the code.

7. Substitution
In the example code, we have defined a dictionary with only one key. However, when we define our template string, we include two identifiers. 
What would happen if we pass this dictionary to the method substitute? Python will raise an error. 
It tries to replace every placeholder and some of them are missing.

8. Substitution
We could try using the try except block again. In the slide, you can observe again the syntax. The try part will test the given code. 
If any error appears the except part will be executed obtaining the following output as a result.

9. Safe substitution
A better way to handle this situation is using the safe substitute method. 
This method will always try to return a usable string. How? It will place missing placeholders in the resulting string. 
Let's say we have the same situation as before. Now, if we pass the dictionary to the safe substitute, we will not get an error. 
Instead, we'll get the identifier dollar sign cake in our resulting string, as you can observe in the output.

10. Which should I use?
In summary, how do you decide which string formatting you should use? String format is easy to use. 
You could start mastering this method and then apply the concepts to f-strings. 
Moreover, the f-strings are always advisable above all methods. But only if you are working with modern versions of Python. 
Use template strings only when working with user-provided strings.

2.10. Preparing a report
Once again, you scraped Wikipedia pages. This time, you searched for the description of useful tools used for text mining. 
Your first task is to prepare a report about different tools you found. 
You want to format the information contained in the dataset to be printed out as: (tool) is a (description).

In this case, template strings are the best solution to interpolate data generated by external sources into an already created template.

For this example, the variables tool1, tool2 and tool3 contain three article titles. 
Each variable description1, description2 and description3 contains the corresponding article description.

If you want to explore the variables, you can use print() to view them in the IPython Shell.

Instructions 1/3
First of all, import Template from string module.

Hint
To import a class from a module, use from module import class.

Code:
# Import Template
from string import Template


Instructions 2/3
Complete the template using $tool and $description identifiers.

Hint
Remember that the syntax for writing a template is Template("$identifier1 text $indentifier2").

Code:
# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")


Instructions 3/3
Substitute identifiers with the correct tool and description variables in the template and print out the results.

Hint
To substitute the identifier1 and identifier2 in the template string created, use string.substitute(). 
Don't forget to specify identifier1=name and identifier2=description inside each call.

Code:
# Import Template
from string import Template

# Create a template
wikipedia = Template("$tool is a $description")

# Substitute variables in template
print(wikipedia.substitute(tool=tool1, description=description1))
print(wikipedia.substitute(tool=tool2, description=description2))
print(wikipedia.substitute(tool=tool3, description=description3))

Template strings are a simpler string substitution mechanism and even though it's less powerful, 
it's the right choice when you are not sure about the source of strings.


2.11. Identifying prices
After you showed your report to your boss, he came up with the idea of offering courses to the company's users on some of the tools you studied. 
In order to make a pilot test, you will send an email offering a course about one of the tools, randomly chosen from your dataset. 
You also mention that the estimated fee needs to be paid on a monthly basis.

For writing the email, you will use Template strings. 
You remember that you need to be careful when you use the dollar sign since it is used for identifiers in this case.

For this example, the list tools contains the corresponding tool name, fee and payment type for the product offer. 
If you want to explore the variable, you can use print() to view it in the IPython Shell.

Instructions
-Assign the first, second, and third element of tools to the variables our_tool, our_fee and our_pay respectively.
-Complete the template string using $tool, $fee, and $pay as identifiers. 
Add the dollar sign before the $fee identifier and add the characters ly directly after the $pay identifier.
-Substitute identifiers with the three variables you created and print out the results.

Hint
-To select the nth element of list, use list[n-1].
-To write a template, use Template("$identifier1 text $indentifier2"). 
Remember you need to escape the dollar sign by using $$ and use ${identifier} to add valid characters immediately after.
-To substitute an $identifier in a tempstr with a value, use tempstr.substitute(identifier=value).

Code:
# Import template
from string import Template

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))

Because the dollar sign is used for identifiers, 
you need to use curly braces to enclose the identifier name to add valid characters immediately after. 
Also, if a dollar sign has to be in the string, your need to escape it using $$.

2.12. Playing safe
You are in charge of a new project! Your job is to start collecting information from the company's main application users. 
You will make an online quiz and ask your users to voluntarily answer two questions. 
However, it is not mandatory for the user to answer both. 
You will be handling user-provided strings so you decide to use the Template method to print the input information. 
This allows users to double-check their answers before submitting them.

The answer of one user has been stored in the dictionary answers. 
You can use the print() function to view the variables in the IPython Shell.

Instructions 1/3
Complete the template string using $answer1 and $answer2 as identifiers.

Hint
To create a template string, use the following syntax: 
Template("text $identifier text2 $identifier2")

Code:
# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")


Instructions 2/3
Use the method .substitute() to replace the identifiers with the values in answers in the predefined template.

Hint
To substitute identifiers in a tempstr by values in a dict, use tempstr.substitute(dict). 
Remember that if any placeholder is missing, it will raise an error.

Code:
# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use substitute to replace identifiers
try:
    print(the_answers.substitute(answers))
except KeyError:
    print("Missing information")
    

Instructions 3/3
Use the method .safe_substitute() to replace the identifiers with the values in answers in the predefined template.

Hint
To safe substitute identifiers in a tempstr by values in a dict, use tempstr.safe_substitute(dict). 
If any placeholder is missing, the original placeholder will be used by default.

Code:
# Import template
from string import Template

# Complete template string using identifiers
the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")

# Use safe_substitute to replace identifiers
try:
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")
    

.safe_substitute() avoids raising a KeyError 
because it uses the original placeholder if it is missing and consequently, always returns a usable string

