# DICTIONARY FUNCTIONS
# Just like lists, dictionary keys can be assigned to different values.
# However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.
# Example:
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 8: 64}

# Example:
squares = {1: 1, 2: 4, 3: "error", 4: 16,} 
squares[8] = 64 
squares[16] = 256 
squares[17] = 289 
squares[24] = 576 
squares[32] = 1024 
squares[3] = 9 
print(squares) # {1: 1, 2: 4, 3: 9, 4: 16, 8: 64, 16: 256, 17: 289, 24: 576, 32: 1024}


# A dictionary defines no sequence for its keys. 
# Especially the sequence of inserting the key:value pairs is not necessarily the same sequence as printing the pairs. 
# Technically the keys are stored in a Hash table, and when iterating the whole dictionary (for printing) 
# the sequence of the hash table comes into play. 


# Python dictionary is based on hash tables. The order of elements is determined by the hash function used and you can't rely on it. 
# It just so happens, that hash function used in Python puts 2**x numbers in the beginning. 
# The fact, that the order of 2**x numbers is not strict is explained by hash collisions and method used to deal with them. 
# You can read more about hast tables on the internet. 
# Simplified explanation would look something like that: 
  # when you type mydict["some_key"] it transforms string "some_key" to some number (using above mentioned hash function), 
  # which corresponds to the actual values as it would in list. 
  # So, you can say that standart dictionary in python is a list that automatically transforms any immutable values(keys) to numbers(indices). 
  # There are also other types of dictionaries based on other data structures such as for example red-black trees. 
  # They are more efficient in some ways and less efficient in other. 
#


# Dictionaries do not "care" about order. 
# Try the code below and add hashed command lines one by one to see how the order of printed content behaves: 
squares = {1: 1, 2: 4, 3: "error", 4: 16} 
squares[8] = 64 
squares[3] = 9 
squares[9] = 81 
squares[7] = 49 
# This code is to show that # DICTIONARIES are NOT ordered. 
# Clear hash signs in rows below 
# one by one and observe 
# how the resulting output behaves # each time a new key is added # in an unordered manner. 
squares["orange"] = "blue" 
squares["apple"] = "green" 
squares[5] = 25 
squares["peach"] = squares["orange"] 
print(squares)                        # {1: 1, 2: 4, 3: 9, 4: 16, 8: 64, 9: 81, 7: 49, 'orange': 'blue', 'apple': 'green', 5: 25, 'peach': 'blue'}

# Why are they named dictionaries? 
# I regard dictionaries as being in rigorous alphabetical order, but maybe computers search for information differently. 

# Dictionaries are mutable unordered collections of elements whereas tuples are ordered ones. So, the place is randomly chosen.
# https://python-reference.readthedocs.io/en/latest/docs/dict/

# Example:
primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])          # 17

# primes[4] refers to the value (recall: each element of a Dictionary posses form Key:Value) in the Dictionary primes that has its (unique identifier) Key as 4. 
# Clearly, it follows that primes[4] refers to 7. Hence, primes[primes[4]] really refers to primes[7]. 
# Following similar lines of thinking as above, it follows that primes[7] refers to 17. 
# Therefore, primes[primes[4]] really refers to primes[7] and hence refers to 17. 
# So, print(primes[primes[4]]) is just print(17), giving output as just 17 clearly.

# Example:
primes = {1: 2, 2: 3, 4: 7, 7: 17}
primes[1] # 2 
primes[2] # 3 
primes[4] # 7 
primes[7] # 17 
# Step by step: 
print(primes[primes[4]]) 
# primes[4] = 7 
# print(primes[7]) 
# primes[7] = 17 
# print(17) # 17 



dic = {'key1':3,'key2':5,'3':'yes'} 
# You have just to understand that the value in the dico['key1'] = 3 will send his value to the super dico[dico['key1']] for that we will have dico[3].
# Or '3' correspond to the key of 'yes' 
# For that dico[dico['key1]] ='yes'
# The value of the dico in the bracket will become the new key.


# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
# Example:
nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)        # True      # 1st print returns "True", because the dictionary contains the key 1; 
print("three" in nums)  # False     # 2nd print returns "False", because "three" in dict. is not a key, but a value; 
print(4 not in nums)    # True      # 3rd print returns "True", because there is really not a key 4 in dict.

# Example:
nums = {1:'one',2:'two', 3:'three'} 
print(1 in nums.keys())             # True
print('three' in nums.values())     # True
print(4 not in nums)                # True


# Example:
nums = { 1: "one", 2: "two", 3: "three", "four": 4, } 
print("four" in nums) # True



# Example: to print "Yes", if the key 112 is present in the dictionary named "pairs".
if 112 in pairs:
  print("Yes")
#


# Example with a possible related dictionary: 
pairs = { 111:[1,1,1], 112:[1,1,2], 113:[1,1,3], } 
if 112 in pairs:
  print("Yes")
#


# Example:
x = 3
y = 7 

for i in range(y):
    if x == 10:
        print("can i get 5 likes?")
    else:
        x += 1 
        # 1. pancakes, 2. 7, 3. can i get 5 likes?, 4. None (nothing)
#

# A useful dictionary method is get. It does the same thing as indexing, 
# but if the key is not found in the dictionary it returns another specified value instead ('None', by default).
# Example:
pairs = { 111:[1,1,1], 112:[1,1,2], 113:[1,1,3], } 
if 112 in pairs: 
  print("Yes")
