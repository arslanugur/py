# Question:
# Which of these metacharacters isn't to do with repetition? --> \
# \ could only be a repetition if is used with digits 1 to 99. E.g \1 means one repetition, \2 means two repetition and so on

# The "\" character is to do with repetitions as \1 results in one repetition of the preceeding group. \2 results in two repetitions etc. 
# If what was meant was "Which character may result in repetitions without any other proceeding characters?" this should be specified in the question.

# For those looking for practical applications with regular expressions, Google has their own guide. 
# https://developers.google.com/edu/python/regular-expressions

# + means 1 or more repetitions * means 0 or more repetitions / is used for special predefined sequences; like words, whitespace, or digits

# Example:
import re #your code goes here 
user = input() 
find = re.findall("^[189]\d{7}$",user) 
if find: 
  print("Valid")
else: 
  print("Invalid")
#

# Example:
import re 
pattern = r"[1|8|9][0-9]{7}" 
number = input() 
check = re.match(pattern, number) 
if check: 
  print("Valid") 
else: 
  print("Invalid")
#


# Question: How many groups are in the regex (ab)(c(d(e)f))(g)? ---> 5        Count the number of opening brackets, 

# in case anybody wonders about this one: number of opening parentheses equals numer of groups.
  
"""
 group(0) = abcdefg     # group(0) is same as group()
.group(1) = (ab) 
.group(2) = (cdef) 
.group(3) = (def) 
.group(4) = (e) 
.group(5) = (g)
"""

# Why is group 0 not taken into Account? 
# It is a group, after all, so when asking for the number of groups, it should be counted. 
# The question was not "what is the highest group-index" -in which case 5 would be right, as pointed out above.

# Why is group 0 not taken into account. 
# It is a group, after all, so when asking for the number of groups, it should be counted. 
# The question was not "what is the highest group-index" -in which case 5 would be right, as pointed out above.
# Group 0 isn't really a group, just like the Earth isn't a continent/country/city.


# Question: Which regex would match "email@domain.com"? ---> \w+@domain.com
# That's because to get '.' you must use '\.' in regexp 
# The dot stands for any character including the dot itself.

# \w matches word character In ASCII mode equivalent to [0-9], [ \t\n\r\f\v], 
# and [a-zA-Z0-9_] + matches one or more repetition then \w+ means one or more repetition of word character

# the regex for email follows this pattern 
# pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)" = string should contain a word (with dots and dashes allowed), 
# followed by the @ sign, then another similar word, then a dot and another word (thus creating 3 groups). 
# from the question email@domain.com we can already cross out the option with [0-9]. 
# based on the pattern, email = [\w\.-]+ {of the first group} 
# the option of email/@(domain\w)+ to me only constitutes the second group 
# {of course taking into account that the code is correct to begin with} and leaves out the ".com" part. 
# Hence I was able to think in this way to get the answer: \w+@domain.com

# Question: Which string would be watched by "[01]+0$"? ---> 10101111001010         # end with "0"
# Because you should have a zero at the end of the string
# Which string would be MATCHED by "[01]+0$"? 
# Well, pretty much ANY string that successfully meets the following criteria. 
# String BEGINS with: 1 or more occurrences OF ANY digit among 0 or 1 String ENDS with 0

# $ means ending of the string has to match, in this case it hss to end in 0. There is only one answer that ends with a 0.
# Let's break it down:- [01]+0$ ✅ [01]+ : One or more occurences of 0 and 1 continuously ✅ 0$ : Ends with a 0
# 0$ means you should have a zero at the end of the string.

# A zero should be at the end of the string and it should contain one or more 1's and 0's

# Question: What would be watched by "(4{5,6})\1"? ---> 10 or 12 fours
# 4{5,6} means "4 multiply by 5 or 6", 
# then \1 means "repeat group 1", therefore we should match either 5*2 or 6*2 characters of "4", 
# I.e. 4444444444 or 444444444444 (10 or 12 "4" in the row)

