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
# LISTS: []             mutable, indexed
# TUPLES: ()            immutable, indexed 
# DICTIONARY: {pairs}   mutable, not indexed (dict don't use an index, instead they use a key which must be arbitrarily defined) 
# SETS: {}              mutable, unique elements, not indexed
# Dictionaries and Sets are unordered. Also, sets don't store duplicates.
 


Example: 
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

scipbel