#



# A useful dictionary method is get. 
# It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead ('None', by default).
# Example:
pairs = {1: "apple",
    "orange": [2, 3, 4], 
    True: False, 
    None: "True",
}

print(pairs.get("orange"))                      # [2, 3, 4]   -- because it is as defined 
print(pairs.get(7))                             # None        -- 7 doesnt exist in the dict and by default, if the key doesn't exist in dict, it is defined as None
                                                #             -- (i.e. absence of value, which would not be redefined)
print(pairs.get(12345, "not in dict"))          # not in dict -- ask to define 12345, if key doesn't exist in dictionary, it is defined as "not in dictionary"
# The reason that happens is because in python 1 is also True. 
# But why does it refer me to True instead of the 1 which appears first on the dictionary? 
# the reason for that is very simple. in python, if you give same key different values, it will always bring up the last. 
# Example, the code : pairs = {1:'apple', 1:'smart'} print(pairs.get(1)) returns 'smart' because it's the last value assigned to the key 1.
  

# Other Prints:
print(pairs.get(56789,"hahaha"))                # ask to define 56789, if key doesn't exist in dictionary, it is defined as "hahaha"
print(pairs.get("orange", "not in dictionary")) # ask to define "orange", if doesn't exist in dict, it is defined as "not in dict". But it exists in the dict as [2, 3, 4]  
(6) print(pairs.get(1))                         # False # ask to define 1, which means True in Python by default. True is defined as False
(7) print(pairs.get("apple"))                   # None # there is no dictionary KEY called apple
(8) print(pairs.get(None))                      # True # None: True


# If you are wondering why print(pairs.get(1)) prints 'False' not 'apple' 
# First you need to know that True is equivalent to 1. But still why prefer this 1 (True) over that 1. 
# To make things clear try this spam={True:'Apple',1:'Banana'} print(spam.get(1)) output: Banana 
# Then this spam={1:'Banana',True:'Apple'} print(spam.get(1)) 
# output: Apple Python and all languages read the code (top to bottom , left to right) 
# so python in the first example will come across the first key which is True ( True is equivalent to 1 as I said ) 
# the code will go to read what value True is holding (It is 'Apple') 
#so it will store 1 as 'Apple',but when it gets to the second key 1 the value will get updated to 'Banana' the second example is the opposite. 
# You can think of it as if you are assigning a value to a variable then reassign the same variable to a different value the old value will be overwritten. 
# eggs=10 eggs=20 print(eggs) output: 20
      

# Example
fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))    # 8
#                 3 + 5 because 7 is not in dictionary. so result 3 + 5 = 8
# 5 is just the default value that was arbitrarily assigned instead of the default None. If the it was get(7,1000) the return would be 1000 since 7 is missing.


# Simple rule for get() : 
# 1. If key is present in dictionary, then get will return the value of key. 
# 2. If key is not present in dictionary, then get will return None or the value mentioned after comma. 
# 3. get() will not add a new key or modify the value of a key in dictionary. 
# So, this is the reason that get(4,0) returns 3 because key(4) is present in dictionary with value(3).

# absence of the value, will print anything after the comma


# There are a few other interesting ways to iterate over dictionaries. 
# Python 3 has an object type called a "view object" that is useful for iterating. 
# Dictionaries have view types "items()", "keys()", and "values ()". You can also convert these to lists. 
# Example: 
nums = { 1: "one", 2: "two", 3: "three", }
for key,value in nums.items(): 
  print(key,value) 
  print("This is a view object: ", nums.items()) 
  print("This is a list: ", list(nums.items())) 
  print("\n") 
  
for key in nums.keys(): 
  print(key) 
  print("This is a view object: ", nums.keys()) 
  print("This is a list: ", list(nums.keys())) 
  print("\n") 

for value in nums.values(): 
  print(value) 
  print("This is a view object: ", nums.values ())
  print ("This is a list: ", list(nums.values()))
#
"""
1 one
This is a view object:  dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
This is a list:  [(1, 'one'), (2, 'two'), (3, 'three')]


2 two
This is a view object:  dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
This is a list:  [(1, 'one'), (2, 'two'), (3, 'three')]


3 three
This is a view object:  dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
This is a list:  [(1, 'one'), (2, 'two'), (3, 'three')]


1
This is a view object:  dict_keys([1, 2, 3])
This is a list:  [1, 2, 3]


2
This is a view object:  dict_keys([1, 2, 3])
This is a list:  [1, 2, 3]


3
This is a view object:  dict_keys([1, 2, 3])
This is a list:  [1, 2, 3]


one
This is a view object:  dict_values(['one', 'two', 'three'])
This is a list:  ['one', 'two', 'three']
two
This is a view object:  dict_values(['one', 'two', 'three'])
This is a list:  ['one', 'two', 'three']
three
This is a view object:  dict_values(['one', 'two', 'three'])
This is a list:  ['one', 'two', 'three']
"""

# Example:
books = { "Life of Pi": "Adventure Fiction", 
         "The Three Musketeers": "Historical Adventure", 
         "Watchmen": "Comics", 
         "Bird Box": "Horror", 
         "Harry Potter":"Fantasy Fiction", 
         "Good Omens": "Comedy" 
        }
book = input()

if book not in books: 
  print("Not found") 
else: 
  print(books[book])
#   



