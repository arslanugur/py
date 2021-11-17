# Shuffles the deck and deals 5 cards each to four players. 

import random
cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suits = ["S", "C", "D", "H"]   # Spade, Club, Diamond, Heart
order = []
p1 = []
p2 = []
p3 = []
p4 = []
def shuffle():
    while (len(order) < 52):        
        a = random.choice(cards)
        b = random.choice(suits)
        draw = a + b
        while(draw not in order):
            order.append(str(draw))
            print(draw) #for debugging
            
            
shuffle()
print(str(len(order)) + " cards in the deck.")
def deal(): #draws 5 cards randomly from the deck. 
    for i in range(5):
        z = random.choice(range(len(order)))
        y = order.pop(z)
        p1.append(y)
        p1.sort()
    for i in range(5):
        z = random.choice(range(len(order)))
        y = order.pop(z)
        p2.append(y)
        p2.sort()
    for i in range(5):
        z = random.choice(range(len(order)))
        y = order.pop(z)
        p3.append(y)
        p3.sort()
    for i in range(5):
        z = random.choice(range(len(order)))
        y = order.pop(z)
        p4.append(y)
        p4.sort()
deal()
print("Player 1: " + str(p1))
print("Player 2: " + str(p2))
print("Player 3: " + str(p3))
print("Player 4: " + str(p4))


# Output: 52 cards in the deck.
# Random Example:
# Player 1: ['3D', '3H', '6S', 'AC', 'JS']
# Player 2: ['3C', '6H', '9D', 'JC', 'QH']
# Player 3: ['2S', '7D', '8S', '9S', 'KD']
# Player 4: ['2C', '3S', '4H', '9C', 'AD']


