# SECTION 1
# Sets are data structures, similar to lists or dictionaries. 
# They are created using curly braces, or the set function. 
# They share some functionality with lists, such as the use of in to check whether they contain a particular item.
# Example:
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)           # True
print("spam" not in word_set) # False

# To create an empty set, you must use set(), as {} creates an empty dictionary.
# To create an empty SET, this works: x = set([ ])

# Dictionaries are also built with curly brackets but contain a pairs: dict={"a":1,"b":2}

# Set Methods 
# Python has a set of built-in methods that you can use on sets. 
# add()                           Adds an element to the set 
# clear()                         Removes all the elements from the set 
# copy()                          Returns a copy of the set 
# difference()                    Returns a set containing the difference between two or more sets 
# difference_update()             Removes the items in this set that are also included in another, specified set 
# discard()                       Remove the specified item 
# intersection()                  Returns a set, that is the intersection of two other sets 
# intersection_update()           Removes the items in this set that are not present in other, specified set(s) 
# isdisjoint()                    Returns whether two sets have a intersection or not 
# issubset()                      Returns whether another set contains this set or not 
# issuperset()                    Returns whether this set contains another set or not 
# pop()                           Removes an element from the set # remove() Removes the specified element 
# symmetric_difference()          Returns a set with the symmetric differences of two sets 
# symmetric_difference_update()   Inserts the symmetric differences 

# Example:
set1 = {1, 2, 3 } 
set2 = {1, 2, 2, 3 } 
set3 = {3, 2, 2, 1 }      # Sets CAN'T have duplicates
print(set1) 
print(set2) 
print(set3) 

if set1 == set3: 
  print(True) 
else: 
  print(False)            # Result : {1, 2, 3 } {1, 2, 3 } {1, 2, 3 } True


# HINTS:
# [ ] = list        mutable, indexed
# ( ) = tuple       immutable, indexed
# { } = set         mutable, unique elements, not indexed           set() = empty set
# { } = dictionary  mutable, not indexed (dict don't use an index, instead they use a key which must be arbitrarily defined)
#                   (key : value) = {pairs}         {} = empty dictionary 
# Dictionaries and Sets are unordered. Also, sets don't store duplicates.



# Example: 
my_set = {1, 2, 2, 3, 3, 3} 
print("Length: ", len(my_set))      # Length: 3
print("Elements:")                  # Elements
for element in my_set: 
  print(element)                    # 1 2 3
# watch out when iterating over a set with a for loop like I did: 
# sets are unordered, so you may not always get the elements in the order you expect them to be 
# (but it works nicely for this demonstration of not storing duplicates) 

# The pair for dictionary is called a key and value. For example, {x:y} The "x" is the key while the "y" is the value.
# Set cannot store any duplicates. You can prove by len().

# Dictionary uses key to access value, not indexed. 
# It uses hash (random access method) in background to refer the key. 
# And it is the fastest way if you want to access a value that is not referenced by number.

# Example:
num_set = {1,2,3,3,4,4,5} 
print(num_set,len(num_set)) # output {1,2,3,4,5}, 5 
# The len property tells us dah d lenght of d set is 5 meanwhile physically looking at it, its 7
# Values cannot be repeated in sets//python automatically eliminates them if encountered.

# Keys of dictionaries are not arbitrary. 

# Example:
set(["spam"])   # = {"spam"} 
set("spam")     # = {"s","p","a","m"}

# An easy way to check whether a list contains duplicates: 
list1 = [1, 2, 3, 4] 
list2 = [1, 2, 2, 3] 
list1 == list(set(list1)) # True 
list2 == list(set(list2)) # False
# This is because creating a set removes all duplicate elements from the argument

# here is a difference between lists ,tuple and sets:
alpha ='rabbit' ,'zebra' ,'cat' ,'dog' 
print(list(alpha))                              # ['rabbit', 'zebra', 'cat', 'dog']
print(tuple(alpha))                             # ('rabbit', 'zebra', 'cat', 'dog')
print(set(alpha))                               # {'zebra', 'rabbit', 'cat', 'dog'}

