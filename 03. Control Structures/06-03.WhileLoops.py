numbers = [1, 2, 3, 4, 5]
# we could reach each element with for loop but if we have no list
# what if to print the numbers from 1 to 100

x = 0  # counting starts with 0, to 100
# to increase one by one when the loop works
# if it comes to 100, the loop stops automatically
# so that the condition always gives "true", whenever it comes "false", the loop will be over (like 100)
while True:
    print(x)    # it produces an infinite loop with while, it means it writes 0 all the time
                # but we need to stop this at certain place
    x < 100:    # this process continues until 100 


# Example:
while x < 100:  # keeps producing true and x <= 100 --> not a stop yet
    print(x)    # happens an infinite loop again. because "x" value should be changed
                # changes if we write x = x + 1 or x += 1
    x += 1      # counts until 99. if you want two by two --> x= x + 2
print('Count is over!')

# we don't have to write all expressions, we use conditional to avoid typing 

# Example:
while x < 100:
    if x % 2 == 0: # if x is even numbers, prints   
        print(x)             
    x += 1         # to write odd numbers --> if x % 2 == 1
print('Count is over!')


# Example:
while x < 100:
    if x % 2 == 1:  # prints if x is odd numbers       
        print(f'number odd: {x}')
    else:           # Otherwise, even numbers is printed
        print(f'number even: {x}')             
    x += 1         # both even and odd numbers, so all of them
print('Count is over!')


# Example:
# to request a value from user, keep asking until the user know that
name = ''       # name takes a string value
                # "name" equals ''
while not name: # the above '' null evaluates as a false 
# while yanındaki ifadenin sürekli true olarak üretilmesi demek, false'un tersini almak demek
# producing the expression as true next to while, means getting the inverse of false 
# 'not name' --> true. means working codes which is true

# input for "name" from the user
    name = input('enter your name: ')
    # ne zaman isim doğru girilirse print ile hallo blabla diyelim
print(f'Hallo {name}')

# inputa bi değer girmediğiniz sürece 'enter ur name' ekrana çıkar
# çünkü name bilgisinin boşluk karakterine eşit olması false'a eşit

# bi değer girmek yerie boşluk(spacebar) karakterine basarsa boş gözükür
# '' bu boş bi str ifade
# ' ' içinde boş bir karakter var
# bunu engellemek için ise while not name.strip(): yazarız.
# böylece spacebar kabul etmez

# Example:
while False:
    print('Looping..') # 0 değerde sonuç çıkmaz

