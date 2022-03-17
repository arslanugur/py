# lesson should be before the metacharacters
# SECTION 1
# A group can be created by surrounding part of a regular expression with parentheses.
# This means that a group can be given as an argument to metacharacters such as * and ?.
# Example:
import re
pattern = r"egg(spam)*"                 # The string has to start "egg" and be followed by "spam" zero or more times

if re.match(pattern, "egg"):
    print("Match 1")  #

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")  #

if re.match(pattern, "spam"):
    print("Match 3")
#

# (spam) represents a group in the example pattern shown above. 

import re 
pattern = r"egg(spam)*" 
if re.search(pattern, "egg"): 
    print("Match 1") #
if re.findall(pattern, "eggspamspamspamegg"): 
    print("Match 2") #
if re.finditer(pattern, "spam"): 
    print("Match 3") #
#

# What would '([^aeiou][aeiou][^aeiou])+' match? -- One or more repetitions of a non-vowel, a vowel and a non-vowel

# It would have been more accurate 
# to say it would match one or more repetitions of a [non vowel or an "uppercase" vowel], [a "lower case" vowel], 
# and again [a non-vowel or an "uppercase" vowel].

# "Nothing" will match. "Not", "hin" match the pattern.

# the ^ means anything else apart from what is stated in that particular group, 
# on the other hand the meta character"+" means one or more repetitions,
# therefore the answer is one more repetition of a vowel and non- vowel so easy.


# SECTION 2
# The content of groups in a match can be accessed using the group function.
# A call of group(0) or group() returns the whole match.
# A call of group(n), where n is greater than 0, returns the nth group from the left.
# The method groups() returns all groups up from 1.
# Example:
import re
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())    # abcdefghi
    print(match.group(0))   # abcdefghi
    print(match.group(1))   # bc
    print(match.group(2))   # de
    print(match.groups())   # ('bc', 'de', 'fgh', 'g')
#

# As you can see from the example above, groups can be nested

# 1st Group = bc 
# 2nd Group = fgh 
# 3rd Group = g 
# 4th Group = de 
# In the following code example, note how the groups appear to be given by the above. 
import re 
pattern = r"a(bc)(f(g)h)(de)i" 
match = re.match(pattern, "abcfghdeijklmnop") 
if match: 
    print(match.group()) # the entire MATCH 
    print(match.group(0)) 
    print(match.group(1)) # the 1st GROUP 
    print(match.group(2)) #the 2nd GROUP 
    print(match.group(3)) #the 3rd GROUP 
    print(match.group(4)) #the 4th GROUP 
    print(match.groups()) #ALL GROUPs!!! 
# OUTPUT: abcfghdei abcfghdei bc fgh g de ('bc', 'fgh', 'g', 'de')
#    

# Example with a new pattern:
pattern = r"a(bc)(f(g)h)(de)i"
# so 1st Group = bc 
# 2nd Group = fgh 
# 3rd Group = g (which is a subgroup of "fgh") 
# 4th Group = de like he stated in the first place.


# Example:
import re 
pattern = r"egg(spam)(pearl)(huri)" 
match = re.match(pattern, "eggspampearlhuriTTT") 
if match: 
    print(match.group(0)) # the entire MATCH 
    print(match.group()) 
    print(match.group(1)) # the 1st GROUP 
    print(match.group(2)) # the 2nd GROUP 
    print(match.group(3)) # the 3rd GROUP 
    print(match.groups()) # ALL GROUPs!!! 
# OUTPUT: eggspampearlhuri eggspampearlhuri spam pearl huri ('spam', 'pearl', 'huri')


# Example:
# It's worth noting that if the first group is not found it is essentially skipped and the first FOUND group becomes group(1). 
import re 
pattern = r"a(bc)*(de)(f(g)h)i" 
match = re.match(pattern, "adefghijklmnop") 
if match: 
    print(match.group()) 
    print(match.group(0)) 
    print(match.group(1)) 
    print(match.group(2)) 
    print(match.groups()) # Output: adefghi adefghi None de fgh (None, 'de', 'fgh', 'g')
#


# It is not logically consistent in Python to use index of (1) for the first found case, 
# because like in lists indexing always starts with zero, ==> match.group(0) would make more sense to me.

# But python has to be logically consistent with the rules of regexp when performing regexp operations. 
# If python wrote their own rules for regexp then that would cause even more confusion for those trying to use regexp coming from another language. 
# Principle of Least Surprise..


