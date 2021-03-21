#Object Oriented Programming in Py
#Nesne tabanlı programlama nedir?

#class


#instance #diğer ado object
lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4]

#bu kopyalar üzer kullanılan bazı metodlar
lst1.append #clear, copy gibi  #bu metodların hepsi oluşturulmuş instance üzerinden kullanılabilir


result = type(lst1) #tanımlanan listenin tipini ekra ayzdır
result = type(lst2) #anyı sonuç çünkü aynı list classından üretilmiş bi kopya
#bi liste tanımladıımız zaman oluşturmuş old classın bi kopyasını oluşturuyoruz
print(result) #class list

#kendi classlarımızı da oluşturabiliriz

#örneğin bi kullanıcı kaydı tutalım
#class --> Person(name, surname, age)
# burda bazı metodlar da kullanabiliriz
# mesela age tutmak yerine birthday hesabı yapmak gibi calculateAge() metodu gibi
# class ın olayı çok kişi üzerinden aynı bilgileri sınıflandırma gibi düşünülebilir 
#bi nevi person object yarattık bu class ile toplu bilgi düzenlemesi yapılabilir
# yani örnek classı çoğaltma işlemi. name atama, year 

#yani tek bi class ile  - Jack object, John object, James object

