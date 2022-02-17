# SECTION 1
# Inheritance provides a way to share functionality between classes.
# Imagine several classes, Cat, Dog, Rabbit and so on. 
# Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name).
# This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
# To inherit a class from another class, put the superclass name in parentheses after the class name.
# Example: 
class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()


comments











#Nesne tabanlı prpgramlama  - Kalıtım
#Classların birbirinden miras almasıyla olan bi durum

#Person class; name, surname, age, eat() metodu, walk() metodu
#Student ya da Teacher classes; Person class görevlerini bunlara da olmasını isterim
#Student(Person) , Teacher(Person) tüm özellikler onlarda da var
#Person için tanımlanan bütün özeelikler attributes ve methods Student ve Teacher parçası olcak
#yani aynı özellikleri tekrar tekrar oluşturmaya gerek yok
#Student ya da Teacher classa öğrenci/öğretmen özellikleri de eklenebilcek
#Person sadece standard yani temel sınıf
#Animal() --- Dog(Animal), Cat(Animal), Horse(Animal)
"""
class Person():
    def __init__(self):
        print('Person Created')

class Student(Person):
    def __init__(self):
        Person.__init__(self)  #stu, person init metodunu bu şekilde alır
        print('Student Created')


#persondan türetilen bi p1 objesi tanımlarsak
#p1 = Person()
s1 = Student() #Person Created
#student objesini çağırmak personın init metodunu tekrar çağırmak demek
#Studenta bi init metodu eklersek
"""

#SECOND PART
class Person():
    def __init__(self, fname, lname):
        self.firstname = fname #bi alan türetip dışardan gönderdiğimiz firstname atamak istesin
        self.lastname = lname
        print('Person Created')

    def who(self):
        print('I am a person')

    def play(self):
        print('I am playing..')

class Student(Person):
    def __init__(self, fname, lname, snumber):
        Person.__init__(self, fname, lname) #person bigilerini alması gerekir temel sınıf çünkü
        self.studentNo = snumber
        print('Student Created')

    #OVERRIDE: aynı isimdeki obj att metodun temel sınıftaki class att metodu ezmesi
    def who(self):
        print('I am a student') #çünkü artık personın o özelliğine gerek yok

    def say(self):
        print('Highway to Hell')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)  # Person.__init__(self, fname, lname) aynısı ama daha kısası 
        self.branch = branch

    def who(self):
        print(f'I am a {self.branch}')

    def say(self):
        print('Johnny B. Goode')


p1 = Person('Guitar', 'Player')
s1 = Student('Angus', 'Young', 1)
t1 = Teacher('Chuck', 'Berry', 'GTeacher')
print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNo))
#str yerine f str de kullanabilirdik

p1.who()
s1.who() #stu üzerinden de aynı elemana ulaşabiliriz
t1.who()

p1.play()
s1.play()
s1.say()
t1.say()


