#1  girilen bi sayının 0-100arasınolup olmadığını kontrol et
"""
num = float(input('number: '))
result = (num > 0) and (num <= 100)
print(f'number is between zero and hundred?: {result}')
"""
""" #if bloklu hali
#bunu ilk gördüğümüzde ifi kullanamıyorduk, şimdi ise olacak
num = float(input('number: '))
if (num > 0) and (num <= 100):
    print('number is between 0 and 100.')
else:
    print('number is not between 0 and 100.')

"""

#2  girilen bir sayının pozitif çift sayı olup olmadığını kontrol et
"""
num = int(input('number: '))
result = (num > 0) and (num % 2 == 0)
print(f'Number is positive and even number? {result}')
"""

#if bloklu hali
"""
num = int(input('number: '))
if (num > 0):
    if num % 2 == 0: #sayı pozifse içerde bi soru daha tru cevabıysa sayı 0dan büyük
        print(f'{num} is positive and even number.')
    else:
        print(f'{num} is positive but its odd.')
else:
    print(f'{num} is negative number.')
#peki ya sayı 0 ya da -2 olursa
#onu daha sonra incele
"""
#3  mail ve password bilgileriyle giriş kontrolü yap
"""
mail = 'arslangmail.com'
password = '1234'

writtenMail = input('mail: ')
writtenPass = input('pass: ')

result = (writtenMail == mail) and (writtenPass == password)
print(f'Entrance is success. {result}')
"""
#if hali
"""
mail = 'arslan@gmail.com'
password = '1234'

writtenMail = input('mail: ')
writtenPass = input('pass: ')

if writtenMail == mail:
    if writtenPass == password:
        print('Entry is successful.')
    else:
        print('Password is wrong.')
else: #aksi durumda
    print('Mail is wrong')
"""

#4  girilen üç sayıyı büyüklük olrak karşılaştır
"""
firstNo = int(input('1st Number: '))
secondNo = int(input('2nd Number: '))
thirdNo = int(input('3rd Number: '))

result = (firstNo > secondNo) and (firstNo > thirdNo) 
print(f'1st Number is the biggest number. {result}')
result = (secondNo > firstNo) and (secondNo > thirdNo)
print(f'2nd Number is the biggest number. {result}')
result = (thirdNo > firstNo) and (secondNo < thirdNo)
print(f'3rd Number is the biggest number. {result}')
"""
#if hali 
"""
firstNo = int(input('1st Number: '))
secondNo = int(input('2nd Number: '))
thirdNo = int(input('3rd Number: '))

if (firstNo > secondNo) and (firstNo > thirdNo):
    print(f'{firstNo} is the biggest number.')
elif (secondNo > firstNo) and (secondNo > thirdNo):
    print(f'{secondNo} is the biggest number.')
elif (thirdNo > firstNo) and (secondNo < thirdNo):
    print(f'{thirdNo} is the biggest number.')
"""

#5 user'dan iki vize (%60) ve bir final (%40) notu olarak ortalama hesapla
"""
visa1 = float(input('visa1: '))
visa2 = float(input('visa2: '))
final = float(input('final: '))

average = ((visa1 + visa2) / 2) * 0.6 + (final * 0.4)
result = (average >= 50) or (final >= 70)
print(f'Öğrenci ortalası {average} ve geçme durumu {result}')
"""

#if hali
"""
visa1 = float(input('visa1: '))
visa2 = float(input('visa2: '))
final = float(input('final: '))

average = ((visa1 + visa2) / 2) * 0.6 + (final * 0.4)

#ilk altern
if (average >= 50):
    if (final >= 50): #bu da başarılıysa tamam
        print(f'Öğrenci ortalası {average} ve geçme durumu başarılı')
    else:
        print(f'Öğrenci ortalası {average} ama final notu <50 başarısız')
else: 
    print(f'Öğrenci ortalası {average} ve geçme durumu ort. yüzünden başarısız')
#ortalama 50den büyükse final notuna baksın
"""

#ikinci altern
"""
if (average >= 50): #eğer ortalama 50den büyükse final notuna bakılmadan başarılı
    print(f'Öğrenci ortalası {average} ve geçme durumu başarılı')
else:
    if (final >= 70):
        print(f'Öğrenci ortalası {average} ama final notu en az 70 olduğundan geçtin')
    else:
        print(f'Öğrenci ortalası {average} ve geçme durumu ort. yüzünden başarısız')

"""


#6  user'dan ad, kilo, boy bilgileri alıp kilo indeksini hesapla
#   Formula: (kilo / length root) ->boy uzunluğunun karesi
#   Aşağıdaki tabloya göre kişi hangi gruba girer
#   0-18.4      => Zayıf
#   18.5-24.9   => Normal
#   25.0-29.9   => Fazla kilolu
#   30.0-34.9   => Şişman (Obez)
"""
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
#herindex için 4 tane mesaj oluyordu ama if bloklarıyla
"""
#if hali
name = input('Name: ')
kg = float(input('Kilo: ')) #kg/boy ondalıklı da girebilir bu yüzden float
hg = float(input('Length: ')) #userdan ekran ondalıklı yazması istenir örnek gösterilir

kiloindex = (kg) / (hg**2) #verdiğimiz formül

if (kiloindex >= 0) and (kiloindex <= 18.9):
    print(f' {name} kilo indeksin: {kiloindex} ve kilo değerlendirmen zayıf.')
elif (kiloindex >= 19.0) and (kiloindex <= 24.9):
    print(f' {name} kilo indeksin: {kiloindex} ve kilo değerlendirmen normal.')
elif (kiloindex >= 25.0) and (kiloindex <= 29.9):
    print(f' {name} kilo indeksin: {kiloindex} ve kilo değerlendirmen şişman.')
elif (kiloindex >= 30.0) and (kiloindex <= 39.0):
    print(f' {name} kilo indeksin: {kiloindex} ve kilo değerlendirmen obez.')
else:
    print('Bilgiler yanlış.')