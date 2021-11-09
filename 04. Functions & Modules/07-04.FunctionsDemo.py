# Gönderilen bi kelimeyi belirtilen kez ekranda gösteren fonku yaz
# "parametre belirleyip bu pm kaç kez yazdırılacak"
"""
def yazdir(word, piece): #dışarıdan bi kelime ve adet isminde bi değişken alan yazdir adında fonk
    print(word * piece)#gönderilen kelimeyi print ile söylenen adet kadar çarpıp ekrana versin
#fonksiyon çağırılmaya hazır
yazdir('change\n', 5) # \n  new line yani alt alta yazılır
"""

# Kendine gönderilen sınırsız sayıdaki parametreyi bi listeye çeviren fonk hazırla
# "str ya da number türünde"
"""
def turnintolist(*args): #listeye çevir şeklinde fonk #*args ya da *params sınırsız sayıda bilgiyi almak için
    liste = [] # başlangıçta boş olan liste tanımlaması

#gönderilen bütün parametreleri dolaşmak için
    for param in params:
        liste.append(param) #paramdan her bi elemanı aldımız zaman da liste üzerine append edelim
    return liste #bitişte oluşturulan listeyi geriye çevirelim

result = turnintolist(10, 20, 30, 'loudproud', 4.00, 567) #bu ifade functan geriye dönceği içi result kullanmak daha iyi
# böylece result hazırlanan bi liste olacak ve print edilcek
print(result)
"""

# Gönderilen iki sayı arasındaki tüm asal sayıları bul
# "asal sayı hesaplamayı döngüler bölümünde gördük"
# "asal sayı, 1 ve kendisinden başka böleni olmayan sayılar"
"""
def findPrimeNumbers(number1, number2): #gönderilen iki sayı arasında
    for number in range(number1, number2 + 1): #ilk etapta döngü oluştur
#no1den başla no2ye kadar git. no2yi de işin içinde katmak için +1 de
        #aralıktaki tüm sayılara number değişkeni üzerinden ulaşma imkanımız olsun
        if number > 1: # 1 sayısı asal değil, bu yüzden işin içinden çıkar
           #yani 1den büyükse for döngüsüyle asal işleme tabi tut
            for i in range(2, number): #ikiden başla, o anda elde ettiğimiz sayıya kadar git
            #yani 2den ittiban sayıya kadar bi böleni var mı ona bakıyoruz
                if (number % i == 0):   #yani bi böleni varsa, asal değildir 
                    break #ile asal sayı olmadığı için döngüden çıkar
            else: #for döngüsünün else kısmında ise
                print(number) #asal sayıysa kendisini yazdıralım

number1 = int(input('number1: ')) # "aralık bul"
number2 = int(input('number2: '))  # bunlar yukarıdaydı neyse önemsiz

findPrimeNumbers(number1, number2)
#+1 dediğimiz için 17 desek ikinci sayıya onu da dahil eder
"""

# Kendisine gönderilen birsayının tam bölenlerini bi liste şeklinde döndür, geri gönderen func
# "yani 10 değerini funka gönderiyorsa 10 değerini tam bölünlerin listesi olarak funktan geri gönderilebilir"

def findFullDivisors(number):
    fullDivisors = [] #burda ilk başta boş olan bi tam bölenler listesitanımla

    for i in range(2, number): # 2den başlayıp aldığımız sayıya kadar gitcez
        if (number % i == 0): # bize gelen sayı eşit eşit sıfırsa
                             # demek ki bu sayının bi tam bölenini bulduk
            fullDivisors.append(i) 
            #tam bölenler listesinin üzerine append ile bulduğumuz i değerini ekleyebiliriz                

    return fullDivisors #tambölenler listesini geriye gönderelim

print(findFullDivisors(20)) #fonk kuulnırsak 20 sayısının tam bölenlerini getirecek
#bu input olarak nasıl yaparız öğren

#printsiz yazdırmaya kalkarsan terminal boşa atar

