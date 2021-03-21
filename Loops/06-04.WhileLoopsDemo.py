
#1 numbers listesini while ile ekrana yazdır
    # for ile daha kolay ama while ile de yapılabilir
"""
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
for i in numbers:
    print(i)   #bu kadar kolay işte
"""

"""
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
i = 0
while (i < len(numbers)): #böylece hile true değerine ulaşılır
# numbers 0 ya da 1. indexlemeyle elemanlara tek tek ulaşılır numbers[0]
# ama indexlerken 0.cı eleman için i yazılır
    print(numbers[i]) #ulaştıktan sonra yanına print
    #yazdıktan sonra i'yi bi artırmalısın ki i'yi 1 yerine saymasın
    i += 1 #iyi her turda 1 artırıcaz ki birer birer listedeki alemanlara yaklaşıp true değerine ulaşcak
# True = i sayısı numbersların eleman sayısından küçü old sürece dönerse
#while döngüsünün yanında true getirecek olan bi koşul/yapı olması gerekli
#sayılar listesinin eleman sayısı kadar dönmesii dolayısıyla bi kontrol değişkeni tanımla i = 0
"""



#2 Başlangıç ve bitiş değerlerini userdan alıp aradaki tüm tek sayıları ekrana yazdır
"""
begin = int(input('begin: '))
end = int(input('end: '))
#tabi yukarıda bağlangıç bitişten az olmalı gibi kontroller/sorgulamalarda yapılabilinir
#i adıyla kontrol değişkeni tanımlarsak
i = begin #i başlangıçtan başlar yani başlangıcın değerini iye sakladık, her seferde başlangıcın değerini artırmak yerine i nin değeri artsın
while i < end: #begin end den az old sürece olabilir
    i += 1 #içerik birer birer artar ve bitişe kadar gider
#ne zamanki bitişe gelip false değer verdiğinde while döngüsü de bitecek
    #if i % 2 == 0: #sadece çiftleri yazdırır, alttaki print de tab edilir
    print(i) #user mesela 5'den başlasın 10a kadar gitsin dedi
#başlangıç değerini dahil etmez, ama bitişi dahil eder
"""

#3 1-100 arasındakisayıları azalan şekilde yazdır (CEVAP YORUMLARDA)
"""
i = 0 #kontrol değişkeni 0 yerine 100 yaparsak
#başlangıç değeri 100 olur
while i < 100: #koşul ise while i > 0: olur
    print(i) #i 0dan 100e kadar gider. ama tersten nasıl
    i +=1 #yerine i -= 1 yaz. Kontrol değişkeni böyle bi yol izliyor 
"""


#4 userdan aldığın 5 sayıyı ekranda sıralı şekilde yazdır
"""
numbers = [] #aldımız her bi sayıyı bi yerde saklamak için, sıralayıp ekraa böylee yazdırabiliriz
i = 0 #kontrol değişkeni tanımla 0dan başlat
while i < 5: #i 5den kğçğk old sürece bir döngümüz olsun
    number = int(input('number: '))    #döngünün her seferinde de userdan bi bilgi alalım
#sonrası input komutunu number adında bi değişken yap, sayısal olarak bi sıralama olacağı için str değil int
    numbers.append(number)  #verdiği sayı değişkenini ise append ile her seferinde ekleyelim
    i += 1
numbers.sort() #üsteki işlemler bittikten sonra bunları sırala
print(numbers) #girilen sayılar liste içinde saklanacak artık
"""

#5 userdan aldığınız sınırsız ürün bilgisini ürünler listesi

#    **ürün sayısını usera sor
#    **dictionary listesi yapısı (name, price) şeklinde olsun
#    **ürün ekleme işlemi bittiğinde ürünler ekranda while ile 

products = [] #products adında bi dizi tanımla
#her bir veriyi bi dict objesine tanımlıcak, in önce usera adet bilgisini sormak gerekir

quantity = int(input('How many products you wanna add?: '))

i = 0

while i < quantity: #adet kadar döner
    name = input('Product name: ') #her seferde usera ürün bilgilerini sor
    price = int(input('Product price: '))
    products.append({
        'name' : name,    # virgülü unutma!!!
        'price' : price  #dict 
    })
    i += 1 #adet kadar ekleyeğiz çünkü

#peki ürünleri nasıl listeleriz
for product in products:
    print(f'Ürün Adı: {product["name"]} Ürün fiyatı: {product["price"]}')
#dışarda tek tırnak kllanıyrsan içerde de çift tırnak kullanman gerek
