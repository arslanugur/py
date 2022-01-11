# Tuples are very similar to lists, except that they are immutable (they cannot be changed).
# Also, they are created using parentheses, rather than square brackets.
# Example:
words = ("spam", "eggs", "sausages",)
# You can access the values in the tuple with their index, just as you did with lists:
print(words[0])   # spam


# Trying to reassign a value in a tuple causes a TypeError. 
words = ("spam", "eggs", "sausages",)
words[1] = "cheese" # TypeError

# Like lists and dictionaries, tuples can be nested within each other.

# tuples are immutable but the content of mutable elements (like lists) inside a tuple can be changed! 
t = (1, "hungry", ['x' , 'y']) 
t[0] = 234 # results in a type error because t is immutable 

t = (1, "hungry", ['x' , 'y']) 
t[2][0] = 'abc' 
print(t) # output is: (1, "hungry", ['abc' , 'y']) so the content of the list inside the tuple is mutable
  
# Why use tuples? 
# Because they require less processing power from Python because they're immutable. 
# Doesn't make a big diff in small programmes but if you're working on a big project it will improve speed and efficiency. 

# Lists are created with square brackets,           # list = [0, 1, "two"]
# Dictionaries are created with curly brackets,     # dict = {"keyOne": 0, "keyTwo": 1, "keyThree": "two"}
# Tuples are created with parentheses.              # tuple = (0, 1, "two")

# https://learnpython31.blogspot.com/2020/07/python-data-types.html


# Tuples can also be "packed" and "unpacked" which can be very useful for creating variables 
fruits = ("Apple", "Pear", "Banana") 
f1, f2, f3 = fruits
print(f1) # Apple
print(f2) # Pear
print(f3) # Banana


# Example:
# you can omit the parentheses: 
words = "spam", "eggs", "sausages" 
print(words[0]) # Output: spam 
# You can also assign separate variables: 
a, b, c = "spam", "eggs", "sausages" 
print(b) # Output: eggs


# Example:
words1 = ("spam", "eggs", "sausages",) 
words2 = ("spaam", "eeggs", "saausages",) 
print(words1 + words2) # ("spam", "eggs", "sausages", "spaam", "eeggs", "saausages")

# Tuples are unmutable and can be used as keys in dictionaries. 
# Tuples can help in some cases when you need lists as dictionary keys: just transform lists into tuples.

# Example:
# If you have tuple as elements in a list, you can convert it to dictionary with one command! 
lst = [(“a”, 9), (“b”, 8), (“c”, 7), (“d”, 6), (“e”, 5)] 
dct = dict(lst) 
print(dct) 
# Output: {“a”:9, “b”:8, “c”:7, “d”:6, “e”:5}

# Example:
words = ("spam", "eggs", "sausages",) 
words = ("spam", "pop", "sausages",) 
print(words[1]) # output: pop


# Immutable means the value of original memory(RAM) space which referred by an immutable object(number, strings, tuple...) can't be changed, 
# but the immutable object can be changed by creating a new memory space.
num = 1
print(id(num)) # 22862960
num = 2
print(id(num)) # 22862948
a = 1
b = a
b += 1
print(a) 1
print(b) 2
# Mutable means the value of original memory space which referred by a mutable object(list, dictionary) can be changed without creating a new memory space, 
# then the mutable object changes.
a = [1, 2]
b = a
b += [3]
print(a) [1, 2, 3]
print(b) [1, 2, 3]
print(id(a)) # 27814608
print(id(b)) # 27814608

# List          A= [...,...,...] 
# Dictionaries  B= {...,...,...} 
# Tuple         C= (...,...,...)
# The difference is Mutability between list and tuple! Tuple is enum in C, while list is array in C.


# Although tuples' elements can't be reassignd 
# But you can reassign the tuple itself as a whole
tupleA = () 
print(tupleA)
# output : () 
tupleA = (1,2,3) 
print(tupleA) 
# output : 1,2,3 
tupleA += (4,5,6) 
print(tupleA) 
# output : 1,2,3,4,5,6


# Example of nested tuples: 
tpl1 = ("abc","def") 
tpl2 = ("123",tpl1,"456") 
print(tpl1) 
print(tpl2) # Output: ('abc', 'def') ('123', ('abc', 'def'), '456')

# A tuple is a collection which is ordered and unchangeable
# In Python tuples are written with round brackets.
# Example:
Tuple =("spam","eggs","sausages",) 
print(Tuple)


# Example:
# Tuple is a kind of sequence normally it is written in parentheses like: t={1,2,3,4,5} in tuple, we can put heterogeneous elements. 
# In tuple parentheses is not compulsary. list --> mutable, tuple --> immutable


# Example: to create a list, dictionary, and tuple:
list = ["one", "two"]       # describe a list
dict = {1:"one", 2:"two",}
tp = ("one", "two")         # no need paranthesis, but use for readability
                            # tuples use commas. parantheses is just best practice but not needed. 
                            # Example: 4,4,4 is a tuple. also written as (4,4,4)

# list uses []:-mutable; Array in c++ ,
# dict uses{}:-mutable; Similar structure in c++ 
# tup uses():-immutable;Similar to struct

