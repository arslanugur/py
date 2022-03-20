# SECTION 1: LIST
# Liste veri yapısı oluşturma
list_= [10,20,30,40,50]
print(list_)
# Output: [10,20,30,40,50]

# Listenin birinci elemanına ulaşmak için
list_[0]
# Listenin birinci elemanının değerini değiştirme
list_[0] = 5
# Output: [5,20,30,40,50]

# Listenin uzunluğunu öğrenmek için
len(list_)

# Listeye yeni bir eleman eklemek için
list_.append(120)         # Ekleme işlemi tırnak paranteziyle yapılır
# Output: [5,20,30,40,50,120]

# Listeye farklı bir liste eklemek için
list_1 = ['A','B','C']          # Metinsel bir veri içeren liste
list_= [10,20,30,40,50, list_1]
print(list_)
# Output: [5,20,30,40,50, ['A','B','C']]


# Listenin birden çok elemanına erişmek için
list_[1:4]      # [20,30,40]
list_[1:5]      # [20,30,40,50]

# Başlangıç ve bitiş index'i belirtilmeden istenen sayıda elemana erişmek için
list_[:3]       # [5,20,30,40]          # Başlangıç değeri 0'dır.
list_[2:]       # [30,40,50,120]


# Atlama aralığı ile liste elemanlarını yazdırmak için
list_2=[12,34,83,94,384,623,808,1029,3812,8637]
list_2[4:9:2]           # [a:b:k]     --> k: liste elemanlarını yazdırırken atlanılacak aralık değerlerini belirtir
                        # a ile başlar, fakat b-1 ile biten elemanları gösterir.

# listedeki bir elemanın index numarasını bulmak için
names = ["A","B","C","D","E","F"]
names.index("B")        # 1             # index metodu kullanılır.

# Listede index numarası girilen elemanı silmek için
names.pop(1)
print(names)      # Output: ["A","C","D","E","F"]


# Listeden del() ve .remove() metodu ile eleman silmek içim
final = [60,70,80,45,55,77]
del(final[2])               # Index değeri 1 olan elemanı del komutu ile silinir
print(final)                # Output: [60,80,45,55,77]

final.remove(1)     
print(final)                # Output: [60,80,45,55,77]


# Listede yer alan elemanları sıralamak için        .sorted()     metodu kullanılır.
# Sıralama işlemini büyükten küçüğe yapmak için     reverse=TRUE  argümanı yazılması gerekir.
# Listedeki elemanları tersten yazdırma için        .reverse()    metodu kullanılır.


# Example: Temperature Values 
temperature_values = [22,23,25,18,27,23,20,23,27]
# Sıcaklık değerleri küçükten büyüğe doğru sıralamak için
sorted(temperature_values)      # Output: [18,20,22,23,23,23,25,27,27]
# Sıcaklık değerlerinin listedeki sırası ters çevirmek için
temperature_values.reverse()    
print(temperature_values)       # Output: [27, 23, 20, 23, 27, 18, 25, 23, 22]



# SECTION 2: TUPLE, SET, DICT
# Tuple oluşturmak için
tuple1 = (3.14,2.78,5.67,78.9)            # Float tipinde bir tuple
tuple2 = ("A","B","C","D",98,65,43)       # String ve Integer tipinde tuple
# Tuple öğelerine erişmek için
tuple2[0]        # Output: 'A'

# Mutable:    Programın çalışması sırasında değiştirilebilir    ---> Tuple nesnelerine veri eklemek ve veri silmek işlemi gerçekleşmez. Hata verir
# Immutable:  Programın çalışması sırasında değiştirilemez      ---> List, Dict, Set

# Tuple nesnelerine veri eklemek ve veri silmek işlemi gerçekleşmez. Hata verir.
# Ancak nesnelerinin her bir elemanı farklı bir değişkene aktarılabilir.
tuple3 = (3.14,2.78)
pi,e = tuple3
print(pi)       # Output: 3.14
print(e)        # Output: 2.78

tuple4 = (12,14,18)
a,b,c = tuple4
print(a,b,c)    # Output: 12 14 18


# SET
# Küme oluşturma örneği
my_set1 = {1,2,3,4,5}

# Liste'yi Küme'ye dönüştürmek için
list1 = [1,2,3,4,5,6]
my_set2=set(list1)
print(my_set2)      # Output: {1,2,3,4,5,6}
type(my_set2)       # Veri yapısının türünü öğrenmek için

# Tuple verisini Küme'ye dönüştürmek için
market_list = ("apple","milk","cheese","oil","milk","bread","drink")
type(market_list)   # Output: tuple
shopping=set(market_list)
print(shopping)                                 # Output: {"apple","milk","cheese","oil","bread","drink"}

# Kümeye veri ekleme, silme, çıkarma işlemleri
shopping.add("yoghurt")                         # Output: {"apple","milk","cheese","oil","bread","drink","yoghurt"}
# Kümeye ikinci bir ek liste eklemek için
market_list2["eggs","lemon","meat"]
shopping.update(market_list2)
print(shopping)                                 # Output: {"apple","milk","cheese","oil","bread","drink","yoghurt","eggs","lemon","meat"}


49













