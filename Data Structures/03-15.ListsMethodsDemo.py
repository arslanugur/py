names = ['Lincoln', 'Franklin', 'Roosevelt', 'Nixon']
years = [1933, 1969, 1764, 1861]

# 'Kennedy' ismini liste sonuna ekle
names.append('Kennedy')
print(names)
# 'Washington' listenin başına ekle
names.insert(0, 'Washington') 
names.insert(len(names), 'Bush') #append gibi değil, index istiyor. ama append gibi sona ekleme de yapılabilir
print(names) 
# 'Franklin' ismini listeden sil
names.remove('Franklin')
#names.pop() bi indeks vermediğin zaman listenin sonundaki elemanı siler
print(names)
# 'Roosevelt' isminin indexi ne
index = names.index('Roosevelt')
print(index)

names.pop(index)    #aldığın indexe göre elemanı silmek istersn
print(names)
# 'Washington' listenin bi elemanı mı
result = 'Washington' in names #result varsa true false var
#diğer yol: result = names.index('Washington') #eğer terminaldeki index numarası -1 değilse true
print(result)
# liste elemanlarını ters çevir
names.reverse()
print(names)
# liste elemanlarını alfabetik olarak sırala
names.sort()
print(names)
# years listesini rakamsal büyüklüe göre sırala
years.sort()
print(years)
# str = 'Obama, Trump' karakter dizisini listeye çevir
str = 'Obama, Trump'
result = str.split(',')
print(result)
# years dizisinin en büyük ve en kçük elemanı ne
min = min(years)
max = max(years)
print(min, max)
# years dizisinde kaç tane '1764' değeri var
result = years.count(1764)
print(result)
# years dizisinin tüm elemanlarını sil
years.clear()
print(years)
# kullanıcıdan aldığın üç tane başkan bilgisini bi listede sakla

presidents = [] #boş bi obje tanımladık

president = input('presidents: ') #input yaz daha sonra bunu president isimli bir değişkene ata
presidents.append(president) #aldığımız bu bilgiyi dizi üzerine append edelim
print(president) #kullanıcı input sayesinde ekrana başkanları girecek
#print(presidents) şeklinde yazsaydık bize liste şeklinde bilgi verir
#bunu üç kere yap ama döngüleri(loops) kullanmadan yap 3 kere kopyalamak zorunda kal
president = input('presidents: ') 
presidents.append(president)
print(presidents) 
#3 farklı başkanı girdikten sonra bunu liste yapar
