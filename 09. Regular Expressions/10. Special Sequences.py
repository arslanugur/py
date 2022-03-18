# SECTION 1
# There are various special sequences you can use in regular expressions. They are written as a backslash followed by another character.
# One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.
# Example:
import re

pattern = r"(.+) \1"      # Don't miss the space between the closing bracket and the backslash! The code really should be in a monospace font.
                          # <space> below is where the space character goes... pattern = r"(.+)<space>\1" make sure to leave a space between the ) and the \
match = re.match(pattern, "word word")
if match:
    print ("Match 1")                   # 

match = re.match(pattern, "?! ?!")
if match:
    print ("Match 2")                   # 

match = re.match(pattern, "abc cde")
if match:
    print ("Match 3")
#

# Note, that "(.+) \1" is not the same as "(.+) (.+)", 
# because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.

# here is a simple explanation: (.+) means 1 or more of any character \1 means a repetition of what was found in group number 1

# Example:
pattern = r"(.+) \1" 
pattern = r"no space (one or more repetition of any char) space one or more repetition of what found in group 1 no space" 
# pattern has only one groupe - we have re.match not re.search 
# Then in the example first (.+)space matchs the str "word word" 
# and \1 repetition of the group (.+) which is "word" without space also matched the sting "no space word space word no space" 
# That's why the pattern "(.+) \1" matches the str "word word" and not "word word " or " word word"


# Example:
import re 
pattern = r"(.+) (.+) (.+) \1" 
match = re.match(pattern, "abc bca cab abc") 
if match: 
  print ("Match 1")                           # 
match = re.match(pattern, "abc bca cab bca") 
if match: 
  print ("Match 2") 
match = re.match(pattern, "abc bca cab cab") 
if match: 
  print ("Match 3")
#  
# now try changing the pattern to: 
pattern = r"(.+) (.+) (.+) \2" # which will print >> Match 2 and then to: 
pattern = r"(.+) (.+) (.+) \3" # which will print >>Match 3


# Example:
# Uncomment different pattern for each match. 
import re 
pattern = r"(.+) (.+) (.+) \1" 
# pattern = r"(.+) (.+) (.+) \2" 
# pattern = r"(.+) (.+) (.+) \3" 
match = re.match(pattern, "ABC bca cab ABC") 
if match: 
  print ("Match 1")                         #
#  
match = re.match(pattern, "abc BCA cab BCA") 
if match: 
  print ("Match 2") 
#
match = re.match(pattern, "abc bca CAB CAB") 
if match: 
  print("Match 3")
#  

# finally i understood the pattern and i share it to you: 
# (.+) \1 is not equal to (.+) (.+) . if (.+) match the word 'china', then (.+) \1 will match 'china china'. 
# you may find out that \1 just repeat the first match. but (.+) (.+) will match 'china usa' or something else 


# For those who didn't understand: 
# Using \1 (or `\i` in general; where 0<i<100) means that you're asking python to re-match the exact string matched in the group number 1 (or i). 
# Example: 
import re 
pattern = r"(...) (...) \1" 
match = re.match(pattern, "foo bar foo") 
if match: 
  print("Match 1") 
match = re.match(pattern, "foo bar bar") 
if match: 
  print("Match 2") # Match 1
#
# first of all: (...) will match any word composed of 3 characters (like 'foo' and 'bar') 
# group(1): 'foo' 
# group(2) :'bar' \1 matches the group(1) which is 'foo' and NOT 'bar' 


# Example:
# This program check if a string (6 characters long) is palindrome. "123321" OK, "123432" NO 
import re 
pattern = r"^(.)(.)(.)\3\2\1$" # No space between characters 
# ^, string starts with # $, string ends with 
# (.), group made of one single character 
# (.)(.)(.)\3\2\1, means "char1 char2 char3 char3 char2 char1" (no space between chars) 
match = re.match(pattern, "abccba") 
if match: 
  print("Match 1")                    #
match = re.match(pattern, "123432") 
if match: 
  print("Match 2") 
match = re.match(pattern, "8x--x8") 
if match:
  print("Match 3")                    # 
match = re.match(pattern, "O || O") 
if match: 
  print("Match 4")                    #
#


# Example:
import re 
pattern = r"(word) (test) \1 \2 \1" 
match = re.match(pattern, "word test word test word") 
if match: 
  print("Match 1")
  print(match.group())
  print(match.groups())   # Output: Match 1 word test word test word (‘word’, ‘test’) 
#

# any character + means one or more repetitions (.+) means any character which repeats one or more times is my understanding correct tiil here? 
# if so, I'm not able to comprehend what a \1 does to (.+) also in the exercise, if I enter \2 for example, it throws invalid expression errors
# Answer: 1. the space altered the meaning of that regex. 2. anything other than \1 is not valid because there's only 1 group in that pattern


# (.+) doesn't means repeats of a character, it means one or more characters, which is to say that all characters are regarded as a metacharacter ".".

# I'd learnt 'a+' means one or more occurence of a.But here there is . (a dot). 
# But i still have a doubt: 
import re 
pattern = r"(.+)(.+) \2" 
match = re.match(pattern, "word word word") 
if match: 
  print("Match 1") 
match = re.match(pattern, "?! ?!") 
if match: 
  print("Match 2") 
match = re.match(pattern, "abc cde") 
if match: 
  print("Match 3") #it print match1 and match3 
#


# This all makes more sense if you just capitalise the expectant results: 
import re 
pattern1 = r"(.+) (.+) (.+) \1" 
pattern2 = r"(.+) (.+) (.+) \2" 
pattern3 = r"(.+) (.+) (.+) \3" 
match = re.match(pattern1, "ABC bca cab ABC") 
if match: 
  print("Match 1") 
match = re.match(pattern2, "abc BCA cab BCA") 
if match: 
  print("Match 2") 
match = re.match(pattern3, "abc bca CAB CAB") 
if match: 
  print("Match 3")
#




https://www.sololearn.com/learning/1073/2479/5173/2
  




