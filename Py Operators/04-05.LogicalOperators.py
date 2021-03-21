"""
x = 5

result = 5 < x < 10

print(result) #false değeri gelir çünkü x 5e eşit 5den büyük değil

#tabi bu işlemleri yukardaki gibi yapmak yerine 
#and
x = 6
result = x > 5 and x < 10 #and operatöründe koşulun her iki durumu true ise bize true der
print(result) #sonuç 'true, true => 'true' olarak gösterir ya da tam tersi çünkü iki soru var
"""
"""
#and ope str ifadelerde de kullanılabilir
hak = 5
devam = 'e'  #user bi oyun oynuyorsa, input bilgisini almamız gerek
result = (hak > 0) and (devam == 'e') 
#hak sıfırdan büyükse ve devam etme seçeneği 'e' ile eşitlenmişse oyuna devam
print(result) #true bilgisi gelir
"""
"""
#or

x = 5
result = (x > 0) and (x % 2 == 0) # eğer x değişkeni 0dan büyükse
# x poz bi değer mi yani 0dan büyük
# ve mod ope kullanarak değer 0 sıfıra eşitse x çift bi sayıdır
print(result)

result = (x > 0) or (x % 2 == 0) #sadece bir tanesinin doğru olmasıyla ilgileniyorsan or
print(result)
# true, false -> true
# false, false -> false olur
"""
"""
#not operatörlerini kullanabiliriz
x = 5
result = not(x > 0) #x pozitif mi true gelir
#ama başına not ope koyarsak false çıkar
print(result)
"""
#x 5 ile 10 arasında yer alan bir çift sayı mı?
x = 6
result = ((x > 5) or (x < 10)) and (x % 2 == 0) 
#3 tane soru sorduk. ilk and/or ope çalışırsa ikinci and ope çalışcak
print(result)
