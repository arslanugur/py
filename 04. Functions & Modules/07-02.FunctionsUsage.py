#fonksiyon oluşturmak için kullanılan anahtar sözcük def (define)
#def sonrası function ismi veriyoruz pop,append vs gibi
"""
def sayHello():
#yazacağımız kodlar sayhellonun bir üyesi olacağı için iki nokta ekliyoruz
    print('Hello')
#oluşturduğumuz function çağırmak için
sayHello() #Böylelikle print yapıyoruz
#sayHello() alt alta yazdıkça hello da artmaya başlar
#yani 3 kere print yazmak yerine 3 kere function çağırmak
"""
"""
#dışardan bi name parametresi alsın,değişken ismi tanımlayalım
def sayHello(name = 'user'):
    print('Hallo' + name) #functiona çağıran name olarak ne gönderirse o yazılır
sayHello('Arslan') #bi parametre bekledi Arslan name parametresi
sayHello('Ugur') #gönderdiimizde user işe yaramaz
sayHello() #parametre belirtilmemişse name yanina user yaabiliriz
"""
"""
#ekrana print yazmak yerine biz dışardan bibilgi gönderelim
#bizim için bi str bilgi oluştursun ve bana geri göndersin
def sayHello(name = 'user'):
    return 'Hallo' + name 
msg = sayHello('Arslan')
msg = sayHello('Uğur') #msgye atanan son bilgi old için uğur ekrana yazılı
print(msg)
#Arslan bilgisi functiona gönderildi ve user yerine geçti ve bize geri hello arslan olarak geldi
"""

"""
#yeni bi function daha
def total(num1, num2):
    return num1 + num2
    #gönderdiğimiz iki sayıyı toplayan bi function
#return ettiğimiz için bi değişken lazım u da result olsun
result = total(10, 20)
result = total(340, 520) #defalarca başka sayılar içinde kullanabilirsin
print(result)
"""

"""
def calculateAge(birthYear):
    return 2019 - birthYear 
    #hesaplayıp bunu return olarka gönderek
#farklı kişiler için yaş hesaplaması yapılır age ile
ageJoseph = calculateAge(2015)
ageJess = calculateAge(2013)
ageJosh = calculateAge(2012)
ageJohn = calculateAge(2000)
print(ageJess, ageJoseph, ageJohn, ageJosh)

#bu metodu başka bi metod içinde kullanırsak
def HowManyYearsLeftToRetire(birthYear, name): #doğum yılı ve isim bilgisi alalım
    #gönderdiğimiz bilgilere göre ilk olarak yaş hesapla
    ''' #def sonrası tab yap ve helpe yorum yazma
    DOCSTRING: How many years left to Retire as your BYear.  #function kullanan için açıklayıcı mesaj, amaç ne
    INPUT: Birth Year #beklenen input
    OUTPUT: Calculated Year Info #bunları help ile de yapabiliriz
    '''
    age = calculateAge(birthYear)
    retirement = 65 - age
    
    if retirement > 0:
        print(f'{retirement} years left to retire')
    else: #diğer durumda ise
        print('You are already retired')

HowManyYearsLeftToRetire(1988, 'Arslan')
HowManyYearsLeftToRetire(1934, 'Uğur')
#fonksiyonun nasıl kullanıldığı önemli içne ne yazdığın değil
#içerisindeki kodlamanın ne old bilmeye gerek yok
#yazarken nasıl kullanılacağını bilmek önemli

print(help(HowManyYearsLeftToRetire))
"""
list = [1,2,3]
print(help(list.append)) #methodun nasıl kullanıldığını açıklar
