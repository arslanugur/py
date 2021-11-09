#for ve while ile kallanabileceğimiz break ve continue
"""1
name = 'Arslan Uğur'

for letter in name: #tek tek harflerine ulaşıyoruz 
    if letter == 'n': #n'ye gldiği zaman döngü durur 
        break #döngüyü durdur
    print(letter) #her bir harf ekrana yazdır ama if ve break kullanılırsa..

for letter in name:
    if letter == 'ğ':
        continue    #ğ gelince döngü turunu iptal eder devam etti işlem için durmadı bu yüzden ğ hariç tüm harfler yazılır
    print(letter)
"""

"""2
x = 0
while x < 5:
    if x == 2: #x eşitse 2ye bu durumda döngüden çık
        break 
    print(x)
    x += 1 #yazdırma işlemi sonrası xi 1 artır aksi durumda sonsuzbi döngüye gider
"""

"""3
x = 0
while x < 5:
    x += 1 #buraya yazdık çünkü x 2de hep takılı kalıp başa dönüp tekrar 2de takılı olcaktı
    if x == 2:
        continue 
    print(x)
"""


#1den 100e kadar tek sayıların toplamı
"""4
x = 1
result = 0 #toplam olarak result tanımlanır ve 0a eşitlenir
while x <=100:
    result += x #gelen her bi x elemanınını += operatörüyle result değişkenine atalım
    x += 1 #xi de artırmamız gerekli
print(f'Total: {result}')
"""

"""5
x = 0 #x 0dan başlasın
result = 0 #toplam olarak result tanımlanır ve 0a eşitlenir
while x <=100:
    x += 1 
    if x % 2 == 1: #eğer gelen x'in mod 2sini aldığımızda sonuç bire eşitse 
        continue #bu durumda continue ile o anki turu erteleyelim    
    result += x
print(f'Total: {result}')
#yani sadece çift sayıların toplamını aldık
# == 0 deseydik tekleri alırdık
"""
