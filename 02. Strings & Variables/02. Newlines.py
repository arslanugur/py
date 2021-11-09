# \n represents a new line.
# It can be used in strings to create multi-line output: 
print('One\nTwo\nThree')

# Similarly, \t represents a tab.



# Newlines will be automatically added for strings that are created using three quotes. There is basically a shortcut. Instead of using \n to create a line break, 
# For example: This makes it easier to format long, multi-line texts without the need to explicitly put \n for line breaks.
print("""this
is a
multiline
text""")  

# you use triple quotations """ """ and just press Enter to skip to the next line. It does it for you and saves time. 
print("""Hello there. 
My name is Brian. 
Nice to meet you.""")

# The \n thing is used for inline line breaks
print("Yo\nBoi" )   # Yo Boi
# The triple quotes (""") is used for multiple lines line breaking
print("""Yo
Boi""") # Yo Boi 
# Explaining: \n and triple quotes (""") are the same thing, except, 
               # \n is used for inline line break (making it a little bit harder to read but smaller), 
               # and triple quotes (""") are for multiple lines line break (making it easier to read but bigger)


