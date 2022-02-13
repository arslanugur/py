class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print("Hello, my name is " + self.name + ",")
    #def aged(self):
        print("I am "  + str(self.age) +  " years old \n" )        
        
class Teacher(Student):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def course(self):
        print("I will be your " + self.subject + " teacher!\n")
             
Kenpachi = Teacher('Dr. Kenpachi Zaraki', 59, 'Data Science')        
Ichigo = Student('Ichigo', 30)
Rukia = Student('Rukia', 35)
Orihime = Student('Orihime', 28 )

Rukia.say_hello()
#Rukia.aged()
Ichigo.say_hello()
#Ichigo.aged()
Orihime.say_hello()
#Orihime.aged()
Kenpachi.say_hello()
Kenpachi.course()

#print(Rukia.name)
#print(Rukia.aged)
#print(Orihime.aged)
#print(Orihime.name)

#print(Kenpachi.age)
print(help(Teacher ))


