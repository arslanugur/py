#tuple da liste gibi ama biraz farklı
list = [1, 2, 3] #liste tanımlanması
tuple = (1, 'two', 3) #paranteze gerek yok ama okunabilirlik için () kullan

#bunların tiplerine bakarsak
print(type(list))
print(type(tuple))

#liste elemanlarına index ile ulaşmak
print(list[0])
print(tuple[1])

#eleman sayılarını yazdırmak istersen
print(len(tuple))

#eleman değişikliği
list[0] = 'one'   #ama tuple için bu şekilde atama yapılmaz
print(list)
# tuple için eleman atandıktan sonra değişim olmaz,
# #bu yüzden yeni bi liste oluşturman gerekli
# list üzerinden kullanılabilecek method çokken
# list.append() gibi
# tuple için bu metodlar oldukça az
print(tuple.count('two'))
print(tuple.index(3)) #3 karakterinin indexini buldu 2

# listeye tuple listesi ekleme
numbers = ('four', 5, 'six') + tuple
print(numbers)

#listede düzenleme, eleman ekleme ve silme işlemi tuple da olmaz
