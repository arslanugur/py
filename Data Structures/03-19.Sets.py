#set listeleri
fruits = {'apple', 'orange', 'banana'} #tipik liste örneği
print(fruits)

#print(fruits[0]) yapamazsın yani indexlenemez bi liste
#aşağıdaki gibi elemanlarına döngü ile ulaşırız

for x in fruits:    #her bi elemanı x'in yerine sırayla koyarız
    print(x)        #sıra sıra çıkar ancak denildiği gibi bunlarda index no yok sıralanmıyor 


fruits.add('cherry')                 #yeni bi eleman ekleme. Birden fazla olursa aynı işlem tekrar
fruits.update(['mango', 'grape'])    #update yöntemiyle listeye yeni bi liste gönderip ekleme yapılır
 
#update'e zaten var olan bi eleman eklemeye kalkarsan göstermez çünkü zaten var, kümeler işte
print(fruits)

fruits.remove('mango')      #silme işlemi
fruits.discard('orange')    #diğer silme yöntemi
print(fruits)

# eğer liste indexlenebiliyorsa pop meteduyla son elemanı siler 
# ama bu liste için olmaz çünkü sıralı liste değil ve son elemanın silineceğinin garantisi yok 
fruits.pop()       #denendi ilk elemanı sildi
print(fruits)

fruits.clear() #tüm elemanlar silinir
print(fruits)  #set()

############################

myList = [1,3,5,5,2,3,1]     #yeni bi list tanılarsak
print(myList)

#MyList, set constructer aracılığıyla myListe gönderirsek, her bir eleman bir kere yazılacak
print(set(myList)) 

