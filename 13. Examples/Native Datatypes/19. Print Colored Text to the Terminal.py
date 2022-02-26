# Native Datatypes Examples
# Example: to Print Colored Text to the Terminal

# Example 1: Using ANSI escape sequences
print('\x1b[38;2;5;86;243m' + 'Programming' + '\x1b[0m')              # Output: Programming
#       Foreground Color    +    Text       +  Background Color

# The working of the above line of code is shown in the figure below.

# Let's understand the escape code \x1b[38;2;5;86;243m.
#    \x1b calls a function. You can also use \033 for the same purpose.
#    38;2;r;g;b helps to set RGB color. 5;86;243 are the rgb color for blue (the color of the logo of Programiz).
#    m is the function name. Here, m means SGR (Select Graphics Rendition) function.

# For more information regarding the ANSI escape code, you can refer to ANSI escape code.

# Example 2: Using python module termcolor
from termcolor import colored

print(colored('Programiz', 'blue'))     # Output: Programming

# Using the module termcolor, you can get the desired output. Also, you can set different styles of the text using this module.
# The first parameter of colored() is the text and the second parameter is the color.