# you can use both method, with index or not! 
# But, for index you need to call all groups == groups()[index value] 
import re 
pattern = r"a(bc)(de)(f(g)h)i" 
match = re.match(pattern, "abcdefghijklmnop") 
if match: 
    print(match.group()) # all of them 
    print(match.group(0)) # all of them 
    print(match.group(1)) # first group 
    print(match.group(2)) # second group 
    print(match.group(4)) # fourth group 
    print(match.groups()) # all groups 
    print(match.groups(0)) # all groups 
    print(match.groups()[0]) # first index value of groups 
    print(match.groups()[1]) # second index value of groups
#


# The method groups() returns A TUPLE OF all groups up from 1. 
# You can try print(list(match.groups())) and you'll get a list of all groups. 
# You may try even for the first print statement: print(list(match.group())) and you'll get: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']. 

# Example:
import re 
pattern = r"a(bc)(de)(f(g)h)i" 
match = re.match(pattern, "abcdefghijklmnop") 
if match: 
    print(match.group()) 
    print(match.group(0)) 
    print(match.group(1)) 
    print(match.group(2)) 
    print(match.group(3)) 
    print(match.group(4)) 
    print(match.groups())
# result: abcdefghi abcdefghi bc de fgh g ('bc', 'de', 'fgh', 'g') 

# Example:
import re 
pattern = r"[1-4][3-6][a-e]"
match = re.search(pattern, "ab35c") 
if match: 
    print(match.group())    # 35c
    print(match.group(0))   # 35c
#

# What would group(3) be of a match of 1(23)(4(56)78)9(0) ---> 56


# This is an odd question since you can't answer it based solely on the information given in the lesson. 
# It requires you to know that if there is a nested group, the numbering goes into the group before going to the adjacent group. 

# To be more specific, group numbering is based on the opening parentheses.

# Edit version of the last lesson example to know how to identify groups: 
import re 
pattern = r"a(bc)(de)(f(g(hi))jk)l" 
match = re.match(pattern, "abcdefghijklmnop") 
if match: 
    print(match.group()) 
    print(match.group(0)) 
    print("group 1: "+match.group(1)) 
    print("group 2: "+match.group(2)) 
    print("group 3: "+match.group(3)) 
    print("group 4: "+match.group(4)) 
    print("group 5: "+match.group(5)) 
    print(match.groups())
# answers: abcdefghijkl abcdefghijkl 
# group 1: bc 
# group 2: de 
# group 3: fghijk 
# group 4: ghi 
# group 5: hi ('bc', 'de', 'fghijk', 'ghi', 'hi')
        
# Only characters in parenthesis are considered groups and the count starts from 1, 
# therefore, for r”1(23)(4(56)78)9(0): Group 1: 23 Group 2: 45678 Group 3: 56 Group 4: 0
# group(1) =23, group(2)=45678, group(3)=56, group(4)=0 



# Each number in parentheses is a group. Parentheses closed in parentheses is a group within a group. 
# For instance, alpha = (1) (2) (3(4)5) (6) alpha has a total of 5 groups. 
# 1 is a group, 2 is a group, 345 is a group, But 4 is a group itself, And 6 is a group.


# 1(23)(4(56)78)9(0) 
# group(1) 1st grouping (within the bracket) ➡ 23 
# group(2) 2nd grouping (within the bracket) ➡ 4(56)78 
# group(3) 3rd grouping (look there's an inner group in the 2nd grouping!) ➡ 56 
# group(4) 4th grouping

# group(56) is nested in group (478) I.e (4(56)78) 
# Therefore (478) would be considered before (56), it would be group(3): group(1) = (23) group(2) = (478) group(3) = (56)

# Example:
import re 
pattern = r"1(23)(4(56)78)9(0)" 
match = re.match(pattern, "1234567890") 
if match: 
    print(match.groups()) # OUTPUT: ('23', '45678', '56', '0') 
#

# Example: 
import re 
pattern = r"1(23)(4(56)78)9(0)" 
match=re.match(pattern, "1234567890") 
print("Group( ): " + match.group()) 
print("Group(0): " + match.group(0)) 
print("Group(1): " + match.group(1)) 
print("Group(2): " + match.group(2)) 
print("Group(3): " + match.group(3)) 
print("Group(4): " + match.group(4))
print("Groups(): {} ".format (match.groups())) 
# Output:
# Group( ): 1234567890 
# Group(0): 1234567890 
# Group(1): 23 
# Group(2): 45678 
# Group(3): 56 
# Group(4): 0 
# Groups(): ('23', '45678', '56', '0') So, the answer is: 56