"""
4{5}\0 44444 
4{5}\1 44444 
total = 10 
4{6}\0 444444 
4{6}\1 444444 
total=12
"""

# I've often more syntax understanding trouble than the logical/concepts by their own, 
# if i say 4* 5 or 6 then "followed by same group so 10, 12 as result, is my reformulation right? 

# Repeat not multiply, as the definition we can explain 4{5,6} 
# as "between 5 and 6 repetitions of 4" \1 mean repeat group 1 
# and we have 5 to 6 of 4 plus \1 (repeat) = double number of 4s = 10 to 12 4s

# Repeat the number 4 either 5 or 6 times: (44444)\1 or (4444444)\1 then repeat the group 1 time...

# We are given a pattern r"4{5,6}\1" !! breaking this up into parts.. 
# 4{5,6} - This means 4 that has to be repeated 5 or 6 times continuously.. 
# i.e. 44444 ('4' * 5) or 444444 ('4' * 6) \1 represents the repetitions of the first group.. 
# that makes it -> twice of ( '4' * 5 ) or ( '4' * 6 ) 
# i.e. 4444444444 (10 fours) or 444444444444 (12 fours) thus it wud match, 10 or 12 fours

# 4{5, 6} Take 4 five times -> 44444 Or Take 4 six times -> 444444 4{5, 6} \1 Take 4 five times, 
# then repeat -> 4444444444 Or Take 4 six times, 
# then repeat -> 444444444444 Match must be with: 4444444444 Or 444444444444

# Break it down () is a group 4 means it needs to be the character "4" {5,6} means it needs to repeat the previous character this many time. 
# In this example 5 or 6 times. So 44444 or 444444 \1 means it must match the first group exactly. 
# So if it was 5 "4"s it must be 5 more (10 total). Or if it was 6 "4"s it now has to be 12 total

# Example:
tel = str(input()) 
pattern = r"^[9,8,1]{1,1}[0-9]{7,7}$" 
if re.match(pattern, tel): 
  print("Valid") 
else:
  print("Invalid")
#


# Example: Test Pattern -- any group of fours from 10 on works. So also 11 or 13 or more fours works. 
import re

pattern = r"(4{5,6})\1"

print(pattern)

match = re.match(pattern, "444444444") #  9 fours
if match:
    print("Match  1", match.group())  # No output

match = re.match(pattern, "4444444444") #  10 fours
if match:
    print("Match  2", match.group())  # Match
    
match = re.match(pattern, "44444444444") #  11 fours
if match:
    print("Match  3", match.group())  # Match
    
match = re.match(pattern, "444444444444") #  12 fours
if match:
    print("Match  4", match.group())  # Match
    
match = re.match(pattern, "4444444444444") #  13 fours
if match:
    print("Match  5", match.group())  # Match
    
match = re.match(pattern, "44444444444444444444") #  20 fours
if match:
    print("Match  6", match.group())  # Match
    
    
pattern = r"(4{5,6}) \1"  # added a space before \1

print(pattern)

match = re.match(pattern, "4444444444") #  10 fours
if match:
    print("Match  7", match.group())  # No output

match = re.match(pattern, "44444 4444") #  5 + 4 fours
if match:
    print("Match  8", match.group())  # No output

match = re.match(pattern, "44444 44444") #  5 + 5 fours
if match:
    print("Match  9", match.group())  # Match

match = re.match(pattern, "44444 444444") #  5 + 6 fours
if match:
    print("Match 10", match.group())  # Match

match = re.match(pattern, "444444 44444") #  6 + 5 fours
if match:
    print("Match 11", match.group())  # No output

match = re.match(pattern, "444444 444444") #  6 + 6 fours
if match:
    print("Match 12", match.group())  # Match

match = re.match(pattern, "44444 444444444444 4444") #  5 + 512 + 4 fours
if match:
    print("Match 13", match.group())  # Match
    
match = re.match(pattern, "444444 44444444 4444444444") #  6 + 8 + 10 fours
if match:
    print("Match 14", match.group())  # Match
#


