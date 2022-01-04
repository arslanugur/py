# Dictionaries are data structures used to map arbitrary keys to values.
# Lists can be thought of as dictionaries with integer keys within a certain range.
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
# Dictionaries are sometimes called associative arrays or hashes in some other languages
# Dictionaries can store any type of values only as values but dictionary require hashable keys!
# Don't forget there's curly bracket while declaring dictionaries

# 1st : 2nd
# key : value
# Key can be a string
# Value can be an integer

# https://realpython.com/iterate-through-dictionary-python/

# Keys are arbitary, means you can put anyhting immutable in key; except list and dictionary. 
# Because list and dictionary are mutable but while retrieving data from key use square brackets.

# Example: to define a valid dictionary with two elements.
cars = {"BMW": "blue", "Volvo": "red"}


# Example:
ages = {"Dave": 24, "Mary": 42, "John": 58}       # as index: ages = {0: 24,1: 42,2: 58}
print(ages["Dave"]) # 24
print(ages["Mary"]) # 42

# Each element in a dictionary is represented by a key:value pair.

# Example:
ages = {"Dave": 24, "Mary": 42, 58:"John"} 
print(ages["Dave"]) # 24
print(ages["Mary"]) # 42
print(ages[58])     # John


# Example:
my_dict = { 6:"six int", "6":"six str", 7:"seven" } 
print(my_dict[6])   # six int
print(my_dict["6"]) # six str 
print(my_dict[7])   # seven
print(my_dict[0])   # KeyError: 0

# Example:
ages = {1 : 24, 2 : 42, 3 : 58} 
for x in ages: 
    print(ages[x])    # 24 42 58
#


# Be careful, Duplicate key are valid, but only the last has been stored. 
# Example:
dict = {1: "knock", 2: "foot", 1: "hot", 4: "shot"}
for i in dict: 
     print(dict[i]) 
#


# False Example about key : value order
dic = {[1,2,3] : "any_value"} # it will provide a Key error because 1,2,3 is not a valid key. 
dic = {"any_value": [1,2,3]} # is valid 
print(dic[any_value][0]) # prints first element of key "any_value"


# Trying to index a key that isn't part of the dictionary returns a KeyError.
# Example:
primary = {
    "red": [255, 0, 0], 
    "green": [0, 255, 0], 
    "blue": [0, 0, 255], 
}

print(primary["red"])
print(primary["yellow"])    # KeyError: yellow

# As you can see, a dictionary can store any types of data as values. 
# An empty dictionary is defined as {}


# Example:
test = { }          # means that key and value are both empty, but the dictionary still exist.
print(test[0])      # we index the key "0", which is not in “test” ---> KeyError


# Only immutable objects can be used as keys to dictionaries. 
# Immutable objects are those that can't be changed. 
# So far, the only mutable objects you've come across are lists and dictionaries. 
# Trying to use a mutable object as a dictionary key causes a TypeError. 
# Example:
bad_dict = {
    [1, 2, 3]: "one two three", 
}                             # TypeError: unhashable type: 'list'    --> unhashable = something that can't be stored in dictionaries 
# bad_dict will cause a Type error bad_dict = {[1, 2, 3]: "one two three", } 
# bad Trying to use a mutable object as a dictionary key causes a TypeError. 
# good_dict = {"one two three": [1, 2, 3],} # good_dict has no errors

# An object is hashable if it has a hash value which never changes during its lifetime (it needs a hash() method). 
# A list is unhashable because its contents can change over its lifetime.

# a dictionary is a type of map, they use a hash to build keys for objects in a map. It is supposed to provide fast access to the key:item pairs


# One way to test whether a variable is mutable or not is to copy it to a new variable, then change the first variable: 
a = 8 
b = a 
a += 2 
print(a) 10 
print(b) 8 
# Integers are immutable, since a change to 'a' was not a change in 'b'. 
a = "hello"
b = a 
a = "goodbye"
print(a) # "goodbye"
print(b) # "hello"
# Strings are immutable, since a change to 'a' was not a change in 'b'. 
a = ['do', 're', 'mi']
b = a
a.append('fa')
print(a) # ['do', 're', 'mi', 'fa']
print(b) # ['do', 're', 'mi', 'fa']
# Lists are mutable, since a change to 'a' was also a change to 'b'.
#

