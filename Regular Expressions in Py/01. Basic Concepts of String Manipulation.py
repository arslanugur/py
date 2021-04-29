1. Basic Concepts of String Manipulation
"""From slicing and concatenating, adjusting the case, removing spaces, to finding and replacing strings. 
   You will learn how to master basic operation for string manipulation using a movie review dataset."""


1.1. Introduction to string manipulation
2. You will learn
In this course, you will learn how to manipulate strings to find and replace specific substrings. 
You will also explore different approaches for string formatting, such as interpolating a string in a template. 
Last, you will dive into basic and advanced regular expressions to master how to find complex patterns in a string.

3. Why it is important
As a data scientist, you can encounter strings when cleaning a dataset to prepare it for text mining or sentiment analysis. 
Sometimes, you will need to process text to feed an algorithm that determines whether an email is spam. 
Maybe, you will need to parse and extract specific data from a website to build a database.Learning 
to manipulate strings and master regular expressions will allow you to perform these tasks faster and more efficiently.

4. Strings
The first step of our journey is strings, a data type used to represent textual data. 
Python recognizes any sequence of characters inside quotes as a single string object. 
As shown on the slide, both single or double quotes can be used. You should use the same quote type to open and close the string. 
If a quote is part of the string as seen in the code, we need to use the other quote type to enclose the string. 
Otherwise, python recognizes the second quote as a closing one.

5. More strings
Python has built-in functions to handle strings. 
Suppose we define the following string. 
We can get the number of characters in the string by applying the function len() which returns eleven as shown in the output. 
The function str() returns the string representation of an object as seen in the code.

6. Concatenation
Suppose now we have the following two strings shown on the slide. You want to concatenate them. 
Concatenate means obtaining a new string that contains both of the original strings. 
Applying the plus operand to sum up both strings, specifying also the space, generates the output seen in the code.

7. Indexing
Individual characters of a string can be accessed directly using an index; the position of that character within the string. 
Let's work with the following example. 
To get the fourth character of the string, we specify the string name followed by the position inside square brackets. 
In python, string indexing is zero-based meaning that the first character has index zero as shown on the slide. 
For character four, we specify index three getting the following output. We can also indicate indices with negative numbers. 
If we specify index minus one, we get the last character of the string as shown in the output.

8. Slicing
With the bracket notation, python allows you to access a specific part or sequence of characters within the original string. 
For that aim, we specify the starting and ending positions inside square brackets separated by a colon as you see on the slide. 
The ending position is excluded in the resulting output. 
Omitting the first or second index results in the slice starting at the beginning or going until the end of the string as shown in the output.

9. Stride
String slicing also accepts a third index which specifies how many characters to omit before retrieving a character. 
In the example, the specified indices returns the following output. 
They are the characters retrieved between positions zero and six, skipping two characters in between. 
Interestingly, omitting the first and second indices and designating a minus one step returns a reversed string as shown in the output.

1.2. First day!
Your first project is to build a model for predicting if a movie will get a positive or negative review.
You need to start exploring your dataset. 
In order to create a function that will scan each movie review, 
you want to know how many characters every string has and print the result out together with a statement that indicate what the number refers to. 
To test if your function works correctly, you are going to start by analyzing only one example.

The text of one movie review has been already saved in the variable movie. 
You can use print(movie) to view the variable in the IPython Shell.

Instructions 1/3
Find out how many characters the variable movie has.

Hint
For example, if you want to find out how many characters var has, you can try using len(var).

Code:
# Find characters in movie variable
length_string = len(movie)

Instructions 2/3
Convert the numeric variable length_string to a string representation.

Hint
In python, any object object can be rendered as string using str(object).

Code:
# Find characters in movie variable
length_string = len(movie)

# Convert to string
to_string = str(length_string)

Instructions 3/3
Concatenate the predefined variable statement and the variable to_string adding a space between them. Print out the result.

Hint
To print out the concatenation of the string1 and string2, print(string1+string2) can be used. 
Don't forget to add a space (" ") between both strings.

Code:
# Find characters in movie variable
length_string = len(movie)

# Convert to string
to_string = str(length_string)

# Predefined variable
statement = "Number of characters in this review:"

