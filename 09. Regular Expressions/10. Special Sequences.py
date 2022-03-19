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



# What would (abc|xyz)\1 match? --> "abc" or "xyz", followed by the same thing
# \1 means one or more like (.+)

# Example:
import re 
pattern = r"(abc|xyz)\1" 
if re.match(pattern, "abcabc"): 
  print("Match_abcabc")           # 
if re.match(pattern, "xyzxyz"): 
  print("Match_xyzxyz")           #
if re.match(pattern, "abc abc"):  # FAILURE 
  print("Match_abc abc") 
if re.match(pattern, "xyz xyz"):  # FAILURE 
  print("Match_xyz xyz") 
if re.match(pattern, "abcxyz"):   # FAILURE 
  print("Match_abcxyz") 
if re.match(pattern, "xyzabc"):   # FAILURE 
  print("Match_xyzabx")
#


# Example:
# Please note the subtle difference with and without a space in pattern. 
# Here there is no space in pattern .... 
import re 
pattern = r"(abc|xyz)\1" 
match = re.match(pattern, "abcabc") 
if match: 
  print("Match 1") # MATCHED 
match = re.match(pattern, "abc abc") 
if match:
  print ("Match 2") # NOT matched # and if we introduce a space before the slash in pattern ....
#
import re 
pattern = r"(abc|xyz) \1" 
match = re.match(pattern, "abcabc") 
if match: 
  print("Match 1") # NOT matched 
match = re.match(pattern, "abc abc") 
if match: 
  print("Match 2") # MATCHED 
#

# \1 was used for back reference in regex. That means it's going to find the same occurence based on its previous matching group (i.e. abc or xyz) 
pattern = r"(abc|xyz)\1"
re.match( pattern, "abcabc" ) ✅ 
re.match( pattern, "xyzxyz" ) ❎ 
re.match( pattern, "abcxyz" )
#


# Doesnt this look a bit ambiguous? (abc|xyz) - sort of looks like (abcyz) or or (abxyz) It (abc)|(xyz) Or is it (ab(c|x)yz)?? 
# How is that the ' | ' operator made to read everything proceeding it a single entity and everything after it a single character.

# Focus on the "followed by the same thing" part 
import re 
pattern = r"(abc|xyz) \1" 
if re.match(pattern, "abc abc"): 
  print("Match 1")
if re.match(pattern, "xyz xyz"):
  print ("Match 2") 
if re.match(pattern, "abc xyz"): 
  print ("Match 3") # O/P: Match 1 Match 2 There is no Match 3 because \1 refers to the first subexpression, not the first RegEx code pattern.
#

# Answer is "abc" or "xyz" plus the same thing of what is retained only once because of the "\1" function. if we had "\2" then it would be repeated twice.
# Because = /1 no reminder

# The backslash \1 as sequence 1 was not the main issue but that | as or and both of the chosen group must be followed by the same thing..
        
# Example:
import re 
pattern = r"(abc|xyz)\1" 
if re.match(pattern, "abcabc"): 
  print("Match_abcabc")         # 
if re.match(pattern, "xyzxyz"): 
  print("Match_xyzxyz")         #
if re.match(pattern, "abc abc"): # FAILURE 
  print("Match_abc abc") 
if re.match(pattern, "xyz xyz"): # FAILURE 
  print("Match_xyz xyz") 
if re.match(pattern, "abcxyz"): # FAILURE 
  print("Match_abcxyz") 
if re.match(pattern, "xyzabc"): # FAILURE 
  print("Match_xyzabx")
#              
              
# SECTION 2
# More useful special sequences are \d, \s, and \w.
# These match digits, whitespace, and word characters respectively.
# In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
# In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
# Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. 
# For instance, \D matches anything that isn't a digit.
# Example:
import re
pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")                    # 

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")
#
# (\D+\d) matches one or more non-digits followed by a digit.

# [ \t\n\r\f\v] are white spaces, but there are more in the source I posted. 
# \t = Matches a tab \u0009.                \t represents a horizontal tab
# \n = Matches a new line \u000A. 
# \r = Matches a carriage return \u000D.    \r is carriage return (usually combined with \n, like \r\n, to represent a newline in Windows)
# \f = Matches a form feed \u000C.          \f is formfeed (next page)
# \v = Matches a vertical tab \u000B.       \v represnts a vertical tab 
# source: http://regexlib.com/CheatSheet.aspx?AspxAutoDetectCookieSupport=1

# \d = digit          : \d stand for only digital patten with alone it self..like 1 
# \D = Non-digit      : \D stand for Non Digital patten like ABC,abc not matter Capital or Small letters
# \s = space          : \s stand for Space or empty values like match=re.match(patten," ") 
# \S = Non-space
# \w = word           : \w stand for everything Numbers,Alphabets but not for space or empty values
# \W = Non-word

# Whitespace literally means " " space. Blank space.


# Example:
import re 
pattern = r"(\D+\d)" 
match = re.match(pattern, "Hi 999!") 
if match: 
  print("Match 1", end=" ") 
  print(match.groups())
  
match = re.match(pattern, ",, 2, 456!") 
if match: 
  print("Match 2", end = " ") 
  print(match.groups()) 
match = re.match(pattern, "1,, 2, 456!") 
if match: 
  print("Match 3", end = " ") 
  print(match.groups()) 
match = re.match(pattern, " ! $?") 
if match: 
  print("Match 4", end = " ") 
  print(match.groups()) # Result: Match 1 ('Hi 9',) Match 2 (',, 2',) 
