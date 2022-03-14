# Metacharacters
# 1 * 0 = 0 ====> Means * : 0 or more. 
# 1 + 0 = 1 ====> Means+ : 1 or more.

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
# Example:
import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")                    #

if re.match(pattern, "gggggggggggggg"):
    print("Match 2")                    #

if re.match(pattern, "abc"):
    print("Match 3")
#    
# To summarize:
# * matches 0 or more occurrences of the preceding expression.
# + matches 1 or more occurrence of the preceding expression.
# So "(sth)+" is equivalent to "sth(sth)*" -- The latter expression is used in languages that do not support the '+' regex.

# The example is not good at all because it confuses. 
# I have to combine both examples and re-read and re-try several times. 
# Try this code to see the difference between "+" and "*", it's quite simple: 
import re 
pattern = r"^a(g)+" 
if re.match(pattern, "aga"): 
    print("Match +1") 
if re.match(pattern, "abcg"): 
    print("Match +2") 
if re.match(pattern, "a"): 
    print("Match +3") 
if re.match(pattern, "gggabc"): 
    print("Match +4") 

pattern = r"^a(g)*" 
if re.match(pattern, "aga"): 
    print("Match *1") 
if re.match(pattern, "abcg"): 
    print("Match *2") 
if re.match(pattern, "a"): 
    print("Match *3") 
if re.match(pattern, "gggabc"): 
    print("Match *4") # output is +1, *1, *2, *3. And the difference is: "+" - must be at least once; "*" - may by present or may be not.
#


# " starts with 'ag' " and then " starts with 'a' ", so this code is equivalent: 
import re 
pattern = r"^ag" 
if re.match(pattern, "aga"): 
    print("Match +1") 
if re.match(pattern, "abcg"): 
    print("Match +2") 
if re.match(pattern, "a"): 
    print("Match +3") 
if re.match(pattern, "gggabc"): 
    print("Match +4") 
pattern = r"^a" 
if re.match(pattern, "aga"): 
    print("Match *1") 
if re.match(pattern, "abcg"): 
    print("Match *2") 
if re.match(pattern, "a"): 
    print("Match *3") 
if re.match(pattern, "gggabc"): 
    print("Match *4") # Result: Match +1 Match *1 Match *2 Match *3 the (g)+ and (g)* 
#

# [^a] means match any character other than a. ^a means the first character must be a. ^a is mostly applicable if you use re.search. 
# For re.match, it's needless to include "^" since re.match always matches the first character in the text.

# The code below is a much better example. This is the first example and only change the * to +. 
# It shows the difference between the metacharacters. 
# The string has to start with egg and spam has to occur at least once afterwards. 
import re 
pattern = r"egg(spam)+" 
if re.match(pattern, "egg"): 
    print("Match 1") 
if re.match(pattern, "eggspamspamegg"): 
    print("Match 2")                    # 
if re.match(pattern, "spam"): 
    print("Match 3")
#

# Check this out: 
import re 
pattern = r"^a(g)+" 
if re.match(pattern, "aga"): 
    print("Match +1")           #
if re.match(pattern, "abcg"): 
    print("Match +2") 
if re.match(pattern, "a"): 
    print("Match +3") 
if re.match(pattern, "gggabc"): 
    print("Match +4") 

pattern = r"^a(g)*" 
if re.match(pattern, "aga"): 
    print("Match *1")           #
if re.match(pattern, "abcg"): 
    print("Match *2")           #
if re.match(pattern, "a"): 
    print("Match *3")           #
if re.match(pattern, "gggabc"): 
    print("Match *4") 
#            


# Example:
# * means always match zero/more occurrences of what is before. This code confirms that. 
# The teaching after magic methods has become incomprehensible until you try things out elsewhere. 
import re 
pattern = r"g*" 
if re.match(pattern, "g"): 
    print("Match 1 *") 
if re.match(pattern, "gggggggggggggg"): 
    print("Match 2 *") 
if re.match(pattern, "abc"): 
    print("Match 3 *") 
    
pattern = r"g+" 
if re.match(pattern, "g"): 
    print("Match 1 +") 
