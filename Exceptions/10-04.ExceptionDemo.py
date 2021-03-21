#Error Handling

myList = ['1', '2', '5a', '10b', 'abc', '10', '50']

"""
#1 Liste elemanları içindeki sadece sayısal değerleri bul
#liste elemanları tek tek dolaşılacak, dönmek lazım for döngüsü
#hangi elemanı sayısal tipe çeviremiyorsam 
#çevirilemeyen değerleri es geçip 
# sadece sayısal değerli olanları yazdır

for x in myList: #her bi eleman sırayla gelir
    try:
        result = int(x)  #gelen elemanları(x) intê çevirmeye çalışcaz
#bu aşamada hata alıyoz mu ona bakarız gelebilecek kısma try:
#burdan gelcek sayısal değeri hata yokmuş gibi result değişkenine atayıp print ediyoruz
        print(result)
#ancak result değişkenindeki x'i int'e çevirirken bi hata alıyorsak except devreye girer
    except ValueError: #bi Value hatası gelp gelmediğine bakarız
        continue #for döngüsü kaldığı yerden devam eder 
    #(yani 1, 2 yazdırır 5a'ya geldiğinde yazamadığı için bi sonraki elemana devam eder)
#try içinde gördüğü her hata için valueerror gördü ve continue diyerek sonrakine geçti
#value error için bi mesajda yazdırılabilir ama bu şekilde devam ettik
"""
"""
#2 User 'q' değerini girmedikçe(q'ye basmadıkça) aldığın her input'un sayısal değer old emin ol aksi halde hata mesajı yaz
#bu soruda bi döngü kullanılmalı  #WHILE DÖNGÜSÜ
#girilen değerler kontrol edilecek q değilse 
#diğer hepsinin sayısal olup olmadığı kontrol edilecek

#başta koşul belirtmeden while döngüsü sürekli dönsün, ancak bu döngü break ile kırılır
#ne zaman kırcaz, userdan alacağımız bi input ile 
while True:
    number = input('Number: ')
    if number == 'q': #eğer girilen sayı q değerine eşitse bu durumda break diyelim
        break
#ama diğer durumlarda FOR DÖNGÜSÜ her zman devam edecek
#user q'ye basarsa while döngüs durur bunun dışında user her seferde bi sayı almaya devam etcek

    try: #try bloğu içinde gelen sayı int'e çevirilebiliyor mu
        result = float(number) #sayı değerini floata çevirmeye çalışalım
    #burda bi sorun varsa except bloğuna geçiş yapar
        print('Number:', result)  #başarılı şekilde girmişse
        #break  #eğer userdan almışsak değeri, döngüyü break ile durdurabiliriz
        #yani geçerli bi sayı girdikçe de uygulama kapanır (q benzeri çıkış) 
    except ValueError: #yani bi değer hatası geldiği zamn bu işlem yapılır
        print('Undefined Number') #geçersiz sayı
        continue #while döngüsüne devam eder yani sormaya devam
#sayıyı Q tuşuna bastığımız zaman uygulama soan erer bunun dışında hep sayı ister
#kısaca geçerli bi değer girmedikçe program çalışır
"""


#3 Girilen parola içinde türkçe karakter hatası ver
#user bi password bilgisi gircek, içinde tr varsa uyarı mesajı
"""
turkishCharacters = 'ığüşöçİ'  #bunlar girilen parola içinden kontrol edilmeli

password = input('Password: ')

#karakter dizisine her bi karaktere sırayla dönüp 
#for döngüsüyle i'nin içine alabiliyoruz
for i in password: #turkishCharacters değil, password içinden giriş yapcaz
    #i'nin içine alınan her bi karakter türkçe karakterler içinde mi kontrol edilcek
    if i in turkishCharacters:  #varsa bi hata fırlat raise
        raise TypeError('Password cannot be with Turkish Characters')
    else: #ve bunu haricinde ise sorun yoksa pass
        pass #parola kabul
print('Password is OK') #geçerli parola
"""

#Bunları bi fonksiyon içinde yaparsak daha iyi
"""
def checkPass(password): #dışardan bi parola almış olalım
    turkishCharacters = 'ığüşöçİ' 

    for i in password:
        if i in turkishCharacters:  
            raise TypeError('Password cannot be with Turkish Characters')
        else:
            pass
    print('Password is OK')

password = input('Password: ') #burdan bi pass alıyoruz

try:
    checkPass(password) #aldığımız passı buraya vercez
#eğer bi hata olarsa except devreye gircek
except TypeError as err:
    print(err) #hata parametresini user ekranında yazdırırız

#eğer sorun yoksa geçerli bi parola yazısı check pass içinde kalsın 
# ama for döngüsünün altında olduğundan emin ol
"""


#4 Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları ver
#faktöriyeli hesaplancak olan bi değeri 
#faktöriyel fonksiyona gönderdiğimiz zmn 
#sayısal bi tipe çevrilemiyorsa hata verelim
#ya da negatif bi sayıysa değerse bu durumda da hata verelim 

def factorial(x): #fact isminde bi fonksiyon oluşturp dışardan x parametrisi alsın
    x = int(x) #gönderdiğimiz x bilgisi int'e çevirelim

    if x < 0: #x değeri negatifse
        raise ValueError('Negative Value') #bi hata fırlatalım

    result = 1 #başlangıç için bir değerini atayalım

    for i in range(1, x + 1): #1den başlayıp x'e kadar gitcez
    #ancak x+1 x değişkenine katmak gerekli çünkü range'de son eleman işin içine katılmaz
    #yani x'i de işin içine katarız
        result *= i #yani gelen her bi değer birbiriyle çarpılır
    return result #en sonunda result'ı geriye göndercez
# ve result da faktoriyelimiz olcak
#yapılan girilen x sayısına kadar 1den başlayarak sayıları tek tek çarpımını bulup geriye göndermek


#şimdi x diyerek bi döngü oluşturalım, döngü bi liste olsun
for x in [5, 10, 20, -3, '10a']:
    #dögü döndükçe dönen her değer için x bilgisini alıp bunu try içinde kontrol etcez
    try:
        y = factorial(x) #faktoriyel içine x bilgisini göndercez
        #-3 için valueerror döncek
        #10a için syntaxerror döncek
        #bunları except ile yakalamamız lazım
    except ValueError as err:
        #hata bilgisini yazdırmak için as err diyelim
        print(err)
        continue #iş bittikten sonra cont diyelm ki bi hata olsa bile bi sonraki eleman için devam etsin
#sonunda da döngüden çıkmayıp döngü içerisindeyke y değerini yazdırırız
    print(y) #faktoriyeli alınan sayıyı da ekrna yazdıralım

#her bi elemanın faktoriyeli alt alta yazar
#-3 negatif sayı
#10a dönüştüülemiyor gibi

#güvenlikod yazmak için try except bloklarını kullanmak da fayda var
