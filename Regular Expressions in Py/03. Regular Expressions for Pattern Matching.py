3. Regular Expressions for Pattern Matching
Time to discover the fundamental concepts of regular expressions! 
In this key chapter, you will learn to understand the basic concepts of regular expression syntax. 
Using a real dataset with tweets meant for sentiment analysis, 
you will learn how to apply pattern matching using normal and special characters, and greedy and lazy quantifiers.

3.1. Introduction to regular expressions
2. What is a regular expression?
A regular expression, or regex, is a string that contains a combination of normal 
and special characters that describes patterns to find text within a text. This sounds very complicated. 
Let's break it down to understand it better. Here, we have an example of what a regular expression looks like. 
In Python, the r at the beginning indicates a raw string. It is always advisable to use it.

3. What is a regular expression?
We said that a regex contains normal characters, or literal characters we already know. 
The normal characters match themselves. In the case shown in our slide, st exactly matches an s followed by a t.

4. What is a regular expression?
They also contain special characters. Metacharacters represent types of characters. 
Let's look one by one as they appear in the slide. Backslash d represents a digit.

5. What is a regular expression?
backslash s a whitespace,

6. What is a regular expression?
backslash w a word character.They also represent ideas, such as location or quantity.

7. What is a regular expression?
In the example, 3 and 10 inside curly braces indicates that the character immediately to the left, in this case backslash w, 
should appear between 3 and 10 times.

8. What is a regular expression?
We said that regex describes a pattern. A pattern is a sequence of characters that maps to words or punctuation.

9. What is a regular expression?
As a data scientist, you will use pattern matching to find and replace specific text. 
To validate strings such as passwords or email addresses. Why use regex? They are very powerful and fast. 
They allow you to search complex patterns that would be very difficult to find otherwise.

10. The re module
Python has a useful library, the re module, to handle regex. You can import it as shown in the code. 
Let's see how it works. To find all matches of a pattern, we use the dot findall method. 
It takes two arguments: the regex and the string. In the code, we want to find all the matches of hashtag movies in the specified string. 
  The method returns a list with the two matches found.

11. The re module
To split a string at each pattern match, we could use the method dot split 
In the example, we want to split the specified string at every exclamation mark match. 
It returns a list of the substrings as you can see in the output.

12. The re module
Finally, we could replace any pattern match with another string using the dot sub method. 
It takes three arguments: the regex, replacement and string. 
In the example, we replace every match of yellow with the word nice. We get the following output.

13. Supported metacharacters
Let's look at the supported metacharacters. In the example, we want to find all matches of the patterns containing User followed by a number. 
We use backlash d to represent the digit. We get the following matches. 
Next, we find matches of the pattern containing User followed by a non-digit. 
In that case, we use backslash capital D obtaining the following match.

14. Supported metacharacters
If we want to find all matches of the pattern containing User followed by any digit or normal character, we can use backlash w. 
We get all following matches. In the next example, we need to find the price in a string. 
We use backslash capital W to match the dollar sign followed by a digit obtaining the following output.

15. Supported metacharacters
Finally, we use backslash s to specify the pattern Data whitespace science getting the following match. 
In the second example, we use backslash capital S to detect the matches of ice, followed by any non-space character, 
followed by cream and replace them with the word ice cream.

3.2. Are they bots?
The company that you are working for asked you to perform a sentiment analysis using a dataset with tweets. 
First of all, you need to do some cleaning and extract some information.
While printing out some text, you realize that some tweets contain user mentions. 
Some of these mentions follow a very strange pattern. A few examples that you notice: @robot3!, @robot5& and @robot7#

To analyze if those users are bots, you will do a proof of concept with one tweet and extract them using the .findall() method.

You write down some helpful metacharacters to help you later:
\d: digit
\w: word character
\W: non-word character
\s: whitespace

The text of one tweet was saved in the variable sentiment_analysis. You can use print(sentiment_analysis) to view it in the IPython Shell.

Instructions
Import the re module.
Write a regex that matches the user mentions that starts with @ and follows the pattern, e.g. @robot3!.
Find all the matches of the pattern in the sentiment_analysis variable.

Hint
To import module, use import module.
Always start a regex with r. Remember that normal characters match themselves. 
Use \d to indicate digits and \W to indicate any non-word character, for example, & or #.
To find all matches of pattern in a string, use the method .findall() from the re module. 
Don't forget to specify the pattern and the string as arguments.

