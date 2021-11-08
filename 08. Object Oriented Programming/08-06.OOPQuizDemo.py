#QUESTION CLASS

class Question():
    def __init__(self, text, choices, answer): 
    #dışarıdan bi self parametresi ve sorunun text kısmı içerik
    #yani text ismindeki değişkene göndercez, ve şık bilgilerini de burda vercez choices
    #sonrasında cevapları answer bilgisiyle göstercez
    #quest class içinde self.text isminde bi alan 
    # ve dışardan aldığımız soru bilgisini göndercez
        self.text = text
        self.choices = choices #bi dizi olcak, dışardan aldığımız dizi bilgilerini göndercez
        self.answer = answer

    #objeye hizmet edecek bi metod tanımlayalım
    def checkAnswer(self, answer): #self parametresini alıp kullanıcının verdiği cevabı alcak
        return self.answer == answer   
        #bu cvba göre return ederek 
        # self.answer yani tanımlamış oldmuz 
        # herhangi bir question objesinin 1 2 3 içerisindeki 
        # answer değeri ile dışardan gönderdiğımız answer değeri 
        # eğer birbirine eşitse dışarıya true değeeri göndercek
        # yani user doğru cevap vermiş olacak

"""sorular aşağıya alındı...
#bu bizim ne işimize yarayacak
q1 = Question('The best programming language?', ['C#', 'Java', 'Javascript', 'Python'], 'Python') #q1 adında bi obje ve quest tipinde ve dışardan bi bilgigöndercez
#verecek oldumuz cevapları da bi dizi şeklinde gönderebiliriz []
#ve bu altern içinden üçüncü parametrede olan insist parametresinde bi bilgi göndercek
#yani doğru kabul ettiğimiz python bunu da üçüncü kısma yazıyoruz
#bu şekilde bi obje tanımladık bunu artırabiliriz
q2 = Question('The most popular programming language?', ['C#', 'Java', 'Javascript', 'Python'], 'Python')
q3 = Question('The most earning programming language?', ['Javascript', 'Java', 'C#' , 'Python'], 'Python')
#şıklar farklı yerlerde olsun diye yerlerini değiştirebiliriz
#her soru kendi içinde gönderirdiğimiz parametreye göre bi cevap söylesin def checkAnswer metodu

QList = [q1, q2, q3]

print(q1.checkAnswer('Python'))
#q1 objesi için check answera Py diye cevap verelim bize true değerini gösterir
print(q2.checkAnswer('Java')) #dışardan verilecek cevap java false
print(q3.checkAnswer('Javascript')) #false
#if else kullanmadan nesne tabanlı mantığına uygun şekilde uygulamanın ilk aşaması yapıldı

#ikinci aşamadan quiz classı oluşturulacak, böylece daha da sistemli olacak
# yani ne kadar az if else bloklarını kullanırsan o kadar kaliteli kod yazıyorsun denilebilir
# if else her yerde yazılmaz çünkü karmaşıklığa götürüyor
"""

#QUIZ CLASS

#dışarıdan questions yani soruları alcak sorulara göre sırayla usera göstercek
#sorulara cevap ve bununla birlikte bi score bilgisi tutcaz
#beş sorunun üçünü bildin gibisinden cevap verz

class Quiz():
    def __init__(self, questions): #dışarıdan ald paramlar ise questions olacak
    #questions bi liste olarak tanımlanacak yani yukardaki sorular 123
    # bu yukarıdaki liste de dışardan quiz classına gönderilecek
    #gönderdiğimiz soruları bize sırayla gönderecek
        self.questions = questions #init içine gelip dışardan alınan questions eşitle
        self.score = 0 #.score diye bi alan tanımlayıp başlangıçta buna sıfır değerini ata
        self.questionIndex = 0 #diyelim ki ..indexi göndermiş olduğumuz liste içerisinden hangi soruyu almak istiyorsak onu kullanacaz
        #indexin 0 olması demek, quiz classına gönderdiğimiz listenin ilk elemanını bize getircek demek
        #indexi 1den başlatırsan 2 numaralı soruyu getirir 1 nolu soru değil
        #tabi bu index nosunu 0 değil random olarak da yapabiliriz
        #yukarıda tanımlanan soruları aşağıya aldık

    def getQuestion(self): #bu metodun görevi bize bi tane question objesi göndermek
        return self.questions[self.questionIndex] #aşağıda tanımlamıştık daha önce
