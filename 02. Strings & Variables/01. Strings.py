# A string is created by entering text between two single or double quotation marks. 
print('Coding in Finance')
print("An investment in knowledge pays the best interest.")

# The delimiter (" or ') used for a string doesn't affect how it behaves in any way.

print ("Spam" , "in", "brain", sep='+', end='!')  # Spam+in+brain!

mystring = 'hello'    # hello 
print(mystring)

mystring = "hello"    # hello 
print(mystring)

hello = "hello" 
world = "world" 
helloworld = hello + " " + world 
print(helloworld)  # hello world


# BACKSLASH
  # Some characters can't be directly included in a string. 
  # For instance, double quotes can't be directly included in a double quote string; this would cause it to end prematurely.

  # Characters like these must be escaped by placing a backslash before them.
  # Double quotes only need to be escaped in double quote strings, and the same is true for single quote strings.

  # For Example:
print('Cat Brian\'s Owner: It\'s not a cat. It\'s a lion!') # Cat Brian's Owner: It's not a cat. It's a lion!

  # Backslashes can also be used to escape tabs, arbitrary Unicode characters, and various other things that can't be reliably printed.
print('''I\'ve found Lydia\'s sword. \nIt\'s broken now. \nLuckily, she\'s still alive.''') # I've found Lydia's sword. It's broken now. Luckily, she's still alive.
  
  # Actually, In Python 3, You don't require backslash! Tried! Its showing the same results without it as well!

  

