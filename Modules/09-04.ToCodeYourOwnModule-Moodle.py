#bu dosyanın asıl ismi mood.py

"""
Modül hakkında bilgilendirme
"""
#sayfanın en başına gelip bi de print ifadesi yazalım

print('modül eklendi')

number = 10

numbers = [1, 2, 3]

person = {
    'name' : 'Jack',
    'age' : '30',
    'city' : 'California'
}   #value şeklinde tanımlandı

def func(x): #bi func tanımlayalım dışardan x parametresi alsın
    '''
    function hakkında bilgilendirme, help dökümanı hazırlayabiliriz
    '''
    print(f'x : {x}')

class Person:
    def speak(self): #person classının speak isminde bi metodu
        print('I am speaking') #yaptığı işlem ise print ile


