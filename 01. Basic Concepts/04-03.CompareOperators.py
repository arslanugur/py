#comparison operators
# username, password  -> bunlar databasee gider
#kullanıcı tekrar geldiğinde bunu input ile alcağız
#'arslanugur' , '12345'
#bunlar için karşılaştırma operatörleri kullanılır

a, b, c, d = 5, 5, 10, 4

username = 'arslanugur'  #değerleri tanımla
password = '12345'

result = a == b #a b ye eşit mi diye soruyoruz, bunu da result içine saklarız
result = a != b #a b ye eşit değil mi operatörü, soru tersten
result = (a == c)  #koşulları artırırsak, parantez de konabilir
result = (a != b) #true der çünkü eşit değil
result = (a > c) 
result = (a >= c)
result = (True == 1) #evet eşit true numerik olarak 1
result = (False == 0) #true olcak
result = False+ True+33 #34 olur trunun değeri var
#a = b deydik b yi a ya eşitlerdik
#result true ya da false olacak
print(result)


result = 'arsnugr' == username     #--->  mantıksal operatörler konusu
#yani hem username sorusu hem de passord sorusu soruyoruz 
#iki soru var iki cevap isteniyor
print(result)
