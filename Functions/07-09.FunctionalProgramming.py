#py 3 farklı prog paradigmasını destekler: Prosedürel Prog Paradigması, Nesne Yönelimli Prog Paradigması, Fonksiyonel Prog Pradigması
#f = g(x)  -> Matematikteki Fonksiyon
#filter, map, reduce -> fonksiyonel prog için fonksiyonlar
#functool, itertool -> fonksiyonel prog için modüller
#comprehensions ve ya liste işlemleri, decorators, generators
#anonim fonksiyonlar: recursive özelliği, lambda fonksiyonlar

'''Ek bilgi
myList = [x for x in range(100)]  #comprehension -> liste oluşturmaya kullandığımız ifadeler
print(myList)                     #range başlangıcı verilmedii için sıfırdan başlar
'''

#py içinde fonksiyonlar birinci sınıf değerlerdir, yani bir fonksiyona argüman olarak fonksiyon verilebilir veya bir fonksiyonun döndüğü değer başka bir fonksiyon olabilir.
#yani bir fonksiyonu değer olarak kullanabiliyoruz başka bir deyişle fonksiyonu veri değerine kullanabiliyoruz

def Calculate(func, x, y):         #func adında fonksiyona bir fonksiyon parametresi ve x ile y adında iki tane değer verildi
    return func(x, y)              #bu fonksiyon, x ve y parametreleriyle return edip func'a dönecek. #func fonksiyonuna x ve y parametresini verdik
  
#Calculate'e func parametresinin argümanını verebilmek için başka fonksiyonlar tanımlamamız gerekiyor
def Add(x, y):                
    return x + y
#add fonksiyonunun iki argümanı var, çünkü yukarıda func(x, y) olarak iki argüman olarak verdik, yani func yerine koyacağımız fonksiyonlar iki argümanlı olması gerekiyor
#iki argümanlı olmalı yoksa parametre sayısı farklı olursa Calculate fonksiyonunda func'ın yerine koyarsak hata alırız

#bir tane daha fonksiyon yazılır
def Subtract(x, y):                #kısaca sub yazılır normalde
    return x - y

#şimdi bunları çağırmamız gerekiyor
Calculate(Add, 200, 100)           
#Add bir fonksiyonun adı ilk olarak yazılır, 200 ile 100'ü toplasın. Yukarıda Calculate fonksiyonunda bize return edecek
#sonucu görmek ve bastırmak için de print edebiliriz
#ikinci fonksiyonu yani Subtract nasıl çağırılacak, onu da print ederek çağıralım
print(Calculate(Subtract, 150, 50))         
#eğer otomatik listeden yazdırdığımız zaman parantez koyar,parantezi koymayacağız Subtract'in arkasındaki parantezi sileriz
#çünkü yukarıdaki Calculate fonksiyonumuza Subtract'in referensını göndermemiz lazım
#tek başına yazarsak referensı göndermiş oluruz   --> bu şekil değil yani print(Calculate(Subtract())), -----> bu şekil print(Calculate(Subtract)) 
#şimdi çalıştıralım. Peki nasıl çalıştı?

#ilk olarak Calculate(Add, 200, 100)'i çalıştırdığımızda add'in referensını gönderiyoruz. 
#Yani yukarıdaki Calculate fonksiyonunda Add fonksiyonunun referansı var
#sonrasında Calculate fonksiyonundaki func'ı return ediyor. bu şu anlama geliyor: Sanki Add fonksiyonunu alıp func(x, y) yerine koymuşuz gibi. Add fonksiyonu ile topluyor gönderiyor

################### SECOND EXAMPLE #########################

#yazılan fonksiyonda verilen değerin 1 arttırılmasını istiyorum
def Increment(x):        
    x = x + 1            #eğer bu x'i böyle yaparsak
    return x             #ve return edersek mantık olarak hatası yok

print(Increment(15))     #15'i 16 yapar sana geri gönderir 16'yı basar

#ancak bir fonksiyonu bu şekil yazarsak fonksiyonel programlamaya uygun şekilde olmaz
#çünkü x değerinin, değerini değiştirmiş oluyoruz ---> x = x + 1 yaparak
#buna fonksiyonel programlamada "side effect" denir. Side effect'in olmaması gerekir.
#bu değişkei başka yerlerde kullanmış olabiliriz. ve çağırdıktan sonra değeri değişmiş olacak.

#peki nasıl fonksiyonel programlamaya uygun hale getiririz?
#içerde bir değişkenin değerini değiştirmek istiyorsak başka bir değişken oluştururuz, yani x yerine y yazarız ve onu return ederiz
def Increment(x):
    y = x + 1
    return y             #böylece side effect kaldırılmış olur, ama y'nin de başka yerde kullanılmadığına emin ol
  
print(Increment(15))

#diğer yol ise değişken tanımlamamıza gerek olmadan return ettirmek -> side effect böylelikle de yok olur
def Increment(x):
    return x + 1         #tabi bunu yapmak mümkünse bazen mümkün olamıyor

#Özetle, Fonksiyonel Programlama yaparken bir değişkenin değeri değiştirilmemeli. Yani bir fonksiyon kendine ait verileri başka kimseyle paylaşmamalı

################### THIRD EXAMPLE #########################


