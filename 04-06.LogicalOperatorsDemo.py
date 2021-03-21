"""
#1 girilen bir sayının 0-100 arasında olup olmadığını bul
#sormamız gereken iki soru 0dan büyük mü 100den küçük mü
number = float(input('x = '))
result = (number > 0) and (number <= 100)
#iki koşulumuz var her ikisi de doğru olmak zorunda 'and'
print(f'Number is between 0 and 100: {result} ')

"""
#2 girilen bir sayının poz çift sayı olup olmadığını kontrol et
#1 ve 2.soruyu bir operator içinde birleştir
"""
number = int(input('x = '))
result = (number > 0) and (number % 2 == 0) 
#sayı mod2 = 0 ise çift
print(f'Is your number both positive and even: {result} ')
"""

"""
#3 mail ve parola bilgileriyle giriş kontrolü yap
#mailiniz ya da parolanız false diye tek bir mesajla bildirilebilir
mail = 'arslan@gmail.com'
password = 'abc123'

writtenMail = input('Mail: ')
writtenPass = input('Pass: ')

result = (writtenMail == mail) and (writtenPass == password)
#ikisi de eşit olmalı ki kullanıcı sisteme giriş yapabilsin. bunu da result'a eşitle
print(f'Is entrance successful: {result}')
"""

"""
#4 girilen ü ç sayıyı büyüklük olarak karşılaştır
firstNo = int(input('1st Number: '))
secondNo = int(input('2nd Number: '))
thirdNo = int(input('3rd Number: '))
#a b ve cden büyük olmalı ki en büyük sayı diyelim
result = (firstNo > secondNo) and (firstNo > thirdNo) 
print(f'1st Number is the biggest number. {result}')
# bnin büyüklüğünü kontrol edersek
result = (secondNo > firstNo) and (secondNo > thirdNo)
print(f'2nd Number is the biggest number. {result}')
# cnin büyüklüğünü kontrol edersek
result = (thirdNo > firstNo) and (secondNo < thirdNo)
print(f'3rd Number is the biggest number. {result}')
#burda terminale 3 tane sayıy yazmak zorundayız yine çünkü if bloklarınıhenüz görmedik
"""

"""
#5 user'dan iki vize (%60) ve bir final (%40) notu olarak ortalama hesapla
#   eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdır
#   a) Ortalama 50 olsa bile final notu en az 50 olmalı
visa1 = float(input('visa1: '))
visa2 = float(input('visa2: '))
final = float(input('final: '))

average = ((visa1 + visa2) / 2) * 0.6 + (final * 0.4)
#geç kalı bize söyleyecek olan bi bool türüne result değeri oluştur
#result = (average >= 50) and (final >= 50) 

#   b) Finalden 70 alındığında ortalamanın önemi olmasın
result = (average >= 50) or (final >= 70)
print(f'Öğrenci ortalası {average} ve geçme durumu {result}')
#hiç ortalamaya bakıllmadam geçecek
"""

#6 user'dan ad, kilo, boy bilgileri alıp kilo indeksini hesapla
#   Formula: (kilo / length root) ->boy uzunluğunun karesi
#   Aşağıdaki tabloya göre kişi hangi gruba girer
#   0-18.4      => Zayıf
#   18.5-24.9   => Normal
#   25.0-29.9   => Fazla kilolu
#   30.0-34.9   => Şişman (Obez)

name = input('Name: ')
kg = float(input('Kilo: ')) #kg/boy ondalıklı da girebilir bu yüzden float
hg = float(input('Length: ')) #userdan ekran ondalıklı yazması istenir örnek gösterilir
#userdan bilgileri aldık
kiloindex = (kg) / (hg**2) #verdiğimiz formül

thin = (kiloindex >= 0) and (kiloindex <= 18.4)
normal = (kiloindex >= 18.5) and (kiloindex <= 24.9)
fat = (kiloindex >= 25.0) and (kiloindex <= 29.9)
obes = (kiloindex >= 30.0) and (kiloindex <= 34.9)

print(f' {name} kilo ideksin: {kiloindex} ve kilo değerlendirmen zayıf {thin}')
print(f' {name} kilo ideksin: {kiloindex} ve kilo değerlendirmen normal {normal}')
print(f' {name} kilo ideksin: {kiloindex} ve kilo değerlendirmen şişman {fat}')
print(f' {name} kilo ideksin: {kiloindex} ve kilo değerlendirmen obez {obes}')

#koşullu İF ifadeleri gördümüzde daha kaliteli bi kod yazcaz