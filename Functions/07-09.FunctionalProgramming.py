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

print(Increment(15))

#Özetle, Fonksiyonel Programlama yaparken bir değişkenin değeri değiştirilmemeli. Yani bir fonksiyon kendine ait verileri başka kimseyle paylaşmamalı

################### THIRD EXAMPLE #########################

dictionary = ["fox", "boss", "orange", "cup", "fury", "toes"]  #kelimeleri içeren bir değişken tanımlanır ve içeriği liste türünde

#şimdi ingilizce kelimeleri çoğul şekline sokacak olan bir fonksiyon yazalım
def Pluralize(words):                  #words adında bir parametre koyarız
    for index in range(len(words))     #range sıfırdan bize versin, len kaç tane elemanım varsa
#çünkü index kullanarak listedeki elemanlara teker teker ulaşıp değiştirecek(Çoğul yapacak), onun için indexini aldım
        word = words[index]            
#yani yukarıdaki dictionary listesini yani Pluralize fonksiyonunu, for döngüsüne koymaktansa bu satırda bu şekilde alındı elemanlar, çünkü değiştirmek istiyoruz
        if word.endswith('s') or word.endswith('x'):   #yani sonu ne ile bitiyorsa    
            word +=  'es'                              #word'ün sonuna es ekle  #English Grammar
        elif word.endswith('y'):                       #y ile bitiyorsa y'yi kaldır yerine ies koyacağız
            word = word[:-1] + "ies"                  
#Slicing: string'lerde yeni bir string alma yolu
#yani -1'den ver, sonunu vermemek, sondan bir öncesini ver. (Index hesabına göre) ve sondan bir öncesini ies ile topla
        else:                                          #hiçbiri değilse 
            word += "s"                                #word'ün sonuna s ekle, sonuçta ingilizcedeki standard kelimelerimiz
        
        words[index] = word
        #words listemiz oluyor ve word listemizin içindekiyle değiştirilir . index'deki değeri, yeni oluşturduğumuz kelimeyle değiştir

#fonksiyonumuzu çağırırsak
Pluralize(dictionary)       #Fonksiyonumuzu çağırdık ve argüman olarak dictionary listesini verdik
print(dictionary)
#buraya kadar normal işliyor, ama tek bir sorunumuz var side effect
#eğer dictionary listesini önceki haliyle kullanmak istiyorsak, artık elimizde öyle bir liste yok. Liste artık çoğul şekle girdi, eski tekil liste yok
#işte bu side effect. Fonksiyon doğru çalışıyor ama side effect'i var. Başka yerdeki değerleri değiştirdi.
#bunu değiştirmek için boş liste oluşturmak gerekli result adında
#daha temiz ve ikinci versiyonuyla gösterirsek


dictionary = ["fox", "boss", "orange", "cup", "fury", "toes"]

def Pluralize(words):
    result = list()       #boş listeyi oluşturduk
    for index in range(len(words))
        
        word = words[index]

        if word.endswith('s') or word.endswith('x'):    
            word +=  'es'
        elif word.endswith('y'):
            word = word[:-1] + "ies"                  
        else: 
            word += "s"
            
        result.append(word) #boş listeyi alırız words[index] = word yerine koyarız. 
#Artık result adında bir değişken tanımladık, liste formatında, boş şekilde.
#her defasında ürettiğimiz kelimeyi append ile bu boş listeye atıyoruz.
#buna fonksiyon dışında da erişebilmek için return etmek lazım
    return result

result = Pluralize(dictionary) #artık böyle çağırmıyoruz, çünkü side effectli bir fonksiyondu Pluralize(dictionary)
print(dictionary)        #liste, orijinal şekilde kaldı ve basıldı
print(result)            #değiştirilmiş yeni liste de bu şekilde basıldı

#Hem amaca uygun sonuç elde edildi, hem de orijinal liste değiştirilmedi

#######################################################
#py'de fonksiyonlarımızı başka bir fonksiyon içinde de tanımlayabiliriz.. 
def HelloWorld(param):
    def World(world):
        print(param, world)
        #peki bunu nasıl çağırırız yani bi fonksiyonun içindeyse fonksiyon nasıl çağrılır
        return World #ama parantezini koymacağız referansını döncez
        #ana fonksiyon kendi parametresini de alt fonksiyonun parametresini de kullanıyor
        
