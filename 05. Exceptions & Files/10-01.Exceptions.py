# Error Handling ---- Hata yönetimi

# NameError (Unknown Valuable) - Tanımlanmamaış bir değişkeni yazdırmaya çalışmak
print(a) 

# ValueError - Inappropriate function value -- yanlışlıkla str ifadesi var
int('1a2') 

# ZeroDivisionError - Sıfır ile bölünemez hatası
print(10/0)

# SyntaxError - Yazım Yanlışı Hatası
print('attemp't)



#bize gelecek bütün hataları grup şeklinde yönlendirebiliriz
# tk tek nameerror ya da syntaxerror diye bakmaktansa

#importerror
#indexerror - range n index number
#typeerror
#gerisine python.org ile builtin exceptions kısmından bakabilirisin


# Example:
try: 
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print('Done calculation')
except ZeroDivisionError:
    print('An error occurred')
    print('due to zero division')


# Example:
try: 
    variable = 10
    print(variable / 'hello')
    print(variable / 2)
except ZeroDivisionError:
    print('due to zero division')
except (ValueError, TypeError):
    print('An error occurred')      #

    
    
# Example:
try:
    print(1)
    assert 2 + 2 == 5
except AssertionError:
    print(3)
except:
    print(4)

    
# Example:
try:
    print(1/0)
except ZeroDivisionError:   # 
    raise ValueError        #

    

# Example:
try:
    num = 5 / 0
except:
    print('An error occurred')
    raise


# Example:
try:
    print('Hallo')
    print(1 / 0)
except ZeroDivisionError:
    print('Divided by zero')
finally:
    print('This code will run no matter what')



# Example:
try:
    print(1)    # 
except:
    print(2)
finally:
    print(3)    #


# Example:
print(1)            #
assert 2 + 2 == 4
print(2)            #
assert 1 + 1 == 3   # AssertionError
print(3)


# Example:
print(0)            #
assert 'h' != 'w'
print(1)            #
assert False        # AssertionError
print(2)
assert True     
print(3)


# Example:
temp = -10
assert (temp >= 0), 'Colder than absolute zero!'    # AssertionError

# Example:
def func(x):
    assert x > 0, 'Error'
    print(x)
    