# Here's the list of class that are immutable: 1. Bool 2. int 3. float 4. tuple 5. str 6. frozen set 
# Here's the list of class that are mutable: 1. list 2.set 3.dict

# unhashable = a value that can be changed in an object     # Mutable types are unhashable - can change. 
# hashable = a value that cannot be changed in an object.


# Python represents all its data as objects. 
# Some of these objects like lists and dictionaries are mutable, meaning you can change their content without changing their identity. 
# Other objects like integers, floats, strings and tuples are objects that can not be changed. 
# An easy way to understand that is if you have a look at an objects ID. 
# Below you see a string that is immutable. You can not change its content. It will raise a TypeError if you try to change it. 
# Also, if we assign new content, a new object is created instead of the contents being modified. 
s = "abc" 
id(s) # 4702124
s[0] 'a' 
s[0] = "o" 
# Traceback (most recent call last): File "<stdin>", line 1, in <module> TypeError: 'str' object does not support item assignment
s = "xyz" 
id(s) # 4800100
s += "uvw"
id(s) # 4800500
# You can do that with a list and it will not change the objects identity
i = [1,2,3]
id(i) # 2146718700
i[0] 1
i[0] = 7 
id(i) # 2146718700


# Example:
dict = { dave: 23 , sam: 14 }
print(dave) #  this gives a NameError. ( says dave is not defined ) 
# Example:
dict={ "dave":23 , "sam":14} 
print("dave") # no error so "" is important while defining a key (in variables) 


# Dictionaries store data in hash tables which optimises lookup when dealing with bulk data...
# So when your program needs to store a lot of data use dictionaries