f = HelloWorld("Hello")
#bu bize neyi verir, Worldü vermiş oluyor aslında
#print(f) #göstermek için çalıştırdığımızda bize bu fonksiyonun localinde World diye fonksiyon tanımlı der
#print(f) yerine
f("World") #çağırdığımızda çıktısı Hello World olur peki nerden geldi aslında print(param, world) den geldi
#çağırdığımız zaman aslında f = HelloWorld("Hello") nun returnünü çağırıyoruz returnü de World oluyor yani World çağırmış oluyoruz

#yani paramı HelloWorld fonksiyonundan alıyor - "Hello", "World" ü ise World fonksiyonundan alıyor

#######################################################

#Biz fonksiyonlarımızı py'de listeleri yazabiliriz

def ActionOne(param):
    print(param)    #aşağıda gelecek olan parametre her neyse onu print eder

    
def ActionTwo(param):
    print(param)

#şimdi bu iki fonksiyonu listeye nasıl koyabilirim

myFuncList = [ActionOne, ActionTwo]  
#bir liste oluşturup parantezsiz olarak fonksiyonlar yazılır
#yani listemize referanslarını veriyoruz
#bir id bu fonksiyonu py interpretorında bize ifade ediyor.
#böylece istediğimiz zaman kullanabiliriz böyle..
myFuncList[0]("Deneme") #birinci fonksiyonu 0 ile gösteririz, parantez içinde Deneme yazarsak
#birinci fonksiyonun çalıştırmış oldu. fonksiyonun amacı zaten yazdırmaktı
#bu yöntem oldukça çok işe yarar

#######################################################

#bazen bir fonksiyonun sonucu, bir fonksiyon olarak dönmesini isteriz
def SampleFunc(callback):   #yaptığın iş başarılıysa bunu bana dön diyorum yani
    print("Bazı işler yap")
    return callback  #eğer yapılabildiyse call back yapsın çağıran fonksiyon sonucu görsün

#callbacki vermek için önce bi callbacki tanımlamak lazım
def Callback(message):
    print(message)

#şimdi çağırırsak bunu
f = SampleFunc(Callback) #Callbackin referansını veriyoruz parantezsiz olarak
f("Merhaba Dünya") #diye parametre verip çalıştıralım
#yani bu içerde yaptığımız işi print("bazı  işler yap") bize fonksiyon olarak döndü
#Biz de ona parametre ismi verip f("Merhaba Dünya")


#######################################################

#daha iyi anlaşılması için değişiklikler yaparsak
def SampleFunc(number, callback1, callback2):
    if number % 2 = 0:     #çift sayıysa callback1 çağır
        return callback1 
    return callback2 #değilse callback2 yap, bu else olarak da yazılabilir tabi
                     #ama zaten ilk returnde callback olmayacaksa ikinci returna gelecek

def Callback1(number):  #geliyorum buraya numberımı bastır ama iki tane callback var
    print("1", number)  #hangi fonksiyonda olduğunu görmek için 1 yazarız
#her biri için farklı fonksiyonlar verebiliriz
    
def Callback2(number):
    print("2", number)    #bu da 2.callbackimiz
    
number = 20 #burda da bi number tanımlayalım    
f = SampleFunc(number, Callback1, Callback2)   #burda verdiğimiz 20 değeri eğer çiftsayıysa bize burda Callback1 ile döner, böylece bir fonksiyona ne yapacağımızı karar vermemizi sağlıyoruz
f(number)   #çağırma şeklimiz de bu

#f = SampleFunc.. SampleFunc ne yapıyor?
#bizim için bir karar veriyor
#20 değerindeki bi sayı için hangi callbacki çalıştırması gerektiğine karar veriyor
#kararından sonra da ilgili fonksiyonu f(number) çalıştırmış oluyor
#number'ı başka bir sayı tanımlarsak ona göre de callback değişecek
#bu kodlama matematiksel işlemlerde ve veri analizlerinde çok faydalı
#number yerine data seti veriyoruz, data setine göre fonksiyon dönüyor ve ona göre işlem yapıyoruz

#Assignment
"""
Programın fibonacci dizisinin toplamını baştan verilen elemana kadar hesaplasın
fibonacci dizisi - 0,1,1,2,3,5,8,13,21
"""
----> çözüm 19:18

