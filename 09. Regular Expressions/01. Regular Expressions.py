# SECTION 1
# Regular expressions are a powerful tool for various kinds of string manipulation.
# They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python.
# They are useful for two main tasks:
# - verifying that strings match a pattern (for instance, that a string has the format of an email address),
# - performing substitutions in a string (such as changing all American spellings to British ones).


# Domain specific languages are highly specialized mini programming languages.
# Regular expressions are a popular example, and SQL (for database manipulation) is another.
# Private domain-specific languages are often used for specific industrial purposes.

# https://www.debuggex.com/cheatsheet/regex/python
# https://regex101.com/
# https://docs.python.org/3/howto/regex.html  

# Which of the following tasks CANNOT be performed using regular expressions? -- Checking whether an email address is real

# Regex can check to see if an email address validates as true, or technically conforming to RFC. 
# It cannot check to see if it's real, or in REAL use. I can assume this means that dont.email.me@not.real.com would be valid and is, 
# but it can't check to see if a recipient is using it, if it's registered or used in any way.

# http://stackoverflow.com/questions/201323/using-a-regular-expression-to-validate-an-email-address

# The wording of this question is somewhat bad. 
# Cause to know is "checking whether an email address is real" we must understand what author ment for "real". 
# It looks very close to checking whether an email address is of the correct format. 
# Only knowing that you shoul choose one option and knowing 
# that you can change strings (and email address is a string) using regexp one can understand 
# that option about "real email adress" is about existence of an address... not about their ability to be registered.

# SECTION 2
# Regular expressions in Python can be accessed using the re module, which is part of the standard library.
# After you've defined a regular expression, the re.match function can be used to determine whether it matches at the beginning of a string.
# If it does, match returns an object representing the match, if not, it returns None.
# To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".
# Raw strings don't escape anything, which makes use of regular expressions easier. 

# Example:
import re

pattern = r"spam"           # r" stands for a raw string

if re.match(pattern, "spamspamspam"):
    print("Match")    #
else:
    print("No match")
#    
# The above example checks if the pattern "spam" matches the string and prints "Match" if it does.
# Here the pattern is a simple word, but there are various characters, which would have special meaning when they are used in a regular expression.


# Example:
import re 

pattern = r"spa" 
print(re.match(pattern, "spamspamspam")) # <_sre.SRE_Match object at 0xf71a82c0> 
# An OBJECT REPRESENTING the match
import re 

pattern = r"spaa" 
print(re.match(pattern, "spamspamspam")) # None

# Raw strings cannot use any newlines, tabs, etc. So print(r"hello\nworld") would literally print "hello\nworld" rather than "hello", newline, "world"

# Example:
import re 
pattern = r"spam" 
if re.match(pattern, "spamspamspam"): 
  print("Match") 
else: 
  print("No match") 
# Here the condition in the if statement does not give a True value. re.match(pattern, "spamspamspam")==True will give as a False. 
# So the condition in the if statement could be something other than True/False

# As some people pointed out, re.match() finds whether the *first* part of the string matches the other string: 
# First Situation:
import re 
pattern = r"spam" 
if re.match(pattern, "spamanythingelse"): 
  print("Match") 
else: 
  print("No match") # Match
  
# Second Situation:
import re 
pattern = r"spam" 
if re.match(pattern, "anythingelsespam"): 
  print("Match") 
else: 
  print("No match") # No match
#

# Which of these patterns would not re.match the string "spamspamspam"? -- pamspam
# The re.match function can be used to determine whether it matches at the BEGINNING of a string. "spamspamspam" first character is not "p" like in "pamspam"

# Maybe it is just me but I was confused why 'pamspam' is correct. 
# It turned out I missed the "NOT" in the question: 
# The question is which pattern would NOT re.match the string "spamspamspam"? 
# Since re.match checks the beggining of the word therefore: 
# 1) "sp" would re.match the string "spamspamspam" since the word starts with "sp" 
# 2) "spamspam" would re.match the string "spamspamspam" since the word start with "spamspam" 
# 3) "pamspam" would NOT re.match the string "spamspamspam" since it does NOT starts with "pamspam" therefore it is the correct answer.

# First Situation:
import re 
p = r".pamspam" 
if re.match(p, "spamspamspam"): 
  print(True) 
else: 
  print(False) # True 
  
# Second Situation:
import re 
p = r".+pamspam" 
if re.match(p, "spamspamspam"): 
  print(True) 
else: 
  print(False) # True
#

# Example:
# If the question is converted to code: 
import re 
if re.match("sp", "spamspamspam"): 
  print("Matched 1") 
if re.match("spam", "spamspamspam"): 
  print("Matched 2") 
if re.match("pamspam", "spamspamspam"): 
  print("Matched 3")
#


# SECTION 3
# Other functions to match patterns are re.search and re.findall.
# The function re.search finds a match of a pattern anywhere in the string.
# The function re.findall returns a list of all substrings that match a pattern.

# Example:
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")   #

if re.search(pattern, "eggspamsausagespam"):
    print("Match")      #
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))    # ['spam', 'spam']

# In the example above, the match function did not match the pattern, as it looks at the beginning of the string.
# The search function found a match in the string.

# The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list. 

# You can add "len" to find out how many occurrences of the word there is... print(len(re.findall(pattern, "eggspamsausagespam"))) # 2

# Shorter Example:
import re 

pattern = r"spam" 
str = "eggspamsausagespam" 

if re.match(pattern, str): 
  print("Match") 
else: print("No match") 
if re.search(pattern, str): 
  print("Match") 
else: 
  print("No match") 
  
print(re.findall(pattern, str))

# Example:
import re 
pattern = r"@" 
if re.search(pattern, "ua@gmail"): 
  print("Valid mail address") 