Code:
# Import the re module
import re

# Write the regex
regex = r"@robot\d\W"

# Find all matches of regex
print(re.findall(regex, sentiment_analysis))

The advantage of regular expressions is that you can use both normal characters and metacharacters. 
You can easily extract complex patterns, which would be more complicated otherwise.

3.3. Find the numbers
While examining the tweet text in your dataset, you detect that some tweets carry more information. 
The text contains the number of retweets, user mentions, and likes. 
You decide to extract this important information that is given as in this example:

Agh,snow! User_mentions:9, likes: 5, number of retweets: 4

You pull a list of metacharacters:\d digit,\w word character,\s whitespace.
Always indicate whitespace with metacharacters.
The variable sentiment_analysis containing the text of one tweet and the re module were loaded in your session. You can use print() to view it in the IPython Shell.

Instructions 1/3
Write a regex that matches the number of user mentions given as, for example, User_mentions:9 in sentiment_analysis.

Hint
Always start a regex with r. Remember that normal characters match themselves. 
Use \d to indicate digits and \s for spaces. Use the .findall() method of the re module.

Code:
# Write a regex to obtain user mentions
print(re.findall(r"User_mentions:\d", sentiment_analysis))


Instructions 2/3
Write a regex that matches the number of likes given as, for example, likes: 5 in sentiment_analysis.

Hint
Always start a regex with r. Remember that normal characters match themselves. 
Use \d to indicate digits and \s to indicate whitespace. Use the .findall() method of the re module.

Code:
# Write a regex to obtain number of likes
print(re.findall(r"likes:\s\d", sentiment_analysis))


Instructions 3/3
Write a regex that matches the number of retweets given as, for example, number of retweets: 4 in sentiment_analysis.

Hint
Always start a regex with r. Remember that normal characters match themselves. 
Use \d to indicate digits and \s to indicate whitespace. Use the .findall() method of the re module.

Code:
# Write a regex to obtain number of retweets
print(re.findall(r"number\sof\sretweets:\s\d", sentiment_analysis))


Using metacharacters in regular expressions will allow you to match types of characters such as digits. 
You can encounter many forms of whitespace such as tabs, space or new line. 
To make sure you match all of them always specify whitespaces as \s.


3.4. Match and split
Some of the tweets in your dataset were downloaded incorrectly. Instead of having spaces to separate words, they have strange characters. 
You decide to use regular expressions to handle this situation. You print some of these tweets to understand which pattern you need to match.

You notice that the sentences are always separated by a special character, followed by a number, the word break, 
and after that, another special character, e.g &4break!. 
The words are always separated by a special character, the word new, and a normal random character, e.g #newH.

The variable sentiment_analysis containing the text of one tweet, as well as the re module were already loaded in your session. 
You can use print(sentiment_analysis) to view it in the IPython Shell.

Instructions 1/4
Write a regex that matches the pattern separating the sentences in sentiment_analysis, e.g. &4break!.

Hint
Start a regex with r. Use \W to match special characters and \d to match digits. Don't forget that normal characters match themselves.

Code:
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"


Instructions 2/4
Replace regex_sentence with a space " " in the variable sentiment_analysis. Assign it to sentiment_sub.

Hint
To replace a regex in a string, use the method .sub of the re module.
Don't forget to specify regex, the new characters and the string inside the method.

Code:
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)


Instructions 3/4
Write a regex that matches the pattern separating the words in sentiment_analysis, e.g. #newH.

Hint
Start a regex with r. Use \W to match special characters and \w to match any word character. 
Don't forget that normal characters match themselves.

Code:
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

Instructions 4/4
Replace regex_words with a space in the variable sentiment_sub. Assign it to sentiment_final and print out the result.

Hint
To replace a regex in a string, use the method .sub of the re module. 
Don't forget to specify regex, the new characters and the string inside the method.

Code:
# Write a regex to match pattern separating sentences
regex_sentence = r"\W\dbreak\W"

# Replace the regex_sentence with a space
sentiment_sub = re.sub(regex_sentence, " ", sentiment_analysis)

# Write a regex to match pattern separating words
regex_words = r"\Wnew\w"

# Replace the regex_words and print the result
sentiment_final = re.sub(regex_words, " ", sentiment_sub)
print(sentiment_final)


