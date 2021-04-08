#dictionary - bir liste türü
#key - value  -  bi bilgiye ulaşmak için key bilgisini kullanıyoruz

# 41 => kocaeli    34 => istanbul        temsil ediyor


#peki dictionary olmadan liste olarak bu nasıl yapılır
cities = ['kocaeli', 'istanbul']
plaques = [41, 34]

print(plaques[cities.index('istanbul')]) #unutma sıraların birbirine uyması gerekir

#ama iki liste yerine tek bi listeyle
# print(plaques['istanbul'])  => 34 vermeli
#yani amaç, key bilgisiyle value bilgisine ulaşmak

#DICT ile nasıl yapılır
#plaques = { 'key' : 'value' } #keye karşılık bi value bilgisi yazdırcaz
plaques = { 'kocaeli' : 41, 'istanbul' : 34 } #plaques tekrar tanımlanır ama köşeli değil süslü olarak 
print(plaques['istanbul'])

plaques['ankara'] = 6 #yeni  value eklersek
plaques['kocaeli'] = 'new value' #yeni value atadık
print(plaques)


######
#yeni örnek
users = {'Shakespeare': {
          'age': 30,
          'roles':['user'], 
          'email': 'shakespeare@gmail.com',
          'address' : 'Manchester',
          'phone' : '507'
          },
         'Joyce' : {
          'age': 31,
          'roles':['admin', 'user' ] #web sitesinde rolleri belirtme
          },
         'au' : 26,
         'ua' : 50}    #aynı şekilde süslü parantezle diğer valueler de verilir

print(users['Shakespeare'])
print(users['Shakespeare']['phone'])
print(users['Joyce']['roles'][0])

#genel olarak yaptığımız şey, salladığımız bilgilere verdiğimiz isim

