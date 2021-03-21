################# FIRST IMPORT WAY
"""
#import math  #veya
import math as m #burda farklı bi isim ile atıyoruz yani kütüphanenin takma ismi

value = dir(math)
#math içinde ne var hepsini dir komutu ile value değişkenine atayalım
print(value) #math modülündeki bütün fonk karşmıza çıkar
#func sadece isimleri yetmez bilgi sahibi olalım dersek
value = help(math) #yardım doc karşımızda cntrl c ile çabuk çıkış yapılabilir
print(value)
"""

"""
value = help(math.factorial) #tek bi func ve hangi parametreleri aldığını açıklar
print(value)
"""

"""
# value = math.sqrt(49) #karekökü 7
# value = math.factorial(5) #5in faktöriyeli 120
value = m.floor(5.9) #aşağıya doğru bi yuvarlama
value = m.ceil(5.9) #yukarı doğru bi yuvarlama 
print(value)
"""

############# SECOND IMPORT WAY
#ilgili modülden nasıl tek tek import ederiz ya da hepsini nasıl
# from math import *  #hepsini
from math import factorial, sqrt #tek tek istediğimizi


#bu şekilde bütün fonksiyonları import ettiğimizden dolayı
value = factorial(5) #diyebilirz
value = sqrt(9)
#value = ceil(9.6) #çalışmaz import tanımlanmadı çünkü
print(value)

#eğer bu kütüphane func gibi bi func biz tanımlarsak py nasıl karşılar bunu
def sqrt(x): #x değeri alsın
    print('x : ' + str(x))
#bunu importun altına alırsak sqrt(9) bizim tanımladığımız şekilde çalışır
#importun üztüne alırsak ta sqrt(9) tanımlandığı gibi çalışır


#burda önemli olan kütüphaneyi nasıl kullandığımızdır


