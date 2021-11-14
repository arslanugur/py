INPUT               METHOD                  OUTPUT
--------------------------------------------------------------
"Hello World"       .endswith("by")         False
"Hello World"       .startswith('Hello')    True
"hello world"       .capitalize()           "Hello World"
"13/11/2021"        .split("/")             ["13","11","2021"]
" Hello "           .strip()                "Hello"
"Hello A"           .replace("A","B")       "Hello B"
"hello world"       .count("o")             2
"Hello World"       .find("o")              4                 # Index Number
"123456"            .isnumeric()            True
"HELLO"             .lower()                "hello"
"hello"             .upper()                "HELLO"
"I am the Batman"   .title()                "I Am The Batman"



message = "Hello there. I am the Batman."

message = message.split()
message = message.split('.')   # splits from dots, not the space
message = ' '.join(message)    # * instead of the space

index = message.find('the')
print(index)                  # output: 6  --> 6th index
                              # output: -1 --> no word in the sentence

isFound = message.startswith('H') # True
isFound = message.endswith('H')   # False
print(isFound)

message = message.replace('Batman', 'Superman')
message = message.replace(' ', '*')
message = message.replace('ç', 'c')
                 .replace('ş','s')
                 .replace('ö','o')
    
message = message.center(100)      # puts the message in the middle of 100 characters (Container)
message = message.center(50, '*')  # puts * instead of the space
print(message)


print(message[2]) # by using split method 
                  # each index number shows word in the array



  
# STRING FORMATTING
name = 'Da'
surname = 'Vinci'
age = 30

print('My name is {} {}'.format(name, surname))       # str metodlarından biri: format. format namei süslü parantezin yerine koyar
print('My name is {1} {0}'.format(name, surname))     # 0, 1 --> Da Vinci
                                                      # 1, 0 --> Vinci Da
# print('My name is {s} {n}'.format(n=name, s=surname)) #index numaralarını kullanmak yerine bu sefer...
#eğer yukarıdaki gibi age bilgisi tanımlamıyorsan "30 string'i yazar geçersin
# print("My name is {} {} and I'm {} years old.".format(name, surname, age))
# print("My name is {} {} and I'm {} years old.".format(name, name, name))

# result = 200 / 700
# print('the result is {r:1.4}'.format(r=result))

print(f"My name is {name} {surname} and I'm {age} y/o.") #fstring metodu


# result = 200 / 700
# print("the result is {}".format(result))
#sonuç float olacağından bunu formatmak gerekli
# print("the result is {r:1.3}".format(r=result))
#ilk parametre olarak 1 bilgisi,2.parametre olarak 3 bilgisi verilir ve sayı yuvarlanır
#1 bilgisi ise o miktarsa karakterlik alan bırakır 3 bilgisi kaç basamak olacağını temsil
#1 bilgisi sayının kendisini yazdırır

str = '{c}, {b}, {a}'.format(a = 5, b = 9, c = 7)
print(str)
  
  

  
