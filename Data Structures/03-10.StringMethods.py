message = "Hello there. I'm Jane Austen."

message = message.upper()      #bütün karakterleri büyültür
message = message.lower()      #bütün karakterleri küçültür
message = message.title()      #her kelimenin baş barfleri büyür
message = message.capitalize() #sadece ilk harf büyük olur
message = message.strip()      #stringi kontrol eder, uygunsuz boşluk var mı yok mu!

message = message.split()      #string metin bölününür ve terminale karakter dizisi olarak yansır
message = message.split('.')   #boşluktan değil ama noktalardan itibaren ayırır
message = ' '.join(message)    #parantez içinde olanı birleştirir tekrardan. Boşluk yerine * da olur

index = message.find('Austen') #cümle içerindeki kelimeyi index nosu ile bulma
print(index)                   #index numarası 17 = A
#eğer negatif -1 gibi bi sonuç çıkarsa kelime cümle içinde yok

isFound = message.startswith('H') #sonuç true/false. Bu da mesajın H ile başladığını söyler
isFound = message.endswith('H')   #sonuç false çıkar çünkü H ile bitmedi
print(isFound)


message = message.replace('Jane', 'John')  #yer değiştirme
message = message.replace(' ', '*')        #boşluk karakterleri yerine yıldız ekle
message = message.replace('ç', 'c')
                 .replace('ş','s')
                 .replace('ö','o')
    
message = message.center(100)      #Burda container oluşturur. 100 kaakterin içine mesajı tam ortalar
message = message.center(50, '*')  #Boşluk yerine yıldız koyar
print(message)

#print(message[2]) split yaptığımızda dizileri elde ederiz bu da numaaralı olur 
#her bir numara dizideki kelimeyi bulirtir.mesela 2 gibi ya da 0 gibi


