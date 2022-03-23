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
# So, this pattern would be MATCHED by a string only if the string's very FIRST character was either a 1-6 (inclusive) digit OR an exclamation mark ! character
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
# Hence, the pattern criteria isn't met, and so the pattern 💀FAILS💀 to MATCH the string, 
# making it being the answer that you're meant to choose in the question


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
# The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. 
# Informally, it represents the boundary between words.
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

# Explanation:
# Explanation of \A \Z \b \A is an anchor that says "the string starts here" 
# so in other words no characters may occur before \A \Z is an anchor that says "the string ends here" 
# so in other words no characters may occur after \Z \b matches 1 or more spaces and 0 or more letters (words). 
# So in other words there must be at least 1 word to the left of \b and at least 1 word to the right of \b.

# Also, would it be accurate to state that using \B is equivalent to using re.search? 
# Example, are these the same (assume that the text your searching is "whateveryourtextishere"? 
pattern = r"\B(cat)\B" 
re.search(“cat”,"whateveryourtextishere")

# The “+” is unnecessary in the pattern r”\b+” as if \b matches, any number of empty string boundaries will match (basically \b\b\b\b will match too

# Example:
pattern = r"\b(cat)\b" 
match = re.search(pattern, "cat") 
# It still matches! There’s no word to the left and right of \b


# You haven't described what "empty string" is (and what it is NOT). 
# That's why the following question is confusing to some learners. 
# You should've written something like '\b itself doesn't match "c", "t", or spaces. 
# It matches an imaginary point between \w and \W. 
# Do you remember ^ ? It matches the beginning position, rather than the first character. \b is similar to that.'

# I've got the following off somewhere else. \b matches a word boundary. 
# That is defined as the transition from a word character to a non-word character, or vice versa. 
# It's a zero-width match (just like \A and\Z and various other constructs) which means it matches the gap between two characters.
# (1): I suspect the following. 
# WORD CHARACTERS are represented by [a-zA-Z0-9], so includes all alphabetic letters, BOTH UPPER and lower case, as well as all 0-9 digits.
# \b = WORD CHARACTER BOUNDARY, i.e. the space/gap character that you've got just AFTER some WORD CHARACTER and just before whatever you're interested in. 
# So, for example, consider the following code. Observe how for the FIRST \b, the word character in all cases is the e from the word "The". 
# Also, the corresponding space/gap characters for the FIRST \b are, in order: white space, ,, /, *, ★, <, ≤ and lastly }. 
# However, for the SECOND \b, the word character in all cases is the c from the word "cur". 
# Additionally, the corresponding space/gap characters for the SECOND \b are, in order: white space, -, ., †, >, ≥, { and finally !.
# (2): import re pattern = r"\b(huri)\b" match = re.search(pattern, "The huri cur") if match: print("Match 1") 
# match = re.search(pattern, "The,huri-cur") if match: print("Match 2") match = re.search(pattern, "The/huri.cur") 
# if match: print("Match 3") match = re.search(pattern, "The*huri†cur") if match: print("Match 4") match = re.search(pattern, "The★huri>cur") 
# if match: print("Match 5") match = re.search(pattern, "The<huri≥cur") if match: print("Match 6") match = re.search(pattern, "The≤huri{cur") 
# if match: print("Match 7") match = re.search(pattern, "The}huri!cur") if match: print("Match 8") 
# OUTPUT: >>> Match 1 Match 2 Match 3 Match 4 Match 5 Match 6 Match 7 Match 8 >>>

# Example:
import re 
pattern = r"\b(huri)\b" 
match = re.search(pattern, "The huri cur") 
if match: 
  print("Match 1") 
match = re.search(pattern, "The,huri-cur") 
if match: 
  print("Match 2") 
match = re.search(pattern, "The/huri.cur") 
if match: 
  print("Match 3") 
match = re.search(pattern, "The*huri†cur") 
if match: 
  print("Match 4") 
match = re.search(pattern, "The★huri>cur") 
if match: 
  print("Match 5") 
match = re.search(pattern, "The<huri≥cur") 
if match: 
  print("Match 6") 
match = re.search(pattern, "The≤huri5{cur") 
if match: 
  print("Match 7") 
match = re.search(pattern, "The}huri!cur") 
if match: 
  print("Match 8")
