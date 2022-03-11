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




https://www.sololearn.com/learning/1073/2477/5165/1 comments

