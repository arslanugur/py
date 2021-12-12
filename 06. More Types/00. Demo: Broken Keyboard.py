# Useful Functions

# Your friend sent you a message, however his keyboard is broken and types a # instead of a space.

# Replace all of the # characters with spaces and output the result.
# You can use the replace() method of a string to replace one substring with another.

# input: hello#there,#how#are#you?                          input: this#text###contains##many####spaces
# output: hello there, how are you?                         output: this text   contains  many    spaces

# Code:
txt = input() #write a broken sentence where is '#' instead of space
def space(txt):
	text=txt.replace('#',' ')
	return(text)
print(space(txt)) # a right sentence with space instead of '#'

