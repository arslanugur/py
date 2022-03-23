# Control Structures: 
# Sıralı, Seçimli, Tekrarlı olarak üçe ayrılır.
# Sıralı Kontrol Yapıları
    # Herhangi bir karşılaştırma işlemi olmaz

# Seçimli Kontrol Yapıları
    # Dallanma, iki ya da daha fazla alternatif yol arasından seçim yapma durumunda olan problemlerin çözümünde kullanılır.
    # if, if...else

# Tekrarlı Kontrol Yapıları
    # Döngü için kullanılan bu yapı, bir kodu arka arkaya bir çok kez çalıştırır.
    # for loop, while loop

# SECTION 1: IF
# Sonuç açısından iki durum varsa
point = 80
if point>85:
  print("Pass")
else:
  print("Fail")     #
#

# Sonuç açısından ikiden fazla durum varsa
point = 65
if point>85:
  grade = "A"
elif point>70:
  grade = "B"
elif point>60:
  grade = "C"
elif point>50:
  grade = "D"
else:
  grade = "F"

print(grade)


# Example:
x = 7
y = 10
if x>y:
    print("x is bigger than y")
elif x ==y:
    print("x and y are equals")
else:
    print("y is bigger than x")
#

# in işlecinin kullanımı
# Example 1:
text1 = "Hello Science"
if ("Hello" in text1):
    print("Yes, this word is in text1")             # True sonucu üretir.
else:
    print("No, this word is not in text1")
#

# Example 2:
myList = [10, 20, 30, 40, 50]
if (90 in myList):
    print("Girilen değer listenin içinde var.")
else:
    print("Girilen değer listenin içinde yok.")     # False sonucu üretir.
#


# SECTION 2: FOR LOOP
# For yapısısıralı geçişler için kullanılır.
# Örneğin: Bir liste, string veya dizide gezinme/dolaşmak gibi
# Py'da -- for (i=0; i<n; i++) -- gibi diğer dillerdeki gibi bir yapı yokç
# bunun yerine - for in - döngüsü kullanılır.
# Example 1:
myList = [1, 2, 3, 4, 5]
for numbers in myList:
    print(numbers, "-", "Science Lesson")
#

# Example 2:
myList=[1, 2, 3, 4, 5]
for numbers in myList:
    print(numbers*7)
#

# Example 3: for loop with if
myList = [1, 2, 16, 4, 5]
for numbers in myList:
    if numbers%2 == 0:          # (%2) ifadesi bölmede kalan değerin sıfır olup olmadığını kontrol eder.
        print(numbers, "-", "Even Numbers")
#

# Example 4: for loop with if
myList = [1, 2, 16, 4, 5]
for numbers in myList:
    if numbers%2==0:    # Py'de eşit ifadesi == ile yapılır.
        print(numbers, "-", " is Even Number")
    else:
        print(numbers, "-", " is Odd Number")
#

# For döngüsüyle liste veri yapısının dışındaki diğer veri tipleri ile de işlemler yapmak mümkündür.
# Example 5:
myWord="Data"
for letter in myWord:
    print(letter)
#

# Example 6: Harfleri tek bir satırda yazdırmak
myWord="Data Science"
for letter in myWord:
    print(letter, end==" ")     # end=" ", ifadesi karakterlerin tek satırda yazdırılmasını sağlar.
#

# For Döngüsünün Py veri yapıları ile kullanımı
# Example 1: Küme Veri Yapısının Kullanımı
set1 = {("A", 1), ("S", 54), ("T", 34)}
for city in set1:
    print(city)
# Example 2: Küme Veri Yapısının Kullanımı
set2 = {("A", 1), ("S", 54), ("T", 34), ("K", 36)}
print("-"*10, "İkinci Örneğin Çıktısı", "-"*10)
for (x, y) in set2:         # Görüldüğü gibi tuple'ın içeriği (x, y) değişkenlerine aktarıldı
    print("City's Name:", x,";      City's Number:",y)              # x ve y değişkenleri yazdırıldı
#


# For döngüsünün, Sözlük veri yapısı ile Kullanımı
# Example 1:
dict1 = {"stu1":70,"stu2":45,"stu3":90,"stu4":30,"stu5":100}
print("-"*5, "Birinci Örneğin Sonucu","-"*5)
for (key, value) in dict1.items():
    print(key)
#

