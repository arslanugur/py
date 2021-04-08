names = ['Lincoln', 'Franklin', 'Roosevelt', 'Nixon']
years = [1933, 1969, 1764, 1861]


names.append('Kennedy')          #'Kennedy' ismini liste sonuna ekle
names.insert(0, 'Washington')    #'Washington' listenin başına ekle
names.insert(len(names), 'Bush') #append gibi değil, index istiyor. ama append gibi sona ekleme de yapılabilir
print(names) 

names.remove('Franklin')         #'Franklin' ismini listeden sil
names.pop()                      #bi indeks vermediğin zaman listenin sonundaki elemanı siler
print(names)

index = names.index('Roosevelt') #indexini gösterir
print(index)

names.pop(index)    #aldığın indexe göre elemanı silmek istersn
print(names)

result = 'Washington' in names # 'Washington' listenin bi elemanı mı #in names, true false verir
#diğer yol: result = names.index('Washington') #eğer terminaldeki index numarası -1 değilse true
print(result)

names.reverse()      #liste elemanlarını ters çevir
print(names)

names.sort()         # liste elemanlarını alfabetik olarak sırala
print(names)

years.sort()         # years listesini rakamsal büyüklüe göre sırala
print(years)

str = 'Obama, Trump' # str = 'Obama, Trump' karakter dizisini listeye çevir
result = str.split(',')
print(result)

min = min(years)     # years dizisinin en büyük ve en kçük elemanı ne
max = max(years)
print(min, max)

result = years.count(1764)   # years dizisinde kaç tane '1764' değeri var
print(result)


years.clear()   # years dizisinin tüm elemanlarını sil
print(years)


# kullanıcıdan aldığın üç tane başkan bilgisini bi listede sakla
presidents = [] #boş bi obje tanımladık
president = input('presidents: ') #input yaz daha sonra bunu president isimli bir değişkene ata
presidents.append(president) #aldığımız bu bilgiyi dizi üzerine append edelim
print(president) #kullanıcı input sayesinde ekrana başkanları girecek
#print(presidents) şeklinde yazsaydık bize liste şeklinde bilgi verir

#bunu üç kere yaparsak amatörce olacak çünkü, döngüleri(loops) kullanmak daha iyi 3 kere kopyalamak zorunda kalmazdık
president = input('presidents: ') 
presidents.append(president)
print(presidents) 
#3 farklı başkanı girdikten sonra bunu liste yapar
