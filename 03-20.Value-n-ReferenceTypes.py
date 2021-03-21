#value & reference data types
#bi veri tipi bi değişken bi obje tanımladığımız zaman 
# pc üzerinde yani bellek üzerinde nasıl değerlendiriliyor
x = 5
y = 25

x = y #değişkenleri eşitlersek

y = 10 #y 10 olduğunda x etkilenir mi? hayır
print(x,y)   #x 25 çıktı y ise 10 olarak kaldı

#bellek üzerinde tanımladığımız iki farklı değişken ile ilgili
#çünkü ikisi farklı alanda tanımlanan bi veri tipi
#bunlara VALUE TYPE denir 
# Value type -> string ve number(float, integer) veri tiplerini kapsar

#REFERENCE TYPE -> ikinci grubumuz
# -> bir list ya da class yapısı olabilir
a = ['thriller', 'science fiction', 'drama']
b =  ['thriller', 'science fiction', 'drama']   #aynı şekilde burda da kullan

a = b #a list e b yi atmış olalım
#atama sonrası değişiklik yaparsak
b[0] = 'action' #sıfınrıncı indexdekini değiştirirsek

print(a, b)  #yani sonuç: b üzerinde yapılan değişiklik a listesini de etkiledi
#value ile refence arasındaki fark refence da ikiside aynı adresi taşıyor
#referens da adresler bellekte eşitleniyor. 
# bu yüzden aynı adrsi gösterdiği için aynı bilgiler kaşımıza çıkar
# örnek olarak elimizde bi ürün listesi var
# 5000 elemanlı bi ürün listesi
#dictionarydeki adı fiyatı özellkleri gibi bi liste
#listeyi kopyalayacaksan bellek perform açısından kötü bi durum 
#yani bi kopyalama isteğinde adresi kopyalayalım kopyasını değil
#o adresteki bilgi istendiğinde ilk tanımlanan 500 ürün gelsin
#kullanıcı için ideal olan bu

#value type - kendisiyle
#reference type  - adresiyle ilgilenir





