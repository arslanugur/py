#loop operators
"""
list = [1, 2, 3, 4, 5]
for item in list:
    print(list) #elemnlar tek tek ekrana yazılır
"""
#ama elimizde bi liste yoksa 0-100 yazdırcaksak bunu while ile yapabiliriz
# ama for döngüsüyle bunu nasıl yaparız?  range()
#range while için de kullanılabilir

#RANGE METODU
""" 
for item in range(10): #10 değerini verip çalıştırdığımızda 10a kadar gösterir
    print(item)   #başlangıç 0 son sayo 9 olur, 10değil
#range aslında bi liste oluşturuyor
"""
"""
for item in range(2, 15): #2den başla 15e kadar git 
    print(item) #bu range listesi içinden itemler tek tek alınır yazılır
"""
"""
for item in range(3,33,3):
#3den başla 33e kadar git, artış miktarı da 3er 3er olsun 
    print(item)
#ardışık sayılar için ideal
print(list(range(30,330,30))) #range ile gelen bilgileri listeye çeviririz.tür dönüşümü
"""

#ENUMERATE METODU
#eg str bi bilgimiz var

"""
greet ='hello there'
for letter in greet:
    print(letter) #tek tek kelimeler yine ekrana yazdırılır
"""    
#yukarı bilindik zaten, 
# ama her ulaştığımız harfin indexine ulaşmak istersek eğer

"""
#yukarıya bi index elemanı tanımlnır
index = 0 #bunu hile döngülerinde yapıyorduk zaten

greet ='hello there'
for letter in greet:
    print(f'index: {index} letter: {letter}') 
    #print(f'index: {index} letter: {greet[index]}') #böyle de olabilir aynı sonuç yine
    index += 1 #bunu 0dan başlatırız her döngü de bize bi index numarası da gelebilir
"""
"""
#index değişkenini tanımlamadan nasıl olacak peki
greet ='hello there'
for index, letter in enumerate(greet): 
    print(f'index: {index} letter: {letter}') #yine aynı sonucu elde ederiz
"""
"""
greet ='hello there'
for item in enumerate(greet): 
    print(item) 
#enumerate bu kez bize liste şeklide verir
"""


#ZIP METODU
"""
list1 = [1,2,3,4,5]   #kullanıcı adı gibi mesela
list2 = ['a','b','c','d','e'] #telefon numaraları gibi mesela
#iki listeyi de birleştirelim
#bunları dict ile yapabiliyoruz ama elimizde böyle bi veri old düşünelim
#her kişi hangi telefona sahip bulmak için ayrı bi list hazırlamak lazım
#index bazlı bi eşleştirme listesi

print(list(zip (list1, list2))) #zip ile bi match yapılır bunu da başına list koyup listeye çeviririz
#1 a'ya karşılık 2 b'ye karşılık
"""

#üçüncü farklı bi liste tanımlarsak

list1 = [1,2,3,4,5]  
list2 = ['a','b','c','d','e']
list3 = [10,20,30,40,50]

#print(list(zip (list1, list2, list3)))  #yan yana yazdırılır

"""
#bunları for döngüsünde nasıl kullanırız
for item in zip (list1, list2, list3):
    print(item) #bu kez alt alta yazdırılır
"""
"""
for a,b,c in zip (list1, list2, list3):
    print(a) #sadece a değerini alırsak liste gibi yazılmaz
    #print(a,b,c) #liste içinden çıkar hepsi
"""
