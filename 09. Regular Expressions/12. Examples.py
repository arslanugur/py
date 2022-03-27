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

in case anybody wonders about this one: number of opening parentheses equals numer of groups.
  
.group(1) = (ab) .group(2) = (cdef) .group(3) = (def) .group(4) = (e) .group(5) = (g)

Group(0)= abcdefg Group(1)= ab Group(2)= cdef Group(3)= def Group(4)= e Group(5)= g


Why is group 0 not taken into Account? It is a group, after all, so when asking for the number of groups, it should be counted. The question was not "what is the highest group-index" -in which case 5 would be right, as pointed out above.

ab cdef def e g = 5groups

Why is group 0 not taken into Account? It is a group, after all, so when asking for the number of groups, it should be counted. The question was not "what is the highest group-index" -in which case 5 would be right, as pointed out above.

group(0) is same as group()

Group 0 isn't really a group, just like the Earth isn't a continent/country/city.

Too much if this coding instruction misses adding critical information the student needs to know in order to even understand the question let alone answer. it would be nice if the developers made the lessons looking at things from the viewpoint of someone who has no idea what's going on.














