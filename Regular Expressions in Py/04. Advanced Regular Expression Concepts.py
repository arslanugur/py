4. Advanced Regular Expression Concepts
"""You will learn more complex methods of pattern matching using parentheses to group strings together 
    or to match the same text as matched previously. Also, you will get an idea of how you can look around expressions."""

4.1. Capturing groups
1. Grouping and capturing
In the last stop of our journey, we are going to talk about some advanced concepts of regex. 
More specifically, in this video, we'll talk about capturing groups.

2. Group characters
Let's say that we have the following text.

3. Group characters
And we want to extract information about a person, how many and which type of relationships they have. 
So, we want to extract Clary 2 friends, Susan 3 brothers and John 4 sisters, as you can see in the slide. 
We know the structure of the sentences. Let's try our first approach. 
We would write something like in the code, 
any upper or lowercase letter, whitespace, any word character, whitespace, a number, whitespace and any word character. 
Let's see the output. Quite close. But we don't want the word has.

4. Capturing groups
What can we do about this? We start simple by trying to extract only the names. 
We can place parentheses to group those characters as shown in the slide. Capture them. And retrieve only that group.

5. Capturing groups
In the code, we have now added parentheses to group our first part of the regex. 
We can observe in the output that the group was captured. And only the three names were retrieved.

6. Capturing groups
Let's look at the example again. We can place parentheses around the three groups that we want to capture as shown in the slide. 
Each group will receive a number. The entire expression will always be group zero. 
The first group one, the second two, and the third number three. We'll see how to use these numbers later.

7. Capturing groups
Let's see this in the code example. We add the parentheses to group together each of the three parts of the regex. 
In the output, we got a list of tuples. The first element of each tuple is the match captured corresponding to group one. 
The second to group two. The last to group three.

8. Capturing groups
As we already discussed, we can use capturing groups to match a specific subpattern in a pattern. 
We can use this information for retrieving the groups by numbers as we'll learn later in the next videos.

9. Capturing groups
But we can also use it to organize data. As you saw earlier, the matches are retrieved as lists. 
In the code, we placed the parentheses to capture the name of the owner, the number and which type of pets each one has. 
We can access the information retrieved by using indexing and slicing as seen in the code. You've learned this in the first videos.

10. Capturing groups
But capturing groups have one important feature. Remember that quantifiers apply to the character immediately to the left. 
So, we can place parentheses to group characters and then apply the quantifier to the entire group. 
In the code, we have placed parentheses to match the group containing a number and any letter. 
We applied the plus quantifier to specify that we want this group repeated once or more times. 
And we get the following match shown in the output.

11. Capturing groups
But be careful. It's not the same to capture a repeated group than to repeat a capturing group. 
In the first code, we use findall to match a capturing group containing one number. 
We want this capturing group to be repeated once or more times. We get 5 and 3 as an output. 
Because these numbers are repeated consecutively once or more times. 
In the second code, we specify that we should capture a group containing one or more repetitions of a number. We now get the following output.


4.2. Try another name
You are still working on your Twitter sentiment analysis. You analyze now some things that caught your attention. 
You noticed that there are email addresses inserted in some tweets. Now, you are curious to find out which is the most common name.

You want to extract the first part of the email. E.g. if you have the email marysmith90@gmail.com, you are only interested in marysmith90.
You need to match the entire expression. So you make sure to extract only names present in emails. 
Also, you are only interested in names containing upper (e.g. A,B, Z) or lowercase letters (e.g. a, d, z) and numbers.

The list sentiment_analysis containing the text of three tweets as well as the re module were loaded in your session. 
You can use print() to view it in the IPython Shell.

Instructions
Complete the regex to match the email capturing only the name part. The name part appears before the @.
Find all matches of the regex in each element of sentiment_analysis analysis. Assign it to the variable email_matched.
Complete the .format() method to print the results captured in each element of sentiment_analysis analysis.

Hint
To capture a group, place parentheses to surround that group: (group)regex. 
  To match any lowercase letter use a-z, any uppercase use A-Z and numbers 0-9. 
  Use [] to indicate optional characters. Use + to match once or more times. @ will match itself.
To find all matches of a regex, use .findall().
Remember the .format() syntax: "text {}".format(string).
  
Code:
# Write a regex that matches email
regex_email = r"([A-Za-z0-9]+)@\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))
    
Remember that placing a subpattern inside parenthesis will capture that content and stores it temporarily in memory. This can be later reused.