nums ='1' ,'2' ,'3' ,'12' ,'8' ,'4' ,'5' ,'1'
print(list(nums))                               # ['1', '2', '3', '12', '8', '4', '5', '1']
print((tuple(nums)))                            # ('1', '2', '3', '12', '8', '4', '5', '1')
print(set(nums))                                # {'5', '4', '1', '2', '8', '3', '12'}

num2 = 1 , 2 , 3 , 4 , 5 ,18 , 9 , 15 
print(list(num2))                               # [1, 2, 3, 4, 5, 18, 9, 15]
print(tuple(num2))                              # (1, 2, 3, 4, 5, 18, 9, 15)
print(set(num2))                                # {1, 2, 3, 4, 5, 9, 15, 18}

alpha_nums = 'rabbit' ,'cat' , '1' ,' zebra' ,'18' ,'9' 
print(list(alpha_nums))                         # ['rabbit', 'cat', '1', ' zebra', '18', '9']
print(tuple(alpha_nums))                        # ('rabbit', 'cat', '1', ' zebra', '18', '9')
print(set(alpha_nums))                          # {'18', ' zebra', '1', '9', 'cat', 'rabbit'}

alpha_num2 ='dog' , 1 , 9 ,5 ,'rabbit' 
print(list(alpha_num2))                         # ['dog', 1, 9, 5, 'rabbit']
print(tuple(alpha_num2))                        # ('dog', 1, 9, 5, 'rabbit')
print(set(alpha_num2))                          # {1, 5, 9, 'dog', 'rabbit'}

alpha_nums_num2 = 1 , '1' , 11 , ' 12' , 'rabbit' ,'zebra' 
print(list(alpha_nums_num2))                    # [1, '1', 11, ' 12', 'rabbit', 'zebra']
print(tuple(alpha_nums_num2))                   # (1, '1', 11, ' 12', 'rabbit', 'zebra')
print(set(alpha_nums_num2))                     # {1, ' 12', 11, '1', 'zebra', 'rabbit'}


# Example:
letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print(1)
else: 
  print(2)  # 1, because e is not in letters.
#    


# SECTION 2
# Sets differ from lists in several ways, but share several list operations such as len.
# They are unordered, which means that they can't be indexed.
# They cannot contain duplicate elements.
# Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.
# Instead of using append to add to a set, use add.
# The method remove removes a specific element from a set; pop removes an arbitrary element.
# Example:
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)       # {1, 2, 3, 4, 5, 6}
nums.add(-7)
nums.remove(3)
print(nums)       # {1, 2, 4, 5, 6, -7}

# Basic uses of sets include membership testing and the elimination of duplicate entries.


# Example:
nums = {1, 2, 1, 3, 1, 4, 5, 6} 
while len(nums) > 0: 
  nums.pop() 
  print(nums)
#   
# so much for 'arbitrary' 
# {2, 3, 4, 5, 6}
# {3, 4, 5, 6}
# {4, 5, 6}
# {5, 6}
# {6}
# set()
#


# it looks like "pop" always deletes first element, not arbitrary? 
nums = {1, 2, 1, 3, 1, 4, 5, 6} 
print(nums)   # {1, 2, 3, 4, 5, 6}
nums.add(-7) 
nums.pop() 
print(nums)   # {2, 3, 4, 5, 6, -7}
# run code 10 times and pop always delete first element.

# Notice that the add() and remove() methods don't return a new set - they only change the set in place. 
# Example:
set_1 = {1, 2, 3} 
a = set_1.remove(3) 
print(a) # this doesn't work - the output is 'None' 
set_1.remove(3) 
print(set_1) # this works

# You can save the element being popped, but not the one being removed: 
nums = {1, 2, 3, 4, 5, 6} 
print(nums) # {1, 2, 3, 4, 5, 6}ş
a = nums.pop() 
print(a)    # 1
b = nums.pop() 
print(b)    # 2
print(nums) # {3, 4, 5, 6}


# You can add multiple elements to a set by using .update() method. 
# For instance: 
nums = set([1, 2, 3]) 
print(nums)           # {1, 2, 3}
nums.update([4, 5]) 
print(nums)           # {1, 2, 3, 4, 5}