# Concatenate strings and print result
print(statement+" "+to_string)

Knowing how to manipulate strings will help you perform many data science tasks faster and easier.


1.3. Artificial reviews
While checking out the movie reviews in your dataset, you realize that some of them show an atypical pattern. 
Since you should only include true reviews in your analysis, you decide to extract the suspicious ones that follow this pattern. 
You want to see if it is possible to artificially create reviews by using the first 
and last part of one example review and changing a keyword in the middle.

The text of two movie reviews has been already saved in the variables movie1 and movie2. 
You can use the print() function to view the variables in the IPython Shell.

Remember: The 1st character of a string has index 0.

Instructions 1/4
Select the first 32 characters of the variable movie1 and assign it to the variable first_part.

Hint
To select the first n characters of a variable, use variable[:n]. Second index is not included in the resultant substring.

Code:
# Select the first 32 characters of movie1
first_part = movie1[:32]

Instructions 2/4
Select the substring going from the 43rd character to the end of movie1. Assign it to the variable last_part.

Hint
To select a substring from the nth character to the end of a variable, use variable[n-1:]. Indices in python are 0-based.

Code:
# Select the first 32 characters of movie1
first_part = movie1[:32]

# Select from 43rd character to the end of movie1
last_part = movie1[42:]

Instructions 3/4
Select the substring going from the 33rd to the 42nd character of movie2. Assign it to the variable middle_part.

Hint
To select a substring going from the mth to the nth character of a variable, use variable[m-1:n].

Code:
# Select the first 32 characters of movie1
first_part = movie1[:32]

# Select from 43rd character to the end of movie1
last_part = movie1[42:]

# Select from 33rd to the 42nd character of movie2
middle_part = movie2[32:42]

Instructions 4/4
Print the concatenation of the variables first_part, middle_part and last_part in that order. Print the variable movie2 and compare them.

Hint
To concatenate the string1, string2 and string3, use the plus operator: string1+string2+string3.

Code:
# Select the first 32 characters of movie1
first_part = movie1[:32]

# Select from 43rd character to the end of movie1
last_part = movie1[42:]

# Select from 33rd to the 42nd character
middle_part = movie2[32:42]

# Print concatenation and movie2 variable
print(first_part+middle_part+last_part) 
print(movie2)

Remember that indexing in python is 0-based and that the first index specified is included while the second index is excluded!


1.4. Palindromes
Next, you are committed to find any peculiarity in the words included in the movie review dataset. 
A palindrome is a sequence of characters which can be read the same backward as forward, 
for example: Madam or No lemon, no melon. You realize that there are some funny movie names that can have this characteristic. 
You want to make a list of all movie titles that are funny palindromes but you will start by analyzing one example.

In python, you can also specify steps by using a third index. 
If you don't specify the first or second index and the third one is negative, it will return the characters jumping and backwards.

The text of a movie review for one example has been already saved in the variable movie. 
You can use print(movie) to view the variable in the IPython Shell.

Instructions
-Extract the substring from the 12th to the 30th character from the variable movie which corresponds to the movie title. 
Store it in the variable movie_title.
-Get the palindrome by reversing the string contained in movie_title.
-Complete the code to print out the movie_title if it is a palindrome.

Hint
To select a substring going from the mth to the nth character of a variable, use variable[m-1:n].
Remember that if you use -1 as a third index and you don't specify the first two you can get your string backwards.
Use print() and the variable movie_title.

Code:
# Get the word
movie_title = movie[11:30]

# Obtain the palindrome
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)
  
Reversing a string as a result of omiting the first and second indices and designate a minus one step is a very common strategy.

1.5. String operations
1. String operations
In this video, we'll learn more about string manipulation, specifically, about basic string operations.

2. Adjusting cases
Most data science projects involve string manipulation. Python has many built-in methods that allow us to handle strings. 
Let's check some of them. Suppose we have a string like the one in the example code. 
Sometimes, the analysis requires the string to be entirely lowercase. 
We could use the dot lower method to convert all alphabetic characters to lowercase as shown in the output. 
On the contrary, we might want the string to be uppercase. 
We could use the dot upper method to convert all alphabetic characters to uppercase as displayed.