4.3. Flying home
Your boss assigned you to a small project. They are performing an analysis of the travels people made to attend business meetings. You are given a dataset with only the email subjects for each of the people traveling.

You learn that the text followed a pattern. Here is an example:

Here you have your boarding pass LA4214 AER-CDB 06NOV.

You need to extract the information about the flight:
-The two letters indicate the airline (e.g LA),
-The 4 numbers are the flight number (e.g. 4214).
-The three letters correspond to the departure (e.g AER),
-The destination (CDB),
-The date (06NOV) of the flight.

All letters are always uppercase.

The variable flight containing one email subject was loaded in your session. You can use print() to view it in the IPython Shell.

Instructions 1/4
Import the re module.

Code:
# Import re
import re

Instructions 2/4
Complete the regular expression to match and capture all the flight information required. Only the first parenthesis were placed for you.

Hint
To match uppercase letters use A-Z inside []. To match numbers \d. Use {m} to specify m repeated times. 
Capture groups by placing the expression inside parentheses. Only the first pair was placed for you.

Code:
# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

Instructions 3/4
Find all the matches corresponding to each piece of information about the flight. Assign it to flight_matches.

Hint: Use .findall().

Code:
# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)

Instructions 4/4
Complete the format method with the elements contained in flight_matches. In the first line print the airline,and the flight number. 
In the second line, the departure and destination. In the third line, the date.

Hint
findall() returns tuples. The n group capture will be the n element in the tuple. You can access it by doing tuple[0][n].

Code:
# Import re
import re

# Write regex to capture information of the flight
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all matches of the flight information
flight_matches = re.findall(regex, flight)
    
#Print the matches
print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))

findall() returns a list of tuples. The nth element of each tuple is the element corresponding to group n. 
This provides us with an easy way to access and organize our data.

4.4. Alternation and non-capturing groups
1. Alternation and non-capturing groups
In this video, we'll talk about other ways in which grouping characters can help us.

2. Pipe
You've learned in previous videos about the vertical bar or pipe operator. 
Suppose we have the following string. And we want to find all matches for pet names. 
So we can use the pipe operator to specify that we want to match cat or dog or bird as you see in the code. 
This will output the following list.

3. Pipe
Now, we changed the string a little bit. And once more we want to find all the pet names. 
But this time only those that come after a number and a whitespace. So we specify this again with the pipe operator. 
Hmm we got the wrong output. Why? 
The pipe operator works comparing everything that is to its left (digit whitespace cat) with everything to the right, dog.

4. Alternation
In order to solve this, we can use alternation. 
In simpler terms, we can use parentheses again to group the optional characters as you can see in the slide. 
In the code, now the parentheses are added to group cat or dog or bird. This time we get the output cat and dog. 
This is the correct match as only these two patterns followed a number and whitespace.

5. Alternation
In the previous example, we may also want to match the number. 
In that case, we need to place parentheses to capture the digit group as seen in the slide. 
In the code, we now use two pair of parentheses. We use findall in the string. And we get a list with two tuples as shown in the output.

6. Non-capturing groups
Sometimes, we need to group characters using parentheses. But we are not going to reference back to this group. 
For these cases, there are a special type of groups called non-capturing groups. 
For using them, we just need to add question mark colon inside the parenthesis but before the regex.

7. Non-capturing groups
We have the following string. We want to find all matches of numbers. 
We see that the pattern consists of two numbers and dash repeated three times. After that, three numbers, dash, four numbers. 
We want to extract only the last part without the first repeated elements. We need to group the first two elements to indicate repetitions. 
But we don't want to capture them. So we use non-capturing groups to group backslash d repeated two times and dash. 
Then we indicate this group should be repeated three times. 
Then, we group backslash d repeated three times, dash, backslash d repeated three times as shown in the slide. 
In the code, we then match the regex to the string. And we get the numbers we were looking for as shown in the output.

8. Alternation
Finally, we can combine non-capturing groups and alternation together. 
Remember that alternation implies using parentheses and the pipe operand to group optional characters. 
Let's suppose that we have the following string. And we want to match all the numbers of the day. 
We know that they are followed by th or rd. But we only want to capture the number and not the letters that follow. 
We write our regex. We capture inside parentheses backslash d repeated once or more times. 
Then, we can use a non-capturing group. Inside we use the pipe operator to choose between th and rd as shown in the code. 
We find all the matches in the string. And we get the correct output.

4.5. Love it!
You are still working on the Twitter sentiment analysis project. First, you want to identify positive tweets about movies and concerts.

