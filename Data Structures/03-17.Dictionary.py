#dictionary bir liste türüdür
#key - value  -  bi bilgiye ulaşmak için key bilgisini kullanıyoruz

# 41 => kocaeli     temsil ediyor
# 34 => istanbul

#peki dictionary olmadan liste olarak bu nasıl yapılır
cities = ['kocaeli', 'istanbul']
plaques = [41, 34]

print(plaques[cities.index('istanbul')]) #unutma sıraların birbirine uyması gerekir

#ama iki liste yerine tek bi listeyle
# print(plaques['istanbul'])  => 34 vermeli
# yani key bilgisiyle value bilgisine ulaşmak amaç

#plaques tekrar tanımlanır ama köşeli değil süslü olarak 
#plaques = { 'key' : 'value' } #keye karşılık bi value bilgisi yazdırcaz
plaques = { 'kocaeli' : 41, 'istanbul' : 34 }
print(plaques['istanbul'])

plaques['ankara'] = 6 #yeni  value eklersek
plaques['kocaeli'] = 'new value' #yeni value atadık
print(plaques)

#yeni örnek
users = {'arslanugur': {
          'age': 28,
          'roles':['user'], 
          'email': 'a@gmail.com',
          'address' : 'Aksaray',
          'phone' : '507'
          },
         'ugurarslan' : {
          'age': 30,
          'roles':['admin', 'user' ] #web sitesinde rolleri belirtme
          },
         'au' : 26,
         'ua' : 50}    #aynı şekilde süslü parantezle diğer valueler de verilir

print(users['arslanugur'])
print(users['arslanugur']['phone'])
print(users['ugurarslan']['roles'][0])

#genel olarak yaptığımız şey, saladığımız bilgilere verdiğimiz isim

