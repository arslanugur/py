# SECTION 1: Metacharacters
# Metacharacters are what make regular expressions more powerful than normal string methods.
# They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel".

# All of the metacharacters are： . ^ $ * + ? { [ ] \ | ( ) }

# The existence of metacharacters poses a problem if you want to create a regular expression (or regex) that matches a literal metacharacter, such as "$". 
# You can do this by escaping the metacharacters by putting a backslash in front of them.
# However, this can cause problems, since backslashes also have an escaping function in normal Python strings. 
# This can mean putting three or four backslashes in a row to do all the escaping.

# To avoid this, you can use a raw string, which is a normal string with an "r" in front of it. We saw usage of raw strings in the previous lesson.


# To avoid sth like this: str = "/p///$" 
# They do this: str = r"p/$" 
# That's what I understand. Maybe not an applicable example but illustrates the concept 

# The backslash (\) is used as a escape character. 
# For instance, you can use it to create a newline using “\n”. 
# For you actually to print a “\” string you need to add a 2nd backslash “\\”. 
# Now imagine you are printing a Windows path “C:/user/documents/file”, 
# you would have to add a 2nd backslash wherever a backslash appears: “C://user//documents//file”. 
# That can be a bit messy... Lucky, with r we can create a raw string... path = r”C:/user/documents/file” Now the backslash will not be escaped 

# Example: to create a raw string. 
str = r "I am \r\a\w!"

# The r"I am \r\a\w!", without the 'r' prefix, we will get '\w!' when print. 
# Explanation: 
# \r returns Carriage, 
# which deletes the previous characters "I am " \a is the ASCII for 'alert' - ring the bell (invisible character) \w! are normal literal characters. 
# They are printed out.

# SECTION 2:
# The first metacharacter we will look at is . (dot).
# This matches any character, other than a new line.
# Example:
import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")          #

if re.match(pattern, "gray"):
    print("Match 2")          #

if re.match(pattern, "blue"):
    print("Match 3")
#

# You can match the characters with number of dots for example 
import re 

pattern = r"gr..y" 

if re.match(pattern, "grey"): 
  print("Match 1") 
if re.match(pattern, "graly"):  # This program displays 'Match 2' so we need to increase dots based on the string length. 
  print("Match 2")              # So one may search for a discontinued string
if re.match(pattern, "blue"): 
  print("Match 3")            
# 

# Example:
import re 

def metacharacters(): 
  string_list = [ "spam", "spum", "spim", "sram" ] 
  string_pattern = "sp.m" 
  for str in string_list: 
    if re.match(string_pattern, str): 
      print("{} match \t\t\t{}".format(str, string_pattern)) 
    else: 
      print("{} doesn't match \t{}".format(str, string_pattern)) 
      
metacharacters() # Output: spam match sp.m >> spum match sp.m >> spim match sp.m >> sram doesn't match sp.m
#

# The dot . acts like a *wildcard* character (placeholder) in regex.
# the dot character serve as a place holder. The more dot u put the more characters it will represent 
# For instance, 
import re 
pattern=r"...bla" 

if re.match(pattern, "blabla"): 
  print("correct1")               #
if re.match(pattern, "blubla"): 
  print("correct2")               #
if re.match(pattern, "bbla"): 
  print("correct3") 
if re.match(pattern, "bla"): 
  print("correct4")
#

# Example:
import re 
pattern = r"gr.y" 

if re.match(pattern, "grey"): 
  print("Match 1")                #
if re.match(pattern, "gray"): 
  print("Match 2")                #
if re.match(pattern, "greyfindor"): 
  print("Match 3")                #
if re.match(pattern, "agrey"):
  print("Match 4") 
if re.match(pattern, "greay"):
  print("Match 5")
# if we put another character that is not necessary e.g(agrey) it does not match so by using $ in the next lesson will prove itself useful 
# but in the case of ^ i do nit know yet where it can be useful

# In regex, the dot "." matches every character except newline. 
# Don't ask why, it has always been like this, in every regex application (shell for exemple). 
# So, "e.g" will match "eag", "ebg", "eZg", "e$g", "e g", "e_g", but also "e g" (with the tab char). 
# So, the string "...." wil match every string composed of four characters, including space, tab, underscore, etc. 
# "aaaa", "j9)+", " ", "...." (yes, it would also match a four-point string) !. 
# But, it won't match a string written on two lines, because the new-line character won't match!


# SECTION 3:
# The next two metacharacters are ^ and $.
# These match the start and end of a string, respectively.
# Example:
import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")          #

if re.match(pattern, "gray"):
    print("Match 2")          #

if re.match(pattern, "stingray"):
    print("Match 3")
#

# The pattern "^gr.y$" means that the string should start with gr, then follow with any character, except a newline, and end with y.

# if you use the method "search" that look for your pattern anywhere in the string, then the "ˆ" with be useful. 
# In any case you're wondering, yes, do re.match("egg", "eggspam") will as match as re.search("ˆegg","eggspam") will do! 
# Just an advice, don't mind about the "match" method, and only use the "ˆ" meta characters !