if re.match(pattern, "gggggggggggggg"): 
    print("Match 2 +") 
if re.match(pattern, "abc"): 
    print("Match 3 +")
#

# tried comparing * and + 1--> For * 
import re 
pattern = r"g*" 
if re.match(pattern, "g"): 
    print("Match 1") 
    print(re.match(pattern, "gggggggggggggg")) 
    print(re.match(pattern, "abc")) # Output #Match1 #match at span (0-14) #match at span (0,0) 
# for + 
import re 
pattern = r"g+" 
if re.match(pattern, "g"): 
    print("Match 1") 
    print(re.match(pattern, "gggggggggggggg")) 
    print(re.match(pattern, "abc")) # Output #match1 #match at span (0-14) # no output
#


# Example: 
import re 
pattern_1 = r"(spam)+egg" 
if re.match(pattern_1,"spamspamspamegg"): 
    print('match_1') 

pattern_2 = r"(spam)egg" 
if re.match(pattern_2,"spamegg"): 
    print('match_2') 
if re.match(pattern_2,"spamspamegg"): 
    print('match_3')
#


# Example: To create a pattern that matches strings that contain one or more 42s -- r"(42)+$"
# $ is in the end is because it matches the last character of the string,
# * is used to match zero or more occurence of characters + Is used to match one or more occurence of characters.. So answer is +
# The r"(42)+$" means it matches that ends with 42 for search method but for match method it should start with 42 and with 42 this was the use of $ in raw string


# SECTION 3
# The metacharacter ? means "zero or one repetitions".
# Example:
import re

pattern = r"ice(-)?cream"           # This search pattern looks for a string with "ice", 0 or 1( -) hyphens, and "cream". Without any spaces

if re.match(pattern, "ice-cream"):
    print("Match 1")                # 1

if re.match(pattern, "icecream"):
    print("Match 2")                # 2

if re.match(pattern, "sausages"):
    print("Match 3")

if re.match(pattern, "ice--ice"):
    print("Match 4")
#
 

To be more istructive in the last line of the code one would write "ice--cream" instead of "ice--ice"

As "-" is only a single character the parentheses aren't actually needed. pattern = r"ice-?cream"

* = 0 or more + = 1 or more ? = 0 or 1

# Using character class: 
import re 
pattern = r"ice[- ]?cream" 
if re.match(pattern, "ice-cream"): 
    print("Match 1")            # 
if re.match(pattern, "icecream"): 
    print("Match 2")            #
if re.match(pattern, "ice cream"): 
    print("Match 3")            #
if re.match(pattern, "ice--cream"): 
    print("Match 4")
#

# Round brackets have not been introduced yet. 
# Either the module "Groups" should come before this module, or the round bracket should be ommited, as it is not really necessary here 

# Example:
import re 
pattern_1 = r"(spam)?egg" 
if re.match(pattern_1,"spamspamspamegg"): 
    print('match_1') 
if re.match(pattern_1,"spamegg"): 
    print('match_2') 
if re.match(pattern_1,"egg"): 
    print('match_3')
#

# it looks for the words: ' ice' and 'cream' where they are joined once with a dash (-) or without it.
    
# Example:
import re 
pattern = r"egg(spam)?" 
if re.match(pattern, "eggspamspam"): 
    print("match found") 
else: 
    print("No match") # output: match found
    
pattern = r"egg(spam)?bacon" 
if re.match(pattern, "eggspamspambacon"):
    print("match found")
else:
    print("No match") # output: No match
#

# what is the difference between * and ? both are used for zero or more repeatation.. then what's the need of two different options? 
# I thought * is used at end where as ? should be used at in between string.

# Example:
ic = r'(ice)?cream' 
if re.match(ic, 'iceicecream'): 
    print("found") 
if re.match(ic, 'icecream'): 
    print("found")
#


# Example: To match both 'color' and 'colour'. pattern = r"colo(u)?r"
# (Funfact: British English says "colour" and American English says "color") 
# In order to accept both Colour and Color, writing "Colo(u)?r" we tell python to accept "(u)?" Either once or zero times. 
# Because the ? Character tells that the u (in paranthesis) can be used Zero or one time.. This builds the both words "colour" and "color"

