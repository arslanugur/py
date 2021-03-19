#karakter dizileri: string

"""
name = "Uğur"
surname = "Arslan"
age = 30
 
print("My name is "+ name + " "+ surname + " and \nI'm "+ str(age) + " y/o.")

#yada deneme = my name is adında string de atayabiliriz
#str(age) ile tür dönüşümü yaptık
#\n ifadesi ile sonrasında gelen cod bi alt satıra iner
# ya da greating = "My name is "+ name + " "+ surname + " and \nI'm "+ str(age) + " y/o."
# sonra print(greeting)
"""
"""
# eğer ifadelerden birinin nosunu yazdırırsak sıra numarası gelir
print(name[0]) #ya da print(greeting[2]) gibi
"""

#print(len(greeting)) greeting ifadesinin kaç karakterli olduğunu söyler
#bunu bu şekilde de yapılabilir length = len(greeting)
#print(greeting[length-1]) ya da print(greeting[-1])ile de SON karakteri buluruz
#print(greeting[2:5]) bu durumda 2. indexden başka 5.indexe kadar gider
#print(greeting[3:]) bu durumda 3den başlar sonuna kadar gider
#print(greeting[:15]) bu durumda baştan 15e kadar gider
# print(greeting[2:40:2]) 2den 40a kadar ama her iki karakterde bir alır
  
#bu yapılanlar string formatlamayla bağlantılı + ile yaptık yani zordu



#name = 'arslan'

# print(dir(name)) #neler yapabilirsin

# print(help(str)) #tanım yapar
name = 'arslan\'s dog'
# message = f'hello {name}'
# print(message)   #ya da
message = 'hello {}'
print(message.format(name))#name = 'arslan'

# print(dir(name)) #neler yapabilirsin

# print(help(str)) #tanım yapar
name = 'arslan\'s dog'
# message = f'hello {name}'
# print(message)   #ya da
message = 'hello {}'
print(message.format(name))