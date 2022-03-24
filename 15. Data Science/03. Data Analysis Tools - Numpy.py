# SECTION 1: NUMPY
# Diziler, bir ya da daha fazla boyuta sahip olabilen öğeler/değerler koleksiyonudur.
# Vektör, tek boyutlu bir dizi
# Matris, iki boyutlu bir dizi
# Numpy dizileri ndarray veya N boyutlu diziler olarak adlandırılır ve aynı tür ve boyuttaki öğeleri depolar.

# Numpy dizisi oluşturmak için
# nparray() metodu kullanılır.
# Liste, Tuple veya herhangi bir dizi benzeri nesne, array() metodu ile Numpy dizisine dönüştürülür.
value = [10,20,30,40,50,60,70,80,90,100]    # Generated a list
value_series = np.array(value)              # liste numpy dizisine dönüştürülür

# Bu işlem direk olarak da yapılabilir
value_series = np.array([10,20,30,40,50,60,70,80,90,100])


# Liste veri yapısında matematiksel ve istatistiksel işlemler yapılamaz.
# Liste veri yapısı ile ortalama hesaplama örneği hatalı sonuç verir
exam1 = [100,84,76,48,36,77,90]
exam2 = [95,78,66,57,75,89,95]
mean = (exam1 + exam2) / 2        # TypeError
# Numpy dizileri listelerden farklı olarak sadece tek türde veri içerir. Farklı veriler tanımlanırsa bile aynı veri tipine çevrilir.
# Numpy dizilerivile ortalama hesaplama örneği
import numpy as np

exam1 = [100,84,76,48,36,77,90]
exam2 = [95,78,66,57,75,89,95]
exam1_np = np.array(exam1)
exam2_np = np.array(exam2)
mean = (exam1_np+exam2_np)/2
print(mean)

# nparray ile integer tipinde elemanları olan bir dizi üretilir.
#             float tipinde elemanları olan bir dizi üretmek için dtype komutu dtype=np.float biçiminde kullanılır.
# Float tipinde Numpy dizisi oluşturmak için
series = np.array([1,2,3,4,5])
series = np.array([1,2,3,4,5], dtype=np.float)


# İki boyutlu Numpy dizisi (matris) oluşturmak için
import numpy as np
series2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
mtrx = np.array(series2D)
print(mtrx)


# Random komutuyla iki boyutlu Numpy dizisi oluşturmak için
import numpy as np
import random
randmat = np.random.rand(2,3)
print(randmat)


# Belli bir atlama değeri ile dizi oluşturmak için np.arange() metodu kullanılır.
# Örneğin elemanları (0,1,2,3,4,5,6,7,8,9,10) olan bir dizi yerine; elemanları (2,4,6,8) gibi bir dizi oluşturmak isteyelim.
# arange() komutu ile dizi oluşturmak için
import numpy as np
zeroto10 = np.arange(10)
print(zeroto10)             # [0 1 2 3 4 5 6 7 8 9]

twoto10 = np.arange(2, 10, 2)
print(twoto10)              # [2 4 6 8]


# DİLİMLEME
# Dilimleme, bir index'ten diğer index'e kadar olan öğeleri almak anlamına gelir.
# Bunun için dşzşndeki [start: end] noktalarını seçmek gerekir.
# Ayrıca adım boyutunu seçerek de bir parça alınabilir. [start: end: step-size]
# Örneğin adım boyutunu 2 almak demek, öğeyi mevcut indexten 2 basamak uzağa almak demektir.
# Example 1:
series1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(series1[1:9:2])

# Example 2:
import numpy as np
series1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(series1[:11:2])   # [1 3 5 7 9]
print(series1[1::2])    # [ 2  4  6  8 10]
print(series1[1:11:])   # [ 2  3  4  5  6  7  8  9 10]


# İki boyutlu diziyi dilimleme
# İki boyutlu dizinin satırları ve sütunları vardır.
# Örnekte "series2" adında iki boyutlu bir dizi oluşturuldu.
# Matrisin sıfır indexli satır ve sütun elemanı, sonra satır indexi bir, sütun index değeri iki olan eleman; 
# daha sonra satır indexi bir ve sütun indexi sıfır olan matris elemanları dilimlenerek ekrana yazdırıldı
import numpy as np
series2 = np.array([[1,2,3,4,5][6,7,8,9,10]])
print(series2[0,0])   # 1
print(series2[1,2])   # 8
print(series2[1,0])   # 6


