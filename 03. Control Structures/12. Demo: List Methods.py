names = ['Lincoln', 'Franklin', 'Roosevelt', 'Nixon']
years = [1933, 1969, 1764, 1861]


names.append('Kennedy')          # add to the end of the list --> 'Kennedy'
names.insert(0, 'Washington')    # add to the beginning of the list --> 'Washington'
names.insert(len(names), 'Bush') # append gibi değil, index istiyor. ama append gibi sona ekleme de yapılabilir
print(names) 

names.remove('Franklin')         # delete 'Franklin' from the list
names.pop()                      # delete the last element of the list, if no index in the method
print(names)

index = names.index('Roosevelt') # indicate the index
print(index)

names.pop(index)                  # delete the element according to index
print(names)

result = 'Washington' in names    # is 'Washington' an element in names list --> gives True False
# result = names.index('Washington')  # another way --> # if index number is not -1 --> True
print(result)

names.reverse()                   # to reverse the elements of the list
print(names)

names.sort()                      # to sort the list elements alphabetically
print(names)

years.sort()                      # sort by numeric size the list 'years'
print(years)

str = 'Obama, Trump'              # turn series of characters into a list --> str = 'Obama, Trump'
result = str.split(',')
print(result)

min = min(years)                  # the smallest element of the list 'years'
max = max(years)
print(min, max)

result = years.count(1764)        # how many the value '1764' in the list 'years'
print(result)


years.clear()                     # clear all the elements from the list 'years'
print(years)


# to store in a list --> three presidents information from user via input
presidents = []                   # to define an empty list
president = input('presidents: ') # input from users, and then assign to a variable named 'president'
presidents.append(president)      # to append given information on the list
print(president)                  # to print presidents via user input
# print(presidents)               # if we write this way, it gives information as a list

# if we write/copy above three times, it would be amateurish,  because using loop(döngü) is better than writing/copying three times
president = input('presidents: ') 
presidents.append(president)
print(presidents)

# after writing three presidents, it makes it a list



