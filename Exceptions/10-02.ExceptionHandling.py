#Hata yönetimi
"""
x = int(input('x : '))
y = int(input('y : '))

print(x/y) #eğer y sayısını 0 girerse error
#bu yüzden önlem alınması gerek
"""

#hata gelebilecek olan kod bloklarını try içine almak
try:
    x = int(input('x : '))
    y = int(input('y : '))
    print(x/y) #print ifadesi buraya gelir
except ZeroDivisionError: #öngörülen hata türü önlem için yazılır    
    print('y cannot be 0') #şimdi user'a bi mesaj verelim
#böylece hatayı bize göstermez ve user hatayı kendisinde bulur
#ifadelerden birine yanlışlıkla string ifade yazmak
except ValueError:  #ikinici yakaladığımız hata
    print('you need to write an integer')
#except (ZeroDivisionError, ValueError): #bu şekilde de kısaltabiliriz
#   print('you wrote either 0 or string') #ya da daha genel yanlış bi bilgi girdiniz hataları gruplandırdı yani
#ya da 
except (ZeroDivisionError, ValueError) as e: #yazarak obje şeklinde ele alırız
    print('you wrote a wrong info')
    print(e) #dersek yapılan hatanın türünü gösterir

######
#tek tek hata mesajlarının tipini yazmak yerine
except: #ancak objeye ulaşıp hatanın türünü burd şekilde tespit edemiyoruz
    print('you wrote a wrong info')
#yani try kısmından gelecek olan herhangi bir hatayı except kısmına getirebiliriz
# bu yüzden bu yöntem çok genel ve hatayı bulmak zorlaşıyor    

#ancak hatayı görmek için genel bi hata olan exceptionı yazabilir
# except Exception:
#sonuçta error types, exception 'dan türemiştir
#yani axception bi baseclass diğerleri bunun altı 
except Exception as ex:  #bu class ile alabileceğiiz hataları genelleyip hata mesajlarını loglayabiliriz
    print('you wrote a wrong info', ex)
#exception detayı da böylelikle ekrana yazılır yani hata kodu


##############
while True: #else durumunda break varsa while bloğundan çıkar
    try:
        x = int(input('x : '))
        y = int(input('y : '))
        print(x/y)
    except:
        print('you wrote a wrong info')
    else:   #except kısmında hata yoksa else ile herşey yolunda
        print('alright')
        #break #break i gördüğü zaman userdan bilgi istemez
#while durumunda ne olur kullanıcıdan sürekli x ve y yi isteriz
# yani eğer bi hata varsa tekrar döngüye girer x ve y bilgisini tekrar yazmayı denersin çünkü break ile karşılaşmadı

#finally bloğu, try except bloğundan çıktığımız zaman finally çalışır
#finally, try ve except sonrası her zman çalışır ama except bloğu çalışmazsa else bloğu çalışır

    finally:
        print('try except sonlandı.')
#her şey ylunda olsun olmasın çalışır
#bunun çalışmasının sebebi kaynakların kapatılması aşaması için
#örneğin bi dosya açtık okuma işlemi bittikten sonra kapamak gerekiyor
#tanımlanmış olan değişkenlerin içeriklerin sonlandırılması bitirilmesi aşamasını gösteriyor

#bu aşamaya kadar builtin hata tiplerini ya da geneli olan exception gördük

#bi func örn bi class yazdığımızda class içinde yazdığımız metodlar içerisinde 
# bize gelen parametreler ile ilgili bi hata olduğunda 
# bi exceptionı kendimiz fırlatıyor olmamız gerekli 
# yani bi exception objesinin o anda oluşturulduğunu göstermememiz gerekiyor
#user hata yapmasının önüne geçip gelen bilgileri str ya da int old yani istediğimiz format old 
# emin olmak gerkiyor

