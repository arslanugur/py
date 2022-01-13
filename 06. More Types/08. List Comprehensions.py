# Section 1
# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
# For example, we can do the following: 
cubes = [i**3 for i in range(5)]                        # HINT: double asterisk ** means to the power of, so 2**3 = 2 x 2 x 2 = 8   --> i**3 =i³
print(cubes)                    # [0, 1, 8, 27, 64]

# List comprehensions are inspired by set-builder notation in mathematics.

# range 5 means from 0 to 4 giving (0, 1, 2, 3, 4.) making 5 in total. 
# and the key is x**3. so; 0**3= 0×0×0= 0 1**3= 1×1×1= 1 2**3= 2×2×2= 8 3**3= 3×3×3= 27 4**3= 4×4×4= 64

# cubes = [i**3 for i in range(5)] is the same as:
# cubes= [] // create empty list
# for i in range(5): //looping 5 times
# cubes.append(i**3) //putting new values of i in the list . 
# If you look closely, you'll find that those two ways contain the same elements, just removed the colon and indentation, and re-arranged them. 


# Using list comprehension you can separate a dictionary into two lists one for keys and one for values: 
dict = {"key1":"value1", "key2":"value2", "key3":"value3",} 
keyList = [i for i in dict]         # Creates a list of keys 
valueList = [dict[i] for i in dict] # Creates a list of values
print(keyList)                      # [“key1”, ”key2”, ”key3”]
print(valueList)                    # [“value1”, ”value2”, ”value3”] 

# Example:
def power(a,b): 
    if b==0: 
        return 1 
    else: 
        return a*power(a,b-1) 

listA=[power(n,3) for n in range(10)] 
listB=[n for n in range(10)] 
print(listB)                # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(listA)                # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
                            # listA would contain the outputs of the function "power" applied on numbers in range from 0 to 10
        
# https://en.m.wikipedia.org/wiki/Set-builder_notation










#for döngüsüne alternative olur
"""
for x in range(10):
    print(x) #0dan 10a kadar yazdırır
#bu basit biliyoruz
"""

"""
numbers = []
for x in range(10):
    numbers.append(x)
#append ile aldığımız x değerini dizi üzerine aktarırırz
#aşağıdaki ile aynı sonuca varırız
"""
"""
#number adında bi dizi tanımla, dizi tanımlama aşamasında 
numbers = [x for x in range(10)] #birinci xin içine gelen değerler dizinin elemanlarını temsil eder
#range içerisinden 10 sayıyı for döngüsüyle tek tek x'in içine atıp bi x değeri elde edip bunları numbers dizisine atıyoruz
print(numbers)
"""

"""
for x in range(10):
    print(x**2) #altalta alır
"""
"""
numbers = [x**2 for x in range(10)]
print(numbers) #hepsinin karesini aldı liste şeklinde
"""

"""
#sadece 3e bölünenler karşımıza gelsin
numbers = [x*x for x in range(10) if x % 3 == 0] #her bi değerin karesini almak için
print(numbers)   #sadece 3e tam bölünebilen sayılar yazılır
"""

#bunları liste üzerinde nasıl tanımlarız
#str karakter tanımla
"""
myStr = 'Hallo'
myList = []  #burdan listeye çevirelim
for letter in myStr:
    myList.append(letter)
print(myList) #hallo bi dizi şekline dönüşür
"""

"""
#basit versiyonu
myStr = 'Hallo'
myList = [letter for letter in myStr]
print(myList)
"""

"""
#years isminde bi dzi tanımla
years = [1923,1945,1965,1987,1989] #her değere tek tek ulaşıp yaş bilgisini hesapla
ages = [2020 - year for year in years]
print(ages)
"""

"""
result = [x if x %2 == 0 else 'odd no' for x in range(1,10)]
#list elemanı yapmak yerine belli bi koşul eklenebilir
#birinci x dahil olması için ifli ifadenin tru değeri getirmesi gerekir. değilse tek sayı
print(result) #135 gibi sayılar için odd no yazdırdı
"""

"""
#içiçe iki döngümüz varsa
result = []
for x in range(3): #loop x için 3 kere döncek
    for y in range(3): #x 0dan başlayıp 0a geldiğinde, y 3e kadar gitcek yani y için bi loop olcak
        result.append((x,y)) #her bi eleman append ile result içine aktarılacak
print(result)
#y bittiğinde tekrar başa döncek bu sefer x 1 ile başlayıp y'ye geçecek
"""
#basitleştirirsek - yine x ve y için birer döngü
numbers = [(x,y) for x in range(3) for y in range(3)]
#x için olan for loopnunu x içine aldık (x,y)
#y için olan for loopunu y içine aldık(x,y)
print(numbers) #sonuç aynı

#3 elemanlı da olabilir
#numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]


####EXAMPLES
cubes = [i ** 3 for i in range(5)]
print(cubes)

evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)



a = [x * 10 for x in range(5,9)]