# An example is as follows: 
import re 
pattern = r"^gr.y" 
if re.search(pattern, "agrey"): 
  print ("Match 1") 
if re.search(pattern, "gray"): 
  print ("Match 2") #
if re.match(pattern, "mygray"): 
  print ("Match 3") # If the carrot ^ symbol is omitted from the pattern, then Match 1 and Match 2 would be printed. 
#

# ^ symbolizes the start of the strict pattern, and $ the end of the strict pattern 
# You can omit it if you don want that it be so strict, it could allow you 'match' the first ocurrence while the another no. 
# Just like this: 
# Example: 
import re 
pattern_strict = r"^love$" 
simple_pattern = r"love" 
if re.match(pattern_strict, "love"): 
  print("Match strict: 1")              #
if re.match(pattern_strict, "lovelazy"): 
  print("Match strict: 2") 
if re.match(simple_pattern, "love"): 
  print("Match simple: 3")              #
if re.match(simple_pattern, "lovelazy"): 
  print("Match simple: 4")              #
if re.match(simple_pattern, "lazylove"): 
  print("Match simple: 5")
# Pay atention to the "(pattern_strict, "lovelazy")" and "(simple_pattern, "lovelazy")". Only matches with "(simple_pattern, "lovelazy"):"


# Example:
# The word regular function 're.match' for the third line should be replaced with 're.search'. with that it is easier to understand.
# Example:
import re 
pattern = r"^gr.y$" 
if re.match(pattern, "grey"): 
  print("Match 1") 
if re.match(pattern, "gray"): 
  print("Match 2") 
if re.search(pattern, "stingray"): 
  print("Match 3") 
# Output: Match 1 Match 2 but if you remove '^' in pattern: Output: Match 1 Match 2 Match 3

# Example:
import re 
string_list1 = [ "grey", "gray", "stingray" ] 
string_pattern1 = r"^gr.y$" 
def metacharacters(list, pattern): 
  for str in list: 
    if re.match(pattern, str): 
      print("pattern '{1}' matches '{0}'".format(str, pattern)) 
    else: 
      print("pattern '{1}' doesn't match '{0}'".format(str, pattern)) 
#      
metacharacters(string_list1, string_pattern1) 
# Output: pattern '^gr.y$' matches 'grey' pattern '^gr.y$' matches 'gray' pattern '^gr.y$' doesn't match 'stingray'

# Example:
import re 
pattern = r"y$" 
if re.match(pattern, "grey"): 
  print("Match 1") 
if re.match(pattern, "gray"): 
  print("Match 2") 
if re.match(pattern, "stingray"): 
  print("Match 3") # shouldn't this code return match 1,2,3 because all end with y
#

# purpose of the $ is to check the string ends with the last character in this case y 
# this slight modification should help you understand more clearly 
import re 
pattern = r"^gr.y$" 
if re.match(pattern, "grey"): 
  print("Match 1")            #
if re.match(pattern, "gray"): 
  print("Match 2")            #
if re.match(pattern, "stingray"): 
  print("Match 3") 
  
pattern = r"^gr.y" 
if re.match(pattern, "grayt"): 
  print("Match 4")            #
#

# Example:
# In order to get match 3 we can change the pattern like this: 
import re 
pattern = r"....gr.y$" 
if re.match(pattern, "grey"): 
  print("Match 1") 
if re.match(pattern, "gray"): 
  print("Match 2") 
if re.match(pattern, "stingray"): 
  print("Match 3") # Output: Match 3 
# Or you can use "re.findall" instead of "re.match" and remove ^: 
import re 
pattern = r"gr.y$" 
if re.findall(pattern, "grey"): 
  print("Match 1") 
if re.findall(pattern, "gray"): 
  print("Match 2") 
if re.findall(pattern, "stingray"): 
  print("Match 3") # Output: Match 1 Match 2 Match 3
#

# Example:
import re 
pattern = r"gr.y$" 
if re.search(pattern, "reystonnegro"): 
  print("Match 1") 
if re.search(pattern, "gray"): 
  print("Match 2") 
if re.search(pattern, "stingray"): 
  print("Match 3") # running this code you'll get: Match 2 and Match 3 only becouse? Of course, pattern must end with 'y'.
#

# Example: to create a pattern  that matches strings that contain 3 characters, out of which the last character is an exclamation mark 
r"..!$"

# Here's the example to demonstrate the behaviour of metacharacters:- pattern1 = r"12.$" pattern2 = r"^12.$" 
# Find a 3-characters string begins with 12 followed by any character ❎ re.match( pattern1, "123123" ) 
# Find a 3-characters string begins with 12 followed by any character ❎ re.match( pattern2, "123123" ) 
# Find any 3-characters substring with pattern 12 followed by any character ✅ re.search( pattern1, "123123" ) 
# Find a 3-characters string begins with 12 followed by any character ❎ re.search( pattern2, "123123" ) 
# match have limited usage which restricts to match from the beginning of string only.


