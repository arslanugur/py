#error

#error handling ---- Hata yönetimi

print(a)  #nameerror  - unknown valuable
#tanımlanmamış bi değişkeni ekrana yazdırmaya çalışma

int('1a2') #valueerror - inappropriate func value
#yanlşlıkla str bi ifade var

print(10/0) #ZeroDivisionError
#print ile bir bölme işlemi, ama sayı 0'a bölünemez

print('attemp't)   #syntaxerror
#yazım yanlışı var


#bize gelecek bütün hataları grupşeklinde yönlendirebiliriz
#tek tek nameerror ya da syntaxerror diye bakmaktansa

#importerror
#indexerror - range n index number
#typeerror
#gerisine python.org ile builtin exceptions kısmından bakabilirisin


"""1
try: 
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print('Done calculation')
except ZeroDivisionError:
    print('An error occurred')
    print('due to zero division')
"""

"""2
try: 
    variable = 10
    print(variable / 'hello')
    print(variable / 2)
except ZeroDivisionError:
    print('due to zero division')
except (ValueError, TypeError):
    print('An error occurred') #çıktısı
"""
"""3
try:
    print(1)
    assert 2 + 2 == 5
except AssertionError:
    print(3)
except:
    print(4)
"""

"""
try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError    #çıktısı Zero ve Value olur
"""

"""
try:
    num = 5 / 0
except:
    print('An error occurred')
    raise
"""

"""
try:
    print('Hallo')
    print(1 / 0)
except ZeroDivisionError:
    print('Divided by zero')
finally:
    print('This code will run no matter what')
"""

"""
try:
    print(1)
except:
    print(2)
finally:
    print(3)   #output - 1 and 3
"""

"""
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)
"""

"""
print(0)
assert 'h' != 'w'
print(1)
assert False
print(2)
assert True     
print(3)
"""

"""
temp = -10
assert (temp >= 0), 'Colder than absolute zero!'
"""

def func(x):
    assert x > 0, 'Error'
    print(x)
    
