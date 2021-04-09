#Veri tipi dönüşümleri
"""
x = input('number1: ')
y = input('number2: ')

total = x + y
print(total)
"""
#input komutu yardımıyla kullanıcı veri girer.
#str işlem. mesela 2 + 3 = 5 değil, 23 gösterir
#Düzelme yolu, x ve y'yi toplamaya sokmadan önce int çevir

x = input("number1: ")
y = input("number2: ")

print(type(x))
print(type(y))

total = int(x) + int(y)   #sayıları int çevir ve total değişkeni ata

print(total)

##################################

#Other examples
x = 5               #int
y = 2.5             #float
name = "Arslan"     #str
isOnline = True     #bool

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

###################################

###  TYPE CONVERSIONS

#int to float
x = 5
x = float(x)  #x'i floata çevirdik, int 5 bilgisi artık float 5 olacak
print(x)
print(type(x))   

#float to int
y = 2.5
y = int(y)    #sonucu 2.5 değil, 2 çıkar ondalıklı kısım gider
print(y)
print(type(y))

############################

x = 5
y = 2.5

result = x + y
#ya da eğer bunları string olarak toplarsak
result = str(x) + str(y)

print(result)
print(type(result))

############################

#bool to string
isOnline = True
isOnline = str(isOnline)  #bool işlevini kaybeder sadece yazı olarak true olur

print(isOnline)
print(type(isOnline))

#bool to int
isOnline = True
isOnline = int(isOnline)   #sonuç 1 çıkacak. bool yani isonline false ise sonuç 0 sıfır

print(isOnline)
print(type(isOnline))

