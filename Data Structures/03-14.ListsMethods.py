numbers = [2, 3, 7, 1, 98, 67]
letters = ['a', 's', 'z', 'e', 'r', 'u']

val = min(numbers) #numbers dizilerinderinde minimum değer
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6] #bunu stringlerde de yapıyoruz
val = numbers[:4]
val = numbers[3:]
print(val)

numbers[4] = 40 #index nosu 4 olan sayı 40 olur
print(numbers)

numbers.append('500') #ekleme methodu str olarak eklendi
print(numbers)
numbers.append(50) #numnber olarak eklenir
print(numbers)
numbers.insert(3, 79) #üçüncü index'in yerine 79 sayısını ekle
numbers.insert(-2, 88) #son indexin yerine 88 ekle - her bi sayı kendine yer açıyor
print(numbers)

numbers.pop() #append ile eklediğin integer'ı siler.
numbers.pop(0) #sıfırıncı indexi siler
numbers.pop(-1) #sondaki indexdeki str/int silinir
print(numbers)

numbers.remove(7) #remove metodu silme istediğin karakteri ver, ,indexi değil
print(numbers)

numbers.sort() #liste sayısal büyüklük olarak sıralanır
numbers.reverse() #liste tam tersine çevrilir
print(numbers)
letters.sort()
letters.reverse()
print(letters)

print(len(numbers)) #eleman sayısını yaz
print(len(letters))

print(numbers.count(7)) #count metodunu çağırıp numbers üzerinden kaç tane 7 int var öğreniriz
print(letters.count('a')) #kaç tane a var

numbers.clear() #numbersdaki tüm elemanlı siler []
print(numbers) 
