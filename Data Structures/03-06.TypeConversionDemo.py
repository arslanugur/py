"""
Dairenin Alanı: πr²
Dairenin çevresi: 2πr

r = yariCap
Yarı Çapı verilen bir dairenin alan çapı ve çevresini hesapla 
(r: 3.14)
"""

pi = 3.14
r = float(input("yarı çap: "))
alan = pi * (r ** 2)
cevre = 2 * pi * r 

"""
#bu durumda str bilgi verir 
# bu yüzden number türlerine (int ya da float) çevir 
# input başına float ile string floata çevrilir
"""
print("alan:", alan)
print("cevre:", cevre)


"""
print("alan: "+ alan + "çevre: "+ çevre)
#böyle yazılmaz çünkü str bi bilgi gibi, kabul etmez 
# çünkü alan dediğimiz yer - float 
# başına str ekle - float to str işlemi
print("alan: "+ str(alan) + "çevre: "+ str(çevre))
"""
