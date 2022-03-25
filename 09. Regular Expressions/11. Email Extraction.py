# SECTION 1
# To demonstrate a sample usage of regular expressions, lets create a program to extract email addresses from a string.
# Suppose we have a text that contains an email address: 
str = "Please contact info@gmail.com for assistance"

# Our goal is to extract the substring "info@gmail.com".
# A basic email address consists of a word and may include dots or dashes. 
# This is followed by the @ sign and the domain name (the name, a dot, and the domain name suffix).
# This is the basis for building our regular expression. 
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

# [\w\.-]+ matches one or more word character, dot or dash.
# The regex above says that the string should contain a word (with dots and dashes allowed), followed by the @ sign, 
# then another similar word, then a dot and another word. 

# Our regex contains three groups:
# 1 - first part of the email address.
# 2 - domain name without the suffix.
# 3 - the domain suffix.

# While the given pattern works it actually isn't correct because the domain suffix (the word after the last period) can't contain an internal period. 
# So the [\w\.]+ at the end of the pattern should really be just \w+

# Better to exclude '\.' from group 2: 
import re 
pattern1 = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)" 
pattern2 = r"([\w\.-]+)@([\w-]+)(\.[\w\.]+)" 
str = "Please contact info-1.5@gmail_42.co.uk for assistance" 
match = re.search(pattern1, str) 
if match: 
  print(match.groups()) # ('info-1.5','sololearn_42.co','.uk') 
match = re.search(pattern2, str) 
if match: 
  print(match.groups()) # ('info-1.5','sololearn_42','.co.uk')
#


# All your examples already match with the first group after the @: ([\w\.-]+) It already says that you can have more dots. 
# The group at the end (\.[\w\.]+) just makes sure that there is a dot. 
# Following does not match: test@de and the last group has [\w\.] and not only [\w] because following domain is also allowed: test@co.uk.com. 
# A dot at the end of a domain name is technically completely ok.

# Example: Regex for email extraction
import re

pattern = r"([\w.-]+)@([\w.-]+)"
str = "Please contact info@gmail.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())

pattern = r"([\S]+)@([\S]+)"
str = "Please contact info@gmail.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())

r"([\w\.-]+)@([\w\.-]+)"
r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
# 


# Please don't ever use a regular expression to match e-mailaddresses. 
# Just for laughs; this pattern matches 99,9% of all valid e-mail syntaxes; 
"""
(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")
@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]) 
"""
# Read more at for example https://davidcel.is/posts/stop-validating-email-addresses-with-regex/

# Example:
import re 
pattern = r"([\w\S]+)@([\w\S]+)" 
str = "Please contact i-n._fo@gmail.com.au for assistance" 
match = re.search(pattern, str) 
if match: 
  print(match.group()) # output: i-n._fo@gmail.com.au
#

# True regex for matching email https://i.stack.imgur.com/SrUwP.png

# The RFC allows also + in the address before @. Programmers ignoring this has caused me problems quite often.

# https://www.regular-expressions.info/email.html

# Example: re to check date
import re

pattern = r"\d+\-\d+\-\d+"
str = "Please submit the project by 5-2-2020"

match = re.search(pattern, str)
if match:
    print(match.group())
#


# Example: '''The program uses a regular expression to check if the input value is a valid Roman number.'''
import re

pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

def main():
    nr = input()
    if re.search(pattern,nr.upper()):
        print('This is a Roman number.')
    else:
        print('This is not a Roman number.')

if __name__ == "__main__":
    main()
#

# Question: # Which of these better be done with regular expressions, rather than string methods? --> Checking to see if a string sontains a date
# There are some situations where regex are best suited to extract / search / find in a text. 
# String methods are for quick modifications / usage of strings (for example "lower" to convert a text into lowercase) 
# Now the question: They are asking what to use (regex or string methods) to perform the following operations and which operation gets regex into your mind. 
# Now the operations: 
# 1) Splitting a string - this is not for regex (it is easier with string methods) 
# 2) Checking a character in a string - Can be done easily using "in" since a string can be treated as list of characters 
# 3) Checking a "date" in a string - 
#    Here date is just an example. Date is something which contains numbers, hyphens or slashes and words. 
# This is something which should be searched by defining a "pattern". ( Just like finding email in last example). 
# Using regex is very much needed here. So this is the answer for the question.

# Example:
import re # Let's say you have a pattern that records today's date as follows, "Today's Date: 00/00/0000". 
# And this changes daily. Our pattern is; (I have used groups) 
r"(Today's Date: [\d+]+)/([\w.-]+)/(\d+)" 
 
