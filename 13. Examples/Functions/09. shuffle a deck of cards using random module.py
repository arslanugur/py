# Function Examples
# Example: to shuffle a deck of cards using random module

# Source Code: Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
#

"""
Output
You got:
5 of Heart
1 of Heart
8 of Spade
12 of Spade
4 of Spade
"""

# Note: Run the program again to shuffle the cards.
# In the program, we used the product() function in itertools module to create a deck of cards. 
# This function performs the Cartesian product of the two sequences.
# The two sequences are numbers from 1 to 13 and the four suits. 
# So, altogether we have 13 * 4 = 52 items in the deck with each card as a tuple. For example,

deck[0] = (1, 'Spade')

# Our deck is ordered, so we shuffle it using the function shuffle() in random module.
# Finally, we draw the first five cards and display it to the user. 
# We will get different output each time you run this program as shown in our two outputs.
# Here we have used the standard modules itertools and random that comes with Python.


