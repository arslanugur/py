#1  userdan isim, yaş ve eğitim biligilerini isteyip 
#   ehliyet alabilme durumunu kontrolet
#   ehliyet alabilme koşulu en az 18 ve eğitim durumu lise ya da üni olmalı
"""
name = input('your name: ')
age = int(input('your age: '))
degree = input('your degree: ')

if (age >= 18) and (degree == 'high school' or degree == 'university'): 
#yaş 18den büyük ya da eşit olmalı durumu ve bu bize true değeri vermeli
    print(f'{name}, you can get driving license') #f stringli
else:
    print('you cant get driving license')
"""

"""
#ancak neden alınamıyor yazmıyor bu durumda
name = input('your name: ')
age = int(input('your age: '))
degree = input('your degree: ')

if (age >= 18):
    if (degree == 'high school' or degree == 'university'): 
        print(f'{name}, you can get driving license')
    else:
        print('you cant get driving license because of degree')
else:
    print('you cant get driving license because of age')
"""


"""
#2  öğrencinin iki yazılı bir sözlü notunu alıp hesaplanan ortalmaya göre
#   not aralığına karşılık gelen not bilgisini yazdır
#    0 - 24 --> 0
#   25 - 44 --> 1
#   45 - 54 --> 2
#   55 - 69 --> 3
#   70 - 84 --> 4
#   85 - 100 --> 5

exam1 = float(input('examOne: '))
exam2 = float(input('examTwo: '))
speech = float(input('speech: '))

average = (exam1 + exam2 + speech) / 3

if (average >= 0) and (average <= 24):
    print(f'Your average is {average} and your score: 0')
elif (average >= 25) and (average <= 44):
    print(f'Your average is {average} and your score: 1')
elif (average >= 45) and (average <= 54):
    print(f'Your average is {average} and your score: 2')
elif (average >= 55) and (average <= 69):
    print(f'Your average is {average} and your score: 3')
elif (average >= 70) and (average <= 84):
    print(f'Your average is {average} and your score: 4')
elif (average >= 85) and (average <= 100):
    print(f'Your average is {average} and your score: 5')
else:  #(yukardakiler dışında herşeyse)
    print('you gave a wrong info')
#aralığımız 100 kadar bunun dışında girilen her bir bilgi yanlış
"""


#3 (kullanıcıdan) trafiğe çıkış zmanı alınan bir aracın (araç kaç gündür trafikte)
#    servis zamanını aşağıdaki bilgilere göre hesaapla 
#    (eg 20.11.2010 ile şimdinin tarihiyle fark alınır gün olarak çıkartmak gerek)
#    güne göre sorgulama yapılmalı *datetime modülü ileriki konu
#  1.bakım -> 1.yıl
#  2.bakım -> 2.yıl
#  3.bakım -> 3.yıl
#  **süre hesabına alınan gün, ay, yıl bilgisine göre gün bazlı hesapla
#  **datetime modülünü kullanmak gerekir  
"""
days = int(input('how many days your vehicle in traffic?: ')) #datetime modülü şimdilik dursun daha sonra katcaz
#gelen bilginin str olmaması için int çevir
if days <= 365: #365 günü servis aralığı olarak kabul ederiz
    print('1st service time')
elif (days > 365) and (days <= 365 *2): #yani 1 y ile 2 y arasındysa
    print('2nd service time')
elif (days > 365 * 2) and (days <= 365 *3): #yani 2 yıl ile 3 yıl arası
    print('3rd service time')
else: #bunlar haricindeki herbir süre hatalı süre bilgisini göstersin
    print('error usage in traffic')

"""

"""
#datatime modülüyle yapılırsa
import datetime #modülü import ediyoruz

date = str(input('which date did your vehicle start being in traffic? (2019/8/9): ')) 
date = date.split('/') #gelecek olan tarih bilgisi split metoduyla slashla ayrılır
print(date[0]) #yıl
print(date[1]) #ay
print(date[2]) #gün ay yıl diye aldık alt altta şekilde ayırdık
#neden ayırdık? çünkü fark işlemi yapcaz

today = datetime.datetime.now() #today değişkenine bugünün tarihini almış oluruz
#print(today) #şuanın tarihini terminale gösterir
#farkı almak için bi obje hazırlanır
# trafiğe çıkış şeklinde bi tarih objesi datetime modülüyle hazırla
entranceTraffic = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
minus = today - entranceTraffic #farkını almak için trafiğe çıkışla şimdiki tarih çıkartılır
#print(minus)
#minus yani fark değişkeni içinden days bilgisini alman gerekli
#print(minus.days) #gün bilgisi gelcek ama amacımız bu değil, bunun yerine
days= minus.days #days objesinin içine alalım yani sadece gün bilgisini alır saati filan değil
#sonrasında koşullu işlemlere geç

if days <= 365:
    print('1st service time')
elif (days > 365) and (days <= 365 *2): 
    print('2nd service time')
elif (days > 365 * 2) and (days <= 365 *3):
    print('3rd service time')
else: 
    print('error usage in traffic')
"""

#temiz bi şekilde görmek için
import datetime 

date = str(input('which date did your vehicle start being in traffic? (2019/8/9): ')) 
date = date.split('.')

today = datetime.datetime.now()
entranceTraffic = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
minus = today - entranceTraffic
days= minus.days

if days <= 365:
    print('1st service time')
elif (days > 365) and (days <= 365 *2): 
    print('2nd service time')
elif (days > 365 * 2) and (days <= 365 *3):
    print('3rd service time')
else: 
    print('error usage in traffic')