# Example 2:
dict1 = {"stu1":70,"stu2":45,"stu3":90,"stu4":30,"stu5":100}
print("-"*5, "İkinci Örneğin Sonucu","-"*5)
for (key, value) in dict1.items():
    print(value)
#

# Example 3:
dict1 = {"stu1":70,"stu2":45,"stu3":90,"stu4":30,"stu5":100}
print("-"*5, "Üçüncü Örneğin Sonucu","-"*5)
for (key, value) in dict1.items():
    print(key,": ",value)
#

# For döngüsünün iç içe kullanımı
# Example:
attributes = ["red","big","tasty"]
fruits = ["apple","banana","strawberry"]

for x in attributes:
    for y in fruits:
        print(x, "-", y)
#



# SECTION 2: WHILE LOOP
# Example 1: 1'den 10'a kadar sayıları yazdırmak için while kontrol yapısı
x = 1
while x<11:
    print(x, end=" ")
    x = x+1             # bir sonraki döngü için x her seferinde 1 arttılıyor
#

# Example 2:
y = 1
while y<5:
    print("Science")
    y = y+1
#

# Example 3:
myList = [2,4,6,8,10]
t = 1
while 6 in myList:
    print("6 sayısı", t, ".kez hala listemde")
    myList.pop()            # listenin en son elemanını siler, t=1 de 10'u siler
                            # t=2 de 8'i siler, t=3 te 6'yı siler.
    t = t+1
#

# Break: Şart ifadesinin True olduğu anda geçerli döngüyü sonlandırır,
       # Şart ifadesi gerçekleşmediği sürece False döngü içindeki ifadeler yürütülmeye devam eder.
#

# Listedeki tüm elemanlar sırayla okunduktan sonra 5 ile çarpılır.
# Sonrasında (if numbers == 30) şartı gerçekleştiği için geri kalan liste elemanları yazdırılmadan döngüden çıkar. 
# Example 1:
myList = [15,20,25,30,35,40,45,50]
print("-"*5, "Birinci Örneğin Çıktısı", "-"*5)
for numbers in myList:
    print(numbers*5)
#

# Example 2:
myList = [15,20,25,30,35,40,45,50,55,60]
print("-"*5, "İkinci Örneğin Çıktısı", "-"*5)
for numbers in myList:
    if numbers == 30:
        break
    print(numbers*5)
#

# Example:
# While döngüsünün durdurulması
while True:
    answer = input("Enter a number (write 0 to exit):")
    print("The number which you inputted: ", answer)
    if int(answer) == 0:
        print(answer, "you pressed the number (exit)!!)
        break
 #


# Continue anahtar komutu
# Continue, Break döngü kontrol komutunun tam tersidir.
# Döngüyü bir sonraki yinelemeyi devam ettirmeye veya yürütmeye zorlar.
myList = [15,20,25,30,35,40,45,50]
print("-"*5,"Birinci Örneğimizin Çıktısı","-"*5)
for numbers in myList:
    print(numbers, end=" ")
#
myList = [15,20,25,30,35,40,45,50]
print("-"*5,"İkinci Örneğimizin Çıktısı","-"*5)
for numbers in myList:
    if numbers == 30:
        continue            # 30 sayısına gelince bir sonraki sayıya atlanacak
    print(numbers, end=" ")
#


# Range Metodu
# Bu metodu belli bir sayı aralığı girilir ve bu sayı aralığının içerisinde liste elemanları otomatik oluşturulur
# List ve String gibi veri yapılarında for ve while döngüsü ile birlikte kullanılır.

# range(stop)
for numbers in list(range()):
    print(numbers, end=" ")
# range(start,stop)
for numbers in list(range(5, 20)):
    print(number, end=" ")
# range(start, stop, step)              
for numbers in list(range(5, 20)):
    print(numbers, end=" ")
# range(start, stop, step)
for numbers in list(range(5,20,3)):
    print(numbers, end=" ")
#


# Random Metodu
# Rastgele Float tipinde sayı üretmek için
import random
random.random()

# Rastgele Integer tipinde sayı üretmek için
import random
print("1 ile 100 arasında bir sayıüretelim.")
number1 = random.randint(1, 100)
print("Üretilen Integer Sayı: ", number1)
              
# Belli bir aralıkta istenen sayıda rastgele tamsayı dizisi oluşturmak için
from numpy.random import randint
for tamsayilar in randint(0,10,20):
    print(tamsayilar, end=" ")
#

# Zip Metodu
