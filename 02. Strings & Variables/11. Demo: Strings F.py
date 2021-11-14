website = "http://www.englishteachershakespeare.com"
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
result = course[:22]    #2.yol
result = course[-22:-1] #3.yol
result = course[-22:]   #4.yol

# course ifadesi içndeki karakterleri tersten yazdır
result = course[::]    #bütün elemanlar için :: eklenir
result = course[::2]   #bir karakter alır bi karakter almaz. ::3 - 3de bir alır
result = course[::-1]  #tersten tüm karakterleri alır

##############################

name, surname, age, job = "William", "Shakespeare", 30, "English Teacher."
# Yukarıdaki değişkenlerle terminal'e aşağıdaki ifadeyi yazdır
# "My name is William Shakespeare, I'm 30 y/o. I'm an English Teacher."

#1.yol
result = "My name is "+ name+ " " + surname+ ", I'm "+ str(age) + " y/o. I'm an "+ job
#2.yol
result = "My name is {} {}, I'm {} y/o. I'm an {}".format(name, surname, age, job)
#3.yol süslü parantezleri numaralandır {0},{1}... gibi
result = f"My name is {name} {surname}, I'm {age} y/o. I'm an {job}"

print(result)

##############################

# "Hello world" ifadesindeki w harfini "W" ile değiştir
x = "Hello world"
x = x[6]
x = x[0:6] + "WWW"+ x[-4:]
print(x)

#2.yol - replace metodu
x = x.replace("w","WWW")

##############################

# "abc" ifadesini yanyana 3 kere yazdır
x = "abc" * 3
print(x)
#ya da
print(x[::3]) #sadece a değerini verir