# Tuples can be created without the parentheses, by just separating the values with commas.
# Example:
my_tuple = "one", "two", "three"
print(my_tuple[0])  # one

# An empty tuple is created using an empty parenthesis pair.
tpl = ()
# Tuples are faster than lists, but they cannot be changed.


# Hint: A function can return more than 1 value by using tuples 
def f(): 
  x=12 
  y=8 
  return 

x,y z = f() 
print(z)    # (12,8) 
print(z[1]) # 8

# https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
# https://www.careerride.com/python-list-vs-tuple-vs-dictionary-vs-set.aspx
# https://monjurulhabib.wordpress.com/2016/09/22/python-when-to-use-list-vs-tuple-vs-dictionary-vs-set-theory/

# Note that to recognize a tupla with only one item it is needed to add a comma at the end, in other cases (more items) comma is optional. 
tupl = "Example"
print(tupl[0]) # print "E" since tupl is a string 
tupl = Example
print(tupl[0]) # print "Example" since tupl is a tupla Note also that 'tuple' object does not support item assignment, 
# but it is possible to change which tuple is assigned to a variable: 
tupl = "first", "second", tupl[1]="sec                # Error 'tuple' object does not support item assignment 
tupl = "first", "second", tupl = "one","two","three", # No error


# Example:
print("\nFalse tupla, 1 item without comma") 
my_tuple = "Example" 
print(my_tuple[0]) #print "E" 

print("\nReal tupla, 1 item with comma") 
my_tuple = "Example", 
print(my_tuple[0]) #print "Example" 

print("\nTupla change, new tupla assignment") 
my_tuple = "one", "two", "three" 
print(my_tuple[0]) #print "one"

print("\nTupla error, item assignment cannot change") 
my_tuple[0] = "One" #TypeError 



# Example:
my_tup = 5,"red","eggs",7 
print(my_tup)       # 5,'red','eggs',7 
# print multiple values 
print(my_tup[0:4])  # 5,'red','eggs',7 
# range values 
print(my_tup[0:3])  # 5,'red','eggs 
print(my_tup[0:2])  # 5,'red' 
# you can use this too 
print(my_tup[0:-1]) # it will print all values except last one 5,'red','eggs

# 1. Tuples are faster than lists and cannot be changed(No reassignment). 
# 2. If a tuple consists of only a single element,it needed to be end with comma as- t=(1,)

# Example:
tuple = (1, (1, 2, 3))            # (1) = 0 and (1, 2, 3) = 1 in tuple order. 
print(tuple[1])       # (1, 2, 3)
print(tuple[1][0])    # 1
print(tuple[1][1])    # 2
print(tuple[1][2])    # 3
# The following is a reminder of how to print out an element that exists in a sublist/sub-tuple, or a list/tuple WITHIN a list/tuple. 



# Examples of Each IRL: 
# tuples 
seasons = ('spring','summer','fall','winter') 
# chose seasons cuz names of seasons never change 
# lists 
homework = ['math','english']   # Oh no history teacher assigned homework 
homework.append('history')      # Finally finished homework del homework [2] 
                                # dog ate my history homework 
# dictionaries 
#assigning item ids in rpg 
swords = {'redblade':18819,'dragontail': 19923,'bubbleangel':19024} 
# spring event! Time to add a new sword! swords['sakurapiercer'] = 10383



# The difference between tuples and list
import sys
# 1 tuples are immutable unlike lists
# Example
print("list")

list = [1,"hello",False]
tuple = (1,"hello",False)
print(list)

list[1] = "love you"
print("after change")
print(list)
print("\n \ntuple")
print(tuple)

try:
 tuple[1] = "love you"
 print(tuple)
 
except:
 print("tuples are immutable")
 print(tuple)
 print("\n\n")
#2 lists take more memory than tuples
print("the memory differences")
print("list: " + str(sys.getsizeof(list)))
print("tuple: " + str(sys.getsizeof(tuple)))
print("That\'s all i know")





#bunların tiplerine bakarsak
print(type(list))
print(type(tuple))

#liste elemanlarına index ile ulaşmak
print(list[0])
print(tuple[1])

#eleman sayılarını yazdırmak istersen
print(len(tuple))

#eleman değişikliği
list[0] = 'one'   #ama tuple için bu şekilde atama yapılmaz
print(list)
# tuple için eleman atandıktan sonra değişim olmaz, bu yüzden yeni bi liste oluşturman gerekli
# list üzerinden kullanılabilecek method çokken list.append() gibi, tuple için bu metodlar oldukça az

print(tuple.count('two'))
print(tuple.index(3))      #3 karakterinin indexini buldu 2


# listeye tuple listesi ekleme
numbers = ('four', 5, 'six') + tuple
print(numbers)

#listede düzenleme, eleman ekleme ve silme işlemi tuple da olmaz
list = ['Agatha','Victoria']
tuple = ('Dakota','Alice','Alice')
names = ('Denver','Eiffel','Alice') + tuple
print(names)

list[0] = 'Dante'
# tuple[0] = 'Nabokov'

print(tuple.count('Alice'))
print(tuple.index('Alice'))

print(list)
print(tuple)