You plan to find all the sentences that contain the words love, like, or enjoy and capture that word. 
You will limit the tweets by focusing on those that contain the words movie or concert by keeping the word in another group. 
You will also save the movie or concert name.

For example, if you have the sentence: I love the movie Avengers. You match and capture love. You need to match and capture movie. 
Afterwards, you match and capture anything until the dot.

The list sentiment_analysis containing the text of three tweets and the re module are loaded in your session. 
You can use print() to view the data in the IPython Shell.

Instructions
Complete the regular expression to capture the words love or like or enjoy. 
  Match and capture the words movie or concert. Match and capture anything appearing until the ..
Find all matches of the regex in each element of sentiment_analysis. Assign them to positive_matches.
Complete the .format() method to print out the results contained in positive_matches for each element in sentiment_analysis.

Hint
Use | between the optional words you want to capture inside the parentheses (). 
  Use the . metacharacter together with the plus quantifier if you want to match any type of character. 
  Consider using a non-greedy quantifier adding ?.
To find all matches, use .findall().
Remember the .format() syntax: "text {}".format(variable).

Code:
# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)
    
    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))
    
The pipe operator works by comparing everything that is to its left with everything to the right. 
Grouping optional patterns is the way to get the correct result.

4.6. Ugh! Not for me!
After finding positive tweets, you want to do it for negative tweets. 
Your plan now is to find sentences that contain the words hate, dislike or disapprove.
You will again save the movie or concert name. 
You will get the tweet containing the words movie or concert but this time, you don't plan to save the word.

For example, if you have the sentence: I dislike the movie Avengers a lot.. You match and capture dislike. 
You will match but not capture the word movie. Afterwards, you match and capture anything until the dot.

The list sentiment_analysis containing the text of three tweets as well as the re module are loaded in your session. 
You can use print() to view the data in the IPython Shell.

Instructions
Complete the regular expression to capture the words hate or dislike or disapprove. 
  Match but don't capture the words movie or concert. Match and capture anything appearing until the ..
Find all matches of the regex in each element of sentiment_analysis. Assign them to negative_matches.
Complete the .format() method to print out the results contained in negative_matches for each element in sentiment_analysis.

Hint
To capture optional groups, use | inside the parentheses. To capture any character use the . metacharacter. 
    Consider using a non-greedy quantifier. To match but not capture a group, use non-capturing syntax ?:. Remember to escape the dot.
To find all matches, use .findall().
Remember the .format() syntax: "text {}".format(variable).

Code:
# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\."

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)
    
    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))
    
Non-capturing groups are very often used together with alternation. Sometimes you have optional patterns and you need to group them. 
However you are not interested in keep in them. It's a nice feature of regex.

4.7. Backreferences
1. Backreferences
We will now discuss how we can backreference capturing groups.

2. Numbered groups
Imagine we come across this text. And we want to extract the date highlighted. But we want to extract only the numbers. 
So, we can place parentheses in a regex to capture these groups as we learned.

3. Numbered groups
We have also seen that each of these groups receive a number. The whole expression is group zero. 
The first group one, and so on, as shown in the slide.

4. Numbered groups
Let's use dot search to match the pattern to the text. 
To retrieve the groups captured, we can use the method dot group specifying the number of a group we want. 
For example, three. The method retrieves the match corresponding to group number three as shown in the output. 
We can also retrieve group zero. It will output the entire expression. Dot group can only be used with dot search and dot match methods.

5. Named groups
We can also give names to our capturing groups. 
Inside the parentheses, we write question mark capital p, and the name inside angle brackets as shown in the slide.

6. Named groups
Let's say we have the following string. We want to match the name of the city and zipcode in different groups. 
We can use capturing groups and assign them the name city and zipcode as shown in the code. 
We retrieve the information by using dot group. We indicate the name of the group. 
For example, specifying city gives us the output Austin. Specifying zipcode gives us the number match as shown.

7. Backreferences
There is another way to backreference groups. 
In fact, the matched group can be reused inside the same regex or outside for substitution. 
We can do this using backslash and the number of the group as you can see in the slide.

8. Backreferences
Let's see an example. We have the following string. We want to find all matches of repeated words. 
In the code, we specify that we want to capture a sequence of word characters. Then a whitespace.

9. Backreferences
Then we write backslash one. This will indicate that we want to match the first group captured again. 
In other words, it says match that sequence of characters that was previously captured once more. 
And we get the word happy as an output. This was the repeated word in our string.

