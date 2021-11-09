#Asal sayı uygulaması
#1 Girilen bi sayının asal olup olmadığını bul
#** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılardır
#2 3 5 7 11  -- 1 sayısı asal değil - özel

number = int(input('Number: '))

isPrime = True #asal olan truedur varsayımsal olarak. hiç bi böleni olmazsa burda kalacak
#asal olmadığında ise 
if number == 1: #bu özel durum - gelen sayı 1 ise
    isPrime = False #print('Number 1 is not Prime')


#2den başlayarak girilen her bir sayıyı ele alıcak 
# yani her bi sayıyı. ve sayının tam böleni var mı bunu kontrol et
for i in range(2, number):
    if number % i == 0: #ise kalan yoksa asal değil. altına print yazıp iki durumu da kontrol etmek yerine
        isPrime = False #asal olmadığı durumda ise true değeri false oldu
        break #devam etmeye gerek yok
#girilen sayı mod i değer (çünkü range ile gelen değer zaten inch ile geliyor)
#ve aldığımız sayı da sayı içerisinde. aldığımız sayı gelen sayı

#eğer isPrime bize true değerini gönderiyorsa yani asal mı
if isPrime:
    print('Number is Prime')
else:
    print('Number in not Prime')




