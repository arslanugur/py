# SECTION 1
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


# Example: 
nums = [i*2 for i in range(10)] # This list comprehension create a list of even numbers between 0 and 18

# range(10) refers to ALL numbers from 0(inclusive) to 10(NON-inclusive). 
# Hence, range(10) REALLY refers to 0,1,2,....,8,9 i*2 just means multiply i by 2 aka double it. 
# So, i =0 => 0 i =1 => 2 i =2 => 4 .... .... .... i =8 => 16 i =9 => 18 
# So, nums = [0,2,4,...,16,18].

# 1.) range(10) are numbers from 0 to 9 
# 2.) i*2 is 2 multiplied by the numbers in the range(10). 
# That is: 0 * 2 = 0 1 * 2 = 2 2 * 2 = 4 3 * 2 = 6 4 * 2 = 8 5 * 2 = 10 6 * 2 = 12 7 * 2 = 14 8 * 2 = 16 9 * 2 = 18 
# 3.) print(nums) will print the numbers within the range when multiplied by 2. that is: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# 10 list items not the final value of 10


# SECTION 2
# A list comprehension can also contain an if statement to enforce a condition on values in the list.
# Example:
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)                                        # [0, 4, 16, 36, 64]

# create a LIST called evens which contains elements given by the follow: 
# i² for EACH i in range(10), 
# so each i from 0(inclusive) to 10(NON-inclusive), on the CONDITION that the resulting i² MUST have 0 as its remainder when divided by 2.

# You can add as many 'if's as you want! 
evens=[i**2 for i in range(10) if i**2 % 2 == 0 if i**2 % 3 == 0] 
print(evens) # output: [0, 36]

# Example:
evens = [i**2 for i in range(10) if i%2 == 0] 
# could be written in a longer way like this:
evens = []
for i in range(10):
    i = i**2
    if i%2 == 0:
        evens.append(i) 
#
# 1- list name, equals, opening square brackets. 
# 2- name of an imaginary variable (python devs usually use i) 
# 3- operation to do on the variable. (multiply by 2, or add 2 or something) 
# 4- for/while loop (to indicate how many times u want to do the previous operation) 
# 5- any additional conditions (using 'if' statements) 6- closing square brackets.

# Second Way:
events=[] 
for i in range(5): 
    if (i*i) % 2 == 0: 
        events.append(i*i)
#

# evens = [i**2 for i in range(0,10,2)] gives the same output as evens = [i**2 for i in range(10) if i**2 % 2 == 0] output >>> [0,4,16,36,64]


# Because: range(10) = range(0, 1, 2, 3, 4, 5, 6, 7, 8, 9) 0**2 = 0 and 0/2 has remainder 0
# this will print because remainder is 0 1**2 = 1 and ½ has remainder ? 2**2 = 4 and 4/2 has remainder 0 
# this will print because remainder is 0 3**2 = 9 and 9/2 has remainder 1 4**2 = 16 and 16/2 has remainder 0 
# this will print because remainder is 0 #and so on up through the 9th index in the range(10) 
# with all even numbers having remainder of 0 and therefore printed 8**2 = 64 and 64/2 has remainder of 0 
# this will print because remainder is 0 9**2 = 81 and 81/2 has remainder of 1 We should print: 
# all of the integers (i.e: i) in the range(10) for which: 
# when multiplied to the power of 2 (i.e.: **2) have no (i.e.: 0) remainder when divided by 2 (i.e.: %2). 
# This is why the results are: [0, 4, 16, 36, 64]
    
# it could have just add easily been i % 2 == 0 as i**2 % 2 == 0 for the condition. 
# if an even square has an integer square root then its square root is even ;) 

# To simplify it 
# First part: i**2 for i in range(10) will print [0,1,4,9,16,25,36,49,64,81] 
# Second part: i**2 % 2 == 0 
# This if condition will make sure the values from the first part is only printed when the remainder of it will be zero. 
# 0%2 =0 - print 0 
# 1%2 = 0.5 - dont print
# 4%2 = 0 - print 4 
# 9%2 = 1 - dont print 
# 16%2 = 0 - print 16 
# 25%2 = 1 - dont print 
# 36%2 - 0 - print 36 
# 49%2 = 1 - dont print 
# 64%2 = - print 64 
# 81%2 = 1 - dont print 
# Hence the values printed are [0,4,16,36,64]


