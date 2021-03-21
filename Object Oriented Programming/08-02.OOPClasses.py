#SINIFLAR
#bi class oluşturcaz
"""
class Person: #büyük harfle başla
    pass #pass keywordu yer tutucu olarak kullanılabilir, pass yazmadan geçer 
    #normalde att ya da met kullanmak gerekli
    #class kapsamı içinde tanımlayabileceğimiz ifadeler
    # attributes        # methods

#bi object tanımlayalım
p1 = Person() #küçük harfle başla
    #person classını p1 objesini tanımlamak için kullanıcaz #değişken tanımlamaya benziyor 
p2 = Person() #ikinci bi pbje daha, tipi yine person
print(p1) #p1e bellek üze bi adres verir #objectin de bi person tipi old söyler
print(p2) #p1in aksine farklı bi adreste tanımlanır
print(type(p1)) #tiplerini yazdırırsak class ve person classı olur bu class str ya da int gibi 
print(p1 == p2) #dersek bunlar farklı old gösteirir False
"""

# ATTRIBUTES
# Class Attributes
class Person:
    #pass artık ihtiyaç yoksilelim
    address = 'no info' 
# const içinden o objedeki bilgiyle ilgili bi adres bilgisi eklemek yerine 
# yani addressi direk class att olarak tanımlayabiliriz çünkü her zman kullanmıyacağız
#ki gereken bilgileri yani olmazsa olmazları obj att yapmak daha iyi

# Object Attributes
    #constructor method ile obj attr yapıcaz (yapıcı metod)
    #method tanımlaması yaparsak
    def __init__(self, name, year): #const örnek init methodu
#init methdunun parametreleri olacak
#ilki self isminde bi parametre
#classdan türettiğimiz p1 ya da p2 objesi burda self 
#yani obj üzerine bi şey yapılacaksa burda self kullanılacak
#diğer özelliklerde self sonrası gelir ,name , age gibi
#userın gönderdii name ve year bilgileri aktarılacak
        self.name = name
        self.year = year
#önemli olan p1 objesinden self.name veye .year alanına ulaşılabiliyor olmak
#init oluşturulan her bir obje için mutlak çalıştırıyor almasından yapıcı metod
#cons gönderdiğimiz bilgiler böylece obje içinde yer alacak

        print('init metodu çalıştı')
#self için parametre göndermeye gerek yok kendiliinden p1 ve 2 objelerini temsil ediyor
p1 = Person(name ='Jack', year = 1990) #('init metodu çalıştı')
#parametreleri gönderirken isimlerini de belirtebiliriz okunabilirlik için  name= ...
p2 = Person(name = 'John', year = 2000) #('init metodu çalıştı')
#update etmek istediğimizde peki
p1.name = 'George'
p2.address = 'London'

#p objelerinin değerlerini ekrana yazdırırsak
#aşağıda yapılan işlemin adı 
#accessing object attributes
print(f'p1 name: {p1.name}, year: {p1.year}, address: {p1.address}')
print(f'p2 name: {p2.name}, year: {p2.year}, address: {p2.address}')



print(p1)
print(p2)
