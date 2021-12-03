# Example: 
# 1 girilen iki sayıdan hangisi büyük
numbera = int(input('number a: '))
numberb = int(input('number b: '))

result = numbera > numberb #true-false gelcek - true olursa a değeri büyük
print(f'number a: {numbera} number b: {numberb} den büyük: {result}') 
#süslü parantez sayı değerini vercek
#true ya da false değeri kullanıcıya gösterilmez ama
"""

"""
#2 kullanıcıdan iki vize (%60) ve bir final (%40) notu al ortalama hesapla

vize1 = float(input('1st midterm: '))
vize2 = float(input('2nd midterm: '))
final = float(input('final: '))

# aldığımız bilgiyi floata çevir çünkü ondalıklı bi sayı da girilebilir

#3 ortalama 50 ve üstündeyse geçti değilse kaldı yazdır
#üsteki bilgilerin ortalaması
average = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f'Not ortalamanız: {average} ve dersten geçme durumunuz: {average>=50} ')
#50den büyük ya da eşitse geçti/true, altında ise kaldı/false
#bu konuları if bloklarında daha sağlıklı görcen
"""

"""
#4 girilen bir sayını tek mi çift mi olduğunu yazdır

number = int(input('number: '))

oddeven = (number % 2 == 0)
#girilen sayının mod2 sini aldığımızda sonuç sıfıra eşitse sayı çift yani bölüne bölüne 0 kalır
print(f'girilen sayının çift olma durumu: {oddeven}')
"""

"""
#5 girilen bir sayının pozitif negatif durumunu yazdır

number = int(input('number: '))
positive = (number > 0) #true gelirse demek ki pozitif, eksi değer girilirse false
print(f'girilen sayının pozitif olma durumu: {positive}')
"""

#6 parola ve mail bilgisi iste, doğruluğunu kontrol et
# arslan@gmail.com password: arslan --> bunlar kullanıcının kaydı ve database de durur
email = 'arslan@gmail.com' 
password = 'arslan'

girilenMail = input('email: ') #zaten str olsuğu için dönüşüm yapmak gereksiz
girilenPass = input('password: ')

isMail = email  == girilenMail
#isMail = (email  == girilenMail.lower()) #yanlışlıkla büyük yazılabilir diye otomatik küçültür
#isMail = (email  == girilenMail.lower().strip()) #yanlışlıkla hem büyük hem de sonda boşluk bırakırsa düzeltir
#str başına yanına sonuna girdiğimiz boşluklar strip metoduyla silinir
isPass = password == girilenPass    #bu sorulara true ya da false gelcek
print(f'Email bilgisi doğrumu: {isMail} ve parola doğru mu: {isPass} ')




