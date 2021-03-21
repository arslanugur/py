x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6


# kullanıcıdan aldığınız iki sayının çarpımı ile x, y, z toplamının farkı?
"""
a = int(input('1st number: ')) #mat işlemi yapacağımız için bunu integera çevir
b = int(input('2nd number: '))
result = (a*b) - (x+y+z) #result isminde bi değişikene atıp print
print(result)

"""

# y'nin x'e kalansız bölümünü hesapla 
result = y // x #kalansız tam bölme işareti
print(result)

# (x, y, z) toplamının mod 3'ü ne
total = (x+ y+ z)
result = total % 3
print(result)

# y'nin x'inci kuvvetini hesapla
result = y ** x
print(result)

# x, *y, z = numbers işlemine göre z değerinin küpü kaç
numbers = 1, 5, 7, 10, 6   #xyz numbers içindeki değerlere ata
x , *y , z = numbers #beş elemanı üç değişkene atamak için yıldız
print(y)
result = z ** 3   #znin küpü
print(result)


# x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaç
numbers = 1, 5, 7, 10, 6 
x , *y , z = numbers
result = y[0] + y[1] + y[2]
print(result)
