#METHODS

list = [1,2,3]
list.append(4)
print(list)
print(type(list))
#class içerisinde bi çok metod bulunduran yapı kod bütünü
#append,pop vs
myStr = 'Hallo'
print(type(myStr))
#mesele şu: str ve list birer class ve bunlar için kütüphanede tanımlanmış bi çok metod var
#class bilgisini öğrendikten sonra bu metodlaır kendimiz oluşturabileceğiz

#FUNCTIONS
#metod gibi belli amaçlara yönelik olrak oluşturulmuş olan bi yapı
#fonsiyonlar class içinde tanımlanmaz
#class üzerinden yani list. ya da str. üzerinden ulaşmıyoruz. fonksiyonlara kendileri üzerinden buluyoruz
#class ismi gerekmiyor!


#ikisi de aynı amaçla kullanılıyor ama kullanış yerleri farklı



# FIVE POWERFUL PY FUNCTIONS
# 1. Lambda Function
# Lambda function is used as a substitute of traditional function 
# as declaring and using lambda function is easy when we want to do only a single operation
lambda_cube = lambda y : y*y*y
print(lambda_cube(5)) # 125

# 2. Map Function
# The map() function executes a specified function for each item in an iterable
nums = [1, 2, 3, 4]   # double number using map and lambda
result = map(lambda x : x+x, nums)  # syntax: map(function, iterable)
print(list(result))   # [2, 4, 6, 8]

# 3. Filter Function
# The filter() function returns an iterator were the items are filtered through a function to test of the item is accepted or not
seq = [0, 1, 2, 3, 5, 8, 13]  # sequence # filter all odd numbers
result = filter(lambda x: x%2!=0, seq)
print(list(result)) # [1, 3, 5, 13]

# 4. Zip Function
# The purpose of py zip() method is to map the similar index of multiple containers so that they can be used just using as single entity
name = ['one', 'two', 'three']
value = [1, 2, 3]

result = zip(name, value) # syntax: zip(iterable1, iterable2, ...)
print(list(result))       # [('one', 1), ('two', 2), ('three', 3)]

# 5. enumerate Function
# enumerate() function adds a counter to an iterable and returns it in a form of enumerated object.
# This enumerated object can then because directly for loops or converted into list or tuples using type cast functions
seq = ['one', 'two', 'three']

result = enumerate(seq, start=1)  # syntax: enumerated(iterable1, [start=1])
print(list(result)) # [(1, 'one'), (2, 'two'), (3, 'three')]



