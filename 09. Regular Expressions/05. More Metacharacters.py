# SECTION 1
# Some more metacharacters are * + ? { and }.
# These specify numbers of repetitions.
# The metacharacter * means "zero or more repetitions of the previous thing". 
# It tries to match as many repetitions as possible. 
# The "previous thing" can be a single character, a class, or a group of characters in parentheses.
# Example:
import re
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")                    #

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")                    # 

if re.match(pattern, "spam"):
    print("Match 3")
#

# The example above matches strings that start with "egg" and follow with zero or more "spam"s.



# Example: here is a better example of usage of *. 
import re 
pattern = r"(spam)*egg" 
if re.match(pattern, "spambaconegg"): 
    print("Match 1") 
if re.match(pattern, "spamegg"): 
    print("Match 2") #
if re.match(pattern, "spamspamegg"): 
    print("Match 3") #
if re.match(pattern, "egg"): 
    print ("Match 4") # This would also match              
if re.match(pattern,"eggspambaconegg"): 
    print ("Match 5") # This would also match
#
        
# For those struggling with "why use (  )*  " Think if you wanted to find all occurances of  the sequence 123 followed by 456. 
# This would be a good time to use (  )*: 
import re 
pattern = r"123([0-9])*456" 
if re.match(pattern, "123456"): 
    print("Match 1") 
if re.match(pattern, "123000000000456"): 
    print("Match 2") 
if re.match(pattern, "1230456"): 
    print("Match 3") 
if re.match(pattern, "123333444456"): 
    print("Match 4") 
if re.match(pattern, "12356"): 
    print("Match 5")
#

# Example: pattern = r"egg(spam)*" gives the same result as pattern = r"egg" 

# Example: Here is a better example of usage of *. #first if the unlimited "spam" has been interupted by bacon. so the is no match. 
# for the second, third and fourth if there is 1, 2 and 0 "spam respectively" 
import re 
pattern = r"(spam)*egg" 
if re.match(pattern, "spambaconegg"): 
    print("Match 1") 
if re.match(pattern, "spamegg"): 
    print("Match 2") 
if re.match(pattern, "spamspamegg"): 
    print("Match 3") 
if re.match(pattern, "egg"): 
    print("Match 4")
#


# Example and Ways
# What would [a^]* match? -- Zero or more repetitions of "a" or "^"
# [a^]* would mean zero or more repetitions of a or ^ . You might confuse it with character classes where ^ should be at the beginning. 
# Hence [^a] would mean any character other than 'a'.

# The right answer is "Zero or more repetitions of any character". 
# Just try it in code: 
import re 
pattern = r"[a^]*" 
string = input(": ") 
if re.match(pattern, string): 
    print("Yes") 
else: 
    print ("No match") 
#

# Second Way
"""
Mistake in test of the python lesson Regular Expressions
Regular Expressions 4/7
More Metacharacters 1/4

What would [a^]* match?

Zero or more repetitions of "a" or "^" - right answer in test
Zero or more repetitions of any character   - Real right anwser
Zero or more repetitions of any characters other than "a"
"""
import re

pattern = r"[a^]*"

string = input(": ")

if re.match(pattern, string):
    print("Yes")
else:
    print ("No match")
#


# SECTION 2
# The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".
Example:
