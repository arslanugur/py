SET                 DICTIONARY          LIST          LIST CHEATSHEET
------------------------------------------------------------------------------------------
add()               copy()              append()      ⬛ ⬛   .append(⬛)      --> ⬛ ⬛ ⬛ 
clear()             clear()             copy()        ⬛ ⬛ ⬛.copy()          --> ⬛ ⬛ ⬛
pop()               fromkeys()          count()       ⬛ ⬛ 🔴.count(⬛)       --> 2
union()             items()             insert()      ⬛ ⬛   .insert(1,🔴)    --> ⬛ 🔴 ⬛
issuperset()        get()               reverse()     ⬛ ⬛ 🔴.reverse()       --> 🔴 ⬛ ⬛
issubset()          keys()              remove()      🔴 🔴 ⬛.remove(⬛)      --> 🔴 🔴 
intersection()      pop()               sort()
difference()        values()            pop()         🔴 🔴 ⬛.pop(1)          --> 🔴 ⬛
isdisjoint()        update()            extend() 
setdiscard()        setdefault()        index()       ⬛ 🔴 ⬛.index(🔴)       --> 1
copy()              popitem()           clear()       ⬛ ⬛ 🔴.clear()         --> 



# Py Set Methods
add()                   # adds an element to the set
clear()                 # removes all the elements from the set 
copy()                  # returns a copy of the set
difference()            # returns a set containing the difference between two or more sets
discard()               # remove the specified item
intersection()          # returns a set, that is the intersection of two or more sets
isdisjoint()            # returns whether two sets have a intersection or not
pop()                   # removes the specified element
remove()                # removes he specified element
symmetric_difference()  # returns a set with the symmetric differences of two sets
union()                 # returns a set containing the union of sets 



