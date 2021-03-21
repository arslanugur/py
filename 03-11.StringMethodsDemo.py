website = 'http://www.arslanugur.com'
course = 'English Course: To the end (40 Hours)'


# 1  ' Hello World ' karakter dizisinin başında ve sonunda boşluk karakterilerini sil
result = ' Hello World '.strip()
result = ' Hello World '.lstrip() #soldaki boş karakterleri sil
result = ' Hello World '.rstrip() #sağdaki boş karakterleri sil
result = website.lstrip('thp/:') #solundaki belli ettiğin karakterleri siler

# 2  'www.arslanugur.com' arslanugur bilgisi hariç her karakteri sil
result = 'www.arslanugur.com'.strip('w.omc')

# 3  'course' karakter dizisinin tüm harflekarakterleri küçük harf yap
result = course.lower()
result = course.upper() #bütün harfler büyük olur
result = course.title() #her kelimenin baş harfi büyük olur

# 4  'website' kaç kane a karakteri var? (count('a'))
result = website.count('a')
result = website.count('u',0,10) #0 ile 10 arasında bi arama alanı belirtiyoruz burda bulursa çıkar

# 5  'website' www ile başlayıp com ile bitiyor mu?
result = website.startswith('www') #yanlış, hayır
result = website.startswith('http') #true olur
result = website.endswith('com') #evet

# 6  'website' içinde '.com' ifadesi var mı?
result = website.find('.com') #bunun yerine .count strigini de kullanabilirdik ama .find daha iyi
#index numarasını gösterecek 21 gibi
result = website.find('.com',0,20) #varsa indexi gösterir yoksa -1
result = course.find('English') #sıfırıncı indexden başlar burdan itibaren başlıyor
result = course.rfind('English') #sağdan saymaya başlayıp index numarasını ordan verir
result = website.index('.com') #alrenatif yol
result = website.rindex('.com')
#eğer aradığımız değer yoksa -index stringinde error verir, find stringinde -1 olur
#exception- hata objesine karşılık gelen bi ifade

# 7  'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha() #false demek ki değil
result = course.isdigit() #alse demek ki bu da değil
result = 'hello'.isalpha() #helo diye değişkin tanımlayıp alfabet mi true olur
result = '123'.isdigit() #true olur

# 8  'Contents' ifadesini satırda 50 karakter içine yerleştir, sağ ve sola * ekle
result = 'Contents'.center(50)
result = 'Contents'.center(50,'*')
result = 'Contents'.ljust(50,'*') #leftjust ifadesi ile
result = 'Contents'.rjust(50,'*')

# 9  'course' karakter dizisindeki tüm boşluk karakterleri '-' ile değiştir
result = course.replace(' ', '-')
result = course.replace(' ', '-',3) # sınırını 3 karakter olarak belirleriz
result = course.replace(' ','') #tüm boşluk karakterlerini siler

# 10  'Hello World' karakter dizisinin 'World' karakterini 'There' ile değiştir
result = 'Hello World'.replace('World','There')

# 11  'course' karakter dizisini boşluk karakterlerinden ayır
result = course.split(' ') 
#boşluk karakterlerinden ayırdı ve karşımıa DİZİ geldi
result = result[2]
#0 = English 1= Course oluyor

print(result)
