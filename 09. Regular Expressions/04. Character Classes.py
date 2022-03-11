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

# Example:
import re 
pattern = r"[A-Z][A-Z][0-9]" 
search1 = re.search(pattern, "LS8") 
search2 = re.search(pattern, "E3") 
search3 = re.search(pattern, "AC130") 
if search1: 
    print("Match 1", search1.group()) 
if search2: 
    print("Match 2", search2.group()) 
if search3: 
    print("Match 3", search3.group())
# you can validate an email address by using this code. and ofc you can modify it according to your need. 
import re 
email = r"[a-z A-Z 0-9]+[@]+[a-z]+[.]+[a-z]" 
if re.search(email, "Bilal123@gmail.com"): 
    print("Valid Email Address") 
else: 
    print("Invalid email address! try again")
#

# Example:
import re 
pattern = r"[A-Z][a-z][0-9]" 
if re.search(pattern, "LS8"): 
    print("Match 1") 
if re.search(pattern, "E3"): 
    print("Match 2") 
if re.search(pattern, "Dg1"): 
    print("Match 3")            #
#

# Example:
import re 
password = input("Enter your password: ") 
isStrong = re.search(r"[A-Z]", password); 
isStrong = isStrong and re.search(r"[a-z]", password) 
isStrong = isStrong and re.search(r"[0-9]", password) 
if isStrong: 
    print("Your password is strong.") 
else: 
    print("Your password is too weak!") 
# Enter your password: aa5                      Your password is too weak! 
# Enter your password: SECRETpassword1234       Your password is strong.

# So the match can be anywhere in str and not just the first 3 chars 
import re 
pattern = r"[A-Z][a-z][0-9]" 
if re.search(pattern, "LS8"): 
    print("Match 1") 
if re.search(pattern, "Re3"): 
    print("Match 2") 
if re.search(pattern, "1abRe3"): 
    print("Match 3") 
# nxt pge example, removed ending square bracket and still came up with output Match 1 Match 2 Match 3 why didn't it error out with typo? 
# Note missing end bracket after 5 
import re 
pattern = r"[1-5[0-9]" 
if re.search(pattern, "59"): 
    print("Match 1") 
if re.search(pattern, "5900000"): 
    print("Match 2") 
if re.search(pattern, "123459"): 
    print("Match 3")
#

# What would [1-5][0-9] match? -- Any two-digit number from 10 to 59

# The answer to this is a little tricky but easy when you get it The first letter is from 1-5 
# And the second one from 0-9 (the 0 can represent numbers like 10/20/30/40/50) Not above 50 because the highest first digit possible is 5 

# [1-5] Min value:1 Max value:5 [0-9] Min value:0 Max value:9 Valid number range: 10 to 59

# Example:
import re 
pattern = r"[10-59]" 
if re.search(pattern, "62"): 
    print("Match") # OUTPUT: Match
#

# [1-5] means 1 2 3 4 5 [0-9] means 0 1 2 3 4 5 6 7 8 9 So answer is any two digits number # from 10 to 59

# [1-5][0-9] Number first digit 1 to 5 and second digit is 0 to 9 means 10,11,......,19 20,21,...,28,29 ...... 50,51,...,58,59 so it means 10-59 numbers

# Example:
import re 
pattern = r"[1-5][0-9]" 
if re.search(pattern, "10"): 
    print("Match 1") 
if re.search(pattern, "59"): 
    print("Match 2") 
if re.search(pattern, "1100"): 
    print("Match 3") 
#
# The output of this code is Match1 Match2 Match3 
# So I would like to conclude that the range is not fixed our first 2 digits matches with criteria, 
# the range can be anything for e g. 1100, 5917, 4809 etc. 



# SECTION 3
# Place a ^ at the start of a character class to invert it.
# This causes it to match any character other than the ones included.
# Other metacharacters such as $ and ., have no meaning within character classes.
# The metacharacter ^ has no meaning unless it is the first character in a class.
# Example:
import re
pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet"):
    print("Match 1")                        #

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")                        #

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")
#

# The pattern [^A-Z] excludes uppercase strings.
# Note, that the ^ should be inside the brackets to invert the character class.

# [a-z]: 1 lower case letter 
# [A-Z]: 1 upper case letter 
# [A-Z]{3}: 3 consecutive upper case letters 
# [A-Z]{3}[a-z][A-Z]{3}: 3 upper case letters + 1 lower case letter + 3 upper case letters 
# [^A-Z]: any character BUT an upper case letter 
# [^A-Z]+: at least one such character 
# [^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+: something else before and after our patter(AAAbCCC) 
# so there's no more than 3 consecutive upper case letters on each side

# Example:
import re 
pattern = r"[^A-Z]+" 
if re.search(pattern, "THaNK YoU!") 
print(Match)    #


# Example: what if I invert a lowercase alphabet? 
import re 
pattern = r"[^a-z]" 
if re.search(pattern, "this is all quiet"): 
    print("Match 1") 
if re.search(pattern, "AbCdEfG123"): 
    print("Match 2") 
if re.search(pattern, "THISISALLSHOUTING"): 
    print("Match 3")    # OUTPUT: >>> Match 1 Match 2 Match 3 Why does it match all? I thought it will only match the "Match 2" and "Match 3"
#

# [^A-Z] triggered by anything other than upper case letters. 
# This includes line breaks (\n) and other escape characters: 
import re 
pattern = r"[^A-Z]" 
str = "ASDF\nGFFG" 
match = re.search(pattern, str) 
if match: 
    print(repr("Match: {}".format(match.group()))) 
else: 
    print("No match") # output: Match: \n
#            

# Example: to show how ^ works: 
import re 
pattern = r"[^(0-9)]" 
if re.search(pattern, input("please enter your age: ")): 
    print("you are child, welcome!") 
else: 
    print("you are too old!; you are not allowed here")
#

# [^A-Z] means any char except A-Z So it "Match 1" because all are small char at "this is all quiet" and "Match 2" 
# because we have some numbers at this strange and some small char "AbCdEfG123" and not "Match 3" 
# because all in capital letter with this string THISISALLSHOUTING"
                        
# For those who confusing about the result of Match 1 and Match 2, 
# The ^A-Z is work like moving on target string to check the first character char by char, 
# if the whole string are in upper case it will return false and skip it like in Match 3: "THISISALLSHOUTING", 
# otherwise once it found any first char except upper case like a-z or 0-9 it will match and return true! 
# like in Match 1: "this is all quiet" here the string is already in lower case as well as the first char not upper, 
# and in Match 2: "AbCdEfG123" the string is in upper case but the first chart after upper char contain number 0-9 which is not in A-Z.

# Example: To match strings that are not entirely composed of digits
import re 
pattern = r"[^0-9]"
m = re.search(pattern, "Hi there!")

# In case anyone else has trouble with the logic here: 
# The ^ inverts the class, not the statement of the regex. 
# The class "zero to nine" becomes the class "something other than zero to nine". 
# Thus, "contains zero to nine" becomes "contains something other than zero to nine."
    

