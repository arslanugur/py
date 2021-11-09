# koşul ifadeleri
# koşullu durum blokları: if - elif ve else

"""
x = 10
y = 20 
if x > y:
    print('x is bigger than yeah') #değil yazmaz yani
else:
    print('yeah is beggie than x')
"""

"""
#peki x ve y aynı değer olup kod aynı kalsaydı 
# elsedeki değer saçma şekilde yine çıkardı
#bunu düzeltmek için operatörü değiştirip if x >= y: yapabilirsin
#ama bunu için elif komutunu kullanmak daha mantıklı
x = 20
y = 20 
if x > y:
    print('x is bigger than yeah') #değil yazmaz yani
elif x == y: #diye bi sorumuz olsun
    print('x and yeah the same equal') 
#koşul fazlalaştıkça her bi durumu kontrol etmek için elif komutunu da aynı şekilde artırabiliriz
else:
    print('yeah is beggie than x')
"""

"""
#kullanıcıdan alırsak peki
x = int(input('x: ')) #inputtan gelen değer str algılanmasın diye int
y = int(input('y: '))
if x > y:
    print('x is bigger than yeah')
elif x == y:
    print('x and yeah the same equal') 
else:
    print('yeah is beggie than x')
"""

#kullanıcıdan bi değer alalım
num = int(input('no: '))
if num > 0:    #sayı 0dan büyükse
    print('number is positive')
elif num < 0:    #sayı 0dan küçükse, pozitif değilse 
    print('number is negative')
else:  #diğer her durumda ise
    print('number is null/zero')
