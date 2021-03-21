#set listeleri
fruits = {'apple', 'orange', 'banana'} #tipik liste örneği
print(fruits)
#ama indexlenemez bi liste
# print(fruits[0]) yapamazsın
#aşağıdaki gibi elemanlarına döngü ile ulaşırız
for x in fruits: #her bi elemanı xin yerine sırayla koyalıyoruz
    print(x)  #sıra sıra çıkar ancak denildiği gibi bunlarda index no yok sıralanmıyor 

#yeni bi eleman ekleme ise
fruits.add('cherry') #birden fazla olursa aynı işlem tekrar
#update yöntemiyle listeye yeni bi liste gönderip ekleme yapılır
fruits.update(['mango', 'grape'])  
#update'e zaten var olan bi eleman eklemeye kalkarsan göstermez çünkü zaten var
#kümeler gibi
print(fruits)
#silme işlemini nasıl yaparız peki
fruits.remove('mango')
fruits.discard('orange') #bu da diğer silme yöntemi
print(fruits)
#eğer liste indexlenebiliyorsa pop meteduyla son elemanı siler 
# ama bu liste için olmaz çünkü sıralı liste değil ve son elemanın silineceğinin garantisi yok 
fruits.pop() #denendi ilk elemanı sildi
print(fruits)

fruits.clear() #tüm elemanlar silinir
print(fruits)  #set()

#yeni bi list tanılarsak
myList = [1,3,5,5,2,3,1]
print(myList) #hepsi yazılır
#bunu set constructer aracılığıyla myListe gönderirsek
print(set(myList)) #bir kere yazılacak her eleman




