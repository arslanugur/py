# Modülleri içe aktarmak
import itertools, random

# Kart Destesi Oluşturmak
cards = list(itertools.product(range(1,14),['ace','heart','diamond','spade']))

# Kartları Karıştırmak
random.shuffle(cards)

# Karıştırılmış Kartları yazdırmak
print("Your Cards: ")
for i in range(5):
  print(cards[i][1], " ", cards[i][0])
#


