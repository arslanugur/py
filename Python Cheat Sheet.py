# Websites:
# https://www.practicepython.org/
# https://www.tiobe.com/tiobe-index/
# https://www.practicepython.org/exercises/
  
# Python Data Type Cheatsheet
# String                    List                      Tuple                     Set                         Dict
# -----------------------------------------------------------------------------------------------------------------------------------
# immutable                 mutable                   immutable                 mutable                     mutable
# ordered/indexed           ordered/indexed           ordered/indexed           unordered                   unordered
# allows duplicate members  allows duplicate members  allows duplicate members  not allow duplicate members not allow duplicate keys
empty_string=""             empty_list=[]             empty_tuple=()            empty_set=set()             empty_dict={}
str_w_single_element="h"    list_w_single_item=["h"]  tup_w_single_item=("h")   set_w_single_item={"h"}     dict_w_single_item={"h":1}

# list, can store any data types str, list, set, tuple, int and dict
# tuple, can store any data types str, list, set, tuple, int and dict
# set, can store data types (str, int, tuple) but not (list, set, dict)
# dict, inside of dict key can be int, str, and tuple only values can be of any data type int, str, list, set and dict.



# Must Learn Py Libraries
pygame, random, numpy, os, collections, subprocess, functools, itertools, multiprocessing


# REMOVE & DEL statement
# Remove() function is used to delete a specific object in the list
list1 = [1,2,3,4,5,6]
list1.remove(2)  # [1,2,4,5,6]

# DEL or POP
# Used to delete an object at a specific location (index) in the list
list1 = [1,2,3,4,5,6]
del list1[2]  # [1,2,4,5,6]




###### TRICKS
# Trick 1: Lambda Function vs. Regular Function
# This is a regular function
def Function(Parameter):
  return Parameter

# This is a lambda function
Function = lambda Parameter : Parameter

# Regular Function Example
def Add(a, b):
  return a + b
print(Add(3, 4))  # output: 7

# Lambda Function Example
Add = lambda a, b: a + b
print(Add(3, 4))  # output: 7


# Trick 2: Using Generators Inside Functions
lst = [1, 5, 6, 7, 8]
print(sum(num for num in lst))

# You can also do this
print(sum(range(10)))

# output: 27
#         45

# Trick 3: Checking the Usage of Memory
import sys
num = 2
char = 'Abc'
lst = ['Abc']

print(sys.getsizeof(num))    # 28
print(sys.getsizeof(char))   # 52
print(sys.getsizeof(lst))    # 72


# Trick 4: List Comprehensions
cities = ['Dublin', 'London', 'Oslo']

def visit(city):
  print("Welcome to  "+city)
  for city in cities:
    visit(city)

# output:
# Welcome to Dublin
# Welcome to London
# Welcome to Oslo


# Trick 5: Using the zip() function
name = ["Max", "Mike", "Dustin"]
roll_num = [10, 11, 12]

z = list(zip(name, roll_num))
print(z)     # output: [("Max", 10), ("Mike", 11), ("Dustin", 12)]


# Trick 6: **kwargs
dictionary  = ("a": 5, "b": 8)

def calculate(a, b):
  print(a + b)
  return

calculate(**dictionary)  # output: 13


# ONE-LINERS
# 01. To Swap Numbers
a, b = b, a

# 02. Reverse a String
mystring[::-1]

# 03. String Palindrome
mystring = mystring[::-1]

# 04. Palindrome Python One Liner
phrase.find(phrase[::-1])

# 05. Factorial of a number
fact = lambda n:[1,0][n>1] or Fact(n-1)*n

# 06. Factorial of a Number
reduce(lambda x,y:x*y, range(1,n+1))

# 07. Fibonacci Sequence
fib = lambda x: x if x<=1 else fib(x-1) + fib(x-2)

# 08. Read a File
[line.strip() for line in open(filename)]





# Trick 8: Assign Value to Multiple Variables in one line
# Stop doing below
list1 = ["a", 1, ("c", "d")] 
a = list1[0] 
b = list1[1]
c = list1[2]
print(a, b, c)  # a 1 ('c', 'd')
# do better way
list1 = ["a", 1, ("c", "d")] 
a, b, c = list1
print(a, b, c)  # a 1 ('c', 'd')



# Trick 8: f string
# Stop doing this
name = "python"
print("Coding"+ name)

# Do this way
name = "python"
print(f"Coding {name}")


# Enum: Enum'lar birbirinden farklı sabit değerlere bağlı sembolik ifadelerdir
class Days:
  Mon, Tue, Wed = range(3)

print(Days.Mon) # 0
print(Days.Tue) # 1
print(Days.Wed) # 2


# Memory Usage: sys.getsizeof, bir nesnenin boyutunu bayt cinsinden döndürür. Nesne herhangi bir tür olabilir
import sys
year = 2020
print(sys.getsizeof(year))  # 28


# Birden fazla değer dönmek: Py'daki fonksiyonlar, tuple'lar yardımıyla birden fazla değişken döndürülebilir
def double(a, b):
  return a * 2, b * 2

n1, n2 = double(3, 4)

print(n1) # 6
print(n2) # 8


# In-Place değişken değiştirme: Py'da değişkenleri yer değiştirmek için üçüncü bir değişkene veya fazladan koda gerek yoktur
age1 = 22
age2 = 33

age1, age2 = age2, age1
print(age1, age2)   # 33 22


# Elemanlardan string oluşturma: Join fonksiyonu ile, elemanlardan string oluşturabiliriz
nums = ["1", "1", "2"]
e = "".join(nums)
print(e)  # 112


# Operatörleri zincirleme: Py'da karşılaştırma operatörlerini zincirleyerek daha okunabilir ve kısa kodlar oluşturabilirsiniz
x = 8
# Bunun yerine
if x > 5 and x < 9:
  print("Yes")
# bu yapılabilir
if 5 < x < 9:
  print("Yes")

# String'i çarpın: Bir string'i bir tamsayı ile çarptığınızda, Py dizeyi tekrarlar ve yeni bir tane döndürür.
ans1 = "Alright"
ans2 = ans1 * 3
print(ans)  # AlrightAlrightAlright


# String'i ters çevirmek: -1 ifadesi kullanılarak, string elemanları tersine çevrilebilir
s1 = "Self Control"
s2 = "lortnoC fleS"

print(s1[::-1]) # lortnoC fleS
print(s2[::-1]) # Self Control

# Reverse String using Py
s = "reverse"                       # initial string
stringlength = len(s)               # calculate length of the list
slicedString = s[stringlength::-1]  # slicing
print(slicedString)                 # print a reversed string

# Armstrong Number Program in Py
num = int(input("Enter: "))
sum = 0
temp = num
while temp > 0:
  digit = temp % 10
  sum += digit ** 3
  temp //= 10
if num == sum:
  print("Armstrong Number")
else:
  print("Not an Armstrong Number")


# Program to find LCM of two numbers
n1, n2 = 15, 20
if(n1 > n2):
  max = n1
else:
  max = n2
while(True):
  if(max % n1 == 0 and max % n2 == 0):
    print(max)
    break;
  max = max + 1 # 60
  
  
# Random Number Generator
import random
print(random.randint(1, 10))


