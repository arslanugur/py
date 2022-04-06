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

# (1):
# 
# - modules should have short, all-lowercase names;
# e.g. import re, import random, import math

# - class names should be in CapWords style;
# e.g. class Dog back in OOP

# - most variables and function names should be lowercase_with_underscores;
# e.g. consider the following bad_dict variable and add_five function.
bad_dict = {
    [1, 2, 3]: "one two three",
}

# As a quick reminder for WHY exactly this is a BAD dictionary, the Key [1, 2, 3] is a LIST, and so is mutable (vulnerable to being changed), 
# so it CANNOT be used as a dictionary Key. After all, lists + dictionaries are mutable. BUT ONLY immutable objects are allowed to be Keys in a dictionary.
# Example:
def add_five(x):
    return x + 5
#

# (2): Also, regarding the last 2 bits of the lesson, I suspect a hopefully decent example is the following.
# x = (5*2) is BETTER than x = ( 5 * 2 ) 

# Clearly, the FIRST has better readability, for 2 reasons I believe:

# whitespace surrounding the = operato,
# BUT whitespace is NOT overused since inside the parenthesis () BRACKETS, whitespace has been 100% COMPLETELY avoided.

# This site lets you Check your code for PEP8 requirements.  Just paste your code and it will check it for PEP8 requirements.  http://pep8online.com/

# Also, Google has their own Python guide.

# https://github.com/google/styleguide/blob/gh-pages/pyguide.md

# never use character :--
# Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.

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



