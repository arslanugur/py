#Karakter Dizileri: String

"""
name = "Aretha"
surname = "Franklin"
age = 30
 
print("Her name is "+ name + " "+ surname + " and \nI'm "+ str(age) + " y/o.")    

#str(age) ile tür dönüşümü yaptık
#deneme = her name is.. adında string de atayabilirdik
#greating = "Her name is "+ name + " "+ surname + " and \nShe is "+ str(age) + " y/o."
#print(greeting)

#\n ifadesi ile sonrasında gelen cod bi alt satıra iner
"""
"""
#eğer ifadelerden birinin nosunu yazdırırsak sıra numarası gelir
print(name[0]) 
#ya da
print(greeting[2])
"""

greeting = 'Her name is '+ name + ' '+ surname + ' and \nShe is '+ str(age) + ' years old'
print(len(greeting)) #atanmış greeting ifadesinin kaç karakterli olduğunu söyler
#bunu bu şekilde de yapılabilir length = len(greeting)

#print(greeting[length-1]) #Son karakteri buluruz
#print(greeting[2:5])      #2.indexden başlar 5.indexe kadar gider
#print(greeting[3:])       #3.indexden başlar sonuna kadar gider
#print(greeting[:15])      #Baş karakterden 15e kadar gider
#print(greeting[2:40:2])   #2den 40a kadar ama her iki karakterde bir alır
  
#bu yapılanlar string formatlamayla bağlantılı: + ile yaptık


###############

#name = 'OtisRedding'
# print(dir(name)) #neler yapabilirsin
# print(help(str)) #tanım yapar

name = 'Redding\'s song'
#message = f'hello {name}'
#print(message)   
#ya da
message = 'hello {}'
print(message.format(name))
