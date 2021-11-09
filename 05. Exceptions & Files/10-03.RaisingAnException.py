#Hata nesnesi oluşturma 

#oluşturulmuş olan exception nesnelerini belli bi olay sonucunda oluşturulduğunu gördük
#örneğin 0a bölme hatasında biz müdahle etmeden bi exception fırlatılıyor.
#ya da herhangi bir komutu yanlış yazdığımızda bize bi exception fırlatılıyor zaten
#yani belli spesifik olaylarda biz zaten fırlatılan bi hatanın bir exception objesinin yakalanma durumunu ele aldık
# bu dosyada ise biz bu durumu kendimiz yaratacağız

#örneğin bi koşul belirtelim 
#x değişkeni 5den büyük oldugunda 
#ya da bi doğum tarihi belli bi yıldan aşağıda olduğu durumlarda bi exceptionn fırlatabiliriz
# yani verdiğiniz bi doğum tarihi bilgisi bi doğum tarihi verisine uymadığından dolayı bi exception fırlattım bu exception da siz ele alın ve usera güzel bi mesaj gösterin gibisinden

"""
x = 10
if x > 5: 
    raise Exception('x cannot be than 5') #x 5den büyükse bu durumda bi hata fırlatalım ve temel sınıftan türetilsin ve parantez içinde hata kodunu yazalım
#en basitinden hata mesajını böyle fırlatabiliriz
"""

"""
#daha gerçekçi örnek için fonk tanımla
def checkPass(psw): #bi validatin işlemi yapalım
    import re
    if len(psw) < 8:
        raise Exception('Password must be least seven character') #bu durumda bi exception fırlat
#devam edersek bunu regular expression adında bi modülü import edebiliriz
#bu modül aracışıyla kontrol işlemlerini yapcaz
#küçükharf,büyükharf,rakamlar,işaretler vs
    elif not re.search('[a-z]', psw):
    #bu modül ile search metodumuz var 
    #bununla birlikte bi aralık belirtiyoruz adanzye aralık
    #ikinci parametre olarak parolayı göndercez
    #eğer true değer gönderiyorsa raise ile exception fırlatcaz
        raise Exception('Password needs small letters')
    #yani NOT dediğimiz içi eğer bulamazsa exception fırlatcak
    #eğer küçük harf bulursa da soruyu tersten sorduğumuz için exception fırlatılmıcak
    #çoğaltalım
    elif not re.search('[A-Z]', psw):
        raise Exception('Password needs big letters')
    elif not re.search('[0-9]', psw):
        raise Exception('Password needs numbers')
    elif not re.search('[_@$]', psw):
        raise Exception('Password needs alphanumerics')
    #son olarak da elif ile re.search ile boşluk karakterini kontrol edelim, (\s) ile re'de belirtebiliyoruz ve parola bilgisini gönderelim
    elif re.search('\s', psw):
        raise Exception('Passwword does not need a space') #eğer boşluk karakteri varsa içermemelidir
    else:
        print('Geçerli Parola') #böylece bize sonuçu boş göstemez
        #aynı işlem try bloğunda

#şimdi bi parola tanımlayalım
password = '12345aA@' #parola en az 7 karakter olmalı indexden saymayı unutma, küçük olmalı, büyük olmalı numerik olmalı
#deneye deneye uyarılara uya uya geçerli bi parolamız oldu
#else ile devam edersek yukarıda

#ve baştan itibaren bunu kontrol edelim 
#yani try bloğu içine bunları almamız lazım
try:
    checkPass(password) #checkpassa hazırladığmmız şifreyi göndericez
#eğer bi hata varsa da bunu except ile kontrol etcez. excep ile exceptionını alcaz
except Exception as ex:
    print(ex) #printle exi yazdıralım
#except ile düşmezse else ile düşecek
else:
    print('Geçerli Parola: else') #bunu nerden veriyoruz bunu else kısmından veriyoruz

#iki tane geçerli parola ifadesi
#bi tanesi metoddan fonksiyondan geldi
#diğeri ise else kısmından geldi, çünkü excep kısmı bi exception almadı

#son olarak finally bloğunu da hazırlarsak
finally:
    print('Validation is completed')
    #her seferinde parola geçerli ya da geçersiz olsun hiç farketmez
    #geçersiz bi parola olursa hata mesajı verir yi ne valid i tamamlar
    #ancak geçerli olan parolayı henz almadık

"""

#bi tane class örneği yaparsak
class Person:
    def __init__(self, name, year):  #person class a bi tane init metodu tanımlayalım
    #bi name bi de year parametresi alıp if kontrol edelim
        if len(name) > 10: #name bilgisi 10 karakterden büyükse ya da daha fazla diyyebiliriz işte
            raise Exception('Name alanı fazla karakter içeriyor') #bi hata mesajı yollayabiliriz 
        #geçerli bi bilgi geliyorsa else ile devam edelim
        else:
            self.name = name #ile dışardan gelen name bilgisini save ederiz
            #self.year = year #aynı şekilde year ile de 
#name year gibi her bir parametre için exception yaratabiliriz
#oluşturduğumuz Person classı içindeki herhangi bi alana istediğimiz bi verinin gittiğinden bu şekilde emin olabiliriz

#bi tane p objesi tanımlayalım Personda ve hata almamak için 10  karakterden küçük bi name bilgisi atayalım
p = Person('JackJones', 1989)



