#03. python objeleri ve veri yapıları
print (2+2)
#sayı tipleri (number)
#1. integer (tam sayılar: 1, 25, -23)
#2. float (ondalıklı sayılar: 1.2, 0.3, 5.0)
#veri tipini anlamak için print(type(2.0)) çıkan <class 'float'>
print(2+10*10+2)
#işlem önceliği
print((2+10)*10+2)


number = 6.70  #float sayısını yuvarlar
print(round(number)) #number, 1 ya da 2 dersek virgül sonrasını alır

print(pow(3,2)) #3ün 2.kuvvetini getirir
print(max(4, 3, 5, 11)) #min yaparsak en küçük değer

number = 4
number += 2 #çarpı ya da eksi de olabilir
print(number)

num1 = '23'
num2 = '34'  #str toplanmaz, yanyana dizilir ama integera çevir
num1 = int(num1)
num2 = int(num2)
print(num1 + num2 * 3) 


x = 3
num = 17
print(num % x)

numbers[::-1] - #listeyi ters dizer

-----------
#matematiksel operatörler
# ** - üs 
# % - mod
# // - tam bölme

4-0.5
0.5*2
2**3
3**0.5
10%2    #10nun 2ye bölümünden kalan 0
10/3    #3.333333 
#eğer 10//3 dersek ondalıklı kısmı atar tan kısmı yani 3ü gösteir
-15//4

--------
#useful functions
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))
