# SECTION 1
# Character classes provide a way to match only one of a specific set of characters.
# A character class is created by putting the characters it matches inside square brackets.
# Example:
import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")                  #

if re.search(pattern, "qwertyuiop"):
    print("Match 2")                  #

if re.search(pattern, "rhythm myths"):
    print("Match 3")
#

# The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

# Example: Password Analysor 
while True: 
  password = str(input('Insert a password: ')).strip() # Password length validation 6 - 10 characterss 
  
lenPw = len(password) 
if lenPw < 6 or lenPw > 10: 
  print('Number of characters incorrect!') 
  continue # with number or not? only password with numbers allowed 

import re   
patternPw = r"[0123456789]" #or [0-9] 
if re.search(patternPw, password): 
  print('This password has at least one number') 
  break 
else: 
  print('This is not a Valid Password! It needs at least one number') 
  print('try again, dude!')
#

# If we used match instead of search we have to start the string with a litter that exist in the pattern 
# Example: 
import re 
pattern =r'[ieo]' 
if re.match(pattern,'good'): 
  print('good job_1') 
if re.match(pattern,'egood'): 
  print('good job_2')         #
#

# For those looking for practical applications with regular expressions, Google has their own guide. https://developers.google.com/edu/python/regular-expressions

# Lets say you have string and you have to find all names starting with [AEIOU] <- (starting with A / E / I / O / U) and ending with e or c NOTE: 1 square bracked == 1 letter. 
# Example:
import re 
pattern = r'^[AEIOU][a-z]*[ec]$' # * <- matches 0 or more 
string = "Does your brother Eric likes Jane or Anna" # I didn't use question mark for easier explanation. 
string = string.split(" ") # It will make list of words. 
for word in string: 
  names = re.search(pattern,word) 
  if names: 
    print(word) # Eric
#

# Example:
import re 
pattern = r"[aei][ou]" 
if re.search(pattern, "aeiou"): 
  print("Match 1")              #
if re.search(pattern, "uoiea"):
  print("Match 2") 
if re.search(pattern, "aei"): 
  print("Match 3") 
if re.search(pattern, "oi"): 
  print("Match 4") 
if re.search(pattern, "ao"): 
  print("Match 5")              # 
if re.search(pattern, "oa"): 
  print("Match 6") 
if re.search(pattern, "oau"):
  print("Match 7")              #
#

# if r is a raw string indicator used to avoid back slashes when you have an escape character in your text 
# then why does r"[aeiou]" recognize [ & ] as escape characters? 
# Shouldn't r override that functionality? to me r should mean all strings after me are only strings and not escape characters.

# less confusing example:
import re 
pattern = r"[eq]" 
if re.search(pattern, "grey"): 
  print("Match 1")                  # 
if re.search(pattern, "qwrtyuiop"): 
  print("Match 2") 
if re.search(pattern, "rhythm myths"): 
  print("Match 3")                  #
#

# What would [abc][def] match?    Any letter out of "abc", then any out of "def"

# [abc][def] would mean that in any given string 
# there must at least be any one instance in the string where a character from [abc] is immediately followed by a character from [def]. 
# So something like "I like to add" would return true because in the word add, there is an "a" immediately followed by a "d". 
# But in the word "and" because the "n" is between "a" and "d" the search would result false.

# Example:
import re 
pattern = r"[aei][ou]" 
if re.search(pattern, "grey"): 
  print("Match 1") 
if re.search(pattern, "qwertyuiop"): 
  print("Match 2")                  # 2 
if re.search(pattern, "a rhythm myths"): 
  print("Match 3")
#

# Example:
import re pattern = r"[abc][def]" 
# The pattern will match if at least one letter of the first square bracket [abc] and at least one letter of the second square bracket [def] appear together
if re.search(pattern, "a"): 
  print("Match 1") # Choosing a letter 'a' from the first square bracket, it doesn't have a letter from the second square bracket, it won't match
if re.search(pattern, "d"): 
  print("Match 2") # Choosing a letter 'd' from the second square bracket, it doesn't have a letter from the first square bracket, it won't match
if re.search(pattern, "ad"): 
  print("Match 3") # Here we have two letters ('a' and 'd') from both square brackets, it will match.
# 

# First of all questions needs to ask properly in string format. 
# i.e., '[abc][def]' & r'[abc][def]' for meta character [abc][def] gives you syntax error. 
# because --> def <-- is used to create user defined functions.(or built-in-function) so use of --> def <-- gives you syntax error. 
# '[abc][def]' means a character from '[abc]' 
# IMMEDIATELY FOLLOWED by a character from '[def]' ONLY ONCE anywhere in the string. 
# i.e., 'xxaxxdxxxbforaxble' match i.e., 'valid' no match i.e., 'adorable' match but, if you just put ^ at starting in either square. 
# it gives you output match. no matter wherever it appears in the string. 
# but, don't put them together. i.e., '[abc][^def]' or '[^abc][def]' 
# i.e., 'valid' match i.e., 'xxaxxxdxxxbxxfxxxexc' match i.e., 'adorbf' no match '[^abc]' matching characters other than abc in short, ^ invert the string

# If any letter from "abc" is followed by any letter from "def" in a string. It will be marked as True otherwise false. 
# Example:
pattern = r"[abc][def]" 
if re .search(Pattern, "my name is adam"): 
  print("there is a match")
else:
  print("there isn't a match") # there is a match <<<<< since "a" is followed by "d" in "adam".
#

# Easy example : 
import re 
pattern = r'[ieo][abc]' 
if re.match(pattern,'i'): 
  print('good job_1') 
if re.match(pattern,'a'): 
  print('good job_2') 
if re.match(pattern,'ia'): 
  print('good job_3') #
#


# SECTION 2
# Character classes can also match ranges of characters.
# Some examples:
# The class [a-z] matches any lowercase alphabetic character.
# The class [G-P] matches any uppercase character from G to P.
# The class [0-9] matches any digit.
# Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
# Example:
import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")          #

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")
#

# The pattern in the example above matches strings that contain two alphabetic uppercase letters followed by a digit.


https://www.sololearn.com/learning/1073/2478/5163/1 comments






  
  
  
  
  
  
  
  
  
  
  
  