# There's another difference between sets and lists; 
# Lists can take any item while sets, as for dictionaries' keys, can only take hashable objects. 
# What do I mean by hashable objects? Hashable objects are objects which: 
# - there is a .__hash__() defined for each of them and it is constant throughout the life of their corresponding objects and 
# - there is also another method called .__eq__(), which simply let us know that these objects can be compared to each other. 
# For instance, all immutable objects are hashable, likewise consider the following code 
# a="Hi" b="Hi" print(a.__hash__() == b.__hash__(), a is b) which will print True True due to strings being hashable(a and b are the same thing).
# x = [] y = [] print(x is y) 
# This one will print False, which is a hint to show us that lists are indeed nonhashable, so can't be elements of a set. (x and y are not the same thing). 

# Example:
nums = {7, 5, 6, 8, 2, 1, 4, 1, 4, 5, 6} 
print(nums)         # {1, 2, 4, 5, 6, 7, 8}
nums.add(3)
nums.remove(1)
print(nums)         # {2, 3, 4, 5, 6, 7, 8}
print(nums.pop())   # 2
# which means that sets order "list" and pop() delete and return the smallest element in that "list"


# Sets get some kind of random order (not ascending and not the order we wrote it). 
# Pop _usually_ (always in this example) removes "first" element, but we can not be sure which one is first in a set! 
# (See how sets that are considered equal became not equal after "popping" one element in each 'cause they had diferent "order") 
# Only if we check it first, but remember: it's still not guaranteed that same "first_one" will be deleted. 
# Especially if we would be working with parallel processes, multithreading.

# This code will explain the .pop() method more: 
nums = {1, 2, 1, 3, 1, 4, 5, 6} 
while len(nums)>1: 
  print(nums) 
  nums.pop() 
  print(nums)
#
"""
{1, 2, 3, 4, 5, 6}
{2, 3, 4, 5, 6}
{2, 3, 4, 5, 6}
{3, 4, 5, 6}
{3, 4, 5, 6}
{4, 5, 6}
{4, 5, 6}
{5, 6}
{5, 6}
{6}
"""

# Would have guessed list would be faster at returning search results than set due to indexing, but there is some logical fallacy in that thought. 
# http://stackoverflow.com/questions/2831212/python-sets-vs-lists

# To show that a set can execute the result more faster than a list, this is my try. 
import time 
my_list = [1,3,3.14,"Vas","dBy"] 
tic1 = time.time() 
# starting time 
print(3.14 in my_list)              # True
tac1 = time.time() 
#ending time 
print(tac1 - tic1)                  # 3.600120544433594e-05
# total duration of execution 
my_set = set(my_list) 
tic2 = time.time() 
print(3.14 in my_set)               # True
tac2 = time.time() 
print(tac2 - tic2)                  # 6.9141387939453125e-06
# or something else True 1.430511474609375e-6 So here, set is executing the result much faster than list.

# your_set.pop() removes the first element and returns it's value. So, using a set together with your_set.add(x) could be used as a queue of unique values


# Example: To create a set, add the letter "z" to it, and print its length.
nums = {"a", "b", "c", "d"}
nums.add("z")
print(len(nums))  # 5

# 1. Create a set with {} 
# 2. Use the add function to include the letter z into the set. 
# 3. Then call the len function to print it's length. So.. nums = {"a","b","c","d} nums.add("z") print(len(nums)) 
 

# SECTION 3
# Sets can be combined using mathematical operations.
# The union operator | combines two sets to form a new one containing items in either.
# The intersection operator & gets items only in both.
# The difference operator - gets items in the first set but not in the second.
# The symmetric difference operator ^ gets items in either set, but not both. 
# Example:
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second)   # {4, 5, 6}
print(first - second)   # {1, 2, 3}
print(second - first)   # {8, 9, 7}
print(first ^ second)   # {1, 2, 3, 7, 8, 9}
# Set are 'randomly' ordered; that mean for Everest element in set are calculated some number in internal 'storage' (hash); 
# For example, for some object it May be 16832, and for another obj 6425. that may be some index of that element in that storage. 
# so it may be visible as almost random... items in a set appear at random without index


