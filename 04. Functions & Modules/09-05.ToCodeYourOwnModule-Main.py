#bu dosyanın asıl ismi main.py

import mood #09-04.ToCodeYourOwnModule aslında modül sayfamız
#bunu böylece yani main.py çalıştırdığımızda modül eklendi mesajını alırız
#isim değişikliği sebebiyle hata vermesi normal

#module içinde çalıştırılabilen bi kod varsa  direk çalışr mainpy de

#modül başarılı

#şimdi modül ile bilgi alalım

#result = help(mood)
result = help(mood.func) #ya da içindeki func bi açıklaması görebiliriz
print(result) #mod dosyası hakkında bilgi kısmı
#içerisindeki bilgileri tek tek görebiliriz

#şimdi sırayla
result = mood.number
result = mood.numbers
result = mood.person['name'] #almak istediğimiz bilgi gelir
result = mood.func(10) #fonksiyon çağırma işlemi bizden bi paramete bekliyor () 10 bilgisini girelim
#x : 10 şeklinde bi bilgi

#ya da bi person objesi tanımlayıp
p = mod.Person() #mod.Person üzerinden alalım
p.speak() #obje üzerinden speak dediğimiz zaman
#ekrana direk im speaking yazdırır


print(result)


#şimdi mood modulü, main modülüyle aynı dizin içinde bulup import ettik
#aynı şekilde import math dediğimizda, kurulumun yapıldığı python klasöründe arıyor
#terminale python yazıp geçiş yapıp klasörlere bakaarsak
#import sys modülünü ekleyelim
#sys.path dediğimizde pcdeki python klasörünü bize gösteriyor
#kütüphaneyle gelen modülleri lib klasörü adı altında ekliyor
#py kurulumunu yaparken ilgili py dizinini path'e ekle diye bi checkboz vardı
#onu seçmiştik ki lib klasörü bu yüzden geldi
#lib klasörünü ziyaret edersek py ile gelen modüllerin konumuna ulaşmış oluruz
#sonuç olarak py bakarak ilgili modülü yani mood gibi bunu o konumda arıyyor

#modülleri ve modülerin birleşimi olan paketleri libde görebiliriz
#netten bulduğumuz modülleri indirip lib klasörüne atarsak py üzerinde modül eklemiş oluruz
#yine de bazı modüller libde gözükmez math gibi, ya da built in metodları, fonksiyonları bunlar hız açısından C dili ile yazılıp DLLs de kütüphane haline çevrilmesi

#peki builtinlere nasıl bakarız
#terminal - python - import sys - sys.builtin_module_names dersek builtin modules görürüz math gibi
#bunlar py uzantılı değiş C dilinde yazılmıştır


