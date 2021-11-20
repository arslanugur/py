# Bubble Sort is used to sort a list of elements, by comparing two adjacent elements and swapping them, if they are not in order.
def bubble_sort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for j in range(passnum):
            if nlist[j]>nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]

nlist = [14,46,43,27,57,41,45,21,70]
bubble_sort(nlist)
print(nlist)

# output: [14, 21, 27, 41, 43, 45, 46, 57, 70]

# Bubble Sort is used to sort a list of elements, by comparing two adjacent elements and swapping them, if they are not in order


# Easier example:
def bubble_sort(list):
    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list




# Example:
myList = [8,4,1,3,2,6]
count = 0
for i in range(len(myList)-1):
 for t in range(len(myList)-1):
         if myList[t]>myList[t+1]:
             myList[t],myList[t+1] = myList[t+1],myList[t]
             count += 1
print(myList,count)


# Example:
import random
list_1 = []

while len(list_1) < 10:
    x = random.randint(1, 10)
    if x not in list_1:
        list_1.append(x)

print("starting list")
print(list_1)

for i in range(len(list_1)):
    for x in range(1, len(list_1)-i):
        if list_1[x] < list_1[x-1]:
            list_1[x], list_1[x-1] = list_1[x-1], list_1[x]

print('done')
print(list_1)

# Output:
# starting list: [5, 2, 3, 4, 9, 6, 10, 8, 1, 7]
# done: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Example:
from random import randint
 
def bubble_sort(a):
    f = lambda x:x if x>=0 else None
    sort = False
    while not sort:
        sort = True
        for i, n in enumerate(a):
            if i<len(a)-1 and n>a[i+1]:
                a[i:i+2] = a[i+1:f(i-1):-1]
                sort = False
    return a
    
a = [randint(1,20) for elem in range(8)]
print (a)
a = bubble_sort(a)
print (a)

# output:
# [1, 10, 6, 18, 19, 12, 9, 3]
# [1, 3, 6, 9, 10, 12, 18, 19]


# Example:
#!/usr/bin/python3
import random

# You may change the default:
array_len = 6

# Acquire random numbers
def create_random_array():
  print("Acquire", array_len, "random numbers.")
  arr = []
  for i in range(array_len):
    arr.append(random.randint(0, 50))

  return arr

# This function bubble sorts the given list
def sort(arr):
  size = len(arr)
  for i in range(1, size):
    for j in range(i, size):
      if arr[i - 1] > arr[j]:
        # Swap the items
        arr[i-1], arr[j] = arr[j], arr[i-1]

  # Thats it
  return arr

# These are random unsorted numbers
ls = create_random_array()
print ("Unsorted list:\n" ,ls)

# SORTING THE LIST...
ls = sort(ls)
print("Sorted list:\n", ls)

# output:
# Acquire 6 random numbers.
# Unsorted list:
# [28, 32, 32, 45, 18, 33]
# Sorted list:
# [18, 28, 32, 32, 33, 45]


# Example:
n=[int(x) for x in input("enter elements").split()];i=0
for k in range(len(n)+1):
    for j in range(1,len(n)):
        if(n[i]>n[j]):
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
        i=i+1
    i=0
print(n)
#66 87 98 33 --> [33, 66, 87, 98]


# Example:
def bubble_sort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        a=0
        for j in range(passnum):
            if nlist[j]>nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                a=a+1
        if a==0:
                return
#optimize by reducing it when there is no change in if condition
nlist = [14,46,43,27,57,41,45,21,70]
bubble_sort(nlist)
print(nlist)

# [14, 21, 27, 41, 43, 45, 46, 57, 70]

# Example:
def bubble_sort(nlist):
    timessort = {'sorts':0, 'swaps':0}
    for passnum in range(len(nlist)-1,0,-1):
        timessort['sorts'] += 1
        for j in range(passnum):
            if nlist[j]>nlist[j+1]:
                timessort['swaps'] += 1
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
    return timessort 

nlist = [71,46,43,27,57,41,45,21,70]
t = bubble_sort(nlist)
print(nlist)

print(t)
# [21, 27, 41, 43, 45, 46, 57, 70, 71]
# {'sorts': 8, 'swaps': 22}


# Example:
def bubsrt(ul):
    i = 0
    corr = 0
    while i < (len(ul) - 1):
        if ul[i] > ul[i+1]:
            ul[i], ul[i+1] = ul[i+1],ul[i]
            corr +=1
        i+=1
    if corr > 0:
        bubsrt(ul)
    return ul

print(bubsrt([10,3,1,20,5]))
# [1, 3, 5, 10, 20]









