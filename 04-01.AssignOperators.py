#atama operatörleri
"""x = 5
y = 10
z = 20 #değişken = değer
"""
#ya da üstekiler yerine bu şekilde atama yapabiliriz
x, y, z = 10, 40, 30 
#peki bu değerleri değiştirirsek
x, y = y, x # bu şekilde değişir

x = x + 20 # yeni değer atarız ya da x += 5 
z -= 3
y *= 2
x /= 2
z %= 2 #y için mod işlemi 
y //= 3 #tam bölme yap
y **= 5 #üst alma operatörü
z *= x  #z ile xi çarp ve bunu zye yansıt

print(x, y, z)

#atama operatörleri liste üzerinde nasıl kullanılır
values = 1, 2, 3 #tuple liste örneği

x, y, z = values #tuple içindeki değerleri x y z ye aktar
print(x, y, z)   
#karşımızda 123 ama values değerlerinden birini silersek hata gösterir
# liste içerindeki iki eleman üç değer içine aktarılamaz -not enough
#eğer values listesinde fazla eleman varsa yine hata -too many
#ama değişkenlerden birinin başına yıldız eklersen o değişkene dizi şeklinde gider 
"""
values = 1, 2, 3, 4, 5 

x, *y, z = values 
print(x, y, z) 

#z için bi liste oluşturur
#print(x, y, z[0]) yazdırırsak sadece 3 gelir
"""
print(values)
print(type(values)) #tipini de yazdır class 'tuple'



