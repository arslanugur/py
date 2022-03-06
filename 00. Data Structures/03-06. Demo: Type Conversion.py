"""
Dairenin Alanı: πr²
Dairenin çevresi: 2πr

r = yariCap
Yarı Çapı verilen bir dairenin alan çapı ve çevresini hesapla  (r: 3.14)
"""

pi = 3.14
r = float(input("yarı çap: "))

alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre))

print("alan: "+ str(alan) + " çevre: "+ str(cevre))    #bu durumda str bilgi verir 
#print("alan: "+ alan + "çevre: "+ çevre)  #böyle yazılmaz çünkü str bi bilgi gibi, kabul etmez 
# çünkü alan dediğimiz yer - float  # başına str ekle - float to str işlemi

print("alan:", alan)
print("cevre:", cevre)



