import os
import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/yeniklasör")

# listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)


# etkin dizin öğrenme
# result = os.getcwd()


# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)  # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime)  # son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)  # değiştirilme tarihi

# os.system("notepad.exe")

# path

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/python/advanced-modules/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/python/advanced-modules/_os1.py")
result = os.path.exists("C:/python/advanced-modules")
result = os.path.isdir("C:/python/advanced-modules")
result = os.path.isfile("C:/python/advanced-modules/_os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)


##############################################


"""
import os
result = dir(os)
print(result) #bir sürü class ve metod çıkar

#os modulü genelde işletim sistemiyle ilgili bi bilgi talebinde bulunabiliriz
#klasör bilgileri ya da bi oluşturma yapılabilabilir
"""

""" #Dizin/klasör değiştirme ve Klasör oluşturma işlemi
import os
result = os.name #işletim sistemini gösterir
os.chdir('C:\\')  #..şu andaki konumunu c dizini altına getirip mkdir metodunu yorum yaparsak result bize c dizini içinde olduğumuzu söyler. mevcut os dosyasıdizini değil, c dizini altında oluruz
#yoruma çevirdiğimiz mkdir metodunu bu işlemden sonra açarsak klasör c dizini altında oluşacak
result = os.getcwd() #os dosyasının adresini hangi klasörde old gösterir #etkin dizin öğrenme
#os.mkdir("NewDirectory")  #os için mkdir metoduyla bi klasör aynı dizin içinde oluşturur
                          #bunun öncesinde change directory metodunu çalıştırırsak
print(result)  
#c dizini yerine os.chdir('..') dersek bi üst dizine geçeriz mkdir metodundan sonra ya da önce c yazmak yerine de kullanılabilir
#bunu alt alta iki kere yaparsak c dizinine varırız ya da (../..) yazarsak da olur

#klasör isminideğiştirmek istersek 
os.rename('NewDirectory', 'YeniKlasor')
#klasör silme istersek
os.rmdir('NewDirectory')
os.removedirs('NewDirectory/NewDirectory') #alt dizindeki de silinir
"""

"""
import os 
os.makedirs('C:\\NewDirectory/NewFolder')   #bu metodla iç içe klasörler oluşturulabilir- c dizinini de başına ekleyebiliriz
"""

"""
#Listeleme işlemleri
import os
result = os.listdir()
#result = os.listdir('C:\\') #herhangibir konumda bir listeleme işi yapmak istersek mesela cnin altındaki bütün klasörler
print(result) #etkin olan dizinin içindeki klasörleri gösterir

#bir listeleme islemi yaparken filtreleme işlemini for döngüsüyle oluştururuz
for dosya in os.listdir(): #listdir ile gelen dosyaların sonundaki bi bilginin py ile bitip bitmediğine bakabiliriz
    if dosya.endswith('.py')
        print(dosya) #bu durumda sadece py ile biteler çıkar
"""        

"""
import os
result = os.stat('15-02.Module-OS.py') #bu stat metodu belirtilen dosya bilgisini verir
result = result.st_size/1024   #dosya boyutuna byte cinsinden bu sekilde de ulaşırız 1024e bölersek de kb cinsinden çıkar
print(result) #bunu yazdırırsak karşımıza pek anlamadığımız rakamlar geliyor yani dosyanın byte cinsinden büyüklüğü, değiştirilme tarihi, oluştuulma tarihi ya da dosyaya son erişilme zamanı gibi
"""

"""
#datetime modülü üzerindedn datetime classını kullanarak dosyanın oluşturulma zamanına bakarsak
import os
import datetime
result = os.stat('15-02.Module-OS.py')
result = datetime.datetime.fromtimestamp(result.st_ctime)  
#ctime - oluşturma, atime - access son erişim tarihi, mtime - modify değiştirilme tarihi
print(result)
"""

"""
import os
os.system('notepad.exe')  #istediğimiz programı bu şekilde çalıştırabilir
"""


#os modülünün bir parçası olan path modülüne de bakarsak
#path daha çok uzantıları ya da isimleri üzerinde işlem yapar - örn resim 
import os
result = os.path.abspath('15-02.Module-OS.py') #dosya ismi
#abspath metodu ile dosyanın tam konumunu bize verir
result = os.path.dirname('C:/../..') #dizin ismi öğrenme
#elimizde olan dosya yoluyla yani konumla dosyanın dizin ismine ulaşırız
result = os.path.dirname(os.path.abspath('15-02.Module-OS.py'))
#dosyanın tam yolunu bulur, tam yolu içerisinden de dizin ismini alır

#exist metodu
result = os.path.exists('15-02.Module-OS.py') #ilgili konumda dosya var mı yok mu onu gösterir true false ek olarak klasör de sorgulayabiliriz

#ulaştığın bir alan dosya mı klasör mü
result = os.isdir('15-02.Module-OS') #dosya ise false der klasör ise true diyecek
result = os.isfile('15-02.Module-OS.py') #dosya ise true der klasör ise false diyecek

#konuma gönderirken path oluşturmak
#join metoduyla verilen parçalar birleştirilir
result = os.path.join('C:\\', 'trial') #c dizini ile trial dizinini değiştir. devam edersek ..,'trial1' bu şekilde de bir dizin oluşturuulur

# metoduyla verilen bilgileri bölmek istersek
result = os.path.split('C:\\Trial') #böyle çalıştırırsak karşımıza bi liste gelir
#dosyanın ismi ile uzantısını ayırır
result = os.path.splitext('15-02.Module-OS.py') #çalıştırısak ismi farklı yerde dosya farklı yerde
#resultun sıfırıncı elemanını resuta atarsak
result = result[0]  #sadece ismi gelir
result = result[1] #sadece dosya uzantısı gelir



###########################################
#code to shutdown a machine in py
import os
os.system("shutdown /s /t 1")






