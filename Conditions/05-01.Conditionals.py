# koşul ifadeleri
# koşullu durum blokları: if - else
#şu ana kadar bi kod bloğundan dier bloğa direk geçiş yaptın
#artık bi kod bloğundan diğerine koşullu geçiş yapacaksın: true, false
#yani uygulamanın gidişatını değiştirmek
#username yanlışsa usera username ya da parolan yanlış diye mesaj verebilirsin
#belli koşullarda belli kodbloklarını iletmek amacımız

"""
if 3>2:     
#koşuldan gelecek olan bi true false eğeri mutlaka olmalı
#print belli bi koşul durumunda kullanılıcak bunun için if
    print('welcome back') #3 2den büyük olduğu için bize 'welcome back yazar.
#if 3 > 3 olsaydı yazmazdı
#if 3 == 3 olsaydı 'welcome back'
#if True --> 'welcome back'
"""

"""
isLoggedIn = True #yani kullanıcı giriş yaptı mı
if isLoggedIn:
# ya da burda 'if isLoggedIn == True:' olarak da sorabiliriz
#yani true == true mu diyoruz , bu saçmalık sadece mantığı öğren ama
    print('ok')
#print için her zaman bi kere tablıyoruz!!!!!!!!!!!!!!!! yoksa kod çalışmaz  
"""

"""
#değişken tanımlamakla başlayalım
username = 'arslanugur'
password = '123abc'
isLoggedIn = (username == 'arslanugur') and (password == '123abc') 
#iki karşılaştırma yaptın - username arslanugura eşit mi bunu sorguladın
#iki soruda true olmalı ki and operatörü bize true değeri göndersin
#operatör kullanımıyla bool türüne değer üretiyoruz burda
if isLoggedIn:
    print('Welcome Home')
"""
"""
#diğer basit şekilde yazarsak
username = 'arslanugur'
password = '123abc'
if (username == 'arslanugur') and (password == '123abc'):
    print('thats it babe')
#bilgileriniz yanlış nasıl yazdırılır o da else ile
#yani ifin yanındaki ifadeler false olursa bu durumda else devreye girer
else:
    print('babe!, you dont remember your name and number or both?!')
"""

"""
#peki username mi yoksa parola mı yanlış bunu kullanıcı bilmek ister
username = 'arslanugur'
password = '123abc'
if (username == 'arslanugur'):
    if (password == '123abc'):
        print('thats it babe')
    else: #peki parola yanlışsa (çünkü if-else sadece parolayla ilgili)
        print('your passed wrong way')
else:
    print('Schoz!, you dont remember your name?!') #üsteki if ve onun else

#bu kadar uğraşamadan elif komutuyla yapmak yada yalın olcak
"""


temp = -5
freezing = 0
raining = False
snowing = True
if temp < freezing and (raining == True or snowing == True):
    print('Bad weather!')

temp = 10
if temp >= 10:
    print('Warm')
if temp >= 20:
    print('Hot')

#or kullanılablir input için
