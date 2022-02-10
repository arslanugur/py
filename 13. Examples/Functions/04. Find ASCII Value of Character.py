# Function Examples
# Example: Find ASCII Value of Character

# ASCII stands for American Standard Code for Information Interchange.

# It is a numeric value given to different characters and symbols, for computers to store and manipulate. 
# For example, the ASCII value of the letter 'A' is 65.

# Source Code: Program to find the ASCII value of the given character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
# Output: The ASCII value of 'p' is 112

# Note: To test this program for other characters, change the character assigned to the c variable.

# Here we have used ord() function to convert a character to an integer (ASCII value). This function returns the Unicode code point of that character.

# Unicode is also an encoding technique that provides a unique number to a character. 
# While ASCII only encodes 128 characters, the current Unicode has more than 100,000 characters from hundreds of scripts.

# Your turn: Modify the code above to get characters from their corresponding ASCII values using the chr() function as shown below.
"""  
>>> chr(65)
'A'
>>> chr(120)
'x'
>>> chr(ord('S') + 1)
'T'
"""
# Here, ord() and chr() are built-in functions. 