10. Backreferences
Now, we will replace the repeated word with one occurrence of the same word. In the code, we use the same regex as before. 
This time, we use the dot sub method. In the replacement part, we can also reference back to the captured group. 
We write r backslash one inside quotes. This says replace the entire expression match with the first captured group. 
In the output string, we have only one occurrence of the word happy.

11. Backreferences
We can also use named groups for backreferencing. To do this, we use question mark capital p equal sign and the group name. 
In the code, we want to find all matches of the same number. We use a capturing group and name it code. 
Later, we reference back to this group. And we obtain the number as an output.

12. Backreferences
On the other hand, to reference the group back for replacement we need to use backslash g and the group name inside angle brackets. 
In the code, we want to replace repeated words by one occurrence of the same word. Inside the regex, we use the previous syntax. 
In the replacement field, we need to use this new syntax as seen in the code to get the following output.

4.8. Parsing PDF files
You now need to work on another small project you have been delaying. Your company gave you some PDF files of signed contracts. 
The goal of the project is to create a database with the information you parse from them. 
Three of these columns should correspond to the day, month, and year when the contract was signed.
The dates appear as Signed on 05/24/2016 (05 indicating the month, 24 the day). 
You decide to use capturing groups to extract this information. 
Also, you would like to retrieve that information so you can store it separately in different variables.

You decide to do a proof of concept.

The variable contract containing the text of one contract and the re module are already loaded in your session. 
You can use print() to view the data in the IPython Shell.You now need to work on another small project you have been delaying. 
Your company gave you some PDF files of signed contracts. 
The goal of the project is to create a database with the information you parse from them. 
Three of these columns should correspond to the day, month, and year when the contract was signed.
The dates appear as Signed on 05/24/2016 (05 indicating the month, 24 the day). 
You decide to use capturing groups to extract this information. 
Also, you would like to retrieve that information so you can store it separately in different variables.

You decide to do a proof of concept.

The variable contract containing the text of one contract and the re module are already loaded in your session. 
You can use print() to view the data in the IPython Shell.

Instructions 1/3
Write a regex that captures the month, day, and year in which the contract was signed. Scan contract for matches.

Hint
To capture a group, place the expression inside parentheses (group). To find a number repeated m times you can use {m} quantifier. 
The \s matches the spaces between the words. Don't forget to match the words signed, on before the date. 
Use .search() to scan the string for a match.

Code:
# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

Instructions 2/3
Assign each captured group to the corresponding keys in the dictionary.

Hint
To retrieve captured groups, you can use the numbers assigned to them in the matching process. 
The m group match can be retrieved using .group(m). Remember that the first matched group receives the number 1.

Code:
# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}


Instructions 3/3
Complete the positional method to print out the captured groups. Use the values corresponding to each key in the dictionary.

Hint
To insert values associated with a key in a dictionary, remember the .format() syntax: text {data[key]}".format(data=dictionary).

Code:
# Write regex and scan contract to capture the dates described
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign to each key the corresponding match
signature = {
	"day": dates.group(2),
	"month": dates.group(1),
	"year": dates.group(3)
}
# Complete the format method to print-out
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))


Remember that each capturing group is assigned a number according to its position in the regex. 
Only if you use .search() and .match(), you can use .group() to retrieve the groups.

4.9. Close the tag, please!
In the meantime, you are working on one of your other projects. The company is going to develop a new product. 
It will help developers automatically check the code they are writing. 
You need to write a short script for checking that every HTML tag that is open has its proper closure.

You have an example of a string containing HTML tags:

<title>The Data Science Company</title>

You learn that an opening HTML tag is always at the beginning of the string. It appears inside <>. 
A closing tag also appears inside <>, but it is preceded by /.

You also remember that capturing groups can be referenced using numbers, e.g \4.

The list html_tags, containing three strings with HTML tags, and there module are loaded in your session. 
You can use print() to view the data in the IPython Shell.

Instructions
Complete the regex in order to match closed HTML tags. Find if there is a match in each string of the list html_tags. Assign the result to match_tag.
If a match is found, print the first group captured and saved in match_tag.
If no match is found, complete the regex to match only the text inside the HTML tag. Assign it to notmatch_tag.
Print the first group captured by the regex and save it in notmatch_tag.

Hint
To capture the text inside <>, place parenthesis around the expression: r"<(text)>. ,
    To confirm that the same text appears in the closing tag, reference back to the m group captured by using \m.
