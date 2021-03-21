#class içinde nasıl metod tanımlarız?
"""
# Class Attributes
class Person:
    address = 'no info' 

# Object Attributes
    #constructor method
    def __init__(self, name, year): #const örnek init methodu
        self.name = name
        self.year = year

    # INSTANCE METHOD - Objelere hizmet eder, bu yüzden self referansı
    def intro(self): 
        print('Hi There. I am ' + self.name)    #metodun yaptığı işlem bu
        #jack yazdı ama başka bi obje üzerinden çağırırsak p2.intro()
    # INSTANCE METHOD
    def calculateAge(self): #ikinci obje metodu
        return 2019 - self.year #printlemek yerine return et

#Object (Instance)
p1 = Person(name ='Jack', year = 1990) 
p2 = Person(name = 'John', year = 2000) 

p1.intro() #p1 objesi üzerinden intro metodunu çağır
p2.intro()

print(f'{p1.name} age: {p1.calculateAge()}') #calculateAge metodunu çağır
print(f'{p2.name} age: {p2.calculateAge()}')

"""

#New Class

class Circle:
    pi = 3.14 #circle classında bi pi değeri tanımlayıp bunu 3.14 eşitle 
    # bu işlem class seviyesinde class object attribute olrak tanımlanır

    def __init__(self, semiDiameter = 1): #init metodu tanımlayıp self parametresi alsın ve yarıçap bilgisi alsın
#yarı çap bilgisinin değeri belirtilmemişse buna 1 değerini ata
        self.semiDiameter = semiDiameter #self.semiDiameter'e dışardan gönderdiğimiz yarı çap bilgisini atayacağız

    #METHODs
    def calculatePerimeter(self): #çevre hesaplaması için self parametresi alıp class içindeki bilgilere ulaşcak
        return 2 * self.pi * self.semiDiameter #hesaplama işlemini return ile geriye gönder
    #bi de alan hesaplayan method
    def calculateArea(self):
        return self.pi * (self.semiDiameter **  2) #**2 üsünü almak

c1 = Circle() #bi yarıçap bilgisi belirtilebilir yoksa 1e eşitlenir
c2 = Circle(5) # yarı çap = 5 bilgisini atadık

#print ile c1 bölgesinin alan bilgisi
print(f'c1: Area = {c1.calculateArea()}, Perimeter = {c1.calculatePerimeter()}') 
print(f'c2: Area = {c2.calculateArea()}, Perimeter = {c2.calculatePerimeter()}')
#böylece tanımladığımız her bir dairenin alanını ve çevresini hesaplarız
#pi, classta nımlandı çünkü her bir obje için ortak değer olduğu için
# yoksa constr yani init metoduna tek tek bu bilgiyi aktarmak zorunda olurduk