#

# Example:
pattern = r"(\D+\d)" 

match = re.match(pattern, "Hi 999!") 
if match: 
  print("Match 1") 
# It matches, because the string starts with a non-digit (\D - opposit of \d). 
# Since we used "match" function it also matches "!" at the end of the string since "match" checks only the beginning of the string. 
match = re.match(pattern, "1, 23, 456!") 
if match: 
  print("Match 2") # It doesn't match since the string doesn't start with non-digit (\D) 
  
match = re.match(pattern, " ! $?") 
if match: 
  print("Match 3") # It doesn't match since there's no any digit (\d) after non-digit sign (\D)
#


# Example:
import re 
pattern = r"(\D+\d)" 
match = re.match(pattern, "Hi 999!") 
if match: 
  print("Match 1") #
match = re.match(pattern, "1, 23, 456!") 
if match: 
  print("Match 2") 
match = re.match(pattern, " we 1 jffgghh mjhff") 
if match: 
  print("Match 3") #
#


# Example:
import re
pattern = r"(\D+\s+\d)" 
match = re.match(pattern, "Hi 999!") 
if match: 
  print("Match 1") # 
match = re.match(pattern , " Hi999! ") 
if match: 
  print("Match 2")
#


# Example:
import re 
text = input()
# use re.findall() with r"#\w+" as the regex 
pattern = r"#\w+" 
find = re.findall(pattern, text) 
n = 0 
if find: 
  for a in find: 
    print(find[n]) 
    n +=1
#

# What is the difference between this two patterns? 
pattern = r"(\D+\d)" 
pattern = r"^(\D+\d)"
# Both patterns have the same effect with re.match() but not with re.search().

# Which pattern would NOT match "123!456!"? --> (\D+\s?)+

# (1): Match eh? A pattern would MATCH "123!456!" only if part of this string (if not the entire string), 
# beginning right from the start, successfully meets the criteria outlined by the pattern. 
# So, let's actually go through each and every pattern given, and get our head around what they're all saying. 
# [1-6!] ~ a character class consisting of the numbers 1 to 6 (inclusive) as well the ! character. 
# So, this pattern would be MATCHED by a string only if the string's very FIRST character was either a 1-6 (inclusive) digit OR an exclamation mark ! character. 
# Clearly, this is true since the first character of the string is a digit between 1 and 6 (inclusive), 
# namely 1. Hence, the pattern "criteria" got successfully MATCHED by the string in question.
# (2): (\d*\W)+ ~ 1 or more occurrences OF 0 or more digits FOLLOWED by ★any★ character that's just NOT a word character. 
# Also, bare in mind that I THINK a word character is either any alphabetic lower case character a-z, any alphabetic UPPER case character A-Z, OR a digit 0-9. 
# Hence, for some character out there to qualify as NOT a word character, it simply must NOT be any of the 3 kinds of characters just mentioned. 
# For instance, ! is NOT a word character. 123!456! Just the 123! 
# bit alone successfully meets the criteria, as you have got 1 occurrence of 3 digits, namely 123, followed by the non-word character ! 
# Therefore, the pattern MATCHES "123!456!", since just by looking at the beginning of the string, 
# we clearly see the pattern criteria successfully met, since it holds true.
# (3): (\D+\s?)+ 💀💀💀💀💀💀💀💀💀💀 ~ 1 or more occurrences OF 1 or more NON-digits FOLLOWED by 0 or 1 whitespace characters. 
# This pattern clearly is NOT at all exhibited by the string "123!456!". 
# The string ★BEGINS★ off with a DIGIT, not a non-digit character. 
# Hence, the pattern criteria isn't met, and so the pattern 💀FAILS💀 to MATCH the string, making it being the answer that you're meant to choose in the question


# Actually, “123!456!” matches the entire string as the “+” allows “(\d*\W)(\d*\W)” for a pattern to work. 
# However, you would be right that only the string “123!123!” would work if the pattern was instead “(\d*\W)\1”.


# [1-6!] In above option It has all characters from 1 till 6 along with ! So it will match the pattern (\d*\W)+ 
# This expression says digits or not word characters more than one occurance for the example of 123!456! 
# It will match the pattern (\D+\w)+ 
# this expression says not digits and with word characters for above string pattern fails to match hence it is NOT a pattern match

# \d for digits \D for non-digits \s for white space... \S for non-white-space... 
# \w for word charecters respectively as matching accent words... 
# \W matchs for charecters (of words ) in away opposite to \w.. 
# we need non digits (using upper case \D ) and making white spaces ( using lowercase s as \s) in order NOT get that describtion of :- "123!456!"? 
# By this way, the correct answer is:- "(\D+\s?)+"


# 2. First i confused for (!). I think it’s a regular expression like others. That's simple but confusing. 
# Answer is : (\d*\W)+ I THINK a word character is either any alphabetic lower case character a-z, any alphabetic UPPER case character A-Z, OR a digit 0-9


# SECTION 3
# Additional special sequences are \A, \Z, and \b.
# The sequences \A and \Z match the beginning and end of a string, respectively.
# The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
# The sequence \B matches the empty string anywhere else.
# Example:
import re
pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print ("Match 1")                       #

match = re.search(pattern, "We s>cat<tered?")
if match:
    print ("Match 2")                       #

match = re.search(pattern, "We scattered.")
if match:
    print ("Match 3")
#
# \b(cat)\b" basically matches the word "cat" surrounded by word boundaries.


https://www.sololearn.com/learning/1073/2479/5175/1 comments

