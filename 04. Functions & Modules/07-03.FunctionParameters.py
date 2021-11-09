"""
def changeName(n): #gönderdiğimiz parametre n 
    n = 'Jason' #gönderdiğimiz parametreyi jason olarak değiştirelim n değişkeninde jason bilsigi adres
    #değişken tanımlıcaz name
name = 'Jack' #bunun içinde bellekte ayrı bi adres tanımladık
changeName(name)
#fonksiyonu çağırıp bi name değeri gönderirsek 
# bu n değişkenine kopyalanır, 
# ancak n bellekte farklı tanımlanan bi alan
# dolasıyla o alanın içindeki değeri n ile günceller
print(name) #dersek fonksiyon tarafından değiştirilemeyecek jack yine jack
#bunları value ve reference tiplerde gömüştük
"""

"""
#yukarıdaki işlemin aynısını liste üzerinde
def change(n): #cities buraya gelip, o indexdeki elemanı amster yapcak 
    n[0] = 'Amsterdam' #bu bi liste olacak ve bunun 0.indexini amster olrak değiştircez
#cities adında bi dizi
cities = ['Berlin', 'Los Angeles']

change(cities) #fonksiyonu çağırıp cities bilgisi göndericez

print(cities) #yukarıdaki str örneğin aksıne değişir
#ilk örnek yani value typelardan farklı olrak, liste örneğinde bi referans koplayaması yapıyoruz
#nye cities dizisinin adresi gönderiliyor. adresteki ilk index bilgisi de böylelikle değişiyor
#value typedaki gibi değişkenin farklı bi kopyası hazırlanmıyor, sadece adresteki bilgiyi güncelliyoruz
"""
"""
#bunu fonksiyonsuz yaparsak
cities = ['Berlin', 'Los Angeles']
n = cities #bunun anlamı aynı adresi tutan iki değişken bilgisi
n[0] = 'Amsterdam'
print(cities) #aynı adresi tuttukları için yukarıdaki gibi deiştirir
#referans old dolayı değiştirir adres mevzusu
"""

'''
#cities listesinin bi kopyasını oluşrutcaksak parçalama/slicing yapmak gerel
#citiesdeki tüm elemanlar n dizisine aktarılır
cities = ['Berlin', 'Los Angeles']
n = cities[:] #slicing - cities üzerinde bilgileri al, (iki nokta bütün bilgileri al demek ya da [0:2]kadar gibi)
#burda adres kopyalaması ya reference değil, value type örneğinde old gibi bi kopyalama yapıyoruz
n[0] = 'Amsterdam'
print(cities) #bunda yapmadı #orjinal listeye dokunulmaz
print(n)  #bunda yaptı #farklı listeler meydana gelir
'''

#yeni bi fonksiyon
"""
def add(a, b): #add fonk dışarda iki parametre alsın
    #gönderdiğimiz pmleri toplayarak ki bunu a+b şeklinde de olabilir
    #yada sum isminde bi fonk var bu fonk bulit-in yani gömülü bi fonk
    #sum bi nesne class üzerinden ulaşılmaz. list fonksiyonu gibi
    #bizden bi liste bekler()
    return sum((a, b))
#print(add(10, 20)) #add fonk ile sayıları gönderip print yaparsak
"""
"""
#üç tane pm gönderirsek peki olmaz
#print(add(10, 20, 30)) #bunu düzelmek için c parametresi eklenebilir
#ama bazen üç bazen iki pm ile fonk kullanılacaksa
#c pm belirtilmemişse buna def add(a, b, c = 0) diyebiliriz.
#hem iki hem de üç pmli versiyonu da çalışır
def add(a, b, c = 0): #d=0, e = 0 uzar gider
    #burda print(params) dersek tüm gönderdiklerimiz bi tuple listesi olarak karşımza çkar. params[0] index ile ulaşabiliriz
    return sum((a, b, c)) #buraya da c pmsini eklemeyi unutma
print(add(10, 20))  #cye otomatik olrak 0 bilgisi gönderdi
print(add(10, 20, 30)) #60
#6 tane parametre de artık def add(*params) denir!!!! ---sum((params))
"""
"""
#sum fonk kullanmazsak
def add(*params):
    #print(type(params)) #tuple, bi liste göndereceksek tek yıldız
    sum = 0 #değişken tanımlayıp döngü kullanırız

    for n in params: #elemanları tek tek dolaşırız
        sum = sum + n #deyip elemanları tek tek yazdırırız
    
    return sum #sum bilgisini geri göndeririz göndermezsek none cevabını alcaz yoksa
print(add(10, 20))
print(add(10, 20, 30, 40, 50, 60, 70))
"""

"""
# yukarıda gönderdiğimiz tip belli sayı bilgisi gönderiyor sonuçta
# gönderdiğimiz parametreler isim şehir maaş bilgisi olsaydı ne olurdu
#gönderilen pmler liste olması yeterli
#bunun için dict kullanıyorduk key value yapısı
def displayUser(**args): #params değeri args da olabilir arguments
    #print(type(args)) #gönderdiğimiz pmler bi tuple değil, dict olmasını istiyoruz, **
    #dolasıyla bi dict geleceğini bildirmek için ** oluyor
    for key, value in args.items(): #bi döngü oluşturalım kigönderdiğimiz args items içerisindeki value bilgileri almak için
        print('{} is {}'.format(key, value)) #aldıktan sonra yazdır
        #formatla key value bilgilerini gönderelimç karşımıza da öyle çıksın
displayUser(name = 'Kevin', age = 30, city = 'London')
#bu sekilde bi user detayları yaz, sonra yukarıda fonk tanımla
displayUser(name = 'Kelly', age = 20, city = 'Bristol', phone = 1234)
displayUser(name = 'Kendall', age = 32, city = 'Somerset', phone = 143224, mail = 'kendall@gmail.com')
"""

    #args ile normal bi liste ve argümanları aynı fonka gönderirsek nolur peki
def myfunc(a, b, *args, **kwargs): #eğer c de eklersen 3.değerde cye karşılık gelir
    print(a) #10u temsil eder
    print(b) #20yi temssil eder
    print(args) #listeyi temsil eder
    print(kwargs) #keywords args #dict temsil eder

myfunc(10, 20, 30, 40, 50, key1 = 'value 1', key2 = 'value 2') #şimdi çağıralım
