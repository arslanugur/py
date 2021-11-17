#for döngüsüne alternative olur
"""
for x in range(10):
    print(x) #0dan 10a kadar yazdırır
#bu basit biliyoruz
"""

"""
numbers = []
for x in range(10):
    numbers.append(x)
#append ile aldığımız x değerini dizi üzerine aktarırırz
#aşağıdaki ile aynı sonuca varırız
"""
"""
#number adında bi dizi tanımla, dizi tanımlama aşamasında 
numbers = [x for x in range(10)] #birinci xin içine gelen değerler dizinin elemanlarını temsil eder
#range içerisinden 10 sayıyı for döngüsüyle tek tek x'in içine atıp bi x değeri elde edip bunları numbers dizisine atıyoruz
print(numbers)
"""

"""
for x in range(10):
    print(x**2) #altalta alır
"""
"""
numbers = [x**2 for x in range(10)]
print(numbers) #hepsinin karesini aldı liste şeklinde
"""

"""
#sadece 3e bölünenler karşımıza gelsin
numbers = [x*x for x in range(10) if x % 3 == 0] #her bi değerin karesini almak için
print(numbers)   #sadece 3e tam bölünebilen sayılar yazılır
"""

#bunları liste üzerinde nasıl tanımlarız
#str karakter tanımla
"""
myStr = 'Hallo'
myList = []  #burdan listeye çevirelim
for letter in myStr:
    myList.append(letter)
print(myList) #hallo bi dizi şekline dönüşür
"""

"""
#basit versiyonu
myStr = 'Hallo'
myList = [letter for letter in myStr]
print(myList)
"""

"""
#years isminde bi dzi tanımla
years = [1923,1945,1965,1987,1989] #her değere tek tek ulaşıp yaş bilgisini hesapla
ages = [2020 - year for year in years]
print(ages)
"""

"""
result = [x if x %2 == 0 else 'odd no' for x in range(1,10)]
#list elemanı yapmak yerine belli bi koşul eklenebilir
#birinci x dahil olması için ifli ifadenin tru değeri getirmesi gerekir. değilse tek sayı
print(result) #135 gibi sayılar için odd no yazdırdı
"""

"""
#içiçe iki döngümüz varsa
result = []
for x in range(3): #loop x için 3 kere döncek
    for y in range(3): #x 0dan başlayıp 0a geldiğinde, y 3e kadar gitcek yani y için bi loop olcak
        result.append((x,y)) #her bi eleman append ile result içine aktarılacak
print(result)
#y bittiğinde tekrar başa döncek bu sefer x 1 ile başlayıp y'ye geçecek
"""
#basitleştirirsek - yine x ve y için birer döngü
numbers = [(x,y) for x in range(3) for y in range(3)]
#x için olan for loopnunu x içine aldık (x,y)
#y için olan for loopunu y içine aldık(x,y)
print(numbers) #sonuç aynı

#3 elemanlı da olabilir
#numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]


####EXAMPLES
cubes = [i ** 3 for i in range(5)]
print(cubes)

evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)



a = [x * 10 for x in range(5,9)]
