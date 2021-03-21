website = "http://www.englishteacherarslan.com"
course = "English Language Studies"

# "course" karakter dizisinde kaç karakter var?
result = len(course)
length = len(website) #2.yol

# website içinden www karakterlerini al
result = website[7:10] #7den başla 10da bitir
# website içinden com karakterlerini al
result = website[32:35]
result = website[length-3:length] #2.yol
# course içinden ilk 5 son 3 karakterleri al
result = course[0:22]
result = course[:22] #2.yol
result = course[-22:-1] #3.yol
result = course[-22:] #4.yol
# course ifadesi içndeki karakterleri tersten yazdır
result = course[::] #bütün elemanlar için :: eklenir
result = course[::2] #bi karakter alır bi karakter almaz, ::3 3de bir alır
result = course[::-1] #tersten tüm karakterleri alır

name, surname, age, job = "Uğur", "Arslan", 30, "English Teacher."

# Yukarıdaki değişkenlerle terminal'e aşağıdaki ifadeyi yazdır
# "My name is Uğur Arslan, I'm 30 y/o. I'm an English Teacher."

result = "My name is "+ name+ " " + surname+ ", I'm "+ str(age) + " y/o. I'm an "+ job
#2.yol
result = "My name is {} {}, I'm {} y/o. I'm an {}".format(name, surname, age, job)
#ya da süslü parantezleri numaralandır {0},{1}... gibi
#3.yol
result = f"My name is {name} {surname}, I'm {age} y/o. I'm an {job}"
# "Hello world" ifadesindeki w harfini "W" ile değiştir

x = "Hello world"
#result = x[6]
#result = x[0:6] + "WWW"+ x[-4:]
# print(x) ile gösterebiliriz
#2.yol 
x = x.replace("w","WWW") #bu da bir diğer metod
# "abc" ifadesini yanyana 3 kere yazdır
#x = "abc" *3
print(x)
#print(x[::3]) #sadece a değerini verir

print(result)
