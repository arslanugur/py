#sayı tahmin uygulaması
'''
1-100 arasında rasgele üretilecek bi sayıyı 
aşağı yukarı ifadeleri ile buldurmaya çalış (hak = 5)
**random modülü için py random şeklinde arama yap
**100 üzerinden puanlama sistemi ekle. her soru 20 puan
**hak bilgisini kullanıcıdan alın (yani kaç hakta bunu bilirsin)
(bilemezse her bilmediğinde 100 üzerinden 20 puanı aşağıya iner)
(10 hak derse her bilemediği için 10 puan aşağıya)
ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''
import random
number = random.randint(1,10) #rastgele sayılar üretir
#print(number)
live = int(input('How many lives you wanna use?: ')) #hak bilgisini kullanıcıdan al
right = live #right = 5 #5 kerede bu soruyu bilmesi gerekiyor, kullanıcıdan alınmayan hak 
counter = 0 #üçüncü defada bildiniz diye ekran çıksın, bu bilgiyi de tutcak olan sayaç isminde bi değişken atayalım

#hak değeri 0dan büyük old sürece ki bu 5e kadar. userdan sayı istemeye devam
while right > 0:
    right -= 1 #her hakkımızı kullandığımızda haktan bir eksitmemiz gerek
    #yani 5 hak vermiştik, user while döngüsüne girdiğide bi sayı tahmininde bulunacak, haktan bi düşecek
    counter += 1 #her döngüye girdiğimizde sayaç değişkeni içerisine 1 artıralım
    predict = int(input('guess number: ')) #userdan int tahmini alalım

    #eğer sayı userın tahmin ettiği sayıya eşitse demek ki sayıyı bildi.
    #her bilinmeyen soru için 20 puan 100 üzerinden düşecek (5 hak verdiğimiz için bunu biliyoruz)
    #bunu da sayaçla çarparak buluruz
    #ancak sayaç yukarıda while döngüsüne girdiğimiz anda artırıyoruz
    #ve user gelip tahmin ettiği sayıyı buluyor, buld anda hak için yani o anki tur için sayaç değişkeni 1 artıyor
    # artığı için 100 üzrinden 20 puan extra bildiği turda bile dönüyor
    # dolayosoyla sayacın bi eksiğini almak lazım
    #o anda turda user bu işlemi sayıyı bilicek bildiği zamanda bunun yirmi puanı kapbolmucak. çünkü o turda bilmiş oluyor
    if number == predict:
        print(f'Congratulations! You knew it on the {counter} attempt. Score: {100 - (100/live) * (counter - 1)}') #her denemede (20) puanın gider ya da (100/live) 10 defa bahsi varsa 10 puan düşecek 5 defa bahsi varsa 20 puan düşecek
        break 
    #sayı bilindiği için döngüden break ile çıkılır
#eğer sayı tahmini eşit değilse bu durumda
    elif number > predict: #sayı tahminden büyükse
        print('upp') #usera yukarı demek lazım
    else: #bunun aksi olursa da usera aşağı demek lazım
        print('doown') 

# bu işlemlerden sonra hak değişkenini her seferinde kontrol edelim
#çünkü başa döndüğünde hak değişkeni bitti diyelim o zman bir daha soru sormasın
    if right == 0: #hak 0a eşitlenmişse hakkınız bitti diyelim 
        print(f'You lost. The number was {number}')


