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

1st Group = bc 
2nd Group = fgh 
3rd Group = g 
4th Group = de 
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
    print(match.groups()) #ALL GROUPs!!! OUTPUT: >> abcfghdei abcfghdei bc fgh g de ('bc', 'fgh', 'g', 'de')
#    


https://www.sololearn.com/learning/1073/2480/5170/1 coomentsa
    





