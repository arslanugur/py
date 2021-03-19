#03-03. değişken (variables) tanımlama

#iki brüt maaştan vergi çıkarmak
salaryA = 5000
salaryB = 4000
tax = 0.27  #maaşın yüzde 27 vergi oranını hesaplama

print(5000 - (5000 * 0.27)) #bunu yazmak sıkıntı bu yüzden bellekte değişken tanımlama
print(salaryA - (salaryA * tax))
 
print(4000 - (4000 * 0.27))
print(salaryB - (salaryB * tax))

# değişken tanımlama kuralları
#1 değişken bir ifade, rakam/sayısal bi ifadeyle başlayamaz ama sonuna eklenir 
num1 = 10 #değişkene değer atamak
print(num1)
num2 = 15
print(num2)

#2 değişken tanımlarken büyük küçük harf uyumsuzluğu var
num1 +=20
print(num1)

age = 30
AGE = 20

print(age)
print(AGE)

#3. değişkende boşluk olamaz ama alt çizgi

# Değişken tipleri
x = 1                   # int
y = 2.0                 # float
name = 'arslan'         # string
isStudent = True        # bool

a = 10      #int
b = 20
print(a + b) #30

#string birleştirme işlemi
a = "10"
b = "20"
print(a + b) #1020

FirstName = "Uğur"
LastName = " Arslan"
print(FirstName + LastName) #Uğur Arslan

#tek bi satırdan tüm değişkenlere atama yapmak içinse..
a, b, FirstName, isStudent = (1, 2.3, "Uğur", True)

