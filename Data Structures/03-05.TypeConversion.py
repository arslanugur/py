#veri tipi dönüşümleri
"""
x = input('number1: ')
y = input('number2: ')

total = x + y
print(total)

#input komutu yardımıyla kullanıcı veri girer.
#str işlem. mesela 2 + 3 = 5 değil, 23 gösterir
#düzelme yolu, x ve y'yi toplamaya sokmadan önce int çevir
"""

"""
x = input("number1: ")
y = input("number2: ")

print(type(x))
print(type(y))

total = int(x) + int(y) #sayıları int çevir ve total değişkeni at

print(total)
"""


#other examples
"""
x = 5               #int
y = 2.5             #float
name = "Arslan"     #str
isOnline = True     #bool

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

"""

#TYPE CONVERSIONS

#int to float
"""
x = 5
x = float(x)  #x'i floata çevirdik
print(x)
print(type(x))
#int 5 bilgisi artık float 5 olacak 
"""

#float to int
"""
y = 2.5
y = int(y)
print(y)
print(type(y))
#sonucu 2.5 değil 2 çıkar ondalıklı kısım gider
"""

"""
x = 5
y = 2.5

result = x + y
print(result)
print(type(result))
"""

#eğer bunları string olarak toplarsak
"""
x = 5
y = 2.5

result = str(x) + str(y)
print(result)
print(type(result))
"""

#bool to string
"""
isOnline = True

isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))
#bool işlevini kaybeder sadece yazı olarak true olur
"""

#bool to int
"""
isOnline = True
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
#sonuç 1 çıkacak. bool yani isonline false ise sonuç 0 sıfır
"""
