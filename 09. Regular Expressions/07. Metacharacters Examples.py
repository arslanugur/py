# Example: * as re meta-character example
import re

pattern = r"(egg)*spam"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggeggspam"):
    print("Match 2")                #

if re.match(pattern, "spam"):
    print("Match 3")                #

if re.match(pattern, "eggespam"):
    print("Match 4")
#


# Example: + as re meta-character example
import re

pattern = r"(egg)+spam"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggeggspam"):
    print("Match 2")                #

if re.match(pattern, "spam"):
    print("Match 3")

if re.match(pattern, "eggespam"):
    print("Match 4")
#


# Example: ? as re meta-character example
import re

pattern = r"(egg)?spam"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggeggspam"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")            #

if re.match(pattern, "eggespam"):
    print("Match 4")
#


# Example: {,} as re meta-characters example
import re

pattern = r"(egg){1,3}spam"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggeggspam"):
    print("Match 2")                #

if re.match(pattern, "spam"):
    print("Match 3")

if re.match(pattern, "eggespam"):
    print("Match 4")
#



