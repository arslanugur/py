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
#py'de fonksiyonlarımızı başka bir fonksiyon içinde de tanımlayabiliriz.. 11:47
...