# Creating a Nested Dictionary 
nested_dict = { 'dict1': {'key_A': 'value_A'}, 'dict2': {'key_B': 'value_B'}} 
dict = {1: 'Geeks', 2: 'For', 3: {'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}


# Coolest Example:
X = {1:10, 2:20}
Y = {3:30, 4:40}
Z = {**X, **Y}


# these values can be also used as a dictionary key       "one two three", False

# Example:
mydict = {"BMW":12, "DODGE":23} 
# The KEYS in this dictionary are: BMW and DODGE 
# The values in this dictionary are: 12 and 23 rescpectively 
# The question above asks: Which of these CAN'T be used as a dictionary KEY? 
# False can be used as a key 
mydict = {False:3}
print(mydict[False]) # will print 3 "one two three" can be used as a key 
mydict = {"one two three":6} 
print(mydict["one two three"]) # will print 6 {2: 4, 3: 9, 4: 16,} cannot be used as a dictionary key mydict = {{2: 4, 3: 9, 4: 16,}:10} print(mydict[{2: 4, 3: 9, 4: 16,}]) will print some error Remember False and false are two different things
                                        

# Example:
my_dict={'1':{'2':4,'3':6}, '2':{'4':16,'5':25}} 
print(my_dict['1']['3'])      # 6



# Example:
mydict = {false : 3} 
print(mydict[false]) # the answer is error 
false = 1 
mydict = {false : 3} 
print(mydict[1]) 
# the answer is 3 
false = 1 
mydict = {false : 3} 
false = 2 
print(mydict[2]) # the answer is error 



# INTERESTING FACT
# Dictionaries are your snipers! 
# Dictionaries are one of the most commonly used data structures. 
# Quite often a dictionary is built for the sole purpose of having uber fast access to its items. 
# Imagine you have 1 million swords objects with a different name (and strength, resistance, special powers, magic energy, type, speed, fluffiness, ecc ecc); 
# if you store all your swords in a list and you precisely want "The Dragon's Claw" 
# you'd have to start reading such list from the start and compare every name to find the one you want. 
# Quite differently, with a dictionary where the name is the key and the sword object is the value, you would do just ONE read. Boom! No for loops required. 
# In cases like this, lists are AK47, dictionaries are snipe rifles! Use them! 
# Example: 
print(swords["The Dragon's Claw"].resistance) 
# side note: for improved performance/memory usage use an integer unique id as key rather than the name string. Game devs always fight back string comparisons.

# There is no restriction in putting lists in dictionaries and dictionaries in lists. 
mylist = [0,{"d":45,5:[7,8]},7] 
print (mylist[1][5][1])       # 8
                              # Accessing the list in the dictionary in a list.

    
# Example:
my_d = { "red": [1, 3, 8], "green": [8, 77, 9], "blue": [45, 67, 8], }
print(my_d["red"][0])
print(my_d["green"][1])
print(my_d["blue"][2])


# Example:
latlon = {"San Francisco": [37.77493,-122.41942], "New York City": [40.71427, -74.00597], "Tuscon": [32.22174, -110.92648],} 
print(latlon["New York City"])
print(latlon["Tuscon"])


# Example:
primary = {
    "red": [255, 0, 0], 
    "green": [0, 255, 0], 
    "blue": [0, 0, 255], 
}
for i in primary:
    print(i)    # red, green, blue
print('\n')
for i in primary:
  print(primary[i]) # values of colours
print('\n')
for i in primary:
    print(i,primary[i]) # print the whole dictionary
print('\n')
for i,j in primary.items():
    print(i,j[0],j[1],j[2]) # print the whole dictionary without brackets

# By default, dicts iterate over their keys, so you can write "for k in d" rather than the wordier "for k in d.keys()".



# Example:
dict1 = {'key1':'value1','key2':'value2'}
print(dict1)

print("1")

print(dict1["key1"])
print(dict1["key2"])

print("2")

for i in dict1:
    print(i) #keys

for i in dict1:
    print(dict1[i]) #values, coz i are keys

for key, value in dict1.items():
    print(key,value) #key and value

print("3")

a = 'key2'
print(dict1[a]) # == dict['key2']

print("4")

dict1['key3']='value3' #if list,use append()
print(dict1) # added key3:value3

print("5")

b = 'key4'
c = 'value4'
dict1[b]=c
print(dict1)

print("6")

dict2 = {"who":"John","time":"6"}
dict3 = {"time":"9","who":"Susan"}

def wakeUp(who="Peter",time="8"):
    print(who,"wakes up at",time,"o\'clock.")

wakeUp()
wakeUp(**dict2) # ** for keyworded argument
wakeUp(**dict3) # sequence irrelevant for keyw''d arg



# Example:
list = [4,{"dic":5,{"fear":0,"love":9},"tion":6},7] 
print(list[0]) 
print(list[1]["dic"]) # Output: SyntaxError in line 1 
# Update: 
list = [4,{"dic":5,"fear":{"love":9,"hate":3},"tion":6},7] 
print(list[0])                  # 4
print(list[1]["dic"])           # 5
print(list[1]["fear"]["love"])  # 9


# Example:
student = {'name':'Gloria' , 'age':25, 'courses':['Math', 'CompSci']} 
print(student) # output {name': 'Gloria', 'age' :25, 'courses':['Math', 'CompSci'] 
# We can update this code e.g by adding student phone number. 
student ['phone'] = 070370753 
student ['name'] = Jane
print(student) # Updated output will now be: {'name': 'Jane', 'age':25, 'courses':['Math', 'CompSci'], 'phone':070370753}
                                                                                   



# ALL EXAMPLES ABOUT DICTIONARIES
# Dictionaries map keys to values and store them in an array or collection.
# The keys must be of a hashable type, which means that they must have a hash value
# that never changes during the key’s lifetime.
# The keys can be any object with __hash__() and __eq__() methods.

fruits = {'apple':5, 'orange':10}
print(0, fruits)
print(1, fruits.items())
print(2, fruits.keys())
print(3, fruits.values())

for key in fruits: #fruits.keys()
    print(4, key, fruits[key])
for item in fruits.items():
    print(5, item)
for item in fruits.items():
    print(6, *item)                            # unpacking
for key, value in fruits.items():              # unpacking
    print(7, key, value)
for key in fruits.keys():
    print(8, key)
for value in fruits.values():
    print(9, value)
    
sum1 = sum(list(v for v in fruits.values()))
sum2 = sum([v for v in fruits.values()])    # list comprehension
sum3 = sum(v for v in fruits.values())     # generator expression
sum4 = sum(fruits.values())
print(10, sum1, sum2, sum3, sum4)

print()
dic = {'one': 1, 'two': 2}
print(11, dic)
new_dic = {value: key for key, value in dic.items()}
print(12, new_dic)

from itertools import chain
for item in chain(dic.items(), new_dic.items()):
    print(13, item)

for item in {**dic,**new_dic}.items():  # ** unpacking operator
    print(14, item)
    
print()
dic = {1: 111, 2: '222'}                           # be careful
print(15, dic)
print(16, dic[1], type(dic[1]))
print(16, dic[2], type(dic[2]))
# 111 int    222 str

print()
print(17, *dir({}))
print()
help({})



# Examples on simple database with dictionary and list:
"""
Simple database made with dictionary and list
To make it work you have to copy to IDLE due to restrictions
"""
base = {}  # empty dictionary for start

while True:
    print()
    print('Base')  
    print('Chose option:')
    print('New input "n"')
    print('Delete "d"')
    print('Overview "p"')
    print('Exit "z"')
    print()

    inputopt = input('Please input option: ')
    if inputopt == 'n':
        name = input('Enter name: ')
        birth = input('Enter date of birth (dd/mm/yyyy): ')
        salary = input('Enter salary: ')
        date = input('Date of begining: ') 
        base.update({name : [birth, salary, date]})  # after we gather all required inputs from user  
        print(base)                                  # Key - first input (name), Value - list with 3 elements         
        # print result so we can overview all steps (if there is multiply inputs)
        
    if inputopt == 'd':
        delete = input('Enter name: ')
        del base[delete]  # delete key in dictionary together with its value 
        print(base) # print result so we can overview this step

    if inputopt == 'p':
        i = 1
        for k, v in base.items():  #printing overwiev with ascending number and content of database (dictionary)
            print(i, '.', k, ',', v[0], ',', v[1], ',', v[2])  
            i = i + 1
 
    if inputopt == 'z':
        break   #exit




#dictionary - bir liste türü
#key - value  -  bi bilgiye ulaşmak için key bilgisini kullanıyoruz

# 41 => kocaeli    34 => istanbul        temsil ediyor


#peki dictionary olmadan liste olarak bu nasıl yapılır
cities = ['kocaeli', 'istanbul']
plaques = [41, 34]

print(plaques[cities.index('istanbul')]) #unutma sıraların birbirine uyması gerekir

#ama iki liste yerine tek bi listeyle
# print(plaques['istanbul'])  => 34 vermeli
#yani amaç, key bilgisiyle value bilgisine ulaşmak

#DICT ile nasıl yapılır
#plaques = { 'key' : 'value' } #keye karşılık bi value bilgisi yazdırcaz
plaques = { 'kocaeli' : 41, 'istanbul' : 34 } #plaques tekrar tanımlanır ama köşeli değil süslü olarak 
print(plaques['istanbul'])

plaques['ankara'] = 6 #yeni  value eklersek
plaques['kocaeli'] = 'new value' #yeni value atadık
print(plaques)


######
#yeni örnek
users = {'Shakespeare': {
          'age': 30,
          'roles':['user'], 
          'email': 'shakespeare@gmail.com',
          'address' : 'Manchester',
          'phone' : '507'
          },
         'Joyce' : {
          'age': 31,
          'roles':['admin', 'user' ] #web sitesinde rolleri belirtme
          },
         'au' : 26,
         'ua' : 50}    #aynı şekilde süslü parantezle diğer valueler de verilir

print(users['Shakespeare'])
print(users['Shakespeare']['phone'])
print(users['Joyce']['roles'][0])

# genel olarak yaptığımız şey, salladığımız bilgilere verdiğimiz isim