# 'Symmetrical difference' is also known as 'exclusive or'. The symbol in logic is ⊕. 
# You often see it written as XOR. It means all the elements in the first set plus all the elements in the second set minus all the elements in both sets. 
# So if s1 = {1, 2, 3, 4} and s2 = {3, 4, 5, 6}, then s1 ^ s2 = {1, 2, 5, 6}

# you can also write down it like this: 
first = {1, 2, 3, 4, 5, 6} 
second = {4, 5, 6, 7, 8, 9} 
print(first.union(second))                  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first.intersection(second))           # {4, 5, 6}
print(first.difference(second))             # {1, 2, 3}
print(first.symmetric_difference(second))   # {1, 2, 3, 7, 8, 9}


# Sets in python are very simillar to set in mathematics which that: 
# A∪B = A | B (union) =============> objects that belong to set A or set B 
# A∩B = A & B (intersection) ==========> objects that belong to set A and set B 
# A-B = A - B (relative complement) ====> objects that belong to A and not to B 
# A∆B = A ^ B (symmetric difference) ===> objects that belong to A or B but not to their intersection
# Remember that in set A-B not equal to B-A

# A | B ： A∪B A & B ： A∩B A - B：A -A∩B A^B : A∪B-A∩B

# Sets are none-indexed list. They cant be index so they are not necessarily sorted. 
# but we can make it sorted by turning it into a list.
# Example: Sorting a Set
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

third = second - first
forth = [i for i in third]
forth.sort()
print(forth)    # [7, 8, 9]

# Example:
a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)       # {3}      # «&» means «intersection». It takes the values that are common to both sets. In this case, it's 3.

# | is OR -> Elements in first OR in second -> all elements (no duplicate). 
# & is AND -> Elements in first AND second -> elemenst in both sets. - is SUBTRACTION -> Elements in first NOT in second (differenece).
# This one is different. And is the elements in either not in the other.



# SECTION 4: Data Structures
# As we have seen in the previous lessons, Python supports the following data structures: lists, dictionaries, tuples, sets.

# When to use a dictionary:
# - When you need a logical association between a key:value pair.
# - When you need fast lookup for your data, based on a custom key.
# - When your data is being constantly modified. Remember, dictionaries are mutable.

# When to use the other types:
# - Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
# - Use a set if you need uniqueness for the elements.
# - Use tuples when your data cannot change. 

# Many times, a tuple is used in combination with a dictionary, for example, a tuple might represent a key, because it's immutable. 


# list = ["a", "b", "c"] 
# dictionary = {"a": 0, "b": 1, "c": 2} 
# set = {"a", "b", "c"} 
# tuple = ("a", "b", "c")

# Immutable Structures: Tuple 
# Mutable Structures: Dictionary, List, Set
# Unique Elements: Set 
# Not Unique Elements: Dictionary, List, Tuple Indices? √ Dictionary(keys), list, tuple × Set
# Notations: 
# Curly braces: Dictionary, 
# Set Square brackets: lists 
# Parentheses: Tuple
# - Sets are mutable while frozensets are immutable. 
# - The keys of dictionaries are unique, they are not indices, they are just unique keywords. The set type is mutable 
# — its contents can be altered using methods like add() and remove(). 
# Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. 
# The frozenset type is immutable and hashable 
# — its contents cannot be altered after it is created; it can therefore be used as a dictionary key or as an element of another set. 
# Plus: - Below are sequential objects: List, Tuple, String - Below are unordered objects: Dictionary, Set


# There are currently two built-in set types, set and frozenset. 
# The set type is mutable — the contents can be changed using methods like add() and remove(). 
# Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set. 
# The frozenset type is immutable and hashable — its contents cannot be altered after it is created; 
# it can therefore be used as a dictionary key or as an element of another set.

# Sets, the data types does not allow duplicate values


