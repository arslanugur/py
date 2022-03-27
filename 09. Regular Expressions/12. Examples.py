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


# Question: How many groups are in the regex (ab)(a(d(e)f))(g)? ---> 5























