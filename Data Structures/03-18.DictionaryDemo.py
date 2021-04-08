
students = {
    '120':{
        'name' : 'Amadeus',
        'surname' : 'Mozart',
        'phone' : '507'
    },
    '125':{
        'name' : 'James',
        'surname' : 'Joyce',
        'phone' : '607',
    },
    '130':{
        'name' : 'William',
        'surname' : 'Shakespeare',
        'phone' : '707',
    },
}

#1-bilgileri verilen studentsların kullanıcıdan aldığınız bilgilerle dictionary içinde sakla

#bi listeyi öğrenciden aldığımız bilgilere göre hazırlayıp, 
#kullanıcaya input vererek sözlük yapısı oluşturup liste üzerine eklicez

students = {}   #sözlük veri tipi tanımlandı
number = input('student no: ')
name = input('student name: ')
surname = input('student surname: ')
phone = input('student mobile: ')

#kullanıcadan alacağımız bilgilerle dolacak
#şuan için döngü yapısını bilmediğimiz için copy paste yapıyoruz yukarıdaki düzeni
#update in aksine birden fazla veri girmek için copy paste yapman gerek

students[number] = {
    'name': name,
    'surname': surname,
    'phone': phone
}

# kullanıcan alınan bilgilerle liste oluşturdu

##print(students)


# diğer bi şekilde update metodunu da kullanabiliriz
students.update({
    number: {        #key = number, value = gerisi
        'name': name,
        'surname': surname,
        'phone': phone
    }
}) #},) diyerek birden fazla veriyi girersin

###update ile birden fazla veriyi liste üzerine ekleme şansımız var
print(students)


#ŞİMDİ LOOP BİLMEDİĞİMİZ İÇİN BUNU ÜÇ KERE TEKRARLIYORUZ AŞAĞIDA
students.update({
    number: {        #key = number, value = gerisi
        'name': name,
        'surname': surname,
        'phone': phone
    }
})
number = input('student no: ')
name = input('student name: ')
surname = input('student surname: ')
phone = input('student mobile: ')

students.update({
    number: {        #key = number, value = gerisi
        'name': name,
        'surname': surname,
        'phone': phone
    }
})
number = input('student no: ')
name = input('student name: ')
surname = input('student surname: ')
phone = input('student mobile: ')

students.update({
    number: {        #key = number, value = gerisi
        'name': name,
        'surname': surname,
        'phone': phone
    }
})
number = input('student no: ')
name = input('student name: ')
surname = input('student surname: ')
phone = input('student mobile: ') 

#print(students)
#printi eğer süslersek
print('*'*50)



#2-students numaralarını kullanıcıdan alıp ilgili student bilgilerini göster

stuNo = input('student no: ')  #kullanıcıdan input iste
#stuNo adında bi değişken içine de atadın, bulunan öğrenci öğrenci isminde girilir
student = students[stuNo]
print(student)
#yukardaki printteki öğrenciyi obje şeklinde göstermek yerine f str oluştur
print(f"Aradığınız {stuNo} nolu öğrencinin adı: {student['name']} surname: {student['surname']} ve telefonu ise {student['phone']}")

#yıldızlar sonrası üste doldurduğun verilerinden öğrenci numarasıyla f str ile yazılanları çıkaracak

#burada yapılan sözlük yapısını kullanıcıdan alınan bilgilere göre oluşturulması
#bunu daha sağlıklısı loop yani döngü yapısını bilmek, mesela 10 öğrenci ise 10 kere döngü çalışır ve ona göre çıkar
