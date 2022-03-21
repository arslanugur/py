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


# SECTION 2: FOR
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















