#lambda fonksiyonları ve onun map ve filter metodları
"""
def square(num): return num ** 2 #aynı satır içinde de yazabiliriz
#number bilgisi alan kare alma fonksiyonu, return ile bize geri göndersin

result = square(2)
print(result)
#gönderdiğimiz sayının karesini alır göndenrir
"""

"""
def square(num): return num ** 2 

numbers = [1, 3, 5, 9] #bi liste olsaydı bu sayıların hepsinin karesini alırsak
#bunu for dönüsüyle de yapabiliriz ama map diye bi metod var
result = list(map(square, numbers)) #map(square, numbers) liste ya da for döngüsüyle yapılabilir 
#numbers içerisindeki her bi değeri tek tek fonka gönderilir
#ve square metodu içinde işlem gördükte sonra return edilir ve list şeklinde yazılır
#list yazmadan önce bellek üzerinde bize bi adresle döner yazdırır, 
# yani mapden dönen sonuç listeye çevrilir  
print(result)

# diğer bi yolu ise for döngüsü oluşturması
for item in map(square, numbers):
    print(item) #bu durumda da yine

#önemli: map metodunun ya bi liste ile ya da for döngüsüyle enumerate edilmesi gerekiyor
"""

"""
#fonksiyonu yorum satırı yaptığını düşün
# ismi olmayan anonymus bi fonksiyon tanımlayabiliriz...
numbers = [1, 3, 5, 7]
result = list(map(lambda num: num ** 2,numbers))
# fonka giriş olan değer aynen yukardaki gibi tanımlanır 
# bi return ifadesi kullanmadan bunun karesini alabiliriz
# map görevi dizinin elemanlarını fonksiyona tek tek göndermek
print(result) #artık square metodu ya da for döngüsü olmadan aynı şekilde listelenmiş bi sonuç alırız
#square yaptığı işlemi isimsiz bi foksiyonla yapıyoruz
"""

"""
#hatta burda tanımladığımız lambda fonksiyonuna isim de verebiliriz
square = lambda num: num ** 2 #square değişkenine atadık
#suare değişkenini başa alıp lambda yerine formülde suare yazabiliriz
"""

"""
#diğer yol 
square = lambda num: num ** 2
numbers = [1,2, 3, 4, 5, 6, 7]
result = square(3) #parametre bekler, index gibi
print(result) #3ün karesi ekranı yazdırılır
"""


"""
#bütün elemanların üzerinde işlem yapmak istiyorum 
# ancak geriye result ile tüm elemanların geriye gönderiyoruz
# şimdiki yol filter işlemi yapmak
# mesela içerisinden gelen sayıların sadece çiftlerini geri gönder. mesela tekden geriye dönmesin ya da tam tersini de düşünebiliriz
numbers = [1,2, 3, 4, 5, 6, 7]
#filter fonku ile yapabiliriz
#normal bi fonk tanımlamas yapıp lambda expressiona çevir
def checkEven(num): return num % 2 == 0 #aynı satır içinde yazmak daha iyi
#gönderdiğimiz sayının modunu al, 
# sonuç 0 ise true değer gönder, tek ise de false değeri gönder
#result = list(filter(checkEven, numbers)) 
# yerine
result = list(filter(lambda num: num % 2 == 0, numbers)) #bunula da yine aynı sonuç 
#filter yöntemiyle fonku gönder ve numbers üzeride işlem yapsın bunuda result atayıp çalıştıralım
print(result) #list içindeki tekler gelmez
"""

numbers = [1,2, 3, 4, 5, 6, 7]
checkEven = lambda num: num % 2 == 0
result = list(filter(checkEven, numbers))
#result değişkeni yorum yapıp yerine checkEven print edersek de olur
print(result)
#print(checkEven(numbers[2])) #2çindex tek olduğu için false bilgisi gönderir