# Example: to see dictionary in a program
db = {} 
print('Welcome to the simplest key-value database') 
while True:
    print('What do you want to do?')
    print('Enter P to [P]ut, G to [G]et or L to [L]ist') 
    print('Or enter Q to [Q]uit') 
    action = input()
    if action == 'P':
        k = input('Enter key: ')
        d = input('Enter data: ')
        db[k] = d
    elif action == 'G': 
        k = input('Enter key: ')
        if not k in db:
            print('No such key')
        else:
            print('Your data: %s' % db[k])
    elif action == 'L': 
        print('DB contents:')
        print(db)
    elif action == 'Q':
        print('Bye') 
    break
#              


# Sets are like lists, with the difference that its elements can't be repeated. 
# Tuples are also like lists, but they can't be modified. 
# Dictionaries are basically lists made up of keys each associated with a value.


# Lists l = [1, "a"] 
# Tuples t = (2, "b") 
# Dictionaries d = {"k1":3, "k2":"c"} 
# or d = dict([("k1", 3), ("k2", "c")]) 
# Sets s = set([4,"d"]) # or s = {4,"d"}


# Example:
nums = {1, 2, 1, 3, 1, 4, 5, 6} 
print(nums)         # {1, 2, 3, 4, 5, 6}
nums.add(-7) 
nums.remove(3) 
print(nums)         # {1, 2, 4, 5, 6, -7}

# Example:
s = {4,2,5,7,8,7} #sets 
l=[4,2,5,7,8,7]   #list 
print(s)  # {2,4,5,7,8}
print(l)  # [2,4,5,7,8,7]


# Example:
A = "woman","man","boy","girl" 
print(list(A))          # ['woman', 'man', 'boy', 'girl']
print(tuple(A))         # ('woman', 'man', 'boy', 'girl')
print(set(A))           # {'man', 'girl', 'boy', 'woman'}
print(dictionary(A))    # NameError: name 'dictionary' is not defined



# Tuples are immutable meaning unable to be changed. 
# You cannot add to, remove, or modify items in the tuple. You can however modify mutable datatypes nested within a tuple. 
# Example:
a = (1,2,3,[4,5,6]) 
a[3][0] = 7 
print(a) # (1, 2, 3, [7, 5, 6])



# EXAMPLES
# Example: Pop() not Random for Sets
# output of these is 1 in each case
print('These don\'t vary:')
print({1, 2, 3}.pop())
print({1, 3, 2}.pop())
print({2, 1, 3}.pop())
print({2, 3, 1}.pop())
print({3, 1, 2}.pop())
print({3, 2, 1}.pop())

# output of these vary each time the code is run
print('These vary from run to run, but the same element pops for each set:')
print({'1', '2', '3'}.pop())
print({'1', '3', '2'}.pop())
print({'2', '1', '3'}.pop())
print({'2', '3', '1'}.pop())
print({'3', '1', '2'}.pop())
print({'3', '2', '1'}.pop())



# Example: Sets get random order of (contained) element (pop removes "first" ones but they may differ)
nums = {1, 2, 1, 3, 1, 4, 5, 6}
nums2 = {-7, 1, -9, 0, 33, 44, 223, 2, 4, 5, 6}
print(nums2)
print(nums)
print()
nums.add(-7)
nums.remove(3)
nums2.remove(223)
nums2.remove(44)
nums2.remove(33)
nums2.remove(0)
nums2.remove(-9)
print(nums)
print(nums2)
if nums == nums2:
    print(True)
else:
    print(False)
while len(nums)>0:
    nums.pop()
    nums2.pop()
    print(nums)
    print(nums2)
    if nums == nums2:
        print(True)
    else:
        print(False)
print(".")
# Output:
"""
{0, 33, 1, 2, 4, 5, 6, 44, -9, -7, 223}
{1, 2, 3, 4, 5, 6}

{1, 2, 4, 5, 6, -7}
{1, 2, 4, 5, 6, -7}
True
{2, 4, 5, 6, -7}
{2, 4, 5, 6, -7}
True
{4, 5, 6, -7}
{4, 5, 6, -7}
True
{5, 6, -7}
{5, 6, -7}
True
{6, -7}
{6, -7}
True
{-7}
{-7}
True
set()
set()
True
.
"""