#ama aşağıdaki gibi şu an quiz classını bilmiyoruz bu durumda yapacağımız daha sonra tanımlanacak olan selfi oun yerine yazmak
# şu andaki self bizim için daha sonradan tanımlanan quize karşılık gelcek
# aşağıda tanımlanan bu quiz = Quiz(questions)
 #selfin yani quiz clasının içindeki questionslardan selfin içindeki questionindexini alcaz

    def displayQuestion(self):
        question = self.getQuestion() #dışarıda yapılan işlemi class içinde yaparak ilgili questionı alalım
        print(f'Question {self.questionIndex + 1}: {question.text}')
        #soru 1 olur ve aldığımız questionın texini yazdırırsak  -----quiz.display.... aşağıdaki print ederiz  

        #bu metod ile aldığımız question yukarıda tanımlamış old Question classının bi örneği
        # ve o class da choice isminde bi alan vardı
        #choices aslında bi liste ve her bi elemanı tek tek ekrana yazdırmamız gerekli
        #listenin her bi elemanına ulaşmamız gerekiyor
        for q in question.choices: #aldığımız question objesne choices alanlarına gidip print diyelim
            print('-' + q) #bu usera altern sunar user bunları cevap olrak yazması gerekli

        #şıklardan sonra userdan bi bilgi alalım şimdi
        answer = input('answer: ')     
        #answer değişkeni tanımla userın girdiği değer aokunup answer değişkeni içine alıncak
        # print(question.checkAnswer(answer)) #aldığımız answer  bilgisii de checkanswer metoduna göndercez
#gönderdiğimiz değere göre print ile yazdıralım
#cevabına göre true false gelecek. kontrol başarılı
#bunun sonrasında index numarasını artırmamız gerekiyor ki her zman 1. soru yani 0. index gelmesin
#yani burdaki cevap sonrası index 1 olsun 2 olsun böyle devam etsin
#indexi bir artırmamız gerekli
#bunların hepsi display question metoduyla yapma o görevini tamamlamdı
#o anki question neyse onu cevap layıp bitior aktif indexe bağlı çalışyor
#90.satırı yazmak yerine tahmin isminde bi metod tanımlanır
        self.guess(answer) #kullanıcının verdiği cevabı bu şekilde göndercez
        self.loadQuestion() #loadquesti burda çağıralım display question yerine
   
    def guess(self, answer): #gönderdiğimiz cevap bilgisini alacak parametreyle birlikte
        #tabi yine questionı alacak question = self.getQuestion()
        question = self.getQuestion() #tekrar istendiğinde tekrar gelecek şuanki aktif olan index 0.index
        if question.checkAnswer(answer):
        #aldığımız question üzerinden check answer kontrol edip 
        # gönderdiğimiz text bilgisiyle bu kontrolü yapalım
        #user verdiği bilgiye göre bi kontrol yapcak
        #burdan dönen değer true ise user dopru bilmiş
        #sonuç olarak quiz classı içindeki score bilgisini bi artırmak
        # ve true ya da false yaptığına bakmadan question indexini bir artırmak
        #böylece bir sonraki soruya geçeriz
            self.score += 1 #score bir arttı
            #bunu if içinde yapmamız gerekli ki
            #eğer yanlış cevap geliyorsa skor bilgisini aartırmayız
            #çünkü burda bildiği soru adetini toplamı oluyoruz
        self.questionIndex += 1 #true ya da false önmsiz burda önemli olan bir artırmak
        #çünkü bir sonraki soruya geçmek istiyoruz
        #sonuçta index nosunu artırdığımız için display.. metodu burda bize farklı indexdeki bi soruyu gönderecek
        #display altındaki question bi sonraki soru olcak
        ## self.displayQuestion() #burda displayi çağırıcaz
        #soruları çözdükten sonra index hatası alırız yani dizinin sınırlarını aştk
        #çünkü sadece üç elemanlı ve her seferinde 1 artırdık
        #sona geldiğimizde getQuestion bize hata döndürür
        # dolasıyla indexin bi kontrolünü yapıyor olmak gerekli
        #yani displayQuestion burda çağırılmaz başka bi metod ile çağırılır
     
    def loadQuestion(self): #bu metod index kontrolü yapcak
    #bu metod bize soru yükleyecek
    #index ve soru sayılarına göre işlem yapcaz
        if len(self.questions) == self.questionIndex:
        #self demek ilgili obje
        #yani ilgili obje içerisinden questions kaç adet soru old vercek
        #üç srumuz var yani question indexine eşitse
        # sonuçta 3 bilgisini question içinden alamıyor bu yüzden index range sınır aşımı hatası verdi
        # yani 3e geldiği anda bizim için quiz bitmiştir diyebilirzi
            self.showScore()  #user için score bilgisini gösteriirz
        else: #eğe biz indexi aşmamışsak
            self.displayProgress() #ilerlemeleri göstercek ayrı bi method açalım 
            #yukarıdaki displayquestionı buraya yazabilirzi
            self.displayQuestion()
