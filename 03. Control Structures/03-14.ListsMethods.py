numbers = [2, 3, 7, 1, 98, 67]
letters = ['a', 's', 'z', 'e', 'r', 'u']

val = min(numbers)  #numbers dizilerinderinde minimum değer
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]   #bunu stringlerde de yapıyoruz
val = numbers[:3]
val = numbers[4:]
print(val)

numbers[4] = 40 #index nosu 4 olan sayı 40 olur

numbers.append(49) #numara ekleme, '49' str olarak ekleme
numbers.append(59)
numbers.insert(3, 79) #üçüncü index'in yerine 79 sayısını ekle
numbers.insert(-1,52) #son indexin yerine 88 ekle - her bi sayı kendine yer açıyor

numbers.pop() #append ile eklediğin integer'ı siler.
numbers.pop(0) #sıfırıncı indexi siler
numbers.pop(-1) #sondaki indexdeki str/int silinir
numbers.remove(59)
print(numbers)

numbers.sort()
numbers.reverse()

letters.sort()      #harf listesi sayısal büyüklük/sırasal olarak sıralanır
letters.reverse()   #harf listesi tam tersine çevrilir


print(numbers)
print(letters)

print(len(numbers))      #len - eleman sayısını gösterir
print(len(letters))

print(numbers.count(10))    #count metodunu çağırıp numbers üzerinden kaç tane 7 var öğreniriz
print(letters.count('a'))   #kaç tane a var

numbers.clear()    #numbersdaki tüm elemanlı siler []
print(numbers)

numbers.remove(7) #remove metodu silme istediğin karakteri ver, ,indexi değil
print(numbers)
