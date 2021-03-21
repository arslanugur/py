'''1 
message = 'Hello There. My Name Is Arslan'.split() #split-dizi liste yapmak
print(message)
print(message[0]) #karşımıza hello index numarasıylaçıkar split kullanmazsan sadece H gelir
'''

'''2
my_list = [1,2,3]
my_list = ['bir',2, True, 5.6]
print(my_list) 
'''

"""3
list1 = ['one','two','three']
list2 = ['four','five','six']
numbers = list1 + list2
print(numbers)
print(len(numbers)) #len metoduyla adetini öğreniriz
print(numbers[2])

userA = ['Ugur', 30]
userB = ['Arslan', 25]
#users = userA + userB
users = [userA, userB] #bu şekilde yeni bi liste daha oluştururz
#print(users[1]) #ulaşmak istersek de userBiçeriğine ulaşırız
print(users) #liste içinde bi liste elemanı oldu

a = users[1]
print(a[0]) #dizinin içindeki Arslan bilgisi çıkar
#ya da aynı sonuç için aşağodaki gibi yazılır
print(users[1][0]) 

print(users[0][0])
print(users[0][1])
print(users[1][0])
print(users[1][1])
"""

letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])

###EXAMPLES
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) #2.index ve 6.index arasını print eder

print(squares[3:8])
print(squares[0:1])
print(squares[1::4]) #atlar
print(squares[1:-1]) #sondan -1 indexle başlar, baştan 1.indexle başlar

a = list[0:2] #ilk iki element yazdırır

