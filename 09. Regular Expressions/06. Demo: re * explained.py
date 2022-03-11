import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match anything with egg at beginning")   #

if re.match(pattern, "egggghhjhvbfvbgvbg"):
    print("Match anything after egg")               #

if re.match(pattern, "spam"):
    print("Match?")

    
#here is a better example of usage of *.
import re

pattern = r"(spam)*egg"

if re.match(pattern, "spambaconegg"):
    print("Match 1")

if re.match(pattern, "spamegg"):
    print("Match 2")                                  #

if re.match(pattern, "spamspamegg"):
    print("Match 3")                                  #

if re.match(pattern, "egg"):
 print("Match 4")                                     #

# first if the unlimited "spam" has been interupted by bacon. so the is no match. for the second, third and fourth if there is 1, 2 and 0 "spam respectively"



