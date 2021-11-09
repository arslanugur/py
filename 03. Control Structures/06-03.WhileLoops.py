numbers = [1, 2, 3, 4, 5]
#bunu for döngüsüyle her elemana ulaşabiliyorduk ama elimizde bi liste yoksa

#1den 100e kadar sayıları ekranda yazdırırsak peki

x = 0  #sayma sıfırdan başlar bunu 1 ya da 2 den de başlayabilir
#0dan başlayıp 100e kadar gitsin, her döngü durumundayken
# ekrana sayı yazdırıp birer artıralım
# ve 100e geldiği zaman döngü otomatik olarak dursun
# yani koşul hep true vercek, ne zmanki false düştük orda bitecek (100gibi)
"""1
while True:
    print(x)  #while ile sonsuz bi döngü üretir, 
              #yani sürekli 0 yazıyor, bunu belli biyerde kesmek gerekli
              # x < 100: deriz bu işlem 100 kadar devam eder 
"""

"""2
while x < 100:  #true üretmeye devam eder ve x<=100 yaparsak 100 de girer sıraya
    print(x)    #yine sonsuz döngü olur çünkü x değeri değişmeli
                #bu durumda x = x + 1 ya da x += 1 dersek değişir
    x += 1   # 99a kadar sayar. ikili gitsin diyorsan x= x + 2
print('Count is over!')
"""
#bütün ifadeleri yazmak zorunda değiliz
#koşul kullanırız yazmamakiçin
"""3
while x < 100:
    if x % 2 == 0: #x sadece çift sayılar ise yazdır   
        print(x)             
    x += 1         #sadece tekler yazılıcaksa if x % 2 == 1
print('Count is over!')
"""
"""4
while x < 100:
    if x % 2 == 1: #x sadece tek sayılar ise yazdır       
        print(f'number odd: {x}')
    else: #diğer hepsi de çift
        print(f'number even: {x}')             
    x += 1         #hem çiftleri hem de tekleri yazdırırsaki yani hepsini
print('Count is over!')
"""

"""5
#userdan bi değer iste, user bilene kadar sormaya devam et
name = '' #string değer alsın
while not name: #yukardaki '' boşluk değeri false olarak değerlendirir
#while yanındaki ifadenin sürekli true olarak üretilmesi demek, falseun tersini almak demek
#yani 'not name' aslında true'ya karşılık geliyor. bu da true değerindeki kodları sürekli işlet demek
#name, boşluk karakterine eşit old sürece while döngüsü işlesin
#yani userdan name için bi input almak lazım
    name = input('enter ur name: ')
    #ne zaman isim doğru girilirse print ile hallo blabla diyelim
print(f'Hallo {name}')

#inputa bi değer girmediğiniz sürece 'enter ur name' ekrana çıkar
#çünkü name bilgisinin boşluk karakterine eşit olması false'a eşit

#bi değer girmek yerie boşluk(spacebar) karakterine basarsa boş gözükür
#'' bu boş bi str ifade
#' ' içinde boş bir karakter var
#bunu engellemek için ise while not name.strip(): yazarız.
#böylece spacebar kabul etmez
"""

while False:
    print('Looping..') # 0 değerde sonuç çıkmaz