TodaysDate = "Today's Date: 01/03/2019" # So lets say today we have; "Today's Date: 01/03/2019"; (I have as a variable)
if re.search(r"(Today's Date: ([\d+]+)/([\d+]+)/([\d+]+))", TodaysDate): 
  print("Match 1") 
else: 
  print("Not a match.")
# 


# SECTION 2
# Putting it all together: 
import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@gmail.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())      
#

# In case the string contains multiple email addresses, we could use the re.findall method instead of re.search, to extract all email addresses.

# The regex in this example is for demonstration purposes only.
# A much more complex regex is required to fully validate an email address.
# https://regex101.com/#python

# Use re.sub() function to change the host address. 
import re 
str = "Please contact info@gmail.com for assistance" 
pattern = r"([\w\.-]+)@([\w\.-]+)([\w\.-]+)" 
replace = r"\1@DataCamp.com" 
sub = re.sub(pattern,replace,str) 
print(sub)

# https://davidcel.is/posts/stop-validating-email-addresses-with-regex/

# \. means to match the "." itself and needs the backslash to tell Python you want the "." not .... as in check to see if any character matches. 
# so \.- means zero or one matches of the "." character after the @

# If a special character is added to the name before the email address it concenates the email address instead of ignoring the email address. 
import re 
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)" 
str = "Please contact inf$o@gmail.com for assistance" 
match = re.search(pattern, str) 
if match: 
  print(match.group())
#

# Example: for several email validation could be used this: 
import re 
pattern = r"[\w\.-]+@[\w\.-]+\.[\w\.]+" 
str = "Please contact info@gmail.co.com or test@mail.com for assistance" 
match = re.findall(pattern, str) 
if match: 
  print(match) # ['info@sololearn.co.com', 'test@mail.com'] 
#
# if you don't remove parentheses in regexp pattern the out ut list will look like..  [('info', 'sololearn.co', '.com'), ('test', 'mail', '.com')]
    
# http://emailregex.com/

# a simple python code to check a string that contains severals email addresses, then print a list of valid email addresses. 
import re 
check_text = 'Enter your email list here to check: 123@gmail.com, .@..., some.one@erricsson.com, a#^*()@2d.c0m' 
def email_extractor(text): 
  pattern = '(\w)+([\.-](\w+))*@(\w)+([\.-]\w)*(\.(\w+))' 
  email_list = [] 
  find_iter = re.finditer(pattern, text) 
  try: 
    while True: 
      n = next(find_iter) 
      email_list.append(n.group()) 
  except Exception: 
    pass 
    return email_list
def main(): 
  inputtext = check_text result = email_extractor(inputtext) 
  print(result)
  
if __name__ == '__main__': 
main()
#


# Example: Password Validator with Regex
import re
password = input()
print('Strong')
if len(password) >= 7 and len(re.findall('[!@#\$%&*]', password)) >= 2 and len(re.findall('[0-9]', password)) >= 2 
else:
  print('Weak')
#

# Question:
# In our example, why is the dot character preceded by a backslash? --> to treat it as a character

# The example contains 4 dots The 1st, 2nd and 4th dot are inside a character class [ ] so they need NO escape. 
# Only the 3rd needs the \. escape sequence because it shall match literally (and not as special character)

# a.bc.d@sub.domain.net.com If dot has no escape, you are admitting any invalid email char like '&' or additional '@' as "a.bc@d@sub.domain&net.com" 
# And what you want is accept literally a dot character following the word.

# My notes say that: "Other metacharacters such as $ and . (dot) have no special meaning within character classes. 
# The metacharacter ^ has no meaning unless it is the first character in a class. 
# A backslash before . (dot) would have been needed if the regex used parentheses (group).

# Without the backslash dot is interpreted as no or one any character. Backslash tells it's a character dot

# if [\.] = [.] why if we remove " \ " in " ." we do not have the same result? 
import re 
pattern = r"([\w.-]+)@([\w.-]+)(.[\w.]+)" 
str = "Please contact info@gmail.com or han.solo@rebells.org and also amatias16@alustudent.com for assistance" 
match = re.findall(pattern, str) 
if match: 
  for Jesus in match: 
    print(Jesus[0] + "@" + Jesus[1] + Jesus[2]) # info@gmail.com or han.solo@rebells.org and amatias16@alustudent.com for

# Backslash character can be used to escape the metacharacter in the pattern to treat is as a literal.     






