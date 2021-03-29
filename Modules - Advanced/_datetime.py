#İleri seviye py modülleri: Datetime

from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now()       #şimdiyi verir - print(result)
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%X')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %A')

t = '15 April 2019 hour 10:12:30'            #elimizde tarihle ilgili bi str bilgi, bu ifadelerin anlamı ne şuan makine bilmiyor
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year


t = '21 April 2019' 
day, month, year = t.split()  #bunu tanıtmak için değişkenler atayarak ayırma işlemi yaparız
print(day)
print(month)
print(year)


birthday = datetime(1983,5,9,12,30,10)
#kendimiz bi tarih bilgisi vermek istersek, bir obje tanımladık 
#ve bunu datetime üzerinden oluşturduk parametreleri gireriz gün ve saat bilgisi 
##print(birthday)

result = datetime.timestamp(birthday) # saniye
result = datetime.fromtimestamp(result) # saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(simdi)

# result = simdi + timedelta(days=10)
# result = simdi + timedelta(days=730, minutes = 10)

result = simdi - timedelta(days = 10)

print(result)

################################################

"""
import datetime

result = dir(datetime)
print(result) 
#modül içinde neler var bakmak için date classı ya da datetime classı gibi
#tarih ile ilgili - date
#zamanla ilgili - time
#tarih ve zamanla ilgili birleşik işlemler - datetime
"""

#from datetime import date   #modları import etmek için
#yada import datetime ---- result = dir(datetime.date) aynı yola çıkar
# time ve date üzerinden yapılan işlemler datetime ile de yapılır bu yüzden sadece datetime kullanmak yeterli

"""1
from datetime import datetime

result = dir(datetime)
print(result)  #datetime classı içindeki metodlar karşımız gelir
"""


"""3
now = datetime.now()    #atama yaptık
result = datetime.now() #now yerine today de olabilir

result = now.year #karşımıza sene bilgisi gelir method ile classtan yıl bilgisini alırız
result = now.day
result = now.minute
result = now.second
result = datetime.ctime(now)  #ctime fonk bizden datetime objesi bekler atadığımız now yazarsak daha açıklayıcı bi bilgi verir

result = datetime.strftime(now, '%Y %B %A')    #x dersek sadece saat bilgisini verir, d dersek gün bilgisi, a dersek gün bilgisini str olarak verir b ise srt ay bilgisi
#biçimlendirme metodu obje istiyor verelim, ikinci parametrede ise bi format değişkeni veriyoruz yıl bilgisini alıyoruz
#tüm bu kısaltmaları öğrenmek için datetime py diye arat dates w3schools
print(result)
"""



"""5 #sql işlemleri için önemli olabilir
t = '21 March 2021 hour 21:58:12'
#bu şekil bir bilgiye tek tek split ile ayırmak uzun olacak
#bu yüzden bir method kullanmak gerekli
#dt değişkeni atayalım bize bir obje üretsin
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S') #ilk parametre t ama sonrasında str ifadeyi nasıl burdan çözmleyecek alacağız
#böyle bu ifade içinden istediğimiz bilgiyi alabiliriz
dt = dt.year #yıl bilgisi gelir artık kullanacağımız bir dt objesi var önceki örneklerdeki now gibi
print(dt) #str ifade böylece çözümlenir
"""

"""

#elimizdekilerini kullanarak methoda bu bilgileri verirsek
result = datetime.timestamp(birthday)  #saniye bilgisi verir
result = datetime.fromtimestamp(result) #result saniye bilgisini tekrar datetime bilgisine çevirir saat bilgisi
#ya da 0 bilgisini verirsek
result = datetime.fromtimestamp(0) #1970 bilgisi gelir yani bilgisayarlar için milat bilgisi
#biz saniye bilgisii çevirdik ama 1970den şuanki tarihe kadar olan saniye bilgisini elde ediyoruz ya da yazdığımız tarihten şuanki tarihe kadar

#peki iki tarih arasındaki farkı nasıl bulabiliriz?
result = now - birthday   #burda aslında timedelta objesi geliyor yani farklı bi classtan türetilen objeyi getiriyor
#now yukarda atadığımız tarih objesiydi  

result = result.days #dediğimizde timedeltadaki gün bilgisini bize geri getirir
#result = result.seconds #saniye bilgisi gelir
#result = result.microseconds
print(result) #bu durumda ilgili tarih objei bize saniye cinsinden getirir

"""

#ileri bir tarihi bulmak istiyorsak eğer
from datetime import timedelta

result = now + timedelta(days=10) #days=10, minutes=123...
#now diye atadığımız tarih bilgisinin üzerine 10 gün daha eklemiş oluyoruz
print(result)
#mesela + yerine - dersek şimdiden 10 gün öncesini print ederiz

#now atamasında hata olabilir kontrol et