# SECTION 3
# There are several kinds of special groups.
# Two useful ones are named groups and non-capturing groups.
# Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. 
# They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
# Non-capturing groups have the format (?:...). They are not accessible by the group method, 
# so they can be added to an existing regular expression without breaking the numbering.
# Example:
import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))         # abc
    print(match.groups())               # ('abc', 'ghi')
#

# this code will let you know all the difference: 
import re 
pattern = r"(?P<first>abc)(?:def)(ghi)" 
match = re.match(pattern, "abcdefghi") 
if match: 
    print(match.group("first"))         # abc
    print(match.group(1))               # abc
    print(match.group(2))               # ghi
    print(match.groups())               # ('abc', 'ghi')
#

# A group nested within a non-capturing group can still be accessed by the group method: 
pattern = r"(?P<first>abc)(?:d(e)f)(ghi)" 
match = re.match(pattern,"abcdefghi") 
if match: 
    print(match.groups()) # ("abc", "e", "ghi")
#

# Example:
import re 
pattern = r"(?P<first>abc)(?:def)(ghi)" 
match = re.match(pattern, "abcdefghi") 
if match: 
    print(match.group("first")) 
    print(match.groups()) # abc ('abc', 'ghi') 
# But consider this: 
import re 
pattern = r"(?P<first>abc)(?:def)(ghi)" 
match = re.match(pattern, "abcdefghi") 
if match: 
    print(match.group()) 
    print(match.group("first")) 
    print(match.groups())
# Output: abcdefghi abc ('abc', 'ghi') 


# Example:
import re 
pattern = r"(?P<first>abc)(?:def)(ghi)" 
match = re.match(pattern, "abcdefghi") 
if match: 
    print(match.group("first")) 
    print(match.group()) 
    print(match.group(0)) 
    print(match.group(1)) 
    print(match.group(2)) 
    print(match.groups())
    print(match.group("first"))
    print(match.group(1) 
#
           
# Example: nested noncapturing group
# (?: …) simply means thatin the list of .groups(), you need to cross out the responding group. 
# But any nested group including or being included by this group should be treated as if there is no ?: at the beginning of this group.
# Code:
import re

pattern = r"(?P<first>abc)(?:d(?:e)(f))(()g(?:hi))"
pattern2 = r"(a)(b(?:c)(d)(?:e))"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))     # abc
    print(match.group(2))           # f
    print(match.groups())           # ('abc', 'f', 'ghi', '')
#
print(re.match(pattern2, "abcde").groups()) # ('a', 'bcde', 'd')



# Example:
import re
mails = ['maria@gmail.com','paulo.guedes@gov.com.br', 'Keosvokiz_kaisaz@outlook.com', 'viktorlenz@solomail.com','hi,iamAnInvalid@mail@gmail.com','aaa@invalid.domain.com']

pattern = r"^(?P<name>[^@]+)(?:@)(?P<domain>[^@\.]+)(?:\.com(\.[a-z][a-z])?)$"
name = []
domain = []
for mail in mails:
    match = re.match(pattern, mail)
    if match:
        name.append(match.group("name"))
        domain.append(match.group("domain"))
#
print(name)     # ['maria', 'paulo.guedes', 'Keosvokiz_kaisaz', 'viktorlenz']
print(domain)   # ['gmail', 'gov', 'outlook', 'solomail']


# Example:
# So, what is the difference between the following two codes? 
# they differ in definition of pattern expression, but produce the same results 
# code1:
from re import match, search, findall, finditer, sub 
pattern = r"(?P<first>abc)(?:def)(ghi)j" 
m1 = match(pattern, "abcdefghij") 
if m1: 
    print(m1.group(1)) 
    print(m1.group(2)) 
    print(m1.groups())
    print(m1.group())
#
# code2 
from re import match, search, findall, finditer, sub 
pattern = r"(?P<first>abc)def(ghi)j" 
m1 = match(pattern, "abcdefghij") 
if m1: 
    print(m1.group(1))
    print(m1.group(2))
    print(m1.groups())
    print(m1.group())
#


# Example as name: 
import re 
pattern = r"(?P<first>gol)(?:dys)(ran)" 
match = re.match(pattern, "goldysran") 
if match: print(match.group("first")) 
    print(match.groups()) # gol ('gol', 'ran') 
# in simple words ?:.... skips the word but numbring remains same as you can see in the the given example(dys) skipped.... 



https://www.sololearn.com/learning/1073/2480/5171/2 
          
          
          
          
          