#loadqoes eğer indexi aşmışsa bize score bilgisini göndercek
#eğer aşmamışsak bize soru göstercek display ile
#bu şekidlde sanki döngü içine girmiş olcaz
#burda bu yüzden for döngüsü kullanmadık

#user kaç tane soru var bilmei ister sonuçta
#mesela 10 tae sorunun 3.sünde gibi   self.displayProgress ile yapabiliriz


#bu şekilde hata vermalindeki eden, bize pass hshow score gösterdi
#şimdi show scoreu pass olmadan ayarlayalım

    #score bilgisi içinde ayrıca bi metod
    def showScore(self):
        #pass #şimdilik boş kalsın
        print('Score: ', self.score)
#tabi bunu daha da fazla süsleyebiliriz

    def displayProgress(self):
        #bazı parametrelere ihtiyacmız var
        #örenğin ktoplam soru
        totalQuestion = len(self.questions) #uestions listesini sayaak bu toplamı alabiliriz
        questionNumber = self.questionIndex + 1 #kaçıncı soruda oldumuzu
#yani ilk/sıfırıncı indexdeysek kullanıcıya 1.soruda oduunu göstercek
        if questionNumber > totalQuestion:
            print('Quiz is over.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100, '*')) #o anda kaçıncı soruda bunu söylemek gerek 
#bunu da 100 karakterlik bi bilgi içine alursak


q1 = Question('The best programming language?', ['C#', 'Java', 'Javascript', 'Python'], 'Python')
q2 = Question('The most popular programming language?', ['C#', 'Java', 'Javascript', 'Python'], 'Python')
q3 = Question('The most earning programming language?', ['Javascript', 'Java', 'C#' , 'Python'], 'Python')

questions = [q1, q2, q3]  #sorular liste şeklinde elimizde
#questions bilgilerini biz bi liste şeklinde hazırladık
#tabi bunlar q4, q5 olarak da devam edebilir
#bu hazırladığımız listeyi DATABASE ile de alabiliriz
#databaseden gelen bilgileri Question objesinin içine doldurup
#bu şekilde quiz classına gönderip loadquestionı çalıştırabiliriz



quiz = Quiz(questions) #bi quiz objesi tanımlayıp dışardan questions alacak
#quiz artık questionslarla çalışır halde
#qquiz üzerinden herhangi bi question almak istersek
#question = quiz.questions[quiz.questionIndex] #bi question objesi tanımlayalıp bi objesyi qquiz üzerinden alacağız questions ile bütün sorular gelcek
# quiz ierisindeki questionindexine göre bi bilgi alcaz
#ve alınan bilgi ekranda print
#bunun yerine değiştirdğimizi kullanalım
# question = quiz.getQuestion() #böylece bize ilk soru gelir
# print(question.text) #bize ram adresi gönderiyor ama .text dersek içine ullaşırız
#eğer indexi 0 değil de 1 de başlatsak ikinci soru karşımız gelir

#tek tek bu işlemi indexle yapmak yerine Quiz içinde bunu bi method olarak yapmak gerek def getQuest...

#question = quiz.getQuestion()   ---- print(question.text)
# üstekilerin yerine, quiz üzerinden bi soru aldığımızda 
# bize bunu yazdıracak olan bi method yazdıırsak bu işimizi daha da kolayşatırır. 
# def display..

## quiz.displayQuestion() #böylece işler daha basitleşiyor
#şimdi yuardaki methodun altına cevpları yazdıralım
#artık bunu da kullanmayız load.quest deriz
quiz.loadQuestion()
#bunu çağırdığımızda index noyu kontrol edecek
#kaçıncı soruda old gösterecek sonrası displayi burda çağırcaz
#displayde bize ilgili soru bilgilerini getrck

