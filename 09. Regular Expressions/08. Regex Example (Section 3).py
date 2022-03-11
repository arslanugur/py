import re

# Finding a string ends with multiple occurences of 42

pattern = r"(42)+$"

# Match pattern from the beginning of string #

if re.match(pattern, "42"):     print("Match 1") #
if re.match(pattern, "242"):    print("Match 2")
if re.match(pattern, "424"):    print("Match 3")
if re.match(pattern, "4242"):   print("Match 4") #
if re.match(pattern, "24242"):  print("Match 5")
if re.match(pattern, "42424"):  print("Match 6")

# Search pattern anywhere in the string #

if re.search(pattern, "42"):    print("Search found A") #
if re.search(pattern, "242"):   print("Search found B") #
if re.search(pattern, "424"):   print("Search found C")
if re.search(pattern, "4242"):  print("Search found D") #
if re.search(pattern, "24242"): print("Search found E") #
if re.search(pattern, "42424"): print("Search found F")