else: 
  print("Enter a valid mail address") 
#

# print(list(re.finditer(pattern, "eggspamsausagespam"))) 
# or 
# for i in re.finditer(pattern,"eggspamsausagespam"): print(i.group())


# Example:
import re
def print_status(pattern,expression):
    match=re.search(pattern,expression)
    if match:
        print("Found {}".format(match.group()))
    else:
        print("Not found")
print_status(r'iii','piiig')

print_status(r'igs','piiig')
print_status(r'..g','piiig')
print_status(r'\d\d\d','p123g')
print_status(r'\w\w\w','@@abcd!!')
# This module provides regular expression matching operations similar to those found in Perl. 
# Both patterns and strings to be searched can be Unicode strings as well as 8-bit strings. 
# Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their special meaning. 
# This collides with Python’s usage of the same character for the same purpose in string literals; 
# For example, to match a literal backslash, one might have to write '\\\\' as the pattern string, 
# because the regular expression must be \\, and each backslash must be expressed as \\ inside a regular Python string literal.

# Example:
import re 
pattern = r"spa" 
if re.match(pattern, "eggspamsausagespam"): 
  print("Match") 
else: 
  print("No match")   
if re.search(pattern, "eggspamsausagespam"): 
  print("Match") 
else: 
  print("No match") 
  
for x in re.finditer(pattern, "eggspamsausagespam"): 
print(x) 
print(x.group()) 
print(x.start()) 
print(x.end()) 
print(x.span()) 
R="span=" 
y = re.search(R,str(x)) 
print(y) 
print(y.group()) 
print(y.start()) 
print(y.end()) 
print(y.span()) 
print("------")

# Example:
import re 
pattern = r"chimaobi" 
if re.match(pattern, "eggspamsausagespam"): 
  print("Match") 
else: 
  print("No match") 

name = input(r"name: ") 
if re.search(name, "ogbonnachimaobisamuel"): 
  print("there u are") 
else: 
  print("if I catch u!") # No match 
#


# Example:
import re 
seq = r"spam" 
for i in re.finditer(seq, "spamspamspamspamspam"): 
  print((i.start(), i.group())) # This is an example for re.finditer()
#

# match= compare the first character between two word in pattern and re.match search= find any where in re.search, 
# similar word or character findall = this is bigger than search , it find all similar words in the re.findall

# re.match Vs re.search re.match() function will match with whole string. 
# Example- re.match(r"p", "spam") It will return >>> No match. 
# Because p will not match with whole string. 
# You can understand like this- "spam" is not equal to "p" but "spam" is equal to "spam". re.search(r"p", "spam") 
# It will return- >>> Match found. Because it will search the letter p inside the string.

# Which of these is not a function in the re module?  -- findlist
# search, findall

# Example:
def searching(pattern): 
    search_list = dir(re) 
    if pattern in search_list: 
        print("yes") 
    else: 
        print("no") 
        
searching("findlist")
# 


# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html

# SECTION 4
# The regex search returns an object with several methods that give details about it.
# These methods include group which returns the string matched, 
# start and end which return the start and ending positions of the first match, 
# and span which returns the start and end positions of the first match as a tuple.
# Example:
import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())    # pam
    print(match.start())    # 4
    print(match.end())      # 7
    print(match.span())     # (4, 7)
#

# how the ending position will be 7, in the above program I this it will be 6, becos 'm' is in the index of 6th position 

# Example:
import re 
base_pattern = r"spam" 
def re_methods(): 
    re_string = "eggspamsausagespam" 
    re_search_state = re.search(base_pattern, re_string) 
    base_message_search = "found" 
    if re_search_state: 
        print("{1} {0} in '{2}'".format(base_message_search, re_search_state.group(), re_string)) 
        print("start position: {}".format(re_search_state.start())) 
        print("end position: {}".format(re_search_state.end())) 
        print("range: {}".format(re_search_state.span())) 
        print("all findings: {}".format(re.findall(base_pattern, re_string))) 
     else: 
        print("{} {}".format(base_message_search, re_search_state)) 
        
re_methods()

# Example:
import re 
pattern = r"pam" 
match = re.search(pattern, "eggspamsausage") 
if match: 
    print("string matched: " + '' + match.group()) 
    print("string start position: {}".format(match.start())) 
    print("string end position: {}".format(match.end())) 
    print("string span => start&end: {}".format(match.span())) 
#result string matched: pam string start position: 4 string end position: 7 string span => start&end: (4, 7)


# Example: Return Probels
import re
# change pattern
pattern = r"gspams"

match = re.search(pattern, "eggspamsausagchbvvgbcdgnmke")
def probels():
    nums = len(match.group() )
    p = " " * (nums-2)
    return p
    
if match:
    print(match.group())
    print(str( match.start() ) + probels() + str( match.end() ) )
    
    print(type(match.group   ))
    print(type(match.group() ))
    print(type(match.start   ))
    print(type(match.start() ))
    print(type(match.end     ))
    print(type(match.end()   ))
    
    print( match.span() )
#


# CLARIFICATION import re pattern = r"pam" match = re.search(pattern, "eggspamsausage") if match: print(match.group()) print(match.start()) print(match.end()) print(match.span()) OUTPUT pam 4 7 (4, 7) >>>> Pam(string matched) is printed because it's found in the string "eggspamsausage" , done by the .group() method >>>>4 Is printed because, it's the start position of the string matched (pam), done by the .start() method >>>> 7 Is printed because it's the end position of the string matched ( pam), done by the .end() method >>>> lastly, (4,7) is printed because the .span() method brings out the start and end positions respectively of the string matched ( Pam ) as a tuple( unchangeable ordered sequence of values)

https://www.sololearn.com/learning/1073/2475/5158/1








