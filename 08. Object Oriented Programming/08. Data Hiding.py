# SECTION 1
# A key part of object-oriented programming is encapsulation, 
# which involves packaging of related variables and functions into a single easy-to-use object - an instance of a class.
# A related concept is data hiding, which states that implementation details of a class should be hidden, 
# and a clean standard interface be presented for those who want to use the class.
# In other programming languages, this is usually done with private methods and attributes, 
# which block external access to certain methods and attributes in a class.

# The Python philosophy is slightly different. 
# It is often stated as "we are all consenting adults here", meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. 
# Hence there are no ways of enforcing a method or attribute be strictly private.
# However, there are ways to discourage people from accessing parts of a class, such as by denoting that it is an implementation detail, 
# and should be used at their own risk.


# 1. Every piece of explanation about every topic in every lesson should be supported by contextual code snippets that complement the text. 
# This enables the learners to understand and retain the concepts more effectively. 
# 2. Links to previous lessons and concepts should be made available inside every lesson. 
# For example, if I forget what a method is or what dictionaries are and need to quickly refresh my memory, 
# there should be a link that takes me to the respective pages of those concepts. 
# Or a persistent glossary of all concepts should be accessible by swiping from the edge of the screen.

# More details and examples about data hiding in Python here: http://radek.io/2011/07/21/private-protected-and-public-in-python/

# MAIN BENEFIT OF DATA HIDING 
# Let's say that you have in your class a variable called 'atdep'. 
# If the attribute 'atdep' is public, the user of the class can change its value to something unwanted and does braking the working of the functions in that class. 
# So you should not have 'atdep' as public, 
# so two underscores before it '__atdep' should do the job of hiding it. 
# Same concept for some class methods and for magic methods. 
# Data hiding is just the technique of hiding the attributes and methods inside a class which are not relevant for the user to call. 
# Finally, in python you cannot really hide data, so the '__atdep' attribute can be accessed using objects of that class. 
# You just need to add before it 'instanceName._className'


# Encapsulation is just the technique of bundling the information in a single unit in a way as to hide what should be hidden and make visible what should be visible.


# What is a private method in Python? -- A method external code is discouraged from using


# "Strictly speaking, private methods are accessible outside their class, just not easily accessible. Nothing in Python is truly private." 
# http://www.diveintopython.net/object_oriented_framework/private_functions.html

https://www.sololearn.com/learning/1073/2471/5139/2
  
hong ding