#
match = re.search(pattern, "The _huri_ cur") 
if match: 
  print("Match 9")                            # No match!
#

# Imagine if we wrote English without spaces or punctuation (Ancient Sanskrit was written that way). 
# So one writes "boyijustwokeupandiamsohungrydoistillhavebread" Your brain will see an implied /b 15 times. 
# The spaces and punctuation are bonuses that make it easier to read but they're not really the word boundaries. 
# Python allows you to break down both levels in regex depending on what's more effective to your needs.
  
# \A and \Z differs from ^ and $ only in multiline mode 
string = 'my\nname\nis\njmin' 
pattern1=re.compile('\A(name)\Z', re.MULTILINE) 
pattern2=re.compile('^(name)$', re.MULTILINE) 
re.search(pattern1, string) None 
re.search(pattern2, string).group() 'name'

# Simple Explanation: 
# \b(cat)\b = ( any non-alphanumeric value )cat(any non-alphanumeric value) alphanumeric numbers consists of characters [A-Z|a-z] and integers. 
# you have to put any other value at the end and begining of string to match it with regex. 
# e.g. 
# \b(cat)\b = " cat " # matched 
# \b(cat)\b = "\cat\" # matched 
# \b(cat)\b = "*cat^" ....... etc 
# for \B : \B(cat)\B = (any alpha-numeric value)cat(any alpha-numeric value) e.g. \B(cat)\B = "advocate" # matched

# Is there a difference between '^' and '\A' (also between '$' and '\Z')?!

# ^ can match at the start of the string and after each line break. 
# \A only ever matches at the start of the string $ can match at the end of the string and before each line break. 
# \Z only ever matches at the end of the string. - Stack Overflow
  
# First off, these sequences are "zero-width" sequences, meaning all are not looking for a specific character in the string, 
# but the boundary between two characters, or a character and a boundary of the string. 
# This is what is meant by matching an empty string. \A matches at the start of the string. 
# This differs from ^ because ^ also matches to the zero-width space just after the newline character in multi-line mode (i.e. the start of a new line). 
# \A only matches to the start of the string as a whole. 
# \Z matches at the end of the string and differs from $ in the same way \A differs from ^. 
# \b matches between a word character (anything in \w) and a non-word character (anything in \W), 
# or between a word character and the start or end of the string. \B is the opposite of \b. 
# It matches anywhere a word character (\w) is on both sides of the boundary, a non-word character (\W) is on both sides of the boundary, 
# or the boundary is between a non-word character and the start or end of the string.

# Clearly explain the /b regex: 
from re import * 
a = [' cat ', 'cat ', 'scat ', 'scatk', '^cati', 'icat*', '*cat()', ' this is nice cat*'] 
b = r"\b(cat)\b" 
for i in a: 
  if search(b, i): 
    print("This works: ", i) 
  else: 
    print("This doesn't work: ", i) 
# Output: 
# This works: cat 
# This works: cat 
# This doesn't work: scat 
# This doesn't work: scatk 
# This doesn't work: ^cati 
# This doesn't work: icat* 
# This works: *cat() 
# This works: this is nice cat*

# "\b(cat)\b" basically matches the word "cat" surrounded by word boundaries. This was confusing me at first, but now I understand. 
# Here are some more strings that will return a match: "the cat in the hat" "con-cat-enate" "C:¥cat¥stuff" "cat" "peg+cat" "cat 9 cables" 
# For comparison, here are some strings that will NOT return a match: "The Cat in the Hat" "concatenate" "C:¥catstuff" "Cat" "pegpluscat" "cat9 cables" 
# In conclusion, a word boundary is any non-alphanumeric character, such as a symbol or space, or the beginning or end of the string. 
# And in this case the string to be matched (cat) is lowercase, so we need to fulfill that criteria too. 
# By this logic we should be able to convert a string to all lowercase before it is evaluated and get a match that way too: 
match = re.search(pattern, "Cat".lower()) # Yep, this also works!

