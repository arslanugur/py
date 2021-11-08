# Nesne tabanlı programlama - Objeler içinde kullanılan bazı Özel metotlar
"""
myList = [1, 2, 3, 4]      #eleman sayısını yazdırır
print(len(myList))  #4

myStr = 'Tarantino'        #karakter sayısını yazdırır
print(len(myStr))   #9
print(type(myList))
print(type(myStr))
"""
#yani len metdou her bi obje için farklı çalışır
#eğer kendimiz bi obje tanımlarsak bi class üzerinden
"""
class Movie():
    pass #boş bi class olsun

m = Movie() #bi tane de obje tanımlayalım movia classından
#yukarda yaptığımız aynıişlemi len metodunu m objesinden çalıştıralım
print(type(m))
print(len(m)) #bize söylediği movie objesi m için len metodunun olmadığını söylüyor
#şimdi yukarıda str ve list için type yapalım
#hatta tanımladığımız m objesiniin de typenı yazdıralım
#str ya list bir builtin classları yani önceden py kütüphanesinde tanımlanmış
# yani len ya da type metodlarını bu objeler üzerinden çağırdığımız zaman
# arkka tarafta çalışan bi methodun çalıştırılmasına neden oluyoruz
#tabi bu metodları kendi oluşturduğumuz classlara da tanımlayabiliriz
"""

class Movie():
    def __init__(self, title, director, duration):    #__ dediğimizde özel metodlar zateen karşımıza çıkar
                #dışardan alacağımız bilgiler
        self.title = title #dışarıdan gönderdiğimiz title böyle set edilir
        self.director = director
        self.duration = duration
        print('Movie object created') #böyle dersek, tabi obj tanımlamalarında bilgileri yazıyor olmamız gerekli movie name, dir name gibi

    def __str__(self):
        return f'{self.title} by {self.director}' #geri gelecek olan stringi kendimiz tanımlayabiliriz f str ile
        #bunu çalıştırdığımızda artık adres yerine obje için bi str ifade ekrana print edilir

    def __len__(self):
        return self.duration #str olarak 'movie duration' gönderirlir ya da m objesi üzerinden int bi bilgi girilir 120 gibi

    def __del__(self):
        print('movie is deleted')
    #aşağıda tekrar ulaşmaya çalıştığımız için hata mesajı çıkabilir
    #nasıl siliniyor peki bellek üzerinden siliniyor
    
m = Movie('movie name','directors name', 120 ) #arka tarafta init metodu çalışıyordu şimdi biz yazdık ve açık halde çalışcak
#böylece movie objesini oluşturdukk
print(type(m))
#print(len(m))

#şimdi print ile hem m hem de mylist objelerini ekrana yazdırırsak
lst = [1, 2, 3]
print(lst)  #direk listeyi gösterirken
print(m)    #direk movienin ram üzerinde oluşturduğu adresi gösterir
#bu ikisini str ile çevreleyip yazdırırsak yine aynı sonuç gelir
#bu iki durumda da arka tarafta çalışan metodumuz yularıda da yazacamın gibi ---- __str__ ile

#len metodunu kullanırsak peki?
print(len(m)) #onun için de bi len methodunu objeiçine eklerz yukarıya def 


#eğer bi obje silersek
#del m
#print(m) #silip printle m obj ulaşmaya çalışırsak objenin tanımlanmadığını bize söyler - undefined
#peki silindiğin kullanıcıyya söylemek içinse def __del__ ---
