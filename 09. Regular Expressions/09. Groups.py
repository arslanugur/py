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
https://www.sololearn.com/learning/1073/2480/5169/2   comments

    