# Example:
# we can drop parenthesis and it works as well: 
import re 
pattern = r"colou?r" 
if re.match(pattern, "color"): 
    print("Match 1") #
if re.match(pattern, "colour"): 
    print("Match 2") #
#


# SECTION 4: Curly Braces
# Curly braces can be used to represent the number of repetitions between two numbers.
# The regex {x,y} means "between x and y repetitions of something".
# Hence {0,1} is the same thing as ?.
# If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
# Example:
import re
pattern = r"9{1,3}$"    # $ stands for not just end of a string., it says "it should end with 9 itself" otherwise 9996 should've matched.
                        # When you remove the ‘$’, re.match matches the first 3 9’s (you can verify using group() method) 
                        # but with the ‘$’ it can’t match like that as the third 9 isn’t the end of the string.
if re.match(pattern, "9"):
    print("Match 1")            #

if re.match(pattern, "999"):
    print("Match 2")            #

if re.match(pattern, "9999"):
    print("Match 3")
#
# "9{1,3}$" matches string that have 1 to 3 nines.
# Info box is wrong: "that have 1 to 3 nines at the end" this pattern would be: ".*9{1,3}$" the right text: "that have 1 to 3 nines"
# I think the info box should be changed to "that have 1 to 3 nines at the beginning of the string" 
# because: 
# - they use re.match() which searches only at the beginning 
# - they use $ with re.match() which will tell the function to search for a string that ENDS in 1 to 3 nines 
# but this group has to be at the BEGINNING of the string :) 
# So if you have 9999 like in the last 'if' the group of nines will end in more that 3 nines at the beginning. 
# e.g: (999)9 -> doesn't match OR If you take the '$' out of the expression the output will be Match1, Match2, Match3 
# Does this make sense ? It is pretty complex I think they should find a more straightforward example that just demonstrates the use of { }

# The difference between match and search functions is that match starts from beginning of string. 
# So if you use start of line anchor ^ in pattern, search & match are equivalent. 
# Example: 
import re 
pattern = r"9{1,3}$" # original script 
if re.match(pattern, "9"): # match 
    print("Match 1") 
if re.match(pattern, "999"): # match 
    print("Match 2") 
if re.match(pattern, "9999"): # no match 
    print("Match 3")

pattern = r"^9{1,3}$" # add ^ at beginning of string # use search instead of match 
if re.search(pattern, "9"): # match 
    print("Match 1") 
if re.search(pattern, "999"): # match 
    print("Match 2") 
if re.search(pattern, "9999"): # no match 
    print("Match 3")
#    

# You can notice that: {,} and {0,} are the same as * {1,} is the same thing as + {,1} and {0,1} are the same as ? 

# Also, a single number in curly braces means exactly that many repetitions. For example, r"9{3}" would match *only* the second example.

# Some fun password authenicator code with the mandatory requirement of at least one uppercase and one number 
import re 
password = input() #your code goes here 
format1 = r"[a-z]*" 
format2 = r"[0-9]+" 
format3 = r"[A-Z]+" 
if re.search(format1, password): 
if re.search(format2, password):
if re.search (format3, password): 
    print ("Password created") 
else: 
    print("Wrong format") 
else: 
    print("Wrong format")
else:
    print("Wrong format")
#

# Example:
import re 
password = input() 
pattern1 = r'.*[A-Z]+.*[0-9]+' 
if re.match(pattern1, password): 
    print('Password created') 
else: 
    print('Wrong format')
#

# Example:
import re pattern = r"9{3,4}$" if re.match(pattern, "9"): print("Match 1") if re.match(pattern, "999"): print("Match 2") if re.match(pattern, "9999"): print("Match 3") Match 2 Match 3
            
It should be pointed out that re.match implies that the whole string should match, not just a part of it. Previous examples used re.search, for which 9{1,3}$ would also match the last example, since "999$" is a sub string of "9999".

"9999" it is not match because match function go only first match and than match stop searching. re.search(pattern,"9999") it is match because search go end of the string. re.search(pattern,"993") it not match because it end with 3 not in repetition of 9


# 



