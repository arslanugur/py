#for dögüsü neden kullanılır
#listeler için olabilir

""""1
numbrs = [1, 2, 3, 4]
print(num[0])
print(num[1])
print(num[2])
print(num[3])"""
#döngüsüz şekli bu

#döngülü
"""2
numbrs = [1, 2, 3, 4]
for num in numbrs:
    print(num) #for döngüsünün kapsamı içinde bi kod yazıyoruz
#listedeki her elemanı (değişken)num içine at ve for içerisinde döndür
for a in numbrs: #listenin elemansayısı kadar for döngüsü döner
    print('1den 4e kadar life yazıldı')
"""
"""3
names = ['Joseph', 'George', 'Daniel', 'Arslan', 'Victor']

for name in names:
    print(f'My name is {name}')
"""

#peki string bi ifade yazdırırsak
"""4
name = 'Arslan Ugur' #her bir eleman bi dizi elemanı olark değerlendirilir
for n in name:
    print(n) #her bi eleman tek tek alta yazılır
"""

"""5
tuple = (1, 2, 3, 4, 5)
for t in tuple:
    print(t)

tuple = [(1, 2),(3, 4),(5, 6), (7, 8)] #her bi liste elemanı bi tuple listeisne karşılık geliyor
for t in tuple:
    print(t)

tuple = [(1, 2),(3, 4),(5, 6), (7, 8)] 
for a, b in tuple:
    print(a) #sadece aya karşılıkları yazdırır
"""

"""6
#dictionary listesi {key : value}
d = {'k1': 1, 'k2': 2, 'k3': 3} 
for item in d:
    print(item) #bu şekilde sadece key bilgiler gelir

for item in d.items(): #şimdi eleman gruplarına tek tek ulaşırız
    print(item)

for key, value in d.items():
    print(key)

for key, value in d.items():
    print(key, value)
"""


list = [1, 2, 3]
for var in list:
    print(var) #alt alta yazdırır
