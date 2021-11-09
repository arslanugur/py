
numbers = [1,3,5,7,9,11,13,15]

#1 Sayılar listesindeki hangi sayılar 3'ün katı?
"""
for number in numbers: 
#listedeki tüm sayılar number değişkeninde olacak böylece 3ün katımı kontrol edilebilecek
#mod kullanıyoruz üçe  kalan 0 ise sayı 3ün katı
    if (number%3==0): 
        print(number)
"""

#2 sayılar listesindeki sayıların toplamı kaç?
"""
total = 0 #bu değişkene sayılar gelecek tek tek
for number in numbers: #aynı şekilde listeyi tek tek dolaşmamız gerek
#her gelen bi sayı bilgisi toplam değişkenine alınır ama öncesinde toplam formülü for döngüsüne girmeden tanımlanmalı
    total += number #long ver. --->  total = total + number
#toplam şuan ama döngü başladığında toplam 1 olacak
#ve formül devreye girince de 1 olan toplam 
# listedeki ikinci sayı ve 1 olan toplamla toplanıp, 
# bize yeni toplamı vercek ve döngü bu şekil devam edecek
print('tootal: ', total)
"""

#3 sayılar listesindeki tek sayıların karesini al
"""
for number in numbers:
#bi sayının tek olup olmadığını nasıl anlarız 
# o anki döngüden gelen sayının (number %2 == 0) ise çift
#ancak teke ihtiyacımız var bu yüzden dönen değer 1 mi demek gerek
    if (number %2 == 1):
#eğer sayı tek ise o anki ulaşılan sayının karesi alınır
        print(number ** 2)
"""


#4 Şehirlerden hangileri en fazla 6 karakterli?
"""
cities = ['Angeles', 'Berlin', 'London', 'Amsterdam', 'Tokyo']
#diziyi tek tek dolaşmamız gerekiyor yine
for city in cities:
    if (len(city) <= 6):
        print(city)
#gelen şehrin karakter sayısı alınır len ile
#6ya eşit ya küçük iseeee print ile şhri yazdır
"""


#6 Ürünlerin fiyatları toplamı nedir?
#7 ürünlerden fiyatı en fazla 5000 olan ürünleri göster

products = [
    {'name': 'Samsung s5', 'Price': '3000' },
    {'name': 'Samsung s6', 'Price': '4000' },
    {'name': 'Samsung s7', 'Price': '5000' },
    {'name': 'Samsung s8', 'Price': '6000' },
    {'name': 'Samsung s9', 'Price': '7000' }
]
#her bi liste elemanı dictionary veri tipinde
#her zamanki gibi for ile bi dolaşalım

#6 Ürünlerin fiyatları toplamı nedir?
"""
total = 0 #toplamı tutcağımız için bi değişken tanımlayalım
for product in products:
    #print(product) yazdırırsak her bi dic veritipi liste içinden çıkar ve bi satır şeklindeyazılır
    # eğer aşağıdaki gibi yaparsak 
    #print(product[price]) #sadece fiyat çıkar
#o anki gelen ürünlerin fiyatları str türünden int e çevirmemiz gerek
    pris = int(product['Price'])
#ve toplam formulünü uygulayalım
    total += pris
#döngüden çıktıktan sonra yazdır total formülün altına print edersek her seferinde yazdırır bu gereksiz
print(total) #ya da print('toplam ürün fiyatı', total)
"""


#7 ürünlerden fiyatı en fazla 5000 olan ürünleri göster
for product in products:
    if (int(product['Price']) <= 5000):
        print(product['name']) #o anki ulaştığımız ürünün ismine ulaşacaz
#5bin altındaki ürünler çıkacak


