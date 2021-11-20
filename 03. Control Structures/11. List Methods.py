numbers = [2, 3, 7, 1, 98, 67]
letters = ['a', 's', 'z', 'e', 'r', 'u']

val = min(numbers)    # minimum value in the list of 'numbers'
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]    # you can do this with strings
val = numbers[:3]
val = numbers[4:]
print(val)

numbers[4] = 40       # the fourth index is 40

numbers.append(49)    # to add number, '49' as a string
numbers.append(59)
numbers.insert(3, 79) # to add '79' instead of the third index
numbers.insert(-1,52) # to add '52' instead of the last index

numbers.pop()         # to delete integer which added with append
numbers.pop(0)        # to delete the zeroth index
numbers.pop(-1)       # to delete str/int in the end
numbers.remove(59)
print(numbers)

numbers.sort()
numbers.reverse()

letters.sort()          # to sort 'letters' list as numeric size/ordinal
letters.reverse()       # to reverse


print(numbers)
print(letters)

print(len(numbers))      # len --> indicates the number of elements
print(len(letters))

print(numbers.count(10))    # how many '7' in 'numbers' by calling 'count' method
print(letters.count('a'))   # how many 'a'

numbers.clear()             # to clear all the elements in 'numbers' []
print(numbers)

numbers.remove(7)           # to write the character (not index) what you want to remove with remove method
print(numbers)


