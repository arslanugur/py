# SECTION 1: PEP
# Python Enhancement Proposals (PEP) are suggestions for improvements to the language, made by experienced Python developers. 
# PEP 8 is a style guide on the subject of writing readable code. It contains a number of guidelines in reference to variable names, which are summarized here:
#  - modules should have short, all-lowercase names; 
#  - class names should be in the CapWords style; 
#  - most variables and function names should be lowercase_with_underscores; 
#  - constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
#  - names that would clash with Python keywords (such as 'class' or 'if') should have a trailing underscore.

# PEP 8 also recommends using spaces around operators and after commas to increase readability.


# However, whitespace should not be overused. For instance, avoid having any space directly inside any type of brackets.

# (1): - modules should have short, all-lowercase names; 
# e.g. import re, import random, import math - class names should be in CapWords style; 
# e.g. class Dog back in OOP - most variables and function names should be lowercase_with_underscores; 
# e.g. consider the following bad_dict variable and add_five function. bad_dict = { [1, 2, 3]: "one two three", } 
# As a quick reminder for WHY exactly this is a BAD dictionary, the Key [1, 2, 3] is a LIST, and so is mutable (vulnerable to being changed), 
# so it CANNOT be used as a dictionary Key. After all, lists + dictionaries are mutable. BUT ONLY immutable objects are allowed to be Keys in a dictionary. 
# Example:
def add_five(x):
    return x + 5
#

# (2): Also, regarding the last 2 bits of the lesson, I suspect a hopefully decent example is the following. 
# x = (5*2) is BETTER than x=( 5 * 2 ) 
# Clearly, the FIRST has better readability, for 2 reasons I believe: whitespace surrounding the = operator, 
# BUT whitespace is NOT overused since inside the parenthesis () BRACKETS, whitespace has been 100% COMPLETELY avoided😀.

# There should be spaces around operator. x = (5 * 2)

# As already mentioned, whitespace can, and should be, around operators, regardless of parentheses. The best solution is therefore x = (5 * 2).

# This site lets you Check your code for PEP8 requirements. Just paste your code and it will check it for PEP8 requirements.  http://pep8online.com/

# Also, Google has their own Python guide.

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md


# never use character : 
# -- Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.

# package and module name :--
# Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. ( e.g._socket ).
# class name :--
# class names should be in the CapWords style ( ex. MyClassName )

# variable and function name :--
# most variables and function names should be lowercase_with_underscores
# Examples:
from typing import TypeVar 
VT_co = TypeVar('VT_co', covariant=True) 
KT_contra = TypeVar('KT_contra', contravariant=True)

# constant name :--
# written in all capital letters with underscores separating words. Examples include MAX_OVERFLOWand TOTAL .

# and for more information goto -  https://www.python.org/dev/peps/pep-0008/#names-to-avoid

# I highly recommend everybody to install AutoPEP8 so your code will be scanned real time as you write it 
# and you will receive recommendations what and how you should change. 
# This way you will always create readable, consistent and nice code without thinking about how to do it.

# See more at https://pypi.org/project/autopep8/

# I highly recommend everybody to install AutoPEP8 so your code will be scanned real time as you write it 
# and you will receive recommendations what and how you should change. 
# This way you will always create readable, consistent and nice code without thinking about how to do it.
# See more at https://pypi.org/project/autopep8/

# Use pylint to check your code is correct https://www.pylint.org

# Use Auto Pep to clean up your code automatically https://pypi.python.org/pypi/autopep8 and Pylint to pick up and coding issues https://www.pylint.org/

# Which choice is PEP 8-compliant as the name of a class? --- MyClassName

# From Wikipedia: "As the first letter of a compound word in camel case may or may not be capitalized, 
# there is no consensus on whether the term "camel case" implies an uppercase or lowercase initial letter. 
# For clarity, this article calls the two alternatives upper camel case (initial upper case letter, 
# also known as Pascal Case) and lower camel case (initial lower case letter). 
# Some people and organizations, notably Microsoft, use the term camel case only for lower camel case." https://en.m.wikipedia.org/wiki/Camel_case
        
# never use character :-- 
# Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names. 
# package and module name :-- Modules should have short, all-lowercase names. 
# Underscores can be used in the module name if it improves readability. ( e.g._socket ). 
# class name :-- 
# class names should be in the CapWords style ( ex. MyClassName ) variable 
# and function name :-- most variables and function names should be lowercase_with_underscores 
# Examples: 
from typing import TypeVar 
VT_co = TypeVar('VT_co', covariant=True) 
KT_contra = TypeVar('KT_contra', contravariant=True) 
constant name :-- written in all capital letters with underscores separating words. 
# Examples include MAX_OVERFLOWand TOTAL . and for more better to understand goto - https://www.python.org/dev/peps/pep-0008/#names-to-avoid


# The earliest use of the name "CamelCase" occurs in 1995, in a post by Newton Love.[18] 
# Love has since said, "With the advent of programming languages having these sorts of constructs, 
# the humpiness of the style made me call it HumpyCase at first, before I settled on CamelCase. I had been calling it CamelCase for years. ... 
# The citation above was just the first time I had used the name on USENET."[19]

# https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/CamelCase.svg/368px-CamelCase.svg.png

# There are two kinds of CamelCase: 1- UpperCamelCase -> PascalCase 2-lowerCamelCase


# SECTION 3
# Other PEP 8 suggestions include the following:
# - lines shouldn't be longer than 80 characters;
# - 'from module import *' should be avoided;
# - there should only be one statement per line.

# It also suggests that you use spaces, rather than tabs, to indent. 
# However, to some extent, this is a matter of personal preference. 
# If you use spaces, only use 4 per line. It's more important to choose one and stick to it.

# The most important advice in the PEP is to ignore it when it makes sense to do so. 
# Don't bother with following PEP suggestions when it would cause your code to be less readable; inconsistent with the surrounding code; or not backwards compatible.
# However, by and large, following PEP 8 will greatly enhance the quality of your code.
# Some other notable PEPs that cover code style:
# PEP 20: The Zen of Python
# PEP 257: Style Conventions for Docstrings

# What is the recommended length limit for a line of code? -- 79-80 --> PEP 8 recommends 80         --> It's just a suggestion to make it more readable and clean
# http://stackoverflow.com/questions/88942/why-does-python-pep-8-specify-a-maximum-line-length-of-79-characters/88948#88948
# Terminals usually had 80 characters wide. In the old D.O.S., screens in text mode has 80x24 characters.
# According to Stack overflow: 
# Keeping your code human readable not just machine readable. A lot of devices still can only show 80 characters at a time. 
# Also it makes it easier for people with larger screens to multi-task by being able to set up multiple windows to be side by side. 
# Readability is also one of the reasons for enforced line indentation.

# https://softwareengineering.stackexchange.com/questions/148677/why-is-80-characters-the-standard-limit-for-code-width




