# Bankamatik uygulaması

#ilkin bi veri yapısı oluşturcaz
accA = {
    'name' : 'Jason Bourne',
    'accNo' : '123456789',
    'balance' : 3000,
    'additionalAcc' : 2000
}
#yukarıdaki birinci kişinin olsun
accB = {
    'name' : 'James Bond',
    'accNo' : '133456789',
    'balance' : 4000, #bakiye
    'additionalAcc' : 1000
}

# hesap bilgi objelerini parametre olarak alıp
# bu veri yapıları üzerinden para çekme işlemleri yapcaz

def drawMoney(acc, amount): #acc ile hangi hesaptan, amount ile ne kadar çekmek istiyoruz
    print(f"Hi, {acc['name']}") # parayı usera vermeden önce bi f str oluşturalım
    # acc üzerinden ad bilgisine ulaşalım
    # çift tırnak ve tek tırnağa dikkat
    #bu aşamadan sonra para çekme işlemine geçelim
    if (acc['balance'] >= amount): #eğer hesap bilgisi olarak bakiye miktardan büyükse user ek hesaba ihtiyaç duymadan
        acc['balance'] -= amount #hesap bakiyesi güncelleme, eksi miktarı bakiye içinden çıkarabilir
        print('You can withdraw your money.')
        askBalance(acc) #her para çekiminde de yapılabilir
    else: #money would be not enough
        total = acc['balance'] + acc['additionalAcc'] #ek hesap artı bakiyede ne kadar var iilk bunu hesapla
    #hesap üzerinden bakiye + tekrar hesap üzerinden ek hesap bilgilerini alıp totali öğrenelim
        #ek hesapta güncellenmesi gerekli
        if (total >= amount):
        #eğer ikisinin totali çekmek istenilen miktaardan büyükse ya da eşitse eh çekebilir
        #ek hesabı kullanmak istiyormusun diye değişken tanımlayıp sormalıyız
            additionalAccUsage = input('Dyou wanna use the other acc? (y/n): ')
            if additionalAccUsage == 'y' : #eğer bize e değerini döndürüyorsa 
                #balance = acc['balance'] #bakiyemiz ne ilk önce ve nerde saklı ama bunun için değişken atamaya gerek yok
                additionalAccUsageAmount = amount - acc['balance'] #ek hesaptan ne kadar çekilecek
                acc['balance'] = 0 #ilk hesaptaki bakiye sıfırlanır
                acc['additionalAcc'] -= additionalAccUsageAmount #ek hesaptan düşülecek para
                #bakiye düşme işlemini ek hesap kullanıldığında da yapmak gerekli
                print('you can withdraw your money')
                askBalance(acc) #bakiye sorgulama
            else: #eğer ek hesabı kullanmak istemzse "n"
                print(f"{acc['accNo']} account number has {acc['balance']}$")
                #en azından userın hesabındaki ne kadar var bunu yazdır, ek hesabı kullanmak istemiyor çnkü
        else: #ek hesap dahil user parası yine yetmiyorsa bu durumda
            print('Balance is not enough!')
            askBalance(acc)
def askBalance(acc): #bi funk daha tanımlarsak 'bakiye sorgulama
# dışarıdan bi hesap parametresi alır
# sorgulamayı fonk dişında yaptık tabi her para çekme sonunda da çağırabilirz

    print(f"{acc['accNo']} account number has {acc['balance']} $, and your additional acc limit is {acc['additionalAcc']} $ ")
drawMoney(accA, 3000) #hangi hesap ve ne kadari fonksiyonu çalıştırark yaparız
#drawMoney(accA, 3000) #bakiye güncellemesinin sonunda aynı işlemi tekrar yapamazsın
#askBalance(accA) # 3000 çektikten sonra bakiye ögren diyelim
#üstte yazdığımız için burda bakiye sorg çağırmamıza gerek yok
print('****************************')
drawMoney(accA, 2000)
#askBalance(accA) # yukarıda yazdık tekrar çağırmaya gerek yok #2k çekelim tekrar sorgulayalım 
#dikkat etmemiz gereken objeler ram de referans tipinde ele alınıyor 
# ve bunları bi metoda/fonk gönderdiğim zaman accA bilgisinin adresi gönderiliyor
# opsiyon içeriside bi güncelleme yapıldığı zaman örneğin bakiye ya da ekk hesap bilgisini
# dışardaki objelerde de bu güncelleme yapılıyor
# yani adresteki aynı veriyi güncellemiş oluyoruz
# ama yukarıdaki gibi veri yapısı kullanmaktansa
# örneğin ad, bakiye, ek hesap bilgisini ayı ayrı değişkenlere tanımlayıp
# ,fonka gönderip güncelleme yapsak orjinal bilgi üzerinde güncelleme yapılamaz 
# çünkü gönderdiğin her bir parametre bi obje değil, sadece değişken yapısıysa
# bu durumda fonk içinde bi kopyalama işlemi yapılır zahmetli ve işe yaramaz 
# bu yüzden ref türünde bi yapı kullanmak şart
# aynı adresi temsill ettiğinden dolayı yani accA, fonk içindeki her bi güncellemeden etkilenecek, yani objeleri de kapsayacak


#tabi extra fonk eklenip farklı farklı görevler verilebilir
#eg para yatır fonksiyonu, extra ek hesap kimiti de tanımlanabilir
#sonuçta limit ayrı ve o anda bulunan para bilgisi limiti ayrı şeyler
#para yatırdığında ek hesapdaki limiti tamamlamak ve ana hesaba kalan parayı yatırmak bi nevi credit card olayı
#ek hesaptan ya da ana hesaptan para çekme yatırma tarihleri kayıt edilebliilr
#ek hesaba faiz bilgisi hesabı da yapılabiliri
#fonk ekledikçe demo genişleyip zengileşebilir