To print the m group captured, use .group(m).
To capture the text inside <>, use parentheses: r"<(text)>.
To print the m group captured, use .group(m).

Code:
for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)
 
    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1))) 
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)
 
    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1))) 
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))
        
Backreferences are very helpful when you need to reuse part of the regex match inside the regex. 
Knowing when and how to use them will simplify many of your tasks!

4.10. Reeepeated characters
Back to your sentiment analysis! Your next task is to replace elongated words that appear in the tweets. 
We define an elongated word as a word that contains a repeating character twice or more times. e.g. "Awesoooome".

Replacing those words is very important since a classifier will treat them as a different term from the source words lowering their frequency.

To find them, you will use capturing groups and reference them back using numbers. E.g \4.

If you want to find a match for Awesoooome. You first need to capture Awes. Then, match o and reference the same character back, and then, me.

The list sentiment_analysis, containing the text of three tweets, and the re module are loaded in your session. 
You can use print() to view the data in the IPython Shell.

Instructions
Complete the regular expression to match an elongated word as described.
Search the elements in sentiment_analysis list to find out if they contain elongated words. Assign the result to match_elongated.
Assign the captured group number zero to the variable elongated_word.
Print the result contained in the variable elongated_word.

Hint
First match the starting characters \w zero or more times. To capture word characters, use (\w+). Reference back to the captured group number m by using \m. Match the ending characters \w zero or more times.
To search for a match, use .search().
To retrieve the group m, use .group(m).
Remember the .format() syntax: "text {variable}".format(variable=string)

Code:
# Complete the regex to match an elongated word
regex_elongated = r"\w*(\w)\1\w*"

for tweet in sentiment_analysis:
	# Find if there is a match in each tweet 
	match_elongated = re.search(regex_elongated, tweet)
    
	if match_elongated:
		# Assign the captured group zero 
		elongated_word = match_elongated.group(0)
        
		# Complete the format method to print the word
		print("Elongated word found: {word}".format(word=elongated_word))
	else:
		print("No elongated word found")     	

You should remember that the group zero stands for the entire expression matched. 
It's always helpful to keep that in mind. Sometimes you will need to use it.

4.11. Lookaround
1. Lookaround
In this final video, we will look into specific types of non-capturing groups. They help us look around an expression.

2. Looking around
Look-around will look for what is behind or ahead of a pattern. Imagine that we have the following string.

3. Looking around
We want to see what is surrounding a specific word. For example, we position ourselves in the word cat. 
So look-around will let us answer the following problem. At my current position, look ahead and search if sat is there. 
Or look behind and search if white is there.

4. Look-ahead
We'll start by exploring look-ahead. 
This non-capturing group checks whether the first part of the expression is followed or not by the lookahead expression. 
As a consequence, it will return the first part of the expression. 
In the previous example, we are looking for the word cat. The look ahead expression can be either positive or negative. 
For positive we use question mark equal. For negative question mark exclamation mark.

5. Positive look-ahead
Let's start with positive lookahead. Let's imagine that we have a string containing file names and the status of that file as shown in the code. 
We want to extract only those files that are followed by the word transferred. 
So we start building the regex by indicating any word character followed by dot txt.

6. Positive look-ahead
We now indicate we want the first part to be followed by the word transferred. 
We do so by writing question mark equal and then whitespace transferred all inside the parenthesis. 
With that specification, we get only the desired strings as shown in the output.

7. Negative look-ahead
Now, let's use negative lookahead in the same example.

8. Negative look-ahead
In this case, we will say that we want those matches that are NOT followed by the expression transferred. 
We use instead question mark exclamation mark inside parenthesis as seen in the code. Now, we get this other output.

9. Look-behind
The non-capturing group look-behind gets all matches that are preceded or not by a specific pattern. 
As a consequence, it will return the matches after the look expression. 
Let's use the same example, but now we are looking before the word cat. 
Look behind expression can also be either positive or negative. 
For positive we use question mark angle bracket equal. For negative question mark angle bracket exclamation mark.

10. Positive look-behind
Let's look at the following string. We want to find all matches of the names that are preceded by the word member. 
How do we construct our regex with positive look-behind? Let's examine the code. 
At the end of the regex, we'll indicate we want a sequence of word characters whitespace another sequence of word characters.

11. Positive look-behind
Pay attention to the code. The look-behind expression goes before that expression. 
We indicate question mark angle bracket equal followed by member, colon, and whitespace. All inside parentheses. 
In that way we get the two names that were preceded by the word member as shown in the output.

