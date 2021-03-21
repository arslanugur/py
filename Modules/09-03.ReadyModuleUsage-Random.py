
#random.py diye modül isminden dosya ismi olmaz hata alırsın, bu yüzden _random.py gibisinden isimlendirmen gerek

import random

# result = dir(random)
# result = help(random)
"""
#Random Metodları
result = random.random() #böylece 0.0 ile 1.0 arasında rasgele bi ondalıklı sayı üretebiliriz
#her çalıştırdığımızda farklı bi sayı
result = random.random() * 100 #aralığı artırabiliriz #üretilen sayılar her seferinde 100 ile çarpılacak
#ya da sonuna + 10 diyerek 10dan başlatabiliriz
result = random.uniform(1, 10) #iki tane parametre bekler ki arasında ondalıklı bi sayı üretir
result = int(random.uniform(1, 20)) #ondalıklı kısmıyla ilgilenmiyoruz
#diğer şekliyle
result = random.randint(1, 20) #int metoduyla aynı
print(result)


#örnk olarak elimizde names listesi olsun ve içinden rasgele bi elemanı almak istiyoruz
#bu arada, piyango için ideal bi hesaplama yöntemi olabilir

names = ['Richard', 'Henry', 'William', 'James', 'John'] #len olduğu için ne kadar eklersek ekleyelim hata vermez
result = names[random.randint(0, len(names)-1)] #index bilgisi verirsek o eleman gelir
#yani burda yapmamız gerekn 0 ile 3 indexi arasında bi sayı üretiyor olmamız gerekiyor
#yani index 4 olamaz out of range olur
#liste dinamik bi liste ise içinde kaç elemanın old henüz bilinmiyorsa
# ya da databaseden geliyorsa bu durumda listenin genişliğini de eleman sayısını da işin içine katıyor olmak gerek
# şimdi yularda deneyelim randomu
# 0 ile 3 diyebiliriz ama 3ü burda dinamik olarak üretceğimizi varsayarsak olmaz bu yüzden len deriz
#ve listenin eleman sayısını böylece alırız
# -1 dedik çünkü 4 sayısı üretirse bu olmuyor
print(result)
"""
"""
#diğer yol
result = random.choice(names) #choice metoduna listeyi veriyoruz o işi bizim yerimize lensiz hallediyor

greeting = 'Hello There'
result = random.choice(greeting)
##greetin içindeki her bi elemanı bi karakter olarak tanımlar str olsa bile
print(result)
"""

#yeni bi liste üretelim  #dikkat tanımlayalım demiyorum tanımlarsam names listesi gbii olur

myList = list(range(10)) #0 ile 10 arasında 10 elemanlı bi liste üretelim
random.shuffle(myList) #bu listeyi random yapmak istersek, her çağırdıımız random olur
result = myList #10 elemanlı bi liste karşımıza gelir
print(result)

myList2 = range(100) #0dan 100e kadar giden bi liste üretelim ama liste çevirmeyelim
result = random.sample(myList, 3) #belirttiğimiz liste içinden istediğimiz eleman kadar bi bilgi talep ediyoruz
#rasgele üç sayı gelecek
#ya da rasgele iki isim result = random.sample(names, 2)
print(result)




#Random metodalrını araştır