# Section Example: Create a list of multiples of 3 from 0 to 20.
a = [i for i in range(20) if i% 3 == 0]

evens=[i for i in range(0,20,3) ]



# Example:
evens = [i**2 for i in range(10) if i**2%2==0]
print(evens)                # [0, 4, 16, 36, 64]
# Create a list where each number within the range 0-9 is squared and then only include the numbers whose remainder is equal to 0 when divided by 2.
# --- breakdown of the math--- (r=remainder) 
# i=0 ---> 0**2=0 ---> 0÷2=0.0 (r=0.0)
# i=1 ---> 1**2=1 ---> 1÷2=0.5 (r=0.5) 
# i=2 ---> 2**2=4 ---> 4÷2=2.0 (r=0.0)
# i=3 ---> 3**2=9 ---> 9÷2=4.5 (r=0.5) 
# i=4 ---> 4**2=16 ---> 16÷2=8.0 (r=0.0)
# i=5 ---> 5**2=25 ---> 25÷2=12.5 (r=0.5) 
# i=6 ---> 6**2=36 ---> 36÷2=18.0 (r=0.0)
# i=7 ---> 7**2=49 ---> 49÷2=24.5 (r=0.5) 
# i=8 ---> 8**2=64 ---> 64÷2=32.0 (r=0.0)
# i=9 ---> 9**2=81 ---> 81÷2=40.5 (r=0.5)

# Example:
evens = [i**2 for i in range(10) if i**2 % 2 == 0] 
# you can simple write the list comprehensions like this 
evens = [i**2 for i in range(10) if i%2 == 0] 
print(evens)
# you can also use double for like this 
res = [(i, j) for i in range(5) for j in range(5)] 
print(res)
# with the output this [[0,0],[0,1],[0,2],[0,3], [0,4], [1,0],[1,1],[1,2], [1,3], [1,4], 
#                       [2,0],[2,1],[2,2], [2,3], [2,4], [3,0],[3,1],[3,2], [3,3], [3,4], [4,0],[4,1],[4,2], [4,3], [4,4]]


a=[i for i in range(0,20,3)]



# SECTION 3
# Trying to create a list in a very extensive range will result in a MemoryError.
# This code shows an example where the list comprehension runs out of memory.
even = [2*i for i in range(10**100)]
# output: No output.

# This issue is solved by generators, which are covered in the next module.


# Example:
n = 100 
for m in range(100): 
    try: 
        even = [2*i for i in range(10**n)] 
        print (even) 
    except MemoryError: 
        n -= 1
# Output: No output.


# Example:
for i in range(10): 
    ans=i*2 
    if ans%2==0: 
        print(ans) 
    else: 
        print('odd number')
#                


# Example:
even = [2*i for i in range(89713)] 
print(len(even))                    # 89713
print(even[len(even)-1])            # 179424


# Example: to create a list of numbers multiplied by 10 in the range of 5 to 9.
a = [x*10 for x in range(5, 9)]     # generates numbers from 5 to 8 (not to 9).

# let me dissect this one also a = [ x * 10 for x in range(5,9)] now remember the (x) is = 5,9 
# now lets start from the begining. 0 0 1. 1 2. 2 3. 3 4. 4 5. 6. 7 8 
# now we gonna start with the #single integers. 5 * 10 = 50 6 * 10 = 60 7 * 10 = 70 8 * 10 = 80 print(a) output:. 50 , 60 , 70 , 80 

# Example:
import math
print ("\n".join([["fizzbuzz",["buzz",["fizz",str(n)][math.ceil(n%3/n)]][math.ceil(n%5/n)]][math.ceil(n%15/n)] for n in range(1,100)]))
# 130 characters







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
