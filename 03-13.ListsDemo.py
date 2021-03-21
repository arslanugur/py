# 'BMW, Mercedes, Mustang, Mazda' elemanlarına sahip bir liste oluştur
cars = ['BMW','Mercedes','Mustang','Mazda']
# Liste kaç elemanlı?
result = len(cars)

# Listenin ilk ve son elemanı?
result = cars[0]
#result = cars[3]
result = cars[-1]
# Mazda değerini Toyota ile değiştir
cars[-1]= 'Toyota'
result = cars
# Mercedes listenin bir elemanı mı? #in operatörünü kullanmak
result = 'Mercedes' in cars
# Listenin -2 indeksindeki değer ne?
result = cars[-2]
# Listenin ilk 3 elemanını al
result = cars[0:3]
#ya da result = cars[:3] ya da result = cars[-2:]
# Listenin son 2 elemanı yerine 'Audi' ve 'Jeep' değerlerini ekle
cars[-2:] = ['Audi', 'Jeep']
result = cars
# Listenin üzerine 'Lamborghini' ve 'Nissan' değerlerini ekle, liste tanımlaması yap
result = cars + ['Lamborghini', 'Nissan']
# Listenin son elemanını sil
del cars[-1]
result = cars
# Liste elemanlarını tersten yazdır
result = cars[::-1]
# Aşağıdaki verileri bir liste içinde sakla
        # studentA: Yiğit Bilgi 2010, (70, 60, 70)
        # studentB: Sena Turan 1999, (80, 80, 70)
        # studentC: Ahmet Turan 1998, (80, 70, 90)
studentA = ['Yiğit', 'Bilgi', 2010,[70, 60, 70]]
studentB = ['Sena', 'Turan', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Turan', 1998, [80, 70, 90]]
        # liste elemanları kişi bilgilerini veriyor
# Liste elemanlarını ekrna yazdır
result = studentA[0]
result = studentB[1]
result = studentC[3] #listenin içinden başka bi listeye geçiş
result = studentC[3][1] #iç listden 1 nolu index 

# result = f'Yiğit Bilgin 9 yaşında ve not ortalaması 66'
result = f'{studentA[0]} {studentA[1]} {2020-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}'
print(result)