3. Adjusting cases2
Lastly, we could use dot capitalize to return a copy of the string with the first character in uppercase while keeping all other characters in lowercase as displayed.

4. Splitting
There are methods that can convert between a string and other types of data, such as lists by breaking a string into pieces. 
Let's work with the following example. We want to split the string into a list of substrings. 
Python provides us with two methods: dot split and dot rsplit. Both of them return a list.
They both take a separating element by which we are splitting the string, and a maxsplit that tells us the maximum number of substrings we want. 
As we can see in the code, the difference is that split starts splitting at the left. rsplit begins at the right of the string. 
If maxsplit is not specified both methods behave in the same way. They give as many substrings as possible. 
If you want the split to be done by the whitespace you don't have to specify the sep argument.

5. Splitting
Consider the following string. If we print it out, we can see that contains two lines. 
Why is that? There are some escape sequences such as slash n or slash r that indicates a line boundary. Sometimes, we want to split a string into lines. 
So in the case of our string, we want to split it at the slash n.

6. splitlines
For this aim, Python has the method splitlines(). 
As we can see in the code, the string is split at the slash n sequence returning a list of two elements.

7. Joining
Some methods can paste or concatenate together the objects in a list or other iterable data. 
This is the case for dot join method. The syntax is simple. It first takes the separating element. 
Inside the call, we specify the list or iterable element. 
We can observe in the example, that whitespace is specified as a separator and the data type is a list. 
The result is a single string containing all the objects in the list separated by whitespace.

8. Stripping characters
Lastly, we'll talk about methods that will trim characters from a string. 
The dot strip method will remove both leading and trailing characters. Inside the call, we can specifying a character. 
If we don't do it, whitespace will be removed. Let's say we have the following string. And we apply the dot strip method as shown. 
We get a string where both the leading space and the trailing escape sequence were removed.

9. Stripping characters2
We can apply dot rstrip method and it will return a string where the trailing slash n was removed. 
If we apply the dot lstrip method, we'll get a string with the leading whitespace eliminated.


1.6. Normalizing reviews
It's time to extract some important words present in your movie review dataset. 
First, you need to normalize them and then, count their frequency. 
Part of the normalization implies converting all the words to lowercase, 
removing special characters and extracting the root of a word so you count the variants as one.

So imagine you have the following reviews: The movie surprises me very much and Marvel movies always surprise their audience. 
If you count the word frequency, you will count surprises one time and surprise one time. 
However, the verb surprise appears in both and its frequency should be two.

The text of a movie review for only one example has been already saved in the variable movie. 
You can use print(movie) to view the variable in the IPython Shell.

Instructions 1/4
Convert the string in the variable movie to lowercase. Print the result.

Hint
To convert to lowercase a string, use string.lower().

Code:
# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)


Instructions 2/4
Remove the $ that occur at the start and at the end of the string contained in movie_lower. Print the results.

Hint
To remove a char of a string from the beginning and the end, use string.strip(char).

Code:
# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove specified character and print the result
movie_no_sign = movie_lower.strip("$")
print(movie_no_sign)

Instructions 3/4
Split the string contained in movie_no_sign into as many substrings as possible. Print the results.

Hint
To split a string, use string.split().

Code:
# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove specified character and print the result
movie_no_sign = movie_lower.strip("$")
print(movie_no_sign)

# Split the string into substrings and print the result
movie_split = movie_no_sign.split()
print(movie_split)

Instructions 4/4
To get the root of the second word contained in movie_split, select all the characters except the last one.

Hint
To select all the character of word except the last one, use word[:-1].

Code:
# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove specified character and print the result
movie_no_sign = movie_lower.strip("$")
print(movie_no_sign)

# Split the string into substrings and print the result
movie_split = movie_no_sign.split()
print(movie_split)

# Select root word and print the result
word_root = movie_split[1][:-1]
print(word_root)

Normalizing strings is a fundamental part of text mining. 
Remember that if you don't specify any arguments in strip() and split(), it will always remove or split whitespaces

