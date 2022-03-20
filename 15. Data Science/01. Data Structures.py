# Liste veri yapısı oluşturma
list_= [10,20,30,40,50]
print(list_)
# Output: [10,20,30,40,50]

# Listenin birinci elemanına ulaşmak
list_[0]
# Listenin birinci elemanının değerini değiştirme
list_[0] = 5
# Output: [5,20,30,40,50]

# Listenin uzunluğunu öğrenme
len(list_)

# Listeye yeni bir eleman ekleme
list_.append(120)         # Ekleme işlemi tırnak paranteziyle yapılır
# Output: [5,20,30,40,50,120]

# Listeye farklı bir liste ekleme
list_1 = ['A','B','C']          # Metinsel bir veri içeren liste
list_= [10,20,30,40,50, list_1]
print(list_)
# Output: [5,20,30,40,50, ['A','B','C']]


# Listenin birden çok elemanına erişme
list_[1:4]      # [20,30,40]
list_[1:5]      # [20,30,40,50]

# Başlangıç ve bitiş index'i belirtilmeden istenen sayıda elemana erişme
list_[:3]       # [5,20,30,40]
list_[2:]       # [30,40,50,120]


# Atlama aralığı ile liste elemanlarını yazdırma
list_2=[12,34,83,94,384,623,808,1029,3812,8637]
list_2[4:9:2]           # [a:b:k]     --> k: liste elemanlarını yazdırırken atlanılacak aralık değerlerini belirtir



35








