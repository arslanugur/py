# func kapsamı global ve local değişkenler

"""
x = 'global x' # global scope

def function(): # local scope
    x = 'local x' # x değişkenine local x şeklinde değer ata
# yani funk için bi çalışma alını hazırlıyoruz
# local değişken global değişkeni etkilemiyor
    print(x) #içeride değişkeni yazdırır

# dışarıya gelip tanımladığımız fonk çağırıp x değişkeni ekrana yazdır
function()
print(x) # karşımıza global x değişkeni gelir ama neden global olrak geldi
# burda yaptığımız normal bi değişken tanımlayıp 
# bu değişkeni bi de func kapsamında tanımlıyoruz
# global olarak gelmesinin sebebi
"""

# func içinde bi tanımlama yapılmadıysa
"""
x = 'global x'

def function():
    print(x)

function()
print(x) #ekrana iki kere x çünkü func kapsamında bi tanımlma yok
# func için global olan kapsamı kullanıyor
"""

"""
name = 'Arslan'

def changeName(newName): # dışarıdan bi name bilgisi alsın
    name = newName #globale func local değeri atasın
    print(name)

changeName('Uğur') #name globalinin yerine gelecek değeri girelim
print(name)
# ikisini de alt alta yazar
"""

# iç içe func tanımlarsak bu işlemler  nasıl olur
"""
name = 'global str'

def greeting():
    name = 'Arslan' # local olarak tanımlanan name değişkeninne bilgiyi atasın
    #bunu da uğur gibi yorum yaparsak çıktı global str olur
    def hello(): # bi tane daha func tanımlayıp
        #name = 'Uğur' # ama bunu yazdırırsak arslan değeri iptal olur uğur değeri yazdırır
        print('Hello' + name) #burda kullanılan name arslanı ifade ediyor, global str deil
#ilk etapta hello func uğuru arar bulamazsa arslanı arar onu da bulamazsa globale geçer
    
    hello() # hello func, gretting kapsamında içinde tanımlanır
    #bu kapsamda da çağırılacak
greeting()
"""

"""
x = 50 
def test(x): # dışarıdan x bilgisini alsın
    print(f'x : {x}')
#f str oluşturmanın sebebi bilgileri int çevirmek zorunda kalmamak için
    x = 100 #yani dışardan alınan x bilgisi func içinde güncellenir
    print(f'changed x to {x}') # x değişkeni burda değiştirildi denilen bilgi

test(x) #test func, x parametresinin göndererek çağıralım
# global çıkar, altındada changed to 100 olur
# print(x) # diye alta yazdırırsak da direk 50 bilgisini verir bize
#----
#peki dışarda tanımlanan bi değişkeni func içinden değiştirceksek
#def test(x) deki ve alttaki test(x)deki x silinir ve altına global x olarak tanımlanır
#def test():
#    global x
# yani bunun için "global" keyword kullanmamız gerekiyor
#func içinde yapılan bütün işlemler dışardaki x bilgisi üzerinden yapılır
#bunun sonucu olarak da print(x) yazdırırsak 50 değil 100 bilgisi çıkar
"""

# önceki örneği global olarak tanımlarsak
name = 'Arslan'
def changeName(newName): # dışarıdan bi name bilgisi alsın
    global name
    name = newName #globale func local değeri atasın
    print(name)
changeName('Uğur') #name globalinin yerine gelecek değeri girelim
print(name)

#ilk denemede ugur altında arslan yazdı
#şimdi global ile ugur altında ugur yazıyor