1.7. Time to join!
While normalizing your text, you noticed that one review had a particular structure. 
This review ends with the HTML tag <\i> and it has a lot of commas in different places of the sentence. 
You decide to remove the tag from the end and use the strategy of splitting the string and joining it back again without the commas.

The text of a movie review has been already saved in the variable movie. You can use print(movie) to view the variable in the IPython Shell.

Instructions 1/3
Remove tag <\i> from the end of the string. Print the results.

Hint
To remove a char from the end of a string, use string.rstrip(char).

Code:
# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

Instructions 2/3
Split the string contained in movie_tag using the commas as a separating element. Print the results.

Hint
To split a string using a char as a separating element, use string.split(char).

Code:
# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

Instructions 3/3
Join back together the list of substring contained in movie_no_comma using a space as a join element. Print the results.

Hint
To join a list of substring using a char as join elements, use "char".join(list).

Code:
# Remove tags happening at the end and print results
movie_tag = movie.rstrip("<\i>")
print(movie_tag)

# Split the string using commas and print results
movie_no_comma = movie_tag.split(",")
print(movie_no_comma)

# Join back together and print results
movie_join = " ".join(movie_no_comma)
print(movie_join)

Remember that if you specify an argument in strip() and split(), it will use that character to remove or split.

1.8. Split lines or split the line?
You are about to leave work when a colleague asks you to use your string manipulation skills to help him. 
You need to read strings from a file in a way that if the file contains strings on different lines, they are stored as separate elements. 
He also wants you to break the strings into pieces if you see that they contain commas.

The text of the file has been already saved in the variable file. You can use print(file) to view the variable in the IPython Shell.

Instructions
Split the string file into many substrings at line boundaries.
Print out the resulting variable file_split.
Complete the for-loop to split the strings into many substrings using commas as a separator element.

Hint
To split a string at line boundaries, use string.splitlines().
To print out a variable, use print(variable).
To split a string using a char as separator element, use string.split(char).

Code:
# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(",")
    print(substring_split)
    

1.9. Finding and replacing
The difference between split() and splitlines is that splitlines() breaks a string by line boundaries 
while split() uses the separating element to break a string into pieces.

1. Finding and replacing
Finally, we'll talk about different methods that allow us to search or replace substrings.

2. Finding substrings
Python has several built-in methods that will help you search a target string for a specified substring. 
The first method is dot find. As you can see in the slide, it takes the desired substring as a mandatory argument. 
You can specify two other arguments. An inclusive starting position and an exclusive ending position. 
In the example code, we search for Waldo in the string Where's Waldo?. 
The dot find method returns the lowest index in the string where it can find the substring, in this case, eight. 
If we search for Wenda, the substring is not found and the method returns minus one.

3. Finding substrings
Now, we check if we can find Waldo between characters number zero and five. 
In the code, we specify the starting position, zero, and the ending position, six, because this position is not inclusive. 
The dot find method will not find the substring and returns minus one as we see in the output.

4. Index function
The dot index method is identical to dot find. In the slide, we see that it takes the desired substring as mandatory argument. 
It can take optional starting and ending positions as well. In the example, we search again for Waldo using dot index. 
We get eight again. When we look for a substring that is not there, we have a difference. 
The dot index method raises an exception, as we can see in the output.

5. Index function
We can handle this using the try except block. In the slide, you can observe the syntax. The try part will test the given code. 
If any error appears the except part will be executed obtaining the following output as a result.

6. Counting occurrences
The dot count method searches for a specified substring in the target string. It returns the number of non-overlapping occurrences. 
In simple words, how many times the substring is present in the string. 
The syntax of dot count is very similar to the other methods as we can observe. 
In the example, we use the dot count method to get how many times fruit appears. In the output, we see that is two. 
Then, we limit the occurrences of fruit between character zero and fifteen of the string as we can observe in the code. 
The method will return 1. Remember that starting position is inclusive, but the ending is not.

7. Replacing substrings
Sometimes you will want to replace occurrences of a substring with a new substring. 
In this case, Python provides us with the dot replace method. 
As we see in the slide, it takes three arguments: 
the substring to replace, the new string to replace it, and an optional number that indicates how many occurrences to replace. 
In the example code, we replace the substring house with car. The method will return a copy with all house substrings replaced. 
In the next example, we specified that we only want 2 of the occurrences to be replaced. 
We see in the output that the method return a copy of the string with the first two occurrences of house replaced by car.