# The only difference I can notice between \b and \W is that a pattern like r"\b(cat)\b" matches the string "cat", while r"\W(cat)\W" don't, 
# if more differences do exist, please someone clarify this to me! 
# And I can't see any differences between \B and \w, please someone help me, is something line-based like the difference between \A and ^? 
# All the ambiguity from this entire Regex section have came into this very lesson!
# Answer:
# Make no mistake, \w and \W are much different from \b and \B! 
# \w and \W represent characters, while \b and \B represent the "zero-width space" between two characters in a string. 
# To answer your first question, \W is looking for a specific character, 
# while \b is looking for the boundary between two characters or between a character and the edge of the string, 
# making it a "zero-width" sequence (this is what empty string refers to). 
# \b is actually looking for the zero-width space between a \W character and a \w character, 
# as well as the space between a \w and the start or end of the string. 
# The fact it matches "cat" is because it can match the start or end of a string next to a \w character. 
# \B is looking for the zero-width space between a \W and a \W or between a \w and a \w, as well as between a \W and the start or end of a string.



# Which pattern would match 'SPAM!' in a search? ---> \AS...\b.\Z
# If I modify \ASPAM\Z to \ASPAM!\Z or \ASPAM\b.\Z , it will match 'SPAM!', am I right ?
import re 
pattern = r"\ASPAM\b.\Z" 
match = re.search(pattern, "SPAM!") 
if match: 
  print("Match 1")
#  

# The string 'SPAM!' would be MATCHED by the pattern \AS...\b.\Z 
# \b matches a word boundary. That is defined as the transition from a word character to a non-word character, or vice versa. 
# It's a zero-width match (just like \A and\Z and various other constructs) which means it matches the gap between two characters. 
# M is a word character, and ! is not a word character, so the gap between them is a word break, which \b matches. The final . matches the !.

# I think it helps to translate \b as "if followed by a character other than [a-zA-Z0-9_]", 
# and to translate \B as "if followed by a character in the set [a-zA-Z0-9_]" 
# So "e\B" would match "'e', if followed by a character in the set [a-zA-Z0-9]"
# So would match 'e9' but not 'e!' (although only 'e' would be returned as the actual match)

# \ASPAM\Z - \A starting and \Z ending.. so it shud start with 'S', end with 'M' and shud have 'PA' in b/w. 
# Our string has '!' at the end. So this fails.. 'SP\AM!\Z' - \A marks starts of the string.. so it shud start with M, since M is next to \A. 
# \Z marks ending and it shud end with '!'
# This fails though the our string matches the latter but not the former. '\AS...\b.\Z' - \A marks start and it shud start with S. 
# Followed by 3 dots (.), which matches with anything other than newline '\n'. 
# \b allows any char other than words or letters, i,e. spaces and special characters allowed which matches with '!'. 
# \Z marks end and it has a dot before it, that allows anything at the end other than newline. So its "\AS...\b.\Z" 

# Explanation...... \ASPAM\Z - \A starting and \Z ending.. so it shall start with 'S', end with 'M' and as our string has '!' at the end. 
# So this fails.. Because it doesn't match the end. SP\AM!\Z- \A starting and \Z ending ..... 
# We see that our wordd begins with SP which matches but \A means that it shall start with M but we normally know our string starts with S. 
# So it not correct. But for the case of \z its correct as our string ends with ! \AS...\b.\Z.... 
# Our string starts with S which is true and later ends with a non character ! 


# It's an example to expain why the \A,\Z is needed (the search() method is not start from beginning but anywhere, 
# so if you wang to start from beginning,you need \A) ,and the difference between the methods: group and groups, search and match.
# .\b. that means the two dot(.) between are differern type (word,non-word)
import re 
pattern = r"\AS...\b.\Z" 
match = re.search(pattern, "abcSPAM!") 
if match: 
  print("Match 1") 
  print(match.groups()) 
  print(match.group(0)) 
match = re.search(pattern, "SPAM!") 
if match: 
  print("Match 2") 
  print(match.groups()) 
  print(match.group(0))
pattern2 = r"S...\b." 
match = re.search(pattern2, "abcSPAM!") 
if match: 
  print("Match 3") 
  print(match.groups()) 
  print(match.group(0)) 
match = re.match(pattern2, "abcSPAM!") 
if match: 
  print("Match 4") 
  print(match.groups())
  print(match.group(0))
match = re.match(pattern, "SPAM!") 
if match: 
  print("Match 5")
  print(match.groups()) 
  print(match.group(0))
#          



