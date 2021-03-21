
students = {
    '120':{
        'name' : 'Ugur',
        'surname' : 'Arslan',
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
# bi listeyi öğrenciden aldığımız bilgilere göre hazırla
#kullanıcaya no gir adı dicez sözlük yapısı oluşturup liste üzerine eklicez
students = {}   #sözlük veri tipi tanımla
number = input('student no: ')
name = input('student name: ')
surname = input('student surname: ')
phone = input('student mobile: ')
# kullanıcadan alacağımız bilgilerle dolacak
#şuan için döngü yapısını bilmediğimiz için copy paste yapıyoruz yukarıdaki düzeni
students[number] = {
    'name': name,
    'surname': surname,
    'phone': phone
}
# kullanıcan alınan bilgilerle liste oluşturdu
#update in aksine birden fazla veri girmek için copy paste yapman gerek
## print(students)

# diğer bi şekilde update metodunu da kullanabiliriz
students.update({
    number: {        #key = number, value = gerisi
        'name': name,
        'surname': surname,
        'phone': phone
    }
}) #},) diyerek birden fazla veriyi girersin
#update ile birden fazla veriyi liste üzerine ekleme şansımız var
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
# yukarıdaki printi eğer süslersek
print('*'*50)
#2-students numaralarını kullanıcıdan alıp ilgili student bilgilerini göster

stuNo = input('student no: ')  #kullanıcıdan öğreni nosunu iste
#stuNo adında bi değişken içine de atadın
#bulunan öğrenci öğrenci isminde girilir
student = students[stuNo]
print(student)
#yukardaki printteki öğrenciyi obje şeklinde gösteermek yerine f str oluştur
print(f"Aradığınız {stuNo} nolu öğrencinin adı: {student['name']} surname: {student['surname']} ve telefonu ise {student['phone']}")

#yıldızlar sonrası üste doldurduğun verilernden öğrenci numarasıyla f str ile yazılanları çıkaracak

#bu derste sözlü yapısını kullanıcıdan alınan bilgilere göre oluşturuldu
#bunu daha sağlıklısı loop yani döngü yapısını bilmek
# mesela 10 öğrenci ise 10 kere döngü çalışır ve ona göre çıkar