8. Wrapping up
In this chapter, we walked through learning how to manipulate strings, a valuable skill for any data science project. 
You saw how to slide, concatenate and adjust cases of strings, how to split them into pieces and join them back together, 
how to remove characters and finally how to find, count and replace occurrences of substrings.

1.10. Finding a substring
It's a new day at work and you need to continue cleaning your dataset for the movie prediction project. 
While exploring the dataset, you notice a strange pattern: 
there are some repeated, consecutive words occurring between the character at position 37 and the character at position 41. 
You decide to write a function to find out which movie reviews show this peculiarity, 
remembering that the ending position you specify is not inclusive. 
If you detect the word, you also want to change the string by replacing it with only one instance of the word.

Complete the if-else statement following the instructions.

The text of three movie reviews has been already saved in the variable movies. 
You can use print(movies) to view the variable in the IPython Shell.

Instructions
Find if the substring actor occurs between the characters with index 37 and 41 inclusive. If it is not detected, print the statement Word not found.
Replace actor actor with the substring actor if actor occurs only two repeated times.
Replace actor actor actor with the substring actor if actor appears three repeated times.

Hint
Find if a pattern occurs between the characters 1 and 4 (inclusive) of string using string.find(pattern, 1, 5). If not found, .find() will return -1.
Count the occurrences of pattern in string using string.count(pattern).
Replace old with new in string using string.replace(old, new).

Code:
for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))
        
Remember that start and end argument are optional in .find() and .count() methods. 
When specified, the method interprets them for slicing the string.

1.11. Where's the word?
Before finishing cleaning your dataset, you want to check if a specific word occurs in the reviews.
You noticed earlier a specific pattern in the strings. 
Now, you want to create a function to check if a word is present between characters with index 12, and 50, 
remembering that ending position is exclusive, and print out the lowest index where this word occurs. 
There are two methods to handle this situation. You want to see which one works best.

The text of two movie reviews has been already saved in the variable movies. 
You can use print(movies) to view the variable in the IPython Shell.

Instructions 1/2
Find the index where money occurs between characters with index 12 and 50. If not found, the method should return -1.

Hint
To find the first occurrence of pattern in string between characters with index 1 and 5 and return -1 if not found, use string.find(pattern, 1, 6). 
Remember that the ending position is exclusive.

Code:
for movie in movies:
  # Find the first occurrence of word
  print(movie.find("money", 12, 51))
  
Instructions 2/2
Find the index where money occurs between characters with index 12 and 50. If not found, it should raise an error.

Hint
To find the first occurrence of pattern in string between characters with index 1 and 5 and raise and error if not found, use string.index(pattern, 1, 6). 
Remember that the ending position is exclusive.

Code:
for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index("money", 12, 51))
  except ValueError:
    print("substring not found")

find() will return the value minus one if the substring is not found which, in most of cases, 
is better than handling the exceptions index() will raise because it improves performance.

1.12. Replacing negations
In order to keep working with your prediction project, your next task is to figure out how to handle negations that occur in your dataset. 
Some algorithms for prediction do not work well with negations, 
so a good way to handle this is to remove either not or n't, and to replace the next word by its antonym.

Let's imagine that you have the string: The movie isn't good. You will need to remove n't and replace good for bad. 
This way, your string ends up being The movie is bad. 
You notice that in the first column of the dataset, you have a string that uses the word isn't followed by important.

The text of this column has been already saved in the variable movies so you start working with it. 
You can use print(movies) to view it in the IPython Shell.

Instructions
Replace the substring isn't with the word is.
Replace the substring important with the word insignificant.
Print out the result contained in the variable movies_antonym.

Hint
-To replace a substr1 by other new_substr in a string use string.replace(substr, new_substr). 
Remember to use double quotes so that the single quotes in isn't does not interfere.
-To print new_string use print(new_string).

Code:
# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)

Consider that when you use .replace("word", "new") all occurences of the word will be replaced. 
You can specify a number of occurrences to replace by adding a third argument .replace("word", "new", count).