Regular expressions are very useful for finding and replacing complex patterns in text. Using them will make your analysis cleaner and faster.


3.5. Repetitions
1. Repetitions
In this video, we are going to talk about how to match repeated characters.

2. Repeated characters
Let's imagine that we are given the task to validate a password.

3. Repeated characters
It should contain eight characters

4. Repeated characters
followed by four numbers.

5. Repeated characters
To search for a pattern, we can use the method dot search. It takes the regex and string. It tells us if there is a match. 
Let's apply what we have learned until now. 
We use backslash w eight times to match the first part and backslash d four times to match the last part. So our method finds a match.

6. Repeated characters
But this seems cumbersome for longer regex. Instead, we can use quantifiers to save this situation. 
A quantifier is a metacharacter that specifies how many times a character located to its left needs to be matched. 
In our example, we specify that backslash w is repeated 8 times and backslash d four times. And we get a match as seen in the output.

7. Quantifiers
In the following string, we want to match the dates. 
We can see that the pattern is one or multiple digits, dash, and again one or multiple digits. 
The plus metacharacter indicates a character that appears once or more times. 
Let's construct the regex from simple to complex. We will use dot findall method as you can see in the code.

8. Quantifiers
We indicate that the digit, backslash d, should appear once or more times adding the plus quantifier. Then, a dash.

9. Quantifiers
And again a digit, backslash d. It should appear once or more times, so again we use the plus quantifier. 
We get the two matches that we expected as seen in the output.

10. Quantifiers
To indicate that a character should appear zero or more times, we can use the star metacharacter. 
In this example, we have the following string. We want to find all mentions of users, which start with an at. 
We notice that they could contain or not contain a non-word character in the middle. 
So, we construct our regex as seen in the code: an at, followed by backslash w plus, 
backslash capital w with start to indicate a non-word character zero or more times, then backslash w plus. 
And we get the matches seen in the output.

11. Quantifiers
Another helpful quantifier is the question mark. It indicates that a character should appear zero times or once. 
In the example, we need to find matches for the word color, which has spelling variations. 
So, our regex is c, o, l, o, u which can appear once or zero times, so we add the question mark after it, then r. 
With this regex, we get the two matches wanted.

12. Quantifiers
Finally, we can use the curly braces to indicate a specific minimum and maximum times. 
In the example, we want to find all matches for a phone number. We'll use the dot findall method and construct our regex step by step.

13. Quantifiers
As we can see, we can have a digit, once or twice, then slash.

14. Quantifiers
Then, again a digit, three times. Then, a slash.

15. Quantifiers
Then, a digit twice or three times. Then, slash. And finally a digit again. 
We indicate that this last digit need to appear at least four times leaving the second argument in black. 
The regex engine returns two matches as expected.

16. Quantifiers
It's very important to remember that the quantifier applies only to the character immediately to the left. 
As an example, in the regex apple plus, the plus applies only to the letter e and not to the entire word.


3.6. Everything clean
Back to your Twitter sentiment analysis project! There are several types of strings that increase your sentiment analysis complexity.
But these strings do not provide any useful sentiment. Among them, we can have links and user mentions.

In order to clean the tweets, you want to extract some examples first.
You know that most of the times links start with http and do not contain any whitespace, e.g. https://www.datacamp.com. 
User mentions start with @ and can have letters and numbers only, e.g. @johnsmith3.

You write down some helpful quantifiers to help you: * zero or more times, + once or more, ? zero or once.

The list sentiment_analysis containing the text of three tweet are already loaded in your session. 
You can use print() to view the data in the IPython Shell.

Instructions
Import the re module.
Write a regex to find all the matches of http links appearing in each tweet in sentiment_analysis. Print out the result.
Write a regex to find all the matches of user mentions appearing in each tweet in sentiment_analysis. Print out the result.

Hint
To import module, use import module.
To match a pattern that starts with sequence and has no whitespace, use sequence and \S+. To find all matches, use the method .findall().
To match a pattern that starts with @ symbol and can contain letters and numbers, use @ and \w+. To find all matches, use the method .findall().

Code:
# Import re module
import re

