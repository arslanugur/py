#identity ve membership operatörleri

#IDENTITY = is
"""
x = y = [1, 2, 3] #aynı adresde tanımlı liste, sadece referanslar farklı
z = [1, 2, 3] 
print(x==y) #true çünkü eşitlik operatöründeki değerlere bakılır
print(x==z) #yine true oolur, sadece referanslar ayrı değer aynı
#ama derğer değil de referans türünde bi adres karşılatırması yaparsak 
print(x is y) #true çünkü adres aynı
print(x is z) #false olur - farklı referanslara sahip
#bu konuyu valu ve referans tiplerinde detaylıca gördük
"""
"""
#diğer örnek
x = [1, 2, 3]
y = [2, 4]
###print(x is y) #farklı objeler ve farklı adreslerdeler
#içine attığınız bilgiler önemsiz, y tamamen xe benzesen bile olmaz
del x[2]
y[1] = 1 #birinci indexe 1 sayısını atsak
y.reverse() #tamamen ters çevirsek
#hem eşittir hem de is operatörüyle karşılaştıma yaptığında
print(x == y) #aynı elemanlara sahip x ve ynin #elemanları eşittir true
print(x is y)    #x ve y aynı referansa eşit değil (bellekte ayrı adresteler)
print(x is not y) #bu da olabilir true olur o zman
"""

"""
#MEMBERSHIP = in
x = ['apple', 'banana']
print('banana' in x) #aradığımız bi elemanın olup olmadığıını soruyoruz

name = 'arslan' #dizi bilgi tanımla
print('a' in name) #a karakteri name içinde var mı. TRUE
#aynı soru print('a' not in name) şeklinde de sorulabilir FALSE
"""
