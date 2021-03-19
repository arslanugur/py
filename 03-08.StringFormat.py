#string formatlama
name = "Uğur" #yine değişken tanımlama
surname = "Arslan"
age = 30

# print("My Name is {} {}".format(name, surname)) 
# nokta sonrası kullanılabilicek str metodları karşımıza gelir
#str metodlarından biri: format. format namei süslü parantezin yerine koyar
#ikinci argümana da surname yazılır. ikinci süslü parantz ile birlikte
# print("My Name is {0} {1}".format(name, surname)) 
#0 ve 1 Uğur Arslan 1 ve 0 Arslan Uğur
#index numaralarını kullanmak yerine bu sefer...
# print("My Name is {s} {n} and I'm {a} y/o.".format(n = name, s = surname, a = age)) 
#eğer yukarıdaki gibi age bilgisi tanımlamıyorsan "30" string'i yazar geçersin

print(f"My Name is {name} {surname} and I'm {age} y/o.") 
#f string metodu

# result = 200 / 700
# print("the result is {}".format(result))
#sonuç float olacağından bunu formatmak gerekli
# print("the result is {r:1.3}".format(r=result))
#ilk parametre olarak 1 bilgisi,2.parametre olarak 3 bilgisi verilir ve sayı yuvarlanır
#1 bilgisi ise o miktarsa karakterlik alan bırakır 3 bilgisi kaç basamak olacağını temsil
#1 bilgisi sayının kendisini yazdırır




str = '{c}, {b}, {a}'.format(a = 5, b = 9, c = 7)
print(str)


