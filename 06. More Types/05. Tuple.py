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
# The output is: {“a”:9, “b”:8, “c”:7, “d”:6, “e”:5}

# Example:
words = ("spam", "eggs", "sausages",) 
words = ("spam", "pop", "sausages",) 
print(words[1])




#tuple da liste gibi ama biraz farklı
list = [1, 2, 3]           #liste tanımlanması
tuple = (1, 'two', 3)      #paranteze gerek yok ama okunabilirlik için kullan

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