for tweet in sentiment_analysis:
  	# Write regex to match http links and print out result
	print(re.findall(r"http\S+", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+", tweet))
  
Regular expressions provide very useful metacharacters that you should not forget to use. \S is an example. 
It is very useful to use when you know a pattern doesn't contain spaces and you have reached the end when you do find one.

3.7. Some time ago
You are interested in knowing when the tweets were posted. 
After reading a little bit more, you learn that dates are provided in different ways. 
You decide to extract the dates using .findall() so you can normalize them afterwards to make them all look the same.

You realize that the dates are always presented in one of the following ways:

27 minutes ago
4 hours ago
23rd june 2018
1st september 2019 17:25

The list sentiment_analysis containing the text of three tweets, as well as the re module are already loaded in your session. 
You can use print() to view the data in the IPython Shell.

Instructions 1/3
Complete the for-loop with a regex that finds all dates in a format similar to 27 minutes ago or 4 hours ago.

Hint
To match a number that appears once or twice, use \d{1,2}. Remember that \s indicates whitespace present in the pattern. 
You can use \w for normal characters together with + to specify that it can be repeated once or more times. 
Pay attention that both formats end in ago and normal characters match themselves. To find all matches use .findall().

Code:
# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\s\w+\sago", date))
  

Instructions 2/3
Complete the for-loop with a regex that finds all dates in a format similar to 23rd june 2018.

Hint
To match a number that appears once or twice, use \d{1,2}. Remember that \s indicates whitespace present in the pattern. 
You can use \w for normal characters together with + to specify that it can be repeated once or more times. 
If a date ends with the year you can use the {n} quantifier to specify that the number is repeated exactly n times. 
To find all matches use .findall().

Code:
# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}", date))
  

Instructions 3/3
Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25.

Hint
To specify the time, you can use \d together with the {n,m} quantifier to indicate a minimum n and a maximum m numbers of times. 
The : is there to match the : appearing between numbers. Remember that \s indicates whitespace present in the pattern. 
To find all matches use .findall().

Code:
# Complete the for loop with a regex to find dates
for date in sentiment_analysis:
	print(re.findall(r"\d{1,2}\w+\s\w+\s\d{4}\s\d{1,2}:\d{2}", date))
  
Handling dates can become a really difficult task. Fortunately, regular expressions can simplify this task!

3.8. Getting tokens
Your next step is to tokenize the text of your tweets. 
Tokenization is the process of breaking a string into lexical units or, in simpler terms, words. 
But first, you need to remove hashtags so they do not cloud your process. 
You realize that hashtags start with a # symbol and contain letters and numbers but never whitespace. 
After that, you plan to split the text at whitespace matches to get the tokens.

You bring your list of quantifiers to help you: * zero or more times, + once or more, ? zero or once, {n, m} minimum n, maximum m.

The variable sentiment_analysis containing the text of one tweet as well as the re module are already loaded in your session. 
You can use print(sentiment_analysis) to view it in the IPython Shell.

Instructions 1/3
Write a regex that matches the described hashtag pattern. Assign it to the regex variable.

Hint
To match a letter or a number, use \w. If you want these character to be repeated once or multiple times, you can use +. 
The hashtag symbol will match itself.

Code:
# Write a regex matching the hashtag pattern
regex = r"#\w+"

Instructions 2/3
Replace all the matches of the regex with an empty string "". Assign it to no_hashtag variable.

Hint
To replace a regex with a new sequence, use .sub(). 
Remember to specify the regex, the new sequence of characters, and the string inside the method.

Code:
# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)


Instructions 3/3
Split the text in the no_hashtag variable at every match of one or more consecutive whitespace.

Hint
To split a text at every pattern match, use .split(). 
To specify you want to split the text at one or more consecutive whitespace (\s), use the + quantifier.

Code:
# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace the regex by an empty string
no_hashtag = re.sub(regex, "", sentiment_analysis)

# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))

Regular expressions can be very useful when replacing and splitting string using complex patterns.

3.9. Regex metacharacters
1. Regex metacharacters
Now, we will look at some other metacharacters that are very useful.

2. Looking for patterns
Let's first look at two methods of the re module: dot search and dot match. 
As you can see, they have the same syntax and are used to find a match. 
In the example, we use both methods to find a digit appearing four times. 
Both methods return an object with the match found. The difference is that dot match is anchored at the beginning of the string. 
In the second example, we used them to find a match for a digit. In this case, dot search finds a match, but dot match does not. 
This is because the first characters do not match the regex.

3. Special characters
The dot metacharacter matches any character. In the example code, we need to match links in the string. 
We know a link starts with w, w, w and ends with c, o, m. So we first write this in our regex.

4. Special characters
We don't know how many character are in between. So we indicate that we want any character, a dot, once or more times, adding the plus. 
We can see in the output that we get our match.

5. Special characters
The circumflex anchors the regex to the start of a string. 
In the example, we find the pattern starting with t, followed by h, e, whitespace, two digits and ending with s. 
The method finds the following two matches. Now, we add the anchor metacharacter. We receive only one match. 
The one that appears at the beginning of the string.

6. Special characters
On the contrary, the dollar sign anchors the regex to the end of the string. 
If we use it in the previous example, we get the match that appears at the end of the string.

7. Special characters
What if I want to use characters like dollar sign or dot, which also have other meanings? 
Let's look at an example. We want to split the string by dot whitespace. We write the following regex. 
And we get an output that it is not what we expected. Why? Because the regex interprets the dot as any character. 
To solve this situation, we need to escape the character by adding a backslash in front of the dot. Now we get the correct output.

8. OR operator
In the example code, we want to match the word elephant. However, we see that it's written with capital E or lower e. 
In that case, we use the vertical bar. In this way, we indicate that we want to match one variant OR the other obtaining both elephant-matches.

9. OR operator
Square brackets also represent the OR operand. Inside them, we can specify optional characters to match. Look at the example. 
We want to find a pattern that contains lowercase or uppercase letter followed by a digit. To do so, we can use the square brackets. 
Inside them, we will use lowercase a dash lowercase z to specify any lowercase letter. 
Then, uppercase a dash uppercase z to indicate any uppercase letter. Then the plus. Then backslash d. Thus, we get the following matches.

10. OR operator
In the following string, we want to replace the non-word characters by whitespace. 
We specify optional characters inside the square brackets. The engine searches for one or the other. 
When it finds a match, it replaces the character by a whitespace, getting the following output.

11. OR operand
The circumflex transforms the expression inside square brackets into negative. 
In the example, we add the circumflex to specify we want the links that do not contain any number. And we get the following output.


3.10. Finding files
You are not satisfied with your tweets dataset cleaning. There are still extra strings that do not provide any sentiment. 
Among them are strings that refer to text file names.

You also find a way to detect them:
-They appear at the start of the string.
-They always start with a sequence of 2 or 3 upper or lowercase vowels (a e i o u).
-They always finish with the txt ending.
You are not sure if you should remove them directly. So you write a script to find and store them in a separate dataset.

You write down some metacharacters to help you: ^ anchor to beginning, . any character.

The variable sentiment_analysis containing the text of two tweets as well as the re module are already loaded in your session. 
You can use print() to view it in the IPython Shell.

Instructions
Write a regex that matches the pattern of the text file names, e.g. aemyfile.txt.
Find all matches of the regex in the elements of sentiment_analysis. Print out the result.
Replace all matches of the regex with an empty string "". Print out the result.

Hint
-Use [] to indicate optional characters such as [aeiou]. The dot . metacharacter matches any character. 
The txt ending can match itself. Use ^ to anchor it to the beginning of the string.
-Use .findall() to find all matches of a regex. Specify regex and string.
-Use .sub() to replace all matches of a regex. Specify the regex, new sequence, and string.

Code:
# Write a regex to match text file name
regex = r"^[aeiouAEIOU]{2,3}.+txt"

for text in sentiment_analysis:
	# Find all matches of the regex
	print(re.findall(regex, text))
    
	# Replace all matches with empty string
	print(re.sub(regex, "", text))
  
The dot . metacharacter is very useful when we want to match all repetitions of any character. However, we need to be very careful how we use it.


3.11. Give me your email
A colleague has asked for your help! When a user signs up on the company website, they must provide a valid email address.
The company puts some rules in place to verify that the given email address is valid:
-The first part can contain:
  Upper A-Z and lowercase letters a-z
  Numbers
  Characters: !, #, %, &, *, $, .
-Must have @
-Domain:
  Can contain any word characters
  But only .com ending is allowed
  
The project consist of writing a script that checks if the email address follow the correct pattern. 
Your colleague gave you a list of email addresses as examples to test.

The list emails as well as the re module are loaded in your session. 
You can use print(emails) to view the emails in the IPython Shell.


Instructions
Write a regular expression to match valid email addresses as described.
Match the regex to the elements contained in emails.
To print out the message indicating if it is a valid email or not, complete .format() statement.

Hint
To choose between different characters use []. Use a-z for lowercase, A-Z for uppercase letters and 0-9 for numbers. 
    Don't forget to escape . and $ as they have another meaning. Use \w for any word character.
To match a pattern to a string, use .match(pattern, string).
Remember the .format() syntax: "text {variable}".format(variable=string).

Code:
# Write a regex to match a valid email address
regex = r"[A-Za-z0-9!#%&*\$\.]+@\w+\.com"

for example in emails:
  	# Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example))   
        
Validating strings is a task that becomes simpler when we use regular expressions. Square brackets are very useful for optional characters. 
Notice that we used the .match() method. The reason is that we want to match the pattern from the beginning of the string.


3.12. Invalid password
The second part of the website project is to write a script that validates the password entered by the user. The company also puts some rules in order to verify valid passwords:
-It can contain lowercase a-z and uppercase letters A-Z
-It can contain numbers
-It can contain the symbols: *, #, $, %, !, &, .
-It must be at least 8 characters long but not more than 20

Your colleague also gave you a list of passwords as examples to test.

The list passwords and the module re are loaded in your session. You can use print(passwords) to view them in the IPython Shell.

Instructions
Write a regular expression to match valid passwords as described.
Scan the elements in the passwords list to find out if they are valid passwords.
To print out the message indicating if it is a valid password or not, complete .format() statement.

Hint
To choose between different characters use []. Use a-z for lowercase,A-Z for uppercase letters and 0-9 for numbers. 
    Don't forget to escape . and $. Use the {n, m} quantifier to specify minimum n and maximum m repetitions.
To scan the string, use .search() method.
Remember the .format() syntax: "text {variable}".format(variable=string).

Code:
# Write a regex to match a valid password
regex = r"[A-Za-z0-9!#%&*\$\.]{8,20}" 

for example in passwords:
  	# Scan the strings to find a match
    if re.search(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example))     
        
Notice that we used the .search() method. The reason is that we want to scan the string to match the pattern. 
We are not interested in where the regex finds the match.


3.13. Greedy vs. non-greedy matching
1. Greedy vs. non-greedy matching
You have already worked with repetitions. In this video, we'll deepen our understanding of how the quantifiers work.

2. Greedy vs. non-greedy matching
There are two types of matching methods: greedy and non-greedy (also called lazy) operators. 
The quantifiers that you have been learning until now (which are called standard quantifiers) are greedy by default.

3. Greedy matching
We said that the standard quantifiers have a greedy behavior, meaning that they will attempt to match as many characters as possible. 
And in doing so, they will return the longest match found with a match attempt. Let's take a look at this code. 
We want to find a pattern that has one or more digits on the string displayed and our greedy quantifier will return the pattern '12345'. 
We can explain this in the following way: our quantifier will start by matching the first digit found, '1'. 
Because it is greedy, it will keep going to find 'more' digits and stop only when no other digit can be matched, returning '12345'.

4. Greedy matching
However, there is another characteristic that we should explore. 
If the greedy quantifier has matched so many characters that can not match the rest of pattern, 
it will backtrack, giving up characters matched earlier one at a time and try again. 
Backtracking is like driving a car without a map. 
If you drive through a path and hit a dead end street, you need to backtrack along your road to an earlier point to take another street. 
To make this more clear, we'll take this example code. 
We use the greedy quantifier .* to find anything, zero or more times, followed by the letters "h" "e" "l" "l" "o". 
We can see here that it returns the pattern 'xhello'. So our greedy quantifier will start by matching as much as possible, the entire string. 
Then it tries to match the h, but there are no characters left. So it backtracks, giving up one matched character. Trying again. 
It still doesn't match the h, so it backtracks one more step repeatedly till it finally matches the h in the regex, and the rest of the characters.

5. Non-greedy matching
Because they have lazy behavior, non-greedy quantifiers will attempt to match as few characters as needed returning the shortest match. 
So how do we obtain non-greedy quantifiers? We can append a question mark at the end of the greedy quantifiers to convert them into lazy. 
If we take the same code as before, our non-greedy quantifier will return the pattern '1'. 
In this case, our quantifier will start by matching the first digit found, '1'. 
Because it is non-greedy, it will stop there as we stated that we want 'one or more' and one is as few as needed.

6. Non-greedy matching
Non-greedy quantifiers also backtrack. 
In this case, if they have matched so few characters that the rest of the pattern cannot match, they backtrack, expand the matched character one at a time and try again. 
Let's take the same example code again. This time we will use the lazy quantifier .*?. 
Interestingly, we obtain the same match 'xhello'. But how this match was obtained is different from the first time. 
The lazy quantifier first matches as little as possible, nothing, leaving the entire string unmatched. 
Then it tries to match the h, but it doesn't work. 
So it backtracks, matching one more character, the x. Then it tries again, this time matching the h, and afterwards, the rest of the regex.

3.14. Understanding the difference
You need to keep working and cleaning your tweets dataset. You realize that there are some HTML tags present. 
You need to remove them but keep the inside content as they are useful for analysis.

Let's take a look at this sentence containing an HTML tag: I want to see that <strong>amazing show</strong> again!

You know that to get the HTML tag you need to match anything that sits inside angle brackets < >. 
But the biggest problem is that the closing tag has the same structure. 
If you match too much, you will end up removing key information. So you need to decide whether to use a greedy or a lazy quantifier.
The string is already loaded as string to your session.

Instructions
Import the re module.
Write a regex expression to replace HTML tags with an empty string.
Print out the result.

Hint
Write a regex that looks for any character one or more times but uses a lazy quantifier by appending ?. 
Use it inside the function re.sub(regex,replacement, string).

Code:
# Import re
import re

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

# Print out the result
print(string_notags)

Remember that a greedy quantifier will try to match as much as possible while a non-greedy quantifier will do it as few times as needed, 
expanding one character at a time and giving us the match we are looking for. 

3.15. Greedy matching
Next, you see that numbers still appear in the text of the tweets. So, you decide to find all of them.

Let's imagine that you want to extract the number contained in the sentence I was born on April 24th. 
A lazy quantifier will make the regex return 2 and 4, because they will match as few characters as needed. 
However, a greedy quantifier will return the entire 24 due to its need to match as much as possible.

The re module as well as the variable sentiment_analysis are already loaded in your session. 
You can use print(sentiment_analysis) to view it in the IPython Shell.Next, you see that numbers still appear in the text of the tweets. 
So, you decide to find all of them.

Instructions 1/2
Use a lazy quantifier to match all numbers that appear in the variable sentiment_analysis.

Hint
In order to use a lazy quantifier, append ? to a regex that looks for numbers that occur one or more times. 
Don't forget to use .findall() method from the re module.

Code:
# Write a lazy regex expression 
numbers_found_lazy = re.findall(r"[0-9]+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

Instructions 2/2
Now, use a greedy quantifier to match all numbers that appear in the variable sentiment_analysis.

Hint
In order to use a greedy quantifier, write a regex that looks for numbers that appear once or multiple times. 
Don't forget to use .findall() method from the re module.

Code:
# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"[0-9]+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)

Even though greedy quantifiers lead to longer matches, they are sometimes the best option. 
Because lazy quantifiers match as few as possible, they return a shorter match than we expected. 
It is always good to know when to use greedy and lazy quantifiers!


3.16. Lazy approach
You have done some cleaning in your dataset but you are worried that there are sentences encased in parentheses that may cloud your analysis.

Again, a greedy or a lazy quantifier may lead to different results.

For example, if you want to extract a word starting with a and ending with e in the string I like apple pie, 
you may think that applying the greedy regex a.+e will return apple. 
However, your match will be apple pie. A way to overcome this is to make it lazy by using ? which will return apple.

The re module and the variable sentiment_analysis are already loaded in your session.

Instructions 1/2
Use a greedy quantifier to match text that appears within parentheses in the variable sentiment_analysis.

Hint
For a greedy approach, use the quantifier .*. Remember to use \ to escape the parentheses. Use .findall() method to find all matches.

Code:
# Write a greedy regex expression to match 
sentences_found_greedy = re.findall(r"\(.*\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)

Instructions 2/2
Now, use a lazy quantifier to match text that appears within parentheses in the variable sentiment_analysis.

Hint
For the lazy mode, append ? to the quantifier .*. Remember to use \ to escape the parenthesis. Use .findall() method to find all matches.

Code:
# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)

Notice that using greedy quantifiers always leads to longer matches that sometimes are not desired. 
Making quantifiers lazy by adding ? to match a shorter pattern is a very important consideration to keep in mind when handling data for text mining.


