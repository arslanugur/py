# SECTION 1: The Zen of Python
# Writing programs that actually do what they are supposed to do is just one component of being a good Python programmer.
# It's also important to write clean code that is easily understood, even weeks after you've written it.

# One way of doing this is to follow the Zen of Python, a somewhat tongue-in-cheek set of principles that serves as a guide to programming the Pythoneer way. 
# Use the following code to access the Zen of Python.
import this

"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# https://github.com/amontalenti/elements-of-python-style#a-little-zen-for-your-code-style

Here are some more... >>> import __hello__ Hello world... >>> >>> import antigravity >>> (opens a comic website) >>> from __future__ import braces File "<stdin>", line 1 SyntaxError: not a chance >>> >>> love=this >>> this is love True >>> love is True False >>> >>> love is False False >>> >>> love is not True or False; love is love True True >>>

"this" is a self-referring key word in many languages- like "self" in Pyhton. And he used it here as self-referring to the zen-essence of the language. oh, this Dutch people, practical, progressive, clear, wise and stingy (read: non-wasteful) : no wonder, such small nation, on such small land has commanded so much of the (past) and current wealth, yet have remained relatively unbombastic.

# SECTION 2
# Some lines in the Zen of Python may need more explanation.
# Explicit is better than implicit: It is best to spell out exactly what your code is doing. This is why adding a numeric string to an integer requires explicit conversion, rather than having it happen behind the scenes, as it does in other languages.
# Flat is better than nested: Heavily nested structures (lists of lists, of lists, and on and on…) should be avoided.
# Errors should never pass silently: In general, when an error occurs, you should output some sort of error message, rather than ignoring it.

# There are 20 principles in the Zen of Python, but only 19 lines of text.
# The 20th principle is a matter of opinion, but our interpretation is that the blank line means "Use whitespace".
# The line "There should be one - and preferably only one - obvious way to do it" references 
# and contradicts the Perl language philosophy that there should be more than one way to do it.

import this
help(this)

# https://medium.com/@Pythonidaer/a-brief-analysis-of-the-zen-of-python-2bfd3b76edbf

# Factorial using a 'while loop' 
num = int(input()) 
fac = 1 
while num >=1: 
  fac *= num 
  num -= 1 
  print(fac) 
#
# Factorial using 'recursion (in functional programming)'
# num = int(input()) def factorial(n): if n <= 1: return n else: return n * factorial(n-1) print(factorial(no))
# Recursion should always be the second thought