12. Negative look-behind
Now, we have this other string. We will use negative look-behind. 
We will find all matches of the word cat or dog that are not preceded by the word brown. 
In this code example, we use question mark angle bracket exclamation mark, followed by brown, whitespace. All inside the parenthesis. 
Then, we indicate our alternation group: cat or dog. Consequently, we get cat as an output. 
The cat or dog word that is not after the word brown.


4.12. Surrounding words
Now, you want to perform some visualizations with your sentiment_analysis dataset. 
You are interested in the words surrounding python. You want to count how many times a specific words appears right before and after it.

Positive lookahead (?=) makes sure that first part of the expression is followed by the lookahead expression. 
Positive lookbehind (?<=) returns all matches that are preceded by the specified pattern.

The variable sentiment_analysis, containing the text of one tweet, and the re module are loaded in your session. 
You can use print() to view the data in the IPython Shell.

Instructions 1/2
Get all the words that are followed by the word python in sentiment_analysis. Print out the word found.

Hint
In order to indicate that you want what comes before word, use (?=\sword). You can use \w to indicate word characters. 
Use the findall function of the re module.

Code:
# Positive lookahead
look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

Instructions 2/2
Get all the words that are preceded by the word python or Python in sentiment_analysis. Print out the words found.

Hint
In order to find words that are preceded by word or Word, 
use the findall() function of the re module and the regex expression (?<=[Ww]ord\s). Indicate word characters using \w.

Code:
# Positive lookbehind
look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)

It is important to know that positive lookahead will return the text matched by the first part of the expression after asserting 
that it is followed by the lookahead expression while positive lookbehind will return all matches that follow a specific pattern.

4.13. Filtering phone numbers
Now, you need to write a script for a cell-phone searcher. It should scan a list of phone numbers and return those that meet certain characteristics.

The phone numbers in the list have the structure:
-Optional area code: 3 numbers
-Prefix: 4 numbers
-Line number: 6 numbers
-Optional extension: 2 numbers

E.g. 654-8764-439434-01.

You decide to use .findall() and the non-capturing group's negative lookahead (?!) and negative lookbehind (?<!).

The list cellphones, containing three phone numbers, and the re module are loaded in your session. You can use print() to view the data in the IPython Shell.

Instructions 1/2
Get all cell phones numbers that are not preceded by the optional area code.

Hint
To get all matches of a pattern that are not preceded by a subpattern, use (?<!subpattern)pattern. 
Remember to use \d for digits. Use {n, m} to specify a minimum of n and a maximum of m repetitions.

Code:
for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)

Instructions 2/2
Get all the cell phones numbers that are not followed by the optional extension.

Hint
To get all matches of a pattern that are not followed by a subpattern, use pattern(?!subpattern). 
Remember to use \d for digits. Use {n, m} to specify a minimum of n and a maximum of m repetitions.

Code:
for phone in cellphones:
	# Get all phone numbers not followed by optional extension
	number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number)
  
Negative lookarounds work in a similar way to positive lookarounds. 
They are very helpful when we are looking to exclude certain patterns from our analysis.

4.14. Finishing line
1. Finishing line
You have reached the finishing line of this course on regular expression in python.

2. Our journey
In our journey, you started by learning the key concepts of string manipulation. 
Along the way, you have manipulated strings coming from movie reviews. You concatenated them and split them. 
You accessed them by index and sliced them. Finally, you replaced and removed characters.

3. Our journey
You went a little bit further and learned how to insert custom strings into predefined text. 
You worked with strings scraped from the web. You applied the three string formatting methods that Python allows. 
You also learned in which situation they fit best.

4. Our journey
These concepts helped you take a deep turn and learn the basic syntax of regular expressions. 
You worked with a dataset containing real tweets. You matched, found and replaced normal characters and metacharacters. 
You also applied quantifiers, both greedy and non-greedy ones.

5. Our journey
Finally, you went ahead and learned advanced concepts of regular expressions. 
You used capturing and non-capturing groups to match a specific subpattern in a text. 
You also learned how to backreference them as well as how to look what comes before or after a specific pattern. 
Overall, you now have a better understanding of regular expressions.

6. Last tips
However, there is more to learn. And I would like to give you some last tips. Practice regex whenever you can. 
This will help you reinforce what you've learned. Apply them in your projects. They will help you do things in an easier way. 
Regex can be difficult at the beginning. But enjoy learning them as they are a powerful tool.





