# SECTION 1: LIST
# Liste veri yapısı oluşturma
list1= [10,20,30,40,50]
print(list1)          # Output: [10,20,30,40,50]

# Listenin birinci elemanına ulaşmak için
list1[0]
# Listenin birinci elemanının değerini değiştirme
list1[0] = 5          # Output: [5,20,30,40,50]

# Listenin uzunluğunu öğrenmek için
len(list1)

# Listeye yeni bir eleman eklemek için
list1.append(120)         # Ekleme işlemi tırnak paranteziyle yapılır
# Output: [5,20,30,40,50,120]

# Listeye farklı bir liste eklemek için
list2 = ['A','B','C']          # Metinsel bir veri içeren liste
list2= [10,20,30,40,50, list_2]
print(list2)          # Output: [5,20,30,40,50, ['A','B','C']]


# Listenin birden çok elemanına erişmek için
list2[1:4]      # [20,30,40]
list2[1:5]      # [20,30,40,50]
# Example:
list20 = [11,12,13,14,15,16]
print(list20[1:4])          # 12,13,14


# Başlangıç ve bitiş index'i belirtilmeden istenen sayıda elemana erişmek için
list2[:3]       # [5,20,30,40]          # Başlangıç değeri 0'dır.
list2[2:]       # [30,40,50,120]


# Atlama aralığı ile liste elemanlarını yazdırmak için
list3=[12,34,83,94,384,623,808,1029,3812,8637]
list3[4:9:2]           # [a:b:k]     --> k: liste elemanlarını yazdırırken atlanılacak aralık değerlerini belirtir
                        # a ile başlar, fakat b-1 ile biten elemanları gösterir.

# listedeki bir elemanın index numarasını bulmak için
names = ["A","B","C","D","E","F"]
names.index("B")            # 1             # index metodu kullanılır.

# Listede index numarası girilen elemanı silmek için
names.pop(1)
print(names)                # Output: ["A","C","D","E","F"]


# Listeden del() ve .remove() metodu ile eleman silmek içim
final = [60,70,80,45,55,77]
del(final[2])               # Index değeri 1 olan elemanı del komutu ile silinir
print(final)                # Output: [60,80,45,55,77]
# Example:
list10 = [11,12,13,14,15,16,17]
print(del(list10[4]))       # 15 silinir.

final.remove(1)     
print(final)                # Output: [60,80,45,55,77]
# Example:
list30 = [11,12,13,14,15,16]
print(list30.remove(14))    # 11,12,13,15,16


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



# SECTION 2: TUPLE
# Tuple (Demet) oluşturmak için
tuple1 = (3.14,2.78,5.67,78.9)            # Float tipinde bir tuple
tuple2 = ("A","B","C","D",98,65,43)       # String ve Integer tipinde tuple
# Tuple öğelerine erişmek için
tuple2[0]        # Output: 'A'
# Example:
tuple10 = (20,30,40,50,60,70,80,90,100)
print(tuple10[8])   # 100

# Tuple elemanları değiştirilemez
# Mutable:    Programın çalışması sırasında değiştirilebilir    ---> Tuple nesnelerine veri eklemek ve veri silmek işlemi gerçekleşmez. Hata verir
# Immutable:  Programın çalışması sırasında değiştirilemez      ---> List, Dict, Set

# Tuple nesnelerine veri eklemek ve veri silmek işlemi gerçekleşmez. Hata verir.
# Ancak nesnelerinin her bir elemanı farklı bir değişkene aktarılabilir.
tuple3 = (3.14,2.78)
pi,e = tuple3
print(pi)       # Output: 3.14
print(e)        # Output: 2.78
# Example:
tuple20 = (12,13,14,15)
tuple20 = x,y,z,k
print(tuple20)      # z = 14

tuple4 = (12,14,18)
a,b,c = tuple4
print(a,b,c)    # Output: 12 14 18


# SECTION 3: SET
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

###
shopping.discard("meat")      # Kümeden öğe çıkarmak için method
shopping.pop()                # Kümeden ilk ve sonuncu eleman dışında rasgele öğe silmek için method



# SECTION 4: DICT
# {key:value}
# Sözlük oluşturma işlemi için
model = ["A","B","C","D","E"]                 # generate a list
price = [15.70, 19.59, 25.70, 17.15, 23.45]   # generate a second list
modelprice_dict = {'A':15.7, 'B':19.59, 'C':25.70, 'D':17.15, 'E':23.45}
type(modelprice)      # Output: dict

modelprice_dict2 = ([('A', 15.7), ('B', 19.59), ('C', 25.70), ('D', 17.15), ('E', 23.45)])
print(modelprice_dict2)       # Output: {'A':15.7, 'B':19.59, 'C':25.70, 'D':17.15, 'E':23.45}


# Sözlük elemanlarına erişmek için
# Bir sözlük verisinden key'leri öğrenmek için .keys() metodu
# Sözlük değerlerini görmek için .values() metodu kullanılır.
dict1 = {"number":50, "text":["A","B","C"], "dictionary":{"A":100}}
print(dict1)        # Output: {"number":50, "text":["A","B","C"], "dictionary":{"A":100}}

print(dict1["dictionary"])    # Output: {"A":100}

dict1.keys()          # Anahtar kelimelerini öğrenmek için
# Output: dict_keys(['number','text','dictionary'])
dict1.values()        # Değerleri öğrenmek için
# Output: dict_values([50, ['A','B','C'], {'A':100}])


# Sözlük elemanlarında değişiklik ve Güncelleme yapmak için
# .update metodu kullanılır
dict2 = {"key1":1100,"key2":"A"}  # Generate a new dict
dict2["key2"] = "S"               # Change the second key's value
print(dict2)                      # Output: {"key1": 1100, "key2": "S"}

dict3 = {"house1":300,"house2":350,"house3":400}
print(dict3)                      # Output: {"house1": 300, "house2": 350, "house3": 400}
new_house = {"house4":375,"house5":450}
dict3.update(new_house)
print(dict3)                      # Output: {"house1": 300, "house2": 350, "house3": 400, "house4": 375, "house5": 450}

# Example:
l = {"name1": "C", "name2": "D", "name": "E"}
# C'yi, M olarak değiştirmek için
l["name1"] = "M"
print(l)

# Other Methods for Dict
### .clear()      .items()      .popitem()      .pop()
new_house2 = {"house6":475,"house7":550}

new_house2.items()                # Sözlüğün anahtar ve değer elemanlarını görüntüler
# Output: dict_items([('house6',475), ('house7', 550)])

new_house2.popitem()      # Sözlüğün son anahtarını ve değerlerini siler
print(new_house2)         # {'house6': 475}

new_house2.pop("house6")  # Anahtar değeri girilen sözlük elemanını siler
print(new_house2)         # {'house7': 550}

new_house2.clear()        # Sözlüğün tüm içeriğini siler
print(new_house2)         # {}


