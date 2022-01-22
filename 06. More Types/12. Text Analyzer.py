# TEXT ANALYZER
# SECTION 1
# This is an example project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
# This section shows how a file could be open and read.
# Code:
filename = input("Enter a filename: ")
with open(filename) as f:
   text = f.read()
print(text)
"""
Result:
Enter a filename: test.txt
Ornh gvshy vf org
"""

# Example: to read the contents of a file using the "with" statement.
with open(filename) as f:
   text = f.read()
#

# They used the "with" function, meaning that there is no need to close the file. 
# But the problem it is that we have stored everything into a variable 
# and if we don't wan't to use memory, it will be better to delete the variable after using it. 
# We can always reopen the file if we need it. 
# If we want just to print what it is inside the file, a better option is: with open(filename) as f: print(f.read())

# Why in this case there is no 'r'ead after the filename? 
# what if I don't write the , 'r' (or 'w' or 'wb') using 'with'.
# what's the default (if any) with open("filename", 'r') as f:


# SECTION 2
# This part of the program shows a function that counts how many times a character occurs in a string.
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count
#
# This function takes as its arguments the text of the file and one character, returning the number of times that character appears in the text.
# Now we can call it for our file.
filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()
#
print(count_char(text, "r"))

# Output:
# Enter a fileneme: test.txt
# 83                       # The character "r" appears 83 times in the file.

# The proper way to utilize Python's built in efficiencies: 
def count_char(text, char): 
    return 
    text.count(char) 
    print(count_char(text, "r"))
#

# Example:
def count_char(text,char): 
   (text,char) 
   # text parameter becomes the file opened and available to read "r" becomes that 
   # char parameter for c in text basically saying for every letter in the text 
   # apply c to it starting for the first letter if c == char #if c is == to "r" c is standing for the every letter in the text 
   # if I write text= "hello my name is steve" then for c in text c will first be "h" then "e" then "L" and so on 
#


# Example using List Comprehension:
def count_char(text, char): 
   return 
   sum([c == char for c in text])
#


# Example to edit:
def count_char(text, char): 
   count = 0 
   for c in text: 
      if c == char: 
         count += 1 
         return 
      count file = open("newfile.txt", "w") 
      file.write("SOLO LEARN") 
      file.close() 
      filename = "newfile.txt" 
      with open(filename) as f: 
         text = f.read() 
         print(count_char(text,"L"))
#

# the character-counting code has been put in a function that's why, So it can be run multiple times


# SECTION 3
# The next part of the program finds what percentage of the text each character of the alphabet occupies. 
# Code:
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))
#

# Let's put it all together and run the program: 
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))     # {O} will be replaced by char, which iterates to give values from a to z.
                                                         # {1} will be replace d by returned value of rounded perc value till 2 decimal points
# Enter a filename: test.txt
# a - 4.68%
# b - 4.94%
# c - 2.28%
# ...



# About using a dictionary instead of looping through the whole text every time, so I tried doing that. 
dic = {} 
for c in "abcdefghijklmnopqrstuvwxyz": 
   dic[c] = 0
   doc = text.lower()
for c in doc:
    for char in "abcdefghijklmnopqrstuvwxyz": 
        if c == str(char): 
            dic[str(char)] += 1 
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * dic[char] / len(text) 
    print("{0} - {1}%".format(char, round(perc, 2)))
#




def count_char(text, char): 
   count = 0 
   for c in text: 
      if c == char: 
         count += 1 
         return 
      count 

filename = input("Enter a filename: ") 
with open(filename) as f: 
text = f.read() 
for char in "abcdefghijklmnopqrstuvwxyz": 
   perc = 100 * count_char(text, char) / len(text) print("{0} - {1}%".format(char, round(perc, 2))) 
#1 - We are defining a new function called "count_char"   
#1 - It has two arguments: "text" and "char". It will be used as placeholders. 
#2 - variable called "count" has a starting value of 0. Important for the for loop 
#3 - for every "c" inside the text, 
#4 - if the "c" is equal to "char", 
#5 - Add a +1 to the "count" variable 
#6 - Return that value. 
#7 - Space 
#8 - Input form for your filename 
#9 & 10 - Whatever text file you put in, open it and read #11 - Space 
#12 - For each "char" inside that string of letters, 
#13 - Calculate the percentage by multiplying 100 with the count_char function 
#13 - divided by the length of the text. 
#14 - Print out the percentage and round it


# Example:
with open('text.txt') as f: 
   v = len(f.read()) 
   f.seek(0) 
   print('{perc}%'.format(perc = round(100 * len([ i for i in list(f.read()) 
   if i == 'r' ]) / v, 2)))
#

# Example
def count_char(text, char): 
   count = 0 
   for c in text: 
      if c.lower() == char.lower(): 
         count += 1 
         return 
         count 
def uniq_char(text): 
   uqchar=[] 
   for ch in text: 
      if ch.lower() not in uqchar: 
         uqchar.append(ch.lower()) 
         return 
         uqchar

file = open("newfile.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.""") 
file.close() 
filename = "newfile.txt" 
with open(filename) as f: 
   text = f.read()
   uniq_chars=uniq_char(text) 
   uniq_chars.sort() 
   dol = 0 
   for char in uniq_chars: 
      perc = 100 * count_char(text, char) / len(text) 
      dol+=perc 
      print("{0} - {1}%, percentage of text:{2}".format(char, round(perc, 2), round(dol,2)))
#

# the purpose of the round function in the code -- To reduce the number of digits printed


# Process of elimination: 
# Is it more precise to reduce decimals? No. If anything, it is less precise. That one is clearly incorrect. 
# Does it save memory? No. After all, it already had to calculate all the decimals earlier. 
# All you're telling the program to do with the "round" function is to limit its answer to two decimals before showing it to you. 
# Then finally, does it reduce the number of digits on screen? 
# Yes, and that is also its primary use. You wouldn't want 20 decimals when 2 are enough. 
# It could severely affect readability if you want to display your results in, for example, a table or list.
   

# 3 Manners of doing the rounding: 
# round method 
print(round(value, 2))                 # 60.57
# f-string for new versions of Python 
print(f'{value:.2f}')                  # 60.57
# and also: 
print('{:.2f}'.format(value))          # 60.57

print(round(2.5623440,2))              # 2.56


