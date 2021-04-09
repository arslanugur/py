"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi   
    Müşteri yaşı 
"""
customerName = 'James'
customerSurname = 'Joyce'
customerNameSurname = customerName + ' ' + customerSurname
print(customerNameSurname)
customerSex = True      #Male
customerIdentityNo = '13165465445'      #string yapmak daha mantıklı
customerBirthyear = 1989
customerAddress = 'Istanbul'
customerAge = 2021 - customerBirthyear 

"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    
    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL
"""
#sipariş bilgileri hesaplama
order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3

print("Total:", total)     #ya da print(order1 + order2 + order3)

