#string formatlama

name = 'Da'
surname = 'Vinci'
age = 30

# print('My name is {} {}'.format(name, surname)) #str metodlarından biri: format. format namei süslü parantezin yerine koyar
# print('My name is {1} {0}'.format(name, surname)) #0 ve 1 Da Vinci 1 ve 0 Vinci Da
# print('My name is {s} {n}'.format(n=name, s=surname)) #index numaralarını kullanmak yerine bu sefer...
#eğer yukarıdaki gibi age bilgisi tanımlamıyorsan "30 string'i yazar geçersin
# print("My name is {} {} and I'm {} years old.".format(name, surname, age))
# print("My name is {} {} and I'm {} years old.".format(name, name, name))

# result = 200 / 700
# print('the result is {r:1.4}'.format(r=result))

print(f"My name is {name} {surname} and I'm {age} y/o.") #fstring metodu


# result = 200 / 700
# print("the result is {}".format(result))
#sonuç float olacağından bunu formatmak gerekli
# print("the result is {r:1.3}".format(r=result))
#ilk parametre olarak 1 bilgisi,2.parametre olarak 3 bilgisi verilir ve sayı yuvarlanır
#1 bilgisi ise o miktarsa karakterlik alan bırakır 3 bilgisi kaç basamak olacağını temsil
#1 bilgisi sayının kendisini yazdırır

str = '{c}, {b}, {a}'.format(a = 5, b = 9, c = 7)
print(str)
